import pyodbc
import datetime
import os
import json
import sys

def connectToDb():
    server = 'tcp:knurehabilitation.database.windows.net,1433' 
    database = 'HeadRotationClinic' 
    username = 'master' 
    password = '8juc68hnr5JhgbzMLOGf' 
    f = open(os.path.join(sys.path[0], "app.settings.json"), "r")
    appsettings = json.loads(f.read())
    connectionString = appsettings['ConnectionStrings']['azureSqlDb']
    context = pyodbc.connect(connectionString)
    return context

def getCustomerById(cursor, id):
    cursor.execute("""
                    SELECT * 
                    FROM dbo.tblUsers 
                    WHERE ID = {}
                    """
                    .format(id))
    return cursor.fetchone()

def getCustomerByName(cursor, UserName):
    cursor.execute("""
                    SELECT * 
                    FROM dbo.tblUsers 
                    WHERE UserName = '{}'
                    """
                    .format(UserName))
    return cursor.fetchone()

def getAllCustomers(cursor):
    cursor.execute("""
                    SELECT * 
                    FROM dbo.tblUsers 
                    """
                    )
    return cursor.fetchone()

def insertCustomer(cursor, context, UserName, UserPassword='', UserRole='', UserFullName='', 
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

def updateCustomer(cursor, context, id, UserName='', UserPassword='', UserRole='', UserFullName='', 
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

def getCustomerExaminations(cursor, id):
    cursor.execute("""
                    SELECT * 
                    FROM dbo.tblStudies 
                    WHERE PatientID = '{}'
                    """
                    .format(id))
    return cursor.fetchone()

def insertExamination(cursor, context, Study='',StudyType='',StudyDate=datetime.datetime.now(),Disease='',StudyResult='', StudyWay='',
                StudyNotes='',Drugs='',PatientID='NULL', PatientAge='NULL',Doctor='',Price='NULL',
                Device='', Method='', System='', StudyFile='', Department='',
                Complaints='', RiskFactors='', 
                PitchDown='NULL', PitchUp='NULL', 
                YawLeft='NULL', YawRight='NULL',
                RollLeft='NULL',RollRight='NULL',
                PitchDownPainDegree='NULL',PitchDownPainDescription='',PitchDownPainDynamics='', PitchDownTriggerSpots='',
                PitchUpPainDegree='NULL',PitchUpPainDescription='',PitchUpPainDynamics='',PitchUpTriggerSpots='',
                YawLeftPainDegree='NULL',YawLeftPainDescription='',YawLeftPainDynamics='',YawLeftTriggerSpots='',
                YawRightPainDegree='NULL', YawRightPainDescription='', YawRightPainDynamics='', YawRightTriggerSpots='',
                RollLeftPainDegree='NULL', RollLeftPainDescription='', RollLeftPainDynamics='', RollLeftTriggerSpots='',
                RollRightPainDegree='NULL',RollRightPainDescription='',RollRightPainDynamics='', RollRightTriggerSpots=''):
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
                        PitchDown,
                        PitchUp,
                        YawLeft,
                        YawRight,
                        RollLeft,
                        RollRight,
                        PitchDownPainDegree,
                        PitchDownPainDescription,
                        PitchDownPainDynamics,
                        PitchDownTriggerSpots,
                        PitchUpPainDegree,
                        PitchUpPainDescription,
                        PitchUpPainDynamics,
                        PitchUpTriggerSpots,
                        YawLeftPainDegree,
                        YawLeftPainDescription,
                        YawLeftPainDynamics,
                        YawLeftTriggerSpots,
                        YawRightPainDegree,
                        YawRightPainDescription,
                        YawRightPainDynamics,
                        YawRightTriggerSpots,
                        RollLeftPainDegree,
                        RollLeftPainDescription,
                        RollLeftPainDynamics,
                        RollLeftTriggerSpots,
                        RollRightPainDegree,
                        RollRightPainDescription,
                        RollRightPainDynamics,
                        RollRightTriggerSpots
                        ) 
                        VALUES
                        ('{}','{}','{}','{}','{}','{}','{}',{},{},'{}',{},'{}','{}','{}','{}','{}',
                        '{}','{}',{}, {}, {}, {}, {}, {}, 
                        {},'{}','{}','{}',
                        {},'{}','{}','{}',
                        {},'{}','{}','{}',
                        {},'{}','{}','{}',
                        {},'{}','{}','{}',
                        {},'{}','{}','{}')
                        '''.format(
                    Study,StudyType,StudyDate.strftime("%Y-%m-%d %H:%M:%S"),Disease,
                    StudyResult,StudyNotes,Drugs,
                    PatientID,PatientAge,Doctor,Price,Device,Method,
                    System,StudyFile,Department,Complaints,RiskFactors,
                    PitchDown, PitchUp, YawLeft, YawRight, RollLeft, RollRight,
                    PitchDownPainDegree, PitchDownPainDescription, PitchDownPainDynamics, PitchDownTriggerSpots,
                    PitchUpPainDegree, PitchUpPainDescription, PitchUpPainDynamics, PitchUpTriggerSpots,
                    YawLeftPainDegree, YawLeftPainDescription, YawLeftPainDynamics, YawLeftTriggerSpots,
                    YawRightPainDegree, YawRightPainDescription, YawRightPainDynamics, YawRightTriggerSpots,
                    RollLeftPainDegree, RollLeftPainDescription, RollLeftPainDynamics, RollLeftTriggerSpots,
                    RollRightPainDegree, RollRightPainDescription, RollRightPainDynamics, RollRightTriggerSpots)
    print(query)
    cursor.execute(query)  
    context.commit()   