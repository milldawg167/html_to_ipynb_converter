from bs4 import BeautifulSoup
import json
import codecs
import lxml

input_file = "path/to/file.html" # must be a .html file
output_file = "path/to/output_file.ipynb" # must be a .ipynb file

f = codecs.open(input_file,'r','utf-8')
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
		
open(output_file, 'w').write(json.dumps(dictionary))
