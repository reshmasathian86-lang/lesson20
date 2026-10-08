# ================================
# SHOPPING DISCOUNT CALCULATOR
# ================================

# ---------- PART 1: retry loop ----------
valid = False
while not valid:

    # ---------- PART 2: input and calculation ----------
    try:
        bill = float(input("Bill amount: "))
        discount = float(input("Discount percent: "))
        people = int(input("Number of people: "))

        discount_amount = bill * discount / 100
        final_bill = bill - discount_amount
        each = final_bill / people

    # ---------- PART 3: handle errors ----------
    except ValueError:
        print("Please type numbers only.")
    except ZeroDivisionError:
        print("People cannot be 0.")

    # ---------- PART 4: else and finally ----------
    else:
        print("Final bill:", final_bill)
        print("Each person pays:", each)
        valid = True
    finally:
        print("Attempt finished.")
