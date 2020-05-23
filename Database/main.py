import pyodbc
import datetime
connectionString = "Provider=SQLOLEDB.1;Integrated Security=SSPI;Persist Security Info=False;Data Source=IDEA-PC;Initial Catalog=HeadRotationClinic;"

#IN CASE OF PROBLEMS MAKE CONTEXT AS AN ARGUMENT OF EACH FUNCTION

def connectToDb():
    server = 'IDEA-PC' 
    database = 'HeadRotationClinic' 
    username = 'vrach' 
    password = 'vrach' 
    context = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return context
    #cursor.execute('SELECT * FROM dbo.tblUsers')
    #while row is not None:
    #   print(row)
    #   row = cursor.fetchone()

context = connectToDb()
cursor = context.cursor()

def retrieveCustomerById(id):
    cursor.execute("""
                    SELECT * 
                    FROM dbo.tblUsers 
                    WHERE ID = {}
                    """
                    .format(id))
    return cursor.fetchone()

def retrieveCustomerByUserName(UserName):
    cursor.execute("""
                    SELECT * 
                    FROM dbo.tblUsers 
                    WHERE UserName = '{}'
                    """
                    .format(UserName))
    return cursor.fetchone()

def insertCustomer(UserName, UserPassword='', UserRole='', UserFullName='', 
                    UserBirthDate=datetime.datetime(1980, 1, 1, 0, 0, 0), UserPhone='', UserEmail='',
                    OfficeNumber='', Prefix='', Title='', Speciality='', Department='', Division='', 
                    Supervisor='', AddTime='', LastLoginTime=datetime.datetime.now(),
                    LastLogoutTime=datetime.datetime.now(), Dead=False, PhotoPic=None):
    cursor.execute('''
                    INSERT 
                    INTO dbo.tblUsers
                        (
                        UserName, 
                        UserPassword, 
                        UserRole, 
                        UserFullName,  
                        UserBirthDate, 
                        UserPhone, 
                        UserEmail,
                        OfficeNumber, 
                        Prefix, 
                        Title, 
                        Speciality, 
                        Department, 
                        Division, 
                        Supervisor, 
                        AddTime, 
                        LastLoginTime,
                        LastLogoutTime, 
                        Dead, 
                        PhotoPic
                        ) 
                        VALUES
                        ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',
                        '{}','{}','{}')
                        '''
                    .format(
                    UserName,UserPassword,UserRole,UserFullName,
                    UserBirthDate.strftime("%Y-%m-%d %H:%M:%S"),UserPhone,UserEmail,
                    OfficeNumber,Prefix,Title,Speciality,Department,Division,
                    Supervisor,AddTime,LastLoginTime.strftime("%Y-%m-%d %H:%M:%S"),
                    LastLogoutTime.strftime("%Y-%m-%d %H:%M:%S"),Dead,PhotoPic))  
    context.commit()   

def updateCustomer(id, UserName='', UserPassword='', UserRole='', UserFullName='', 
                    UserBirthDate=None, UserPhone='', UserEmail='',
                    OfficeNumber='', Prefix='', Title='', Speciality='', Department='', Division='', 
                    Supervisor='', AddTime='', LastLoginTime=None,
                    LastLogoutTime=None, Dead=False, PhotoPic=None):
    if(UserName==''):
        UserName = retrieveCustomerById(id)[1]
    heads = '\''
    if(UserName!=''):
        UserNameValue='UserName='+heads+UserName+heads
    UserPasswordValue=''
    if(UserPassword!=''):
        UserPasswordValue=',UserPassword='+heads+UserPassword+heads
    UserRoleValue=''
    if(UserRole!=''):
        UserRoleValue=',UserRole='+heads+UserRole+heads
    UserFullNameValue=''
    if(UserFullName!=''):
        UserFullNameValue=',UserFullName='+heads+UserFullName+heads
    UserBirthDateValue=''
    if(UserBirthDate!=None):
        UserBirthDateValue=',UserBirthDate='+heads+UserBirthDate.strftime("%Y-%m-%d %H:%M:%S")+heads
    UserPhoneValue=''
    if(UserPhone!=''):
        UserPhoneValue=',UserPhone='+heads+UserPhone+heads
    UserEmailValue=''
    if(UserEmail!=''):
        UserEmailValue=',UserEmail='+heads+UserEmail+heads
    OfficeNumberValue=''
    if(OfficeNumber!=''):
        OfficeNumberValue=',OfficeNumber='+heads+OfficeNumber+heads
    PrefixValue=''
    if(Prefix!=''):
        PrefixValue=',Prefix='+heads+Prefix+heads
    TitleValue=''
    if(Title!=''):
        TitleValue=',Title='+heads+Title+heads
    SpecialityValue=''
    if(Speciality!=''):
        SpecialityValue=',Speciality='+heads+Speciality+heads
    DepartmentValue=''
    if(Department!=''):
        DepartmentValue=',Department='+heads+Department+heads
    DivisionValue=''
    if(Division!=''):
        DivisionValue=',Division='+heads+Division+heads
    SupervisorValue=''
    if(Supervisor!=''):
        SupervisorValue=',Supervisor='+heads+Supervisor+heads
    AddTimeValue=''
    if(AddTime!=''):
        AddTimeValue=',AddTime='+heads+AddTime+heads
    LastLoginTimeValue=''
    if(LastLoginTime!=None):
        LastLoginTimeValue=',LastLoginTime='+heads+LastLoginTimeValue.strftime("%Y-%m-%d %H:%M:%S")+heads
    LastLogoutTimeValue=''
    if(LastLogoutTime!=None):
        LastLogoutTimeValue=',LastLoginTime='+heads+LastLogoutTimeValue.strftime("%Y-%m-%d %H:%M:%S")+heads
    DeadValue=False
    if(Dead!=False):
        DeadValue=',Dead= -1 '
    PhotoPicValue=''
    if(PhotoPic!=None):
        PhotoPicValue=',PhotoPic='+PhotoPic
    Query='''
                    UPDATE dbo.tblUsers
                    SET
                        {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
                    WHERE Id={}
        '''.format(UserNameValue, UserPasswordValue, UserRoleValue, UserFullNameValue,
            UserBirthDateValue, UserPhoneValue, UserEmailValue, OfficeNumberValue, PrefixValue, 
            TitleValue, SpecialityValue, DepartmentValue, DivisionValue, SupervisorValue, 
            AddTimeValue, LastLoginTimeValue, LastLogoutTimeValue, DeadValue, PhotoPicValue, id)
    #print(Query)
    cursor.execute(Query) 
    context.commit()                  

def retrieveCustomerStudies(id):
    cursor.execute("""
                    SELECT * 
                    FROM dbo.tblStudies 
                    WHERE PatientID = '{}'
                    """
                    .format(id))
    return cursor.fetchone()

def insertStudy(Study='',StudyType='',StudyDate=datetime.datetime.now(),Disease='',StudyResult='', StudyWay='',
                StudyNotes='',Drugs='',PatientID='NULL', PatientAge='NULL',Doctor='',Price='NULL',
                Device='', Method='', System='', StudyFile='', Department='',
                Complaints='', RiskFactors='', MinRotation='NULL', MaxRotation='NULL', 
                AvgRotation='NULL', Repeats='NULL'):
    query='''
                    INSERT 
                    INTO dbo.tblStudies
                        (
                        Study, 
                        StudyType, 
                        StudyDate, 
                        Disease,  
                        StudyResult, 
                        StudyNotes, 
                        Drugs,
                        PatientID, 
                        PatientAge, 
                        Doctor, 
                        Price, 
                        Device, 
                        Method, 
                        System, 
                        StudyFile, 
                        Department,
                        Complaints, 
                        RiskFactors, 
                        MinRotation,
                        MaxRotation,
                        AvgRotation,
                        Repeats
                        ) 
                        VALUES
                        ('{}','{}','{}','{}','{}','{}','{}',{},{},'{}',{},'{}','{}','{}','{}','{}',
                        '{}','{}',{}, {}, {}, {})
                        '''.format(
                    Study,StudyType,StudyDate.strftime("%Y-%m-%d %H:%M:%S"),Disease,
                    StudyResult,StudyNotes,Drugs,
                    PatientID,PatientAge,Doctor,Price,Device,Method,
                    System,StudyFile,Department,Complaints,RiskFactors,
                    MinRotation,MaxRotation,AvgRotation,Repeats)
    print(query)
    cursor.execute(query)  
    context.commit()               

def main():
    customer = retrieveCustomerById(1)
    #print(customer)
    #insertCustomer('testUser','password','doctor',Title='doctor')
    #testCustomer = retrieveCustomerByUserName('testUser')
    #updateCustomer(testCustomer[0],Dead=True)
    #print(testCustomer)
    #insertStudy(MinRotation=90)

if __name__ == '__main__':
    main()