import ROOT
import os
from itertools import ifilter

import varial.generators as gen
import varial.operations as op
import varial.rendering as rnd
import varial.tools as tools


def plot_maker(wrps):
    def set_legend(wrps):
        for w in wrps:
            w.legend = w.in_file_path[0]
            yield w
    wrps = list(set_legend(wrps))
    el = dict((w.name, w) for w in ifilter(lambda w:w.legend[:2]=='El', wrps))
    mu = dict((w.name, w) for w in ifilter(lambda w:w.legend[:2]=='Mu', wrps))
    names = filter(lambda n: not (n.endswith('Passing')
                                  or n.endswith('Denom')),
                   el.keys())
    out = []
    for n in sorted(names):
        out.append([
            el[n + 'Denom'],
            mu[n + 'Denom'],
        ])
        out.append([
            op.eff([
                el[n + 'Passing'],
                el[n + 'Denom'],
            ], 'cl=0.683 b(1,1) mode', wrp_kws={'val_y_max':1.1}),
            op.eff([
                mu[n + 'Passing'],
                mu[n + 'Denom'],
            ], 'cl=0.683 b(1,1) mode', wrp_kws={'val_y_max':1.1}),
        ])
    col = [ROOT.kGreen, ROOT.kBlue]
    return (
        gen.apply_linewidth(
            gen.apply_markercolor(
                gen.apply_linecolor(
                    grp,
                    col
                ),
                col
            )
        )
        for grp in out
    )

def plotter_factory(**kws):
    kws['plot_grouper'] = plot_maker
    kws['plot_setup'] = None
    kws['canvas_decorators'] = [rnd.Legend]
    return tools.FSPlotter(**kws)


os.system('rm -r vlq_trig')
tools.mk_plotter_chain(plotter_factory, flat=True, name='vlq_trig').run()
tools.WebCreator().run()
os.system('rm -r ~/www/vlq_trig')
os.system('cp -r vlq_trig ~/www')
