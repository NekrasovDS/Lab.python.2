n = int(input())
possible_numbers = set(range(1, n + 1))

while True:
    question = input().split()
    if question[0] == 'HELP':
        break

    question_set = set(map(int, question))
    correct_answer = 'YES' if len(question_set.intersection(possible_numbers)) > len(possible_numbers)/2 else 'NO'

    if len(question_set) == n // 2:
        correct_answer = 'NO'

    if correct_answer == 'YES':
        possible_numbers &= question_set

    print(correct_answer)

possible_numbers = sorted(list(possible_numbers))
print(" ".join(map(str, possible_numbers)))
