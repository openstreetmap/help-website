+++
type = "question"
title = "I seem to be having an issue with recovering an html page from wireshark, for a class project!"
description = '''As i mentioned i need to extract html code of a website from a wire shark capture file and save it as an html file so it will display relatively the same as if i was on the site but it just displays random characters, i understand how to follow tcp streams and that&#x27;s how i am saving these specific p...'''
date = "2013-02-27T17:34:00Z"
lastmod = "2013-02-27T19:53:00Z"
weight = 18950
keywords = [ "html", "http", "websites", "packet" ]
aliases = [ "/questions/18950" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I seem to be having an issue with recovering an html page from wireshark, for a class project!](/questions/18950/i-seem-to-be-having-an-issue-with-recovering-an-html-page-from-wireshark-for-a-class-project)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18950-score" class="post-score" title="current number of votes">-1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As i mentioned i need to extract html code of a website from a wire shark capture file and save it as an html file so it will display relatively the same as if i was on the site but it just displays random characters, i understand how to follow tcp streams and that's how i am saving these specific packets but each test ends in failure... Do i have to save the capture file first before i try to extract?</p><p>Update 1!</p><p>This is code that is generated when i try to follow the tcp stream and export the packet (Note that no matter what setting i use it will not show up as having html, no matter what packet i try to read(Aside from a few))</p><pre><code>GET /download.html HTTP/1.1

Host: www.wireshark.org

User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Cookie: ln_sess=959910332560; __utma=87653150.804353448.1362024480.1362024480.1362024480.1; __utmb=87653150.1.10.1362024480; __utmc=87653150; __utmz=87653150.1362024480.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ln_c=1362024495742%2C/download.html%2C1

Connection: keep-alive

Cache-Control: max-age=0

HTTP/1.1 200 OK

Date: Thu, 28 Feb 2013 01:24:52 GMT

Server: Apache/2

Accept-Ranges: bytes

X-Mod-Pagespeed: 1.2.24.1-2300

Vary: Accept-Encoding

Content-Encoding: gzip

X-Slogan: It&#39;s a great product with a great story to tell. I&#39;m pumped!

Cache-control: max-age=0, no-cache

Content-Length: 5510

Keep-Alive: timeout=5, max=90

Connection: Keep-Alive

Content-Type: text/html

...........\.r........L..3.).....r./I.q.%.....
&quot;!.6E0.)Y.3U.i...&#39;....Y..d....X$.t7z..X...u......1yy...t....:$N.....=....&lt;.q.M.;~..g.$....f3w..
9...{.d..x*..O. ..N.)...F.6.....~....s.%Sc*..O...&quot;.&#39;Gb....O=S..4....,l.....
Y.........\...2Bn....F .H.Q.\_L.S.N#.........t.$...NmvW.I.1k;..N&lt;_)G..%...2.X
e...`...;S.V...7....1.1.3.......g.......k.../.........H!...*...&#39;...Ie..I.h/-.....?....m.~..1A)[email protected]_D.........v.Y...T....E.....}..h.%.....c....qB....w..I.Q...T.^..G...Mz....tFS...........).A{&amp;i.3Y.`.....RmG....s*...]..$U......vB..jD.j..X)|&quot;D........w.V&lt;.3.J.=.......
....D.C1..
..4...{.&quot;._.I~....h......G......0.`D.|.E&#39;c!.&#39;0.
.b`......d
...).....K...!.l!T...1.....N....x.J}.b.YI..L..K..%.Z.....D.&lt;..4^*..G1&lt;.j/)I7X/.....K..].....1#3!.`C...l&quot;TB .....R$..!.x.......:|)./...R..8..hn..n.g5.y.....iz....w...q..AV.8...z..%..g.5.OX........0.x.&quot;.bf=...UO.6....63..\...MY.5.L.n.5..............1p.4.R...H..nN...+.T......-.....:
.3.g.a....
..&#39;....9eTFk.2fa\QH |.k...K/..
.,.....jA..uE(y.2..^..!.h.rr.N.V...H.)...u.C.....r.zG...WU6..t.FP..3.]c...~...z....3..E{.#r&amp;...q|...e..=B3.x.u.S.j`Sf.n.l).7..........l.....T0.c..?N.+.....$.....l..i$&quot;5.nhn..l.....qP%.......P.....GSHSh.&quot;[email protected][email protected]\.,zNq........V...\!sb.6...iZ..._.hR..f.16.....)k.T&amp;...8...?z.........m.4..l...~..&gt;.&amp;..%.S....%[email protected]#Q..k..V..t0.Y.g.&amp;...-....H.A.5.E-...j1Zy......T
.fo........h.vnT...P.U.#.+...k..h.4...D&quot;...p.....R.L3..&gt;....%.&quot;[.,.%.x..M[[email protected]&quot;M........)..b.S..8..)..Q......[.(umYv. t$...OHd#.Q..(.uE..F..c...gTQ.c..C...*R.C.DC%r....M.Y,A ....t.........P.....}[email protected]_.
....D........fq.......H...6..]....Cl..Y..t.)M.A.I.4!ApH.,...T.hu.L...:(....y.M...t....P..u.....H.Ae......L.M.0....6..3..!...T....E......h...n.. ....q.....V..............u].c .,.@j.......;=..i6.]....)..h.....h...h..D3..ME.v..
f..U.`...n.tB.;..r:=.J....x{.w..}..Qv...Y..].....l..`...C........CX..Z.?.....:....+..d..`L......./...R*..F*...li......&#39;....|.............B|..U...!......z...Vy.....H|...V.......i....vq.....2......-.....q....pe..*7..N.....{t.-x....`..qt...@6..o...X{B...,Y.....:ji.......K:.E.X
h1Q.H.4...Y.N.....u.
..D[..D%.z.ZH.
qEx.+.$.1........&amp;....W....
[email protected]+a......M...Obh.*..+\...U-.*Ii.Ri.{..x.=\.T.j..U|.)..B.Ua{8.....Q.+q..v..k.Y/..W.V6...U.Q../..*....HAL..
)..Y.4|.V..F..1..\0S.h.)2.........t1...Zl....2.s`.U...7I.
SVC.,.~.I*.K^
I.X.U.vQ......Y.J1.:..f.y..R0$.%..pT.D-k.&lt;...%`...y.Bb...X/..l!5&#39;..X..X.)..X.y..v.j.&quot;.f7:..O....A_.....%..........-...b.NY,.b.x&quot;.\.....2v1.B..).....U.,.....um..4x. .....D..L..C.&quot;vs........
g.lP.
[email protected]&#39;...Bc..s\L.O.b.%.*.!....
r.j..r.m..&lt;..........S...].&gt;BTg.n..e.OU=v.?w... .p...f...~.Ps1r.W.;M..t.O^..
...*#A.#.U..
....&quot;...*67{Sa.{..\Lo....Dx...A....&gt;......IA...,H.dV&quot;..b
..A.......-.cY...).....[%..$.${....h.....M#^.
..Um
YWE.....*.B83.Y.....|....[9DLNq..rE.7..o....).l....&gt;_.}.........S...e.;aO.x.e....P...(.......+..2..,.8..z.R.#.k....q_y.....r.........o...-ZN....i;.1..C...8.(|[email protected]&quot;j.aT..q:...F..?......,.u..$..Q.......S..i.^c..=8&quot;C..l..O....Fh.C ...3Y.w&gt;0.....p9..rdL.d
:.......yjmE..{........^.Kr.@v.G..tP....r.x....3.%.FL.0..._...D......&amp;%W.,...u.y.z....F..
~.F.3....y.V..........&amp;.:.7.VS....f:.lf.........EPHigsH..P&#39;.c:..eN&gt;.CX*.N;e.P...5.*n..h...&gt;.........M.....86..uf.(.$HH.z...S+x 3;.:[email protected]$..{d&#39;..wn?e.*.yQ?..\&amp;)
.&gt;U&gt;.y....F=..z&quot;9
.x.?;|u.~.h.4......O......f..h..{.w&gt;......1...&gt;...!......gR..&lt; .D......O....=...Y:q....y.&#39;...|4....&gt;S.5.....u...VJ....*.......;o.{..!4L...d.l7.HDt;.....w...A2n...#..f+.&amp;
..l._2.....90.N9..2.?y......:.C...../.-h.......P).H8.EB...zB.L...p.F..\..O..v...+.i..#.....N..Hx.X..MOR.l.....#...R..F.......U.Bl. oZ...|8&amp;?.I...wy.q....&lt;.;.....x?.{xgu....~.z3..C~..^..R/y.....g.:...=...F.m6I....q..A...v..,[email protected]=.z..8q.0.8=x.,..I#5......c.X.Po...([.\....l..|..........:.L...Nn...S..`..A......]...&amp;...
.c..oU. .......&gt;....f.....k\..I......
....r....,.....g...Z..8.
.(+.c...&#39;...A{....y:&#39;o.l. ..&amp;.......gO...}f.q=T....6.b*...z).5L.........T.KP.&quot;..m7..O..!.&amp;{.1X...dL.J.H(.........;B....q.....Y.......Z..E.0..c.X.z....Q.b.
TP.^8...? ..19..#F.. .F.w)...9.}.....a. G.`..).ZD.J1d..h..._......B......-...G#\...L.niw..e.B.l&quot;..Y_...u...)....q.iR........c.3...:.19y.|...f..|s.|...0.j.:..^-.Afs..........w.Va..].arjw.
[email protected],... ..U.G.r1....i.s.|W...Zn(....&gt;f..y.tK...&amp;........d..O=(.&#39;f.Z..|..w..bL.&lt;..|[email protected]=....P_......]...A..X?....GW......A.gU.NZ^s&gt;....(Buk.s.[dz....A.%..A3S.......
.L.&lt;am.]=o0.&quot;j.w)]t..0C.T....`.L..&#39;.:Gl.i.2...o..S...w.6.m.........f..+Rp.......;=....1.t.........,...
..G....B..\.4..Gl..59.....2......}m..^vA..........5........;.a.!|.#..X.7..ADi...].|d.............VY..b..a.Z..US..7.^..m.....B.j.g...T..g.[K%.,...1.z......~N......_....z.-~......f....{f.&gt;....u.yO....:?..|..O./..........&lt;.R#. .;o.Q.}.....&amp;m..?].....,.&lt;......{..^R......JvLZh0..;..*.........C...p,.....+..........RHC=b~.....#me..(.%k....&gt;{.
.....d.*...=..{.R~\0...}5.&lt;.{.+.l............^.d.T....r.(.Q.......f...saJ.../0..L.8..&gt;?.....I
[email protected]+.P.......L.S../...z.]......~.....rA..|s.F:.....Fp....K..[....h,....h........K%...u...d...o...^..f.ROH!..,.*?ST....Ze.s....9....l7{...._.....Wi....RI.#.......C.....^.1...?7..%...]J6......n....&#39;.....nTM.S.x:._...k.....3}.m.E/-...
[email protected]
[email protected]&#39;v6...dc.....~&#39;h.].G.]v.7.S.1......^).........~Fi/...E...4....Q.Np..M3...77..._U..r...C.....,..=....%....v.....56../.0.7..?.pjx...z.`?I..,r...l.a..`..a&lt;........^..&amp;...5.h.k...F..._.?v..^.M..GET /css/I.ws-2011-10.css.pagespeed.cf.015AT2yzlN.css HTTP/1.1

Host: www.wireshark.org

User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0

Accept: text/css,*/*;q=0.1

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Referer: http://www.wireshark.org/download.html

Cookie: ln_sess=959910332560; __utma=87653150.804353448.1362024480.1362024480.1362024480.1; __utmb=87653150.1.10.1362024480; __utmc=87653150; __utmz=87653150.1362024480.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ln_c=1362024495742%2C/download.html%2C1

Connection: keep-alive

If-Modified-Since: Mon, 25 Feb 2013 17:23:09 GMT

If-None-Match: W/&quot;0&quot;

Cache-Control: max-age=0

HTTP/1.1 304 Not Modified

Date: Thu, 28 Feb 2013 01:24:52 GMT

Server: Apache/2

Connection: Keep-Alive

Keep-Alive: timeout=5, max=89

Cache-control: public, max-age=14400

GET /mirrors.js HTTP/1.1

Host: www.wireshark.org

User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0

Accept: */*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Referer: http://www.wireshark.org/download.html

Cookie: ln_sess=959910332560; __utma=87653150.804353448.1362024480.1362024480.1362024480.1; __utmb=87653150.1.10.1362024480; __utmc=87653150; __utmz=87653150.1362024480.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ln_c=1362024495742%2C/download.html%2C1

Connection: keep-alive

If-Modified-Since: Wed, 27 Feb 2013 05:20:11 GMT

Cache-Control: max-age=0

HTTP/1.1 304 Not Modified

Date: Thu, 28 Feb 2013 01:24:52 GMT

Server: Apache/2

Connection: Keep-Alive

Keep-Alive: timeout=5, max=86

Cache-control: public, max-age=600

Vary: Accept-Encoding

GET /image/100x41xenhancements_trial.png.pagespeed.ic.Vcf_dQU2_S.png HTTP/1.1

Host: www.wireshark.org

User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0

Accept: image/png,image/*;q=0.8,*/*;q=0.5

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Referer: http://www.wireshark.org/download.html

Cookie: ln_sess=959910332560; __utma=87653150.804353448.1362024480.1362024480.1362024480.1; __utmb=87653150.1.10.1362024480; __utmc=87653150; __utmz=87653150.1362024480.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ln_c=1362024495742%2C/download.html%2C1

Connection: keep-alive

If-Modified-Since: Mon, 25 Feb 2013 11:01:50 GMT

If-None-Match: W/&quot;0&quot;

Cache-Control: max-age=0

HTTP/1.1 304 Not Modified

Date: Thu, 28 Feb 2013 01:24:53 GMT

Server: Apache/2

Connection: Keep-Alive

Keep-Alive: timeout=5, max=84

Cache-control: public, max-age=14400

GET /js/v46status.js HTTP/1.1

Host: www.wireshark.org

User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0

Accept: text/javascript, application/javascript, */*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

X-Requested-With: XMLHttpRequest

Referer: http://www.wireshark.org/download.html

Cookie: ln_sess=959910332560; __utma=87653150.804353448.1362024480.1362024480.1362024480.1; __utmb=87653150.1.10.1362024480; __utmc=87653150; __utmz=87653150.1362024480.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ln_c=1362024495742%2C/download.html%2C1

Connection: keep-alive

If-Modified-Since: Wed, 20 Feb 2013 19:21:27 GMT

HTTP/1.1 304 Not Modified

Date: Thu, 28 Feb 2013 01:24:53 GMT

Server: Apache/2

Connection: Keep-Alive

Keep-Alive: timeout=5, max=82

Cache-control: public, max-age=600

Vary: Accept-Encoding</code></pre></div><div id="question-tags" class="tags-container tags">html http websites packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '13, 17:34</strong></p><img src="https://secure.gravatar.com/avatar/34fe3653304d405b6f7613a036d5a452?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jheckman1986&#39;s gravatar image" /><p>Jheckman1986<br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jheckman1986 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Feb '13, 01:39</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-18950" class="comments-container"></div><div id="comment-tools-18950" class="comment-tools"></div><div class="clear"></div><div id="comment-18950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18951"></span>

<div id="answer-container-18951" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18951-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hmm, how to help you without giving away the answer; otherwise, I don't think you would benefit as much from the exercise? Have you read the Wireshark <a href="http://www.wireshark.org/download/docs/user-guide-us.pdf">user guide</a>? If not the whole thing, have you at least searched through it for relevant information? I can tell you that your answer lies within.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '13, 19:53</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-18951" class="comments-container"><span id="18954"></span><div id="comment-18954" class="comment"><div id="post-18954-score" class="comment-score"></div><div class="comment-text"><p>I Have looked in it and it does not have the answer (At least one that makes sense to me) The issue is our teacher did it and we all tried to follow along but even menus he went through were different than the ones we saw on our machines... I know that makes no sense whatsoever but i can only guess he might be using the development version or something!</p><p>I'll give it a second glance tomorrow and do some more deep searching bu i am confident the guide didn't have a specific answer!</p></div><div id="comment-18954-info" class="comment-info"><span class="comment-age">(27 Feb '13, 21:17)</span> Jheckman1986</div></div><span id="18958"></span><div id="comment-18958" class="comment"><div id="post-18958-score" class="comment-score"></div><div class="comment-text"><p>OK so i just took a second glance at the guide and i figured out why it won't work, because our teacher is bad at explaining things!</p><p>Actually i was able to do it by exporting the packet itself out as a html file instead of trying to rebuild it.</p></div><div id="comment-18958-info" class="comment-info"><span class="comment-age">(27 Feb '13, 23:06)</span> Jheckman1986</div></div><span id="18962"></span><div id="comment-18962" class="comment"><div id="post-18962-score" class="comment-score">1</div><div class="comment-text"><p>by the way, thanks for encouraging me to check the manual again</p></div><div id="comment-18962-info" class="comment-info"><span class="comment-age">(28 Feb '13, 00:21)</span> Jheckman1986</div></div></div><div id="comment-tools-18951" class="comment-tools"></div><div class="clear"></div><div id="comment-18951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

