export function sortItems(list, type){
    if (!Array.isArray(list)) return list;
    if(type === "priceAsc") return [...list].sort((a,b)=>a.price-b.price);
    if(type === "priceDesc") return [...list].sort((a,b)=>b.price-a.price);
    if(type === "qtyAsc") return [...list].sort((a,b)=>a.quantity-b.quantity);
    if(type === "qtyDesc") return [...list].sort((a,b)=>b.quantity-a.quantity);
    return list;
}
