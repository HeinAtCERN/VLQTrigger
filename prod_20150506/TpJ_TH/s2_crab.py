from CRABClient.UserUtilities import config
config = config()

config.General.requestName  = 'Trig20160506_TpJ_TH'
config.General.transferLogs = True

config.JobType.pluginName  = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName    = 'step2.py'

# This string determines the primary dataset of the newly-produced outputs.
# For instance, this dataset will be named /CrabTestSingleMu/something/USER
config.Data.inputDataset = '/TprimeJetToTH_M800GeV_Tune4C_13TeV-madgraph-tauola/htholen-Trig20160506_TpJ_TH_step1-a0f8002c19ea9dda476d548c2bd5f68b/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 300
config.Data.publication = True

# This string is used to construct the output dataset name
config.Data.publishDataName = 'Trig20160506_TpJ_TH_step2'

# Where the output files will be transmitted to
config.Site.storageSite = 'T2_DE_DESY'
config.Site.whitelist   = ['T2_DE_DESY']

