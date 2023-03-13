from guizero import App, Box, Text, Combo, TextBox, PushButton

password = "1234"


def password_check():
    app.disable()
    # Ask, user for the password
    enter_password = app.question("Enter password",
                                  "Please enter the password to gain access the Currency Converter system")
    # Check a password has been entered, Otherwise,  ask the user whether they want The application to quit
    if enter_password is not None:
        # Check the password matches the correct password  call  this function  again, an
        if password == enter_password:
            print("Correct")
            app.enable()
            app.display()

        else:
            app.error("Incorrect password", "You have entered the incorrect password please try again!")
            password_check()
    else:
        if app.yesno("Quit?", "Do you want to quit?"):
            app.destroy()


options = ["Choose", "£(GBP)", "$(USD)"]
border_width = 1
# Create new App object,this will manage the user interface
app = App(title="Currency Converter")
# Create main box for containing layout constraints
master_box = Box(app, layout="grid")
# Create parent box object for containing all objects relating to entering the starting currency
starting_currency_box = Box(master_box, grid=[0, 0])
# Create label for the starting currency, drop-down box
starting_currency_label = Text(starting_currency_box, text="Starting Currency:", )
# Create a drop-down box for entering the starting currency
starting_currency_dropdown = Combo(starting_currency_box, options=options)
# Create parent box object for containing all objects relating to entering the starting amount
starting_amount_box = Box(master_box, grid=[1, 0])
# Create label for the starting amount text entry box
starting_amount_label = Text(starting_amount_box, text="Starting Amount:")
# Create text entry box for entering the starting amount
starting_amount_text_entry_box = TextBox(starting_amount_box, text="0.00")
# Create parent box object for containing all objects relating to entering the desired currency
desired_currency_box = Box(master_box, grid=[2, 0])
# Create label for the desired currency, drop-down box
desired_currency_label = Text(desired_currency_box, text="Desired Currency:")
# Create a drop-down box for entering the desired currency
desired_currency_dropdown = Combo(desired_currency_box, options=options)
# Create parent box object for containing all objects relating to entering the exchange rate
exchange_rate_box = Box(master_box, grid=[1, 1])
# Create label for the starting amount text entry box
exchange_rate_label = Text(exchange_rate_box, text="Exchange Rate:")
# Create text entry box for entering the starting amount
exchange_rate_text_entry_box = TextBox(exchange_rate_box, text="0.00")
# Create box for holding the convert button
convert_button_box = Box(master_box, grid=[1, 2])
# Create convert button
convert_button = PushButton(convert_button_box, text='Convert')
# Create box for holding the results label
results_box = Box(master_box, grid=[1, 3])
# Create text label for displaying the results of the calculation
results_text = Text(results_box, text="Results will be displayed here")
# call the function to check the password
password_check()
