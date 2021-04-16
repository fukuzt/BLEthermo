# BLE体温計 データ受信確認用モジュール
import sys
from bluepy import btle

BLE_ADDRESS="xx:xx:xx:xx:xx:xx"

peripheral = btle.Peripheral()
SERVICE_UUID="xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxx"


class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print("Handle = " + hex(cHandle))
#        print("- C1:Temperature Measurement Value(Celsius) = " + hex(data[1])+":"+hex(data[2])+":"+hex(data[3])+":"+hex(data[4]))
        print(data.decode())

if __name__ == '__main__':
    print("Start")
    print("Connecting Wait...")
    try:
        peripheral = btle.Peripheral()
        peripheral.connect(BLE_ADDRESS, btle.ADDR_TYPE_RANDOM)
    except:
        print("connect Error!")
        sys.exit(0)

    print("Connected!")
    peripheral.withDelegate(MyDelegate())

    # Enable Indicate
    peripheral.writeCharacteristic(0x0c, b'\x01\x00', True)

    # 通知を待機する
    print("Indicate Wait...")
    try:
        TIMEOUT = 3.0
        while True:
            if peripheral.waitForNotifications(TIMEOUT):
                # handleNotification()が呼び出された
                continue

            # handleNotification()がTIMEOUT秒だけ待っても呼び出されなかった
            print("wait...")
    except:
        # 切断されるとここにくる
        print("except!")

    print("end")

