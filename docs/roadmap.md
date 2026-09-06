# Roadmap

## Phase 0 — Bring-up
- [x] Buy ESP32-S3
- [x] Buy BME688
- [x] Solder header
- [x] Verify wiring
- [x] Detect BME688 over I2C
- [x] Read environmental and gas measurements

## Phase 1 — Measurement Discipline
- [ ] Decide warm-up duration
- [ ] Define purge / baseline / exposure / recovery timing
- [ ] Build repeatable sampling fixture
- [ ] Add trial metadata
- [ ] Save raw CSV
- [ ] Collect clean-air repeatability data

## Phase 2 — First Dataset
- [ ] Coffee trials
- [ ] Orange-peel trials
- [ ] Peppermint trials
- [ ] Repeat on multiple days
- [ ] Check humidity / temperature confounding

## Phase 3 — First ML Model
- [ ] Plot every trial
- [ ] Extract trial-level features
- [ ] Train baseline models
- [ ] Split by independent trial
- [ ] Generate confusion matrix
- [ ] Test on completely new measurements

## Phase 4 — Version 1 Demo
- [ ] Real-time acquisition
- [ ] Real-time classification
- [ ] Confidence / unknown handling
- [ ] Simple UI
- [ ] Repeatability test

## Phase 5 — Productization
- [ ] Sensor-array decision
- [ ] Airflow / chamber design
- [ ] Power architecture
- [ ] Custom PCB
- [ ] Enclosure
- [ ] Calibration strategy
- [ ] Drift compensation

## Phase 6 — Version 2 Research
- [ ] Define constrained odor vocabulary
- [ ] Research odor representation
- [ ] Prototype scent-cartridge generator
- [ ] Controlled mixing
- [ ] Human perceptual evaluation
