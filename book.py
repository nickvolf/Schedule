class Book:
    def __init__(self, title):
        file = open("books/booklist.csv", 'r')
        self.unit_list = []
        self.current_page = 1
        self.current_HW_page = 1
        self.book_found = False

        for line in file:
            print(line.split(",")[0])

            if line.split(",")[0] == title:
                print("Book Found")
                self.title = line.split(",")[0]
                self.numUnits = int(line.split(",")[1])
                self.book_found = True
                break
        file.close()

        if not self.book_found:
            print(f"Did not find {title}.")


        # Close the booklist and open the specific list of files
        fname = "books/" + title + ".csv"
        ufile = open(fname)
        for line in ufile:
            index = line.split(",")[0]
            title = line.split(",")[1]
            start_page = line.split(",")[2]
            self.unit_list.append(Unit(index, title, start_page))

    def create_assignment(self, todo, hw_todo):
        # look through the list of units. Find the Unit that the starting page belongs to.
        for i in range(len(self.unit_list) - 1):
            if int(self.unit_list[i].startpage) <= int(self.current_page) < int(self.unit_list[i + 1].startpage):

                msg1 = f'{self.unit_list[i].index}:\n'
                msg2 = f'{self.unit_list[i].title}\n'
                msg3 = f"{self.current_page} - {self.current_page + (todo-1)}"
                classMsg = msg1 + msg2 + msg3


                # the comma is there so I can split the returned string
                hwMsg = f",Workbook:\np. {self.current_HW_page} - {self.current_HW_page + hw_todo-1}\n \n Study " \
                        f"flashcards "
                msg = classMsg + hwMsg
                return msg

            # This is the final unit of the book. Needed this because I can't use a less than sign
            # at the end. I don't know the final page.
            elif int(self.current_page) >= int(self.unit_list[-1].startpage):
                msg1 = self.unit_list[-1].index + ":\n"
                msg2 = self.unit_list[-1].title + "\n"
                msg3 = str(self.current_page) + "-" + str(self.current_page + (todo - 1))
                classMsg = msg1 + msg2 + msg3

                # the comma is there so I can split the returned string
                hwMsg = f",Workbook:\np. {self.current_HW_page} - {self.current_HW_page + hw_todo-1}" \
                        f"\n \n Study flashcards"
                msg = classMsg + hwMsg
                return msg
                break


class Unit:
    def __init__(self, index, title, startpage):
        self.index = index
        self.title = title
        self.startpage = startpage