import requests
from datetime import datetime

RTX_3080 = "https://api.nvidia.partners/edge/product/search?page=1&limit=9&locale=en-gb&gpu=RTX%203080"
RTX_3090 = "https://api.nvidia.partners/edge/product/search?page=1&limit=9&locale=en-gb&gpu=RTX%203090"
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/814490986490232892/fhWhz412kduLd2bh8IUTLUAPfXdT6fBdKUe5lGJULQ********************"
SLEEP_SECONDS = 0
purchase_link_3080 = None
purchase_link_3090 = None


def link_30x0(url):
    # check 30x0
    try:
        response = requests.get(url)
        response_30x0 = response.json()
        purchase_30x0 = response_30x0['searchedProducts']['featuredProduct']['retailers'][0]['purchaseLink']
        # print(purchase_30x0)
        return purchase_30x0
    except:
        return "Error"


def send_message(message):
    data = {"content": message}
    response = requests.post(DISCORD_WEBHOOK, json=data)
    # print("Discord message sent")


def check():
    global purchase_link_3080
    global purchase_link_3090
    new_purchase_link_3080 = link_30x0(RTX_3080)
    new_purchase_link_3090 = link_30x0(RTX_3090)

    if (new_purchase_link_3080 != "Error"):
        if (purchase_link_3080 != new_purchase_link_3080):
            print("3080 - {}".format(new_purchase_link_3080))
            send_message("3080 - {}".format(new_purchase_link_3080))
            purchase_link_3080 = new_purchase_link_3080
    else:
        print("CANNOT GET 3080")
        
    if (new_purchase_link_3090 != "Error"):
        if (purchase_link_3090 != new_purchase_link_3090):
            print("3090 - {}".format(new_purchase_link_3090))
            send_message("3090 - {}".format(new_purchase_link_3090))
            purchase_link_3090 = new_purchase_link_3090
    else:
        print("CANNOT GET 3090")
    

while True:
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    check()
    print("")
    time.sleep(SLEEP_SECONDS)
