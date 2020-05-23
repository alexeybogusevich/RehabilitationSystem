import database_access               

def main():
    context = database_access.connectToDb()
    cursor = context.cursor()
    users = database_access.getAllCustomers(cursor)
    print(users)

if __name__ == '__main__':
    main()