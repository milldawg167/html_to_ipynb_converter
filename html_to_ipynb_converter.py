from bs4 import BeautifulSoup
import json
import codecs
import lxml

response = "C:/Users/andre/Documents/CQF/Python_Labs/Introduction to Financial Time Series/01-Financial-Timeseries.html"
f = codecs.open(response,'r','utf-8')
text = f.read()

soup = BeautifulSoup(text, 'lxml')

dictionary = {'nbformat': 4,
		  'nbformat_minor': 2,
		  'cells': [],
		  'metadata': {"kernelspec":{"display_name": "Python 3",
						     "language": "python",
						     "name": "python3"}
  }}

for d in soup.find_all("div"):
    if 'class' in d.attrs.keys():
        for clas in d.attrs["class"]:
            if clas in ["CodeMirror", "jp-MarkdownCell"]:
                # code cell
                if clas == "CodeMirror":
                    cell = {}
                    cell['metadata'] = {}
                    cell['outputs'] = []
                    cell['source'] = [d.get_text()]
                    cell['execution_count'] = None
                    cell['cell_type'] = 'code'
                    dictionary['cells'].append(cell)

                else:
                    cell = {}
                    cell['metadata'] = {}

                    cell['source'] = [d.decode_contents()]
                    cell['cell_type'] = 'markdown'
                    dictionary['cells'].append(cell)
open('C:/Users/andre/Downloads/notebook.ipynb', 'w').write(json.dumps(dictionary))