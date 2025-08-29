# student (id,name,department ,domain)[set_student(),display_students()]


class Student:

    id:int

    name:str

    department:str

    domain:str

    def set_student(self,id,name,department,domain):

        self.id =  id

        self.name = name

        self.department = department

        self.domain = domain

    def display_student(self):
      
      print(self.id,self.name,self.department,self.domain)

student_instance1 = Student()

student_instance2 = Student()

student_instance1.set_student(1,"dona","CS","AI")

student_instance1.display_student()

student_instance2.set_student(2,"Anagha","CS","ML")

student_instance2.display_student()




# super heros [name,movie,year,series type](set_superheros(),display_superheros())

class SuperHero:
   
   name:str

   movie:str

   year:int

   seriesType:str

   def set_superheros(self,name,movie,year,seriesType):
      self.name = name

      self.movie = movie

      self.year = year

      self.seriesType = seriesType

   def display_superheros(self):
         
         print(  self.name,self.movie,  self.year,  self.year)

superhero_instamce1 = SuperHero()

superhero_instamce2 = SuperHero()

superhero_instamce1.set_superheros("Iron Man","Iron Man 3",2018, "Avengers series")

superhero_instamce1.display_superheros()

superhero_instamce2.set_superheros("Captain America","Winter Soldier",2004,"Avengers series")

superhero_instamce2.display_superheros()






