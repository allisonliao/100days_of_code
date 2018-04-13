import csv
import sys


class Room:
    def __init__(self, row):
        self.data = self._trim(row)

    def name(self):
        return self.data[0]

    def description(self):
        return self.data[1]

    def has_lock(self):
        return '|' in self.data[2] and self.data[2].startswith('lock')

    def has_item(self):
        return self.data[2].startswith('key')

    def get_item(self):
        if self.has_item():
            return self.data[2]

    def is_locking(self, direction, player):
        lock_name, di = self.data[2].split('|')
        if di == direction:
            if player.has_key_for_lock(lock_name):
                print("You unlocked the lock with a key")
                return False
            else:
                return True
        return False

    def parse_command(self, cmd, player):
        c0 = cmd.split(' ')[0]

        # Handle actions
        if c0 == 'take' or c0 == 'pickup' or c0 == 'collect':
            if self.has_item():
                player.add_to_inventory(self.get_item())
                print("You picked up the key")
                return ''
            else:
                return None

        # Check locks for exits
        if self.has_lock() and self.is_locking(cmd, player):
            print("That direction is locked")
            return ''

        # Moving to next room
        for cmd_state_idx in range(3, len(self.data)):
            cmd_state = self.data[cmd_state_idx]
            c, room_name = cmd_state.split('|')
            if c == cmd:
                return room_name
        return None

    def is_exit(self):
        return self.name() == 'E'

    @staticmethod
    def _trim(row):
        last_good = len(row)-1
        for i in range(last_good, -1, -1):
            if row[i] != "":
                last_good = i
                break
        return row[:last_good+1]


class Player:
    def __init__(self):
        self.inventory = {}

    def add_to_inventory(self, item):
        self.inventory[item] = True

    def has_key_for_lock(self, lock_name):
        key_name = lock_name.replace('lock', 'key')
        return key_name in self.inventory


class Dungeon:
    def __init__(self, file):
        self.rooms = []
        self.player = Player()
        with open(file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != 'Name':
                    self.rooms.append(Room(row))

        self.current_room = self.rooms[0]

    def run(self):
        while True:
            # First print current state description
            print(self.current_room.description())
            if self.current_room.is_exit():
                break

            # Next take input
            cmd = input('> ')
            next_room_name = self.current_room.parse_command(cmd, self.player)
            if next_room_name is None:
                print("Don't know what you talkin' about")
            else:
                next_room = self.locate_room(next_room_name)
                if next_room is not None:
                    self.current_room = next_room

    def locate_room(self, room_name):
        for room in self.rooms:
            if room.name() == room_name:
                return room

        return None


def main():
    dungeon = Dungeon(sys.argv[1])
    dungeon.run()


if __name__ == "__main__":
    main()
