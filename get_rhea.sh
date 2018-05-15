echo "Enter folder name: " 
read folder 

mkdir $folder 
cd $folder 
curl https://github.com/Lagkouvardos/Rhea.git > Rhea-master.zip 
