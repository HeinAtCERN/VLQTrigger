import ROOT
import os

import varial.tools as tools
import varial.operations as op


def plot_maker(wrps):
    wrps = dict((w.name, w) for w in wrps)
    names = filter(lambda n: not (n.endswith('Passing')
                                  or n.endswith('Denom')),
                   wrps.keys())
    out = []
    for n in names:
        out.append(wrps[n + 'Denom'])
        out.append(op.eff([
            wrps[n + 'Passing'],
            wrps[n + 'Denom'],
        ], 'cl=0.683 b(1,1) mode'))
        out[-1].val_y_max = 1.1
        # out[-1].val_x_max = out[-2].histo.GetXaxis().GetXmax()
    return out

def plotter_factory(**kws):
    kws['plot_grouper'] = None
    kws['plot_setup'] = plot_maker
    return tools.FSPlotter(**kws)


os.system('rm -r RootFilePlots')
tools.mk_plotter_chain(plotter_factory).run()
tools.WebCreator().run()
os.system('rm -r ~/www/RootFilePlots')
os.system('cp -r RootFilePlots ~/www')
