'''
import os
if os.getcwd()[-5:] != 'train':
    os.chdir('./train')
print(os.getcwd())
'''

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
    import jieba  # 加入結巴
    words = words.replace("？", "")
    words = jieba.lcut(words)  # 結巴要秀了
    for i in range(1, len(words)):
        if words[i - 1] not in wordDict:
            #Create a new dictionary for this word
            wordDict[words[i - 1]] = {}
        if words[i] not in wordDict[words[i - 1]]:
            wordDict[words[i - 1]][words[i]] = 0
        wordDict[words[i - 1]][words[i]] += 1


files = ['ygz.txt', 'xmr.txt', 'lf.txt']

notfirst = ["裏", "著", "的", "嗎", "吧", "，", "。"]

no = [
    "●", "———", "余光中詩集『白玉苦瓜』(九歌2008.5.1重排新版)", "\xa0\xa0\xa0\xa0",
    "\u3000\u3000", "\n的", "\n嗎", "(", ")", "（", "）", "」", "「", "高僧"
]


def write(n, length, fn):
    re = ""
    wordDict = buildWordDict(files[fn])

    # 產生n首詩，挑出押韻最多的一首
    poem = ""
    value = 0

    # 紀錄
    midx, mvalue = 0, 0
    # 以下做n次
    for idx in range(n):
        #Generate text of length 100
        initialWord = choice(list(wordDict.keys()))
        while initialWord in notfirst:
            initialWord = choice(list(wordDict.keys()))

        text = ""
        currentWord = initialWord
        i = 0
        wpl = 0
        while True:
            i += 1
            if currentWord not in wordDict:
                currentWord = initialWord
            currentWord = retrieveRandomWord(wordDict[currentWord])

            if currentWord == '\n':
                wpl = 0
            else:
                wpl += 1

            if wpl > 15:
                currentWord = '\n'

            text += currentWord
            if currentWord == '\n' and i >= length:
                break
        passed = True
        for n in no:
            if n in text:
                passed = False
        if passed:
            re += text + "\n"
            re += "------------------------\n"
    return re
