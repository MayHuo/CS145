#### Problem2
##### 2.1
row_size = 3+4+10+5+4+2+4+224=256 bytes
##### 2.2 How many rows can be stored per 64MB IO blocks?
rows = $\lfloor{64MB / 256B}\rfloor$ = 250,000
##### 2.3 How many 2x64MB blocks would you need to store 2 million rows?
256B x 2,000,000/(2x64MB) = 4
##### 2.4 How large in MB will the table of course reviews be?
quarters x rows_each_quarter x bytes_per_row/1000000 = quarters x (students_take_classes x classes_per_student) x 0.5
		= 40 x 15000 x 3 x 0.5 x 256/1000000 = 230.4MB
##### 2.5 How many 64MB blocks would be needed to store the course reviews table?
blocks = $\lceil230.4MB/64MB\rceil$ = 4
##### 2.6 How long would it take in hours to retrieve an evaluation (row) if the table rows are stored randomly on HDD? HDD access takes 10ms, transfer speed 100MB/sec
For each row, we need to access the HDD and retrieve the data, check if we find the row we wanted, then return. 
rows = 900,000
bytes_per_row = 256

900000 x access + scanTime = 900000 x 10ms + 230.4MB/100MBps = 2.5 hours
##### 2.7 How long would it take in seconds if rows are grouped in 64MB blocks(which are randomly stored in HDD)?
For each 64MB block, we need to access the HDD and retrieve the data and transfer
blocks = 4
4 x access + scanTime = 4 x 0.01 sec + dataSize/scanSpeed = 0.04 + 230.4MB/100MBps = 2.7 seconds

#### Problem 3
##### 3.1 What is the average response time for a query? All data stored randomly on HDD. row_size = 64KB
0.01 seconds, Which is the access time for HDD.


##### 3.2
A fixed 1% of the table rows are responsible for 90% of the query traffic.

1% tables rows = 32 GB stored in RAM, then only 10% query need to access HDD
so the average response time in secs is 0.001 secs
#### Problem 4
##### 4.1 - 4.5
- user_id: 1 billion users, 1000000000, 需要多少 bits 来保存呢？$\lceil\log_2N\rceil$ = $\frac{\log_{10}N}{\log_210} ≈ 30$  -- int32
- user_name: char[64]
- item_id: 1 billion items, 100000000, int32
- item_name: char[64]
- transaction_id: 1 trillion, 1000000000000, int64
- money_of_transactions $: float
##### 4.6
bytes_per_row = 4 + 64 + 4 + 64 + 8 + 4 = 148 bytes
##### 4.7 
table_size = rows x bytes_per_row = 1000000000000 x 148 = 148 TB
#### Problem 5
##### 5.1
RAM transfer speed: 100GB/sec
Table Size: 200TB
period = 200TB/100GB/sec = 2000 secs
##### 5.2
SSD access takes: 10us
SSD transfer speed: 5GB/sec
For 1 trillion rows and 200TB size table, 
if each row is randomly stored in the SSD, then for each row, we need to retrieve from SSD, then
hours_used = (1 trillion x 10us + 200TB/5GBps)/3600 = 2788.9
##### 5.3
Data in SSD 64MB-blocks
blocks: 200TB/64MB = 3.125 x $10^6$
hours_used = (3.125 x $10^6$ x 10us + 200TB/5GBps)/3600  = 11.12
##### 5.4
HDD access takes: 10ms
HDD transfer speed: 100MB/sec
if each row is randomly stored in the HDD, we need to read from HDD
days_used = 1 trillion x ($10^{-2}$ secs + 148B/100MB/sec) /(3600x24) = 132870
##### 5.5
If table is stored in 4x64MB blocks, then we read from HDD as blocks
For each blocks, secs_used = 0.01 + 4x64MB/100MB/sec = 2.57 secs
blocks = 200TB/4x64MB 
days_used = 781250x2.57/3600x24 = 23
##### 5.6
cost_of_ram = 200TB/32GB x $100 = 625000
##### 5.7
cost_of_HDD = 200TB/1TB x $25 = 5000
#### Problem 6
##### 6.1
products table
users table
transactions table
orders table
##### 6.2
bits for 5 billion products of unique product id
bits = $\lceil\log_25000000000\rceil$ = 33
bigint
##### 6.3
bits for 1 billion users of unique user id
bits = $\lceil\log_21000000000$ = 30
int
##### 6.4
bytes_per_row = 8 + 8 + 4 + 4+4+4+100 = 132 bytes
##### 6.5
100 million orders / day x 7 days/week = $10^8$ x 7 x 132 / $10^6$ = 92400MB
##### 6.6
RAM access can be ignored
RAM transfer speed: 100GB/sec
millsec_used = 132B/100G/sec x 1000 = 1.32x$10^{-3}$ ms
##### 6.7
700 million records are in random locations on HDD
days_used_one_record = 700 million x (10ms + 132B/100MB/sec) / (3600x24) = (7000000 + 7x132)/(3600x24) = 81
##### 6.8
10GB table, 700 million rows, divide into 64MB blocks
blocks = 10GB/64MB = 16 
secs_per_block = 10ms + 64MB/100MB/sec = 0.65 secs
secs_used_one_row = 16 x 0.65 = 10 secs
##### 6.9 
The speed of looking up one record will be faster if we divide data into 10 machines.
Assume we divide 64MB into 10 machines, then we can read from 10 machines paralleled, each machine for 6400KB.

secs_used_one_row = 10 x (10ms + 6400KB/100MB/sec) = 740ms = 0.74 secs
10 secs/0.74 secs = 13.5
##### 6.10
Network transfer takes 1us
(network) 10GB/5GBps + (RAM on machine1) 10GB/100GBps + (RAM on machine2) 10GB/100GBps  = 2.2 secs

