from CRABClient.UserUtilities import config
config = config()

config.General.requestName  = 'Trig20160506_TpJ_TH'
config.General.transferLogs = True

config.JobType.pluginName  = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName    = 'step1.py'

# This string determines the primary dataset of the newly-produced outputs.
# For instance, this dataset will be named /CrabTestSingleMu/something/USER
config.Data.inputDataset = '/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/Phys14DR-AVE20BX25_tsg_PHYS14_25_V3-v2/GEN-SIM-RAW'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 300
config.Data.publication = True

# This string is used to construct the output dataset name
config.Data.publishDataName = 'Trig20160506_TpJ_TH_step1'

# Where the output files will be transmitted to
config.Site.storageSite = 'T2_DE_DESY'
config.Site.whitelist   = ['T1_DE_KIT']

