# font_en_seg7.py
# Display charactors library for segment LED, some letters
# may looks unreadable, but trust me that's already the best
# that a segment LED can do.

# Segment definition in MAX7219 SEG registers
segA = 6
segB = 5
segC = 4
segD = 3
segE = 2
segF = 1
segG = 0
segDP = 7

# Segment table of 0~9 & a~f.
data =  {" " : 0x00,                                                                                \
         "0" : ((1<<segA) + (1<<segB) + (1<<segC) + (1<<segD) + (1<<segE) + (1<<segF)),             \
         "1" : ((1<<segB) + (1<<segC)),                                                             \
         "2" : ((1<<segA) + (1<<segB) + (1<<segD) + (1<<segE) + (1<<segG)),                         \
         "3" : ((1<<segA) + (1<<segB) + (1<<segC) + (1<<segD) + (1<<segG)),                         \
         "4" : ((1<<segB) + (1<<segC) + (1<<segF) + (1<<segG)),                                     \
         "5" : ((1<<segA) + (1<<segC) + (1<<segD) + (1<<segF) + (1<<segG)),                         \
         "6" : ((1<<segA) + (1<<segC) + (1<<segD) + (1<<segE) + (1<<segF) + (1<<segG)),             \
         "7" : ((1<<segA) + (1<<segB) + (1<<segC)),                                                 \
         "8" : ((1<<segA) + (1<<segB) + (1<<segC) + (1<<segD) + (1<<segE) + (1<<segF) + (1<<segG)), \
         "9" : ((1<<segA) + (1<<segB) + (1<<segC) + (1<<segD) + (1<<segF) + (1<<segG)),             \
         "a" : ((1<<segA) + (1<<segB) + (1<<segC) + (1<<segE) + (1<<segF) + (1<<segG)),             \
         "b" : ((1<<segC) + (1<<segD) + (1<<segE) + (1<<segF) + (1<<segG)),                         \
         "c" : ((1<<segD) + (1<<segE) + (1<<segG)),                                                 \
         "d" : ((1<<segB) + (1<<segC) + (1<<segD) + (1<<segE) + (1<<segG)),                         \
         "e" : ((1<<segA) + (1<<segD) + (1<<segE) + (1<<segF) + (1<<segG)),                         \
         "f" : ((1<<segA) + (1<<segE) + (1<<segF) + (1<<segG)),                                     \
         "g" : ((1<<segA) + (1<<segB) + (1<<segC) + (1<<segD) + (1<<segF) + (1<<segG)),             \
         "h" : ((1<<segC) + (1<<segE) + (1<<segF) + (1<<segG)),                                     \
         "i" : ((1<<segE) + (1<<segF)),                                                             \
         "j" : ((1<<segB) + (1<<segC) + (1<<segD)),                                                 \
         "k" : ((1<<segA) + (1<<segC) + (1<<segE) + (1<<segF) + (1<<segG)),                         \
         "l" : ((1<<segD) + (1<<segE) + (1<<segF)),                                                 \
         "m" : ((1<<segA) + (1<<segC) + (1<<segE) + (1<<segG)),                                     \
         "n" : ((1<<segC) + (1<<segE) + (1<<segG)),                                                 \
         "o" : ((1<<segC) + (1<<segD) + (1<<segE) + (1<<segG)),                                     \
         "p" : ((1<<segA) + (1<<segB) + (1<<segE) + (1<<segF) + (1<<segG)),                         \
         "q" : ((1<<segA) + (1<<segB) + (1<<segC) + (1<<segF) + (1<<segG)),                         \
         "r" : ((1<<segE) + (1<<segG)),                                                             \
         "s" : ((1<<segA) + (1<<segC) + (1<<segD) + (1<<segF) + (1<<segG)),                         \
         "t" : ((1<<segD) + (1<<segE) + (1<<segF) + (1<<segG)),                                     \
         "u" : ((1<<segB) + (1<<segC) + (1<<segD) + (1<<segE) + (1<<segF)),                         \
         "v" : ((1<<segC) + (1<<segD) + (1<<segE)),                                                 \
         "w" : ((1<<segB) + (1<<segD) + (1<<segF) + (1<<segG)),                                     \
         "x" : ((1<<segB) + (1<<segC) + (1<<segE) + (1<<segF) + (1<<segG)),                         \
         "y" : ((1<<segB) + (1<<segC) + (1<<segD) + (1<<segF) + (1<<segG)),                         \
         "z" : ((1<<segA) + (1<<segB) + (1<<segD) + (1<<segE) + (1<<segG)),                         \
         "-" : ((1<<segG)),                                                                         \
         }
