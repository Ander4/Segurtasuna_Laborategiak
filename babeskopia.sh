#!/bin/bashç
#eguna, urtea eta hilabetea lortzeko date komandoa erabili
gaur=$(date '+%Y-%m-%d')
EGUNA=$(date '+%d')
HILABETEA=$(date '+%m')
URTEA=$(date '+%Y')
ATZO=$(date -d '-1 day' '+%d')

#Hauek data ondo artu duela konprobatzeko dira
#echo $gaur
#echo $EGUNA
#echo $HILABETEA
#echo $URTEA
#echo $ATZO

#/var/tmp/Backups karpetako atzoko babeskopiaren artxiboak /home/ander/Escritorio... karpetaren artxiboekin konparatzen ditu eta aldatzen direnak /var/tmp/Backups gaur karpetan sortzen du haien babeskopia inkrementala
rsync -av --compare-dest=/var/tmp/Backups/$URTEA-$HILABETEA-$ATZO /home/ander/Escritorio/UNI/3.maila/Segurtasuna/Laborategiak/Segur /var/tmp/Backups/$URTEA-$HILABETEA-$EGUNA
