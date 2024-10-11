from collections import deque

bookings_stack = []
ticket_requests_queue = deque
movie_screenings_list = ["blackman movie  - 15:00 PM", "fight war movie - 17:00 PM", "fireman movie  - 19:00 PM"]

def display_movie_screenings():
    print("\nAvailable Movie Screenings:")
    for movie in movie_screenings_list:
        print(f"- {movie}")

def book_ticket(movie, customer_name):
    booking = f"Booking: {customer_name} for {movie}"
    bookings_stack.append(booking)
    print(f"{booking} added.")

def undo_last_booking():
    if bookings_stack:
        last_booking = bookings_stack.pop()
        print(f"Undone: {last_booking}")
    else:
        print("No bookings to undo.")

def add_ticket_request(customer_name, movie):
    request = f"Ticket Request: {customer_name} for {movie}"
    ticket_requests_queue.append(request)
    print(f"Ticket request added: {customer_name} for {movie}")

def process_ticket_request():
    if ticket_requests_queue:
        next_request = ticket_requests_queue.popleft()
        print(f"Processing: {next_request}")
    else:
        print("No ticket requests to process.")

def display_bookings():
    if bookings_stack:
        print("\nCurrent Bookings:")
        for booking in bookings_stack:
            print(f"- {booking}")
    else:
        print("No bookings available.")

def display_ticket_requests():
    if ticket_requests_queue:
        print("\nCurrent Ticket Requests:")
        for request in ticket_requests_queue:
            print(f"- {request}")
    else:
        print("No ticket requests available.")

def movie_theater_system():
    while True:
        print("\n1. Display Movie Screenings")
        print("2. Book a Movie Ticket")
        print("3. Undo Last Booking")
        print("4. Add Ticket Request")
        print("5. Process Next Ticket Request")
        print("6. Display All Bookings")
        print("7. Display Ticket Requests")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_movie_screenings()
        elif choice == '2':
            customer_name = input("Enter customer name: ")
            display_movie_screenings()
            movie = input("Enter movie to book (exact title with time): ")
            if movie in movie_screenings_list:
                book_ticket(movie, customer_name)
            else:
                print("Invalid movie selected.")
        elif choice == '3':
            undo_last_booking()
        elif choice == '4':
            customer_name = input("Enter customer name: ")
            display_movie_screenings()
            movie = input("Enter movie for ticket request (exact title with time): ")
            if movie in movie_screenings_list:
                add_ticket_request(customer_name, movie)
            else:
                print("Invalid movie selected.")
        elif choice == '5':
            process_ticket_request()
        elif choice == '6':
            display_bookings()
        elif choice == '7':
            display_ticket_requests()
        elif choice == '8':
            print("Exiting the movie theater system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    movie_theater_system()
