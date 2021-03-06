import FWCore.ParameterSet.Config as cms

electronPFIsoMapProd = cms.EDProducer('ElectronPFIsoMapProd',
    eleLabel = cms.untracked.InputTag("gsfElectrons"),
    vtxLabel = cms.untracked.InputTag("offlinePrimaryVertices"),
    pfLabel = cms.untracked.InputTag("particleFlow"),
)
