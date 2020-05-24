import pyodbc
import datetime
import os
import json
import sys
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def connectToDb():
    connectionString = os.environ.get("azureSqlDb")
    context = pyodbc.connect(connectionString)
    return context


def getUserById(cursor, id):
    cursor.execute(
        """
                    SELECT * 
                    FROM dbo.tblUsers 
                    WHERE ID = {}
                    """.format(
            id
        )
    )
    return cursor.fetchone()


def getPatientById(cursor, id):
    cursor.execute(
        """
                    SELECT * 
                    FROM dbo.tblMain 
                    WHERE ID = {}
                    """.format(
            id
        )
    )
    return cursor.fetchone()


def getUserByName(cursor, UserName):
    cursor.execute(
        """
                    SELECT * 
                    FROM dbo.tblUsers 
                    WHERE UserName = '{}'
                    """.format(
            UserName
        )
    )
    return cursor.fetchone()


def getPatientByName(cursor, name):
    cursor.execute(
        """
                    SELECT * 
                    FROM dbo.tblMain 
                    WHERE Patient = {}
                    """.format(
            name
        )
    )
    return cursor.fetchone()


def getAllUsers(cursor):
    cursor.execute(
        """
                    SELECT * 
                    FROM dbo.tblUsers 
                    """
    )
    return cursor.fetchall()


def getAllPatients(cursor):
    cursor.execute(
        """
                    SELECT * 
                    FROM dbo.tblMain 
                    """
    )
    return cursor.fetchall()


def getAllStudies(cursor):
    cursor.execute(
        """
                    SELECT * 
                    FROM dbo.tblStudies 
                    """
    )
    return cursor.fetchall()


def insertUser(
    cursor,
    context,
    UserName,
    UserPassword="",
    UserRole="",
    UserFullName="",
    UserBirthDate=datetime.datetime(1980, 1, 1, 0, 0, 0),
    UserPhone="",
    UserEmail="",
    OfficeNumber="",
    Prefix="",
    Title="",
    Speciality="",
    Department="",
    Division="",
    Supervisor="",
    AddTime="",
    LastLoginTime=datetime.datetime.now(),
    LastLogoutTime=datetime.datetime.now(),
    Dead=False,
    PhotoPic=None,
):
    cursor.execute(
        """
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
                        """.format(
            UserName,
            UserPassword,
            UserRole,
            UserFullName,
            UserBirthDate.strftime("%Y-%m-%d %H:%M:%S"),
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
            LastLoginTime.strftime("%Y-%m-%d %H:%M:%S"),
            LastLogoutTime.strftime("%Y-%m-%d %H:%M:%S"),
            Dead,
            PhotoPic,
        )
    )
    context.commit()


def updateUser(
    cursor,
    context,
    id,
    UserName="",
    UserPassword="",
    UserRole="",
    UserFullName="",
    UserBirthDate=None,
    UserPhone="",
    UserEmail="",
    OfficeNumber="",
    Prefix="",
    Title="",
    Speciality="",
    Department="",
    Division="",
    Supervisor="",
    AddTime="",
    LastLoginTime=None,
    LastLogoutTime=None,
    Dead=False,
    PhotoPic=None,
):
    if UserName == "":
        UserName = retrieveCustomerById(id)[1]
    heads = "'"
    if UserName != "":
        UserNameValue = "UserName=" + heads + UserName + heads
    UserPasswordValue = ""
    if UserPassword != "":
        UserPasswordValue = ",UserPassword=" + heads + UserPassword + heads
    UserRoleValue = ""
    if UserRole != "":
        UserRoleValue = ",UserRole=" + heads + UserRole + heads
    UserFullNameValue = ""
    if UserFullName != "":
        UserFullNameValue = ",UserFullName=" + heads + UserFullName + heads
    UserBirthDateValue = ""
    if UserBirthDate != None:
        UserBirthDateValue = (
            ",UserBirthDate="
            + heads
            + UserBirthDate.strftime("%Y-%m-%d %H:%M:%S")
            + heads
        )
    UserPhoneValue = ""
    if UserPhone != "":
        UserPhoneValue = ",UserPhone=" + heads + UserPhone + heads
    UserEmailValue = ""
    if UserEmail != "":
        UserEmailValue = ",UserEmail=" + heads + UserEmail + heads
    OfficeNumberValue = ""
    if OfficeNumber != "":
        OfficeNumberValue = ",OfficeNumber=" + heads + OfficeNumber + heads
    PrefixValue = ""
    if Prefix != "":
        PrefixValue = ",Prefix=" + heads + Prefix + heads
    TitleValue = ""
    if Title != "":
        TitleValue = ",Title=" + heads + Title + heads
    SpecialityValue = ""
    if Speciality != "":
        SpecialityValue = ",Speciality=" + heads + Speciality + heads
    DepartmentValue = ""
    if Department != "":
        DepartmentValue = ",Department=" + heads + Department + heads
    DivisionValue = ""
    if Division != "":
        DivisionValue = ",Division=" + heads + Division + heads
    SupervisorValue = ""
    if Supervisor != "":
        SupervisorValue = ",Supervisor=" + heads + Supervisor + heads
    AddTimeValue = ""
    if AddTime != "":
        AddTimeValue = ",AddTime=" + heads + AddTime + heads
    LastLoginTimeValue = ""
    if LastLoginTime != None:
        LastLoginTimeValue = (
            ",LastLoginTime="
            + heads
            + LastLoginTimeValue.strftime("%Y-%m-%d %H:%M:%S")
            + heads
        )
    LastLogoutTimeValue = ""
    if LastLogoutTime != None:
        LastLogoutTimeValue = (
            ",LastLoginTime="
            + heads
            + LastLogoutTimeValue.strftime("%Y-%m-%d %H:%M:%S")
            + heads
        )
    DeadValue = False
    if Dead != False:
        DeadValue = ",Dead= -1 "
    PhotoPicValue = ""
    if PhotoPic != None:
        PhotoPicValue = ",PhotoPic=" + PhotoPic
    Query = """
                    UPDATE dbo.tblUsers
                    SET
                        {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
                    WHERE Id={}
        """.format(
        UserNameValue,
        UserPasswordValue,
        UserRoleValue,
        UserFullNameValue,
        UserBirthDateValue,
        UserPhoneValue,
        UserEmailValue,
        OfficeNumberValue,
        PrefixValue,
        TitleValue,
        SpecialityValue,
        DepartmentValue,
        DivisionValue,
        SupervisorValue,
        AddTimeValue,
        LastLoginTimeValue,
        LastLogoutTimeValue,
        DeadValue,
        PhotoPicValue,
        id,
    )
    # print(Query)
    cursor.execute(Query)
    context.commit()


def getPatientExamination(cursor, id):
    cursor.execute(
        """
                    SELECT * 
                    FROM dbo.tblStudies 
                    WHERE PatientID = '{}'
                    """.format(
            id
        )
    )
    return cursor.fetchone()


def getLastNotNullPatientYawLeftExamination(cursor, id):
    rows_count = cursor.execute(
        """
                SELECT TOP 1 * 
                FROM dbo.tblStudies 
                WHERE PatientID = '{}' AND YawLeft IS NOT NULL
                ORDER BY StudyDate DESC
                """.format(
            id
        )
    )
    if rows_count == 0:
        return None
    return cursor.fetchone()


def getLastNotNullPatientYawRightExamination(cursor, id):
    rows_count = cursor.execute(
        """
                SELECT TOP 1 * 
                FROM dbo.tblStudies 
                WHERE PatientID = '{}' AND YawRight IS NOT NULL
                ORDER BY StudyDate DESC
                """.format(
            id
        )
    )
    if rows_count == 0:
        return None
    return cursor.fetchone()


def getLastNotNullPatientPitchDownExamination(cursor, id):
    rows_count = cursor.execute(
        """
                SELECT TOP 1 * 
                FROM dbo.tblStudies 
                WHERE PatientID = '{}' AND PitchDown IS NOT NULL
                ORDER BY StudyDate DESC
                """.format(
            id
        )
    )
    if rows_count == 0:
        return None
    return cursor.fetchone()


def getLastNotNullPatientPitchUpExamination(cursor, id):
    rows_count = cursor.execute(
        """
                SELECT TOP 1 * 
                FROM dbo.tblStudies 
                WHERE PatientID = '{}' AND PitchUp IS NOT NULL
                ORDER BY StudyDate DESC
                """.format(
            id
        )
    )
    if rows_count == 0:
        return None
    return cursor.fetchone()


def getLastNotNullPatientRollLeftExamination(cursor, id):
    rows_count = cursor.execute(
        """
                SELECT TOP 1 * 
                FROM dbo.tblStudies 
                WHERE PatientID = '{}' AND RollLeft IS NOT NULL
                ORDER BY StudyDate DESC
                """.format(
            id
        )
    )
    if rows_count == 0:
        return None
    return cursor.fetchone()


def getLastNotNullPatientRollRightExamination(cursor, id):
    rows_count = cursor.execute(
        """
                SELECT TOP 1 * 
                FROM dbo.tblStudies 
                WHERE PatientID = '{}' AND RollRight IS NOT NULL
                ORDER BY StudyDate DESC
                """.format(
            id
        )
    )
    if rows_count == 0:
        return None
    return cursor.fetchone()


def insertExamination(
    cursor,
    context,
    Study="Местное обследование",
    StudyType="Голова",
    StudyDate=datetime.datetime.now(),
    Disease="",
    StudyResult="",
    StudyWay="Стандартная",
    StudyNotes="Нет",
    Drugs="Нет",
    PatientID="NULL",
    PatientAge="NULL",
    Doctor="",
    Price="NULL",
    Device="Система реаблитации КНУ",
    Method="Дигностика",
    System="RS",
    StudyFile="",
    Department="КНУ",
    Complaints="Нет",
    RiskFactors="Нет",
    PitchDown="NULL",
    PitchUp="NULL",
    YawLeft="NULL",
    YawRight="NULL",
    RollLeft="NULL",
    RollRight="NULL",
    PitchDownPainDegree="NULL",
    PitchDownPainDescription="",
    PitchDownPainDynamics="",
    PitchDownTriggerSpots="",
    PitchUpPainDegree="NULL",
    PitchUpPainDescription="",
    PitchUpPainDynamics="",
    PitchUpTriggerSpots="",
    YawLeftPainDegree="NULL",
    YawLeftPainDescription="",
    YawLeftPainDynamics="",
    YawLeftTriggerSpots="",
    YawRightPainDegree="NULL",
    YawRightPainDescription="",
    YawRightPainDynamics="",
    YawRightTriggerSpots="",
    RollLeftPainDegree="NULL",
    RollLeftPainDescription="",
    RollLeftPainDynamics="",
    RollLeftTriggerSpots="",
    RollRightPainDegree="NULL",
    RollRightPainDescription="",
    RollRightPainDynamics="",
    RollRightTriggerSpots="",
    YawLeftRotationDynamics="",
    YawRightRotationDynamics="",
    RollLeftRotationDynamics="",
    RollRightRotationDynamics="",
    PitchDownRotationDynamics="",
    PitchUpRotationDynamics="",
):
    if PatientID != "":
        if PitchDown != "NULL":
            previousExamination = getLastNotNullPatientPitchDownExamination(
                cursor, PatientID
            )
            if previousExamination != None:
                previousResult = previousExamination[20]
                if int(previousResult) > int(PitchDown):
                    PitchDownRotationDynamics = "Негативная"
                elif int(previousResult) == int(PitchDown):
                    PitchDownRotationDynamics = "Без изменений"
                else:
                    PitchDownRotationDynamics = "Позитивная"
        if PitchUp != "NULL":
            previousExamination = getLastNotNullPatientPitchUpExamination(
                cursor, PatientID
            )
            if previousExamination != None:
                previousResult = previousExamination[21]
                if int(previousResult) > int(PitchUp):
                    PitchUpRotationDynamics = "Негативная"
                elif int(previousResult) == int(PitchUp):
                    PitchUpRotationDynamics = "Без изменений"
                else:
                    PitchUpRotationDynamics = "Позитивная"
        if RollLeft != "NULL":
            previousExamination = getLastNotNullPatientRollLeftExamination(
                cursor, PatientID
            )
            if previousExamination != None:
                previousResult = previousExamination[24]
                if int(previousResult) > int(RollLeft):
                    RollLeftRotationDynamics = "Негативная"
                elif int(previousResult) == int(RollLeft):
                    RollLeftRotationDynamics = "Без изменений"
                else:
                    RollLeftRotationDynamics = "Позитивная"
        if RollRight != "NULL":
            previousExamination = getLastNotNullPatientRollRightExamination(
                cursor, PatientID
            )
            if previousExamination != None:
                previousResult = previousExamination[25]
                if int(previousResult) > int(RollRight):
                    RollRightRotationDynamics = "Негативная"
                elif int(previousResult) == int(RollRight):
                    RollRightRotationDynamics = "Без изменений"
                else:
                    RollRightRotationDynamics = "Позитивная"
        if YawLeft != "NULL":
            previousExamination = getLastNotNullPatientYawLeftExamination(
                cursor, PatientID
            )
            if previousExamination != None:
                previousResult = previousExamination[22]
                if int(previousResult) > int(YawLeft):
                    YawLeftRotationDynamics = "Негативная"
                elif int(previousResult) == int(YawLeft):
                    YawLeftRotationDynamics = "Без изменений"
                else:
                    YawLeftRotationDynamics = "Позитивная"
        if YawRight != "NULL":
            previousExamination = getLastNotNullPatientYawRightExamination(
                cursor, PatientID
            )
            if previousExamination != None:
                previousResult = previousExamination[23]
                if int(previousResult) > int(YawRight):
                    YawRightRotationDynamics = "Негативная"
                elif int(previousResult) == int(YawRight):
                    YawRightRotationDynamics = "Без изменений"
                else:
                    YawRightRotationDynamics = "Позитивная"

    query = """
                    INSERT 
                    INTO dbo.tblStudies
                        (
                        Study, 
                        StudyType, 
                        StudyDate, 
                        StudyWay,
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
                        RollRightTriggerSpots,
                        YawLeftRotationDynamics,
                        YawRightRotationDynamics,
                        RollLeftRotationDynamics,
                        RollRightRotationDynamics,
                        PitchDownRotationDynamics,
                        PitchUpRotationDynamics
                        ) 
                        VALUES
                        ('{}','{}','{}','{}','{}','{}','{}','{}',{},{},'{}',{},'{}','{}','{}','{}','{}',
                        '{}','{}',{}, {}, {}, {}, {}, {}, 
                        {},'{}','{}','{}',
                        {},'{}','{}','{}',
                        {},'{}','{}','{}',
                        {},'{}','{}','{}',
                        {},'{}','{}','{}',
                        {},'{}','{}','{}',
                        '{}','{}','{}','{}','{}','{}')
                        """.format(
        Study,
        StudyType,
        StudyDate.strftime("%Y-%m-%d %H:%M:%S"),
        StudyWay,
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
        RollRightTriggerSpots,
        YawLeftRotationDynamics,
        YawRightRotationDynamics,
        RollLeftRotationDynamics,
        RollRightRotationDynamics,
        PitchDownRotationDynamics,
        PitchUpRotationDynamics,
    )
    # print(query)
    cursor.execute(query)
    context.commit()
