import FWCore.ParameterSet.Config as cms

ecalBarrelOccupancyTask = cms.EDFilter("EBOccupancyTask",
    prefixME = cms.untracked.string('EcalBarrel'),
    enableCleanup = cms.untracked.bool(False),
    mergeRuns = cms.untracked.bool(False),    
    EcalRawDataCollection = cms.InputTag("ecalEBunpacker"),
    EBDigiCollection = cms.InputTag("ecalEBunpacker","ebDigis"),
    EcalTrigPrimDigiCollection = cms.InputTag("ecalEBunpacker","EcalTriggerPrimitives"),
    EcalPnDiodeDigiCollection = cms.InputTag("ecalEBunpacker"),
    EcalRecHitCollection = cms.InputTag("ecalRecHit","EcalRecHitsEB")
)

