echo "Enter folder name: "
read filename 
echo "Enter date: " 
read date 
folder=$filename"-"$date
mkdir -p $folder/{src,bin,results,data,docs}