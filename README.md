# ros2_multi_hik_camera

<span style="color: orange;">⚠️</span>
If this package runs on an ARM64 platform, please modify libs in /hikSDK/lib/arm64 and headers with latest from https://www.hikrobotics.com/en/machinevision/service/download/. You may also copy them from where MVS installed.
<span style="color: orange;">⚠️</span>

A ROS2 packge for Hikvision industrial camera. 
Our purpose is to use GiGE cameras, but it should also works with USB cameras with some modifications:
```C++
nRet = MV_CC_EnumDevices(MV_GIGE_DEVICE, &device_list);
RCLCPP_INFO(this->get_logger(), "Found camera count = %d", device_list.nDeviceNum);
//Replace all MV_GIGE_DEVICE with MV_USB_DEVICE

while (device_list.nDeviceNum == 0 && rclcpp::ok()) {
  RCLCPP_ERROR(this->get_logger(), "No camera found!");
  RCLCPP_INFO(this->get_logger(), "Enum state: [%x]", nRet);
  std::this_thread::sleep_for(std::chrono::seconds(1));
  nRet = MV_CC_EnumDevices(MV_GIGE_DEVICE, &device_list);
  //Replace all MV_GIGE_DEVICE with MV_USB_DEVICE
}
```
Or, you may use ``` MV_GIGE_DEVICE | MV_USB_DEVICE ```, if both two types you have.

## Usage
<span style="color: orange;">⚠️</span>
We noticed that HikSDK headers and libs are not up-to-date might cause all camera unsuccessfully enumed. Even some old models, like CS016 family, their most recent batch had changed their CMOS, and we suspect that it would be the cause.
<span style="color: orange;">⚠️</span>

### Add cameras
1. Create ```/camera${CameraSerialNumber}/hik_camera:``` and its params in config/camera_params.yaml.
2. Create a file ```camera_info_${CameraSerialNumber}.yaml``` in config.
3. In launch file```hik_camera.launch.py```, modify:
   ```Python
   serial_numbers = ['DA3302323', 'DA2584810', 'DA2419544']
   ```
  With every cameras' serial number.

You shoud find serial number on your camera. Also, line 40 of the code could be uncommented to display all the serial numbers of connected devices.
```C++
// RCLCPP_INFO(this->get_logger(), "Device: [%s]", serial.c_str());
```

### Launch nodes
```
ros2 launch hik_camera hik_camera.launch.py
```

## Params
- exposure_time
- gain
