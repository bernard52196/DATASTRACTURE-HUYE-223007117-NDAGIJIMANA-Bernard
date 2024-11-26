
# 63. Movie Theater Booking System: Stack for undoing bookings, queue for ticket requests and list for available movie screenings

from collections import deque

class MovieTheaterBookingSystem:
    def __init__(self):
        self.available_movies = ["blackman 4:00pm", "ware 3:00pm", "Ip man 7:00pm"]  
        self.ticket_requests = deque() 
        self.booking_stack = [] 
    
    def display_movies(self):
        print("\nAvailable Movies:")
        for i, movie in enumerate(self.available_movies, start=1):
            print(f"{i}. {movie}")
    
    def request_ticket(self, customer_name, movie_choice):
        if 1 <= movie_choice <= len(self.available_movies):
            movie_name = self.available_movies[movie_choice - 1]
            self.ticket_requests.append((customer_name, movie_name))
            print(f"\nTicket request added for {customer_name} to watch '{movie_name}'")
        else:
            print("\nInvalid movie selection. Please try again.")
    
    def process_request(self):
        if self.ticket_requests:
            customer_name, movie_name = self.ticket_requests.popleft()
            self.booking_stack.append((customer_name, movie_name))
            print(f"\nBooking confirmed: {customer_name} is watching '{movie_name}'")
        else:
            print("\nNo ticket requests to process.")
    
    def undo_booking(self):
        if self.booking_stack:
            customer_name, movie_name = self.booking_stack.pop()
            print(f"\nBooking for {customer_name} watching '{movie_name}' has been undone.")
        else:
            print("\nNo bookings to undo.")

if __name__ == "__main__":
    theater = MovieTheaterBookingSystem()
    
    while True:
        print("\nMovie Theater Booking System Menu:")
        print("1. Display Available Movies")
        print("2. Request Ticket")
        print("3. Process Ticket Request")
        print("4. Undo Last Booking")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            theater.display_movies()
        
        elif choice == '2':
            theater.display_movies()
            try:
                customer_name = input("\nEnter customer's name: ")
                movie_choice = int(input("Enter the number of the movie: "))
                theater.request_ticket(customer_name, movie_choice)
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
        
        elif choice == '3':
            theater.process_request()
        
        elif choice == '4':
            theater.undo_booking()
        
        elif choice == '5':
            print("\nThank you for using the Movie Theater Booking System. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")
