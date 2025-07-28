import time
from datetime import datetime
from bmx160_imu.DFRobot_BMX160 import BMX160

def main():
    bmx160 = BMX160(bus=1)
    if not bmx160.begin():
        print("BMX160 initialization failed.")
        return

    bmx160.set_accel_range(BMX160.AccelRange_2G)
    bmx160.set_gyro_range(BMX160.GyroRange_250DPS)

    log_file = "magnetometer_log.txt"
    print(f"Logging started... Output file: {log_file}")

    try:
        with open(log_file, "w") as f:
            start_time = time.time()
            while True:
                data = bmx160.get_all_data()
                mag = data[0:3]

                # Log in tab-separated format
                line = f"{mag[0]:.2f}\t{mag[1]:.2f}\t{mag[2]:.2f}\n"
                f.write(line)

                # Optionally show preview on screen
                # print(f"[{datetime.now().strftime('%H:%M:%S')}] Logged: {line.strip()}")
                time.sleep(0.2)

    except KeyboardInterrupt:
        print("\nLogging stopped by user.")

if __name__ == "__main__":
    main()
