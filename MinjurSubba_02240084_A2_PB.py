class PokemonCardBinderManager:
    def __init__(self):
        pass  
    
    
    MaxPokemonNumber = 1025
    CardsPerPage = 64
    rows = 8
    column = 8
    
    '''These are basically some stats that we will use in later coding, say.. its like
    constants that we have assigned a value.'''

    def __init__(self):
        self.pokemon_binder = {}
        
    '''This dictionary will hold all the added cards
     Key: Pokedex number, Value:(Page, Row, Column)'''

    def run(self):
        while True:
            print("Welcome to Pokemon Card Binder Manager!")
            print("Main Menu:")
            print("1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View current placements")
            print("4. Exit")

            binder_choice = input("Select option: ")

            if binder_choice == "1":
                try:
                    pokedex_number = int(input("Enter Pokedex number (1-1025): "))
                    self.add_pokemon_card(pokedex_number)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif binder_choice == "2":
                self.reset_binder()
            elif binder_choice == "3":
                self.view_current_binder()
            elif binder_choice == "4":
                self.exit_binder_manager()
                break
            else:
                print("Invalid input. Please try again.")

    def add_pokemon_card(self, pokedex_number):
        if not (1 <= pokedex_number <= self.MaxPokemonNumber):
            print("Invalid Pokedex number. It must be between 1 and 1025.")
            return
       
        '''I am doing this to validate the users input. i cannot simply use if statement here because 
        if i do so, the logic will be wrong and it will neber execite the program'''

        if pokedex_number in self.pokemon_binder:
            page, row, col = self.pokemon_binder[pokedex_number]
            print(f"Page: {page}")
            print(f"Position: Row {row}, Column {col}")
            print(f"Status: Pokedex #{pokedex_number} already exists in binder")
            return
        '''To check if a card already added'''



        index_of_card = len(self.pokemon_binder)
        page_number = (index_of_card // self.CardsPerPage) + 1
        position_on_page = index_of_card % self.CardsPerPage
        row = (position_on_page // self.column) + 1
        col = (position_on_page % self.column) + 1
        '''We use the length of the current binder, to find the next available slot.
     Now because, cards are placed in order, the index of the next card will be equal to the 
     number of cards already added.

     page_number = (index of card // cards per page) + 1
     We divide the card index by 64 (cards per page) to get the 0-based page.
     (Basically python numbers from 0)
     We add 1 so that the first page shows as Page 1 instead of Page 0 (computer-style).

     position_on_page = card_index % cards per page
         Finds the position within the page (0 to 63).

     row = (position_on_page // column) + 1
     Each row has 8 cards. We calculate which row the card should go in.
     We add +1 to change from 0-indexed to 1-indexed (user sees Row 1, not Row 0).

     col = (position_on_page % column) + 1
     Finds the column within the row.
     '''
     

        self.pokemon_binder[pokedex_number] = (page_number, row, col)
        
        '''this is basically Saving card in memory'''



        print(f"Page: {page_number}")
        print(f"Position: Row {row}, Column {col}")
        print(f"Status: Added Pokedex #{pokedex_number} to binder")


    '''This section handles the output after successfully adding a Pokémon card to the binder.

      it prints:
      
      1. The page number where the card is placed.
      2. The position of the card within the page
     3. A status message confirming the Pokedex number of the card added'''



    def view_current_binder(self): #This prints out all the Pokemon cards currently saved in your binder.
        print("Contents:")

        if not self.pokemon_binder:
            print("The binder is empty.")
            print("Total cards in binder: 0")
            print("completion: 0%")
            return
        
        ''' this will check if the binder is empty (if the dictionary has no entries).
          If it is empty, it prints that there are 0 cards and 0% completion and exits the method.'''


        for pokedex_number in sorted(self.pokemon_binder): #Loops through all saved Pokémon cards in order.
            page, row, col = self.pokemon_binder[pokedex_number]
            print(f"Pokedex #{pokedex_number}:")
            print(f" Page: {page}")
            print(f" Position: Row {row}, Column {col}")
            
            ''' This gets the position of the Pokémon card in the 
                binder: which page, row, and column it's in.'''

        
        total_cards = len(self.pokemon_binder)
        completion_percent = (total_cards / self.MaxPokemonNumber) * 100
        print(f"Total cards in binder: {total_cards}")
        print(f"% completion: {completion_percent:.1f}%")
        
        '''this section of code is used to show completion stats basically
        like from the'''

    def reset_binder(self):
        print("WARNING: This will delete ALL Pokemon cards from the binder.")
        print("This action cannot be undone.")
        user_input = input("Type 'CONFIRM' to reset or 'EXIT' to return to the Main Menu: ")

        if user_input == "CONFIRM":
            self.pokemon_binder.clear()
            print("The binder reset was successful! All cards have been removed.")
        elif user_input == "EXIT":
            print("Binder reset cancelled. Returning to Main Menu.")
        else:
            print("Invalid input. Binder reset aborted.")

    def exit_binder_manager(self):
        print("Thank you for using Pokemon Card Binder Manager!")


