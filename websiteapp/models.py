import email
from tkinter import CASCADE
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class menus(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, default=0)


class Gender(models.Model):
    title= models.CharField(max_length=25)
    description= models.TextField()

    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Gender Table'
    
    def __str__(self):
        return f"Gender - {self.title} "


class StudentClass(models.Model):
    title= models.CharField(max_length=25)
    description= models.TextField()

    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.title}"
    


class StudentGrade(models.Model):
    title= models.CharField(max_length=25)
    description= models.TextField()

    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.title}"




class Admission(models.Model):
    first_name = models.CharField(default="", max_length=25)
    last_name = models.CharField(default="", max_length=25)
    full_name = models.CharField(default="", max_length=256)
    password = models.CharField(default="", max_length=500)
    student_id = models.CharField(default="", max_length=11)
    fathers_name= models.CharField(default="", max_length=50)
    fathers_mobile= models.CharField(default="", max_length=50)
    mothers_name= models.CharField(default="", max_length=50)
    birth_date = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=14)
    email = models.EmailField()
    admission_fee =models.FloatField(default=0)
    others_fee = models.FloatField(default=0)
    class_name = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    institute = models.CharField(default="", max_length=256)
    total_mark = models.FloatField(default=0)
    grade = models.ForeignKey(StudentGrade, on_delete=models.CASCADE)
    present_address = models.CharField(max_length=256)
    parmanent_address = models.CharField(max_length=256)
    stu_status = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) 
    activate= models.BooleanField(default=False)
    images = models.ImageField(upload_to='images/', blank=True, null=True)

    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Admission'
        verbose_name_plural = 'Student Admission Table'

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.class_name} | {self.mobile}"




class subjectsix(models.Model):
    title = models.CharField(max_length=256)
    descriptions = models.TextField()
    
    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.title}"

class subjectseven(models.Model):
    title = models.CharField(max_length=256)
    descriptions = models.TextField()
    
    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.title}"

class subjecteight(models.Model):
    title = models.CharField(max_length=256)
    descriptions = models.TextField()
    
    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.title}"

class subjectnine(models.Model):
    title = models.CharField(max_length=256)
    descriptions = models.TextField()
    
    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.title}"

class subjectten(models.Model):
    title = models.CharField(max_length=256)
    descriptions = models.TextField()
    
    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.title}"




class stunotes(models.Model):
    classname = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=256)
    descriptions = models.TextField()
    
    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.classname} | {self.subject} | {self.title}"

class stuhomeworks(models.Model):
    classname = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=256)
    descripeditor = RichTextField(blank=True, null=True)


    # descriptions = models.TextField()
    files = models.ImageField(upload_to='images/', blank=True, null=True)

    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.classname} | {self.subject} | {self.title}"
    



    
class teacherregister (models.Model):
    first_name = models.CharField(default="", max_length=25)
    last_name = models.CharField(default="", max_length=25)
    full_name = models.CharField(default="", max_length=256)
    password = models.CharField(max_length=500)
    teacher_id = models.CharField(default="", max_length=11)
    fathers_name= models.CharField(default="", max_length=50)
    fathers_mobile= models.CharField(default="", max_length=50)
    mothers_name= models.CharField(default="", max_length=50)
    birth_date = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=14)
    email = models.EmailField()
    present_address = models.CharField(max_length=256)
    parmanent_address = models.CharField(max_length=256)
    tea_status = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) 
    activate= models.BooleanField(default=False)
    images = models.ImageField(upload_to='images/', blank=True, null=True)

    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'stuadmission'
        verbose_name_plural = 'Student Admission Table'

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.teacher_id} | {self.mobile}"
    

    
class teachereducation(models.Model):
    teacher_id = models.CharField(max_length=12, blank=False, null=False)
    teacher_name = models.CharField(max_length=250, blank=True, null=True)
    institute_name = models.CharField(max_length=250, blank=True, null=True)
    institute_Code = models.CharField(max_length=12, blank=True, null=True)
    department_name = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    contact = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=55, blank=True, null=True)
    admission_date = models.DateField()
    final_exam_date = models.DateField()
    result = models.CharField(max_length=25, blank=True, null=False)
    registration = models.ImageField(upload_to='images/', blank=True, null=True)
    certificate = models.ImageField(upload_to='images/', blank=True, null=True)

    register_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True, auto_now_add=False)


    class Meta:
        verbose_name = 'teachereducation'
        verbose_name_plural = 'Teacher Education Table'

    def __str__(self):
        return f'{self.teacher_name}-{self.institute_name} {self.admission_date} - {self.result}'