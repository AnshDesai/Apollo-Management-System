from django.db import models

# Create your models here.
class EmpInfo(models.Model):
    plt = models.IntegerField(db_column='PLT', primary_key=True)  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='EMP_ID')  # Field name made lowercase.
    emp_name = models.CharField(db_column='EMP_NAME', max_length=30)  # Field name made lowercase.
    passwd = models.CharField(db_column='PASSWD', max_length=10)  # Field name made lowercase.
    sect = models.CharField(db_column='SECT', max_length=10)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=60, blank=True, null=True)  # Field name made lowercase.
    dept_name = models.CharField(db_column='DEPT_NAME', max_length=25, blank=True, null=True)  # Field name made lowercase.
    gate_dept = models.CharField(db_column='GATE_DEPT', max_length=26, blank=True, null=True)  # Field name made lowercase.
    desg = models.CharField(db_column='DESG', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fgsdev_dept = models.CharField(db_column='FGSDEV_DEPT', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMP_INFO'
        unique_together = (('plt', 'emp_id'),)

class Finyear(models.Model):
    fin_year = models.IntegerField(db_column='FIN_YEAR', primary_key=True)  # Field name made lowercase.
    seq_number = models.IntegerField(db_column='SEQ_NUMBER')  # Field name made lowercase.
    fin = models.CharField(db_column='FIN', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FINYEAR'
