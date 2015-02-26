import FWCore.ParameterSet.Config as cms


triggermenu = [
    "HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v1",
    "HLT_Mu40_eta2p1_PFJet200_PFJet50_v1"
]

for triggerpath in triggermenu:
    globals()[triggerpath[4:-3]] = cms.EDAnalyzer(
        "TriggerStudies",
        trigger_path = cms.string(triggerpath),
        jets_inp     = cms.InputTag("ak4PFJetsCHS"),
        muon_inp     = cms.InputTag("muons"),
        ele_inp      = cms.InputTag("gedGsfElectrons"),
        jet_lead_pt  = cms.double(250),
        jet_subl_pt  = cms.double(65),
        jet_eta      = cms.double(2.5),
        muon_pt_cut  = cms.double(45.),
        ele_pt_cut   = cms.double(55.),
        mode         = cms.int32(0 if 'Mu40' in triggerpath else 1),
    )

p = cms.Path()
for triggerpath in triggermenu:
    p += globals()[triggerpath[4:-3]]






















