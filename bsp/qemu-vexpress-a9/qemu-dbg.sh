if [ ! -f "sd.bin" ]; then
dd if=/dev/zero of=sd.bin bs=1024 count=65536
fi

#qemu-system-arm -M vexpress-a9 -kernel rtthread.elf -serial vc -serial vc -sd sd.bin -S -s
qemu-system-arm -M vexpress-a9 -kernel rtthread.bin -nographic -sd sd.bin -S -s

