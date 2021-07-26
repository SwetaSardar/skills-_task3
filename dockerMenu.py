import os 
import time

os.system("clear")
os.system("tput setaf 3")
print("""\t\t\t Welcome to the Docker Menu Program \n""")
print("""\t\t----------------------------""")

while True:
    os.system("tput setaf 6")


    print("""\t\t\tDOCKER_MENU \n
    Press q : for exit\n
    Press s : for clear the screen\n
    Press 1 : to start the docker service\n
    Press 2 : to enable the docker service\n
    Press 3 : to check the docker service\n
    press 4 : to download the docker image\n
    Press 5 : to launch the container\n
    Press 6 : to copy a web_page into the docker container\n
    press 7 : to start the docker container\n
    Press 8 : to attach the docker container\n
    """)

    os.system("tput setaf 3")
    d = input("enter your choice : ")

    if d == "q":
        exit()


    elif d == "s":
        os.system("clear")

    elif int(d) == 1:
        os.system("systemctl start docker")
        os.system("tput setaf 2")
        print("\t\t\tService has been started")
        time.sleep(4)
        os.system("clear")

    elif int(d) == 2:
        os.system("systemctl enable docker")
        os.system("tput setaf 2")
        print("\t\t\tService has been enabled")
        time.sleep(4)
        os.system("clear")

    elif int(d) == 3:
        os.system("systemctl status docker")
        time.sleep(4)
        os.system("clear")

    elif int(d) == 4:
        image_name = input("enter the image name : ") 
        os.system("docker pull {}".format(image_name))
        os.system("tput setaf 2")
        print("\t\t\tImage is downloaded successfully")
        time.sleep(4)
        os.system("clear")       

    elif int(d) == 5:
        attach_dtach = input("If u want terminal then type *-i* or if not type *-d* : ")
        container_name = input("enter the container name :")
        image_name = input("enter docker image name : ")
        version = input("enter the version of image : ")
        os.system("docker run {} -t --name {} {}:{}".format(attach_dtach, container_name , image_name, version))
        os.system("tput setaf 2")
        print("\t\t\tDocker container is launched successfully")
        time.sleep(4)
        os.system("clear")

    elif int(d) == 6:        
        file_or_fold_name = input("enter the file/fold name : ")
        container_name = input("enter the container name : ")
        os.system("docker cp /var/www/html/{}/  {}:/var/www/html".format(file_or_fold_name, container_name))
        os.system("tput setaf 2")
        print("\t\t\tFile/folder has been copied successfully")
        time.sleep(4)
        os.system("clear")


    elif int(d) == 7:
        container_name = input("enter the container name : ")
        os.system("docker start {}".format(container_name))
        os.system("tput setaf 2")
        print("\t\t\tDocker container is started")
        time.sleep(4)
        os.system("clear")

    elif int(d) == 8:
        container_name = input("enter the container name : ")
        os.system("docker attach {}".format(container_name))
            
    else:
        print("invalid input")
        input("please choose correct option : ")
                            
