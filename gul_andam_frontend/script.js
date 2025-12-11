const API = "http://127.0.0.1:5001";

async function fetchProducts(){
  const res = await fetch(API + "/products");
  const data = await res.json();
  renderProducts(data);
}

function renderProducts(items){
  const container = document.getElementById("products");
  if(!items || items.length === 0){
    container.innerHTML = "<p>No products yet.</p>";
    return;
  }
  container.innerHTML = "";
  items.forEach(it => {
    const el = document.createElement("div");
    el.className = "product";
    el.innerHTML = `
      <div class="left">
        <div>
          <strong>${escapeHtml(it.name)}</strong>
          <div class="badge">${escapeHtml(it.category)}</div>
        </div>
        <div>Qty: ${it.quantity} | ₹ ${it.price}</div>
      </div>
      <div class="right">
        <button data-action="edit" data-id="${it.id}">Edit</button>
        <button data-action="delete" data-id="${it.id}">Delete</button>
      </div>
    `;
    container.appendChild(el);
  });
}

function escapeHtml(s){
  return (s + "").replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

// Add product form
document.getElementById("addForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const form = e.target;
  const data = {
    name: form.name.value.trim(),
    category: form.category.value.trim(),
    quantity: Number(form.quantity.value),
    price: Number(form.price.value),
  };
  const res = await fetch(API + "/add", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify(data)
  });
  if(res.ok){
    form.reset();
    fetchProducts();
    alert("Product added");
  } else {
    const err = await res.json();
    alert("Error: " + JSON.stringify(err));
  }
});

// Delegation for edit/delete
document.getElementById("products").addEventListener("click", async (e) => {
  const btn = e.target.closest("button");
  if(!btn) return;
  const action = btn.dataset.action;
  const id = btn.dataset.id;
  if(action === "delete"){
    if(!confirm("Delete product?")) return;
    const res = await fetch(API + "/delete/" + id, { method: "DELETE" });
    if(res.ok) { fetchProducts(); alert("Deleted"); }
    else alert("Delete failed");
  } else if(action === "edit"){
    const name = prompt("New name?");
    if(name === null) return;
    const category = prompt("New category?");
    const qty = prompt("New quantity?");
    const price = prompt("New price?");
    const payload = { name, category, quantity: Number(qty), price: Number(price) };
    const res = await fetch(API + "/update/" + id, {
      method: "PUT",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify(payload)
    });
    if(res.ok){ fetchProducts(); alert("Updated"); }
    else alert("Update failed");
  }
});

// initial load
fetchProducts();
