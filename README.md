# Awesome Security of Physical AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, **papers-with-code** map of security & safety research for **Physical AI** — autonomous vehicles, drones, robots, and embodied LLM/VLA agents — organized as a **pipeline stage × security objective** matrix.

![papers](https://img.shields.io/badge/papers-24-blue) ![with code](https://img.shields.io/badge/with%20code-12-brightgreen) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

## How to read this list

Every paper sits at one **pipeline stage** (row) and targets one or more **security objectives** (column). Each matrix cell shows how many papers of each kind land there and links to the details below.

**Kinds** — 🗡️ Attack · 🛡️ Defense · 📊 Benchmark / dataset / tool · 📚 Survey / SoK

**Objectives** — 🔒 Confidentiality (don't leak model/data) · 🧬 Integrity (don't get fooled/poisoned) · ⚡ Availability (stay up under DoS) · 🚦 Safety (don't take unsafe physical action)

**Links** — 📄 paper · 💻 code · 🌐 project page

## The matrix

| Stage \ Objective | 🔒 Confidentiality | 🧬 Integrity | ⚡ Availability | 🚦 Safety |
| --- | --- | --- | --- | --- |
| **Data collection** | — | [🗡️1](#data-collection--integrity) | [🗡️1](#data-collection--availability) | [🗡️2](#data-collection--safety) |
| **Data processing** | — | — | — | — |
| **Model construction** | — | — | — | — |
| **Model training** | [🛡️1](#model-training--confidentiality) | [🗡️2 🛡️1](#model-training--integrity) | [🛡️1](#model-training--availability) | [🗡️2](#model-training--safety) |
| **Model deployment** | [🗡️1](#model-deployment--confidentiality) | — | — | — |
| **Evaluation** | — | — | — | [📊1](#evaluation--safety) |
| **Inference** | — | [🗡️11 🛡️2](#inference--integrity) | [🗡️1](#inference--availability) | [🗡️9 🛡️1](#inference--safety) |
| **System architecture** | — | [🗡️1 📚1](#system-architecture--integrity) | — | [🗡️1 📚1](#system-architecture--safety) |

<sub>Cells count papers by kind; click a cell to jump to its section. “—” = gap we haven't mapped yet (PRs very welcome).</sub>

## ⭐ Papers with code

The reason this list exists — every row ships a public implementation.

| Paper | Stage | Objectives | Venue | Code |
| --- | --- | --- | --- | --- |
| 🗡️ [Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://arxiv.org/abs/2411.13587) | Inference | 🧬 🚦 | arXiv 2024 | [💻](https://github.com/William-wAng618/roboticAttack) |
| 🗡️ [Shape-Invariant 3D Adversarial Point Clouds (SI-Adv)](https://arxiv.org/abs/2203.04041) | Inference | 🧬 | CVPR 2022 | [💻](https://github.com/shikiw/SI-Adv) |
| 🗡️ [Dirty Road Can Attack: Security of Automated Lane Centering (DRP)](https://www.usenix.org/conference/usenixsecurity21/presentation/sato) | Inference | 🧬 🚦 | USENIX Security 2021 | [💻](https://github.com/ASGuard-UCI/DRP-attack) |
| 🗡️ [Invisible for both Camera and LiDAR: Security of Multi-Sensor Fusion (MSF-ADV)](https://arxiv.org/abs/2106.09249) | Inference | 🧬 🚦 | IEEE S&P 2021 | [💻](https://github.com/ASGuard-UCI/MSF-ADV) |
| 🗡️ [AdvPC: Transferable Adversarial Perturbations on 3D Point Clouds](https://arxiv.org/abs/1912.00461) | Inference | 🧬 | ECCV 2020 | [💻](https://github.com/ajhamdi/AdvPC) |
| 🗡️ [TrojDRL: Trojan Attacks on Deep Reinforcement Learning Agents](https://arxiv.org/abs/1903.06638) | Model training | 🧬 🚦 | DAC 2020 | [💻](https://github.com/pkiourti/rl_backdoor) |
| 🛡️ [Certified Adversarial Robustness via Randomized Smoothing](https://arxiv.org/abs/1902.02918) | Inference | 🧬 | ICML 2019 | [💻](https://github.com/locuslab/smoothing) |
| 🗡️ [Generating 3D Adversarial Point Clouds](https://arxiv.org/abs/1809.07016) | Inference | 🧬 | CVPR 2019 | [💻](https://github.com/xiangchong1/3d-adv-pc) |
| 🗡️ [Robust Physical-World Attacks on Deep Learning Visual Classification (RP2)](https://arxiv.org/abs/1707.08945) | Inference | 🧬 🚦 | CVPR 2018 | [💻](https://github.com/evtimovi/robust_physical_perturbations) |
| 🗡️ [ShapeShifter: Robust Physical Adversarial Attack on Faster R-CNN](https://arxiv.org/abs/1804.05810) | Inference | 🧬 🚦 | ECML-PKDD 2018 | [💻](https://github.com/shangtse/robust-physical-attack) |
| 📊 [CARLA: An Open Urban Driving Simulator](https://arxiv.org/abs/1711.03938) | Evaluation | 🚦 | CoRL 2017 | [💻](https://github.com/carla-simulator/carla) |
| 🛡️ [Deep Learning with Differential Privacy (DP-SGD)](https://arxiv.org/abs/1607.00133) | Model training | 🔒 | ACM CCS 2016 | [💻](https://github.com/tensorflow/privacy) |

## Browse by domain

- **`autonomous-driving`** (13) — [Jailbreaking LLM-Controlled Robots](https://arxiv.org/abs/2410.13691), [Physical Backdoor Attacks to Lane Detection Systems in Autonomous Driving](https://arxiv.org/abs/2203.00858), [SoK](https://arxiv.org/abs/2203.05314), [Too Afraid to Drive](https://arxiv.org/abs/2201.04610), [Dirty Road Can Attack](https://github.com/ASGuard-UCI/DRP-attack), [Invisible for both Camera and LiDAR](https://github.com/ASGuard-UCI/MSF-ADV), [Poltergeist](https://ieeexplore.ieee.org/document/9519387), [Towards Robust LiDAR-based Perception](https://arxiv.org/abs/2006.16974), [Adversarial Sensor Attack on LiDAR-based Perception in Autonomous Driving](https://arxiv.org/abs/1907.06826), [All Your GPS Are Belong To Us](https://www.usenix.org/conference/usenixsecurity18/presentation/zeng), [Robust Physical-World Attacks on Deep Learning Visual Classification](https://github.com/evtimovi/robust_physical_perturbations), [ShapeShifter](https://github.com/shangtse/robust-physical-attack), [CARLA](https://github.com/carla-simulator/carla)
- **`backdoor`** (1) — [Physical Backdoor Attacks to Lane Detection Systems in Autonomous Driving](https://arxiv.org/abs/2203.00858)
- **`camera`** (1) — [Poltergeist](https://ieeexplore.ieee.org/document/9519387)
- **`distributed-training`** (1) — [Machine Learning with Adversaries](https://papers.nips.cc/paper/2017/hash/f4b9ec30ad9f68f89b29639786cb62ef-Abstract.html)
- **`drone`** (1) — [Rocking Drones with Intentional Sound Noise on Gyroscopic Sensors](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/son)
- **`edge`** (1) — [Neural Network Extraction Through Physical Side Channels](https://www.usenix.org/conference/usenixsecurity24/presentation/horvath)
- **`embodied-llm`** (3) — [BadRobot](https://arxiv.org/abs/2407.20242), [Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://github.com/William-wAng618/roboticAttack), [Jailbreaking LLM-Controlled Robots](https://arxiv.org/abs/2410.13691)
- **`federated`** (1) — [Machine Learning with Adversaries](https://papers.nips.cc/paper/2017/hash/f4b9ec30ad9f68f89b29639786cb62ef-Abstract.html)
- **`gps`** (1) — [All Your GPS Are Belong To Us](https://www.usenix.org/conference/usenixsecurity18/presentation/zeng)
- **`lane-detection`** (1) — [Physical Backdoor Attacks to Lane Detection Systems in Autonomous Driving](https://arxiv.org/abs/2203.00858)
- **`lane-keeping`** (1) — [Dirty Road Can Attack](https://github.com/ASGuard-UCI/DRP-attack)
- **`lidar`** (3) — [Invisible for both Camera and LiDAR](https://github.com/ASGuard-UCI/MSF-ADV), [Towards Robust LiDAR-based Perception](https://arxiv.org/abs/2006.16974), [Adversarial Sensor Attack on LiDAR-based Perception in Autonomous Driving](https://arxiv.org/abs/1907.06826)
- **`mems`** (1) — [Rocking Drones with Intentional Sound Noise on Gyroscopic Sensors](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/son)
- **`model-extraction`** (1) — [Neural Network Extraction Through Physical Side Channels](https://www.usenix.org/conference/usenixsecurity24/presentation/horvath)
- **`navigation`** (1) — [All Your GPS Are Belong To Us](https://www.usenix.org/conference/usenixsecurity18/presentation/zeng)
- **`object-detection`** (1) — [ShapeShifter](https://github.com/shangtse/robust-physical-attack)
- **`perception`** (5) — [Shape-Invariant 3D Adversarial Point Clouds](https://github.com/shikiw/SI-Adv), [AdvPC](https://github.com/ajhamdi/AdvPC), [Certified Adversarial Robustness via Randomized Smoothing](https://github.com/locuslab/smoothing), [Generating 3D Adversarial Point Clouds](https://github.com/xiangchong1/3d-adv-pc), [Robust Physical-World Attacks on Deep Learning Visual Classification](https://github.com/evtimovi/robust_physical_perturbations)
- **`planning`** (1) — [Too Afraid to Drive](https://arxiv.org/abs/2201.04610)
- **`point-cloud`** (3) — [Shape-Invariant 3D Adversarial Point Clouds](https://github.com/shikiw/SI-Adv), [AdvPC](https://github.com/ajhamdi/AdvPC), [Generating 3D Adversarial Point Clouds](https://github.com/xiangchong1/3d-adv-pc)
- **`privacy`** (1) — [Deep Learning with Differential Privacy](https://github.com/tensorflow/privacy)
- **`reinforcement-learning`** (1) — [TrojDRL](https://github.com/pkiourti/rl_backdoor)
- **`robot`** (1) — [Jailbreaking LLM-Controlled Robots](https://arxiv.org/abs/2410.13691)
- **`robot-control`** (1) — [TrojDRL](https://github.com/pkiourti/rl_backdoor)
- **`robot-manipulation`** (2) — [BadRobot](https://arxiv.org/abs/2407.20242), [Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://github.com/William-wAng618/roboticAttack)
- **`robustness`** (1) — [Certified Adversarial Robustness via Randomized Smoothing](https://github.com/locuslab/smoothing)
- **`sensor`** (2) — [Poltergeist](https://ieeexplore.ieee.org/document/9519387), [Rocking Drones with Intentional Sound Noise on Gyroscopic Sensors](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/son)
- **`sensor-fusion`** (1) — [Invisible for both Camera and LiDAR](https://github.com/ASGuard-UCI/MSF-ADV)
- **`side-channel`** (1) — [Neural Network Extraction Through Physical Side Channels](https://www.usenix.org/conference/usenixsecurity24/presentation/horvath)
- **`simulation`** (1) — [CARLA](https://github.com/carla-simulator/carla)
- **`sok`** (1) — [SoK](https://arxiv.org/abs/2203.05314)
- **`training`** (1) — [Deep Learning with Differential Privacy](https://github.com/tensorflow/privacy)
- **`vla`** (1) — [Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://github.com/William-wAng618/roboticAttack)

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

- 🗡️ **[Physical Backdoor Attacks to Lane Detection Systems in Autonomous Driving](https://arxiv.org/abs/2203.00858)** — Poison/clean-annotation backdoors trigger lane mis-detection via common objects (e.g. traffic cones).  
  _Han, Xu, Liu, Zhang, Zhang, Zhang_. ACM MM 2022  
  [📄 paper](https://arxiv.org/abs/2203.00858) · [🌐 project](https://sites.google.com/view/lane-detection-attack/lda)  
  `autonomous-driving` `lane-detection` `backdoor`
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

- 🗡️ **[Physical Backdoor Attacks to Lane Detection Systems in Autonomous Driving](https://arxiv.org/abs/2203.00858)** — Poison/clean-annotation backdoors trigger lane mis-detection via common objects (e.g. traffic cones).  
  _Han, Xu, Liu, Zhang, Zhang, Zhang_. ACM MM 2022  
  [📄 paper](https://arxiv.org/abs/2203.00858) · [🌐 project](https://sites.google.com/view/lane-detection-attack/lda)  
  `autonomous-driving` `lane-detection` `backdoor`
- 🗡️ **[TrojDRL: Trojan Attacks on Deep Reinforcement Learning Agents](https://github.com/pkiourti/rl_backdoor)** — Backdoors an RL policy via ~0.025% data + in-band reward poisoning; trigger → attacker action.  
  _Kiourti, Wardega, Jha, Li_. DAC 2020  
  [📄 paper](https://arxiv.org/abs/1903.06638) · [💻 code](https://github.com/pkiourti/rl_backdoor)  
  `reinforcement-learning` `robot-control`

### Model deployment

_Packaging weights, releasing/serving the model on the robot/vehicle._

#### Model deployment · Confidentiality

- 🗡️ **[Neural Network Extraction Through Physical Side Channels](https://www.usenix.org/conference/usenixsecurity24/presentation/horvath)** — Recovers a deployed model's weights/architecture from physical (EM/power) side-channel leakage.  
  _Horváth, Picek, et al._. USENIX Security 2024  
  [📄 paper](https://www.usenix.org/conference/usenixsecurity24/presentation/horvath)  
  `side-channel` `model-extraction` `edge`

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
- 🗡️ **[Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://github.com/William-wAng618/roboticAttack)** — A small camera-view patch degrades OpenVLA action accuracy, up to 100% task failure (digital+physical).  
  _Wang, Liu, Cheng, Zhou, Wang, et al._. arXiv 2024  
  [📄 paper](https://arxiv.org/abs/2411.13587) · [💻 code](https://github.com/William-wAng618/roboticAttack)  
  `vla` `robot-manipulation` `embodied-llm`
- 🗡️ **[Jailbreaking LLM-Controlled Robots (RoboPAIR)](https://arxiv.org/abs/2410.13691)** — Automated jailbreak elicits harmful physical actions from LLM-controlled robots (up to 100% ASR).  
  _Robey, Ravichandran, Kumar, Hassani, Pappas_. arXiv 2024  
  [📄 paper](https://arxiv.org/abs/2410.13691) · [🌐 project](https://robopair.org)  
  `embodied-llm` `robot` `autonomous-driving`
- 🗡️ **[Shape-Invariant 3D Adversarial Point Clouds (SI-Adv)](https://github.com/shikiw/SI-Adv)** — A point-cloud sensitivity map yields imperceptible, on-surface adversarial perturbations.  
  _Huang, Dong, Chen, Su, Zhu_. CVPR 2022  
  [📄 paper](https://arxiv.org/abs/2203.04041) · [💻 code](https://github.com/shikiw/SI-Adv)  
  `point-cloud` `perception`
- 🗡️ **[Dirty Road Can Attack: Security of Automated Lane Centering (DRP)](https://github.com/ASGuard-UCI/DRP-attack)** — A malicious road patch steers a production lane-centering system off its lane.  
  _Sato, Shen, Wang, Jia, Lin, Chen_. USENIX Security 2021  
  [📄 paper](https://www.usenix.org/conference/usenixsecurity21/presentation/sato) · [💻 code](https://github.com/ASGuard-UCI/DRP-attack)  
  `autonomous-driving` `lane-keeping`
- 🗡️ **[Invisible for both Camera and LiDAR: Security of Multi-Sensor Fusion (MSF-ADV)](https://github.com/ASGuard-UCI/MSF-ADV)** — A single 3D adversarial object evades camera+LiDAR fusion → 100% collision in simulation.  
  _Cao, Wang, Xiao, Yang, Fang, Yang, Chen, Liu, Li_. IEEE S&P 2021  
  [📄 paper](https://arxiv.org/abs/2106.09249) · [💻 code](https://github.com/ASGuard-UCI/MSF-ADV)  
  `autonomous-driving` `sensor-fusion` `lidar`
- 🗡️ **[AdvPC: Transferable Adversarial Perturbations on 3D Point Clouds](https://github.com/ajhamdi/AdvPC)** — Autoencoder-regularized perturbations that transfer across 3D models and survive defenses.  
  _Hamdi, Rojas, Thabet, Ghanem_. ECCV 2020  
  [📄 paper](https://arxiv.org/abs/1912.00461) · [💻 code](https://github.com/ajhamdi/AdvPC)  
  `point-cloud` `perception`
- 🛡️ **[Towards Robust LiDAR-based Perception: Black-box Sensor Attack and Countermeasures (CARLO)](https://arxiv.org/abs/2006.16974)** — Occlusion/physics-based reasoning (CARLO) detects and rejects spoofed LiDAR obstacles.  
  _Sun, Cao, Chen, Mao_. USENIX Security 2020  
  [📄 paper](https://arxiv.org/abs/2006.16974)  
  `autonomous-driving` `lidar`
- 🗡️ **[Adversarial Sensor Attack on LiDAR-based Perception in Autonomous Driving](https://arxiv.org/abs/1907.06826)** — First LiDAR spoofing attack that injects fake close-range obstacles into AV perception.  
  _Cao, Xiao, Cyr, Zhou, Park, Rampazzi, Chen, Fu, Mao_. ACM CCS 2019  
  [📄 paper](https://arxiv.org/abs/1907.06826) · [🌐 project](https://sites.google.com/view/av-ioat-sec/adv-lidar-attack)  
  `autonomous-driving` `lidar`
- 🛡️ **[Certified Adversarial Robustness via Randomized Smoothing](https://github.com/locuslab/smoothing)** — Turns any classifier into one with a certified L2 robustness radius via Gaussian smoothing.  
  _Cohen, Rosenfeld, Kolter_. ICML 2019  
  [📄 paper](https://arxiv.org/abs/1902.02918) · [💻 code](https://github.com/locuslab/smoothing)  
  `robustness` `perception`
- 🗡️ **[Generating 3D Adversarial Point Clouds](https://github.com/xiangchong1/3d-adv-pc)** — Point shifting/adding/dropping attacks that fool PointNet-style 3D recognition.  
  _Xiang, Qi, Li_. CVPR 2019  
  [📄 paper](https://arxiv.org/abs/1809.07016) · [💻 code](https://github.com/xiangchong1/3d-adv-pc)  
  `point-cloud` `perception`
- 🗡️ **[Robust Physical-World Attacks on Deep Learning Visual Classification (RP2)](https://github.com/evtimovi/robust_physical_perturbations)** — Sticker perturbations on a stop sign cause targeted misclassification from a moving vehicle.  
  _Eykholt, Evtimov, Fernandes, Li, Rahmati, Xiao, Prakash, Kohno, Song_. CVPR 2018  
  [📄 paper](https://arxiv.org/abs/1707.08945) · [💻 code](https://github.com/evtimovi/robust_physical_perturbations)  
  `autonomous-driving` `perception`
- 🗡️ **[ShapeShifter: Robust Physical Adversarial Attack on Faster R-CNN](https://github.com/shangtse/robust-physical-attack)** — First robust targeted physical attack on an object detector; stop signs mis-detected in drive-by tests.  
  _Chen, Cornelius, Martin, Chau_. ECML-PKDD 2018  
  [📄 paper](https://arxiv.org/abs/1804.05810) · [💻 code](https://github.com/shangtse/robust-physical-attack)  
  `autonomous-driving` `object-detection`

#### Inference · Availability

- 🗡️ **[Too Afraid to Drive: Semantic DoS Vulnerability in AD Planning (PlanFuzz)](https://arxiv.org/abs/2201.04610)** — Benign-looking roadside objects freeze the planner (DoS); PlanFuzz finds 9 such vulnerabilities.  
  _Wan, Shen, Chuang, Xia, Garcia, Ma, Chen_. NDSS 2022  
  [📄 paper](https://arxiv.org/abs/2201.04610) · [🌐 project](https://sites.google.com/view/secure-safe-ai/planfuzz)  
  `autonomous-driving` `planning`

#### Inference · Safety

- 🗡️ **[BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://arxiv.org/abs/2407.20242)** — Voice/text jailbreaks push embodied LLM agents into physically harmful manipulation actions.  
  _Zhang, Zhang, Ma, Chen, Huang, Zhang, et al._. ICLR 2025  
  [📄 paper](https://arxiv.org/abs/2407.20242) · [🌐 project](https://embodied-llms-safety.github.io)  
  `embodied-llm` `robot-manipulation`
- 🗡️ **[Exploring the Adversarial Vulnerabilities of Vision-Language-Action Models in Robotics](https://github.com/William-wAng618/roboticAttack)** — A small camera-view patch degrades OpenVLA action accuracy, up to 100% task failure (digital+physical).  
  _Wang, Liu, Cheng, Zhou, Wang, et al._. arXiv 2024  
  [📄 paper](https://arxiv.org/abs/2411.13587) · [💻 code](https://github.com/William-wAng618/roboticAttack)  
  `vla` `robot-manipulation` `embodied-llm`
- 🗡️ **[Jailbreaking LLM-Controlled Robots (RoboPAIR)](https://arxiv.org/abs/2410.13691)** — Automated jailbreak elicits harmful physical actions from LLM-controlled robots (up to 100% ASR).  
  _Robey, Ravichandran, Kumar, Hassani, Pappas_. arXiv 2024  
  [📄 paper](https://arxiv.org/abs/2410.13691) · [🌐 project](https://robopair.org)  
  `embodied-llm` `robot` `autonomous-driving`
- 🗡️ **[Too Afraid to Drive: Semantic DoS Vulnerability in AD Planning (PlanFuzz)](https://arxiv.org/abs/2201.04610)** — Benign-looking roadside objects freeze the planner (DoS); PlanFuzz finds 9 such vulnerabilities.  
  _Wan, Shen, Chuang, Xia, Garcia, Ma, Chen_. NDSS 2022  
  [📄 paper](https://arxiv.org/abs/2201.04610) · [🌐 project](https://sites.google.com/view/secure-safe-ai/planfuzz)  
  `autonomous-driving` `planning`
- 🗡️ **[Dirty Road Can Attack: Security of Automated Lane Centering (DRP)](https://github.com/ASGuard-UCI/DRP-attack)** — A malicious road patch steers a production lane-centering system off its lane.  
  _Sato, Shen, Wang, Jia, Lin, Chen_. USENIX Security 2021  
  [📄 paper](https://www.usenix.org/conference/usenixsecurity21/presentation/sato) · [💻 code](https://github.com/ASGuard-UCI/DRP-attack)  
  `autonomous-driving` `lane-keeping`
- 🗡️ **[Invisible for both Camera and LiDAR: Security of Multi-Sensor Fusion (MSF-ADV)](https://github.com/ASGuard-UCI/MSF-ADV)** — A single 3D adversarial object evades camera+LiDAR fusion → 100% collision in simulation.  
  _Cao, Wang, Xiao, Yang, Fang, Yang, Chen, Liu, Li_. IEEE S&P 2021  
  [📄 paper](https://arxiv.org/abs/2106.09249) · [💻 code](https://github.com/ASGuard-UCI/MSF-ADV)  
  `autonomous-driving` `sensor-fusion` `lidar`
- 🛡️ **[Towards Robust LiDAR-based Perception: Black-box Sensor Attack and Countermeasures (CARLO)](https://arxiv.org/abs/2006.16974)** — Occlusion/physics-based reasoning (CARLO) detects and rejects spoofed LiDAR obstacles.  
  _Sun, Cao, Chen, Mao_. USENIX Security 2020  
  [📄 paper](https://arxiv.org/abs/2006.16974)  
  `autonomous-driving` `lidar`
- 🗡️ **[Adversarial Sensor Attack on LiDAR-based Perception in Autonomous Driving](https://arxiv.org/abs/1907.06826)** — First LiDAR spoofing attack that injects fake close-range obstacles into AV perception.  
  _Cao, Xiao, Cyr, Zhou, Park, Rampazzi, Chen, Fu, Mao_. ACM CCS 2019  
  [📄 paper](https://arxiv.org/abs/1907.06826) · [🌐 project](https://sites.google.com/view/av-ioat-sec/adv-lidar-attack)  
  `autonomous-driving` `lidar`
- 🗡️ **[Robust Physical-World Attacks on Deep Learning Visual Classification (RP2)](https://github.com/evtimovi/robust_physical_perturbations)** — Sticker perturbations on a stop sign cause targeted misclassification from a moving vehicle.  
  _Eykholt, Evtimov, Fernandes, Li, Rahmati, Xiao, Prakash, Kohno, Song_. CVPR 2018  
  [📄 paper](https://arxiv.org/abs/1707.08945) · [💻 code](https://github.com/evtimovi/robust_physical_perturbations)  
  `autonomous-driving` `perception`
- 🗡️ **[ShapeShifter: Robust Physical Adversarial Attack on Faster R-CNN](https://github.com/shangtse/robust-physical-attack)** — First robust targeted physical attack on an object detector; stop signs mis-detected in drive-by tests.  
  _Chen, Cornelius, Martin, Chau_. ECML-PKDD 2018  
  [📄 paper](https://arxiv.org/abs/1804.05810) · [💻 code](https://github.com/shangtse/robust-physical-attack)  
  `autonomous-driving` `object-detection`

### System architecture

_Buses, components, APIs, networking across the cyber-physical system._

#### System architecture · Integrity

- 📚 **[SoK: On the Semantic AI Security in Autonomous Driving](https://arxiv.org/abs/2203.05314)** — Systematizes semantic AD-AI attacks/defenses and ships PASS, an open evaluation platform.  
  _Shen, Wang, Wan, Luo, Sato, Hu, ... Qiao, Chen_. arXiv 2022  
  [📄 paper](https://arxiv.org/abs/2203.05314)  
  `autonomous-driving` `sok`
- 🗡️ **[All Your GPS Are Belong To Us: Towards Stealthy Manipulation of Road Navigation Systems](https://www.usenix.org/conference/usenixsecurity18/presentation/zeng)** — Stealthy GPS spoofing that keeps the route plausible while steering a driver to a target.  
  _Zeng, Liu, Cui, Miao, Yang, Su, Wang, Xu, Yang, Qian_. USENIX Security 2018  
  [📄 paper](https://www.usenix.org/conference/usenixsecurity18/presentation/zeng)  
  `gps` `navigation` `autonomous-driving`

#### System architecture · Safety

- 📚 **[SoK: On the Semantic AI Security in Autonomous Driving](https://arxiv.org/abs/2203.05314)** — Systematizes semantic AD-AI attacks/defenses and ships PASS, an open evaluation platform.  
  _Shen, Wang, Wan, Luo, Sato, Hu, ... Qiao, Chen_. arXiv 2022  
  [📄 paper](https://arxiv.org/abs/2203.05314)  
  `autonomous-driving` `sok`
- 🗡️ **[All Your GPS Are Belong To Us: Towards Stealthy Manipulation of Road Navigation Systems](https://www.usenix.org/conference/usenixsecurity18/presentation/zeng)** — Stealthy GPS spoofing that keeps the route plausible while steering a driver to a target.  
  _Zeng, Liu, Cui, Miao, Yang, Su, Wang, Xu, Yang, Qian_. USENIX Security 2018  
  [📄 paper](https://www.usenix.org/conference/usenixsecurity18/presentation/zeng)  
  `gps` `navigation` `autonomous-driving`

## Stats

- **24** papers — 🗡️ 18 attacks, 🛡️ 4 defenses.
- **12/24** (50%) ship public **code**.

## Contributing

Add a paper by editing [`data/papers.yml`](data/papers.yml) and running `python3 scripts/generate_readme.py`. See [CONTRIBUTING.md](CONTRIBUTING.md). Prioritizing papers whose code is public is the whole point — include the `code:` field whenever a repo exists.

## License

[CC0-1.0](LICENSE) — to the extent possible under law, dedicated to the public domain.

<sub>Generated by `scripts/generate_readme.py` on 2026-09-20. Do not edit README.md by hand.</sub>
