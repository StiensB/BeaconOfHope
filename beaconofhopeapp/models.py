from django.db import models


class CaseWorker(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    firstName = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    lastName = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=75, blank=True, null=True)  # Field name made lowercase.
    isActive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdate = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedby = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CaseWorker'

    def __str__(self):
        return self.firstName + " " + self.lastName


class CityLinkStatusSource(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=100)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CityLinkStatusSource'

    def __str__(self):
        return self.name

class Client(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    firstName = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    lastName = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    dateOfBirth = models.DateField(db_column='DateOfBirth', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1)  # Field name made lowercase.
    ssnHash = models.CharField(db_column='SSNHash', max_length=72, blank=True, null=True)  # Field name made lowercase.
    mySalt = models.CharField(db_column='MySalt', max_length=25, blank=True, null=True)  # Field name made lowercase.
    referralSourceId = models.CharField(db_column='ReferralSourceId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    citylinkStatusId = models.CharField(db_column='CityLinkStatusId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    staffingAgencyId = models.CharField(db_column='StaffingAgencyId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    supportContact = models.TextField(db_column='SupportContact', blank=True, null=True)  # Field name made lowercase.
    initialInterviewerId = models.CharField(db_column='InitialInterviewerId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    lphResident = models.BooleanField(db_column='LPHResident')  # Field name made lowercase.
    phoneNumber = models.CharField(db_column='PhoneNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    emailAddress = models.CharField(db_column='EmailAddress', max_length=75, blank=True, null=True)  # Field name made lowercase.
    ownsCar = models.BooleanField(db_column='OwnsCar')  # Field name made lowercase.
    hasLicense = models.BooleanField(db_column='HasLicense')  # Field name made lowercase.
    rideAvailable = models.BooleanField(db_column='RideAvailable')  # Field name made lowercase.
    jobInterests = models.TextField(db_column='JobInterests', blank=True, null=True)  # Field name made lowercase.
    statusId = models.CharField(db_column='StatusId', max_length=36)  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Client'

    def __str__(self):
        return self.firstName + " " + self.lastName


class ClientAddress(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clientId = models.CharField(db_column='ClientId', max_length=36)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=50)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2)  # Field name made lowercase.
    zipCode = models.CharField(db_column='ZipCode', max_length=10)  # Field name made lowercase.
    neighborhoodId = models.CharField(db_column='NeighborhoodId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    isCurrent = models.BooleanField(db_column='IsCurrent')  # Field name made lowercase.
    isPrimary = models.BooleanField(db_column='IsPrimary')  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientAddress'

    def __str__(self):
        return self.address1


class ClientCrime(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clientId = models.CharField(db_column='ClientId', max_length=36)  # Field name made lowercase.
    crimeId = models.CharField(db_column='CrimeId', max_length=36)  # Field name made lowercase.
    dateConvicted = models.DateField(db_column='DateConvicted', blank=True, null=True)  # Field name made lowercase.
    dateReleased = models.DateField(db_column='DateReleased', blank=True, null=True)  # Field name made lowercase.
    details = models.TextField(db_column='Details', blank=True, null=True)  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientCrime'
        unique_together = (('clientId', 'crimeId'),)

    def __str__(self):
        return self.crimeId.name


class ClientFollowUp(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clientId = models.CharField(db_column='ClientId', max_length=36)  # Field name made lowercase.
    followUp = models.TextField(db_column='FollowUp')  # Field name made lowercase.
    targetDate = models.DateField(db_column='TargetDate')  # Field name made lowercase.
    dateCompleted = models.DateField(db_column='DateCompleted', blank=True, null=True)  # Field name made lowercase.
    dateArchived = models.DateTimeField(db_column='DateArchived', blank=True, null=True)  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientFollowUp'

    def __str__(self):
        return self.followUp

class ClientInterest(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clientId = models.CharField(db_column='ClientId', max_length=36)  # Field name made lowercase.
    companyId = models.CharField(db_column='CompanyId', max_length=36)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientInterest'
        unique_together = (('clientId', 'companyId'),)

    def __str__(self):
        return self.notes


class ClientInterview(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clientId = models.CharField(db_column='ClientId', max_length=36)  # Field name made lowercase.
    interviewerId = models.CharField(db_column='InterviewerId', max_length=36)  # Field name made lowercase.
    interviewtypeId = models.CharField(db_column='InterviewTypeId', max_length=36)  # Field name made lowercase.
    interviewDate = models.DateTimeField(db_column='InterviewDate')  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientInterview'
        
    def __str__(self):
        return self.interviewerId


class ClientNote(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clientId = models.CharField(db_column='ClientId', max_length=36)  # Field name made lowercase.
    note = models.TextField(db_column='Note')  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientNote'
    
    def __str__(self):
        return self.note


class ClientPlacement(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clientId = models.CharField(db_column='ClientId', max_length=36)  # Field name made lowercase.
    companyId = models.CharField(db_column='CompanyId', max_length=36)  # Field name made lowercase.
    jobId = models.CharField(db_column='JobId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    placementDate = models.DateField(db_column='PlacementDate', blank=True, null=True)  # Field name made lowercase.
    exitDate = models.DateField(db_column='ExitDate', blank=True, null=True)  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientPlacement'
        unique_together = (('clientId', 'companyId', 'placementDate'),)

    def __str__(self):
        return self.clientId


class ClientSkill(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clientId = models.CharField(db_column='ClientId', max_length=36)  # Field name made lowercase.
    skillId = models.CharField(db_column='SkillId', max_length=36)  # Field name made lowercase.
    details = models.TextField(db_column='Details', blank=True, null=True)  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientSkill'
        unique_together = (('clientId', 'skillId'),)

    def __str__(self):
        return self.skillId


class ClientUpdate(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clientId = models.CharField(db_column='ClientId', max_length=36)  # Field name made lowercase.
    supportContact = models.TextField(db_column='SupportContact', blank=True, null=True)  # Field name made lowercase.
    lphResident = models.BooleanField(db_column='LPHResident')  # Field name made lowercase.
    phoneNumber = models.CharField(db_column='PhoneNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    emailAddress = models.CharField(db_column='EmailAddress', max_length=75, blank=True, null=True)  # Field name made lowercase.
    ownsCar = models.BooleanField(db_column='OwnsCar')  # Field name made lowercase.
    hasLicense = models.BooleanField(db_column='HasLicense')  # Field name made lowercase.
    rideAvailable = models.BooleanField(db_column='RideAvailable')  # Field name made lowercase.
    jobInterests = models.TextField(db_column='JobInterests', blank=True, null=True)  # Field name made lowercase.
    statusId = models.CharField(db_column='StatusId', max_length=36)  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.
    dateProcessed = models.DateTimeField(db_column='DateProcessed', blank=True, null=True)  # Field name made lowercase.
    processedBy = models.CharField(db_column='ProcessedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientUpdate'

    def __str__(self):
        return self.clientId

class Company(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=100)  # Field name made lowercase.
    primaryFirstName = models.CharField(db_column='PrimaryFirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primaryLastName = models.CharField(db_column='PrimaryLastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    primaryPhone = models.CharField(db_column='PrimaryPhone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    primaryEmail = models.CharField(db_column='PrimaryEmail', max_length=75, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=50)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2)  # Field name made lowercase.
    zipCode = models.CharField(db_column='ZipCode', max_length=10)  # Field name made lowercase.
    neighborHoodId = models.CharField(db_column='NeighborhoodId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.
    dateReviewed = models.DateTimeField(db_column='DateReviewed', blank=True, null=True)  # Field name made lowercase.
    reviewedBy = models.CharField(db_column='ReviewedBy', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Company'

    def __str__(self):
        return self.name


class CompanyInterest(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    companyId = models.CharField(db_column='CompanyId', max_length=36)  # Field name made lowercase.
    clientId = models.CharField(db_column='ClientId', max_length=36)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    upatedBy = models.CharField(db_column='UpatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompanyInterest'
        unique_together = (('companyId', 'clientId'),)

    def __str__(self):
        return self.notes


class Crime(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Crime'

    def __str__(self):
        return self.name


class Interviewtype(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InterviewType'

    def __str__(self):
        return self.name


class Job(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    companyId = models.CharField(db_column='CompanyId', max_length=36)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    contactFirstName = models.CharField(db_column='ContactFirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactLastName = models.CharField(db_column='ContactLastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactPhone = models.CharField(db_column='ContactPhone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    contactEmail = models.CharField(db_column='ContactEmail', max_length=75, blank=True, null=True)  # Field name made lowercase.
    dateListed = models.DateTimeField(db_column='DateListed', blank=True, null=True)  # Field name made lowercase.
    dateFilled = models.DateTimeField(db_column='DateFilled', blank=True, null=True)  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Job'

    def __str__(self):
        return self.description


class JobSkill(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    jobId = models.CharField(db_column='JobId', max_length=36)  # Field name made lowercase.
    skillId = models.CharField(db_column='SkillId', max_length=36)  # Field name made lowercase.
    details = models.TextField(db_column='Details', blank=True, null=True)  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JobSkill'
        unique_together = (('jobId', 'skillId'),)

    def __str__(self):
        return self.skillId

class Login(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=75)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=72)  # Field name made lowercase.
    mySalt = models.CharField(db_column='MySalt', max_length=25)  # Field name made lowercase.
    loginType = models.CharField(db_column='LoginType', max_length=50)  # Field name made lowercase.
    inactiveDate = models.DateTimeField(db_column='InactiveDate', blank=True, null=True)  # Field name made lowercase.
    deletedDate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Login'

    def __str__(self):
        return self.username


class Neighborhood(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Neighborhood'

    def __str__(self):
        return self.name


class PlacementOption(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    clientId = models.CharField(db_column='ClientId', max_length=36)  # Field name made lowercase.
    companyId = models.CharField(db_column='CompanyId', max_length=36)  # Field name made lowercase.
    jobId = models.CharField(db_column='JobId', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ranking = models.IntegerField(db_column='Ranking')  # Field name made lowercase.
    dateCreated = models.DateTimeField(db_column='DateCreated')  # Field name made lowercase.
    createdBy = models.CharField(db_column='CreatedBy', max_length=36)  # Field name made lowercase.
    lastUpdated = models.DateTimeField(db_column='LastUpdated')  # Field name made lowercase.
    updatedBy = models.CharField(db_column='UpdatedBy', max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlacementOption'
        unique_together = (('clientId', 'companyId'),)


class ReferralSource(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReferralSource'

    def __str__(self):
        return self.name


class Skill(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Skill'

    def __str__(self):
        return self.name

class StaffingAgency(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StaffingAgency'

    def __str__(self):
        return self.name

class StateSource(models.Model):
    stateCode = models.CharField(db_column='StateCode', primary_key=True, max_length=2)  # Field name made lowercase.
    stateName = models.CharField(db_column='StateName', unique=True, max_length=50)  # Field name made lowercase.
    province = models.BooleanField(db_column='Province')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StateSource'

    def __str__(self):
        return self.stateName

class StatusSource(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.
    sortOrder = models.IntegerField(db_column='SortOrder', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StatusSource'

    def __str__(self):
        return self.name
