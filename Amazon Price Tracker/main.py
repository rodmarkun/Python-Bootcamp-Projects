import requests
from bs4 import BeautifulSoup
import lxml

PRODUCT = "https://www.amazon.es/L%C3%A1mpara-Escritorio-Protecci%C3%B3n-Polarizada-Lampara/dp/B09FXG4WX6/?_encoding=UTF8&pd_rd_w=eDK3g&content-id=amzn1.sym.5f6951c0-9d61-4e03-b39a-a5647d9ae575&pf_rd_p=5f6951c0-9d61-4e03-b39a-a5647d9ae575&pf_rd_r=4971MW9M2GA40VN2HQ97&pd_rd_wg=gzPJT&pd_rd_r=d031f086-bf88-474f-ae1f-7aef0fdd6d92&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
TARGET_PRICE = 50.0

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "accept-language" : "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
}

def main():
    response = requests.get(url=PRODUCT, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    price_tag = soup.find(name="span", class_="a-offscreen")
    price_numbers = price_tag.getText().strip('€').split(',')

    product_price = float(price_numbers[0]) + float(price_numbers[1])/100
    print(f"Current product price is: {product_price}.")
    if product_price < TARGET_PRICE:
        print(f"PRODUCT PRICE IS LOWER THAN TARGET PRICE {TARGET_PRICE}, BUY NOW!")
    else:
        print(f"Product still above target price {TARGET_PRICE}. Be patient!")

if __name__ == "__main__":
    main()