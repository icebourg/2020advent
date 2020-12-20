def parse_answers(file_name):
    answers = []

    with open(file_name) as input:
        answer = []
        for l in input:
            line = l.strip()
            answer.append(line)

            # this is a blank line, then the previous lines are part of a single group
            if line == "":
                answers.append(answer)
                answer = []
    return answers

def count_answers(answer_group, only_if_unanimous=False):
    answer_keys = {}


    for a in "".join(answer_group):
        if a in answer_keys:
            answer_keys[a] += 1
        else:
            answer_keys[a] = 1

    if only_if_unanimous:
        test_dict = answer_keys.copy()
        for k in test_dict:
            if answer_keys[k] != len(answer_group) - 1:
                del answer_keys[k]
    
    return answer_keys

if __name__ == "__main__":
    test_answers = parse_answers("./test_input")
    total = 0
    for a in test_answers:
        total += len(count_answers(a))
    
    print("The total for the test input is %d " % (total))

    answers = parse_answers("./input")
    total = 0
    for a in answers:
        total += len(count_answers(a))
    
    print("The total for part 1 is %d " % (total))

    total = 0
    for a in test_answers:
        total += len(count_answers(a, True))
    
    print("The total for part 2 test input is %d " % (total))

    total = 0
    for a in answers:
        total += len(count_answers(a, True))
    
    print("The total for part 2 input is %d " % (total))

    