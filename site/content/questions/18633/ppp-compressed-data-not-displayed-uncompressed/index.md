+++
type = "question"
title = "PPP compressed data not displayed uncompressed"
description = '''I am connected via pptp vpn over an ethernet connection to a server. I need to analyze packets to and from the server for a certain application. The application packets on the vpn link are captured as &quot;PPP - Compressed datagram&quot;. The payload packets are not uncompressed in the packet listing so I ca...'''
date = "2013-02-14T08:09:00Z"
lastmod = "2013-02-14T09:00:00Z"
weight = 18633
keywords = [ "ppp", "compressed" ]
aliases = [ "/questions/18633" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PPP compressed data not displayed uncompressed](/questions/18633/ppp-compressed-data-not-displayed-uncompressed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18633-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am connected via pptp vpn over an ethernet connection to a server. I need to analyze packets to and from the server for a certain application. The application packets on the vpn link are captured as "PPP - Compressed datagram". The payload packets are not uncompressed in the packet listing so I can not see the actual payload. Is there a setting or plugin that will uncompress the payloads so I can see the actual data?</p><p>sample packet below:</p><pre><code>No.     Time           Source                Destination           Protocol Length Info
626 230.787803000  192.168.0.36          97.66.74.115          PPP Comp 204    Compressed data

Frame 626: 204 bytes on wire (1632 bits), 204 bytes captured (1632 bits) on interface 0
Ethernet II, Src: WistronI_a4:c4:4c (f0:de:f1:a4:c4:4c), Dst: SierraWi_ff:f0:af (00:a0:d5:ff:f0:af)
Internet Protocol Version 4, Src: 192.168.0.36 (192.168.0.36), Dst: 97.66.74.115 (97.66.74.115)
Generic Routing Encapsulation (PPP)
    Flags and Version: 0x3001
    Protocol Type: PPP (0x880b)
    Key: 0x009e84fc
    Sequence Number: 4783
Point-to-Point Protocol
    Protocol: Compressed datagram (0x00fd)
PPP Compressed Datagram

0000  00 a0 d5 ff f0 af f0 de f1 a4 c4 4c 08 00 45 00   ...........L..E.
0010  00 be 22 ad 00 00 80 2f 00 00 c0 a8 00 24 61 42   ..&quot;..../.....$aB
0020  4a 73 30 01 88 0b 00 9e 84 fc 00 00 12 af fd f2   Js0.............
0030  9d 09 9b 88 20 d8 45 2d cb 97 ff 98 c6 6f 2f 33   .... .E-.....o/3
0040  6c 1b 2c 19 56 56 06 20 eb d4 2d 9b fb 92 f9 58   l.,.VV. ..-....X
0050  ad 99 dd f4 14 2d 44 0c 2b eb 62 1e 0b 6f 8f 08   .....-D.+.b..o..
0060  d5 fd 1d 8b cc 42 84 d6 28 af 7f 60 f6 67 41 65   .....B..(..`.gAe
0070  7f 61 52 3f be 20 91 ed e6 55 14 9e c3 07 2c 8c   .aR?. ...U....,.
0080  0c c6 64 74 65 a9 01 70 c9 13 ab dd fd 0e 14 10   ..dte..p........
0090  f8 a2 22 43 2b 7a a7 df 7d ac 93 5e 3d 69 34 25   ..&quot;C+z..}..^=i4%
00a0  f3 ec c5 4e 73 fa 97 47 47 97 cb da d0 3c 90 39   ...Ns..GG....&lt;.9
00b0  a8 b4 38 7a 54 46 20 4c c3 d0 cf b6 ab a1 45 31   ..8zTF L......E1
00c0  19 47 e1 28 9f 5e f2 a7 91 ca 4b 52               .G.(.^....KR</code></pre></div><div id="question-tags" class="tags-container tags">ppp compressed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '13, 08:09</strong></p><img src="https://secure.gravatar.com/avatar/b071525e0bb5f137b811ef083a04d339?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jcasler&#39;s gravatar image" /><p>jcasler<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jcasler has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Feb '13, 13:55</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-18633" class="comments-container"></div><div id="comment-tools-18633" class="comment-tools"></div><div class="clear"></div><div id="comment-18633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18634"></span>

<div id="answer-container-18634" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18634-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at the current (as of this writing) version of the <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-ppp.c?revision=46359&amp;view=markup">PPP dissector</a>, I see that this functionality is not yet implemented. (See <code>dissect_comp_data</code> at line 4310.) I suggest opening an enhancement bug request for it at the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark bugzilla</a> website.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '13, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-18634" class="comments-container"></div><div id="comment-tools-18634" class="comment-tools"></div><div class="clear"></div><div id="comment-18634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

