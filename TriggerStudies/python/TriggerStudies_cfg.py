import FWCore.ParameterSet.Config as cms
import sys
import glob

process = cms.Process("TriggerStudies")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

process.options = cms.untracked.PSet(allowUnscheduled=cms.untracked.bool(True))

process.TFileService=cms.Service(
    "TFileService",
    fileName=cms.string('trgout_test_new.root'),
)

process.source = cms.Source(
    "PoolSource",
    fileNames=cms.untracked.vstring(
        #'file:/nfs/dust/cms/user/tholenhe/tmp/test_TprimeB_800.root',
        map(lambda s: 'file:'+s, glob.glob('/nfs/dust/cms/user/tholenhe/tmp/RECO_*.root')),
        #'file:/nfs/dust/cms/user/tholenhe/tmp/GENSIMRAWHLT_26.root',
        #'file:/nfs/dust/cms/user/tholenhe/tmp/GENSIMRAWHLT_34.root',
    ),
    duplicateCheckMode=cms.untracked.string('noDuplicateCheck'),
    skipBadFiles=cms.untracked.bool(True),
)


from PhysicsTools.PatAlgos.tools.pfTools import *
postfix = "PFlow"
jetCorrectionsAK4 = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
usePF2PAT(
    process,
    runPF2PAT=True,
    jetAlgo="AK4",
    runOnMC=True,
    postfix=postfix,
    jetCorrections=jetCorrectionsAK4,
    pvCollection=cms.InputTag('offlinePrimaryVertices')
)

## Top projections in PF2PAT
getattr(process, "pfPileUpJME"+postfix).checkClosestZVertex = False
getattr(process, "pfNoPileUpJME"+postfix).enable = True
getattr(process, "pfNoMuonJMEPFBRECO"+postfix).enable = True
getattr(process, "pfNoElectronJMEPFBRECO"+postfix).enable = True
process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")


process.pfIsolatedElectronsPFBRECOPFlow.cut = " \
pt > 5 && gsfElectronRef.isAvailable() && \
gsfTrackRef.hitPattern().numberOfLostHits(\'MISSING_INNER_HITS\') < 2 && \
abs(1 - gsfElectronRef.eSuperClusterOverP())/gsfElectronRef.ecalEnergy() < 0.05 && \
gsfElectronRef.sigmaIetaIeta() < 0.03 && \
gsfElectronRef.hadronicOverEm() < 0.12 \
"

process.pfIsolatedMuonsPFBRECOPFlow.cut = ' \
pt > 5 && muonRef.isAvailable() && \
muonRef.isPFMuon && \
muonRef.isGlobalMuon && \
muonRef.innerTrack.hitPattern.trackerLayersWithMeasurement > 5 && \
muonRef.innerTrack.hitPattern.numberOfValidPixelHits > 0 && \
muonRef.globalTrack.hitPattern.numberOfValidMuonHits > 0 \
'

process.load("VLQTrigger.TriggerStudies.TriggerMenu_cff")

process.p = cms.Path(

    process.trigStudySequence
)



# NAME = sys.argv[2]
#NAME = 'TpJ_TH_M800'
#from VLQTrigger.TriggerStudies.sample_filenames_PreRun2 import *
#dizionario={'TpJ_TH_M800':tH800list,'tH1200':tH1200list,'BpJ_TW_M800':bW800list,'bW1200':bW1200list}
#process.source.fileNames = cms.untracked.vstring(dizionario[NAME])
#process.TFileService.fileName=cms.string('trgout_'+NAME+'.root')
