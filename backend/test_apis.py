import requests
import json

# Test if server is running
def test_server_running():
    try:
        response = requests.get('http://localhost:5000/getProducts')
        if response.status_code == 200:
            print("✓ Server is running")
            return True
        else:
            print("✗ Server not responding")
            return False
    except:
        print("✗ Cannot connect to server")
        return False

# Test get products API
def test_get_products():
    try:
        response = requests.get('http://localhost:5000/getProducts')
        data = response.json()
        
        if len(data) > 0:
            print(f"✓ Get Products API working - Found {len(data)} products")
        else:
            print("⚠ Get Products API working but no products found")
            
        return True
    except:
        print("✗ Get Products API failed")
        return False

# Test get UOM API
def test_get_uom():
    try:
        response = requests.get('http://localhost:5000/getUOM')
        data = response.json()
        
        if len(data) > 0:
            print(f"✓ Get UOM API working - Found {len(data)} units")
        else:
            print("⚠ Get UOM API working but no units found")
            
        return True
    except:
        print("✗ Get UOM API failed")
        return False

# Run all tests
def run_all_tests():
    print("Starting Automated Tests...")
    print("-" * 30)
    
    if test_server_running():
        test_get_products()
        test_get_uom()
    
    print("-" * 30)
    print("Tests completed!")

# Run the tests
if __name__ == "__main__":
    run_all_tests()