from glob import iglob

p = '/nfs/dust/cms/user/marchesi/RECO_files_Phys14like/CMSSW_7_3_2_patch2/'
def mk_lst(glb):
    return map(lambda s: 'file:'+s, iglob(p + glb))

bW1200list = mk_lst('tprime_RECO_TpjM1200_bW_13TeV_xqcut0_*.root')
tH1200list = mk_lst('tprime_RECO_TpjM1200_tH_13TeV_xqcut0_*.root')
bW800list = mk_lst('tprime_RECO_TpjM800_bW_13TeV_xqcut0_*.root')
tH800list = mk_lst('tprime_RECO_TpjM800_tH_13TeV_xqcut0_*.root')

