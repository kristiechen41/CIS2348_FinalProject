from FinalProjectClass import InventoryManager

def main():
    inventoryManager = InventoryManager()
    inventoryManager.loadData('FinalProjectServiceDatesList.txt')

    searchInpt = ""

    while searchInpt.lower() != 'q':
        searchInpt = input("Enter the item type and manufacturer, or 'q' to quit: ").strip()

        if searchInpt.lower() == 'q':
            break

        primaryItem, alternative = inventoryManager.search(searchInpt)

        if primaryItem:
            print("Your item is:", primaryItem[0], primaryItem[1].title(), primaryItem[2].title(), "$" + str(primaryItem[3]))
        if alternative:
            print("You may also consider:", alternative[0], alternative[1].title(), alternative[2].title(), "$" + str(alternative[3]))


if __name__ == "__main__":
    main()