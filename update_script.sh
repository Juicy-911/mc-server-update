#!/bin/bash
mkdir -p "/tmp/minecraft_backups"
save_dir="/tmp/minecraft_backups"
current_dir=${0%/*}
server_dir=./bedrockserver
required_files_dir=./required_files

rm -R *.zip

make_backup(){
    zip -r $save_dir/bedrockserver_backup_$today $server_dir
    mkdir -p $required_files_dir/worlds
    cp $server_dir/server.properties $required_files_dir
    cp -r $server_dir/worlds $required_files_dir
}

remove_old_server_files(){
    rm -R $server_dir
    echo "[-] Old server files deleted..."
}

install_new_server_files(){
    mkdir bedrockserver
    unzip *.zip -d $server_dir
    cp $required_files_dir/server.properties $server_dir/server.properties
    echo "[+] Fichier 'server.properties' copié."
    cp -r $required_files_dir/worlds $server_dir
    echo "[+] Répertoire contenant les mondes copié."
}

clean(){
    rm -R $required_files_dir
    rm *.zip
}



help(){
    echo "This script is made to automatically update your minecraft server".
    echo "Please provide the url of the updated minecraft server as the only argument."
    exit 1
}
if [ "$#" != 1 ]; then
    help
fi

today=$(date '+%Y-%m-%d')
echo "$today"


wget $1
make_backup
remove_old_server_files
install_new_server_files
clean
#rm bedrock-server*



#unzip bedrock-server*