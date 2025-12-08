# gul_andam_backend/test_db.py
from gul_andam_backend import InventoryDB

def quick_test():
    db = InventoryDB(":memory:")
    pid = db.add_product("QAItem", "Test", 5, 9.99)
    assert db.fetch_by_id(pid)[1] == "QAItem"
    assert db.update_product(pid, "QAItem", "Test", 10, 19.99)
    assert db.delete_product(pid)
    assert db.fetch_by_id(pid) is None
    print("Quick DB Test Passed (Gul Andam Day 1)")
    db.close()

if __name__ == "__main__":
    quick_test()
