import FWCore.ParameterSet.Config as cms

from PhysicsTools.MiBiCommonPAT.makeMiBiCommonPAT_cff import *



process = cms.Process("MiBiCommonPAT")



makeMiBiCommonPAT(process, GlobalTag="START38_V12::All", MC=True, Filter=True, SavePAT=True)
#makeMiBiCommonPAT(process, GlobalTag="START38_V12::All", MC=False, Filter=False, SavePAT=True)

process.source.fileNames = cms.untracked.vstring(
  #'file:/gwtera5/users/data/NTUPLES/VBF/WENu_38X.root'
  'file:/media/amassiro/deguio/Datasets/Fall10_WToENu_TuneZ2_7TeV-pythia6_AODSIM_START38_V12-v1.root'
  #'file:/gwpool/users/amassiro/VBF/Releases/CMSSW_3_8_3/src/PhysicsTools/MiBiCommonPAT/669A4128-43D0-DF11-AE93-001A92810ACE.root'  

)

process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string("MiBiCommonPAT_counters.root"),
    closeFileFast = cms.untracked.bool(True)
    )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False))


