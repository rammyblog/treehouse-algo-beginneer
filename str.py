def stringMatching(words):
    final_list = []
    for i in range(len(words)):
        for word in words:
            # print(word, words[i])
            # print(word.find(words[i]))
            if words[i] != word and word.find(words[i]) > -1 and not words[i] in final_list :
                print(word, words[i])
                final_list.append(words[i])
    return final_list


print(stringMatching(["leetcoder","leetcode","od","hamlet","am"]))
