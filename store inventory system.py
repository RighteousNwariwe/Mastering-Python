#code for a store inventory system
from datetime import datetime

products ={
    "1": {
        "name": "Test",
        "price": 1000.00,
        "stock": 10.0
    }

}

number_of_sales = 0
total_sales = 0.00
transactions = []
invoice_number = 1

def display_producs():
    print('ID\tName\tPrice')

    for product_id, product_info in products.items():
        print(f"{product_id}\t{product_info['name']}\t{product_info['price']}")

def display_inventory():
    print("-" * 27)
    print(f"Stock Report @ {datetime.now()}")
    print("-" * 27)
    print("ID   Name   Price      Qty")
    for product_id, product_info in products.items():
        print(f"{product_id}    {product_info['name']}   {product_info['price']:,.2f}   {product_info['stock']:.0f}")
    print("-" * 27)



print("Welcome to Wellness4All POS!")
while True:
    print()
    print(f"Number of Sales: {number_of_sales}")
    print(f"Total Sales: R{total_sales:.2f}")
    print()
    print("1. Add Product")
    print("2. Edit Product")
    print("3. Make a Sale")
    print("4. View Inventory")
    print("5. Exit")

    choice = input('Type the number of your choice: ')


    #adding a product
    if choice == "1":

        try:
            new_id = input("Enter id: ")
            if new_id in products:
                print("Product ID already exists. Try again.")
                continue

            new_name = input("Enter name: ")
            new_price = float(input("Enter price: "))
            new_stock = float(input("Enter initial stock: "))

            products[new_id] = {
                "name": new_name,
                "price": new_price,
                "stock": new_stock
            }

            print(f"Product Added: {new_id} - {new_name} @ R{new_price:.2f} - {new_stock:.0f} (units)")
           
        except ValueError:
            print("Invalid product. Try again.")

#editing the product

    elif choice == "2":
        display_producs()

        edit_id = input("Enter id: ")

        if edit_id == "":
            continue

        if edit_id not in products:
            print("Product not found... Try again")
            continue

        product = products[edit_id]

        print(f"Product to edit: {edit_id} - "
              f"{product['name']} @ "
              f"R{product['price']:,.2f}")

        try:
            new_name = input("Enter name: ")
            new_price = float(input("Enter price: "))

            # cant edit ID or stock
            product["name"] = new_name
            product["price"] = new_price

            print(f"Product edited: {edit_id} - "
                  f"{new_name} @ R{new_price:.2f}")

        except ValueError:
            print("Invalid product edit.")

    elif choice == "3":

        sale_items = []
        sale_total = 0.00

        while True: 
            product_id = input("Enter product id: ")

            #if the ID is blank sale is complete
            if product_id == "":
                break

            if product_id not in products:
                print("Product not found... Try again")
                display_producs()
                continue
            
            try:
                qty = float(input("Enter quantity: "))

                product = products[product_id]
                

                if qty > product["stock"]:
                    print("Not enough stock. Try again.")
                    display_inventory()
                    continue

                total = qty * product["price"]
                
                #to minus stock
                product["stock"] -= qty
                
                sale_total += total

                sale_items.append({
                    "id": product_id,
                    "name": product["name"],
                    "qty": qty,
                    "price": product["price"],
                    "total": total
                })

                print('Name\tQty\tPrice\tTotal')
                for item in sale_items:
                    print(f"{item['name']}\t{item['qty']}\t{item['price']}\t{item['total']}")

                print('=' * 27)
                print(f"Total: R{sale_total:.2f}")
                print('=' * 27)
                
            except ValueError:
                print("Invalid sale. Try again.")

        #the finalized sale
        if len(sale_items) > 0:
            sale_time = datetime.now()  

            number_of_sales += 1
            total_sales += sale_total
            
            transaction = f"{sale_time} - R{sale_total:.2f}"
            transactions.append(transaction)

            #the invoice
            invoice_text = ''
            invoice_text += '=' * 27 + '\n'
            invoice_text += 'Wellness4All\n'
            invoice_text += f'Date: {sale_time.strftime("%d-%m-%Y %H:%M:%S")}\n'
            invoice_text += f'Invoice Number: {invoice_number}\n'
            invoice_text += '=' * 27 + '\n'

            invoice_text += 'Name\tQty\tPrice\tTotal\n'
            for item in sale_items:
                invoice_text += f"{item['name']}\t{item['qty']}\t{item['price']}\t{item['total']}\n"
            invoice_text += '=' * 27 + '\n'
            invoice_text += f"Total: R{sale_total:.2f}\n"
            invoice_text += '=' * 27 + '\n'

            print(invoice_text)

            #saving the invoice file
            filename = f"invoice_{invoice_number}.txt"
            with open(filename, 'w') as file:
                file.write(invoice_text)
            
            print(f"Sale: {sale_time} - R{sale_total:.2f}")
            invoice_number += 1


    #viewing the inventory
    elif choice == "4":
        display_inventory()

    #exiting the program
    elif choice == "5":
        print()
        print('End of day report')
        print(f"Number of Sales: {number_of_sales}")
        print(f"Total Sales: R{total_sales:.2f}")
        print()
        print('Transactions:')

        for transaction in transactions:
            print(transaction)
        print()
        print('=' * 27)

        break  

    else:
        print("Invalid option selected.")