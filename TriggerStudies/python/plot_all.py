#!/usr/bin/env python

import ROOT
import varial
import varial.tools
import varial.util

varial.settings.max_num_processes = 1
varial.raise_root_error_level()
varial.settings.canvas_size_x = 1138
varial.settings.canvas_size_y = 744
varial.settings.root_style.SetPadLeftMargin(0.1)
varial.settings.root_style.SetPadRightMargin(0.1)
varial.settings.root_style.SetPadTopMargin(0.1)
varial.settings.root_style.SetPadBottomMargin(0.1)


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
    txtbx = ROOT.TLatex(
        0.6137566,0.4793003,"CMS")  # default y: 0.6793003
    txtbx.SetNDC()
    txtbx.SetTextFont(61)
    txtbx.SetTextSize(0.06122449)
    txtbx.SetLineWidth(2)
    return txtbx


def mk_txtbx_sim():
    txtbx = ROOT.TLatex(
        0.617284,0.4355685,"Simulation Preliminary")  # default y: 0.6355685
    txtbx.SetNDC()
    txtbx.SetTextFont(52)
    txtbx.SetTextSize(0.0451895)
    txtbx.SetLineWidth(2)
    return txtbx


def mk_txtbx_2015():
    txtbx = ROOT.TLatex(0.9,0.92," 2015, 13 TeV")
    txtbx.SetNDC()
    txtbx.SetTextAlign(31)
    txtbx.SetTextFont(42)
    txtbx.SetTextSize(0.06)
    txtbx.SetLineWidth(2)
    return txtbx


class MyPlotStyler(varial.util.Decorator):
    def do_final_cosmetics(self):
        self.decoratee.do_final_cosmetics()
        h = self.first_drawn
        h.GetXaxis().SetLabelFont(42)
        h.GetXaxis().SetLabelSize(0.035)
        h.GetXaxis().SetTitleSize(0.035)
        h.GetXaxis().SetTitleOffset(1.4)
        h.GetXaxis().SetTitleFont(42)
        h.GetYaxis().SetLabelFont(42)
        h.GetYaxis().SetLabelSize(0.035)
        h.GetYaxis().SetTitleSize(0.035)
        h.GetYaxis().SetTitleOffset(1.0)
        h.GetYaxis().SetTitleFont(42)


def plotter_factory(**kws):
    kws['hook_loaded_histos'] = plot_maker
    kws['plot_setup'] = None
    kws['plot_grouper'] = plot_grouper
    kws['canvas_decorators'] = [
        varial.rnd.Legend(
            xy_coords=(0.4294533,0.1676385,0.8924162,0.2959184),
            text_size=0.028,
            text_font=42,
        ),
        varial.rnd.TextBox(textbox=mk_txtbx_cms()),
        varial.rnd.TextBox(textbox=mk_txtbx_sim()),
        varial.rnd.TextBox(textbox=mk_txtbx_2015()),
        MyPlotStyler(),
    ]
    return varial.tools.Plotter(**kws)


varial.tools.Runner(varial.tools.mk_rootfile_plotter(
    # pattern='trgout_test_TprimeB_800.root',
    plotter_factory=plotter_factory,
    flat=True,
    name='VLQTrig'
))
varial.tools.WebCreator().run()



# HLT_AK8PFJet360_TrimMass30 : Trimmed AK8 jet mass > 30 GeV, p_{T} > 360 GeV
# HLT_AK8PFHT700_TrimR0p1PT0p03Mass50 : AK8 H_{T} > 700 GeV, trimmed AK8 jet mass > 30 GeV
# HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV0p45_v2 : Trimmed AK8 jet mass > 30 GeV, trimmed AK8 jet p_{T} > 280 GeV, trimmed AK8 jet p_{T} > 200 GeV
# HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50 : Non-isolated electron p_{T} > 45 GeV, cleaned AK4 jet p_{T} > 200 GeV, cleaned AK4 jet p_{T} > 50 GeV
# HLT_Mu40_eta2p1_PFJet200_PFJet50 : Non-isolated muon p_{T} > 40 GeV, cleaned AK4 jet p_{T} > 200 GeV, cleaned AK4 jet p_{T} > 50 GeV
# HLT_PFHT800 : H_{T} > 800 GeV
# HLT_PFJet450 : AK4 jet p_{T} > 450 GeV
