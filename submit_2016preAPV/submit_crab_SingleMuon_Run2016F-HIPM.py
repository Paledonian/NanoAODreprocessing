from CRABClient.UserUtilities import config

config = config()

config.General.requestName = "SingleMuon_Run2016F-HIPM"
config.General.workArea = "crab_projects"
config.General.transferLogs = True
config.General.transferOutputs = True

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "run_crab_data.py"
config.JobType.maxMemoryMB = 3000

config.Data.inputDataset = "/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD"
config.Data.outLFNDirBase = "/store/group/METUCMS/photonana/reNanoAOD/"
config.Data.outputDatasetTag = "SingleMuon_Run2016F-HIPM-RunIISummer20UL16APV_NanoAODv9"
config.Data.inputDBS = "global"
config.Data.splitting = "FileBased"
config.Data.unitsPerJob = 1
config.Data.publication = False
config.Data.ignoreLocality = True

config.Site.storageSite = "T2_TR_METU"
config.Site.whitelist = ["T2_*","T3_*"]
