
import sys
sys.path.insert(0, 'transparency/SCRIPTS')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# patch savefig before importing
_orig = plt.Figure.savefig
def _patched(self, path, **kw):
    import pathlib
    p = pathlib.Path(str(path)).with_suffix('.png')
    p = p.parent / ('caption_check_' + p.name)
    kw['format'] = 'png'
    kw['dpi'] = 120
    _orig(self, p, **kw)
    print('PNG saved to', p)
plt.Figure.savefig = _patched

exec(open('transparency/SCRIPTS/fig_section6_network.py').read())
