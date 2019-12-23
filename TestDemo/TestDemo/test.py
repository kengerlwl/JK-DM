from scrapy import cmdline
import  os
ans = '热血'

ans = ans.encode('gbk')
text = str(ans)
text = text.replace('\\x','%' )
text = text.replace('\'', '')
t = list(text)
t.pop(0)
text = ''.join(t)
print(text)
