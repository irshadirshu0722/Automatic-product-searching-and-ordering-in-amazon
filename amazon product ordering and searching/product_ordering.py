from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import time
cchrome_driver = Service(
    r"C:\development\msedgedriver.exe"
)
driver = webdriver.Edge(service=cchrome_driver)
mobile_number = input("enter your login mobile number")
login_password = input("enter your login password")
product_name = input("enter your product you want to search")
pproduct_range = input("enter the product price range").split(" ")

driver.get("https://www.amazon.in/")
# driver.get("https://www.amazon.in/ref=nav_ya_signin")
# driver.get("https://www.amazon.in/Logitech-MK240-NANO-Mouse-Keyboard/dp/B01N4EV2TL/ref=sr_1_3?crid=3FKNFJKL18YB1&keywords=keyboard%2Band%2Bmouse%2Bwireless&qid=1691557076&refinements=p_n_is_cod_eligible%3A4931671031&rnid=4931670031&sprefix=keyboard%2Band%2Bmouse%2Bwireless%2Caps%2C205&sr=8-3&th=1")
driver.maximize_window()
def signin(number,password):

    #click the sign in button
    singin = driver.find_element(By.ID,"nav-link-accountList")
    singin.click()

    # fill email
    email = driver.find_element(By.NAME,'email')
    email.send_keys(mobile_number)
    #submit
    submit = driver.find_element(By.CLASS_NAME,"a-button-input")
    submit.click()
    #fill passowrd
    password = driver.find_element(By.NAME,"password")
    password.send_keys(login_password)

    submit = driver.find_element(By.ID,"signInSubmit")
    submit.click()
def search_item(product):
    search_bar = driver.find_element(By.NAME,"field-keywords")
    search_bar.send_keys(product)
    search_bar.send_keys(Keys.ENTER)
def check_price(prices,target,minimum):
    for price_span in prices:
        price ="".join(price_span.text.split(','))
        print(price)
        if int(price) <target and int(price)>minimum:
            return price_span
    print("return")
    return None

def check_availablitiy(is_available):
    if is_available:
        is_available.click()
    else:
        print("product not available below your target")
    time.sleep(5)



def switch_window_to():
    window_handles = driver.window_handles

    # Switch to the original window
    driver.switch_to.window(window_handles[-1])

def move_cursor_to_element_with_xpath(driver, xpath_expression):
    # Create an Actions object
    actions = webdriver.ActionChains(driver)

    # Move the mouse pointer to the element
    actions.move_to_element(driver.find_element(by=By.XPATH, value=xpath_expression)).perform()

def click_delivery_adress():
    button = driver.find_element(By.ID,"shipToThisAddressButton")
    button.click()
    time.sleep(10)
def click_special_option():
    button = driver.find_element(By.XPATH,"//*[@id='shippingOptionFormId']/div/div[3]/div/span/span")
    button.click()
    time.sleep(10)
def choose_payment_option():
    delivery_addres = driver.find_element(By.ID,"shipaddress")
    delivery_addres_is_on = delivery_addres.get_attribute("class").split(" ")[1]
    if delivery_addres_is_on!="collapsed":
        click_delivery_adress()

    try:
        special_option = driver.find_element(By.ID,"special-delivery-options")
    except:
        pass
    else:
        special_option_is_on = special_option.get_attribute("class").split(" ")[1]
        if special_option_is_on != "collapsed":
            click_special_option()



def order_product():
    #click buynow

    buynow = driver.find_element(By.ID, "buy-now-button")
    buynow.click()

    time.sleep(5)
    choose_payment_option()

    # print("cash on delivery action starting")
    #choice cahs on delivery
    cod_radio_button = driver.find_elements(by=By.NAME, value="ppw-instrumentRowSelection")

    cod_radio_button[-1].click()
    time.sleep(1)
    # click use this payment option

    use_this_payment_option = driver.find_element(By.ID,"orderSummaryPrimaryActionBtn").find_element(By.TAG_NAME,"input")
    use_this_payment_option.click()

    time.sleep(20)

    #place order
    place_order= driver.find_element(By.NAME,"placeYourOrder1")
    place_order.click()
    # print("cash on delivery action ended")/


signin("7025359287","irshad1213")


search_item(product_name)
prudocts_price = driver.find_elements(By.CLASS_NAME,"a-price-whole")
is_available = check_price(prudocts_price,int(pproduct_range[1]),int(pproduct_range[0]))
check_availablitiy(is_available)

switch_window_to()
time.sleep(2)



order_product()
# move_cursor_to_element_with_xpath(driver, "//*[@id='acBadge_feature_div']/div/span[1]/span[1]/span[2]")

print("product ordered")
time.sleep(10)
driver.close()
driver.quit()

