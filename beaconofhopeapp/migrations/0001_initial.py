# Generated by Django 2.2.4 on 2019-09-16 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caseworker',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='FirstName', max_length=50)),
                ('lastname', models.CharField(db_column='LastName', max_length=50)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=15, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=75, null=True)),
                ('isactive', models.BooleanField(db_column='IsActive')),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'CaseWorker',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Citylinkstatussource',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, unique=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
            ],
            options={
                'db_table': 'CityLinkStatusSource',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='FirstName', max_length=50)),
                ('lastname', models.CharField(db_column='LastName', max_length=50)),
                ('dateofbirth', models.DateField(blank=True, db_column='DateOfBirth', null=True)),
                ('sex', models.CharField(db_column='Sex', max_length=1)),
                ('ssnhash', models.CharField(blank=True, db_column='SSNHash', max_length=72, null=True)),
                ('mysalt', models.CharField(blank=True, db_column='MySalt', max_length=25, null=True)),
                ('referralsourceid', models.CharField(blank=True, db_column='ReferralSourceId', max_length=36, null=True)),
                ('citylinkstatusid', models.CharField(blank=True, db_column='CityLinkStatusId', max_length=36, null=True)),
                ('staffingagencyid', models.CharField(blank=True, db_column='StaffingAgencyId', max_length=36, null=True)),
                ('supportcontact', models.TextField(blank=True, db_column='SupportContact', null=True)),
                ('initialinterviewerid', models.CharField(blank=True, db_column='InitialInterviewerId', max_length=36, null=True)),
                ('lphresident', models.BooleanField(db_column='LPHResident')),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=15, null=True)),
                ('emailaddress', models.CharField(blank=True, db_column='EmailAddress', max_length=75, null=True)),
                ('ownscar', models.BooleanField(db_column='OwnsCar')),
                ('haslicense', models.BooleanField(db_column='HasLicense')),
                ('rideavailable', models.BooleanField(db_column='RideAvailable')),
                ('jobinterests', models.TextField(blank=True, db_column='JobInterests', null=True)),
                ('statusid', models.CharField(db_column='StatusId', max_length=36)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'Client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientaddress',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('clientid', models.CharField(db_column='ClientId', max_length=36)),
                ('address1', models.CharField(db_column='Address1', max_length=50)),
                ('address2', models.CharField(blank=True, db_column='Address2', max_length=50, null=True)),
                ('city', models.CharField(db_column='City', max_length=50)),
                ('state', models.CharField(db_column='State', max_length=2)),
                ('zipcode', models.CharField(db_column='ZipCode', max_length=10)),
                ('neighborhoodid', models.CharField(blank=True, db_column='NeighborhoodId', max_length=36, null=True)),
                ('iscurrent', models.BooleanField(db_column='IsCurrent')),
                ('isprimary', models.BooleanField(db_column='IsPrimary')),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'ClientAddress',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientcrime',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('clientid', models.CharField(db_column='ClientId', max_length=36)),
                ('crimeid', models.CharField(db_column='CrimeId', max_length=36)),
                ('dateconvicted', models.DateField(blank=True, db_column='DateConvicted', null=True)),
                ('datereleased', models.DateField(blank=True, db_column='DateReleased', null=True)),
                ('details', models.TextField(blank=True, db_column='Details', null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'ClientCrime',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientfollowup',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('clientid', models.CharField(db_column='ClientId', max_length=36)),
                ('followup', models.TextField(db_column='FollowUp')),
                ('targetdate', models.DateField(db_column='TargetDate')),
                ('datecompleted', models.DateField(blank=True, db_column='DateCompleted', null=True)),
                ('datearchived', models.DateTimeField(blank=True, db_column='DateArchived', null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'ClientFollowUp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientinterest',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('clientid', models.CharField(db_column='ClientId', max_length=36)),
                ('companyid', models.CharField(db_column='CompanyId', max_length=36)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'ClientInterest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientinterview',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('clientid', models.CharField(db_column='ClientId', max_length=36)),
                ('interviewerid', models.CharField(db_column='InterviewerId', max_length=36)),
                ('interviewtypeid', models.CharField(db_column='InterviewTypeId', max_length=36)),
                ('interviewdate', models.DateTimeField(db_column='InterviewDate')),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'ClientInterview',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientnote',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('clientid', models.CharField(db_column='ClientId', max_length=36)),
                ('note', models.TextField(db_column='Note')),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'ClientNote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientplacement',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('clientid', models.CharField(db_column='ClientId', max_length=36)),
                ('companyid', models.CharField(db_column='CompanyId', max_length=36)),
                ('jobid', models.CharField(blank=True, db_column='JobId', max_length=36, null=True)),
                ('placementdate', models.DateField(blank=True, db_column='PlacementDate', null=True)),
                ('exitdate', models.DateField(blank=True, db_column='ExitDate', null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'ClientPlacement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientskill',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('clientid', models.CharField(db_column='ClientId', max_length=36)),
                ('skillid', models.CharField(db_column='SkillId', max_length=36)),
                ('details', models.TextField(blank=True, db_column='Details', null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'ClientSkill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientupdate',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('clientid', models.CharField(db_column='ClientId', max_length=36)),
                ('supportcontact', models.TextField(blank=True, db_column='SupportContact', null=True)),
                ('lphresident', models.BooleanField(db_column='LPHResident')),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=15, null=True)),
                ('emailaddress', models.CharField(blank=True, db_column='EmailAddress', max_length=75, null=True)),
                ('ownscar', models.BooleanField(db_column='OwnsCar')),
                ('haslicense', models.BooleanField(db_column='HasLicense')),
                ('rideavailable', models.BooleanField(db_column='RideAvailable')),
                ('jobinterests', models.TextField(blank=True, db_column='JobInterests', null=True)),
                ('statusid', models.CharField(db_column='StatusId', max_length=36)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
                ('dateprocessed', models.DateTimeField(blank=True, db_column='DateProcessed', null=True)),
                ('processedby', models.CharField(blank=True, db_column='ProcessedBy', max_length=36, null=True)),
            ],
            options={
                'db_table': 'ClientUpdate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=100, unique=True)),
                ('primaryfirstname', models.CharField(blank=True, db_column='PrimaryFirstName', max_length=50, null=True)),
                ('primarylastname', models.CharField(blank=True, db_column='PrimaryLastName', max_length=50, null=True)),
                ('primaryphone', models.CharField(blank=True, db_column='PrimaryPhone', max_length=15, null=True)),
                ('primaryemail', models.CharField(blank=True, db_column='PrimaryEmail', max_length=75, null=True)),
                ('address1', models.CharField(db_column='Address1', max_length=50)),
                ('address2', models.CharField(blank=True, db_column='Address2', max_length=50, null=True)),
                ('city', models.CharField(db_column='City', max_length=50)),
                ('state', models.CharField(db_column='State', max_length=2)),
                ('zipcode', models.CharField(db_column='ZipCode', max_length=10)),
                ('neighborhoodid', models.CharField(blank=True, db_column='NeighborhoodId', max_length=36, null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
                ('datereviewed', models.DateTimeField(blank=True, db_column='DateReviewed', null=True)),
                ('reviewedby', models.CharField(blank=True, db_column='ReviewedBy', max_length=36, null=True)),
            ],
            options={
                'db_table': 'Company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Companyinterest',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('companyid', models.CharField(db_column='CompanyId', max_length=36)),
                ('clientid', models.CharField(db_column='ClientId', max_length=36)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('upatedby', models.CharField(db_column='UpatedBy', max_length=36)),
            ],
            options={
                'db_table': 'CompanyInterest',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50, unique=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
            ],
            options={
                'db_table': 'Crime',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Interviewtype',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50, unique=True)),
            ],
            options={
                'db_table': 'InterviewType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('companyid', models.CharField(db_column='CompanyId', max_length=36)),
                ('title', models.CharField(db_column='Title', max_length=50)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('contactfirstname', models.CharField(blank=True, db_column='ContactFirstName', max_length=50, null=True)),
                ('contactlastname', models.CharField(blank=True, db_column='ContactLastName', max_length=50, null=True)),
                ('contactphone', models.CharField(blank=True, db_column='ContactPhone', max_length=15, null=True)),
                ('contactemail', models.CharField(blank=True, db_column='ContactEmail', max_length=75, null=True)),
                ('datelisted', models.DateTimeField(blank=True, db_column='DateListed', null=True)),
                ('datefilled', models.DateTimeField(blank=True, db_column='DateFilled', null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'Job',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Jobskill',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('jobid', models.CharField(db_column='JobId', max_length=36)),
                ('skillid', models.CharField(db_column='SkillId', max_length=36)),
                ('details', models.TextField(blank=True, db_column='Details', null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'JobSkill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='UserName', max_length=75)),
                ('password', models.CharField(db_column='Password', max_length=72)),
                ('mysalt', models.CharField(db_column='MySalt', max_length=25)),
                ('logintype', models.CharField(db_column='LoginType', max_length=50)),
                ('inactivedate', models.DateTimeField(blank=True, db_column='InactiveDate', null=True)),
                ('deleteddate', models.DateTimeField(blank=True, db_column='DeletedDate', null=True)),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'Login',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50, unique=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
            ],
            options={
                'db_table': 'Neighborhood',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Placementoption',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('clientid', models.CharField(db_column='ClientId', max_length=36)),
                ('companyid', models.CharField(db_column='CompanyId', max_length=36)),
                ('jobid', models.CharField(blank=True, db_column='JobId', max_length=36, null=True)),
                ('ranking', models.IntegerField(db_column='Ranking')),
                ('datecreated', models.DateTimeField(db_column='DateCreated')),
                ('createdby', models.CharField(db_column='CreatedBy', max_length=36)),
                ('lastupdated', models.DateTimeField(db_column='LastUpdated')),
                ('updatedby', models.CharField(db_column='UpdatedBy', max_length=36)),
            ],
            options={
                'db_table': 'PlacementOption',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Referralsource',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50, unique=True)),
            ],
            options={
                'db_table': 'ReferralSource',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50, unique=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
            ],
            options={
                'db_table': 'Skill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staffingagency',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50, unique=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
            ],
            options={
                'db_table': 'StaffingAgency',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Statesource',
            fields=[
                ('statecode', models.CharField(db_column='StateCode', max_length=2, primary_key=True, serialize=False)),
                ('statename', models.CharField(db_column='StateName', max_length=50, unique=True)),
                ('province', models.BooleanField(db_column='Province')),
            ],
            options={
                'db_table': 'StateSource',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Statussource',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50, unique=True)),
                ('sortorder', models.IntegerField(db_column='SortOrder', unique=True)),
            ],
            options={
                'db_table': 'StatusSource',
                'managed': False,
            },
        ),
    ]
