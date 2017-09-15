from summarizer import textranker

doc=open("messages.txt","r",encoding='utf-8')
document=doc.read()
textranker(document)
