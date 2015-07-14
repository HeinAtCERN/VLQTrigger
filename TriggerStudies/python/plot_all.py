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

#varial.settings.defaults_Legend.update({
#    'x_pos': 0.85,
#    'y_pos': 0.5,
#    'label_width': 0.28,
#    'label_height': 0.04,
#    'opt': 'f',
#    'opt_data': 'p',
#    'reverse': True
#})#

varial.settings.canvas_size_x = 1138
varial.settings.canvas_size_y = 744
varial.settings.root_style.SetPadRightMargin(0.1)

def plot_maker(wrps):
    def set_y_axis_name(wrps):
        for w in wrps:
            w.obj.GetYaxis().SetTitle('Efficiency')
            yield w

    def set_legend_and_color(wrps):
        for w in wrps:
            w.legend = w.in_file_path.split('/')[0]
            if w.legend[:2]=='El':
                w.obj.SetMarkerColor(ROOT.kRed)
                w.obj.SetLineColor(ROOT.kRed)
                # w.obj.SetFillStyle(3020)
            elif w.legend[:2]=='Mu':
                w.obj.SetMarkerColor(ROOT.kBlue)
                w.obj.SetLineColor(ROOT.kBlue)
                # w.obj.SetFillStyle(3019)
            w.val_y_max = 1.0
            yield w

    def format_graphics(wrps):
        for w in wrps:
            if w.name.endswith('Eff') and 'TH1' not in w.type:
                w.obj.SetMarkerStyle(1)
                w.obj.SetLineWidth(2)
                w.draw_option_legend = 'L'
                w.draw_option = 'ZP'
            elif w.name.endswith('Eff'):
                w.obj.SetMarkerStyle(1)
                w.obj.SetLineWidth(2)
                w.draw_option_legend = None
                w.draw_option = 'hist'
            else:
                #col = w.obj.GetMarkerColor() - 9
                w.obj.SetFillColor(17)
                w.obj.SetLineColor(15)
                #w.obj.SetLineWidth(0)
            yield w

    def format_cross_triggers(wrps):
        for w in wrps:
            if not w.name.endswith('Eff'):
                #if not w.name.endswith('Eff'):
                #    continue
                if w.legend[:2]=='El':
                    w.legend = 'underlying distribution'
                else:
                    w.draw_option_legend = ''
            elif 'PFJet' in w.legend:
                col = ROOT.kBlue + 3 if w.legend[:2]=='Mu' else ROOT.kGreen + 1
                w.obj.SetMarkerColor(col)
                w.obj.SetLineColor(col)
            yield w

    wrps = varial.gen.gen_make_eff_graphs(
        wrps, 'Passing', 'Denom', 'Eff', yield_everything=True)
    wrps = varial.gen.gen_make_eff_graphs(
        wrps, 'Passing', 'Denom', 'Eff', eff_func=varial.op.div)
    wrps = varial.gen.imap_conditional(
        wrps,
        lambda w: 'Eff' not in w.name,
        varial.op.norm_to_integral,
    )
    wrps = set_y_axis_name(wrps)
    wrps = set_legend_and_color(wrps)
    wrps = format_graphics(wrps)
    wrps = format_cross_triggers(wrps)
    return wrps


def plot_grouper(wrps):
    group_key = lambda w: str(w.in_file_path.split('/')[0][-3:]) + w.name.replace('Eff', '')
    wrps = sorted(wrps, key=lambda w: w.name[::-1])  # All Eff stuff to back
    # for w in wrps: print w.name
    wrps = sorted(wrps, key=group_key)
    # for w in wrps: print w.name
    wrps = varial.gen.group(wrps, group_key)

    # efficiencies to be plotted on top of the raw distributions
    wrps = (sorted(w, key=lambda w: w.name.endswith('Eff')) for w in wrps)
    return wrps


def mk_txtbx_cms():
    txtbx = ROOT.TLatex(0.6137566,0.6793003,"CMS")
    txtbx.SetNDC()
    txtbx.SetTextFont(61)
    txtbx.SetTextSize(0.06122449)
    txtbx.SetLineWidth(2)
    return txtbx


def mk_txtbx_sim():
    txtbx = ROOT.TLatex(0.617284,0.6355685,"Simulation Preliminary")
    txtbx.SetNDC()
    txtbx.SetTextFont(52)
    txtbx.SetTextSize(0.0451895)
    txtbx.SetLineWidth(2)
    return txtbx


def plotter_factory(**kws):
    kws['hook_loaded_histos'] = plot_maker
    kws['plot_setup'] = None
    kws['plot_grouper'] = plot_grouper
    kws['canvas_decorators'] = [
        varial.rnd.Legend,
        varial.rnd.TextBox(textbox=mk_txtbx_cms()),
        varial.rnd.TextBox(textbox=mk_txtbx_sim()),
    ]
    return varial.tools.Plotter(**kws)


varial.tools.Runner(varial.tools.mk_rootfile_plotter(
    #pattern='trgout_test_TprimeB_800.root',
    plotter_factory=plotter_factory,
    flat=True,
    name='VLQTrig'
))
varial.tools.WebCreator().run()
