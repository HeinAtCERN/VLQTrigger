import FWCore.ParameterSet.Config as cms


triggermenu = [
    "HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v1",
    "HLT_Mu40_eta2p1_PFJet200_PFJet50_v1",
    "HLT_Ele105_CaloIdVT_GsfTrkIdT_v1",
    "HLT_Mu45_eta2p1_v1",
]

trig_ht = "HLT_PFHT900_v1"

for with_ht in (True, False):
    for triggerpath in triggermenu:
        globals()[triggerpath[4:-3]+('_OR_'+trig_ht[4:-3] if with_ht else '')] = cms.EDAnalyzer(
            "TriggerStudies",
            process_name    = cms.string('HLT'),
            trigger_path    = cms.string(triggerpath),
            trigger_pathHT  = cms.string(trig_ht if with_ht else ''),
            jets_inp        = cms.InputTag("ak4PFJetsCHS"),
            muon_inp        = cms.InputTag("muons"),
            ele_inp         = cms.InputTag("gedGsfElectrons"),
            jet_lead_pt     = cms.double(250),
            jet_subl_pt     = cms.double(65),
            jet_eta         = cms.double(2.5),
            muon_pt_cut     = cms.double(45.),
            ele_pt_cut      = cms.double(55. if '_PFJet' in triggerpath else 120.),
            mode            = cms.int32(0 if triggerpath.startswith('HLT_Mu') else 1),
        )

p = cms.Path()
for with_ht in (True, False):
    for triggerpath in triggermenu:
        p += globals()[triggerpath[4:-3]+('_OR_'+trig_ht[4:-3] if with_ht else '')]






















