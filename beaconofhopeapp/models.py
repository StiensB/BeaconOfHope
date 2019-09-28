from django.db import models


class CaseWorker(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=75, blank=True, null=True)
    is_active = models.BooleanField()
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'case_worker'
        ordering = ["id"]

    def __str__(self):
        return self.first_name + " " + self.last_name


class CityLinkStatusSource(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city_link_status_source'
        ordering = ["id"]

    def __str__(self):
        return self.name

class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1)
    ssnhash = models.CharField(max_length=72, blank=True, null=True)
    my_salt = models.CharField(max_length=25, blank=True, null=True)
    referral_source = models.ForeignKey('ReferralSource', models.DO_NOTHING, blank=True, null=True)
    city_link_status = models.ForeignKey(CityLinkStatusSource, models.DO_NOTHING, blank=True, null=True)
    staffing_agency = models.ForeignKey('StaffingAgency', models.DO_NOTHING, blank=True, null=True)
    support_contact = models.TextField(blank=True, null=True)
    initial_interviewer = models.ForeignKey(CaseWorker, models.DO_NOTHING, blank=True, null=True)
    lph_resident = models.BooleanField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email_address = models.CharField(max_length=75, blank=True, null=True)
    owns_car = models.BooleanField()
    has_license = models.BooleanField()
    ride_available = models.BooleanField()
    job_interests = models.TextField(blank=True, null=True)
    status = models.ForeignKey('StatusSource', models.DO_NOTHING)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'client'
        ordering = ["id"]

    def __str__(self):
        return self.first_name + " " + self.last_name

class ClientAddress(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    neighborhood = models.ForeignKey('Neighborhood', models.DO_NOTHING, blank=True, null=True)
    is_current = models.BooleanField()
    is_primary = models.BooleanField()
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'client_address'
        ordering = ["id"]

    def __str__(self):
        return self.address1


class ClientCrime(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    crime = models.ForeignKey('Crime', models.DO_NOTHING)
    date_convicted = models.DateField(blank=True, null=True)
    date_released = models.DateField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'client_crime'
        unique_together = (('client', 'crime'),)
        ordering = ["id"]

    def __str__(self):
        return self.crime.name

class ClientFollowUp(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    follow_up = models.TextField()
    target_date = models.DateField()
    date_completed = models.DateField(blank=True, null=True)
    date_archived = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'client_follow_up'
        ordering = ["id"]

    def __str__(self):
        return self.follow_up

class ClientInterest(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    notes = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'client_interest'
        unique_together = (('client', 'company'),)
        ordering = ["id"]

    def __str__(self):
        return self.notes


class ClientInterview(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    interviewer = models.ForeignKey(CaseWorker, models.DO_NOTHING)
    interview_type = models.ForeignKey('InterviewType', models.DO_NOTHING)
    interview_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'client_interview'
        ordering = ["id"]
        
    def __str__(self):
        return self.id


class ClientNote(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    note = models.TextField()
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'client_note'
        ordering = ["id"]
    
    def __str__(self):
        return self.note


class ClientPlacement(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    job = models.ForeignKey('Job', models.DO_NOTHING, blank=True, null=True)
    placement_date = models.DateField(blank=True, null=True)
    exit_date = models.DateField(blank=True, null=True)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'client_placement'
        unique_together = (('client', 'company', 'placement_date'),)
        ordering = ["id"]

    def __str__(self):
        return self.client


class ClientSkill(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    skill = models.ForeignKey('Skill', models.DO_NOTHING)
    details = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'client_skill'
        unique_together = (('client', 'skill'),)
        ordering = ["id"]

    def __str__(self):
        return self.skill.name


class ClientUpdate(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    support_contact = models.TextField(blank=True, null=True)
    lph_resident = models.BooleanField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email_address = models.CharField(max_length=75, blank=True, null=True)
    owns_car = models.BooleanField()
    has_license = models.BooleanField()
    ride_available = models.BooleanField()
    job_interests = models.TextField(blank=True, null=True)
    status = models.ForeignKey('StatusSource', models.DO_NOTHING)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)
    date_processed = models.DateTimeField(blank=True, null=True)
    processed_by = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_update'
        ordering = ["id"]

    def __str__(self):
        return self.client

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    primary_first_name = models.CharField(max_length=50, blank=True, null=True)
    primary_last_name = models.CharField(max_length=50, blank=True, null=True)
    primary_phone = models.CharField(max_length=15, blank=True, null=True)
    primary_email = models.CharField(max_length=75, blank=True, null=True)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    neighborhood = models.ForeignKey('Neighborhood', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)
    date_reviewed = models.DateTimeField(blank=True, null=True)
    reviewed_by = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'
        ordering = ["id"]

    def __str__(self):
        return self.name


class CompanyInterest(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    notes = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    upated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'company_interest'
        unique_together = (('company', 'client'),)
        ordering = ["id"]

    def __str__(self):
        return self.notes


class Crime(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crime'
        ordering = ["id"]

    def __str__(self):
        return self.name


class InterviewType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'interview_type'
        ordering = ["id"]

    def __str__(self):
        return self.name


class Job(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    contact_first_name = models.CharField(max_length=50, blank=True, null=True)
    contact_last_name = models.CharField(max_length=50, blank=True, null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    contact_email = models.CharField(max_length=75, blank=True, null=True)
    date_listed = models.DateTimeField(blank=True, null=True)
    date_filled = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'job'
        ordering = ["id"]

    def __str__(self):
        return self.description


class JobSkill(models.Model):
    id = models.IntegerField(primary_key=True)
    job = models.ForeignKey(Job, models.DO_NOTHING)
    skill = models.ForeignKey('Skill', models.DO_NOTHING)
    details = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'job_skill'
        unique_together = (('job', 'skill'),)
        ordering = ["id"]

    def __str__(self):
        return self.skill.name

class Login(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=75)
    password = models.CharField(max_length=72)
    my_salt = models.CharField(max_length=25)
    login_type = models.CharField(max_length=50)
    inactive_date = models.DateTimeField(blank=True, null=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'login'
        ordering = ["id"]

    def __str__(self):
        return self.user_name


class Neighborhood(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'neighborhood'
        ordering = ["id"]

    def __str__(self):
        return self.name


class PlacementOption(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    job = models.ForeignKey(Job, models.DO_NOTHING, blank=True, null=True)
    ranking = models.IntegerField()
    date_created = models.DateTimeField()
    created_by = models.CharField(max_length=36)
    last_updated = models.DateTimeField()
    updated_by = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'placement_option'
        unique_together = (('client', 'company'),)
        ordering = ["id"]


class ReferralSource(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'referral_source'
        ordering = ["id"]

    def __str__(self):
        return self.name


class Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skill'
        ordering = ["id"]

    def __str__(self):
        return self.name

class StaffingAgency(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staffing_agency'
        ordering = ["id"]

    def __str__(self):
        return self.name

class StateSource(models.Model):
    state_code = models.CharField(primary_key=True, max_length=2)
    state_name = models.CharField(unique=True, max_length=50)
    province = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'state_source'

    def __str__(self):
        return self.state_name

class StatusSource(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    sort_order = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'status_source'
        ordering = ["id"]

    def __str__(self):
        return self.name
