import database_access               

def main():
    context = database_access.connectToDb()
    cursor = context.cursor()
    users = database_access.getAllCustomers(cursor)
    print(users)
    database_access.insertExamination(cursor, context, PatientID=1, YawLeft=80)

if __name__ == '__main__':
    main()