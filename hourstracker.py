from cmu_graphics import *

app.total_hours = 0
background = Rect(0, 0, 400, 400, fill='lightgrey')
title = Label('Honor Society Tracker', 200, 20, size=25)
awards_label_1 = Label('', 200, 320, size=15)
awards_label_2 = Label('', 200, 340, size=15)

inputer = Group(
    Rect(20, 50, 360, 40, fill='lightgrey', border='darkgrey'),
    Label('Enter in Your Hours', 190, 70, size=20),
)

entries = []

def add_entry(entry):
    global entries
    if len(entries) >= 10:
        entries.pop(0)
    entries.append(entry)
    display_entries()
    check_awards(app.total_hours)

def onMousePress(mouseX, mouseY):
    global entries
    if inputer.contains(mouseX, mouseY):
        purpose = app.getTextInput('What is the name of the entry? ')
        if purpose:
            hours = app.getTextInput('How many hours did you spend on this? ')
            if hours.isdigit():
                app.total_hours += int(hours)
                entry = (purpose, int(hours))
                add_entry(entry)

def display_entries():
    global entries
    y_position = 120
    for entry in entries:
        app.entry_label = Label(f'{entry[0]} - {entry[1]} hours', 200, y_position, size=15)
        y_position += 20

app.age = 0
app.age_checked = False
def check_awards(total_hours):
    if app.age_checked == False:
        app.age = int(app.getTextInput('What is your age? '))
    app.age_checked = True
    age_group = determine_age_group(app.age)
    print("Age Group:", age_group)
    awards_eligible = []

    if age_group:
        awards_dict = {
            'Kids': {'Bronze': 26, 'Silver': 50, 'Gold': 75, 'Lifetime Achievement Award': 4000},
            'Teens': {'Bronze': 50, 'Silver': 75, 'Gold': 100, 'Lifetime Achievement Award': 4000},
            'Young Adults': {'Bronze': 100, 'Silver': 175, 'Gold': 250, 'Lifetime Achievement Award': 4000},
            'Adults': {'Bronze': 100, 'Silver': 250,'Gold': 500,'Lifetime Achievement Award': 4000}
        }
        if age_group in awards_dict:
            for award, hours_required in awards_dict[age_group].items():
                if total_hours>= hours_required:

                    awards_eligible.append(award)

            print("Eligible Awards:", awards_eligible)
            if awards_eligible:
                awards_text = f'You are eligible for the following awards: {", ".join(awards_eligible)}'
                # Split the text at the colon
                awards_text_parts = awards_text.split(':', 1)
                awards_label_1.value = awards_text_parts[0]
                awards_label_2.value = awards_text_parts[1]
            else:
                awards_label_1.value = 'You are not eligible for any awards yet.'
        else:
            awards_label_1.value = 'Unable to determine age group. Please contact support.'


def determine_age_group(age):
    if 5 <= age <= 10:
        return 'Kids'
    elif 11 <= age <= 15:
        return 'Teens'
    elif 16 <= age <= 25:
        return 'Young Adults'
    elif age >= 26:
        return 'Adults'
    else:
        return None

cmu_graphics.run()
