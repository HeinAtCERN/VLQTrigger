# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1_3 --step DIGI,L1,DIGI2RAW,HLT --magField 38T_PostLS1 --processName=HLT2 --no_exec -n 10 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions auto:run2_mc --eventcontent RAWSIM --inputEventContent REGEN --pileup AVE_20_BX_25ns --pileup_input dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM --filein dbs:/ZPrimeToTTJets_M1000GeV_W100GeV_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/GEN-SIM-RAW

# step1_6 --step DIGI,L1,DIGI2RAW,HLT --magField 38T_PostLS1 --processName=HLT2 --no_exec -n 10 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RAW --conditions auto:run2_mc --eventcontent RAWSIM --filein file:step1_5_NONE_PU.root

import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT2')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(
        '/store/mc/Phys14DR/ZPrimeToTTJets_M1000GeV_W100GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/PU20bx25_PHYS14_25_V1-v1/00000/065B88C8-7F6F-E411-B825-003048F0E1EC.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/088EF729-2DD0-E411-8086-002590A36FA2.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/08A1CF8F-31D0-E411-BF20-002590A4C69A.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/0C78EA9F-30D0-E411-98A4-002481E15522.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/12779355-2CD0-E411-B0FA-003048D477C2.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/1C225407-2DD0-E411-9C2E-001E67396E64.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/20D1C551-31D0-E411-8C02-002481E15522.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/245F5981-31D0-E411-8798-002590A50046.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/266B14AE-2CD0-E411-B52A-002590A370DC.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/2CF5F122-2CD0-E411-897B-001E67398052.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/30ECEE70-2CD0-E411-A829-001E67396685.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/4271C7E3-2BD0-E411-8ADC-002590A371AA.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/4E93B2F7-2BD0-E411-BC8A-002590A50046.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/5A1987AF-30D0-E411-8883-001E67397D73.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/6869DF15-2DD0-E411-AD47-001E67398052.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/6CE0F39A-2CD0-E411-A081-002590200868.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/748E50C0-30D0-E411-8245-002590A4C69A.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/88511EA3-30D0-E411-859B-002590A50046.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/9CE09BFE-2CD0-E411-BE8B-003048D4779E.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/A612C2A6-2CD0-E411-B8D6-002590200A54.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/AA4A2408-2DD0-E411-A56A-001E6739830E.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/B270D420-2CD0-E411-B329-001E6739670C.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/B8E64D49-2CD0-E411-80D5-002590A36FA2.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/C09014EF-2BD0-E411-90A1-002590A370DC.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/C27142CF-30D0-E411-ACFD-002590A370DC.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/C6F32AAC-2BD0-E411-A5D4-001E6739830E.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/DA2605FD-2CD0-E411-8BC3-002590A50046.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/10000/EA3C06FE-2CD0-E411-8CC9-001E67396685.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/0421632B-0FD4-E411-BB20-002590A8312A.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/04DEB80F-22D4-E411-AE54-001E673970C1.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/0C46A0E4-0ED4-E411-AADB-002590A83308.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/0E7232E3-0ED4-E411-AAE6-002590A83308.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/16B19EF6-1AD4-E411-A26D-001E67397396.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/220E8D11-08D4-E411-9F6F-002590200A18.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/309D00CC-1ED4-E411-A9FD-002481E75CDE.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/385B3F29-08D4-E411-91FB-002590A371C4.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/38A75658-07D4-E411-A25B-001E67398520.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/3AF5201A-08D4-E411-A3AE-001E67398C05.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/42A67EF2-0ED4-E411-84D8-002590A4FFC6.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/46C04113-08D4-E411-8CA0-002590A37116.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/4A2DA8F6-1AD4-E411-A325-001E67397396.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/56EEF6F8-1AD4-E411-9FDF-002590200974.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/5E55DB59-07D4-E411-B52E-002590A3A3D2.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/5EAE2BE5-0ED4-E411-A0D8-002590A3C97E.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/6299CD5B-07D4-E411-86F9-001E67396905.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/6451D7D9-06D4-E411-9A45-001E67396892.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/668EBF0F-22D4-E411-AF10-001E673970C1.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/6E7214EA-06D4-E411-A56D-002590200A18.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/74FAB2E2-0ED4-E411-8AC7-002590A83308.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/8278A8E3-0ED4-E411-9D85-002590A83308.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/8C23BDCB-07D4-E411-8210-001E67396D6F.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/9470AAE4-06D4-E411-B41C-002590200B40.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/94B4B99F-07D4-E411-B572-002590200B40.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/98CDA216-08D4-E411-9F56-001E67396BB7.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/9A6888E2-0ED4-E411-BCA0-002590A3C97E.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/9AEB0344-27D4-E411-B0D6-002590200A38.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/AC5D6613-08D4-E411-8EF3-D8D385FF4B32.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/ACF9E705-2AD4-E411-AC92-001E67398156.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/B4AF9EEF-34D4-E411-9040-001E67398408.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/BC8DC37B-07D4-E411-A242-001E67396892.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/BCA7123B-07D4-E411-B2C7-002590200948.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/BEAB5F06-07D4-E411-BAFF-F04DA23BCE4C.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/C23BFEE4-0ED4-E411-8540-002590A83308.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/C2F400F0-1AD4-E411-8828-002590A3C95E.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/C41E575E-07D4-E411-925E-D8D385FF4B32.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/D8058142-08D4-E411-9DE5-002590A3716C.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/E0994669-07D4-E411-84F2-0025B3E0656C.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/E2DA1CB0-06D4-E411-8C75-001E67398520.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/F0068814-07D4-E411-B834-001E67396D6F.root',
       # '/store/mc/Phys14DR/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/GEN-SIM-RAW/AVE20BX25_tsg_PHYS14_25_V3-v2/50000/F25822E7-0ED4-E411-B63E-001E673972E2.root',
    ),
    inputCommands = cms.untracked.vstring('keep *'),
    secondaryFileNames = cms.untracked.vstring(),
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1_3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('step1_3_DIGI_L1_DIGI2RAW_HLT_PU.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition
process.RAWSIMoutput.outputCommands += ['drop *_*_*_HLT']

# Other statements
process.mix.input.nbPileupEvents.averageNumber = cms.double(20.000000)
process.mix.bunchspace = cms.int32(25)
process.mix.minBunch = cms.int32(-12)
process.mix.maxBunch = cms.int32(3)
process.mix.input.fileNames = cms.untracked.vstring([
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/0E0254B5-5E25-E311-9C87-0026B93F4A37.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/148F0A95-5D25-E311-BED9-00145EDD77B9.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/181B59DC-5F25-E311-BB40-00A0D1EE2F94.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/2AC5C69B-5D25-E311-8D9F-00145EFB6930.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/32C1CE11-5E25-E311-BB5E-00266CF830FC.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/365DB59A-5D25-E311-B050-00145EDD76FD.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/42FBB09A-5D25-E311-9B77-00145EDD784D.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/4A40B231-5F25-E311-9EEF-7845C4FC3C8C.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/4AE67893-5E25-E311-A288-00266CF89604.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/523F35DF-5E25-E311-9905-00145EDD7355.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/5661CB97-5D25-E311-8E4D-000AE488B8B8.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/58191637-5F25-E311-B5AB-00145EDD732D.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/82ED44EC-5E25-E311-800C-00145EDD7635.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/863450AA-5E25-E311-B90F-00145EDD72F1.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/A02DB1B8-5E25-E311-BA1D-00145EFB6930.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/A283B485-5E25-E311-BDB9-000AE488B8B8.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/A8DDF385-5F25-E311-81A1-000AE488B8B8.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/B4B834BA-5D25-E311-B320-0026B93F4A37.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/C69214B1-5E25-E311-B2F8-00145EDD77B9.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/C6DB31DD-5D25-E311-9A64-00145EDD732D.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/CC8E57F9-5D25-E311-BBD1-00145EDD7881.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/CE2A233F-5E25-E311-A248-7845C4FC3C8C.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/F0BA29B8-5E25-E311-BBE3-00145EDD740F.root',
    '/store/mc/Fall13/MinBias_TuneA2MB_13TeV-pythia8/GEN-SIM/POSTLS162_V1-v1/20000/F265F6AD-5D25-E311-B2DC-00145EDD7759.root',
])
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions
