# Generated by Django 3.2.11 on 2024-02-26 11:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecordingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ethnicity', models.CharField(choices=[('Caucasian', 'Caucasian'), ('African', 'African'), ('Arab (Middle-East)', 'Arab (Middle-East)'), ('Asians (South-East)', 'Asians (South-East)'), ('Chinese', 'Chinese'), ('Latin/Hispanic', 'Latin/Hispanic'), ('Indian', 'Indian'), ('Others (mixed)', 'Others (mixed)')], max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('height', models.IntegerField()),
                ('beard', models.CharField(choices=[('Full beard', 'Full beard'), ('Mustache', 'Mustache'), ('Goatbeard', 'Goatbeard'), ('Henriquatre', 'Henriquatre')], max_length=100)),
                ('hair', models.CharField(choices=[('Short hair', 'Short hair'), ('Middle long hair (covering ears, but not long enough to reach the shoulders)', 'Middle long hair (covering ears, but not long enough to reach the shoulders)'), ('Long hair (until shoulder or longer)', 'Long hair (until shoulder or longer)'), ('Bald head', 'Bald head')], max_length=100)),
                ('eyecolour', models.CharField(choices=[('brown', 'brown'), ('gray', 'gray'), ('blue', 'blue'), ('green', 'green')], max_length=100)),
                ('workpackage', models.CharField(choices=[('WP1', 'WP1'), ('WP2', 'WP2'), ('WP3', 'WP3'), ('WP4', 'WP4'), ('WP5', 'WP5')], max_length=100)),
                ('workpackagetype', models.CharField(choices=[('WP1-TV', 'WP1-TV'), ('WP1-K', 'WP1-K'), ('WP2a-TV', 'WP2a-TV'), ('WP2b-TV', 'WP2b-TV'), ('WP2c-TV', 'WP2c-TV'), ('WP2a-K', 'WP2a-K'), ('WP2b-K', 'WP2c-K'), ('WP3-TV', 'WP3-TV'), ('WP3-K', 'WP3-K'), ('WP4-TV', 'WP4-TV'), ('WP4-K', 'WP4-K'), ('WP5-TV', 'WP5-TV'), ('WP5-K', 'WP5-K')], max_length=100)),
                ('carnumber', models.CharField(max_length=100, null=True)),
                ('carstatus', models.CharField(choices=[('Static', 'Static'), ('Drive', 'Drive')], max_length=100, null=True)),
                ('action', models.CharField(max_length=255, null=True)),
                ('clothingaccessories', models.CharField(choices=[('Masks', 'Masks'), ('Scarfs', 'Scarfs'), ('Hands-free headset', 'Hands-free headset'), ('Head/Ear phones', 'Head/Ear phones'), ('Caps, hats, headscarf and turban', 'Caps, hats, headscarf and turban'), ('Headband', 'Headband'), ('Eyepatch', 'Eyepatch'), ('Earrings', 'Earrings'), ('Nose rings', 'Nose rings'), ('Piercings', 'Piercings')], max_length=100, null=True)),
                ('glasses', models.CharField(choices=[('Glasses with anti-glare lenses', 'Glasses with anti-glare lenses'), ('Glasses with mirrored lenses', 'Glasses with mirrored lenses'), ('Sunglasses with IR protection in the band of frequency 780 nm – 1.400 nm', 'Sunglasses with IR protection in the band of frequency 780 nm – 1.400 nm'), ('Glasses with complete spectacle frame', 'Glasses with complete spectacle frame'), ('Metal-rimmed glasses', 'Metal-rimmed glasses'), ('Varifocal glasses with power ranging from –10 to +11', 'Varifocal glasses with power ranging from –10 to +11'), ('Glasses with cylindrical lenses for Astigmatism with power ranging from –10 to +11', 'Glasses with cylindrical lenses for Astigmatism with power ranging from –10 to +11'), ('Spherical contact lenses for Astigmatism with power ranging from  –10 to +11', 'Spherical contact lenses for Astigmatism with power ranging from  –10 to +11'), ('Sunglasses with tinted lenses', 'Sunglasses with tinted lenses')], max_length=100, null=True)),
                ('makeup', models.CharField(choices=[('Makeup eyeliner', 'Makeup eyeliner'), ('Makeup mascara', 'Makeup mascara'), ('Makeup eye shadow', 'Makeup eye shadow'), ('Makeup false eyelashes', 'Makeup false eyelashes'), ('Cover makeup', 'Cover makeup')], max_length=100, null=True)),
                ('recordingstatus', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=100, null=True)),
            ],
        ),
    ]
