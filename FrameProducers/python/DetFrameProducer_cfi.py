import FWCore.ParameterSet.Config as cms 

DetFrames = cms.EDProducer('DetFrameProducer'
    , reducedEBRecHitCollection = cms.InputTag('reducedEcalRecHitsEB')
    , photonCollection = cms.InputTag('gedPhotons')#or 'slimmedPhotons' for mini AOD root file
    , reducedHBHERecHitCollection = cms.InputTag('reducedHcalRecHits:hbhereco')
    , reducedEERecHitCollection = cms.InputTag('reducedEcalRecHitsEE')
    , trackCollection = cms.InputTag("generalTracks")
    , genParticleCollection = cms.InputTag('genParticles')
    , gedPhotonCollection = cms.InputTag('gedPhotons')
    , trackRecHitCollection = cms.InputTag('generalTracks')
   #, vertexCollection = cms.InputTag("offlinePrimaryVerticesWithBS")
    , vertexCollection = cms.InputTag("offlinePrimaryVertices")
    , pfCollection = cms.InputTag("particleFlow")
    , pvCollection = cms.InputTag("offlinePrimaryVerticesWithBS")
    , jetTagCollection    = cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags")
    , ipTagInfoCollection = cms.InputTag("pfImpactParameterTagInfos")                                                     
    , siPixelRecHitCollection = cms.InputTag("siPixelRecHits")
    , siStripRecHitCollection = cms.VInputTag("siStripMatchedRecHits")
    , mode = cms.string("JetLevel")
    # Jet level cfg
    , nJets = cms.int32(-1)
    #, minJetPt = cms.double(35.)
    #, maxJetEta = cms.double(2.4)
    , z0PVCut  = cms.double(0.1)
    #granularity multiplier wrt ECAL maps for tracker and tracking RH images
    , granularityMultiPhi = cms.int32(1)
    , granularityMultiEta = cms.int32(1)
    , doECALstitched = cms.bool(True)
    , doTracksAtECALstitchedPt = cms.bool(True)
    , doTracksAtECALadjPt = cms.bool(True)
    , doHBHEenergy = cms.bool(True)
    , doBPIX = cms.bool(True)
    )
