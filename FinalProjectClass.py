from datetime import datetime

class InventoryManager:
    """stores data from txt file and searches for direct and alternative matches"""
    def __init__(self):
        """establish variable"""
        self.items = []

    def loadData(self, fileName):
        """data is stored from file"""
        with open(fileName, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                itemID, manufacturer, itemType, price, date = parts[:5]
                price = int(price)
                serviceDate = datetime.strptime(date, "%m/%d/%Y").date()
                isDamaged = 'damaged' in parts
                self.items.append([itemID, manufacturer.lower(), itemType.lower(), price, serviceDate, isDamaged])

    def search(self, searchInput):
        """searches through stored list for matches"""
        searchWords = searchInput.lower().split()
        mainMatch = None
        alts = []           #list bc need to search for most expensive

        for item in self.items:
            #item format: [0.itemID, 1.manufacturer, 2.itemType, 3.price, 4.serviceDate, 5.isDamaged]
            if not item[5] and item[4] >= datetime.now().date():            #check not damaged and service date valid
                if item[1] in searchWords and item[2] in searchWords:           #exact match
                    mainMatch = item
                elif item[2] in searchWords:            #alternative match based on type
                    alts.append(item)           #adds all items for alt search

        if mainMatch:
            filteredAlts = []           #later use for finding most expensive
            main_manufacturer = mainMatch[1]            #get manufacturer of mainMatch item

            for i in alts:
                #check if current manufacturer different from main manufacturer
                if i[1] != main_manufacturer:
                    #if different manufacturer, add to filtered list
                    filteredAlts.append(i)

            alts = filteredAlts

        else:
            print("No such item in inventory.")

        if alts:            #check if alts list empty
            mostExpensiveAlt = alts[0]
            for i in alts[1:]:
                if i[3] > mostExpensiveAlt[3]:
                    mostExpensiveAlt = i
        else:
            mostExpensiveAlt = None

        return mainMatch, mostExpensiveAlt
