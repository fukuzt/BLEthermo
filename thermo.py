# このpyを実行するにはsudo権限が必要です。
# 権限がたりないとscanner.scan()でエラーになります。
from bluepy import btle
import sys
import time
import sendline as line

# define
SERVICE_UUID="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

# global
BLE_ADDRESS="xx:xx:xx:xx:xx:xx"
TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def scan():
    try:
        scanner = btle.Scanner(0)
        devices = scanner.scan(3.0)

        for device in devices:
            print(f'SCAN BLE_ADDR：{device.addr}')

            if(device.addr.lower()==BLE_ADDRESS.lower()):
                print("Find!")
                return True
    except:
        print("scan Error!")
        return False
    print("---")
    return False

class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print("Indicate Handle = " + hex(cHandle))
        print("C1:Temperature Measurement Value(Celsius) = " + data.decode())

        line.send_notify(TOKEN,data.decode())

def main():
    #
    # Scan
    #
    print("<Scan Start>")
    while True:
        scanresult = scan()
        if( scanresult==True):
            break
        time.sleep(3)
    print("Scan End")


    #
    # Connect
    #
    print("Connect Start")
    try:
        peripheral = btle.Peripheral()
        peripheral.connect(BLE_ADDRESS, btle.ADDR_TYPE_RANDOM)
    except:
        print("connect Error!")
        sys.exit(0)

    print("Connected!")
    service = peripheral.getServiceByUUID(SERVICE_UUID)
    peripheral.withDelegate(MyDelegate())

    # Enable Notify
    peripheral.writeCharacteristic(0x000c, b'\x01\x00', True)

    # 通知を待機する
    print("Notify Wait...")
    try:
        TIMEOUT = 3.0
        while True:
            if peripheral.waitForNotifications(TIMEOUT):
                # handleNotification()が呼び出された
                continue

            # handleNotification()がTIMEOUT秒だけ待っても呼び出されなかった
            print("wait...")
    except:
        print("except!")

    print("<end>")

if __name__ == '__main__':
    print(sys.argv[0])
    #global TOKEN
    #TOKEN = sys.argv[1]
    print("token = " + TOKEN)

    #global BLE_ADDRESS
    #BLE_ADDRESS = sys.argv[2]
    print("BLE device = " + BLE_ADDRESS)

    while True:
        main()
        time.sleep(3)

