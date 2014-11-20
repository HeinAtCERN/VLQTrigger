import FWCore.ParameterSet.Config as cms


triggermenu = [
    "HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v1",
    "HLT_Mu40_eta2p1_PFJet200_PFJet50_v1"
]

#ele_cut = (
#    '? abs(eta) < 1.479 ? ('                     # Barrel
#      'pt > 48. && '
#      'abs(1 - eSuperClusterOverP)/ecalEnergy < 0.05 && '
#      'abs(deltaEtaSuperClusterTrackAtVtx) < 0.007 && '
#      'abs(deltaPhiSuperClusterTrackAtVtx) < 0.15 && '
#      'sigmaIetaIeta < 0.03 && '
#      'hadronicOverEm < 0.1 && '
#      'dr03EcalRecHitSumEt/pt < 0.2 && '
#      'dr03HcalTowerSumEt/pt < 0.2 && '
#      '(dr03TkSumPt/pt) < 0.2'
#    '):('                                         # Endcap
#      'abs(eta) < 2.5 && '
#      'pt > 48 && '
#      'abs(1 - eSuperClusterOverP)/ecalEnergy < 0.05 && '
#      'abs(deltaEtaSuperClusterTrackAtVtx) < 0.009 && '
#      'abs(deltaPhiSuperClusterTrackAtVtx) < 0.1 && '
#      'sigmaIetaIeta < 0.01 && '
#      'hadronicOverEm < 0.12 && '
#      'dr03EcalRecHitSumEt/pt < 0.2 && '
#      'dr03HcalTowerSumEt/pt < 0.2 && '
#      '(dr03TkSumPt/pt) < 0.2'
#    ')'
#)
#ele_cut = '?(' + ele_cut + ')? 1 : 0'
#print ele_cut

for triggerpath in triggermenu:
    globals()[triggerpath[4:-3]] = cms.EDAnalyzer(
        "TriggerStudies",
        trigger_path = cms.string(triggerpath),
        jets_inp     = cms.InputTag("ak4PFJetsCHS"),
        muon_inp     = cms.InputTag("muons"),
        ele_inp      = cms.InputTag("gedGsfElectrons"),
        jet_lead_pt  = cms.double(220),
        jet_subl_pt  = cms.double(55),
        jet_eta      = cms.double(2.5),
        muon_pt_cut  = cms.double(43.),
        ele_pt_cut   = cms.double(48.),
        muon_cut     = cms.string(
            '? pt > 43 && '
            'abs(eta) < 2.1 && '
            'isGlobalMuon ? 1 : 0'
        ),
#        ele_cut      = cms.string(ele_cut),
        mode         = cms.int32(0 if 'Mu40' in triggerpath else 1),
    )

p = cms.Path()
for triggerpath in triggermenu:
    p += globals()[triggerpath[4:-3]]






















