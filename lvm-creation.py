import os
import subprocess
import time

print("            Welcome to LVM Creation            ")
print("With this Code you will create a Logical Volume")
print("-------------------------------------------------")

print("Let's first see the disks in your system : ")
time.sleep(3)
print("")
os.system("fdisk -l")

print("-------------------------------------------------")
print("")

disk  = input("Enter the disk to be converted into lvm : ")
time.sleep(3)
print("")

os.system("pvcreate " + disk)
print("")
time.sleep(1.5)
os.system("pvdisplay " + disk)


vg = input("Do you have a Volume Group ? [Y/N] : ").lower()
print("")

if vg == "y":
    name_vg = input("Enter volume group : ")
    subprocess.getoutput("vgextend " + name_vg + " " + disk)
    os.system("vgdisplay " + name_vg + " " + disk)

elif vg == "n":
    name_vg = input("Enter the name of volume group to be created : ")
    subprocess.getoutput("vgcreate " + name_vg)
    subprocess.getoutput("vgcreate " + name_vg + " " + disk)
    os.system("vgdisplay")
print("")
size = input("Enter the size of the lvm partition (with [G/M], like 10G): ")
name_lv = input("Enter the name of Logical Volume : ")
print("")
time.sleep(3)

subprocess.getoutput("lvcreate --size +" + size + " --name " + name_lv + " " + name_vg)

# subprocess.getoutput("lvcreate --size -" + size + " --name " + name_lv + " " + name_vg)
# print("\n")
subprocess.getoutput("fsadm resize /dev/" + name_vg)
print("Logical Volume Created")

print("-------------------------------------------------")
print("")
print("Let's check the Logical Volume : ")
time.sleep(3)
os.system("lvdisplay /dev/" + name_vg)
print("")
print("Logical Volume of " + size + "iB is created.")
print("-------------------------------------------------")
