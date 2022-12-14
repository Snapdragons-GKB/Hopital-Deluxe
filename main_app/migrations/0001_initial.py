# Generated by Django 4.1 on 2022-09-19 22:25

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('usertype', models.CharField(choices=[('Patient', 'Patient'), ('Scheduler', 'Scheduler'), ('Provider', 'Provider')], default='Patient', max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedulerProfile', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_personal_blurb', models.CharField(max_length=200)),
                ('provider_specialization', models.CharField(choices=[('None', 'None'), ('General', 'General'), ('Orthopedics', 'Orthopedics'), ('Cardiology', 'Cardiology'), ('Neurology', 'Neurology'), ('Pediatrics', 'Pediatrics'), ('Emergency', 'Emergency'), ('Psychiatry', 'Psychiatry'), ('Radiology', 'Radiology'), ('Internal Medicine', 'Internal Medicine'), ('Other', 'Other')], default='None', max_length=20)),
                ('provider_insurances_taken', models.CharField(choices=[('Without Insurance', 'Without Insurance'), ('Medicaid', 'Medicaid'), ('Medicare', 'Medicare'), ('Private', 'Private')], default='Without Insurance', max_length=20)),
                ('monday', models.CharField(choices=[('Unavailable', 'Unavailable'), ('Available', 'Available'), ('Filled', 'Filled')], default='Unavailable', max_length=20)),
                ('tuesday', models.CharField(choices=[('Unavailable', 'Unavailable'), ('Available', 'Available'), ('Filled', 'Filled')], default='Unavailable', max_length=20)),
                ('wednesday', models.CharField(choices=[('Unavailable', 'Unavailable'), ('Available', 'Available'), ('Filled', 'Filled')], default='Unavailable', max_length=20)),
                ('thursday', models.CharField(choices=[('Unavailable', 'Unavailable'), ('Available', 'Available'), ('Filled', 'Filled')], default='Unavailable', max_length=20)),
                ('friday', models.CharField(choices=[('Unavailable', 'Unavailable'), ('Available', 'Available'), ('Filled', 'Filled')], default='Unavailable', max_length=20)),
                ('saturday', models.CharField(choices=[('Unavailable', 'Unavailable'), ('Available', 'Available'), ('Filled', 'Filled')], default='Unavailable', max_length=20)),
                ('sunday', models.CharField(choices=[('Unavailable', 'Unavailable'), ('Available', 'Available'), ('Filled', 'Filled')], default='Unavailable', max_length=20)),
                ('providerProfile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientRequestForAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientInsuranceType', models.CharField(choices=[('Without Insurance', 'Without Insurance'), ('Medicaid', 'Medicaid'), ('Medicare', 'Medicare'), ('Private', 'Private')], default='Without Insurance', max_length=20)),
                ('patientFirst', models.CharField(max_length=20)),
                ('patientLast', models.CharField(max_length=20)),
                ('patient_ailment_category', models.CharField(choices=[('None', 'None'), ('General', 'General'), ('Orthopedics', 'Orthopedics'), ('Cardiology', 'Cardiology'), ('Neurology', 'Neurology'), ('Pediatrics', 'Pediatrics'), ('Emergency', 'Emergency'), ('Psychiatry', 'Psychiatry'), ('Radiology', 'Radiology'), ('Internal Medicine', 'Internal Medicine'), ('Other', 'Other')], default='None', max_length=20)),
                ('patient_ailment_description', models.CharField(max_length=80)),
                ('patient_preferred_day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=20)),
                ('accepted', models.BooleanField(blank=True, null=True)),
                ('scheduler_comment', models.CharField(blank=True, max_length=200, null=True)),
                ('patientUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patientofrequest', to=settings.AUTH_USER_MODEL)),
                ('schedulerUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedulerofrequest', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_age', models.IntegerField()),
                ('patient_insurance_type', models.CharField(choices=[('Without Insurance', 'Without Insurance'), ('Medicaid', 'Medicaid'), ('Medicare', 'Medicare'), ('Private', 'Private')], default='Without Insurance', max_length=20)),
                ('patient_preexisting_conditions', models.TextField(max_length=80)),
                ('patient_current_medications', models.TextField(max_length=80)),
                ('patientProfile', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('encounter_date', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=20)),
                ('doctor_comment', models.TextField(blank=True, default=None, null=True)),
                ('patient_comment', models.TextField(blank=True, default=None, null=True)),
                ('approved', models.BooleanField(blank=True, null=True)),
                ('patientUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patientofencounter', to=settings.AUTH_USER_MODEL)),
                ('providerUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='providerofencounter', to=settings.AUTH_USER_MODEL)),
                ('schedulerUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedulerofencounter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
