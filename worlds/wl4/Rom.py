import hashlib
from pathlib import Path

import bsdiff4

import Utils
from BaseClasses import MultiWorld
from Patch import APDeltaPatch


MD5_US_EU = "5fe47355a33e3fabec2a1607af88a404"


class WL4DeltaPatch(APDeltaPatch):
    hash = MD5_US_EU
    game = "Wario Land 4"
    patch_file_ending = ".apwl4"

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()


class LocalRom():
    def __init__(self, file: Path, name=None, hash=None):
        self.name = name
        self.hash = hash

        patch_path = Path(__file__).parent / "data" / "basepatch.bsdiff"
        with open(file, "rb") as rom_file, open(patch_path, "rb") as patch_file:
            rom_bytes = rom_file.read()
            patch_bytes = patch_file.read()
            self.buffer = bytearray(bsdiff4.patch(rom_bytes, patch_bytes))

    def read_bit(self, address: int, bit_number: int) -> bool:
        bitflag = (1 << bit_number)
        return ((self.buffer[address] & bitflag) != 0)

    def read_byte(self, address: int) -> int:
        return self.buffer[address]

    def read_bytes(self, startaddress: int, length: int) -> bytes:
        return self.buffer[startaddress:startaddress + length]
    
    def read_halfword(self, address: int) -> int:
        assert address % 2 == 0, f"Misaligned halfword address: {address:x}"
        halfword = self.read_bytes(address, 2)
        return int.from_bytes(halfword, "little")
    
    def read_word(self, address: int) -> int:
        assert address % 4 == 0, f"Misaligned word address: {address:x}"
        word = self.read_bytes(address, 4)
        return int.from_bytes(word, "little")

    def write_byte(self, address: int, value: int):
        self.buffer[address] = value

    def write_bytes(self, startaddress: int, values):
        self.buffer[startaddress:startaddress + len(values)] = values
    
    def write_halfword(self, address: int, value: int):
        assert address % 2 == 0, f"Misaligned halfword address: {address:x}"
        halfword = value.to_bytes(2, "little")
        self.write_bytes(address, halfword)
    
    def write_word(self, address: int, value: int):
        assert address % 4 == 0, f"Misaligned word address: {address:x}"
        word = value.to_bytes(4, "little")
        self.write_bytes(address, word)

    def write_to_file(self, file: Path):
        with open(file, 'wb') as stream:
            stream.write(self.buffer)


def patch_save_data(rom: LocalRom):
    # Use the second byte of each level state word to store the boxes that have
    # been opened and looted, keeping the actual world status in the least
    # significant byte

    # ItemGetFlgSet_LoadSavestateInfo2RAM()
    rom.write_halfword(0x75E4E, 0x7849)  # ldrb r1, [r1, #1]  ; Jewel piece 1
    rom.write_halfword(0x75E78, 0x7849)  # ldrb r1, [r1, #1]  ; Jewel piece 2
    rom.write_halfword(0x75EA0, 0x7849)  # ldrb r1, [r1, #1]  ; Jewel piece 3
    rom.write_halfword(0x75EC8, 0x7849)  # ldrb r1, [r1, #1]  ; Jewel piece 4
    rom.write_halfword(0x75EF0, 0x7849)  # ldrb r1, [r1, #1]  ; CD

    # SeisanSave()
    rom.write_halfword(0x811D0, 0x7848)  # ldrb r0, [r1, #1]  ; Jewel piece 1
    rom.write_halfword(0x811D6, 0x7048)  # strb r0, [r1, #1]  ; Jewel piece 1
    rom.write_halfword(0x811F4, 0x7848)  # ldrb r0, [r1, #1]  ; Jewel piece 2
    rom.write_halfword(0x811FA, 0x7048)  # strb r0, [r1, #1]  ; Jewel piece 2
    rom.write_halfword(0x81216, 0x7848)  # ldrb r0, [r1, #1]  ; Jewel piece 3
    rom.write_halfword(0x8121C, 0x7048)  # strb r0, [r1, #1]  ; Jewel piece 3
    rom.write_halfword(0x81238, 0x7848)  # ldrb r0, [r1, #1]  ; Jewel piece 4
    rom.write_halfword(0x8123E, 0x7048)  # strb r0, [r1, #1]  ; Jewel piece 4
    rom.write_halfword(0x8125A, 0x7848)  # ldrb r0, [r1, #1]  ; CD
    rom.write_halfword(0x81260, 0x7048)  # strb r0, [r1, #1]  ; CD


# Unused; written only for my future reference
def shuffle_keyzer(rom: LocalRom, world: MultiWorld, player: int):
    # Use setting world.keyzer[player]
    rom.write_halfword(0x75F18, 0x7849)  # ldrb r1, [r1, #1]  ; ItemGetFlgSet_LoadSavestateInfo2RAM()
    rom.write_halfword(0x8127C, 0x7848)  # ldrb r0, [r1, #1]  ; SeisanSave()
    rom.write_halfword(0x81282, 0x7048)  # strb r0, [r1, #1]  ; SeisanSave()

    # TODO skip cutscene so Wario doesn't walk through locked doors


def skip_cutscenes(rom: LocalRom):
    # Intro cutscene
    rom.write_halfword(0x00312, 0x2001)  # movs r0, #1  ; MainGameLoop(): Prevent cutscene start
    rom.write_halfword(0x91944, 0x0000)  # movs r0, r0  ; GameReady(): Stop title music
    rom.write_word(0x91DA8, 0x08091DD8)  # ReadySet_SelectKey(): Don't play car engine sound

    # TODO Autosave tutorial
    # TODO Jewel cutscene

    # Post-boss cutscenes
    rom.write_halfword(0x79FDC, 0x2001)  # movs r0, #1  ; MainGameLoop(): Pyramid appears
    rom.write_halfword(0x7A030, 0x2000)  # movs r0, #0  ; MainGameLoop(): Pyramid opens


def improve_qol(rom: LocalRom):
    # Always allow S-Hard
    rom.write_halfword(0x91F8E, 0x2001)  # movs r0, r1  ; ReadySub_Level(): Allow selection 
    rom.write_halfword(0x92268, 0x2001)  # movs r0, #1  ; ReadyObj_Win1Set(): Display option 


def fill_items(rom: LocalRom, world: MultiWorld, player: int):
    for location in world.get_locations(player):
        
        itemid = location.item.code if location.item is not None else ...
        locationid = location.address
        if itemid is None or locationid is None:
            continue
        locationid = locationid & 0xFF

        if location.native_item:
            itemid = itemid & 0xFF
            offset = 0x78F97C + locationid
            rom.write_byte(offset, itemid)
        else:
            pass

def patch_rom(rom: LocalRom, world: MultiWorld, player: int):
    patch_save_data(rom)
    fill_items(rom, world, player)
    skip_cutscenes(rom)
    improve_qol(rom)


def get_base_rom_bytes(file_name: str = "") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_path = get_base_rom_path(file_name)
        base_rom_bytes = bytes(open(file_path, "rb").read())

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        if MD5_US_EU != basemd5.hexdigest():
            raise Exception("Supplied base ROM does not match US/EU version."
                            "Please provide the correct ROM version")
        
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes


def get_base_rom_path(file_name: str = "") -> Path:
    options = Utils.get_options()
    if not file_name:
        file_name = options["wl4_options"]["rom_file"]

    file_path = Path(file_name)
    if file_path.exists():
        return file_path
    else:
        return Path(Utils.local_path(file_name))
