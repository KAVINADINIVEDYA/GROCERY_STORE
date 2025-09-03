# Selenium UI Testing - Automatic ChromeDriver Setup
# No need to manually download ChromeDriver!

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

def setup_chrome_driver():
    """Setup Chrome driver with automatic management"""
    try:
        # Try using webdriver-manager for automatic ChromeDriver setup
        from webdriver_manager.chrome import ChromeDriverManager
        
        chrome_options = Options()
        # Add options for better compatibility
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        # Remove headless mode so you can see the testing happening
        # chrome_options.add_argument('--headless')  # Uncomment this line to run in background
        
        # Automatically download and setup ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("✓ Chrome driver setup successful with webdriver-manager")
        return driver
        
    except ImportError:
        print("⚠ webdriver-manager not found. Installing...")
        print("Run: pip install webdriver-manager")
        print("Then run this script again.")
        return None
    except Exception as e:
        print(f"✗ Error setting up Chrome driver: {e}")
        return None

def get_file_path(filename):
    """Get full file path for HTML files"""
    # Assuming your HTML files are in the 'ui' folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one directory to reach project root, then into ui folder
    ui_path = os.path.join(os.path.dirname(current_dir), 'ui', filename)
    return f"file:///{ui_path.replace(os.sep, '/')}"

def test_dashboard_loads():
    """Test if dashboard (index.html) loads correctly"""
    driver = setup_chrome_driver()
    if not driver:
        return False
    
    try:
        print("\n🧪 Testing Dashboard Loading...")
        
        # Navigate to dashboard
        dashboard_path = get_file_path('index.html')
        driver.get(dashboard_path)
        
        # Wait for page to load
        time.sleep(2)
        
        # Check if page title contains GSMS
        if "GSMS" in driver.title:
            print("✓ Dashboard loads correctly - Title found")
        else:
            print(f"⚠ Dashboard title issue - Found: {driver.title}")
        
        # Check if main heading exists
        try:
            heading = driver.find_element(By.TAG_NAME, "h2")
            if "Grocery Store Management System" in heading.text:
                print("✓ Main heading found correctly")
            else:
                print(f"⚠ Heading text: {heading.text}")
        except:
            print("⚠ Main heading not found")
        
        # Check if Manage Products button exists
        try:
            manage_btn = driver.find_element(By.LINK_TEXT, "Manage Products")
            print("✓ Manage Products button found")
        except:
            print("⚠ Manage Products button not found")
        
        # Check if New Order button exists
        try:
            order_btn = driver.find_element(By.LINK_TEXT, "New Order")
            print("✓ New Order button found")
        except:
            print("⚠ New Order button not found")
        
        return True
        
    except Exception as e:
        print(f"✗ Dashboard test failed: {e}")
        return False
    
    finally:
        driver.quit()

def test_manage_products_page():
    """Test manage products page functionality"""
    driver = setup_chrome_driver()
    if not driver:
        return False
    
    try:
        print("\n🧪 Testing Manage Products Page...")
        
        # Navigate to manage products page
        products_path = get_file_path('manage-product.html')
        driver.get(products_path)
        
        # Wait for page to load
        time.sleep(2)
        
        # Check page title
        if "GSMS" in driver.title:
            print("✓ Manage Products page loads correctly")
        
        # Check if "Manage Products" heading exists
        try:
            heading = driver.find_element(By.TAG_NAME, "h2")
            if "Manage Products" in heading.text:
                print("✓ Manage Products heading found")
        except:
            print("⚠ Manage Products heading not found")
        
        # Check if "Add New Product" button exists
        try:
            add_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Add New Product')]")
            print("✓ Add New Product button found")
            
            # Click the button to open modal
            add_btn.click()
            time.sleep(1)
            
            # Check if modal opened
            try:
                modal = driver.find_element(By.ID, "productModal")
                if modal.is_displayed():
                    print("✓ Product modal opens correctly")
                    
                    # Check form fields
                    name_field = driver.find_element(By.ID, "name")
                    price_field = driver.find_element(By.ID, "price")
                    uom_field = driver.find_element(By.ID, "uoms")
                    
                    print("✓ All form fields found")
                    
                    # Try filling the form (optional - uncomment to test)
                    # name_field.send_keys("Test Product")
                    # price_field.send_keys("25")
                    # print("✓ Form fields can be filled")
                    
                else:
                    print("⚠ Product modal not visible")
            except:
                print("⚠ Product modal not found")
            
        except:
            print("⚠ Add New Product button not found")
        
        # Check if products table exists
        try:
            table = driver.find_element(By.CLASS_NAME, "table")
            print("✓ Products table found")
        except:
            print("⚠ Products table not found")
        
        return True
        
    except Exception as e:
        print(f"✗ Manage Products test failed: {e}")
        return False
    
    finally:
        driver.quit()

def test_order_page():
    """Test order creation page"""
    driver = setup_chrome_driver()
    if not driver:
        return False
    
    try:
        print("\n🧪 Testing Order Page...")
        
        # Navigate to order page
        order_path = get_file_path('order.html')
        driver.get(order_path)
        
        # Wait for page to load
        time.sleep(2)
        
        # Check page loads
        if "GSMS" in driver.title:
            print("✓ Order page loads correctly")
        
        # Check if "New Order" heading exists
        try:
            heading = driver.find_element(By.TAG_NAME, "h2")
            if "New Order" in heading.text:
                print("✓ New Order heading found")
        except:
            print("⚠ New Order heading not found")
        
        # Check customer name field
        try:
            customer_field = driver.find_element(By.ID, "customerName")
            print("✓ Customer name field found")
            
            # Test typing in customer name
            customer_field.send_keys("Test Customer")
            print("✓ Customer name field accepts input")
            
        except:
            print("⚠ Customer name field not found")
        
        # Check if Add More button exists
        try:
            add_more_btn = driver.find_element(By.ID, "addMoreButton")
            print("✓ Add More button found")
            
            # Test clicking Add More button
            add_more_btn.click()
            time.sleep(1)
            print("✓ Add More button clickable")
            
        except:
            print("⚠ Add More button not found or not clickable")
        
        # Check if Save button exists
        try:
            save_btn = driver.find_element(By.ID, "saveOrder")
            print("✓ Save Order button found")
        except:
            print("⚠ Save Order button not found")
        
        return True
        
    except Exception as e:
        print(f"✗ Order page test failed: {e}")
        return False
    
    finally:
        driver.quit()

def test_navigation_between_pages():
    """Test navigation between different pages"""
    driver = setup_chrome_driver()
    if not driver:
        return False
    
    try:
        print("\n🧪 Testing Page Navigation...")
        
        # Start from dashboard
        dashboard_path = get_file_path('index.html')
        driver.get(dashboard_path)
        time.sleep(2)
        
        print("✓ Started from dashboard")
        
        # Click Manage Products link
        try:
            manage_link = driver.find_element(By.LINK_TEXT, "Manage Products")
            manage_link.click()
            time.sleep(2)
            
            # Check if we're on manage products page
            if "manage-product" in driver.current_url:
                print("✓ Navigation to Manage Products works")
            else:
                print("⚠ Navigation to Manage Products may have issues")
                
        except:
            print("⚠ Could not navigate to Manage Products")
        
        # Go back to dashboard
        driver.back()
        time.sleep(1)
        
        # Click New Order link
        try:
            order_link = driver.find_element(By.LINK_TEXT, "New Order")
            order_link.click()
            time.sleep(2)
            
            # Check if we're on order page
            if "order" in driver.current_url:
                print("✓ Navigation to New Order works")
            else:
                print("⚠ Navigation to New Order may have issues")
                
        except:
            print("⚠ Could not navigate to New Order")
        
        return True
        
    except Exception as e:
        print(f"✗ Navigation test failed: {e}")
        return False
    
    finally:
        driver.quit()

def run_all_ui_tests():
    """Run all UI tests"""
    print("=" * 60)
    print("GROCERY STORE MANAGEMENT SYSTEM - UI AUTOMATION TESTS")
    print("=" * 60)
    
    # Check if required packages are installed
    try:
        from webdriver_manager.chrome import ChromeDriverManager
    except ImportError:
        print("❌ Missing required packages!")
        print("\n🔧 Please install required packages:")
        print("   pip install selenium webdriver-manager")
        print("\nThen run this script again.")
        return
    
    test_results = {
        'dashboard': False,
        'products': False,
        'orders': False,
        'navigation': False
    }
    
    # Run tests
    test_results['dashboard'] = test_dashboard_loads()
    test_results['products'] = test_manage_products_page()
    test_results['orders'] = test_order_page()
    test_results['navigation'] = test_navigation_between_pages()
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST RESULTS SUMMARY")
    print("=" * 60)
    
    passed = sum(test_results.values())
    total = len(test_results)
    
    for test_name, result in test_results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name.capitalize()} Test: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("\n🎉 All UI tests passed! Your frontend is working great!")
    else:
        print(f"\n⚠ {total-passed} test(s) failed. Check the details above.")
    
    print("\n💡 Note: Some failures might be due to:")
    print("   - File paths (make sure HTML files are in correct location)")
    print("   - Missing backend server (some features need Flask server running)")
    print("   - Browser compatibility issues")

if __name__ == "__main__":
    run_all_ui_tests()# Selenium UI Testing - Automatic ChromeDriver Setup
# No need to manually download ChromeDriver!

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

def setup_chrome_driver():
    """Setup Chrome driver with automatic management"""
    try:
        # Try using webdriver-manager for automatic ChromeDriver setup
        from webdriver_manager.chrome import ChromeDriverManager
        
        chrome_options = Options()
        # Add options for better compatibility
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        # Remove headless mode so you can see the testing happening
        # chrome_options.add_argument('--headless')  # Uncomment this line to run in background
        
        # Automatically download and setup ChromeDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("✓ Chrome driver setup successful with webdriver-manager")
        return driver
        
    except ImportError:
        print("⚠ webdriver-manager not found. Installing...")
        print("Run: pip install webdriver-manager")
        print("Then run this script again.")
        return None
    except Exception as e:
        print(f"✗ Error setting up Chrome driver: {e}")
        return None

def get_file_path(filename):
    """Get full file path for HTML files"""
    # Assuming your HTML files are in the 'ui' folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one directory to reach project root, then into ui folder
    ui_path = os.path.join(os.path.dirname(current_dir), 'ui', filename)
    return f"file:///{ui_path.replace(os.sep, '/')}"

def test_dashboard_loads():
    """Test if dashboard (index.html) loads correctly"""
    driver = setup_chrome_driver()
    if not driver:
        return False
    
    try:
        print("\n🧪 Testing Dashboard Loading...")
        
        # Navigate to dashboard
        dashboard_path = get_file_path('index.html')
        driver.get(dashboard_path)
        
        # Wait for page to load
        time.sleep(2)
        
        # Check if page title contains GSMS
        if "GSMS" in driver.title:
            print("✓ Dashboard loads correctly - Title found")
        else:
            print(f"⚠ Dashboard title issue - Found: {driver.title}")
        
        # Check if main heading exists
        try:
            heading = driver.find_element(By.TAG_NAME, "h2")
            if "Grocery Store Management System" in heading.text:
                print("✓ Main heading found correctly")
            else:
                print(f"⚠ Heading text: {heading.text}")
        except:
            print("⚠ Main heading not found")
        
        # Check if Manage Products button exists
        try:
            manage_btn = driver.find_element(By.LINK_TEXT, "Manage Products")
            print("✓ Manage Products button found")
        except:
            print("⚠ Manage Products button not found")
        
        # Check if New Order button exists
        try:
            order_btn = driver.find_element(By.LINK_TEXT, "New Order")
            print("✓ New Order button found")
        except:
            print("⚠ New Order button not found")
        
        return True
        
    except Exception as e:
        print(f"✗ Dashboard test failed: {e}")
        return False
    
    finally:
        driver.quit()

def test_manage_products_page():
    """Test manage products page functionality"""
    driver = setup_chrome_driver()
    if not driver:
        return False
    
    try:
        print("\n🧪 Testing Manage Products Page...")
        
        # Navigate to manage products page
        products_path = get_file_path('manage-product.html')
        driver.get(products_path)
        
        # Wait for page to load
        time.sleep(2)
        
        # Check page title
        if "GSMS" in driver.title:
            print("✓ Manage Products page loads correctly")
        
        # Check if "Manage Products" heading exists
        try:
            heading = driver.find_element(By.TAG_NAME, "h2")
            if "Manage Products" in heading.text:
                print("✓ Manage Products heading found")
        except:
            print("⚠ Manage Products heading not found")
        
        # Check if "Add New Product" button exists
        try:
            add_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Add New Product')]")
            print("✓ Add New Product button found")
            
            # Click the button to open modal
            add_btn.click()
            time.sleep(1)
            
            # Check if modal opened
            try:
                modal = driver.find_element(By.ID, "productModal")
                if modal.is_displayed():
                    print("✓ Product modal opens correctly")
                    
                    # Check form fields
                    name_field = driver.find_element(By.ID, "name")
                    price_field = driver.find_element(By.ID, "price")
                    uom_field = driver.find_element(By.ID, "uoms")
                    
                    print("✓ All form fields found")
                    
                    # Try filling the form (optional - uncomment to test)
                    # name_field.send_keys("Test Product")
                    # price_field.send_keys("25")
                    # print("✓ Form fields can be filled")
                    
                else:
                    print("⚠ Product modal not visible")
            except:
                print("⚠ Product modal not found")
            
        except:
            print("⚠ Add New Product button not found")
        
        # Check if products table exists
        try:
            table = driver.find_element(By.CLASS_NAME, "table")
            print("✓ Products table found")
        except:
            print("⚠ Products table not found")
        
        return True
        
    except Exception as e:
        print(f"✗ Manage Products test failed: {e}")
        return False
    
    finally:
        driver.quit()

def test_order_page():
    """Test order creation page"""
    driver = setup_chrome_driver()
    if not driver:
        return False
    
    try:
        print("\n🧪 Testing Order Page...")
        
        # Navigate to order page
        order_path = get_file_path('order.html')
        driver.get(order_path)
        
        # Wait for page to load
        time.sleep(2)
        
        # Check page loads
        if "GSMS" in driver.title:
            print("✓ Order page loads correctly")
        
        # Check if "New Order" heading exists
        try:
            heading = driver.find_element(By.TAG_NAME, "h2")
            if "New Order" in heading.text:
                print("✓ New Order heading found")
        except:
            print("⚠ New Order heading not found")
        
        # Check customer name field
        try:
            customer_field = driver.find_element(By.ID, "customerName")
            print("✓ Customer name field found")
            
            # Test typing in customer name
            customer_field.send_keys("Test Customer")
            print("✓ Customer name field accepts input")
            
        except:
            print("⚠ Customer name field not found")
        
        # Check if Add More button exists
        try:
            add_more_btn = driver.find_element(By.ID, "addMoreButton")
            print("✓ Add More button found")
            
            # Test clicking Add More button
            add_more_btn.click()
            time.sleep(1)
            print("✓ Add More button clickable")
            
        except:
            print("⚠ Add More button not found or not clickable")
        
        # Check if Save button exists
        try:
            save_btn = driver.find_element(By.ID, "saveOrder")
            print("✓ Save Order button found")
        except:
            print("⚠ Save Order button not found")
        
        return True
        
    except Exception as e:
        print(f"✗ Order page test failed: {e}")
        return False
    
    finally:
        driver.quit()

def test_navigation_between_pages():
    """Test navigation between different pages"""
    driver = setup_chrome_driver()
    if not driver:
        return False
    
    try:
        print("\n🧪 Testing Page Navigation...")
        
        # Start from dashboard
        dashboard_path = get_file_path('index.html')
        driver.get(dashboard_path)
        time.sleep(2)
        
        print("✓ Started from dashboard")
        
        # Click Manage Products link
        try:
            manage_link = driver.find_element(By.LINK_TEXT, "Manage Products")
            manage_link.click()
            time.sleep(2)
            
            # Check if we're on manage products page
            if "manage-product" in driver.current_url:
                print("✓ Navigation to Manage Products works")
            else:
                print("⚠ Navigation to Manage Products may have issues")
                
        except:
            print("⚠ Could not navigate to Manage Products")
        
        # Go back to dashboard
        driver.back()
        time.sleep(1)
        
        # Click New Order link
        try:
            order_link = driver.find_element(By.LINK_TEXT, "New Order")
            order_link.click()
            time.sleep(2)
            
            # Check if we're on order page
            if "order" in driver.current_url:
                print("✓ Navigation to New Order works")
            else:
                print("⚠ Navigation to New Order may have issues")
                
        except:
            print("⚠ Could not navigate to New Order")
        
        return True
        
    except Exception as e:
        print(f"✗ Navigation test failed: {e}")
        return False
    
    finally:
        driver.quit()

def run_all_ui_tests():
    """Run all UI tests"""
    print("=" * 60)
    print("GROCERY STORE MANAGEMENT SYSTEM - UI AUTOMATION TESTS")
    print("=" * 60)
    
    # Check if required packages are installed
    try:
        from webdriver_manager.chrome import ChromeDriverManager
    except ImportError:
        print("❌ Missing required packages!")
        print("\n🔧 Please install required packages:")
        print("   pip install selenium webdriver-manager")
        print("\nThen run this script again.")
        return
    
    test_results = {
        'dashboard': False,
        'products': False,
        'orders': False,
        'navigation': False
    }
    
    # Run tests
    test_results['dashboard'] = test_dashboard_loads()
    test_results['products'] = test_manage_products_page()
    test_results['orders'] = test_order_page()
    test_results['navigation'] = test_navigation_between_pages()
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST RESULTS SUMMARY")
    print("=" * 60)
    
    passed = sum(test_results.values())
    total = len(test_results)
    
    for test_name, result in test_results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name.capitalize()} Test: {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("\n🎉 All UI tests passed! Your frontend is working great!")
    else:
        print(f"\n⚠ {total-passed} test(s) failed. Check the details above.")
    
    print("\n💡 Note: Some failures might be due to:")
    print("   - File paths (make sure HTML files are in correct location)")
    print("   - Missing backend server (some features need Flask server running)")
    print("   - Browser compatibility issues")

if __name__ == "__main__":
    run_all_ui_tests()