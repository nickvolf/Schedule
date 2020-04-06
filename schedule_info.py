import datetime
import pyinputplus as pyip
import book


class InfoGrabber:
    def __init__(self):
        self.class_name = self.hello()
        self.num_weeks = self.sched_weeks()
        self.num_books = self.how_many_books()
        self.num_classes = self.num_of_classes()
        self.s_day = self.start_day()
        self.s_month = self.start_month()
        self.s_date = self.start_date()
        self.date = datetime.datetime(year=2020, month=int(self.s_month), day=int(self.s_date))
        self.book_set = []

    @staticmethod
    def hello():
        while True:
            s = pyip.inputStr("What is the name of this class?  ")
            s = s.title()
            print(s + "...Is that right?  ")
            rep = pyip.inputYesNo("Y or N  ")
            if rep == 'yes':
                return s
                break
            else:
                do = True

    @staticmethod
    def sched_weeks():
        i = pyip.inputInt("How many weeks are in this month:  ")
        return int(i)

    @staticmethod
    def how_many_books():
        i = pyip.inputInt("How many books will you be using this month:  ")
        return int(i)

    @staticmethod
    def num_of_classes():
        i = pyip.inputInt("How many classes this month:  ")
        return int(i)

    @staticmethod
    def start_day():
        while True:
            s = pyip.inputStr("What day does the Schedule start:  ")
            s = s.title()
            if s == "Monday" or s == "Tuesday" or s == " Wednesday" or s == "Thursday" or s == "Friday":
                return s
            else:
                print("Try again")

    @staticmethod
    def start_month():
        i = pyip.inputInt("What Month is it (number)?  ", min=1, max=12)
        return int(i)

    @staticmethod
    def start_date():
        i = pyip.inputInt("What Month is the starting date?  ", min=1, max=31)
        return int(i)

    def get_books(self):
        for i in range(self.num_books):
            new_title = pyip.inputStr(f'What is the name of book {i + 1}: ')
            self.book_set.append(book.Book(new_title))

        for i in range(len(self.book_set)):
            current_page = pyip.inputInt(f"What is the current page of {self.book_set[i].title}?: ", min=1)
            current_HW_page = pyip.inputInt(f"What is the current HW page of {self.book_set[i].title}?: ", min=1)
            self.book_set[i].current_page = current_page
            self.book_set[i].current_HW_page = current_HW_page

    @staticmethod
    def today_lesson(self):
        response = pyip.inputMenu(['Study', 'Review', 'Test', 'No Class'], numbered=True)
        return response
    
    def ask_study_day(self):        
        # Get choice and call that book. We need the currentPage
        choice = int(self.daily_book()-1)
        todo = int(self.daily_page())
        HWtodo = int(self.daily_howework())

        print("Today we will do:")
        msg = self.book_set[choice].create_assignment(todo, HWtodo)
        msg = str(msg)
        print(msg)
        self.book_set[choice].current_page += todo
        self.book_set[choice].current_HW_page += HWtodo
        return msg  # Returning a string after updating the curPages

    def daily_book(self):
        print("\nWhich book will you use today: ")
        limit = 0
        for books in range(len(self.book_set)):
            print(f'{books + 1}: {self.book_set[books].title}')
            limit += 1
        response = pyip.inputInt("Please choose: ", min=1, max=limit)
        return response

    @staticmethod
    def daily_page():
        response = pyip.inputInt("How many pages will you complete: ")
        return response

    @staticmethod
    def daily_howework():
        response = pyip.inputInt("How many pages will you complete: ")
        return response
