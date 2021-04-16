# BLE体温計 UUID確認用モジュール
from bluepy import btle

BLE_ADDRESS="xx:xx:xx:xx:xx:xx"

peripheral = btle.Peripheral()
peripheral.connect(BLE_ADDRESS, btle.ADDR_TYPE_RANDOM)

for service in peripheral.getServices():
    print(f'Service UUID：{service.uuid}')
    for characteristic in service.getCharacteristics():
        print(f'- Characteristic UUID：{characteristic.uuid} , Handle：{hex(characteristic.getHandle())} , Property：{characteristic.propertiesToString()}')

