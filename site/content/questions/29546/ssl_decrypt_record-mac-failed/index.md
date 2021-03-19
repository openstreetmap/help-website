+++
type = "question"
title = "ssl_decrypt_record: mac failed"
description = '''I believe if the capture contains an &quot;unexpected&quot; frame (e.g., TCP Retransmission), then the SSL decryption gets messed up. Below is an example where the server and client frames start off properly decoded. However, frame 1983 is a TCP Retransmission from the server to client. After this, the client...'''
date = "2014-02-07T22:03:00Z"
lastmod = "2014-06-30T10:42:00Z"
weight = 29546
keywords = [ "ssl", "ssl_decrypt" ]
aliases = [ "/questions/29546" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ssl\_decrypt\_record: mac failed](/questions/29546/ssl_decrypt_record-mac-failed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29546-score" class="post-score" title="current number of votes">0</div><span id="post-29546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I believe if the capture contains an "unexpected" frame (e.g., TCP Retransmission), then the SSL decryption gets messed up.</p><p>Below is an example where the server and client frames start off properly decoded. However, frame 1983 is a TCP Retransmission from the server to client. After this, the client frames are decrypted correctly but the server frames MAC check fails. You can see from the Plaintext array that the decryption is successful. But the GUI doesn't display the expected Decrypted SSL data (I believe) because the MAC check fails.</p><p>I have purposely removed frames 1981 and 1982 as they contain data I would prefer not to display on a public forum but you can clearly see that Frame 1983 is a duplicate of Frame 1980. However, if a developer takes this up, I would be happy to work directly with him/her.</p><p>Frame 1985 Client-to-Server is decoded/displayed correctly. Frame 1987 Server-to-Client is not. From this point forward, Client-to-Server frames continue to be decoded/displayed correctly while Server-to-Client frames are not.</p><pre><code>dissect_ssl enter frame #1978 (first time)
  conversation = 060BC030, ssl_session = 060BC454
  record: offset = 0, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 48
Ciphertext[48]:
| 20 8e f8 0f 22 41 40 d1 83 b2 83 f1 fd 6a cd 1b | Žø.&quot;[email protected]Ñƒ²ƒñýjÍ.|
| 5c d2 e0 b8 86 95 5a d5 78 3a 12 55 6c 6f 64 d5 |\Òà¸†•ZÕx:.UlodÕ|
| 14 ae 24 53 df 61 b9 64 5e 19 a8 7c 70 36 37 00 |.®$Sßa¹d^.¨|p67.|
Plaintext[48]:
| 37 20 53 45 4c 45 43 54 20 22 47 72 65 65 74 69 |7 SELECT &quot;Greeti|
| 6e 67 73 22 0d 0a 7f 90 f1 45 6f 3a 3f a6 fd 7f |ngs&quot;....ñEo:?¦ý.|
| 52 b5 b1 a6 50 9a 58 dd 61 5d 05 05 05 05 05 05 |Rµ±¦PšXÝa]......|
ssl_decrypt_record found padding 5 final len 42
checking mac (len 22, version 301, ct 23 seq 7)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| 7f 90 f1 45 6f 3a 3f a6 fd 7f 52 b5 b1 a6 50 9a |..ñEo:?¦ý.Rµ±¦Pš|
| 58 dd 61 5d                                     |XÝa]            |
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 22, seq = 403, nxtseq = 425
association_find: TCP port 5671 found 00000000
association_find: TCP port 143 found 05509F70
dissect_ssl3_record decrypted len 22
decrypted app data fragment[22]:
| 37 20 53 45 4c 45 43 54 20 22 47 72 65 65 74 69 |7 SELECT &quot;Greeti|
| 6e 67 73 22 0d 0a                               |ngs&quot;..          |
dissect_ssl3_record found association 05509F70

dissect_ssl enter frame #1980 (first time)
  conversation = 060BC030, ssl_session = 060BC454
  record: offset = 0, reported_length_remaining = 180
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 32
Ciphertext[32]:
| 98 9e 56 05 0c 6d 88 f6 9f 1c 5f ed f5 d4 3a d9 |.žV..m.öŸ._íõÔ:Ù|
| 93 21 a6 14 3a 8e fc f2 af 83 f8 0c 97 06 64 be |“!¦.:Žüò¯ƒø.—.d¾|
Plaintext[32]:
| 6f dc e6 86 e2 b1 b9 fd 37 0c 42 c4 6d c8 a5 29 |oÜæ†â±¹ý7.BÄmÈ¥)|
| dd e6 8d 01 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b |Ýæ..............|
ssl_decrypt_record found padding 11 final len 20
checking mac (len 0, version 301, ct 23 seq 17)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| 6f dc e6 86 e2 b1 b9 fd 37 0c 42 c4 6d c8 a5 29 |oÜæ†â±¹ý7.BÄmÈ¥)|
| dd e6 8d 01                                     |Ýæ..            |
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 0, seq = 467, nxtseq = 467
association_find: TCP port 143 found 05509F70
  record: offset = 37, reported_length_remaining = 143
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 48
Ciphertext[48]:
| 64 e6 3f 9e 57 2d c3 e4 15 46 ee 03 e1 25 76 f6 |dæ?žW-Ãä.Fî.á%vö|
| 42 4f 27 52 45 c8 79 13 f4 c8 73 db d9 99 34 52 |BO&#39;REÈy.ôÈsÛÙ.4R|
| 54 c8 28 14 21 54 54 8f 58 b7 a7 25 6f dd e9 06 |TÈ(.!TT.X·§%oÝé.|
Plaintext[48]:
| 2a 20 34 20 45 58 49 53 54 53 0d 0a 89 4b 16 53 |* 4 EXISTS..‰K.S|
| 73 26 8b 94 0e 31 04 14 a8 17 ed 18 77 4e 93 e9 |s&amp;‹”.1..¨.í.wN“é|
| 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f |................|
ssl_decrypt_record found padding 15 final len 32
checking mac (len 12, version 301, ct 23 seq 18)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| 89 4b 16 53 73 26 8b 94 0e 31 04 14 a8 17 ed 18 |‰K.Ss&amp;‹”.1..¨.í.|
| 77 4e 93 e9                                     |wN“é            |
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 12, seq = 467, nxtseq = 479
association_find: TCP port 143 found 05509F70
dissect_ssl3_record decrypted len 12
decrypted app data fragment[12]:
| 2a 20 34 20 45 58 49 53 54 53 0d 0a             |* 4 EXISTS..    |
dissect_ssl3_record found association 05509F70
  record: offset = 90, reported_length_remaining = 90
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 32
Ciphertext[32]:
| 90 3f ce 4d 27 4b 00 4c 60 53 25 f6 7a 9d 7c ec |.?ÎM&#39;K.L`S%öz.|ì|
| 5b fe f2 6a 66 ef 29 ac 8c 02 7f 7c 4a b1 db f7 |[þòjfï)¬Œ..|J±Û÷|
Plaintext[32]:
| f8 ba 6e 60 e4 78 5a 07 18 8e 1d 0d 2b 47 08 f7 |øºn`äxZ..Ž..+G.÷|
| b0 d1 f6 5d 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b |°Ñö]............|
ssl_decrypt_record found padding 11 final len 20
checking mac (len 0, version 301, ct 23 seq 19)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| f8 ba 6e 60 e4 78 5a 07 18 8e 1d 0d 2b 47 08 f7 |øºn`äxZ..Ž..+G.÷|
| b0 d1 f6 5d                                     |°Ñö]            |
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 0, seq = 479, nxtseq = 479
association_find: TCP port 143 found 05509F70
  record: offset = 127, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 48
Ciphertext[48]:
| cf 48 c2 a0 66 78 6d 2f 74 91 d1 bf 4b ac 54 8a |ÏHÂ fxm/t‘Ñ¿K¬TŠ|
| 6e 3e 25 ad 9b d9 74 12 f2 2e fe 13 c4 66 90 0d |n&gt;%­›Ùt.ò.þ.Äf..|
| b0 cb 2b 0a a7 8f e7 ba 86 f0 ac 1b 81 f9 c2 94 |°Ë+.§.çº†ð¬..ùÂ”|
Plaintext[48]:
| 2a 20 30 20 52 45 43 45 4e 54 0d 0a 3e 59 21 cb |* 0 RECENT..&gt;Y!Ë|
| 1f 72 b2 28 f9 1b 32 e4 73 f2 90 51 ac 01 c2 03 |.r²(ù.2äsò.Q¬.Â.|
| 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f |................|
ssl_decrypt_record found padding 15 final len 32
checking mac (len 12, version 301, ct 23 seq 20)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| 3e 59 21 cb 1f 72 b2 28 f9 1b 32 e4 73 f2 90 51 |&gt;Y!Ë.r²(ù.2äsò.Q|
| ac 01 c2 03                                     |¬.Â.            |
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 12, seq = 479, nxtseq = 491
association_find: TCP port 143 found 05509F70
dissect_ssl3_record decrypted len 12
decrypted app data fragment[12]:
| 2a 20 30 20 52 45 43 45 4e 54 0d 0a             |* 0 RECENT..    |
dissect_ssl3_record found association 05509F70

[Frames 1981 and 1982 purposely removed]

dissect_ssl enter frame #1983 (first time)
  conversation = 060BC030, ssl_session = 060BC454
  record: offset = 0, reported_length_remaining = 180
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 32
Ciphertext[32]:
| 98 9e 56 05 0c 6d 88 f6 9f 1c 5f ed f5 d4 3a d9 |.žV..m.öŸ._íõÔ:Ù|
| 93 21 a6 14 3a 8e fc f2 af 83 f8 0c 97 06 64 be |“!¦.:Žüò¯ƒø.—.d¾|
Plaintext[32]:
| d9 a9 ab de 98 e1 f2 44 e2 be 7e 74 1b 22 54 57 |Ù©«Þ.áòDâ¾~t.&quot;TW|
| dd e6 8d 01 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b |Ýæ..............|
ssl_decrypt_record found padding 11 final len 20
checking mac (len 0, version 301, ct 23 seq 33)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| ac 89 6c db a0 bf c4 db 60 c7 ff 80 4c 6a 50 20 |¬‰lÛ ¿ÄÛ`Çÿ.LjP |
| cd 20 18 4f                                     |Í .O            |
ssl_decrypt_record: mac failed
association_find: TCP port 143 found 05509F70
  record: offset = 37, reported_length_remaining = 143
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 48
Ciphertext[48]:
| 64 e6 3f 9e 57 2d c3 e4 15 46 ee 03 e1 25 76 f6 |dæ?žW-Ãä.Fî.á%vö|
| 42 4f 27 52 45 c8 79 13 f4 c8 73 db d9 99 34 52 |BO&#39;REÈy.ôÈsÛÙ.4R|
| 54 c8 28 14 21 54 54 8f 58 b7 a7 25 6f dd e9 06 |TÈ(.!TT.X·§%oÝé.|
Plaintext[48]:
| 2a 20 34 20 45 58 49 53 54 53 0d 0a 89 4b 16 53 |* 4 EXISTS..‰K.S|
| 73 26 8b 94 0e 31 04 14 a8 17 ed 18 77 4e 93 e9 |s&amp;‹”.1..¨.í.wN“é|
| 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f |................|
ssl_decrypt_record found padding 15 final len 32
checking mac (len 12, version 301, ct 23 seq 34)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| b4 84 da 60 14 4a ca 4f 15 60 e1 45 ef c7 c2 86 |´„Ú`.JÊO.`áEïÇÂ†|
| a7 d5 73 d8                                     |§ÕsØ            |
ssl_decrypt_record: mac failed
association_find: TCP port 143 found 05509F70
  record: offset = 90, reported_length_remaining = 90
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 32
Ciphertext[32]:
| 90 3f ce 4d 27 4b 00 4c 60 53 25 f6 7a 9d 7c ec |.?ÎM&#39;K.L`S%öz.|ì|
| 5b fe f2 6a 66 ef 29 ac 8c 02 7f 7c 4a b1 db f7 |[þòjfï)¬Œ..|J±Û÷|
Plaintext[32]:
| f8 ba 6e 60 e4 78 5a 07 18 8e 1d 0d 2b 47 08 f7 |øºn`äxZ..Ž..+G.÷|
| b0 d1 f6 5d 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b |°Ñö]............|
ssl_decrypt_record found padding 11 final len 20
checking mac (len 0, version 301, ct 23 seq 35)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| d2 9b a4 c4 77 1b ba c7 ea b3 ec 40 7d 7d 0d ec |Ò›¤Äw.ºÇê³ì@}}.ì|
| d6 c7 93 fc                                     |ÖÇ“ü            |
ssl_decrypt_record: mac failed
association_find: TCP port 143 found 05509F70
  record: offset = 127, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 48
Ciphertext[48]:
| cf 48 c2 a0 66 78 6d 2f 74 91 d1 bf 4b ac 54 8a |ÏHÂ fxm/t‘Ñ¿K¬TŠ|
| 6e 3e 25 ad 9b d9 74 12 f2 2e fe 13 c4 66 90 0d |n&gt;%­›Ùt.ò.þ.Äf..|
| b0 cb 2b 0a a7 8f e7 ba 86 f0 ac 1b 81 f9 c2 94 |°Ë+.§.çº†ð¬..ùÂ”|
Plaintext[48]:
| 2a 20 30 20 52 45 43 45 4e 54 0d 0a 3e 59 21 cb |* 0 RECENT..&gt;Y!Ë|
| 1f 72 b2 28 f9 1b 32 e4 73 f2 90 51 ac 01 c2 03 |.r²(ù.2äsò.Q¬.Â.|
| 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f |................|
ssl_decrypt_record found padding 15 final len 32
checking mac (len 12, version 301, ct 23 seq 36)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| 72 da fb b5 b3 fb 7b 5c 9a 18 db 06 f1 df bd 6c |rÚûµ³û{\š.Û.ñß½l|
| 0b d1 36 2c                                     |.Ñ6,            |
ssl_decrypt_record: mac failed
association_find: TCP port 143 found 05509F70

dissect_ssl enter frame #1985 (first time)
  conversation = 060BC030, ssl_session = 060BC454
  record: offset = 0, reported_length_remaining = 69
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 64, ssl state 0x3F
packet_from_server: is from server - FALSE
decrypt_ssl3_record: using client decoder
ssl_decrypt_record ciphertext len 64
Ciphertext[64]:
| 33 55 4a 10 3e c9 61 d4 07 27 0d 15 16 d4 10 af |3UJ.&gt;ÉaÔ.&#39;...Ô.¯|
| ea cf 85 d4 6a 6a 19 f2 3d 88 6d 84 48 df 79 c2 |êÏ…Ôjj.ò=.m„HßyÂ|
| 72 f7 e4 b3 45 fb f1 05 8b ce 4b 3e 46 9e fd 47 |r÷ä³Eûñ.‹ÎK&gt;FžýG|
| 85 b9 e3 56 a8 15 ba 25 70 bc 75 57 ec ec 59 c8 |…¹ãV¨.º%p¼uWììYÈ|
Plaintext[64]:
| 38 20 55 49 44 20 53 45 41 52 43 48 20 31 3a 34 |8 UID SEARCH 1:4|
| 20 4e 4f 54 20 44 45 4c 45 54 45 44 0d 0a 00 c4 | NOT DELETED...Ä|
| 59 4c b3 65 06 dd 97 96 67 a5 67 63 2e 03 68 32 |YL³e.Ý—–g¥gc..h2|
| cc 79 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d |Ìy..............|
ssl_decrypt_record found padding 13 final len 50
checking mac (len 30, version 301, ct 23 seq 8)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| 00 c4 59 4c b3 65 06 dd 97 96 67 a5 67 63 2e 03 |.ÄYL³e.Ý—–g¥gc..|
| 68 32 cc 79                                     |h2Ìy            |
ssl_decrypt_record: mac ok
ssl_add_data_info: new data inserted data_len = 30, seq = 425, nxtseq = 455
association_find: TCP port 5671 found 00000000
association_find: TCP port 143 found 05509F70
dissect_ssl3_record decrypted len 30
decrypted app data fragment[30]:
| 38 20 55 49 44 20 53 45 41 52 43 48 20 31 3a 34 |8 UID SEARCH 1:4|
| 20 4e 4f 54 20 44 45 4c 45 54 45 44 0d 0a       | NOT DELETED..  |
dissect_ssl3_record found association 05509F70

dissect_ssl enter frame #1987 (first time)
  conversation = 060BC030, ssl_session = 060BC454
  record: offset = 0, reported_length_remaining = 180
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 32
Ciphertext[32]:
| 64 35 1d 3e 20 13 ae 40 a7 c3 95 7c 18 c0 97 c7 |d5.&gt; .®@§Ã•|.À—Ç|
| f3 59 98 a1 fb 21 e0 f5 1e e7 8b ad 76 30 ff 88 |óY.¡û!àõ.ç‹­v0ÿ.|
Plaintext[32]:
| e3 7b 92 df e4 d8 9a 9d 8c ca f5 27 f4 96 0a ad |ã{’ßäØš.ŒÊõ&#39;ô–.­|
| cd 20 18 4f 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b |Í .O............|
ssl_decrypt_record found padding 11 final len 20
checking mac (len 0, version 301, ct 23 seq 37)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| 68 bf 20 2b 19 0b d2 a1 ff c3 e0 02 d0 34 e2 17 |h¿ +..Ò¡ÿÃà.Ð4â.|
| 6b 37 d9 a5                                     |k7Ù¥            |
ssl_decrypt_record: mac failed
association_find: TCP port 143 found 05509F70
  record: offset = 37, reported_length_remaining = 143
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 48
Ciphertext[48]:
| 8a 87 26 d7 fd be 9b 90 9d 5c 7c c1 59 44 8d dc |Š‡&amp;×ý¾›..\|ÁYD.Ü|
| 81 34 dc 4a 59 ad f8 fa 6d d7 f2 f2 67 e4 ca 27 |.4ÜJY­øúm×òògäÊ&#39;|
| be 7c 84 3f 38 70 e6 71 1c 3f 25 73 4d 40 c8 52 |¾|„?8pæq.?%[email protected]ÈR|
Plaintext[48]:
| 2a 20 53 45 41 52 43 48 20 33 20 35 20 36 20 37 |* SEARCH 3 5 6 7|
| 0d 0a 90 aa 4a 29 5c 7a fe 81 a6 db 60 d5 bb cd |...ªJ)\zþ.¦Û`Õ»Í|
| a0 0f ed 38 cb 05 09 09 09 09 09 09 09 09 09 09 | .í8Ë...........|
ssl_decrypt_record found padding 9 final len 38
checking mac (len 18, version 301, ct 23 seq 38)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| 84 f9 47 25 85 a2 60 ad 7f dd 37 df 12 4d c7 da |„ùG%…¢`­.Ý7ß.MÇÚ|
| 01 22 6b a2                                     |.&quot;k¢            |
ssl_decrypt_record: mac failed
association_find: TCP port 143 found 05509F70
  record: offset = 90, reported_length_remaining = 90
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 32, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 32
Ciphertext[32]:
| f5 1e c0 29 26 f8 3b 5d f5 83 f9 92 bc 91 c5 66 |õ.À)&amp;ø;]õƒù’¼‘Åf|
| 0d 29 39 73 dd 79 35 c2 16 01 0d 27 32 03 c8 47 |.)9sÝy5Â...&#39;2.ÈG|
Plaintext[32]:
| d2 9b a4 c4 77 1b ba c7 ea b3 ec 40 7d 7d 0d ec |Ò›¤Äw.ºÇê³ì@}}.ì|
| d6 c7 93 fc 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b 0b |ÖÇ“ü............|
ssl_decrypt_record found padding 11 final len 20
checking mac (len 0, version 301, ct 23 seq 39)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| 62 5c 77 e5 41 d4 d0 13 03 23 fa f8 72 63 2f 6f |b\wåAÔÐ..#úørc/o|
| a0 b0 3f b6                                     | °?¶            |
ssl_decrypt_record: mac failed
association_find: TCP port 143 found 05509F70
  record: offset = 127, reported_length_remaining = 53
dissect_ssl3_record: content_type 23 Application Data
decrypt_ssl3_record: app_data len 48, ssl state 0x3F
packet_from_server: is from server - TRUE
decrypt_ssl3_record: using server decoder
ssl_decrypt_record ciphertext len 48
Ciphertext[48]:
| 04 44 e0 58 ec bc 8e d1 66 e0 b1 96 7a 15 2e 51 |.DàXì¼ŽÑfà±–z..Q|
| a8 c3 c0 0d 31 53 5f 03 63 55 bb 22 13 06 fd d0 |¨ÃÀ.1S_.cU»&quot;..ýÐ|
| 7f 4e f3 7c 73 52 d6 f6 e5 0e fc 2f 98 14 72 a4 |.Nó|sRÖöå.ü/..r¤|
Plaintext[48]:
| 38 20 4f 4b 20 53 45 41 52 43 48 20 63 6f 6d 70 |8 OK SEARCH comp|
| 6c 65 74 65 0d 0a a0 2b 64 b0 94 3a 82 25 97 68 |lete.. +d°”:‚%—h|
| ce af e9 d3 e0 a9 5c c6 4e 37 05 05 05 05 05 05 |Î¯éÓà©\ÆN7......|
ssl_decrypt_record found padding 5 final len 42
checking mac (len 22, version 301, ct 23 seq 40)
tls_check_mac mac type:SHA1 md 2
Mac[20]:
| 37 ad 70 16 1e 12 53 44 8e e9 53 92 cd 96 e7 8c |7­p...SDŽéS’Í–çŒ|
| af 9f 39 03                                     |¯Ÿ9.            |
ssl_decrypt_record: mac failed
association_find: TCP port 143 found 05509F70</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-ssl_decrypt" rel="tag" title="see questions tagged &#39;ssl_decrypt&#39;">ssl_decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Feb '14, 22:03</strong></p><img src="https://secure.gravatar.com/avatar/c6c2caa5f908add4ea6fc69b99d3132e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gyh&#39;s gravatar image" /><p><span>gyh</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gyh has no accepted answers">0%</span></p></div></div><div id="comments-container-29546" class="comments-container"><span id="34297"></span><div id="comment-34297" class="comment"><div id="post-34297-score" class="comment-score"></div><div class="comment-text"><p>If you still experience this problem, please report it to <a href="https://bugs.wireshark.org/">https://bugs.wireshark.org/</a> with steps to reproduce (ideally a packet capture and secrets). Do not put something sensitive on it as it is a public bug tracker.</p></div><div id="comment-34297-info" class="comment-info"><span class="comment-age">(30 Jun '14, 10:42)</span> <span class="comment-user userinfo">Lekensteyn</span></div></div></div><div id="comment-tools-29546" class="comment-tools"></div><div class="clear"></div><div id="comment-29546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

