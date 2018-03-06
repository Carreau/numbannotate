"""Provide a simple magic that emits html annotated python code to find potential perf improvements

"""

__version__ = '0.0.3'

from IPython.core.magic import cell_magic, register_cell_magic
from tempfile import mkdtemp
import numba

@register_cell_magic
def numba_annotate(line, cell):
    res = "Functions Ness to be called at least once."
    d = None
    try:
        d =  mkdtemp()
    
        from pathlib import Path

        pd = Path(d)

        code_file = (pd /'code.py')
        html_file = (pd/'frebus23.html')
        with code_file.open('w') as f:
            f.write(cell)
        import subprocess
        subprocess.run(['numba','--annotate-html', str(html_file), str(code_file)])
        if html_file.exists():
            with html_file.open('r') as f:
                from IPython.display import HTML
                res = HTML(f.read())
        res
    except Exception:
        import shutil
        shutil.rmtree(d)
        raise
    
    return res


