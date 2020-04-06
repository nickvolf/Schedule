import datetime
from schedule_prod import Schedule
from schedule_info import InfoGrabber
import pyinputplus as pyip
import book

# get all the information and the basic formatting of the schedule
ig = InfoGrabber()
schedule = Schedule(ig.class_name, ig.num_classes, ig.num_weeks, ig.date)
ig.get_books()

for weeks in range(ig.num_weeks):
    for y in range(10):
        if y % 2 == 0:
            plan = ig.today_lesson()
            if plan == "Study":
                msg = ig.ask_study_day()
                class_todo = msg.split(',')[0]
                print(class_todo)
                hw_todo = msg.split(',')[1]

                row = (weeks+7)+(weeks*2)
                schedule.print_to_cell(class_todo, row, y+1, "cls_todo")
                schedule.print_to_cell(hw_todo, row, y+2, "hw_todo")
            elif plan == 'Review':
                row = (weeks+7)+(weeks*2)
                schedule.print_to_cell("Review", row, y+1, "cls_todo")
                schedule.print_to_cell("Flashcards", row, y+2, "hw_todo")
            elif plan == 'Test':
                row = (weeks+7)+(weeks*2)
                schedule.print_to_cell("Test", row, y+1, "cls_todo")
                schedule.print_to_cell("Flashcards", row, y+2, "hw_todo")
            elif plan == 'No Class':
                row = (weeks+7)+(weeks*2)
                schedule.print_to_cell("No School", row, y+1, "no_school")
                schedule.print_to_cell("No Homework", row, y+2, "no_school")

schedule.save_book(ig.class_name)
