from cmu_graphics import *

app.total_hours = 0 #declares the hours variable

#background, title, and labels that will be used for eligible awards
background = Rect(0, 0, 400, 400, fill='skyblue')
title = Label('Honor Society Tracker', 200, 20, size=25)
awards_label_1 = Label('', 200, 320, size=15)
awards_label_2 = Label('', 200, 340, size=15)

#input button
inputer = Group(
    Rect(20, 50, 360, 40, fill='lightgrey', border='blue'),
    Label('Enter in Your Hours', 190, 70, size=20),
)

#entries list declaration
entries = []

#creates the add entry function that takes entry as a parameter
def add_entry(entry):

    #sets entries to a globale variable
    global entries
    if len(entries) >= 10: #checks whether they have 10 entries 
        entries = entries.pop(0) #remove oldest entry if list is full
    entries.append(entry) #adds the entry to the entries list
    display_entries() # runs display_entries function
    check_awards(app.total_hours) #check whether you are available for any awards

def onMousePress(mouseX, mouseY):  #onMousePress (builit in function in CMU)
    global entries
    if inputer.contains(mouseX, mouseY): #check whether you clicked on the input button
        purpose = app.getTextInput('What is the name of the entry? ') #get the name of the entry
        if purpose: #once purpose is filled out
            hours = app.getTextInput('How many hours did you spend on this? ') #ask how many hours they spent on this task/event
            if hours.isdigit(): #input validation
                app.total_hours += int(hours) #add hours total amount of hours
                entry = (purpose, int(hours)) #set the entry as a tuples
                add_entry(entry) #run the add_entry function

def display_entries(): #declare a display_entries function
    global entries
    y_position = 120 #the starting y postion (the first entrie's y position is at 120)
    realentries = entries

    for entry in realentries: #loop through the entries list
        app.entry_label = Label(f'{entry[0]} - {entry[1]} hours', 200, y_position, size=15) #create label calling tuple values
        y_position += 20 #increment the y position so that the entries go down the screen

#sets age var and age_checked var
app.age = 0
app.age_checked = False

def check_awards(total_hours):  #checks for award eligibility
    if app.age_checked == False:
        app.age = int(app.getTextInput('What is your age? ')) #ask for their age
    app.age_checked = True #sets it to True so that their age doesnt get asked again
    age_group = determine_age_group(app.age) #puts them into an age_group
    print("Age Group:", age_group)
    awards_eligible = [] #declare the list for eligible awards

    if age_group: #if age_group exists
        awards_dict = {  #create a dictionary that contains a dictionary of age groups. this dictionary with age groups are each nested dicitonaries with the awards and their respective values
            'Kids': {'Bronze': 26, 'Silver': 50, 'Gold': 75, 'Lifetime Achievement Award': 4000},
            'Teens': {'Bronze': 50, 'Silver': 75, 'Gold': 100, 'Lifetime Achievement Award': 4000},
            'Young Adults': {'Bronze': 100, 'Silver': 175, 'Gold': 250, 'Lifetime Achievement Award': 4000},
            'Adults': {'Bronze': 100, 'Silver': 250,'Gold': 500,'Lifetime Achievement Award': 4000}
        }
        if age_group in awards_dict: #checks wether age_group exists in dictionary
            for award, hours_required in awards_dict[age_group].items():  #iterate over each award and its corresponding required hours in the age group's dictionary
                if total_hours>= hours_required:
                    awards_eligible.append(award)  #add the award to eligible awards

            print("Eligible Awards:", awards_eligible)
            if awards_eligible:  #if there are any eligible awards
                awards_text = f'You are eligible for the following awards: {", ".join(awards_eligible)}'
                # Split the text at the colon
                awards_text_parts = awards_text.split(':', 1)
                awards_label_1.value = awards_text_parts[0]
                awards_label_2.value = awards_text_parts[1]
            else:
                awards_label_1.value = 'You are not eligible for any awards yet.' #no eligible awards
        else:
            awards_label_1.value = 'Unable to determine age group. Please contact support.' #age_group error message


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
