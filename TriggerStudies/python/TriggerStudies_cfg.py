import FWCore.ParameterSet.Config as cms
import sys

process = cms.Process("TriggerStudies")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')


#process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = cms.string('PRE_LS172_V16::All')

from VLQTrigger.TriggerStudies.sample_filenames_PreRun2 import *
dizionario={'TpJ_TH_M800':tH800list,'tH1200':tH1200list,'BpJ_TW_M800':bW800list,'bW1200':bW1200list}

process.TFileService=cms.Service(
    "TFileService",
    fileName=cms.string('trgout.root'),
)

process.source = cms.Source(
    "PoolSource",
    fileNames=cms.untracked.vstring('test.root'),
    duplicateCheckMode=cms.untracked.string('noDuplicateCheck'),
    skipBadFiles=cms.untracked.bool(True),
)

process.load("VLQTrigger.TriggerStudies.TriggerMenu_cff")



#NAME = sys.argv[2]
#process.source.fileNames = cms.untracked.vstring(dizionario[NAME])
#process.TFileService.fileName=cms.string('trgout_'+NAME+'.root')