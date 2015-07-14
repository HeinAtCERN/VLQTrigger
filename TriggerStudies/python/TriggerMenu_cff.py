import FWCore.ParameterSet.Config as cms


triggermenu = [
    (
        "HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v",
        "HLT_Ele105_CaloIdVT_GsfTrkIdT_v",
        "HLT_Ele32_eta2p1_WPLoose_Gsf_v",
        "HLT_PFHT800_v",

        # 14e33
        "HLT_Ele27_WPLoose_Gsf_WHbbBoost_v",
        "HLT_Ele27_eta2p1_WPLoose_Gsf_HT200_v",
        "HLT_Ele32_eta2p1_WPLoose_Gsf_CentralPFJet30_BTagCSV07_v",
        "HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet30_v",
        "HLT_Ele32_eta2p1_WPLoose_Gsf_TriCentralPFJet50_40_30_v",
    ),
    (
        "HLT_Mu40_eta2p1_PFJet200_PFJet50_v",
        "HLT_Mu45_eta2p1_v",
        "HLT_IsoMu24_eta2p1_v",
        "HLT_PFHT800_v",

        # 14e33
        "HLT_IsoMu16_eta2p1_CaloMET30_v",
        "HLT_IsoMu24_eta2p1_CentralPFJet30_BTagCSV07_v",
        "HLT_IsoMu24_eta2p1_TriCentralPFJet30_v",
        "HLT_IsoMu24_eta2p1_TriCentralPFJet50_40_30_v",
        "HLT_IsoMu27_v",
        "HLT_Mu50_v",
    ),
]

trigStudySequence = cms.Sequence()
for comb in (0, 3, 99):
    for triggerpath in triggermenu:
        triggerpath, other_trgs = triggerpath[0], triggerpath[1:]
        name = triggerpath[4:-3]+('_COMBO_%02d' % comb if comb else '')
        globals()[name] = cms.EDAnalyzer(
            "TriggerStudies",
            process_name    = cms.string('MYHLT'),
            triggerpath     = cms.string(triggerpath),
            triggerpathcomb = cms.vstring(other_trgs[:comb]),
            jets_inp        = cms.InputTag("pfJetsPFBRECOPFlow"),  #ak4PFJetsCHS"),
            muon_inp        = cms.InputTag("muons"),
            ele_inp         = cms.InputTag("gedGsfElectrons"),
            jet_lead_pt     = cms.double(250),
            jet_subl_pt     = cms.double(65),
            jet_eta         = cms.double(2.4),
            muon_pt_cut     = cms.double(45.),
            ele_pt_cut      = cms.double(55. if '_PFJet' in triggerpath else 120.),
            st_muon_pt      = cms.double(26.),
            st_ele_pt       = cms.double(34.),
            mode            = cms.int32(0 if triggerpath.startswith('HLT_Mu') else 1),
        )
        trigStudySequence += globals()[name]



# TODO: processname?
# TODO: PFHT800?
# TODO: trigger path version => v2?
# TODO: include MET in ST??


if __name__ == '__main__':
    with open('trigs.txt') as f:
        trgs = f.readlines()
    trgs2 = map(lambda s: s[:-2], trgs)
    for t in triggermenu[0]:
        if t not in trgs2:
            print t
    for t in triggermenu[1]:
        if t not in trgs2:
            print t
