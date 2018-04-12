import csv
import sys


def trim(row):
    last_good = len(row)-1
    for i in range(last_good, -1, -1):
        if row[i] != "":
            last_good = i
            break
    return row[:last_good+1]


class Dungeon:
    def __init__(self, file):
        self.states = []
        with open(file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != 'ID':
                    self.states.append(trim(row))

        self.current_state = 0

    def run(self):
        while True:
            # First print current state description
            print(self.get_description())
            if self.states[self.current_state][0] == 'END':
                break

            # Next take input
            cmd = input('> ')
            next_state = self.find_command(cmd)
            if next_state is None:
                print("Don't know what you talkin' about")
            else:
                self.current_state = next_state
                # Next find the command in the list of all commands

                # Move state to the correct next state

    def get_description(self):
        return self.states[self.current_state][1]

    def find_command(self, cmd):
        st = self.states[self.current_state]
        for cmd_state_idx in range(2, len(st)):
            cmd_state = st[cmd_state_idx]
            c, state = cmd_state.split('|')
            if c == cmd:
                return self.state_id(state)
        return None

    def state_id(self, state):
        for index, s in enumerate(self.states):
            if s[0] == state:
                return index
        return None


def main():
    dungeon = Dungeon(sys.argv[1])
    dungeon.run()


if __name__ == "__main__":
    main()
