"""Provide a simple magic that emits html annotated python code to find potential perf improvements

"""

__version__ = '0.0.1'

from IPython.core.magic import cell_magic, register_cell_magic
import numba

@register_cell_magic
def numba_annotate(line, cell):
    res = "OOps"
    try:
        d =  mkdtemp()
    
        from pathlib import Path

        pd = Path(d)

        code_file = (pd /'code.py')
        html_file = (pd/'index.html')
        with code_file.open('w') as f:
            f.write(cell)
        import subprocess
        subprocess.run(['numba','--annotate-html', html_file, code_file])

        with html_file.open('r') as f:
            from IPython.display import HTML
            res = HTML(f.read())
        res
    except Exception:
        import os
        os.rmdir(d)
    
    return res


