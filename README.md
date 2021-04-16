# BLEthermo Last Update 2021/4/16  
for Piper Wave5  

以下はテスト用に動作を細分化したプログラムとなります。段階的に動作検証してください  
*bluepyconnect.py：BLE体温計のUUIDを確認するためのモジュール  
*bluepygatt.py：BLE体温計の計測データを受信、確認するためのモジュール  
*notify_test.py：LINE Notifyの送信確認用モジュール  

thermo.py：メインルーチン  
sendline.py：LINE Notify用サブルーチン  
