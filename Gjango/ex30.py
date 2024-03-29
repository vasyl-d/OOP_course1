'''В строке s букв нижнего регистра есть буквы которые повторяясь идут друг за другом.

Например, строка s = "abbxxxxzyy" и группы "a", "bb", "xxxx", "z" и "yy".

Группа идентифицируется интервалом [start, end], где start и end обозначают начальный 
и конечный индексы (включительно) группы. В приведенном выше примере "xxxx" имеет интервал [3,6].

Группа считается большой, если она имеет 3 или более символов.

Верните интервалы каждой большой группы, отсортированные в порядке возрастания по стартовому индексу.

Групп может быть несколько.'''

s = input()
seq = []
cur_seq = [0, 0]
l = len(s)
cur_pos = 1
while cur_pos < l:
    while cur_pos < l and s[cur_pos] == s[cur_pos-1]:
        cur_seq[1] = cur_pos
        cur_pos += 1
    if cur_seq[1] - cur_seq[0] >=2:
        seq.append(cur_seq)
    cur_seq = [cur_pos, cur_pos]
    cur_pos += 1

print(seq)

