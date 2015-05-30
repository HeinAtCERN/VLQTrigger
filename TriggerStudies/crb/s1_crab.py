from CRABClient.UserUtilities import config
config = config()

config.General.requestName  = 'TrigStudy20160530'
config.General.transferLogs = True

config.JobType.pluginName  = 'Analysis'
# Name of the CMSSW configuration file
config.JobType.psetName    = 'cfg.py'

# This string determines the primary dataset of the newly-produced outputs.
# For instance, this dataset will be named /CrabTestSingleMu/something/USER
config.Data.inputDataset = '/TprimeTToTH_M-700_LH_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM'
#config.Data.inputDBS = 'global'
config.Data.ignoreLocality=True
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 20
#config.Data.totalUnits = 300
config.Data.publication = False

# This string is used to construct the output dataset name
config.Data.publishDataName = ''

# Where the output files will be transmitted to
config.Site.storageSite = 'T2_DE_DESY'
#config.Site.whitelist   = ['T2_DE_DESY']

