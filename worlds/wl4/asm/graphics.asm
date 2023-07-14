.gba

.autoregion
.align 2
PassagePaletteTable:
    .halfword 0x7B3E, 0x723C, 0x6576, 0x58B0, 0x4C07  ; Entry passage
    .halfword 0x5793, 0x578D, 0x4B20, 0x2E40, 0x1160  ; Emerald passage
    .halfword 0x6B5F, 0x529F, 0x253F, 0x14B4, 0x14AE  ; Ruby passage
    .halfword 0x6BDF, 0x23DF, 0x139B, 0x1274, 0x0DAE  ; Topaz passage
    .halfword 0x7F5A, 0x7E94, 0x7D29, 0x50A5, 0x38A5  ; Sapphire passage
    .halfword 0x579F, 0x3B1F, 0x1A7F, 0x05DE, 0x00FB  ; Golden pyramid
    .halfword 0x3D9C, 0x327D, 0x2B28, 0x6A3B, 0x6DED  ; Archipelago item

.definelabel @ObjectPalette4, 0x5000280

; Set the end of object palette 4 to the colors matching the passage in r0
SetTreasurePalette:
    ldr r1, =PassagePaletteTable
    lsl r2, r0, #2
    add r0, r2, r0
    lsl r0, r0, #1
    add r0, r1, r0

; DMA transfer - 5 halfwords from palette table entry
    ldr r1, =REG_DMA3SAD
    str r0, [r1]
    ldr r0, =@ObjectPalette4 + 0x296 - 0x280
    str r0, [r1, #4]
    ldr r0, =0x80000005
    str r0, [r1, #8]
    ldr r0, [r1, #8]

    mov pc, lr
.pool

.align 2
APLogoObj:
    .halfword 1, 0xF8, 0x41F8, 0x412E

.align 4
APLogoAnm:
    .word APLogoObj
    .byte 0xC8
    .fill 0, 3
    .word 0, 0
.endautoregion


; Store letters and AP logo in some unused space in the tile data near the jewels
; and such. WL4 stores graphics data in 4bpp uncompressed format.

; Interestingly, graphics are considered as a stream of nybbles (that is, the left
; pixel is the least significant half byte), which means that the easiest way to
; write them is as eight words, such that the hexits appear mirrored in the assembly
; compared to how they look in the final game

.org 0x8401C68
TextTile0:
TextTileO:
    .word 0x03333333
    .word 0x03111113
    .word 0x03133313
    .word 0x03130313
    .word 0x03130313
    .word 0x03133313
    .word 0x03111113
    .word 0x03333333

TextTile1:
    .word 0x00033300
    .word 0x00031330
    .word 0x00031130
    .word 0x00031330
    .word 0x00031300
    .word 0x00331330
    .word 0x00311130
    .word 0x00333330

TextTile2:
    .word 0x03333333
    .word 0x03111113
    .word 0x03133333
    .word 0x03111113
    .word 0x03333313
    .word 0x03333313
    .word 0x03111113
    .word 0x03333333

TextTile3:
    .word 0x03333333
    .word 0x03111113
    .word 0x03133333
    .word 0x03111113
    .word 0x03133333
    .word 0x03133333
    .word 0x03111113
    .word 0x03333333

TextTile4:
    .word 0x03330333
    .word 0x03130313
    .word 0x03133313
    .word 0x03111113
    .word 0x03133333
    .word 0x03130000
    .word 0x03130000
    .word 0x03330000

TextTile5:
TextTileS:
    .word 0x03333333
    .word 0x03111113
    .word 0x03333313
    .word 0x03111113
    .word 0x03133333
    .word 0x03133333
    .word 0x03111113
    .word 0x03333333

TextTile6:
    .word 0x03333333
    .word 0x03111113
    .word 0x03333313
    .word 0x03111113
    .word 0x03133313
    .word 0x03133313
    .word 0x03111113
    .word 0x03333333

TextTile7:
    .word 0x03333333
    .word 0x03111113
    .word 0x03133333
    .word 0x03313300
    .word 0x00331300
    .word 0x00031300
    .word 0x00031300
    .word 0x00033300

TextTile8:
    .word 0x03333333
    .word 0x03111113
    .word 0x03133313
    .word 0x03111113
    .word 0x03133313
    .word 0x03133313
    .word 0x03111113
    .word 0x03333333

TextTile9:
    .word 0x03333333
    .word 0x03111113
    .word 0x03133313
    .word 0x03111113
    .word 0x03133333
    .word 0x03133333
    .word 0x03111113
    .word 0x03333333

TextTileA:
    .word 0x03333333
    .word 0x03111113
    .word 0x03133313
    .word 0x03111113
    .word 0x03133313
    .word 0x03130313
    .word 0x03130313
    .word 0x03330333

TextTileB:
    .word 0x00333333
    .word 0x03311113
    .word 0x03133313
    .word 0x03311113
    .word 0x03133313
    .word 0x03133313
    .word 0x03311113
    .word 0x00333333

TextTileC:
    .word 0x03333333
    .word 0x03111113
    .word 0x03333313
    .word 0x00000313
    .word 0x00000313
    .word 0x03333313
    .word 0x03111113
    .word 0x03333333

TextTileD:
    .word 0x00333333
    .word 0x03311113
    .word 0x03133313
    .word 0x03130313
    .word 0x03130313
    .word 0x03133313
    .word 0x03311113
    .word 0x00333333

.org 0x84020A8
APLogoTile1:
    .word 0x50000000
    .word 0xB5000000
    .word 0xBB555000
    .word 0xB5888500
    .word 0x58888850
    .word 0x58888850
    .word 0x58555850
    .word 0x05FFF500

APLogoTile2:
    .word 0x00000055
    .word 0x000005BB
    .word 0x00555BBB
    .word 0x05DDD5BB
    .word 0x5DDDDD5B
    .word 0x5DDDDD5B
    .word 0x5D555D55
    .word 0x05EEE500

TextTileE:
    .word 0x03333333
    .word 0x03111113
    .word 0x03333313
    .word 0x00311113
    .word 0x00333313
    .word 0x03333313
    .word 0x03111113
    .word 0x03333333

TextTileF:
    .word 0x03333333
    .word 0x03111113
    .word 0x03333313
    .word 0x00311113
    .word 0x00333313
    .word 0x00000313
    .word 0x00000313
    .word 0x00000333

TextTileG:
    .word 0x03333333
    .word 0x03111113
    .word 0x03333313
    .word 0x03111313
    .word 0x03133313
    .word 0x03133313
    .word 0x03111113
    .word 0x03333333

TextTileH:
    .word 0x03330333
    .word 0x03130313
    .word 0x03133313
    .word 0x03111113
    .word 0x03133313
    .word 0x03130313
    .word 0x03130313
    .word 0x03330333

TextTileI:
    .word 0x00333330
    .word 0x00311130
    .word 0x00331330
    .word 0x00031300
    .word 0x00031300
    .word 0x00331330
    .word 0x00311130
    .word 0x00333330

TextTileJ:
    .word 0x03330000
    .word 0x03130000
    .word 0x03130000
    .word 0x03130000
    .word 0x03130333
    .word 0x03133313
    .word 0x03111113
    .word 0x03333333

TextTileK:
    .word 0x03330333
    .word 0x03133313
    .word 0x03313313
    .word 0x00331113
    .word 0x03313313
    .word 0x03133313
    .word 0x03133313
    .word 0x03330333

TextTileL:
    .word 0x00000333
    .word 0x00000313
    .word 0x00000313
    .word 0x00000313
    .word 0x00000313
    .word 0x03333313
    .word 0x03111113
    .word 0x03333333

TextTileM:
TextTileW:
    .word 0x03330333
    .word 0x03133313
    .word 0x03113113
    .word 0x03131313
    .word 0x03133313
    .word 0x03130313
    .word 0x03130313
    .word 0x03330333

.org 0x84024A8
APLogoTile3:
    .word 0x5FFFFF50
    .word 0x5FFFFF50
    .word 0xC5FFFF50
    .word 0xCC5FF500
    .word 0xCC555000
    .word 0xCC500000
    .word 0xC5000000
    .word 0x50000000

APLogoTile4:
    .word 0x5EEEEE50
    .word 0x5EEEEE55
    .word 0x5EEEE5CC
    .word 0x05EE5CCC
    .word 0x00555CCC
    .word 0x00005CCC
    .word 0x000005CC
    .word 0x00000055

TextTileN:
    .word 0x03330333
    .word 0x03133313
    .word 0x03133113
    .word 0x03131313
    .word 0x03113313
    .word 0x03133313
    .word 0x03130313
    .word 0x03330333

TextTileP:
    .word 0x03333333
    .word 0x03111113
    .word 0x03133313
    .word 0x03111113
    .word 0x03333313
    .word 0x00000313
    .word 0x00000313
    .word 0x00000333

TextTileQ:
    .word 0x03333333
    .word 0x03311133
    .word 0x03133313
    .word 0x03133313
    .word 0x03131313
    .word 0x03313313
    .word 0x03131133
    .word 0x03333333

TextTileR:
    .word 0x00333333
    .word 0x03311113
    .word 0x03133313
    .word 0x03311113
    .word 0x03133313
    .word 0x03130313
    .word 0x03130313
    .word 0x03330333

TextTileT:
    .word 0x03333333
    .word 0x03111113
    .word 0x03331333
    .word 0x00031300
    .word 0x00031300
    .word 0x00031300
    .word 0x00031300
    .word 0x00033300

TextTileU:
    .word 0x03330333
    .word 0x03130313
    .word 0x03130313
    .word 0x03130313
    .word 0x03130313
    .word 0x03133313
    .word 0x03111113
    .word 0x03333333

TextTileV:
    .word 0x03330333
    .word 0x03130313
    .word 0x03130313
    .word 0x03133313
    .word 0x03313133
    .word 0x00313130
    .word 0x00331330
    .word 0x00033300

TextTileX:
    .word 0x03330333
    .word 0x03133313
    .word 0x03313133
    .word 0x00331330
    .word 0x03313133
    .word 0x03133313
    .word 0x03130313
    .word 0x03330333

TextTileY:
    .word 0x03330333
    .word 0x03133313
    .word 0x03313133
    .word 0x00331330
    .word 0x00031300
    .word 0x00031300
    .word 0x00031300
    .word 0x00033300

.org 0x8402848
TextTileZ:
    .word 0x03333333
    .word 0x03111113
    .word 0x03113333
    .word 0x03311330
    .word 0x00331133
    .word 0x03333113
    .word 0x03111113
    .word 0x03333333
