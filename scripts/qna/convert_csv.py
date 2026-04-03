import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
i=0
for row in reader:
    if len(row) >= 4 and row[3] == 'disable': continue;
    i+=1
    ref=f" <<{row[2]},icon:link[]>>" if len(row)>=3 and row[2] else ""
    print("""\
[.qna.question]#{count}. {question}#
ifdef::backend-html5[[.qna.answer_label]#Resposta icon:hand-pointer[]#]
[.qna.answer_value.hidden]#{answer}{ref}#
""".format(count=i, question=row[0], answer=row[1], ref=ref))
