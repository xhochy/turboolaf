#!/usr/bin/env python3

import json
import time
import smtplib

INVOICE_WIDTH = 40

print("Welcome to TurboOlaf!")

invoice = json.load(open("invoice.json"))
# set the quantity of all products to 0
print(invoice)
for code, product in invoice.items():
    product["quantity"] = 0

while True:
    product_code = input("Product code:")

    # end if an empty product code was given
    if not product_code:
        break
    else:
        try:
            invoice[product_code]["quantity"] += 1
        except:
            print("No such product!")

invoice_string = ""
invoice_string += "*" * INVOICE_WIDTH + "\n"
invoice_string +="K1 Getränkeverkauf".center(INVOICE_WIDTH) + "\n"
invoice_string += time.strftime("%d %b %Y %H:%M:%S").center(INVOICE_WIDTH) + "\n"
invoice_string += "*" * INVOICE_WIDTH + "\n\n"

total_price = 0
for code, product in invoice.items():
    if product["quantity"] > 0:
        billed_price = product["price"] * product["quantity"]
        total_price += billed_price

        billing_string = str(product["price"]).rjust(5) + \
                str(" x " + str(product["quantity"])).rjust(6) + \
                " = " + \
                str(billed_price).rjust(6)

        name_string = product["name"].ljust(INVOICE_WIDTH - len(billing_string))
        invoice_string += name_string + billing_string + "\n"

invoice_string += "-" * INVOICE_WIDTH + "\n"
invoice_string += "Total:" + str(total_price).rjust(INVOICE_WIDTH - 6) + "\n"

print(invoice_string);

