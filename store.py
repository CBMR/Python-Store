from categories import Category

class Store:

    def __init__(self, name, categories):
        
        self.name = name
        self.categories = categories

    def __repr__(self):
        output = ""
        output += f"{self.name} \n"
        i = 1
        for c in self.categories:
            output += f"{i}. {c.name} \n"
            i += 1
        output += f"{len(self.categories) + 1}. Exit"
        return output



myStore = Store("The Dugout", [Category("Running"), Category("Baseball"), Category("Basketball")])
print(myStore)

selection = 0
num_of_categories = len(myStore.categories) + 1

while selection != num_of_categories :
    selection = input("please select your deparment ")
    try:
        selection = int(selection)
        if selection == num_of_categories:
            print("Thank you, come back soon")
        elif selection > 0 and selection <= num_of_categories :
            print(f"user selected {myStore.categories[selection - 1].name}")
        else: 
            print("not a valid selection")
    except:
        print("Your selection must be a number")
