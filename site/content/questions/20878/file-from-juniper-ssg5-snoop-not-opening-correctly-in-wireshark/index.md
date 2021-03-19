+++
type = "question"
title = "File from Juniper SSG5 &quot;snoop&quot; not opening correctly in Wireshark"
description = '''I&#x27;m running Wireshark 1.8.6. I&#x27;ve done this process before, using the snoop command on a Juniper SSG router, capturing the screen output of the snoop to a text file, then opening it in Wireshark. However, today, every packet appears corrupt (wrong timestamp, wrong protocol info, etc.). Here&#x27;s a samp...'''
date = "2013-05-01T10:19:00Z"
lastmod = "2013-05-01T16:46:00Z"
weight = 20878
keywords = [ "juniper", "snoop", "wireshark" ]
aliases = [ "/questions/20878" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [File from Juniper SSG5 "snoop" not opening correctly in Wireshark](/questions/20878/file-from-juniper-ssg5-snoop-not-opening-correctly-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20878-score" class="post-score" title="current number of votes">0</div><span id="post-20878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running Wireshark 1.8.6. I've done this process before, using the snoop command on a Juniper SSG router, capturing the screen output of the snoop to a text file, then opening it in Wireshark. However, today, every packet appears corrupt (wrong timestamp, wrong protocol info, etc.). Here's a sample of what I'm trying to open. It "looks" the same as files I've previously used, but something must be hinky.</p><pre><code>2425847.0: ethernet0/0(i) len=106:b89bc97b41ee-&gt;2c6bf507bac0/0800
              98.201.24.84 -&gt; 50.196.184.45/17
              vhl=45, tos=20, id=5488, frag=0000, ttl=116 tlen=92
              udp:ports 56192-&gt;2925, len=72
              2c 6b f5 07 ba c0 b8 9b c9 7b 41 ee 08 00 45 20     ,k.......{A...E.
              00 5c 15 70 00 00 74 11 ca f2 62 c9 18 54 32 c4     .\.p..t...b..T2.
              b8 2d db 80 0b 6d 00 48 98 9a e0 1b 7d ae f8 40     .-...m.H....}[email protected]
              14 47 49 3a f3 14 74 11 30 41 ac ff 1c fe 55 2e     .GI:..t.0A....U.
              03 31 1f e6 3b 9a 43 4b 07 94 30 52 9e c9 b7 37     .1..;.CK..0R...7
              6d 80 d4 fb 55 14 01 6a d7 91 82 8d 6b 8b d6 5a     m...U..j....k..Z
              ae 01 e4 af 7e 0f d5 88 64 78                       ....~...dx

2425847.0: ethernet0/0(i) len=106:b89bc97b41ee-&gt;2c6bf507bac0/0800
              98.201.24.84 -&gt; 50.196.184.45/17
              vhl=45, tos=20, id=5490, frag=0000, ttl=116 tlen=92
              udp:ports 56192-&gt;2925, len=72
              2c 6b f5 07 ba c0 b8 9b c9 7b 41 ee 08 00 45 20     ,k.......{A...E.
              00 5c 15 72 00 00 74 11 ca f0 62 c9 18 54 32 c4     .\.r..t...b..T2.
              b8 2d db 80 0b 6d 00 48 f2 35 64 4a 1d 50 2e 41     .-...m.H.5dJ.P.A
              16 a4 7b 82 50 83 5b b4 d4 f4 42 8a d0 4c 44 86     ..{.P.[...B..LD.
              5b 24 cf cb bd 0a 4a f4 b7 14 28 03 c7 91 09 7f     [$....J...(.....
              73 c4 db ea 63 22 02 79 cd 13 22 88 98 b3 5a 86     s...c&quot;.y..&quot;...Z.
              49 f2 42 88 e7 aa 04 cf b1 72                       I.B......r

2425847.0: ethernet0/0(i) len=948:b89bc97b41ee-&gt;2c6bf507bac0/0800
              134.170.2.85 -&gt; 50.196.184.45/17
              vhl=45, tos=20, id=0, frag=4000, ttl=48 tlen=934
              udp:ports 8192-&gt;1811, len=914
              2c 6b f5 07 ba c0 b8 9b c9 7b 41 ee 08 00 45 20     ,k.......{A...E.
              03 a6 00 00 40 00 30 11 d3 36 86 aa 02 55 32 c4     [email protected]
              b8 2d 20 00 07 13 03 92 bd 06 52 13 3d 68 16 a8     .-........R.=h..
              c6 53 2c 11 27 25 e2 38 0f aa a9 bd d0 9b 0e 67     .S,.&#39;%.8.......g
              1e b2 6a 2a 8c 10 64 42 7d 22 a6 06 6a 78 d2 ec     ..j*..dB}&quot;..jx..
              8d 47 20 d9 5d 59 4f 7f 20 02 84 6e ed 0d e1 e5     .G..]YO....n....
              89 52 53 6d 08 7d 8f 7d 93 7e 57 7d 30 f4 1b 63     .RSm.}.}.~W}0..c
              a0 41 50 65 c1 7e 3a b8 2b 05 bc 1f 69 dd bd d2     .APe.~:.+...i...
              4e 59 4a 76 5c 05 e9 72 57 52 ce 36 a4 e6 c9 d5     NYJv\..rWR.6....
              49 e4 8e 72 f8 3a e4 11 b2 9e ae 41 2f 8e d9 ae     I..r.:.....A/...
              cf ca 97 89 a9 12 d8 cb 64 4d 0c 42 89 70 8a 4b     ........dM.B.p.K
              f9 1a b8 8f 8c ac eb 1b a2 74 eb 7c ac 85 30 88     .........t.|..0.
              2c eb 04 e7 37 3c 76 9b ce 04 40 b8 90 0a 1d 7d     ,...7&lt;[email protected]}
              c3 44 32 79 cc 3c e0 a5 cf 39 2f 0c f5 93 50 c5     .D2y.&lt;...9/...P.
              ea 45 21 e5 d7 ed 45 a3 04 22 51 a1 af df d2 cd     .E!...E..&quot;Q.....
              93 ce f1 f0 57 f3 03 1a 4d f4 15 06 e6 96 5c e6     ....W...M.....\.
              78 fb dc 7b 7b c7 e9 09 46 c7 25 cc 44 dd 42 12     x..{{...F.%.D.B.
              b3 6d 1b e0 63 28 86 63 eb 37 d6 70 78 7e 6b 92     .m..c(.c.7.px~k.
              8c e8 16 95 1a c7 b0 f1 05 49 e8 eb 27 33 17 9d     .........I..&#39;3..
              72 65 b7 c0 29 98 85 a0 c4 96 33 9d d9 49 9e 3c     re..).....3..I.&lt;
              13 57 2a e0 d3 b2 be 81 63 d4 8d 6f 8c 9f cf b7     .W*.....c..o....
              d2 cf 07 6e eb fa 18 81 20 5c d2 77 b4 b6 c1 e5     ...n.....\.w....
              8d 80 a4 3f 4c 33 a9 37 08 e7 d8 6f a9 5a cd 42     ...?L3.7...o.Z.B
              91 d3 ce 81 a5 16 56 c0 c9 1d 91 e4 33 b3 d1 25     ......V.....3..%
              56 51 16 5f a2 d8 d1 84 d3 e3 4b e8 02 34 d7 90     VQ._......K..4..
              60 eb d9 44 f1 9c 21 e1 c2 cc 37 8b 13 7d b4 d3     `..D..!...7..}..
              b9 2f b5 79 cd 07 98 f2 0f 28 18 28 ad d0 61 3c     ./.y.....(.(..a&lt;
              9c 21 44 dd 80 fc f0 4a f3 e8 a3 ca f1 28 b4 d5     .!D....J.....(..
              14 28 22 8a d8 a3 3b cc 58 14 55 11 0e 53 ff 3d     .(&quot;...;.X.U..S.=
              c5 f2 42 b2 54 4d 82 c4 79 35 9b 76 d4 88 d8 60     ..B.TM..y5.v...`
              9b 83 4b 1c ca 1a 84 6f b9 f2 9a 5f 60 02 96 6a     ..K....o..._`..j
              9a 47 68 e4 c7 4d 92 33 5f a5 11 ef 94 b5 cb a9     .Gh..M.3_.......
              d8 e3 92 33 7a b5 a0 6d 42 c8 df 8a ca b2 8a 93     ...3z..mB.......
              9d 31 90 14 2b b7 87 a0 ec dd a0 61 c8 a0 ee 2c     .1..+......a...,
              10 9c de 0a fa 24 02 6f 3c 62 cc 1c 99 86 29 b6     .....$.o&lt;b....).
              2c 16 6c fd 30 af d6 97 ee 4b 79 fe 04 21 7f 7d     ,.l.0....Ky..!.}
              6a e1 96 17 8e 20 de 83 2c fa 56 6b 31 b2 71 24     j.......,.Vk1.q$
              bc 2b 3f 0a 13 60 04 aa e2 a3 d0 5d d5 32 ff 20     .+?..`.....].2..
              2b 38 ed a2 e5 6d ab 5f 5a 72 02 c8 0b ad e4 01     +8...m._Zr......
              7f c5 d0 ec 63 23 6f e7 03 98 14 b8 b0 b4 8a 7c     ....c#o........|
              0a 55 ec 00 6d c8 a1 8f ec e8 19 cb ee e2 6c e2     .U..m.........l.
              c3 fb 35 a0 18 36 60 fc af 15 e6 61 1f 2a 65 fc     ..5..6`....a.*e.
              7b 54 24 a1 84 83 95 e4 e5 1f 74 27 e7 81 f2 b6     {T$.......t&#39;....
              8e 50 cb ac 74 94 97 cc 51 8e ae 04 6c b0 90 e0     .P..t...Q...l...
              97 82 41 81 c8 54 dc 1a be e5 f1 46 8d ab 4e c5     ..A..T.....F..N.
              ae 02 61 3b fd 01 b6 58 b6 3e 4c 61 ea c6 b5 5e     ..a;...X.&gt;La...^
              2d ca 0d 09 1e b0 78 db 9a 5b 2c 49 46 72 a6 9f     -.....x..[,IFr..
              f0 59 27 23 c4 af ec 21 01 9c 80 b9 14 e8 a7 1a     .Y&#39;#...!........
              4b 5c ac 95 02 0c 9f 2c e5 df 84 ef 0c d9 3c 4b     K\.....,......&lt;K
              d7 61 ab 32 d4 77 df cb d8 ff 8e 88 52 10 e3 53     .a.2.w......R..S
              dd 30 19 21 49 2c 9d ea 4e 6a e3 75 fa a1 a1 da     .0.!I,..Nj.u....
              fc 76 3a a8 12 25 40 ab 77 2d 2c af d5 d1 b8 06     .v:..%@.w-,.....
              c4 cc 29 c2 3e c3 7f 44 4d 2a 97 05 ac c3 e2 a2     ..).&gt;..DM*......
              33 03 fc 73 5b d9 24 84 77 37 49 24 d3 69 3e be     3..s[.$.w7I$.i&gt;.
              bd da d8 0f 74 76 b4 b1 3d 06 a5 f8 2f 11 9d ba     ....tv..=.../...
              0f a5 d4 bf ef d4 ac b3 6a a0 e2 7d f3 f2 23 c6     ........j..}..#.
              06 fb ec 8c 2d 14 98 df 93 23 9b fd 98 1c 92 26     ....-....#.....&amp;
              c1 d8 15 07 08 41 55 d6 59 9f fb b4 1f 42 80 9a     .....AU.Y....B..
              fa 93 2d 0a ab df e8 6a e5 a6 3d 3e 77 51 8a 01     ..-....j..=&gt;wQ..
              f4 13 32 3a                                         ..2:

2425847.0: ethernet0/0(i) len=103:b89bc97b41ee-&gt;2c6bf507bac0/0800
              98.201.24.84 -&gt; 50.196.184.45/17
              vhl=45, tos=20, id=5491, frag=0000, ttl=116 tlen=89
              udp:ports 56192-&gt;2925, len=69
              2c 6b f5 07 ba c0 b8 9b c9 7b 41 ee 08 00 45 20     ,k.......{A...E.
              00 59 15 73 00 00 74 11 ca f2 62 c9 18 54 32 c4     .Y.s..t...b..T2.
              b8 2d db 80 0b 6d 00 45 e1 c4 fd 0f 7d 48 ff 45     .-...m.E....}H.E
              1d 26 e5 00 13 f0 3c ba d0 1f 43 d9 3e e4 e8 e8     .&amp;....&lt;...C.&gt;...
              de 8a cc 13 a5 b1 00 7f 0b cd 9a a0 ee 20 55 7d     ..............U}
              76 64 bc 39 ca 75 d1 08 82 15 9a 31 4f 9d 88 e1     vd.9.u.....1O...
              24 d7 05 94 ea 42 b6                                $....B.

2425847.0: ethernet0/0(i) len=106:b89bc97b41ee-&gt;2c6bf507bac0/0800
              98.201.24.84 -&gt; 50.196.184.45/17
              vhl=45, tos=20, id=5493, frag=0000, ttl=116 tlen=92
              udp:ports 56192-&gt;2925, len=72
              2c 6b f5 07 ba c0 b8 9b c9 7b 41 ee 08 00 45 20     ,k.......{A...E.
              00 5c 15 75 00 00 74 11 ca ed 62 c9 18 54 32 c4     .\.u..t...b..T2.
              b8 2d db 80 0b 6d 00 48 ef 42 0a 36 5d e0 05 19     .-...m.H.B.6]...
              ed 1a df b9 21 65 fc 9c 38 c3 e5 e1 3d 59 93 c9     ....!e..8...=Y..
              44 3d ec f2 a1 29 e8 91 a5 55 28 6d 1f c1 5a ac     D=...)...U(m..Z.
              c9 5c f9 85 41 9c 5c 50 8b 93 76 67 f3 f1 0e b3     .\..A.\P..vg....
              37 dd 99 ba 50 39 aa 07 46 ec                       7...P9..F.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-juniper" rel="tag" title="see questions tagged &#39;juniper&#39;">juniper</span> <span class="post-tag tag-link-snoop" rel="tag" title="see questions tagged &#39;snoop&#39;">snoop</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '13, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/6970e82da5ba3a59c94679580f11154d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jimstowe01&#39;s gravatar image" /><p><span>jimstowe01</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jimstowe01 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 May '13, 11:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-20878" class="comments-container"></div><div id="comment-tools-20878" class="comment-tools"></div><div class="clear"></div><div id="comment-20878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20881"></span>

<div id="answer-container-20881" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20881-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20881-score" class="post-score" title="current number of votes">0</div><span id="post-20881-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When I run tshark on the snoop output, it dissects fine:</p><pre><code>$ tshark -r snoop.txt 
  1        0.0 98.201.24.84 -&gt; 50.196.184.45 UDP 106 Source port: 56192  Destination port: 2925
  2        0.0 98.201.24.84 -&gt; 50.196.184.45 UDP 106 Source port: 56192  Destination port: 2925
  3        0.0 134.170.2.85 -&gt; 50.196.184.45 UDP 948 Source port: spytechphone  Destination port: scientia-sdb
  4        0.0 98.201.24.84 -&gt; 50.196.184.45 UDP 103 Source port: 56192  Destination port: 2925
  5        0.0 98.201.24.84 -&gt; 50.196.184.45 UDP 106 Source port: 56192  Destination port: 2925
$</code></pre><p>But this is with SVN 48477 (newer than 1.8.6).</p><p>What does your tshark 1.8.6 on your system show?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '13, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20881" class="comments-container"><span id="20888"></span><div id="comment-20888" class="comment"><div id="post-20888-score" class="comment-score"></div><div class="comment-text"><p>OK, I had a look at the source and the following revision solved the issue:</p><pre><code>r46905 | guy | 2013-01-02 23:56:24 +0100 (wo, 02 jan 2013) | 9 lines

Update TODO list - the first two items are done, and with stuff added to
support pcap-NG we might have a better way of doing the third item (more
stuff is needed, but that stuff belongs there for pcap-NG, too).

When parsing hex dump lines, skip leading white space, and skip lines
that have nothing but white space, rather than guessing where the hex
dump information ends based on the line length.  Parse the hex bytes
manually.</code></pre><p>I added this revision to be ported to 1.8.7, in the mean time, you can use an <a href="http://www.wireshark.org/download/automated/">automated build</a>.</p></div><div id="comment-20888-info" class="comment-info"><span class="comment-age">(01 May '13, 16:46)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-20881" class="comment-tools"></div><div class="clear"></div><div id="comment-20881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20885"></span>

<div id="answer-container-20885" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20885-score" class="post-score" title="current number of votes">0</div><span id="post-20885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>However, today, every packet appears corrupt (wrong timestamp, wrong protocol info, etc.)</p></blockquote><p>1.8.6 on Windows XP shows the wrong IP addresses (e.g. src 201.24.84.50 instead of 98.201.24.84). 1.9.2 shows the correct IP addresses.</p><p><strong>Reason:</strong> 1.8.6 'drops' some bytes in the frames (apparently it is the last byte of every line). Looks like a bug.</p><pre><code>First Frame HEX + Text

1.8.6

0000  2c 6b f5 07 ba c0 b8 9b c9 7b 41 ee 08 00 45 00   ,k...... .{A...E.
0010  5c 15 70 00 00 74 11 ca f2 62 c9 18 54 32 b8 2d   \.p..t.. .b..T2.-
0020  db 80 0b 6d 00 48 98 9a e0 1b 7d ae f8 14 47 49   ...m.H.. ..}...GI
0030  3a f3 14 74 11 30 41 ac ff 1c fe 55 03 31 1f e6   :..t.0A. ...U.1..
0040  3b 9a 43 4b 07 94 30 52 9e c9 b7 6d 80 d4 fb 55   ;.CK..0R ...m...U
0050  14 01 6a d7 91 82 8d 6b 8b d6 ae 01 e4 af 7e 0f   ..j....k ......~.
0060  d5 88 64 78                                        ..dx             

1.9.2

0000  2c 6b f5 07 ba c0 b8 9b c9 7b 41 ee 08 00 45 20  ,k.......{A...E 
0010  00 5c 15 70 00 00 74 11 ca f2 62 c9 18 54 32 c4  .\.p..t...b..T2.
0020  b8 2d db 80 0b 6d 00 48 98 9a e0 1b 7d ae f8 40  .-...m.H....}[email protected]
0030  14 47 49 3a f3 14 74 11 30 41 ac ff 1c fe 55 2e  .GI:..t.0A....U.
0040  03 31 1f e6 3b 9a 43 4b 07 94 30 52 9e c9 b7 37  .1..;.CK..0R...7
0050  6d 80 d4 fb 55 14 01 6a d7 91 82 8d 6b 8b d6 5a  m...U..j....k..Z
0060  ae 01 e4 af 7e 0f d5 88 64 78                    ....~...dx</code></pre><p>As it works in 1.9.2, I recommend to upgrade to the current development release.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '13, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 May '13, 13:34</strong> </span></p></div></div><div id="comments-container-20885" class="comments-container"></div><div id="comment-tools-20885" class="comment-tools"></div><div class="clear"></div><div id="comment-20885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

