from student import Student

def leggTilStudent(student_dict):
    ny_stud=input("Hva er navnet paa den nye studenten? ")
    ny_studbrukernavn=input("Hva er brukernavnet paa den nye studenten? ")
    ny_stud_tlf=input("Hva er tlfnummer til studenten? ")
    student_dict[ny_stud]=Student(ny_stud,ny_studbrukernavn,ny_stud_tlf)

def main():
    stud_dict={}
    stud_dict["Geir"]=Student("Geir Turtum","geirtur","47837303")
    stud_dict["Eirin"]=Student("Eirin Korvald","eirinko","47332999")
    stud_dict["Karl"]=Student("Karl","karl","99999999")

    for key in stud_dict:
        stud_dict[key].printInfo()
        
    istud_dict=input("Hvilken student vil du soke etter? ")
    
    if istud_dict in stud_dict:
        print(istud_dict,"finnes i systemet.")
        stud_dict[istud_dict].printInfo()
    else:
        print(istud_dict,"finnes ikke i systemet.")

    leggTilStudent(stud_dict)

main()
