import re,os
from typing import List,Tuple
class 中文小说处理类:
    from typing import List
    整数="[一二三四五六七八九十零百千万亿〇]"
    非句号 = "[\u4E00-\u9FFF，；：0-9]"
    句号 = "[\u4E00-\u9FFF，；：。！？0-9]"
    含半角 = "[\u4E00-\u9FFF，；;：:！!？?0-9\(\)（）、“”]"
    def __init__(self):
        self.中文句子=re.compile("(([\u4E00-\u9FFF，；：。！？“”]+[0-9\.,?\"\']{0,2})+)")
        self.HTML标签=re.compile("<[^<>]+>")
        self.正式章节标准格式=re.compile(".*?((\d+)卷\s*({}*))?\s*第\s?(\d+)\s?章\s*({}*)$".format(self.含半角,self.含半角))
        self.第几卷="^第\s?{}+\s?卷.*$".format(self.整数)
        self.第几章="^第\s?{}+\s?章.*$".format(self.整数)

    def 提取中文段落(self,html代码:str)->List[str]:
        fragments=re.split(self.HTML标签,html代码)
        res=[]
        for s in fragments:
            s=re.search(self.中文句子,s)
            if None!=s:
                res.append(s.group(0))
        return res

def lt2csv(L:List[Tuple],save_path):
    # if not os.path.exists(save_path):
    with open(save_path,"w",encoding='gbk') as f:
        f.writelines(map(lambda t:','.join(t),L))

# obj=中文小说处理类()
# title="凡人修仙传 第11卷 真仙降临 第2446章 飞升仙界(大结局）"
# fp=re.match(obj.正式章节标准格式,title)
# print(fp.groups())