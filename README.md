# IOT_KOALA_RASPERRY_PI

This project uses a Raspberry Pi 3 and a basic 16x2 LCD screen to create an IoT device that automatically connects to a specific hotspot and displays messages from a Firestore database.

## Prerequisites

- **Raspberry Pi 3**
- **16x2 LCD Screen**
- **Python Libraries**: Ensure you have the necessary Python libraries installed (`RPi.GPIO`, `firebase_admin`, `drivers`).
- **Firebase Credentials**: A service account key JSON file from your Firebase project.

## Configuration

1. **Hotspot Configuration**:
   - Configure your Raspberry Pi to auto-connect to a specific hotspot. This can be done by editing the `wpa_supplicant.conf` file:
     ```bash
     sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
     ```
   - Add the following network configuration:
     ```bash
     network={
         ssid="your_hotspot_ssid"
         psk="your_hotspot_password"
         key_mgmt=WPA-PSK
     }
     ```

2. **Crontab Setup**:
   - Add `iot.py` to `crontab -e` to ensure it launches automatically when the Raspberry Pi is turned on:
     ```bash
     crontab -e
     ```
   - Add the following line to the crontab file:
     ```bash
     @reboot python /path/to/your/iot.py &
     ```

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/FIEVET-Cyp/IOT_KOALA_RASPERRY_PI.git
   cd IOT_KOALA_RASPERRY_PI
