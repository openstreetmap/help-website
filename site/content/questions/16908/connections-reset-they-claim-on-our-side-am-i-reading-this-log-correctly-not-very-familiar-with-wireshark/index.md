+++
type = "question"
title = "Connections reset, they claim on our side.  Am I reading this log correctly?  Not very familiar with wireshark"
description = '''We We have a client who uses a web service to pull a report from us. About 5-10% of the time they do not get this report. We are not seeing the request come through on our side at all when this happens. They claim we are closing the connection prematurely. They sent us a wireshark capture and yes it...'''
date = "2012-12-14T11:20:00Z"
lastmod = "2012-12-14T11:34:00Z"
weight = 16908
keywords = [ "rst" ]
aliases = [ "/questions/16908" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Connections reset, they claim on our side. Am I reading this log correctly? Not very familiar with wireshark](/questions/16908/connections-reset-they-claim-on-our-side-am-i-reading-this-log-correctly-not-very-familiar-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16908-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We We have a client who uses a web service to pull a report from us. About 5-10% of the time they do not get this report. We are not seeing the request come through on our side at all when this happens. They claim we are closing the connection prematurely. They sent us a wireshark capture and yes it looks like we are reseting the connection, but my question is what could be causing it to happen? I asked them if we close the connections or leave them open waiting for the requestor to send a FIN. The developers claim we just send them what is requested. It looks like every one of their requests (they are yy.yyy.yy.yyy) is being doubled. Am I reading this correctly and could this cause confusion on our side forcing the reset?</p><pre><code>No.     Time           Source                Destination           Protocol Length Info
    281 303.923383000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      66     53295 &gt; https [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
    282 303.923384000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      66     53295 &gt; https [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=256 SACK_PERM=1
    283 303.937155000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      66     https &gt; 53295 [SYN, ACK] Seq=0 Ack=1 Win=4380 Len=0 MSS=1460 SACK_PERM=1 WS=64
    284 303.937156000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      66     https &gt; 53295 [SYN, ACK] Seq=0 Ack=1 Win=4380 Len=0 MSS=1460 SACK_PERM=1 WS=64
    285 303.937315000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     53295 &gt; https [ACK] Seq=1 Ack=1 Win=65536 Len=0
    286 303.937317000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     [TCP Dup ACK 285#1] 53295 &gt; https [ACK] Seq=1 Ack=1 Win=65536 Len=0
    287 303.937725000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    216    Client Hello
    288 303.937726000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    216    [TCP Retransmission] Client Hello
    289 303.950975000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [ACK] Seq=1 Ack=163 Win=5504 Len=0
    290 303.950977000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     [TCP Dup ACK 289#1] https &gt; 53295 [ACK] Seq=1 Ack=163 Win=5504 Len=0
    291 303.952020000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1514   Server Hello
    292 303.952023000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1514   [TCP Retransmission] Server Hello
    293 303.952178000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP segment of a reassembled PDU]
    294 303.952185000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP Retransmission] [TCP segment of a reassembled PDU]
    295 303.952188000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     53295 &gt; https [ACK] Seq=163 Ack=2921 Win=64000 Len=0
    296 303.952189000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     [TCP Dup ACK 295#1] 53295 &gt; https [ACK] Seq=163 Ack=2921 Win=64000 Len=0
    297 303.952190000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    921    Ignored Unknown Record
    298 303.952191000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    921    [TCP Retransmission] Ignored Unknown Record
    299 303.953303000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    368    Client Key Exchange, Change Cipher Spec, Encrypted Handshake Message
    300 303.953304000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    368    [TCP Retransmission] Client Key Exchange, Change Cipher Spec, Encrypted Handshake Message
    301 303.984319000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    101    Change Cipher Spec, Encrypted Handshake Message
    302 303.984331000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    101    [TCP Retransmission] Change Cipher Spec, Encrypted Handshake Message
    303 303.984388000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     53295 &gt; https [ACK] Seq=477 Ack=3835 Win=65536 Len=0
    304 303.984389000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     [TCP Dup ACK 303#1] 53295 &gt; https [ACK] Seq=477 Ack=3835 Win=65536 Len=0
    305 303.985621000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    464    Application Data
    306 303.985677000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    464    [TCP Retransmission] Application Data
    307 304.032039000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    104    Application Data
    308 304.032051000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    104    [TCP Retransmission] Application Data
    309 304.032307000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    686    Application Data
    310 304.032310000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    686    [TCP Retransmission] Application Data
    311 304.083331000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [ACK] Seq=3885 Ack=1519 Win=8896 Len=0
    312 304.083333000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     [TCP Dup ACK 311#1] https &gt; 53295 [ACK] Seq=3885 Ack=1519 Win=8896 Len=0
    313 304.236770000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1082   Application Data
    314 304.236822000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1082   [TCP Retransmission] Application Data
    315 304.237640000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    465    Application Data
    316 304.237643000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    465    [TCP Retransmission] Application Data
    317 304.250988000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [ACK] Seq=4913 Ack=1930 Win=10176 Len=0
    318 304.250989000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     [TCP Dup ACK 317#1] https &gt; 53295 [ACK] Seq=4913 Ack=1930 Win=10176 Len=0
    319 304.252000000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    104    Application Data
    320 304.252002000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    104    [TCP Retransmission] Application Data
    321 304.252003000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     53295 &gt; https [ACK] Seq=1930 Ack=4963 Win=65536 Len=0
    322 304.252040000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     [TCP Dup ACK 321#1] 53295 &gt; https [ACK] Seq=1930 Ack=4963 Win=65536 Len=0
    323 304.252280000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    1332   Application Data
    324 304.252284000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    1332   [TCP Retransmission] Application Data
    325 304.303301000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [ACK] Seq=4963 Ack=3208 Win=12736 Len=0
    326 304.303302000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     [TCP Dup ACK 325#1] https &gt; 53295 [ACK] Seq=4963 Ack=3208 Win=12736 Len=0
    327 305.340999000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP segment of a reassembled PDU]
    328 305.341003000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP Retransmission] https &gt; 53295 [ACK] Seq=4963 Ack=3208 Win=12736 Len=1460
    329 305.341177000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP segment of a reassembled PDU]
    330 305.341180000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    578    Application Data
    331 305.341188000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP Out-Of-Order] [TCP segment of a reassembled PDU]
    332 305.341190000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      578    [TCP Retransmission] [TCP segment of a reassembled PDU]
    333 305.341192000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     53295 &gt; https [ACK] Seq=3208 Ack=7883 Win=64000 Len=0
    334 305.341193000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     [TCP Dup ACK 333#1] 53295 &gt; https [ACK] Seq=3208 Ack=7883 Win=64000 Len=0
    335 305.342236000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     53295 &gt; https [ACK] Seq=3208 Ack=8407 Win=65536 Len=0
    336 305.342237000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     [TCP Dup ACK 335#1] 53295 &gt; https [ACK] Seq=3208 Ack=8407 Win=65536 Len=0
    337 308.092541000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    464    Application Data
    338 308.092543000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    464    [TCP Retransmission] Application Data
    339 308.105882000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [ACK] Seq=8407 Ack=3618 Win=15296 Len=0
    340 308.105885000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     [TCP Dup ACK 339#1] https &gt; 53295 [ACK] Seq=8407 Ack=3618 Win=15296 Len=0
    341 308.107059000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    104    Application Data
    342 308.107069000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    104    [TCP Retransmission] Application Data
    343 308.107356000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    686    Application Data
    344 308.107359000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    686    [TCP Retransmission] Application Data
    345 308.158886000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [ACK] Seq=8457 Ack=4250 Win=17792 Len=0
    346 308.158888000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     [TCP Dup ACK 345#1] https &gt; 53295 [ACK] Seq=8457 Ack=4250 Win=17792 Len=0
    347 308.297669000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1082   Application Data
    348 308.297673000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1082   [TCP Retransmission] Application Data
    349 308.298460000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    465    Application Data
    350 308.298463000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    465    [TCP Retransmission] Application Data
    351 308.311815000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [ACK] Seq=9485 Ack=4661 Win=20352 Len=0
    352 308.311825000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     [TCP Dup ACK 351#1] https &gt; 53295 [ACK] Seq=9485 Ack=4661 Win=20352 Len=0
    353 308.312762000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    104    Application Data
    354 308.312772000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    104    [TCP Retransmission] Application Data
    355 308.313067000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    1332   Application Data
    356 308.313071000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    1332   [TCP Retransmission] Application Data
    357 308.362855000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [ACK] Seq=9535 Ack=5939 Win=22912 Len=0
    358 308.362856000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     [TCP Dup ACK 357#1] https &gt; 53295 [ACK] Seq=9535 Ack=5939 Win=22912 Len=0
    359 308.405276000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP segment of a reassembled PDU]
    360 308.405279000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP Retransmission] https &gt; 53295 [ACK] Seq=9535 Ack=5939 Win=22912 Len=1460
    361 308.405444000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP segment of a reassembled PDU]
    362 308.405447000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    578    Application Data
    363 308.405456000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP Out-Of-Order] [TCP segment of a reassembled PDU]
    364 308.405458000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      578    [TCP Retransmission] [TCP segment of a reassembled PDU]
    365 308.405461000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     53295 &gt; https [ACK] Seq=5939 Ack=12455 Win=64000 Len=0
    366 308.405462000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     [TCP Dup ACK 365#1] 53295 &gt; https [ACK] Seq=5939 Ack=12455 Win=64000 Len=0
    367 308.407103000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     53295 &gt; https [ACK] Seq=5939 Ack=12979 Win=65536 Len=0
    368 308.407105000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     [TCP Dup ACK 367#1] 53295 &gt; https [ACK] Seq=5939 Ack=12979 Win=65536 Len=0
    369 313.497652000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    464    Application Data
    370 313.497654000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    464    [TCP Retransmission] Application Data
    371 313.516452000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [ACK] Seq=12979 Ack=6349 Win=25472 Len=0
    372 313.516454000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     [TCP Dup ACK 371#1] https &gt; 53295 [ACK] Seq=12979 Ack=6349 Win=25472 Len=0
    373 313.516465000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    104    Application Data
    374 313.516465000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    104    [TCP Retransmission] Application Data
    375 313.516466000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    686    Application Data
    376 313.516468000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    686    [TCP Retransmission] Application Data
    377 313.562235000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [ACK] Seq=13029 Ack=6981 Win=28032 Len=0
    378 313.562237000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     [TCP Dup ACK 377#1] https &gt; 53295 [ACK] Seq=13029 Ack=6981 Win=28032 Len=0
    379 313.706930000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1082   Application Data
    380 313.706933000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1082   [TCP Retransmission] Application Data
    381 313.707655000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    465    Application Data
    382 313.707658000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    465    [TCP Retransmission] Application Data
    383 313.721060000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [ACK] Seq=14057 Ack=7392 Win=30592 Len=0
    384 313.721062000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     [TCP Dup ACK 383#1] https &gt; 53295 [ACK] Seq=14057 Ack=7392 Win=30592 Len=0
    385 313.722109000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    104    Application Data
    386 313.722110000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    104    [TCP Retransmission] Application Data
    387 313.722360000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    1512   Application Data
    388 313.722363000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TLSv1    1512   [TCP Retransmission] Application Data
    389 313.774209000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [ACK] Seq=14107 Ack=8850 Win=33536 Len=0
    390 313.774211000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     [TCP Dup ACK 389#1] https &gt; 53295 [ACK] Seq=14107 Ack=8850 Win=33536 Len=0
    391 314.648919000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP segment of a reassembled PDU]
    392 314.648976000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP Retransmission] https &gt; 53295 [ACK] Seq=14107 Ack=8850 Win=33536 Len=1460
    393 314.649027000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP segment of a reassembled PDU]
    394 314.649031000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      1514   [TCP Retransmission] [TCP segment of a reassembled PDU]
    395 314.649188000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     53295 &gt; https [ACK] Seq=8850 Ack=17027 Win=64000 Len=0
    396 314.649190000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     [TCP Dup ACK 395#1] 53295 &gt; https [ACK] Seq=8850 Ack=17027 Win=64000 Len=0
    397 314.649194000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1514   Ignored Unknown Record
    398 314.649196000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1514   [TCP Retransmission] Ignored Unknown Record
    399 314.662987000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1514   Ignored Unknown Record
    400 314.662991000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1514   [TCP Retransmission] Ignored Unknown Record
    401 314.662996000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     53295 &gt; https [ACK] Seq=8850 Ack=19947 Win=65536 Len=0
    402 314.662997000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     [TCP Dup ACK 401#1] 53295 &gt; https [ACK] Seq=8850 Ack=19947 Win=65536 Len=0
    403 314.663148000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1514   Ignored Unknown Record
    404 314.663151000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    282    Ignored Unknown Record
    405 314.663153000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    1514   [TCP Out-Of-Order] Ignored Unknown Record
    406 314.663158000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TLSv1    282    [TCP Retransmission] Ignored Unknown Record
    407 314.663159000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     53295 &gt; https [ACK] Seq=8850 Ack=21635 Win=65536 Len=0
    408 314.663160000  yy.yyy.yy.yyy         xx.xx.xx.xxx          TCP      60     [TCP Dup ACK 407#1] 53295 &gt; https [ACK] Seq=8850 Ack=21635 Win=65536 Len=0
    409 374.641772000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [RST, ACK] Seq=21635 Ack=8850 Win=33536 Len=0
    410 374.641774000  xx.xx.xx.xxx          yy.yyy.yy.yyy         TCP      60     https &gt; 53295 [RST, ACK] Seq=21635 Ack=8850 Win=33536 Len=0</code></pre></div><div id="question-tags" class="tags-container tags">rst</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '12, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/4c85e91176b3430e00bea2a82a821f91?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tjohnson333&#39;s gravatar image" /><p>tjohnson333<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tjohnson333 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Dec '12, 11:21</p></div></div><div id="comments-container-16908" class="comments-container"></div><div id="comment-tools-16908" class="comment-tools"></div><div class="clear"></div><div id="comment-16908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16909"></span>

<div id="answer-container-16909" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16909-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is a time gap of 60 seconds between frame 408 and 409 (the first reset from x.x.x.x). It looks like 'some' system closed the connection after a timeout. That could be x.x.x.x itself but it could be a firewall as well, killing an idle connection. As long as you don't have a capture on both sides, you can't tell who is sending the RESET, especially as the capture was taken on the side of y.y.y.y.</p><p>These systems could have sent the RESET:</p><ul><li>x.x.x.x.</li><li>The firewall in front of x.x.x.x</li><li>The firewall in front of y.y.y.y</li></ul><p>I suggest to capture on both sides simultaneously and then compare the capture files.</p><p>Do you see anything in your firewall and/or web server logs for the timestamp of frame 407-410? Do you see their requests at all in the web server logs?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-16909" class="comments-container"><span id="16912"></span><div id="comment-16912" class="comment"><div id="post-16912-score" class="comment-score"></div><div class="comment-text"><p>They open a connection and send requests for a number of reports at a time. The issue is for 1 specific report. The requests are always in specific order with the failing one always last. It does not fail all the time, about 5-10%. They do not always request the same reports every time.</p><p>We see one session open on the firewall for all requests and then any number of requests (usually 2-6) on the load balancer and Web server logs. What we don't ever see is a request on the load balancer that does not make it to the web server. Every request to the LB makes it through to the web server.</p></div><div id="comment-16912-info" class="comment-info"><span class="comment-age">(14 Dec '12, 11:56)</span> tjohnson333</div></div><span id="16913"></span><div id="comment-16913" class="comment"><div id="post-16913-score" class="comment-score"></div><div class="comment-text"><p>Do they send several requests in one TCP connection?</p><p>In frame 403-404 your server is sending data. In frame 407 they are sending an ACK (408 is just a duplicate due to an error in their capture setup. The same is true for 405/406).</p><p>Then you see the 60 seconds gap. There are some possible scenarios:</p><ul><li>there is more data to send, but your server does not send it. Result: Your fault.</li><li>there is more data to send, your server sent it, but the data did not reach them (capture at their side!). Several reasons: Loadbalancer, Firewalls, etc.</li><li>there is <strong>no more</strong> data to send and their client is doing nothing (should possibly send the next request). After 60 seconds your Loadbalancer closes the <strong>idle connection</strong>. Result: Their fault.</li></ul><p>Without a trace on both sides, it's impossible to say which scenario is the real/right one.</p></div><div id="comment-16913-info" class="comment-info"><span class="comment-age">(14 Dec '12, 12:11)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16909" class="comment-tools"></div><div class="clear"></div><div id="comment-16909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

