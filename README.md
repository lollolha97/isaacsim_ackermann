# 🚗 **IsaacSim Ackermann Navigation & SLAM**
*A ROS 2-based Navigation and SLAM framework optimized for Ackermann steering vehicles in NVIDIA Isaac Sim 4.5.*

---

## 📌 **Overview**
This project aims to provide a **fully integrated navigation and SLAM stack** tailored for Ackermann steering vehicles in **NVIDIA Isaac Sim 4.5**.  
By leveraging **ROS 2 Navigation2**, **SmacPlannerHybrid**, and **nav2_regulated_pure_pursuit_controller**, this package delivers:  

✅ **Hybrid A* global planning optimized for Ackermann kinematics**  
✅ **A pure pursuit-based local planner with dynamic speed regulation**  
✅ **SLAM support with Cartographer and SLAM-Toolbox**  
✅ **Seamless integration with NVIDIA Isaac Sim**  

This package enables **realistic autonomous navigation**, overcoming conventional differential drive limitations in Ackermann vehicles.

---

## 🖥️ **System Requirements**
- **Operating System**: Ubuntu 22.04  
- **ROS 2 Distribution**: Humble Hawksbill  
- **Simulation Framework**: NVIDIA Isaac Sim 4.5  
- **Hardware**: CUDA-enabled GPU recommended for optimal simulation performance  

---

## 📁 **Package Structure**
### 🎮 **Control Module**
1. **Ackermann Teleoperation & Velocity Conversion**
   - `cmdvel_to_ackermann.launch.py`  
     - Standard **cmd_vel to AckermannDriveStamped** conversion (Isaac Sim tutorial equivalent)  
   - `teleop_to_ackermann.launch.py`  
     - Enables direct control via **teleop_twist_keyboard**  

### 🗺️ **SLAM (Simultaneous Localization and Mapping)**
1. **Cartographer-based SLAM**  
   - `cartographer.launch.py` (Supports online mapping and loop closure)  
2. **SLAM-Toolbox-based SLAM**  
   - `slam_toolbox.launch.py` (Provides both lifelong and static mapping modes)  

### 🚀 **Navigation**
1. **Localization-based Navigation**  
   - `localization.launch.py` (Requires pre-built maps)  
2. **Integrated SLAM & Navigation**  
   - `bringup.launch.py`  
     - `ackermann_fast.yaml` (Optimized for high-speed navigation)  
     - `ackermann_param.yaml` (General navigation settings)  

---

## 🛠️ **Installation**
### **1️⃣ Install Required ROS 2 Packages**
```bash
sudo apt update && sudo apt install -y \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup \
    ros-humble-cartographer \
    ros-humble-cartographer-ros \
    ros-humble-slam-toolbox \
    ros-humble-nav2-regulated-pure-pursuit-controller \
    ros-humble-nav2-smac-planner
```

### **2️⃣ Clone and Build the Package**
```bash
cd ~/ros2_ws/src
git clone https://github.com/lollolha97/isaacsim_ackermann.git
cd ~/ros2_ws
colcon build --symlink-install
source install/local_setup.bash
```

---

## ▶️ **Execution Guide**
### **1️⃣ Manual Control via Teleoperation**
####  Convert cmd_vel to ackermann_cmd
```bash
# cmd_vel to ackermann_cmd
ros2 launch cmdvel_to_ackermann cmdvel_to_ackermann.launch.py

ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
#### Or you can just use teleop-twist-keyboard for control
```bash
# cmd_vel to ackermann_cmd
ros2 launch cmdvel_to_ackermann cmdvel_to_ackermann.launch.py
```

### **2️⃣ SLAM Initialization**
```bash
# Launch Cartographer SLAM
ros2 launch ackermann_slam cartographer.launch.py

# Launch SLAM-Toolbox
ros2 launch ackermann_slam slam_toolbox.launch.py
```

###  **3️⃣ SLAM & Navigation Execution**
```bash
ros2 launch ackermann_nav bringup.launch.py
```



---

## 🔧 **Key Improvements & Planner Optimization**
### ✅ **Global Planner: SmacPlannerHybrid**
- **Hybrid A* algorithm implementation**
- **Ackermann-aware path planning**, preventing unnecessary rotations  
- **Efficient path smoothing**, reducing sharp turns  

### ✅ **Local Planner: nav2_regulated_pure_pursuit_controller**
- **Dynamic speed regulation based on path curvature**  
- **Improved path tracking for Ackermann vehicles**  
- **Elimination of unnecessary backtracking and unstable rotations**  

These optimizations ensure smooth and realistic **Ackermann-based autonomous navigation**, effectively addressing the constraints of traditional differential-drive planners.

---

## 🚀 **Known Issues & Future Enhancements**
🚀 Current limitations and potential enhancements for improved navigation performance:
- ✅ **Spurious circular path generation upon goal arrival** (to be resolved)  
- ✅ **Elimination of Spin Recovery behavior, as Ackermann vehicles cannot pivot**  
- ✅ **Handling of trajectory inconsistencies near obstacles**  

---

## 🔗 **References & External Repositories**
- 📌 **NVIDIA IsaacSim ROS Workspaces**: [IsaacSim-ros_workspaces](https://github.com/isaac-sim/IsaacSim-ros_workspaces)  
- 📌 **NeuronBot2 (Base Framework)**: [NeuronBot2](https://github.com/Adlink-ROS/neuronbot2)  
- 📌 **ROS 2 Navigation2**: [Navigation2](https://github.com/ros-planning/navigation2)  
- 📌 **Smac Planner (Hybrid A*)**: [SmacPlannerHybrid](https://github.com/ros-planning/navigation2/tree/main/nav2_smac_planner)  
- 📌 **Regulated Pure Pursuit Controller**: [nav2_regulated_pure_pursuit_controller](https://github.com/ros-planning/navigation2/tree/main/nav2_regulated_pure_pursuit_controller)  

---

### 🎯 **Final Notes**
This repository serves as a **complete navigation and SLAM solution for Ackermann-based robotic platforms** in simulation environments.  
The integration with **NVIDIA Isaac Sim 4.5** allows high-fidelity physics simulations, enabling realistic testing for **autonomous vehicle applications**.  

If you have any questions or suggestions for improvements, feel free to contribute or open an issue! 🚀

