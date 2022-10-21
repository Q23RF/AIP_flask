from random import randint, choice


def wordListSum(wordList):
    sum = 0
    for value in wordList.values():
        sum += value
    return sum


def retrieveRandomWord(wordList):

    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word


def buildWordDict(fn):
    d = {}
    infile = open(fn, "r")
    body = infile.read()
    infile.close()
    addWord(body, d)
    return d


def addWord(words, wordDict):
    import jieba 
    words = words.replace("？", "")
    words = jieba.lcut(words)
    for i in range(1, len(words)):
        if words[i - 1] not in wordDict:
            wordDict[words[i - 1]] = {}
        if words[i] not in wordDict[words[i - 1]]:
            wordDict[words[i - 1]][words[i]] = 0
        wordDict[words[i - 1]][words[i]] += 1


files = ['懷古.txt', '抒情.txt', '奇詭.txt']

notfirst = "的著嗎吧呢了，。！？：；」"

no = ["●", "余光中詩集『白玉苦瓜』(九歌2008.5.1重排新版)", "\xa0\xa0\xa0\xa0", "\u3000\u3000", "\n的", "\n嗎", "(", ")", "（", "）", "」", "「", "—", "~"]


def write(n, length, fn):
    re = []
    wordDict = buildWordDict(files[fn])

    for idx in range(n):
        initialWord = choice(list(wordDict.keys()))

        text = []
        currentWord = initialWord
        i = 0
        line = ""
        while True:
            i += 1
            if currentWord not in wordDict:
                currentWord = initialWord
            currentWord = retrieveRandomWord(wordDict[currentWord])

            line += currentWord
            if len(line) > 9:
              currentWord = '\n'
            if currentWord == '\n':
              if line[0] in notfirst:
                line = line[1:]
              else:
                text.append(line)
                line = ""
                if i >= length:
                    break
        passed = True
        for n in no:
            if n in text:
                passed = False
        if passed:
            re.append(text)
    return re
