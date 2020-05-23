import database_access               

def main():
    context = database_access.connectToDb()
    cursor = context.cursor()
    users = database_access.getAllCustomers(cursor)
    print(users)
    studies = database_access.getAllStudies(cursor)
    print(studies)
    #database_access.insertExamination(cursor, context, PatientID=1, YawLeft=90)

if __name__ == '__main__':
    main()