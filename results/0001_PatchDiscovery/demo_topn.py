import sys,os
sys.path.append('/home/rohytg/Software/PyHTMLWriter/src');
from Element import Element
from TableRow import TableRow
from Table import Table
from TableWriter import TableWriter

corpus = '../../dataset/PALn1KHayesDistractors/corpus/'

def formElt(match):
  temp = match.split(':')
  e = Element()
  box = [float(el) for el in temp[1].split(',')]
  e.addImg(os.path.join('..', corpus, temp[0]), bboxes=[box])
  e.addTxt(temp[2])
  return e

methods = ['gt', 'svr_linear_10000', 'svr_rbf_10000', 'svr_poly_10000']
t = Table()
r = TableRow(isHeader = True)
r.addElement(Element('Sno'))
for m in methods:
  r.addElement(Element(m))

t.addRow(r)
for i in range(121, 238):
  r = TableRow(rno=i)
  for m in methods:
    with open('all_top_patches/' + m + '/' + str(i) + '.txt') as f:
      lines = f.read().splitlines()
    boxes = []
    for line in lines[:5]:
      temp = line.split(';')
      if float(temp[2]) < 0.5:
        break;
      qbox = [float(el) for el in temp[1].split(',')]
      boxes.append(qbox)
    e = Element()
    e.addImg(os.path.join('..', corpus, temp[0]), bboxes=boxes)
#    e.addTxt('score: ' + temp[2])
    r.addElement(e)
  t.addRow(r)
tw = TableWriter(t, 'out_topn')
tw.write()

