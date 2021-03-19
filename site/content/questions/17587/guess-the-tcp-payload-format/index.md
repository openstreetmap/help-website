+++
type = "question"
title = "Guess the TCP payload format"
description = '''I&#x27;m trying to guess the communication protocol between a program and a webserver. I&#x27;ve already captured the packets and gotten the Ethernet, IP and TCP layers, and now I want to make sense of the payload. It makes no sense in ASCII. I&#x27;m reasonably sure the payload is not encrypted, and I&#x27;m guessing ...'''
date = "2013-01-10T13:12:00Z"
lastmod = "2013-01-11T12:12:00Z"
weight = 17587
keywords = [ "decode" ]
aliases = [ "/questions/17587" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Guess the TCP payload format](/questions/17587/guess-the-tcp-payload-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17587-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to guess the communication protocol between a program and a webserver. I've already captured the packets and gotten the Ethernet, IP and TCP layers, and now I want to make sense of the payload. It makes no sense in ASCII.</p><p>I'm reasonably sure the payload is not encrypted, and I'm guessing it's mainly compressed in some way. I'm also guessing it's something fairly mainstream and something that was available years ago already. And once I guess this layer, I'm pretty sure the rest is near to ASCII.</p><p>I've tried clicking through a number of the Transport decoders in Wireshark, but I don't really know what to look for. I've also tried saving the first packet and decoding it with gzip.</p><p>This is nothing naughty. I can already see the data in the program itself, and I just want to write a program of my own to automatically pick out some data and enrich it in order to automate some tedious tasks.</p><p>Does anybody have some general pointers?</p><p>I attach a couple of lines of payload starting with the first 1452-byte packet which is the first non-zero payload received.</p><p>Thanks for any ideas, Soren</p><pre><code>00000000  0e 3c 0f 7a 78 9c 8d 58  89 7f 1b b7 95 d6 88 b6 .&lt;.zx..X ........
00000010  63 ca 76 e4 a6 4d 76 d3  dd 3a e3 36 69 e2 c6 b6 c.v..Mv. .:.6i...
00000020  38 a4 48 91 6e 95 ac 25  4b 89 37 4e ec 48 4e d2 8.H.n..% K.7N.HN.
00000030  64 0f 16 33 03 ce 80 83  01 c6 c0 80 e4 b0 ad bb d..3.... ........
00000040  f7 d5 a6 f7 5e bd bb db  63 ff cc 7d ef 41 4a f2 ....^... c..}.AJ.
00000050  4b 6b ed ca 96 08 0c 80  ef 5d df 7b 78 c3 b3 57 Kk...... .].{x..W
00000060  d7 eb d5 a8 db db 1c b4  3b 6d a7 12 c9 a7 3a 57 ........ ;m....:W
00000070  db fb ed 34 36 5c 29 6e  60 68 13 5d d7 0d 0c ca ...46\)n `h.]....
00000080  dc 4e 39 7c 26 da 4d b5  8b 46 5b 5d 98 14 ce d4 .N9|&amp;.M. .F[]....
00000090  92 a9 0c 86 2c 36 2c cb  70 87 e4 33 81 28 31 33 ....,6,. p..3.(13
000000A0  8a d7 16 f1 78 6c b4 c5  b5 e9 44 bb 1a d1 78 c8 ....xl.. ..D...x.
000000B0  4c c6 15 8e 6d 29 6c 25  10 c2 94 fe a0 64 29 27 L...m)l% .....d)&#39;
000000C0  80 d8 26 39 0c 26 ce 22  4c ce 65 29 32 a3 61 58 ..&amp;9.&amp;.&quot; L.e)2.aX
000000D0  f1 9a 1b dc 33 d7 72 c2  49 67 16 3b 83 03 ae 0b ....3.r. Ig.;....
000000E0  52 c2 2a c1 70 64 99 4a  72 4d 03 67 c8 a6 94 cb R.*.pd.J rM.g....
000000F0  09 09 ca 78 c9 a5 44 d1  86 0b 2b d0 8c 89 30 3c ...x..D. ..+...0&lt;
00000100  c9 05 9f a0 10 7d 0d c5  4e 99 2a 71 0b 13 e0 12 .....}.. N.*q....
00000110  54 a7 64 26 66 a4 98 aa  67 e8 05 81 66 d4 42 89 T.d&amp;f... g...f.B.
00000120  a5 26 5f d8 52 4b e9 dd  27 a4 64 13 87 a3 9a 4f .&amp;_.RK.. &#39;.d....O
00000130  98 92 6e 81 50 a2 20 67  68 3b 45 85 c1 2a 42 9b ..n.P. g h;E..*B.
00000140  26 25 5b 90 5c 85 1e e7  73 1e 13 c8 c4 08 9e 4a &amp;%[.\... s......J
00000150  bf 07 1c 29 5d 22 1c 2a  e6 52 ed b5 51 22 29 08 ...)]&quot;.* .R..Q&quot;).
00000160  8f c3 56 04 60 4e 26 39  b9 65 02 91 b4 24 ad 1a ..V.`N&amp;9 .e...$..
00000170  c3 4e a9 e7 3e 88 74 b4  90 14 b0 3c 17 06 1c 4d .N..&gt;.t. ...&lt;...M
00000180  b1 73 69 ca bb e4 eb b2  aa c9 8f 61 21 e2 58 d4 .si..... ...a!.X.
00000190  4b 12 90 14 5c d2 f9 4c  d4 9a 9b 0c 51 e2 84 91 K...\..L ....Q...
000001A0  fd ba 14 78 92 2d b8 8c  3a b8 3b 24 d7 ea 39 c2 ...x.-.. :.;$..9.
000001B0  e9 7a 9c 30 e5 bc 9e 4c  8d e1 d7 96 cc 1f e3 f8 .z.0...L ........
000001C0  b0 8c 8d 73 8a 84 30 d5  90 14 96 b2 12 0f 2b 6d ...s..0. ......+m
000001D0  62 74 48 ce a6 ba a2 cf  12 bc 49 96 4e 9d 8f 5f btH..... ..I.N.._
000001E0  26 27 5a 66 c4 d3 24 1a  f5 87 28 37 6d ac e5 ce &amp;&#39;Zf..$. ..(7m...
000001F0  0e 46 a8 70 ce 2d c8 83  63 30 99 19 f0 25 33 e9 .F.p.-.. c0...%3.
00000200  f6 1e 38 05 1c 94 12 19  4a 5d b2 14 2d 66 d2 29 ..8..... J]..-f.)
00000210  34 c4 72 93 92 0f 97 02  15 8d 21 94 0d d0 84 1e 4.r..... ..!.....
00000220  01 c7 e1 af 60 2a ea a1  ac 82 d5 cb 92 79 1a ce ....`*.. .....y..
00000230  e9 2f c4 a4 24 d5 c7 a9  37 da 02 65 0a a2 11 50 ./..$... 7..e...P
00000240  03 57 f8 8c 09 8a 9f 28  19 d9 60 1d 4f d1 2e 84 .W.....( ..`.O...
00000250  a9 44 c2 ac d5 24 49 2d  f1 33 d5 49 69 89 b3 26 .D...$I- .3.Ii..&amp;
00000260  e6 6a 93 62 c4 96 0d f1  5a ea 82 4c b0 2c 21 8a .j.b.... Z..L.,!.
00000270  88 34 e3 b5 4e d9 11 2b  3d e9 32 c3 94 9e f1 9a .4..N..+ =.2.....
00000280  5c 00 54 80 15 e4 ea 9c  d9 23 16 d5 90 0b 0b 1c \.T..... .#......
00000290  cf 98 64 68 3a 46 75 2e  64 3a 9e e7 c2 d6 64 66 ..dh:Fu. d:....df
000002A0  45 d9 97 35 a5 3a a2 ac  9e 49 12 5a b2 8c a2 67 E..5.:.. .I.Z...g
000002B0  34 b7 86 d5 b8 c6 0a 8a  10 73 85 67 22 b2 14 44 4....... .s.g&quot;..D
000002C0  a0 2d 86 a3 6e 12 0f a6  0e a9 57 90 9b 27 13 4a .-..n... ..W..&#39;.J
000002D0  19 88 37 fa 8e 95 5a 48  fb a1 b8 2e ed 4e 8a b4 ..7...ZH .....N..
000002E0  a0 1c 56 4a d8 02 e9 50  e8 24 af 98 2c 49 be f6 ..VJ...P .$..,I..
000002F0  f5 81 89 94 8d cb 62 ac  24 a9 cd e2 71 9f aa 06 ......b. $...q...
00000300  d4 0d 54 0a 32 51 6d a2  ac 86 d6 b5 b1 4b 67 0a ..T.2Qm. .....Kg.
00000310  47 91 b3 a1 ae 26 3e 79  4b 61 28 13 6b 08 50 c6 G....&amp;&gt;y Ka(.k.P.
00000320  28 89 45 36 a7 f3 b5 0f  b7 1f 8c bb 23 64 41 5e (.E6.... ....#dA^
00000330  66 a8 63 15 3b 95 e2 b1  6a 82 b5 84 32 2c 84 4c f.c.;... j...2,.L
00000340  ae 21 13 71 6c c0 99 5a  20 7f ac 71 28 5f 1b 51 .!.ql..Z  ..q(_.Q
00000350  87 a5 36 84 38 35 1a 3f  f2 44 f5 b7 30 98 9c 39 ..6.85.? .D..0..9
00000360  f2 74 26 6c 89 a0 19 04  67 81 83 03 a8 7c 3b be .t&amp;l.... g....|;.</code></pre></div><div id="question-tags" class="tags-container tags">decode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '13, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/f90bcd97d0e6f0119e95199b2a3b8592?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shein&#39;s gravatar image" /><p>shein<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shein has no accepted answers">0%</span></p></div></div><div id="comments-container-17587" class="comments-container"></div><div id="comment-tools-17587" class="comment-tools"></div><div class="clear"></div><div id="comment-17587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17591"></span>

<div id="answer-container-17591" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17591-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your best shot may be to right click on one of the packets and use "follow tcp stream" You'll get another window that shows you the content of the packets in one window.<br />
</p><p>From there, try to see if anything looks usable. For example, EXE files all start with "MZ" (it's the initials of the guy that was in charge of dos exe format). Or you might see "PK" for a zip file. I'm going to guess that PK stands for PKWare (blast from the past!).<br />
</p><p>Open up other files with an ascii aditor to see if you can figure it out.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '13, 19:03</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></br></p></div></div><div id="comments-container-17591" class="comments-container"></div><div id="comment-tools-17591" class="comment-tools"></div><div class="clear"></div><div id="comment-17591-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17619"></span>

<div id="answer-container-17619" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17619-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I attach a couple of lines of payload starting with the first 1452-byte packet which is the first non-zero payload received.</p></blockquote><p>With only one packet it is impossible to detect/guess any data format, as you would not detect any repeating pattern (sequences) throughout the communication.</p><blockquote><p>This is nothing naughty. I can already see the data in the program itself,</p></blockquote><p>if you can post some plain text samples (from your program) together with the captured conversation, it might be possible to detect a system behind the data encoding.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '13, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jan '13, 12:55</p></div></div><div id="comments-container-17619" class="comments-container"></div><div id="comment-tools-17619" class="comment-tools"></div><div class="clear"></div><div id="comment-17619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

