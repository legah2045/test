Linux working session  :

Prime Interview Working Session  :
Time: 7pm Feb 4, 2021
Host: (Abih) Mega Mama
GotoMeeting: https://global.gotomeeting.com/join/898957485




echo 'Functions demo'
hello()
{
	echo 'HelloWorld'
	echo "Welcome to Landmark"
	echo 'I love Devops'
	echo "Today's date is `date`" 
}
hello

userfn()
{


}

echo enter tools
read -a tools
echo Tools enter are $tools
echo The third tool you entered is ${tools[2]}
echo Your Devops tools entered are ${tools[*]}


tools=(git, maven, nexus, jk, docker, aws)
echo $tools
echo ${tools[2]}
echo ${tools[*]}
echo ${tools[0]}


# Building a list
declare -a devopstools
devopstools[0]=GitHub
devopstools[1]=Ant
devopstools[2]=Maven
devopstools[3]=Tomcat
devopstools[4]=Wildfly
devopstools[5]=SonarQube






#Displaying 1st value
echo ${devopstools[0]}

#Displaying 5th value
echo ${devopstools[4]}

#Displaying all values
echo ${devopstools[*]}

#Displaying all values

echo ${devopstools[@]}