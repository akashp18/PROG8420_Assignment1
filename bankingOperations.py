arr_customer = []
arr_available_balance = []
current_user = ""


def int_Validator(input_amount):
    try:
        selected_int = int(input_amount)
        return True, selected_int
    except ValueError:
        print("Please enter number.")
        return False, 0


def acc_validator(acc_holder_name):
    if acc_holder_name in arr_customer:
        return True
    else:
        return False


def float_amount_validator(input_amount):
    try:
        new_amount = float(input_amount)
        if new_amount < 0:
            print("Negative value detected.")
            return False, 0
        else:
            return True, new_amount
    except ValueError:
        print("Please enter amount properly.")
        return False, 0


def create_acc():
    print("Enter below details for new account")
    cust_name = input("Please enter Account number:\n")
    if acc_validator(cust_name.lower()):
        print("Its already used by someone for banking.")
        create_acc()
    else:
        arr_customer.append(cust_name.lower().strip())
        arr_available_balance.append(0)
        global current_user
        current_user = cust_name.lower().strip()
        print(
            "Congratulation {}. Your account has been opened now. You have ${} available balance".format(cust_name,
                                                                                                         0))


def no_user():
    print("1. Create new Account.")
    print("2. Quit")
    selected_value = input("Please enter your choice: \n")
    if int_Validator(selected_value)[0]:
        selected_value_int = int_Validator(selected_value)[1]
        if selected_value_int == 1:
            create_acc()
            select_operations()
        elif selected_value_int == 2:
            print("Thank you for banking with us.")
        else:
            print("Please select valid option.")
            no_user()
    else:
        no_user()


def deposit_operation():
    amount_validator = True
    while amount_validator:
        deposite_amount = input("Please enter deposit amount: \n")
        amount_validated = float_amount_validator(deposite_amount)
        is_amount_valid = amount_validated[0]
        deposit_amount = amount_validated[1]
        if is_amount_valid:
            amount_validator = False
            cust_index = arr_customer.index(current_user)
            total_available =  arr_available_balance[cust_index]
            arr_available_balance[cust_index] = total_available + deposit_amount
            print("Account: {} => Successfully deposited ${}.".format(current_user,deposit_amount))
            print("Account: {} \n Total available balance after deposit: ${}".format(current_user, arr_available_balance[cust_index]))


def Withdrawal_operation():
    amount_validator = True
    while amount_validator:
        withdrawal_amount = input("Please enter withdrawal amount: \n")
        amount_validated = float_amount_validator(withdrawal_amount)
        is_amount_valid = amount_validated[0]
        withdrawn_amount = amount_validated[1]
        if is_amount_valid:
            cust_index = arr_customer.index(current_user)
            total_available = arr_available_balance[cust_index]
            if (total_available - withdrawn_amount) < 0:
                print("Sorry! insufficient balance.")
            else:
                amount_validator = False
                arr_available_balance[cust_index] = total_available - withdrawn_amount
                print("Account: {} => Successfully withdrawn ${}.".format(current_user,withdrawn_amount))
                print("Account: {} \n Total available balance after withdrawal: ${}".format(current_user, arr_available_balance[cust_index]))


def show_balance():
    cust_index = arr_customer.index(current_user)
    print("Account: {} => Total available balance: ${}.".format(current_user, arr_available_balance[cust_index]))


def change_Account():
    global current_user
    current_user = ""
    select_Account()


def select_operations():
    print("1. Balance check")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Go to another Account")
    print("5. Quit Application")
    selected_value = input("Please enter your choice: \n")
    if int_Validator(selected_value)[0]:
        selected_value_int = int_Validator(selected_value)[1]
        if selected_value_int == 1:
            show_balance()
            select_operations()
        elif selected_value_int == 2:
            deposit_operation()
            select_operations()
        elif selected_value_int == 3:
            Withdrawal_operation()
            select_operations()
        elif selected_value_int == 4:
            system_start()
        elif selected_value_int == 5:
            print("Thank you for banking with us.")
        else:
            print("Please select valid option.")
            select_operations()
    else:
        print("Please select valid option.")
        select_operations()


def select_Account():
    selected_acc = input("Please enter your account number: \n")
    if selected_acc in arr_customer:
        global current_user
        current_user = selected_acc
        select_operations()
    else:
        print("Sorry! No such account found in database")
        valid_choice = True
        while valid_choice:
            selected_value = input("Do you have Account? Sure? Y for YES or N for NO. : \n").lower()
            if selected_value == 'y':
                valid_choice = False
                select_Account()
            elif selected_value == 'n':
                valid_choice = False
                no_user()
                #print("Thank you for banking with us.")
            else:
                print("Please select valid option.")


def system_start():
    selected_value = input("Do you have User(Bank account)? Enter Y  for YES or N  for NO: \n").lower()
    if selected_value == 'y':
        select_Account()
    elif selected_value == 'n':
        no_user()
    else:
        print("Please enter proper choice.")
        system_start()