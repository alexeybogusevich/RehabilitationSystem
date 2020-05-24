from database_access import *

def main():
    context = connectToDb()
    cursor = context.cursor()
    patients = getAllPatients(cursor)
    print(patients)
    studies = getAllStudies(cursor)
    print(studies)


if __name__ == "__main__":
    main()
