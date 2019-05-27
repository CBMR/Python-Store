class Store:

    def __init__(self, name, categories):
        
        self.name = name
        self.categories = categories

    def __repr__(self):
        output = ""
        output += f"{self.name} \n"
        i = 1
        for c in self.categories:
            output += f"{i}. {c} \n"
            i += 1
        return output


myStore = Store("The Dugout", ["Runnig", "Baseball", "Basketball"])
print(myStore)