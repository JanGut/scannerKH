# Generated by Django 3.0.5 on 2020-04-18 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grosshaendler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('artikel_nr', models.CharField(max_length=14, primary_key=True, serialize=False, verbose_name='Artikelnummer')),
                ('aenderungskennung', models.CharField(max_length=1, verbose_name='Änderungskennung: N=neu, A=Änderung, X=ausgelistet, R=Restbestand, V=vorübergehend ausgelistet, W=wiedergelistet')),
                ('aenderungsdatum', models.IntegerField(verbose_name='Änderungsdatum: JJJJMMTT')),
                ('aenderungszeit', models.IntegerField(verbose_name='Änderungszeit: SSMM')),
                ('ean_laden', models.BigIntegerField(verbose_name='EANladen')),
                ('ean_bestell', models.BigIntegerField(verbose_name='EANbestell')),
                ('bezeichnung', models.CharField(max_length=50, verbose_name='Bezeichnung')),
                ('bezeichnung2', models.CharField(max_length=50, verbose_name='Bezeichnung2')),
                ('bezeichnung3', models.CharField(max_length=30, verbose_name='Bezeichnung3')),
                ('handelsklasse', models.CharField(max_length=5, verbose_name='Handelsklasse: I, II, III, IV, ...')),
                ('hersteller_inverkehrbringer', models.CharField(max_length=4, verbose_name='Hersteller/Inverkehrbringer')),
                ('hersteller', models.CharField(max_length=4, verbose_name='Hersteller')),
                ('herkunft', models.CharField(max_length=3, verbose_name='Herkunft')),
                ('qualitaet', models.CharField(max_length=4, verbose_name='Qualität')),
                ('kontrollstelle', models.CharField(max_length=15, verbose_name='Kontrollstelle')),
                ('mhd_restlaufzeit', models.IntegerField(verbose_name='MHD-Restlaufzeit in Tagen')),
                ('wg_bnn', models.IntegerField(verbose_name='Warengruppe BNN')),
                ('wg_ifh', models.IntegerField(verbose_name='Warengruppe IfH')),
                ('wg_gh', models.IntegerField(verbose_name='Warengruppe Großhändler')),
                ('ersatz_artikel_nr', models.CharField(max_length=14, verbose_name='Ersate-Artikelnummer')),
                ('min_bestell_menge', models.IntegerField(verbose_name='MinBestellMenge in Bestelleinheit')),
                ('bestelleinheit', models.CharField(max_length=15, verbose_name='Bestelleinheit')),
                ('bestelleinheits_menge', models.IntegerField(verbose_name='Bestelleinheits-Menge: Anzahl Ladeneinheiten je Bestelleinheit')),
                ('ladeneinheit', models.CharField(max_length=10, verbose_name='Ladeneinheit')),
                ('mengenfaktor', models.IntegerField(verbose_name='Mengenfaktor')),
                ('gewichtsartikel', models.CharField(max_length=1, verbose_name='Gewichtsartikel: J/N')),
                ('pfand_nr_ladeneinheit', models.CharField(max_length=10, verbose_name='PfandNrLadeneinheit')),
                ('pfand_nr_bestelleinheit', models.CharField(max_length=10, verbose_name='PfandNrBestelleinheit')),
                ('gewicht_ladeneinheit', models.IntegerField(verbose_name='GewichtLadeneinheit')),
                ('gewicht_bestelleinheit', models.IntegerField(verbose_name='GewichtBestelleinheit')),
                ('breite', models.IntegerField(verbose_name='Breite')),
                ('hoehe', models.IntegerField(verbose_name='Höhe')),
                ('tiefe', models.IntegerField(verbose_name='Tiefe')),
                ('mwst_kennung', models.IntegerField(verbose_name='MwstKennung: 1=reduziert, 2=voll, 3=LandwirtsSatz')),
                ('vk_festpreis', models.IntegerField(verbose_name='VkFestpreis')),
                ('empf_vk', models.IntegerField(verbose_name='EmpfVk')),
                ('empf_vk_gh', models.IntegerField(verbose_name='EmpfVkGH')),
                ('preis', models.IntegerField(verbose_name='Preis')),
                ('rabattfaehig', models.CharField(max_length=1, verbose_name='rabattfähig')),
                ('skontierfaehig', models.CharField(max_length=1, verbose_name='skontierfähig')),
                ('staffel_menge1', models.IntegerField(verbose_name='StaffelMenge1: in Ladeneinheit')),
                ('staffel_preis1', models.IntegerField(verbose_name='StaffelPreis1: je Ladeneinheit o. MWSt')),
                ('rabattfaehig1', models.CharField(max_length=1, verbose_name='rabattfähig1')),
                ('skontierfaehig1', models.CharField(max_length=1, verbose_name='skontierfähig1')),
                ('staffel_menge2', models.IntegerField(verbose_name='StaffelMenge2: in Ladeneinheit')),
                ('staffel_preis2', models.IntegerField(verbose_name='StaffelPreis2: je Ladeneinheit o. MWSt')),
                ('rabattfaehig2', models.CharField(max_length=1, verbose_name='rabattfähig2')),
                ('skontierfaehig2', models.CharField(max_length=1, verbose_name='skontierfähig2')),
                ('staffel_menge3', models.IntegerField(verbose_name='StaffelMenge3: in Ladeneinheit')),
                ('staffel_preis3', models.IntegerField(verbose_name='StaffelPreis3: je Ladeneinheit o. MWSt')),
                ('rabattfaehig3', models.CharField(max_length=1, verbose_name='rabattfähig3')),
                ('skontierfaehig3', models.CharField(max_length=1, verbose_name='skontierfähig3')),
                ('staffel_menge4', models.IntegerField(verbose_name='StaffelMenge4: in Ladeneinheit')),
                ('staffel_preis4', models.IntegerField(verbose_name='StaffelPreis4: je Ladeneinheit o. MWSt')),
                ('rabattfaehig4', models.CharField(max_length=1, verbose_name='rabattfähig4')),
                ('skontierfaehig4', models.CharField(max_length=1, verbose_name='skontierfähig4')),
                ('staffel_menge5', models.IntegerField(verbose_name='StaffelMenge5: in Ladeneinheit')),
                ('staffel_preis5', models.IntegerField(verbose_name='StaffelPreis5: je Ladeneinheit o. MWSt')),
                ('rabattfaehig5', models.CharField(max_length=1, verbose_name='rabattfähig5')),
                ('skontierfaehig5', models.CharField(max_length=1, verbose_name='skontierfähig5')),
                ('artikelart', models.CharField(max_length=1, verbose_name='Artikelart: F=Frische, T=Trocken, W=NaturWaren, P=Pfand, A=Artikel aus FrischePreisliste (aktuellesAngebot)')),
                ('aktionspreis', models.CharField(max_length=1, verbose_name='Aktionspreis: A')),
                ('aktionspreis_gueltig_ab', models.IntegerField(verbose_name='AktionspreisGültigAb: JJJJMMTT, 0/leer=ab sofort')),
                ('aktionspreis_gueltig_bis', models.IntegerField(verbose_name='AktionspreisGültigBis: JJJJMMTT, 0/leer=unbestimmt')),
                ('empf_vk_aktion', models.IntegerField(verbose_name='empfVk-Aktion')),
                ('grundpreis_einheit', models.CharField(max_length=10, verbose_name='Grundpreiseinheit')),
                ('grundpreis_faktor', models.IntegerField(verbose_name='Grundpreis-Faktor')),
                ('lieferbar_ab', models.IntegerField(verbose_name='LieferbarAb: JJJJMMTT')),
                ('lieferbar_bis', models.IntegerField(verbose_name='LieferbarBis: JJJJMMTT')),
                ('grosshaendler', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='grosshaendler.Grosshaendler')),
            ],
        ),
    ]
