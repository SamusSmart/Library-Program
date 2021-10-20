# Opening the bookData file itself. 
bookData = open("bookinfo.txt", "r").read().split("\n")[2:]

# Seperating each attribute with a comma (splits whenever a comma shows up in a string).
for i in range(0, len(bookData)):
    bookData[i] = bookData[i].split(', ')

# Only function used in code, as it appears twice in Option 2 and 4.
def Average(book_data):
    bookCount = 0
    for book in book_data:
        if float(book[5]) > 0:
            bookCount += (float(book[4]))

    avg = bookCount / len(book_data)
    return avg

# Creating the Menu/Option list.
while True: 
    option = 0
    print("1. Output list of book titles and details.\n"
        "2. Output average price of books in stock.\n"
        "3. Output a report detailing the no. of books existing in each genre type.\n"
        "4. Add new book item and display summary report.\n"
        "5. Query if book title is available and increase/decrease stock level.\n"
        "6. Query the List to return book items ordered in alphabetic order by title/genre.\n"
        "7. Plot a labelled bar chart presenting no. of books existing in each genre type.\n"
        "8. Exit the program.\n ")
    
    while True: #ValueError handling with another while loop.
        try:
            option = int(input("Choose a menu option: "))
            break

        except ValueError:
            print("Input an option from '1' to '8'")
    

    # First option that prints book details.
    if option == 1:
        print("This list showcases books in the format of: \n"
        "AUTHOR, TITLE, FORMAT, PUBLISHER, COST, STOCK, GENRE.\n")
        for book in bookData:
            print("Author: ", book[0], ", Title: ", book[1], ", Format: ", book[2], ", Publisher: ",
            book[3], ", Cost: £", book[4], ", Stock: ", book[5], ", Genre: ", book[6])
        
        print("\n")

        bookCountList = [] # Creation of new list to allow genre's to be appended in order to get total number of book titles.
        for book in bookData: #For loop to append "book[5]" into my new empty list.
            bookCountList.append(int(book[5]))

        print("The number of book titles available are: ", (sum(bookCountList)))

        # Multiplying price by stock to get total value of books.
        totalbookvalue = 0
        for book in bookData:
            totalbookvalue += (float(book[4]) * float(book[5]))

        print("The total value of books in stock is: £", round(totalbookvalue, 2))
        print("\n")
    # End of option 1.


    # Second option outputs average price of books in stock
    if option == 2:
        print("The average price of books in stock is: £", (round(Average(bookData), 2)))
        print("\n")
    # End of option 2.


    # Third option outputs the total amount of books in each genre
    if option == 3:
        genres = []
        for book in bookData:
            genres.append(book[6])

        for genre in set(genres):
            genreCount = 0
            for book in bookData:
                if book[6] == genre:
                    genreCount += int(book[5])
            print("The number of books in the", genre, "category are: ", genreCount)
    # End of option 3.


    if option == 4:
        another = 'Yes'

        #bookDetail used to create 7 empty items in a list. (Fixes "out of index" issue.)
        bookDetail = [""]*7

        while another == 'Yes':
            print('Please enter the following book record information: ')
            bookDetail[0] = input('Author Name: ')
            bookDetail[1] = input('Book Title: ')
            bookDetail[2] = input('Format: ')
            bookDetail[3] = input('Publisher: ')
            bookDetail[4] = input('Price: ')
            bookDetail[5] = input('Stock: ')
            bookDetail[6] = input('Genre: ')

            #Writing new book information into the bookData file
            bookData.append(bookDetail)

            #Creation of new list to display total increase in number of titles in stock.
            bookCountList = []

            #For loop to append "book[5]" into my new 'bookCountList' list.
            for book in bookData:
                bookCountList.append(int(book[5]))

            print("The total increase in number of titles in stock is: ", (sum(bookCountList)))
            
            #Gets average price of books by excluding the newly added book item from the calculation
            print("The cost difference in average price of books in stock is: ", round(Average(bookData) - Average(bookData[:-1]), 2))
            
            print('Would you like to add another record to the system?: ')
            another = input('Enter Yes or No: ')

        print('Information has been saved and stored.')
        print('Goodbye.')
        print("\n")
    # End of option 4.


    if option == 5:
        bookName = input('Enter a book name: ')
        
        newbookList = [] # Creation of a new list in order to append the new stock information and update the main book data list.
        for book in bookData:
            if bookName == book[1]:
                if book[5] == "0":
                    print("This book is currently out of stock.")
                update = input("Would you like to update the stock?: ")
                if update == "Yes":
                    book[5] = input("Enter new stock: ")
                
                    
            newbookList.append(book)
            bookData = newbookList           
    # End of option 5.


    if option == 6:
            while True:
                Selection = input('Would you like to sort by Title or Genre?: ')
            
                if Selection == 'Genre':
                    break
                elif Selection == 'Title':
                    break
                else:
                    print("Input either 'Genre' or 'Title'.")
            
            newBookList = []

            if Selection == 'Genre':
                for book in bookData:
                    newBookList.append(", ".join([book[6]]+book[:6]))
                    newBookList.sort()
                print("\n".join(newBookList))

            if Selection == 'Title':
                for book in bookData:
                    newBookList.append(", ".join([book[1]]+book[:1]+book[2:]))
                    newBookList.sort()
                print("\n".join(newBookList))
            
    print("\n")
    # End of option 6.

    if option == 7:
        #Importing Matplotlib along with PyQt5, as the AGG default doesn't work properly.
        import matplotlib
        matplotlib.use('Qt5Agg')
        import matplotlib.pyplot as plt
        
        #Creating empty lists for each attribute used in the Bar Chart.
        genres = []
        x = []
        bookAttributes = []


        for book in bookData:
            genres.append(book[6]) #Appends the genre into the new list

        for genre in set(genres):
            genreCount = 0
            for book in bookData:
                if book[6] == genre:
                    genreCount += int(book[5])

            x.append(genre)
         
            bookAttributes.append(genreCount)

        x_pos = list(range(len(x)))
        
        #Simple Bar Chart labelling.
        plt.bar(x_pos, bookAttributes, color='green')
        plt.xlabel("Genre Type")
        plt.ylabel("Stock")
        plt.title("Number of books existing in each genre type")

        plt.xticks(x_pos, x)

        plt.show()
        print("\n")
    # End of option 7.

    if option == 8:
        print('Goodbye.')
        break
    # End of option 8.
