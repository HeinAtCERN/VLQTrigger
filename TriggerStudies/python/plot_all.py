#!/usr/bin/env python

import ROOT
import varial
import varial.tools

#varial.settings.max_num_processes = 1
varial.raise_root_error_level()
varial.settings.defaults_Legend.update({
    'x_pos': 0.2,  # left edge
    'label_width': 0.2,
    'label_height': 0.03,
})

def plot_maker(wrps):
    def set_legend_and_color(wrps):
        for w in wrps:
            w.legend = w.in_file_path.split('/')[0]
            if w.legend[:2]=='El':
                w.obj.SetMarkerColor(ROOT.kRed)
                w.obj.SetLineColor(ROOT.kRed)
                w.obj.SetFillStyle(3020)
            elif w.legend[:2]=='Mu':
                w.obj.SetMarkerColor(ROOT.kBlue)
                w.obj.SetLineColor(ROOT.kBlue)
                w.obj.SetFillStyle(3019)
            w.val_y_max = 1.1
            yield w

    def format_graphics(wrps):
        for w in wrps:
            if w.name.endswith('Eff'):
                w.obj.SetMarkerStyle(7)
                w.draw_option_legend = 'LP'
                w.draw_option = 'LP'
            else:
                col = w.obj.GetMarkerColor() - 9
                w.obj.SetFillColor(col)
                w.obj.SetLineColor(col)
            yield w

    def format_cross_triggers(wrps):
        for w in wrps:
            if 'PFJet' in w.legend:
                if not w.name.endswith('Eff'):
                    continue
                col = ROOT.kBlue + 3 if w.legend[:2]=='Mu' else ROOT.kGreen + 1
                w.obj.SetMarkerColor(col)
                w.obj.SetLineColor(col)
            elif not w.name.endswith('Eff'):
                w.legend = 'electrons' if w.legend[:2]=='El' else 'muons'
            yield w

    wrps = varial.gen.gen_make_eff_graphs(wrps, 'Passing', 'Denom', 'Eff')
    wrps = set_legend_and_color(wrps)
    wrps = format_graphics(wrps)
    wrps = format_cross_triggers(wrps)
    wrps = varial.gen.gen_noex_norm_to_integral(wrps)
    return wrps


def plot_grouper(wrps):
    group_key = lambda w: str('PFHT' in w.in_file_path) + w.name.replace('Eff', '')
    wrps = sorted(wrps, key=lambda w: w.name[::-1])  # All Eff stuff to back
    wrps = sorted(wrps, key=group_key)
    wrps = varial.gen.group(wrps, group_key)
    return wrps


def plotter_factory(**kws):
    kws['hook_loaded_histos'] = plot_maker
    kws['plot_setup'] = None
    kws['plot_grouper'] = plot_grouper
    kws['canvas_decorators'] = [varial.rnd.Legend]
    return varial.tools.Plotter(**kws)


varial.tools.Runner(varial.tools.mk_rootfile_plotter(
    plotter_factory=plotter_factory,
    flat=True,
    name='VLQTrig'
))
varial.tools.WebCreator().run()