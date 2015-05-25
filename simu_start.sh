#!/bin/sh

TIMES="1 2 3"
SCENARIO="1 2 3 4"

CODEL="1 2"
DRF="10 20"
TGET1="100ms"
INTV1="10ms"
TGET2="500ms"
INTV2="20ms"
#en vi :set fileformat=unix

echo C-GW stats

pCheck=`which gnuplot`
if [ -z "$pCheck" ]
then
  echo "ERROR: This script requires gnuplot (wifi-example-sim does not)."
  exit 255
fi

pCheck=`which sed`
if [ -z "$pCheck" ]
then
  echo "ERROR: This script requires sed (wifi-example-sim does not)."
  exit 255
fi

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:bin/

#Define stadistics files
for scenario in $SCENARIO
do
		cd ..
		touch Cell-$scenario.txt
		touch VideoDel-$scenario.txt
		touch VideoTh-$scenario.txt
		touch VideoTh-cdf-$scenario.txt
		touch VideoDel-cdf-$scenario.txt
		touch VoIPTh-cdf-$scenario.txt
		touch VoIPDel-cdf-$scenario.txt		
		touch FTPDel-cdf-$scenario.txt
        	touch FTPTh-cdf-$scenario.txt
		touch voip-del-$scenario.txt
	
		cd scratch/
#Run simulations		
		for times in $TIMES		
		do
				for times in $CODEL		
				do
					echo Scenario $scenario, time $times, Codel $codel
					
					if [ $codel -eq 1]
					then
						../waf --run "CGW1 --SimTime=60 --runt=$times --Scenario=$scenario  --CoreDataRate=1000Gbps --numberOfUE=10 --run=$scenario-$times --nRB=25 --DrFactor=20 --Target=$tget1 --Interval=$intv1"	

					else
						../waf --run "CGW1 --SimTime=60 --runt=$times --Scenario=$scenario  --CoreDataRate=1000Gbps --numberOfUE=10 --run=$scenario-$times --nRB=25 --DrFactor=20 --Target=$tget2 --Interval=$intv2"	

					fi
					
					cd ..
					python cell.py Cell-$scenario.txt $times 
					python video.py VideoTh-$scenario.txt $times VideoDel-$scenario.txt
					python videocdf.py VideoTh-cdf-$scenario.txt $times VideoDel-cdf-$scenario.txt
					python voip.py VoIPTh-cdf-$scenario.txt  $times VoIPDel-cdf-$scenario.txt voip-del-$scenario.txt
					python ftp.py FTPTh-cdf-$scenario.txt $times FTPDel-cdf-$scenario.txt
					cd scratch/
				done
		done
  
done


# Plot Stats

# python xxxxx.py arg


#
#Another SQL command which just collects raw numbers of frames receved.
#
#CMD="select Experiments.input,avg(Singletons.value) \
#    from Singletons,Experiments \
#    where Singletons.run = Experiments.run AND \
#          Singletons.name='wifi-rx-frames' \
#    group by Experiments.input \
#    order by abs(Experiments.input) ASC;"



# mv ../../data.db .

# CMD="select exp.input,avg(100-((rx.value*100)/tx.value)) \
    # from Singletons rx, Singletons tx, Experiments exp \
    # where rx.run = tx.run AND \
    #       rx.run = exp.run AND \
    #       rx.variable='receiver-rx-packets' AND \
    #       tx.variable='sender-tx-packets' \
    # group by exp.input \
    # order by abs(exp.input) ASC;"

# sqlite3 -noheader data.db "$CMD" > wifi-default.data
# sed -i.bak "s/|/   /" wifi-default.data
# rm wifi-default.data.bak
# gnuplot wifi-example.gnuplot

echo "Done ..."
