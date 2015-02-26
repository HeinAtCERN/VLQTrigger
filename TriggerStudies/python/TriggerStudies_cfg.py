import FWCore.ParameterSet.Config as cms
import sys

NAME = sys.argv[2]

process = cms.Process("TriggerStudies")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = cms.string('PRE_LS172_V16::All')

from VLQTrigger.TriggerStudies.sample_filenames_PHYS14 import *

dizionario={'tH800':tH800list,'tH1200':tH1200list,'bW800':bW800list,'bW1200':bW1200list}

process.TFileService=cms.Service("TFileService",
fileName=cms.string('trgout_'+NAME+'.root'))

process.source = cms.Source(
    "PoolSource",
    fileNames=cms.untracked.vstring(dizionario[NAME]),
    duplicateCheckMode=cms.untracked.string('noDuplicateCheck'),
)

process.load("VLQTrigger.TriggerStudies.TriggerMenu_cff")
