import database_access               

def main():
    context = database_access.connectToDb()
    cursor = context.cursor()
    patients = database_access.getAllPatients(cursor)
    print(patients)
    studies = database_access.getAllStudies(cursor)
    print(studies)
    database_access.insertExamination(cursor, context, PatientID=1, YawLeft=90, YawRight=90, RollLeft=90, RollRight=90, 
            Study='Местное обследование', StudyNotes='рт.', StudyResult='Здоров',Disease='Шейно-позвоночное растяжение', PatientAge=20, Complaints='Нет', YawLeftPainDegree=2, RiskFactors='Нет')
    database_access.insertExamination(cursor, context, PatientID=2, YawLeft=80, YawRight=85, RollLeft=78, RollRight=70, 
            Study='Местное обследование', StudyNotes='рт.', StudyResult='Растяжение',Disease='Шейно-позвоночное растяжение', PatientAge=45, Complaints='Нет', YawLeftPainDegree=2, RiskFactors='Нет')
    database_access.insertExamination(cursor, context, PatientID=2, YawLeft=80, YawRight=85, RollLeft=78, RollRight=70, 
        Study='Местное обследование', StudyNotes='рт.', StudyResult='Тяжелое состояние',Disease='Шейно-позвоночное растяжение', PatientAge=20, Complaints='Нет', YawLeftPainDegree=1, RiskFactors='Нет')
    database_access.insertExamination(cursor, context, PatientID=4, YawLeft=82, YawRight=84, RollLeft=79, RollRight=70, 
    Study='Местное обследование', StudyNotes='рт.2', StudyResult='Здоров',Disease='Шейно-позвоночное растяжение', PatientAge=20, Complaints='Нет', YawLeftPainDegree=3, RiskFactors='Нет')
    database_access.insertExamination(cursor, context, PatientID=7, YawLeft=70, YawRight=85, RollLeft=78, RollRight=70, 
        Study='Местное обследование', StudyNotes='рт.', StudyResult='Угроза жизни',Disease='Тяжелое ранение в шею', PatientAge=20, Complaints='Нет', RiskFactors='Нет')
    database_access.insertExamination(cursor, context, PatientID=4, YawLeft=70, YawRight=85, RollLeft=78, RollRight=70, 
        Study='Местное обследование', StudyNotes='рт.', StudyResult='Требуется операция',Disease='Перелом', PatientAge=20, Complaints='Нет', RiskFactors='Нет')
    database_access.insertExamination(cursor, context, PatientID=5, YawLeft=83, YawRight=91, RollLeft=76, RollRight=70,         PitchDown=82, PitchUp=71, PitchDownPainDegree=3, PitchDownPainDescription='Режущая',    
        Study='Местное обследование', StudyNotes='рт.', StudyResult='Требуется доп. диагностика ',Disease='Тяжелое ранение в шею', PatientAge=20, Complaints='Нет', RiskFactors='Нет')
    database_access.insertExamination(cursor, context, PatientID=6, YawLeft=83, YawRight=91, RollLeft=76, RollRight=70,         PitchDown=10, PitchUp=71, PitchDownPainDegree=4, PitchDownPainDescription='Режущая',    
        Study='Местное обследование', StudyNotes='рт.', StudyResult='Назначено лечение',Disease='Смещение позвонков', PatientAge=20, Complaints='Нет', RiskFactors='Нет')
    database_access.insertExamination(cursor, context, PatientID=3, YawLeft=83, YawRight=91, RollLeft=76, RollRight=70,         PitchDown=10, PitchUp=71, PitchDownPainDegree=1, RollLeftPainDescription='Ноющая',    
        Study='Местное обследование', StudyNotes='рт.', StudyResult='Назначено лечение',Disease='Замыкание суставов', PatientAge=20, Complaints='Нет', RiskFactors='Нет')
    database_access.insertExamination(cursor, context, PatientID=8, YawLeft=90, YawRight=90, RollLeft=90, RollRight=90,         PitchDown=10, PitchUp=71, PitchDownPainDegree=0, RollLeftPainDescription='Нет',    
        Study='Местное обследование', StudyNotes='рт.', StudyResult='Назначены препараты',Disease='Смещение позвонков', PatientAge=20, Complaints='Нет', RiskFactors='Нет')
    database_access.insertExamination(cursor, context, PatientID=8, YawLeft=90, YawRight=90, RollLeft=90, RollRight=90,         PitchDown=10, PitchUp=71, PitchDownPainDegree=0, RollLeftPainDescription='Нет',    
        Study='Местное обследование', StudyNotes='рт.', StudyResult='Выписан',Disease='Нет', PatientAge=20, Complaints='Нет', RiskFactors='Нет')

if __name__ == '__main__':
    main()