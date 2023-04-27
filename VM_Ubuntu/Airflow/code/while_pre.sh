#!/bin/sh



echo "Welcom to shell practice File!!
	This Files desigined by Ljaewon  asdhfae"

echo "Select maybe? item: item1,item2 or item3  so simply"


a=0

while [ "$a" -lt 5 ]
do 
	a=$(expr $a + 1)
	echo $a
done


# while true ; do
#   echo "Please type something in (^C to quit)"
#   read INPUT_STRING
#   echo "You typed: $INPUT_STRING"
# done

echo "select item1 or item2 or item3"

while true ; do
	echo "hihi"
	read item
	case $item in 
		"item1")
			echo " you want stop? "
			echo "(y/n)" # Yes|yes|y|Y) case 하나 더 사용해서 이런식도 나쁘지 않을듯
			read a
			
			if [ "$a" = "y" ]; then
				break
			else 
				continue
			fi
		;;
		"item2" | "item3")
			echo "2 or 3"
			echo "???"
			
			cd /home/jaewon
			cat starbucks_all.json
		;;

		*) echo "Jush default"
		   echo " Try Again"
		;;
	esac
done








