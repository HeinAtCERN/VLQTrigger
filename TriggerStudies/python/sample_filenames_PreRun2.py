from glob import iglob

p = '/pnfs/desy.de/cms/tier2/store/user/htholen/'
def mk_lst(glb):
    return map(lambda s: 'file:'+s, iglob(p + glb))

bW1200list = None
tH1200list = None
bW800list = mk_lst('TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/Trig20160506_TpJ_TH_step2/150519_160048/0000/step2_RAW2DIGI_L1Reco_RECO_EI_*.root')
tH800list = mk_lst('BprimeJetToTW_M800GeV_Tune4C_13TeV-madgraph-tauola/Trig20160506_BpJ_TW_step2/150523_142859/0000/step2_RAW2DIGI_L1Reco_RECO_EI_*.root')

