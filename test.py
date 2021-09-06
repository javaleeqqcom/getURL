import re
# path=".\\content.txt"
path=".\\test2.txt"
# 中文段落=re.compile("<[^<>]+>\s*(([\u4E00-\u9FFF，；：。！？“”]+[0-9\.,?\"\']{0,2})+)\s*<[^<>]+>")
中文句子=re.compile("(([\u4E00-\u9FFF，；：。！？“”]+[0-9\.,?\"\']{0,2})+)")
HTML标签=re.compile("<[^<>]+>")

class 中文小说处理类:
    from typing import List
    def __init__(self):
        self.中文句子=re.compile("(([\u4E00-\u9FFF，；：。！？“”]+[0-9\.,?\"\']{0,2})+)")
        self.HTML标签=re.compile("<[^<>]+>")

    def 提取中文段落(self,html代码:str)->List[str]:
        fragments=re.split(self.HTML标签,html代码)
        res=[]
        for s in fragments:
            s=re.search(self.中文句子,s)
            if None!=s:
                res.append(s.group(0))
        return res

pclass=中文小说处理类()
with open(path,"r",encoding="utf-8") as f:
    content=f.read()
    print(content)
    res=pclass.提取中文段落(content)
    for s in res:
        print(s)