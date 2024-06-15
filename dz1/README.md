## Реализация небольшой сети офиса

### Нужно собрать топологию, как показано на схеме(1 балл)

В работе построена сеть соответствующая схеме

![схема](https://github.com/Wiolator/HSE/raw/main/Lab1/img/1.png)

### VPC1 находится в VLAN 10 и сети 10.0.10.0/24 (1 балл)

В конфиге [Switch2](Switch2) в строке 50 указано, что устройство
подключенное через Gi0/0 (VPC1) подключено к VLAN 10.
В файле, [VPC1](VPC1), в 2 строке указано что VPC1 имеет адрес 10.0.10.10 и лежит в 10.0.10.0/24

### VPC2 находится в VLAN 20 и сети 10.0.20.0/24 (1 балл)

В конфиге [Switch3](Switch3) в строке 50 указано, что устройство
подключенное через Gi0/0 (VPC1) подключено к VLAN 10.
В файле, [VPC2](VPC2), в 2 строке указано что VPC1 имеет адрес 10.0.20.10 и лежит в 10.0.20.0/24

### Коммутатор уровня распределения является корнем сети для обоих VLAN (1 балл)

VLAN 10:
```
Switch1#show spanning-tree vlan 10

VLAN0010
  Spanning tree enabled protocol ieee
  Root ID    Priority    24586
             Address     5000.0001.0000
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    24586  (priority 24576 sys-id-ext 10)
             Address     5000.0001.0000
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Gi0/0               Desg LRN 4         128.1    P2p
Gi0/2               Desg LRN 4         128.3    P2p
Gi0/3               Desg LRN 4         128.4    P2p
```

VLAN20:
```
Switch1>show spanning-tree vlan 20

VLAN0020
  Spanning tree enabled protocol ieee
  Root ID    Priority    24596
             Address     5000.0001.0000
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    24596  (priority 24576 sys-id-ext 20)
             Address     5000.0001.0000
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Gi0/0               Desg FWD 4         128.1    P2p
Gi0/2               Desg FWD 4         128.3    P2p
Gi0/3               Desg FWD 4         128.4    P2p
```

### Линк между коммутаторами уровня доступ должен стать заблокированным (1 балл)

Gi0/1 -- состояние BLK
```
Switch3#show spanning-tree vlan 20

VLAN0020
  Spanning tree enabled protocol ieee
  Root ID    Priority    24596
             Address     5000.0001.0000
             Cost        4
             Port        4 (GigabitEthernet0/3)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32788  (priority 32768 sys-id-ext 20)
             Address     5000.0004.0000
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  15  sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Gi0/0               Desg FWD 4         128.1    P2p
Gi0/1               Altn BLK 4         128.2    P2p
Gi0/3               Root FWD 4         128.4    P2p
```

### Клиенты могут отправить друг другу PING (1 балл)

```
VPC1> ping 10.0.20.20

84 bytes from 10.0.20.20 icmp_seq=1 ttl=63 time=17.237 ms
84 bytes from 10.0.20.20 icmp_seq=2 ttl=63 time=6.678 ms
84 bytes from 10.0.20.20 icmp_seq=3 ttl=63 time=6.892 ms
84 bytes from 10.0.20.20 icmp_seq=4 ttl=63 time=8.328 ms
84 bytes from 10.0.20.20 icmp_seq=5 ttl=63 time=8.567 ms
```

```
VPC2> ping 10.0.10.10

84 bytes from 10.0.10.10 icmp_seq=1 ttl=63 time=8.404 ms
84 bytes from 10.0.10.10 icmp_seq=2 ttl=63 time=7.330 ms
84 bytes from 10.0.10.10 icmp_seq=3 ttl=63 time=10.249 ms
84 bytes from 10.0.10.10 icmp_seq=4 ttl=63 time=7.134 ms
84 bytes from 10.0.10.10 icmp_seq=5 ttl=63 time=10.564 ms
```

### Работа выполнена в EVE-NG (1 балл)
Да

### 1 балл - сеть отказоустойчива. Отключение интерфейса не нарушает связанность между клиентами

После отключения линка между Switch2 и Switch3 пинги продолжают доходить благодаря STP, значит сеть -- отказоустойчива.
