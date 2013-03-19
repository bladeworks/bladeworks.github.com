# Raspberry PI archlinux backup/restore on MAC os

## Backup

```
sudo dd bs=1m if=/dev/rdiskX of=arch.img
```

Please replace the X with the disk number. And using raw disk is much faster. You can use ctrl+t to view the progress.

## Restore

```
sudo dd bs=1m if=arch.img of=/dev/rdiskX
```

It's a reverse process of backup. Please make sure that no partition is mounted.