# exception_mini_project.py

def analyze_purchase(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]

            items = []
            free_items = 0
            total_amount = 0
            discount = 0

            for line in lines:
                parts = line.split()
                if len(parts) == 2:
                    name, price = parts
                    if price.lower() == "free":
                        free_items += 1
                    elif name.lower() == "discount":
                        discount = int(price)
                    else:
                        try:
                            price = int(price)
                            items.append((name, price))
                            total_amount += price
                        except ValueError:
                            print(f"Invalid price for item: {line}")

            print(f"Enter the file name: {filename}")
            print("No of items purchased:", len(items))
            print("No of free items:", free_items)
            print("Amount to pay:", total_amount)
            print("Discount given:", discount)
            print("Final amount paid:", total_amount - discount)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(" Error:", e)


# Run the function
if __name__ == "__main__":
    filename = input("Enter the purchase file name (e.g. Purchase-1.txt): ")
    analyze_purchase(filename)
