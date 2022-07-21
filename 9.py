class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, total_mem_slots = 4, mem_slots=[]) -> None:
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots[:total_mem_slots]
        self.total_mem_slots = total_mem_slots

    def get_config(self):
        return [f'Материнская плата: {self.name}',
        f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
        f'Слотов памяти: {self.total_mem_slots}','Память:'+ ''.join([f' {f.name} - {f.volume}'+ (';' if i < (len(self.mem_slots)-1) else '') for i,f in enumerate(self.mem_slots)])]

cpu = CPU('CORE i3',2048)
mem1 = Memory('Kingston',4096) 
mem2 = Memory('Samsung',8192)
mb = MotherBoard('NTX', cpu, 4, [mem1, mem2])

print(mb.get_config())
