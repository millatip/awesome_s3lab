# Awesome Security of Physical AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, **papers-with-code** map of security & safety research for **Physical AI** — autonomous vehicles, drones, robots, and embodied LLM/VLA agents — organized as a **pipeline stage × security objective** matrix.

![papers](https://img.shields.io/badge/papers-14-blue) ![with code](https://img.shields.io/badge/with%20code-7-brightgreen) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

## How to read this list

Every paper sits at one **pipeline stage** (row) and targets one or more **security objectives** (column). Each matrix cell shows how many papers of each kind land there and links to the details below.

**Kinds** — 🗡️ Attack · 🛡️ Defense · 📊 Benchmark / dataset / tool · 📚 Survey / SoK

**Objectives** — 🔒 Confidentiality (don't leak model/data) · 🧬 Integrity (don't get fooled/poisoned) · ⚡ Availability (stay up under DoS) · 🚦 Safety (don't take unsafe physical action)

**Links** — 📄 paper · 💻 code · 🌐 project page

## The matrix

| Stage \ Objective | Confidentiality | Integrity | Availability | Safety |
| --- | --- | --- | --- | --- |
| **Data collection** | — | [🗡️1](#data-collection--integrity) | [🗡️1](#data-collection--availability) | [🗡️2](#data-collection--safety) |
| **Data processing** | — | — | — | — |
| **Model construction** | — | — | — | — |
| **Model training** | [🛡️1](#model-training--confidentiality) | [🗡️1 🛡️1](#model-training--integrity) | [🛡️1](#model-training--availability) | [🗡️1](#model-training--safety) |
| **Model deployment** | — | — | — | — |
| **Evaluation** | — | — | — | [📊1](#evaluation--safety) |
| **Inference** | — | [🗡️6 🛡️1](#inference--integrity) | — | [🗡️6](#inference--safety) |
| **System architecture** | — | [🗡️1](#system-architecture--integrity) | — | [🗡️1](#system-architecture--safety) |

<sub>Cells count papers by kind; click a cell to jump to its section. “—” = gap we haven't mapped yet (PRs very welcome).</sub>

## Papers by stage

### Data collection

_Sensing the physical world — cameras, LiDAR, radar, IMU/GPS, logs._

#### Data collection · Integrity

- 🗡️ **[Poltergeist: Acoustic Adversarial ML against Cameras and Computer Vision](https://ieeexplore.ieee.org/document/9519387)** — Acoustic injection into image-stabilization blurs frames to create/hide/move detected objects.  
  _Ji, Zhang, Ji, Chen, Zhang, Cheng, Xu_. IEEE S&P 2021  
  [📄 paper](https://ieeexplore.ieee.org/document/9519387)  
  `autonomous-driving` `camera` `sensor`

#### Data collection · Availability

- 🗡️ **[Rocking Drones with Intentional Sound Noise on Gyroscopic Sensors](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/son)** — Resonant acoustic noise saturates MEMS gyroscopes and crashes drones out of the sky.  
  _Son, Shin, Kim, Park, Noh, Choi, Choi, Kim_. USENIX Security 2015  
  [📄 paper](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/son)  
  `drone` `mems` `sensor`

#### Data collection · Safety

- 🗡️ **[Poltergeist: Acoustic Adversarial ML against Cameras and Computer Vision](https://ieeexplore.ieee.org/document/9519387)** — Acoustic injection into image-stabilization blurs frames to create/hide/move detected objects.  
  _Ji, Zhang, Ji, Chen, Zhang, Cheng, Xu_. IEEE S&P 2021  
  [📄 paper](https://ieeexplore.ieee.org/document/9519387)  
  `autonomous-driving` `camera` `sensor`
- 🗡️ **[Rocking Drones with Intentional Sound Noise on Gyroscopic Sensors](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/son)** — Resonant acoustic noise saturates MEMS gyroscopes and crashes drones out of the sky.  
  _Son, Shin, Kim, Park, Noh, Choi, Choi, Kim_. USENIX Security 2015  
  [📄 paper](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/son)  
  `drone` `mems` `sensor`

### Model training

_Optimization, (self-)supervision, RL, distributed/federated training._

#### Model training · Confidentiality

- 🛡️ **[Deep Learning with Differential Privacy (DP-SGD)](https://github.com/tensorflow/privacy)** — Gradient clipping + noise gives per-example DP guarantees against training-data extraction.  
  _Abadi, Chu, Goodfellow, McMahan, Mironov, Talwar, Zhang_. ACM CCS 2016  
  [📄 paper](https://arxiv.org/abs/1607.00133) · [💻 code](https://github.com/tensorflow/privacy)  
  `privacy` `training`

#### Model training · Integrity

- 🗡️ **[TrojDRL: Trojan Attacks on Deep Reinforcement Learning Agents](https://github.com/pkiourti/rl_backdoor)** — Backdoors an RL policy via ~0.025% data + in-band reward poisoning; trigger → attacker action.  
  _Kiourti, Wardega, Jha, Li_. DAC 2020  
  [📄 paper](https://arxiv.org/abs/1903.06638) · [💻 code](https://github.com/pkiourti/rl_backdoor)  
  `reinforcement-learning` `robot-control`
- 🛡️ **[Machine Learning with Adversaries: Byzantine-Tolerant Gradient Descent (Krum)](https://papers.nips.cc/paper/2017/hash/f4b9ec30ad9f68f89b29639786cb62ef-Abstract.html)** — Aggregation rule that tolerates Byzantine workers poisoning distributed/federated training.  
  _Blanchard, El Mhamdi, Guerraoui, Stainer_. NeurIPS 2017  
  [📄 paper](https://papers.nips.cc/paper/2017/hash/f4b9ec30ad9f68f89b29639786cb62ef-Abstract.html)  
  `distributed-training` `federated`

#### Model training · Availability

- 🛡️ **[Machine Learning with Adversaries: Byzantine-Tolerant Gradient Descent (Krum)](https://papers.nips.cc/paper/2017/hash/f4b9ec30ad9f68f89b29639786cb62ef-Abstract.html)** — Aggregation rule that tolerates Byzantine workers poisoning distributed/federated training.  
  _Blanchard, El Mhamdi, Guerraoui, Stainer_. NeurIPS 2017  
  [📄 paper](https://papers.nips.cc/paper/2017/hash/f4b9ec30ad9f68f89b29639786cb62ef-Abstract.html)  
  `distributed-training` `federated`

#### Model training · Safety

- 🗡️ **[TrojDRL: Trojan Attacks on Deep Reinforcement Learning Agents](https://github.com/pkiourti/rl_backdoor)** — Backdoors an RL policy via ~0.025% data + in-band reward poisoning; trigger → attacker action.  
  _Kiourti, Wardega, Jha, Li_. DAC 2020  
  [📄 paper](https://arxiv.org/abs/1903.06638) · [💻 code](https://github.com/pkiourti/rl_backdoor)  
  `reinforcement-learning` `robot-control`

### Evaluation

_Benchmarks, test sets, simulation, red-teaming, certification._

#### Evaluation · Safety

- 📊 **[CARLA: An Open Urban Driving Simulator](https://github.com/carla-simulator/carla)** — Open simulator widely used to red-team and safety-test AV stacks under rare/adversarial scenarios.  
  _Dosovitskiy, Ros, Codevilla, Lopez, Koltun_. CoRL 2017  
  [📄 paper](https://arxiv.org/abs/1711.03938) · [💻 code](https://github.com/carla-simulator/carla)  
  `autonomous-driving` `simulation`

### Inference

_Runtime perception → planning → action in the physical world._

#### Inference · Integrity

- 🗡️ **[BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://arxiv.org/abs/2407.20242)** — Voice/text jailbreaks push embodied LLM agents into physically harmful manipulation actions.  
  _Zhang, Zhang, Ma, Chen, Huang, Zhang, et al._. ICLR 2025  
  [📄 paper](https://arxiv.org/abs/2407.20242) · [🌐 project](https://embodied-llms-safety.github.io)  
  `embodied-llm` `robot-manipulation`
- 🗡️ **[Jailbreaking LLM-Controlled Robots (RoboPAIR)](https://arxiv.org/abs/2410.13691)** — Automated jailbreak elicits harmful physical actions from LLM-controlled robots (up to 100% ASR).  
  _Robey, Ravichandran, Kumar, Hassani, Pappas_. arXiv 2024  
  [📄 paper](https://arxiv.org/abs/2410.13691) · [🌐 project](https://robopair.org)  
  `embodied-llm` `robot` `autonomous-driving`
- 🗡️ **[Dirty Road Can Attack: Security of Automated Lane Centering (DRP)](https://github.com/ASGuard-UCI/DRP-attack)** — A malicious road patch steers a production lane-centering system off its lane.  
  _Sato, Shen, Wang, Jia, Lin, Chen_. USENIX Security 2021  
  [📄 paper](https://www.usenix.org/conference/usenixsecurity21/presentation/sato) · [💻 code](https://github.com/ASGuard-UCI/DRP-attack)  
  `autonomous-driving` `lane-keeping`
- 🗡️ **[Invisible for both Camera and LiDAR: Security of Multi-Sensor Fusion (MSF-ADV)](https://github.com/ASGuard-UCI/MSF-ADV)** — A single 3D adversarial object evades camera+LiDAR fusion → 100% collision in simulation.  
  _Cao, Wang, Xiao, Yang, Fang, Yang, Chen, Liu, Li_. IEEE S&P 2021  
  [📄 paper](https://arxiv.org/abs/2106.09249) · [💻 code](https://github.com/ASGuard-UCI/MSF-ADV)  
  `autonomous-driving` `sensor-fusion` `lidar`
- 🗡️ **[Adversarial Sensor Attack on LiDAR-based Perception in Autonomous Driving](https://arxiv.org/abs/1907.06826)** — First LiDAR spoofing attack that injects fake close-range obstacles into AV perception.  
  _Cao, Xiao, Cyr, Zhou, Park, Rampazzi, Chen, Fu, Mao_. ACM CCS 2019  
  [📄 paper](https://arxiv.org/abs/1907.06826) · [🌐 project](https://sites.google.com/view/av-ioat-sec/adv-lidar-attack)  
  `autonomous-driving` `lidar`
- 🛡️ **[Certified Adversarial Robustness via Randomized Smoothing](https://github.com/locuslab/smoothing)** — Turns any classifier into one with a certified L2 robustness radius via Gaussian smoothing.  
  _Cohen, Rosenfeld, Kolter_. ICML 2019  
  [📄 paper](https://arxiv.org/abs/1902.02918) · [💻 code](https://github.com/locuslab/smoothing)  
  `robustness` `perception`
- 🗡️ **[Robust Physical-World Attacks on Deep Learning Visual Classification (RP2)](https://github.com/evtimovi/robust_physical_perturbations)** — Sticker perturbations on a stop sign cause targeted misclassification from a moving vehicle.  
  _Eykholt, Evtimov, Fernandes, Li, Rahmati, Xiao, Prakash, Kohno, Song_. CVPR 2018  
  [📄 paper](https://arxiv.org/abs/1707.08945) · [💻 code](https://github.com/evtimovi/robust_physical_perturbations)  
  `autonomous-driving` `perception`

#### Inference · Safety

- 🗡️ **[BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://arxiv.org/abs/2407.20242)** — Voice/text jailbreaks push embodied LLM agents into physically harmful manipulation actions.  
  _Zhang, Zhang, Ma, Chen, Huang, Zhang, et al._. ICLR 2025  
  [📄 paper](https://arxiv.org/abs/2407.20242) · [🌐 project](https://embodied-llms-safety.github.io)  
  `embodied-llm` `robot-manipulation`
- 🗡️ **[Jailbreaking LLM-Controlled Robots (RoboPAIR)](https://arxiv.org/abs/2410.13691)** — Automated jailbreak elicits harmful physical actions from LLM-controlled robots (up to 100% ASR).  
  _Robey, Ravichandran, Kumar, Hassani, Pappas_. arXiv 2024  
  [📄 paper](https://arxiv.org/abs/2410.13691) · [🌐 project](https://robopair.org)  
  `embodied-llm` `robot` `autonomous-driving`
- 🗡️ **[Dirty Road Can Attack: Security of Automated Lane Centering (DRP)](https://github.com/ASGuard-UCI/DRP-attack)** — A malicious road patch steers a production lane-centering system off its lane.  
  _Sato, Shen, Wang, Jia, Lin, Chen_. USENIX Security 2021  
  [📄 paper](https://www.usenix.org/conference/usenixsecurity21/presentation/sato) · [💻 code](https://github.com/ASGuard-UCI/DRP-attack)  
  `autonomous-driving` `lane-keeping`
- 🗡️ **[Invisible for both Camera and LiDAR: Security of Multi-Sensor Fusion (MSF-ADV)](https://github.com/ASGuard-UCI/MSF-ADV)** — A single 3D adversarial object evades camera+LiDAR fusion → 100% collision in simulation.  
  _Cao, Wang, Xiao, Yang, Fang, Yang, Chen, Liu, Li_. IEEE S&P 2021  
  [📄 paper](https://arxiv.org/abs/2106.09249) · [💻 code](https://github.com/ASGuard-UCI/MSF-ADV)  
  `autonomous-driving` `sensor-fusion` `lidar`
- 🗡️ **[Adversarial Sensor Attack on LiDAR-based Perception in Autonomous Driving](https://arxiv.org/abs/1907.06826)** — First LiDAR spoofing attack that injects fake close-range obstacles into AV perception.  
  _Cao, Xiao, Cyr, Zhou, Park, Rampazzi, Chen, Fu, Mao_. ACM CCS 2019  
  [📄 paper](https://arxiv.org/abs/1907.06826) · [🌐 project](https://sites.google.com/view/av-ioat-sec/adv-lidar-attack)  
  `autonomous-driving` `lidar`
- 🗡️ **[Robust Physical-World Attacks on Deep Learning Visual Classification (RP2)](https://github.com/evtimovi/robust_physical_perturbations)** — Sticker perturbations on a stop sign cause targeted misclassification from a moving vehicle.  
  _Eykholt, Evtimov, Fernandes, Li, Rahmati, Xiao, Prakash, Kohno, Song_. CVPR 2018  
  [📄 paper](https://arxiv.org/abs/1707.08945) · [💻 code](https://github.com/evtimovi/robust_physical_perturbations)  
  `autonomous-driving` `perception`

### System architecture

_Buses, components, APIs, networking across the cyber-physical system._

#### System architecture · Integrity

- 🗡️ **[All Your GPS Are Belong To Us: Towards Stealthy Manipulation of Road Navigation Systems](https://www.usenix.org/conference/usenixsecurity18/presentation/zeng)** — Stealthy GPS spoofing that keeps the route plausible while steering a driver to a target.  
  _Zeng, Liu, Cui, Miao, Yang, Su, Wang, Xu, Yang, Qian_. USENIX Security 2018  
  [📄 paper](https://www.usenix.org/conference/usenixsecurity18/presentation/zeng)  
  `gps` `navigation` `autonomous-driving`

#### System architecture · Safety

- 🗡️ **[All Your GPS Are Belong To Us: Towards Stealthy Manipulation of Road Navigation Systems](https://www.usenix.org/conference/usenixsecurity18/presentation/zeng)** — Stealthy GPS spoofing that keeps the route plausible while steering a driver to a target.  
  _Zeng, Liu, Cui, Miao, Yang, Su, Wang, Xu, Yang, Qian_. USENIX Security 2018  
  [📄 paper](https://www.usenix.org/conference/usenixsecurity18/presentation/zeng)  
  `gps` `navigation` `autonomous-driving`

## Stats

- **14** papers — 🗡️ 10 attacks, 🛡️ 3 defenses.
- **7/14** (50%) ship public **code**.

## Contributing

Add a paper by editing [`data/papers.yml`](data/papers.yml) and running `python3 scripts/generate_readme.py`. See [CONTRIBUTING.md](CONTRIBUTING.md). Prioritizing papers whose code is public is the whole point — include the `code:` field whenever a repo exists.

## License

[CC0-1.0](LICENSE) — to the extent possible under law, dedicated to the public domain.

<sub>Generated by `scripts/generate_readme.py` on 2026-09-20. Do not edit README.md by hand.</sub>
