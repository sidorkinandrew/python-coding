import requests as r

cookies = {
"_ga": "GA1.2.xx",
"_gid": "GA1.2.xx",
"session": "xx",
"_gat": "xx"
}
task_url = "https://adventofcode.com/2022/day/10/input"

data = r.get(task_url, cookies=cookies)
data = data.text.split("\n")[:-1]

test = [
"""
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""
]

test = test[0].split('\n')[1:-1]


# Day 10

# test = [
#     'noop',
# 'addx 3',
# 'addx -5'
# ]

class Cpu:
  def __init__(self, moves):
    self.x = 1
    self.instr_ptr = 0
    self.cycle = 0
    self.active_program = moves
    self.processing = None
    self.machine_states = {}
    self.CRT = list('.'*240)
    self.append_machine_state()

  def append_machine_state(self):
    self.machine_states[self.cycle] = {
        'x': self.x,
        'instr_ptr': self.instr_ptr,
        'instr': self.active_program[self.instr_ptr],
        'cycle': self.cycle,
        'processing': self.processing,
        'CRT': self.CRT,
    }
    self.print_machine_state()

  def print_machine_state(self):
    print(self.machine_states[self.cycle])
    print(''.join(self.CRT))

  def show_sprite_position(self):
    buffer = self.CRT[:]
    buffer[self.x] = '#'
    buffer[self.x+1] = '#'
    buffer[self.x-1] = '#'
    print('x', self.x, 'cycle', self.cycle)
    print(''.join(buffer))

  def print_crt(self):
    crt = [''.join(self.CRT[i:i + 40]) for i in range(0, len(self.CRT), 40)]
    print('\n'.join(crt))

  def check_sprite_position(self):
    if abs(self.cycle % 40 - self.x) <= 1:
      return True
    else:
      return False

  def process_instructions_cpu_only(self):
    while self.instr_ptr <= len(self.active_program)-1:
      self.cycle += 1
      if 'noop' in self.active_program[self.instr_ptr]:
        self.append_machine_state()
        self.instr_ptr +=1
        continue
      self.processing = int(self.active_program[self.instr_ptr].split('addx ')[1])
      self.append_machine_state()
      self.cycle += 1
      self.append_machine_state()
      self.x += self.processing
      self.processing = None
      self.instr_ptr +=1

  def process_instructions_crt(self):
    self.cycle = -1
    while self.instr_ptr <= len(self.active_program)-1:
      self.cycle += 1
      if 'noop' in self.active_program[self.instr_ptr]:
        if self.check_sprite_position():
          self.CRT[self.cycle] = '#'
          self.show_sprite_position()
        self.append_machine_state()
        self.instr_ptr +=1
        continue
      self.processing = int(self.active_program[self.instr_ptr].split('addx ')[1])
      if self.check_sprite_position():
        self.CRT[self.cycle] = '#'
        self.show_sprite_position()
      self.append_machine_state()
      self.cycle += 1
      if self.check_sprite_position():
        self.CRT[self.cycle] = '#'      
        self.show_sprite_position()
      self.append_machine_state()
      self.x += self.processing
      self.processing = None
      self.instr_ptr +=1


cpu = Cpu(data)

# Day 10 Part I
cpu.process_instructions_cpu_only()
for i in [20, 60, 100, 140, 180, 220]:
  print(cpu.machine_states[i]['x'])

print(sum([cpu.machine_states[i]['x']*i for i in [20, 60, 100, 140, 180, 220]]))

# Day 10 Part II
cpu.process_instructions_crt()
cpu.print_crt()
