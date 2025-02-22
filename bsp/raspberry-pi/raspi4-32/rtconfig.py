import os

# toolchains options
ARCH        ='arm'
CPU         ='cortex-a'
RTT_ROOT    = os.getenv('RTT_ROOT') or r'../../..'
CROSS_TOOL  = os.getenv('RTT_CC') or 'gcc'
PLATFORM    = 'gcc'
EXEC_PATH   = os.getenv('RTT_EXEC_PATH') or r'/opt/gcc-arm-none-eabi-5_4-2016q3/bin/'
BUILD       = os.getenv('RTT_BUILD') or 'debug'

if PLATFORM == 'gcc':
    # toolchains
    # PREFIX = 'arm-none-eabi-'
    PREFIX  = os.getenv('RTT_CC_PREFIX') or 'arm-none-eabi-'
    CC      = PREFIX + 'gcc'
    CXX     = PREFIX + 'g++'
    AS      = PREFIX + 'gcc'
    AR      = PREFIX + 'ar'
    LINK    = PREFIX + 'gcc'
    TARGET_EXT = 'elf'
    SIZE    = PREFIX + 'size'
    OBJDUMP = PREFIX + 'objdump'
    OBJCPY  = PREFIX + 'objcopy'

    DEVICE = ' -march=armv8-a -mtune=cortex-a72 -ftree-vectorize -ffast-math -funwind-tables -fno-strict-aliasing'
    CXXFLAGS= DEVICE + ' -Wall'
    CFLAGS = DEVICE + ' -Wall  -std=gnu99'
    AFLAGS = ' -c' + ' -x assembler-with-cpp -D__ASSEMBLY__'
    LFLAGS  = DEVICE + ' -nostartfiles -Wl,--gc-sections,-Map=rtthread.map,-cref,-u,system_vectors -T link.lds ' + ' -lsupc++ -lgcc '
    CPATH   = ''
    LPATH   = ''

    if BUILD == 'debug':
        CFLAGS   += ' -O0 -gdwarf-2'
        CXXFLAGS += ' -O0 -gdwarf-2'
        AFLAGS   += ' -gdwarf-2'
    else:
        CFLAGS   += ' -Os'
        CXXFLAGS += ' -Os'
    CXXFLAGS += ' -Woverloaded-virtual -fno-exceptions -fno-rtti'

DUMP_ACTION = OBJDUMP + ' -D -S $TARGET > rtt.asm\n'
POST_ACTION = OBJCPY + ' -O binary $TARGET kernel7.img\n' + SIZE + ' $TARGET \n'
