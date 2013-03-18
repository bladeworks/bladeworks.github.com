# How to resize the SD card for Raspberry PI

* Login as root:

```
fdisk /dev/mmcblk0
```

* Delete the second partition of /dev/mmcblk0

```
d
2
```

* Create a new primary partition and use default sizes prompted (full size)

```
n
p
2
Enter
Enter
```

* Save and exit fdisk

```
w
```

* Reboot and run:

```
resize2fs /dev/mmcblk0p2
```

