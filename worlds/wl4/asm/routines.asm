.gba


hook 0x8000728, 0x8000738, PreGamePrep

; Initialize randomizer variables
.autoregion
.align 2
PreGamePrep:
; Copy deathlink option from ROM
    ldr r0, =DeathLinkFlag
    ldrb r0, [r0]
    ldr r4, =DeathlinkEnabled
    strb r0, [r4]

; Reset incoming item
    ldr r4, =MultiworldState
    mov r0, #0
    strb r0, [r4]
    ldr r4, =TextTimer
    strb r0, [r4]

; Replaced code
    ldr r0, =KeyPressContinuous
    strh r7, [r0]
    ldr r0, =KeyPressPrevious
    strh r7, [r0]
    ldr r4, =usTrg_KeyPress1Frame
    strh r7, [r4]
    ldr r0, =sGameSeq
    strh r7, [r0]

    mov pc, lr
.pool
.endautoregion


; Hook into GameSelect() case 2
.org 0x80799E0
.word PyramidScreen

.autoregion
.align 2
; Receive multiworld items (level select)
PyramidScreen:
    push {r4}

    bl ReceiveNextItem
    mov r4, r0
    bl GiveItem
    mov r0, r4

; If we get treasure, tell the player
    lsl r0, r4, #31-6
    lsr r0, r4, #31-6
    cmp r0, #0
    bne @@Return
    mov r0, r4
    bl ItemReceivedFeedbackSound

@@Return:
    pop {r4}
    ldr r0, =0x8079AE0
    mov pc, r0
.pool
.endautoregion


; Hook into GameMain() case 2
.org 0x801B8EC
.word LevelScreen

.autoregion
.align 2
; Receive multiworld items and collect junk (in level)
LevelScreen:
    push {r4}

; If Wario isn't in a playable state, don't bother yet
    ldr r0, =usWarStopFlg
    ldrh r0, [r0]
    cmp r0, #0
    bne @@Return

    bl ReceiveNextItem
    mov r4, r0
    bl GiveItem

; If we get treasure, tell the player
    lsl r0, r4, #31-6
    lsr r0, r0, #31
    cmp r0, #0
    bne @@CollectJunk

    mov r0, r4
    bl ItemReceivedFeedbackSound
    lsl r0, r4, #31-4
    lsr r0, r0, #31-2
    bl SetTreasurePalette
    lsr r0, r4, #5
    bl SpawnCollectionIndicator
    bl LoadReceivedText

@@CollectJunk:
    bl CollectJunkItems

@@Return:
    pop {r4}
    ldr r0, =0x801B950
    mov pc, r0
.pool
.endautoregion


; Hook into the end of GameMain() case 2
hook 0x801BB7A, 0x801BB90, LoadTextSprites

.autoregion
LoadTextSprites:
    push {lr}

; Displaced instructions, up to enemies
    ldrb r0, [r4]
    cmp r0, #0
    bne @@EnemyDisplay
    call_using r0, GmWarioCreate
@@EnemyDisplay:
    call_using r0, EnemyDisplayMain

    ldr r0, =MultiworldState
    ldrb r0, [r0]
    lsl r0, r0, #2
    ldr r1, =@@MWStateTable
    add r1, r0, r1
    ldr r1, [r1]
    mov pc, r1

.align 4
@@MWStateTable:
    .word @@Return
    .word @@Return
    .word @@DrawReceivedText
    .word @@DrawSentText

@@DrawReceivedText:
    mov r0, #1
    b @@LoadText
@@DrawSentText:
    mov r0, #0
@@LoadText:
    bl CreateTextOAM
    
; Count the timer
    ldr r0, =TextTimer
    ldrb r1, [r0]
    cmp r1, #0
    beq @@Clear
    sub r1, #1
    strb r1, [r0]
    b @@Return
@@Clear:
    ldr r0, =MultiworldState
    strb r1, [r0]

@@Return:
; Displaced instructions, continued
    call_using r0, ClearOamBuf
    call_using r0, GmapSceneCreate

    pop {pc}
.pool

.endautoregion
