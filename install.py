https://www.virtualbox.org/ 
https://download.virtualbox.org/virtualbox/7.1.4/VirtualBox-7.1.4-165100-Win.exe 
https://mininet.org/download/ 
https://github.com/mininet/mininet/releases/download/2.3.0/mininet-2.3.0-210211-ubuntu16.04.6
serveri386-ovf.zip 

sudo mn -h 
sudo mn 
mininet> help 
mininet> nodes 
mininet> net 
mininet> dump 
mininet> h1 ifconfig -a 
mininet> s1 ifconfig -a 
mininet> h1 ps -a 
mininet> s1 ps -a 
mininet> h1 ping -c 1 h2 
mininet> pingall 
mininet> h1 python -m http.server 80 & 
mininet> h2 wget -O - h1 
mininet> h1 kill %python 
mininet> exit 

sudo mn -c 
sudo mn --test iperf 
sudo mn --test pingall --topo single,3 
sudo mn --test pingall --topo linear,4



sudo apt-get -y update   
sudo apt-get -y upgrade   
sudo apt-get -y install unzip   
sudo apt-get -y install openjdk-8-jre   
sudo update-alternatives   

ls -l /etc/alternatives/java   
echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-i386' >> ~/.bashrc   

curl -XGET -O https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/karaf/0.8.4/karaf-0.8.4.zip   

ls   
unzip karaf-0.8.4.zip   
cd karaf-0.8.4/   

ls   
./bin/karaf