from collections import deque

booking_stack = []
booking_ticket_queue = deque()
movie_list = ["Blackman 4:00pm", "Ware 3:00pm", "Ip Man 7:00pm"]

def available_movie():
    print("\nAvailable Movie List:")
    for movie in movie_list:
        print(f"- {movie}")

def booking_movie(name, movie):
    booking = f"Booking: {name} for {movie}"
    booking_stack.append(booking)
    print(f"{booking}, added successfully.")

def undo_last_booking():
    if booking_stack:
        last_booking = booking_stack.pop()
        print(f"{last_booking}, undone.")
    else:
        print("No bookings available to undo.")

def add_request(name, movie):
    request = f"Request: {name} for {movie}"
    booking_ticket_queue.append(request)
    print(f"{request}, added to the queue.")

def process_ticket_request():
    if booking_ticket_queue:
        next_request = booking_ticket_queue.popleft()
        print(f"Processing: {next_request}")
    else:
        print("No ticket requests to process.")

def display_movie_booked():
    if booking_stack:
        print("\nMovies Booked:")
        for booked in booking_stack:
            print(f"- {booked}")
    else:
        print("No movies have been booked.")

def display_request():
    if booking_ticket_queue:
        print("\nPending Ticket Requests:")
        for request in booking_ticket_queue:
            print(f"- {request}")
    else:
        print("No ticket requests available.")

def movie_booking_system():
    while True:
        print("\nMovie Booking System Menu:")
        print("1. View Available Movies")
        print("2. Book a Movie")
        print("3. Undo Last Booking")
        print("4. Add a Ticket Request")
        print("5. Process a Ticket Request")
        print("6. Display Booked Movies")
        print("7. Display Ticket Requests")
        print("8. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 8.")
            continue

        if choice == 1:
            available_movie()
        elif choice == 2:
            name = input("Enter your name: ")
            available_movie()
            movie = input("Enter the movie you want to book: ")
            if movie in movie_list:
                booking_movie(name, movie)
            else:
                print("The selected movie does not exist.")
        elif choice == 3:
            undo_last_booking()
        elif choice == 4:
            name = input("Enter your name: ")
            available_movie()
            movie = input("Enter the movie for the ticket request: ")
            if movie in movie_list:
                add_request(name, movie)
            else:
                print("The selected movie does not exist.")
        elif choice == 5:
            process_ticket_request()
        elif choice == 6:
            display_movie_booked()
        elif choice == 7:
            display_request()
        elif choice == 8:
            print("Thank you for using the Movie Booking System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")


movie_booking_system()
