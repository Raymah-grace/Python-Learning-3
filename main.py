# CampusPrint, stage 1: complete TODO 1 through TODO 8.
# Starter scaffold: menu repetition is supplied as an example of a while loop.
# You will write the field-validation loops and a for loop yourself.

BW_RATE = 10
COLOUR_RATE = 30
BINDING_RATE = 50
BULK_THRESHOLD = 100

completed_orders = 0
session_pages = 0
session_revenue = 0
running = True

print("Welcome to CampusPrint")
while running:
    print("\n1. New order\n2. Session summary\n0. Exit")
    choice = input("Choice: ").strip()

    if choice == "1":
        # TODO 1: Read pages and copies with int(input(...)).
        # Write a while loop for EACH field to retry until it is in range.
        # pages: 1..500; copies: 1..100. Do not count failed attempts.
        pages = 0

        while pages < 1 or pages > 500:
            pages =int(input("pages per copy: "))

        copies = 0
        while copies < 1 or copies > 100:
            copies =int(input("copies: "))    


        # TODO 2: Read mode (B/C) and binding (Y/N). 
        # .strip().upper() is supplied vocabulary: it removes surrounding
        # whitespace and normalises letter case. Retry invalid choices.
        read_mode = ""
        while read_mode != "B" and read_mode != "C":
            read_mode = input("read_mode B/C: ").strip().upper()

        binding = "" 
        while binding != "Y" and binding != "N":
            binding = input("binding Y/N: ").strip().upper()

      

        

        # TODO 3: Select rate with if/else and calculate printed_pages
        # and printing_subtotal. Use the named tariff constants above.
        printed_pages = pages * copies
        if read_mode =="B":
            rate = BW_RATE
        else:
            rate =COLOUR_RATE

        printing_subtotals = printed_pages * rate   

           

        # TODO 4: Select the bulk discount; calculate binding_charge
        # and total. Discount applies to printing only, never binding.

        if printed_pages >= 100:
            discount = printing_subtotals * 0.10
        else:
            discount = 0

        if binding == "Y":
            binding_charge = BINDING_RATE
        else:
            binding_charge = 0

        total = printing_subtotals - discount + binding_charge        

       

        

        # TODO 5: Display the five receipt lines in BUSINESS_RULES.md.
        # Example formatting: print("Printed pages:", printed_pages)
        
        print(f"printed_pages: {printed_pages}\n" f"printing_subtotals: {printing_subtotals}\n" f"discount: {discount}\n" f"binding_charge: {binding_charge}\n" f"total: {total}")
        

        # TODO 6: Use for ... in range(...) to print Copy 1 of n, etc.
        # range stop values are exclusive: check both 1 and 3 copies.
        
        for copy in range(1,copies + 1):
            print(copy)

        # TODO 7: Update the THREE session accumulators exactly once,
        # after a valid order. Remove the temporary message below.
        

        completed_orders += 1
        session_pages += printed_pages
        session_revenue += total


    elif choice == "2": 
        # TODO 8a: Display the three session summary lines.

        print("completed_orders:", completed_orders)
        print("session_pages:", session_pages)
        print("session_revenue:", session_revenue)

    elif choice == "0":
    # TODO 8b: Display the same summary before terminating the loop.
        # Keep the line below; explain why the loop stops after it.

        print("completed_orders:", completed_orders)
        print("session_pages:", session_pages)
        print("session_revenue:",session_revenue)
        running = False
    else:
        print("Invalid choice.")

print("Goodbye.")
 