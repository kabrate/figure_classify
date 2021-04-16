target_scores = []
nontarget_scores = []
f = open('merge_result1.csv').readlines()
#将两个数组读出来
for line in f:
    splits = line.strip().split(' ')
    print(splits)
    if splits[1] == '1':
        target_scores.append(eval(splits[0]))
    else:
        nontarget_scores.append(eval(splits[0]))

#排序,从小到大排序
target_scores = sorted(target_scores)
nontarget_scores = sorted(nontarget_scores)

print (target_scores)

target_size = len(target_scores)
target_position = 0
for target_position in range(target_size):
    nontarget_size = len(nontarget_scores)
    nontarget_n = nontarget_size * target_position * 1.0 / target_size
    nontarget_position = int(nontarget_size - 1 - nontarget_n)
    if nontarget_position < 0:
        nontarget_position = 0
    if nontarget_scores[nontarget_position] < target_scores[target_position]:
        print ("nontarget_scores[nontarget_position] is",  nontarget_position, nontarget_scores[nontarget_position])
        print ("target_scores[target_position] is",  target_position, target_scores[target_position])
        break

threshold = target_scores[target_position]
print ("threshold ",  threshold)
eer = target_position * 1.0 / target_size
print ("eer  ",  eer)
