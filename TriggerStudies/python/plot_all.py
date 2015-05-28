#!/usr/bin/env python

import ROOT
import varial
import varial.tools

varial.settings.max_num_processes = 1
varial.raise_root_error_level()


def plot_maker(wrps):
    def set_legend_and_color(wrps):
        for w in wrps:
            w.legend = w.in_file_path.split('/')[0]
            if w.legend[:2]=='El':
                w.primary_object().SetMarkerColor(ROOT.kRed)
                w.primary_object().SetLineColor(ROOT.kRed)
            elif w.legend[:2]=='Mu':
                w.primary_object().SetMarkerColor(ROOT.kBlue)
                w.primary_object().SetLineColor(ROOT.kBlue)
            w.val_y_max = 1.1
            yield w

    wrps = varial.gen.gen_make_eff_graphs(wrps, 'Passing', 'Denom', 'Eff')
    wrps = set_legend_and_color(wrps)
    wrps = varial.gen.gen_noex_norm_to_integral(wrps)
    return wrps


def plot_grouper(wrps):
    group_key = lambda w: w.name
    wrps = sorted(wrps, key=group_key)
    wrps = varial.gen.group(wrps, group_key)
    return wrps


def plotter_factory(**kws):
    kws['hook_loaded_histos'] = plot_maker
    kws['plot_setup'] = None
    kws['plot_grouper'] = plot_grouper
    kws['canvas_decorators'] = [varial.rnd.Legend]
    return varial.tools.Plotter(**kws)


varial.tools.mk_rootfile_plotter(
    plotter_factory=plotter_factory,
    flat=True,
    name='vlq_trig'
).run()
varial.tools.WebCreator().run()
