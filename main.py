from guizero import App, Box, Text, Combo, TextBox

# create new App object , this will manage the main user interface screen
app = App(title=" Currency Converter")
# Create main box for containing layout constraints
master_box = Box(app)
# Create parent box object for containing all objects relating to entering the starting currency
starting_currency_box = Box(master_box, align="left")
# Create label for the starting currency, drop-down box
starting_currency_label = Text(starting_currency_box, text="Starting Currency:", align="left")
# Create a drop-down box for entering the starting currency
starting_currency_dropdown = Combo(starting_currency_box)
# Create parent box object for containing all objects relating to entering the starting amount
starting_amount_box = Box(master_box)
# Create label for the starting amount text entry box
starting_amount_label = Text(starting_amount_box, text="Starting Amount:")
# Create text entry box for entering the starting amount
starting_amount_text_entry_box = TextBox(starting_amount_box)
# Finally display the app screen
app.display()
