+++
type = "question"
title = "Unreadable data in &quot;Follow TCP stream&quot;"
description = '''Hi all, I am new to using wireshark. I captured network activity while loading a simple text based webpage and selected the option &quot;Follow TCP data&quot;. I can see the HTTP request and response in plain text, but the data part is completely scrambled. It is simple http request so I expected the data par...'''
date = "2014-12-15T11:27:00Z"
lastmod = "2014-12-15T12:07:00Z"
weight = 38582
keywords = [ "data", "tcp" ]
aliases = [ "/questions/38582" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Unreadable data in "Follow TCP stream"](/questions/38582/unreadable-data-in-follow-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38582-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I am new to using wireshark. I captured network activity while loading a simple text based webpage and selected the option "Follow TCP data". I can see the HTTP request and response in plain text, but the data part is completely scrambled. It is simple http request so I expected the data part to be readable as well. Where am I going wrong? Please let me know.</p></div><div id="question-tags" class="tags-container tags">data tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '14, 11:27</strong></p><img src="https://secure.gravatar.com/avatar/185daea1ec04fbb8468a53a66e6a8908?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nckr&#39;s gravatar image" /><p>nckr<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nckr has no accepted answers">0%</span></p></div></div><div id="comments-container-38582" class="comments-container"></div><div id="comment-tools-38582" class="comment-tools"></div><div class="clear"></div><div id="comment-38582-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38584"></span>

<div id="answer-container-38584" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38584-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The HTTP response is most certainly using compression, like the example below:</p><p>As "Follow TCP Stream" does not support HTTP decompression, you won't see the HTTP response in cleartext. We would need something like "Follow HTTP Stream", which does not yet exist.</p><p>You can look at the response in cleartext within the packet bytes pane and the packet details pane, as the HTTP dissector <strong>does</strong> decompression of the HTTP data.</p><pre><code>GET / HTTP/1.1
Host: www.apple.com
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
Accept-Encoding: gzip, deflate, sdch

HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Type: text/html; charset=UTF-8
Vary: Accept-Encoding
Content-Encoding: gzip   &lt;======================== HERE !!!!
Content-Length: 2584
Cache-Control: max-age=471
Expires: Mon, 15 Dec 2014 20:10:33 GMT
Date: Mon, 15 Dec 2014 20:02:42 GMT
Connection: keep-alive
Server: Apache

.............r......8.L.ND.r.\.J..9.6m.{,gz...H.B....J.d2s......F......H..e9....`........w..O.&gt;\......3..r..\...1.q.-....YO.4..z.*.E.......a....8 .I.........OG.E/cQ........sp.9.d.P........L....F.$....&#39;..I..X....wR...7y..D.s.(.2
..O.l..9.Yh&#39;].sn8....`.~.....O%..._..&#39;...
j.D...7g......7g?t.L_y&quot;..7D11..Y
.g..43.J.W......s.b.E4.R!&#39;T.n.......n..b..b.....[..9p.....FV5..M...J.L..0.9.K.c..E..
......FWt.T.].t.v.s&amp;.Df2c.....o...o....{.2.a.v...J..N.....wW...O._.}i.mC....C.lz.k.c...e....i.....o..C...l..a[..x..X7.F.:.h..].n.....S....qyL......-.L....r&lt;..
2..&gt;...k..=.c...c..+/.=......)Z..).GG?Ni..r.v.8M...yz...hV.e..r=.e,..u!......&amp;7U..ioRra.&amp;..8Y&gt;M&amp;.?......0p..h.?H3........c..G:..+X.YG....].n..D&amp;K..............r:&#39;&lt;...+(....J.{...R..(x</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '14, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Dec '14, 12:11</p></div></div><div id="comments-container-38584" class="comments-container"><span id="38593"></span><div id="comment-38593" class="comment"><div id="post-38593-score" class="comment-score"></div><div class="comment-text"><p>If I select a single TCP packet and look at its TCP segment data (which in my case has 1452 bytes), in the packet details pane, it has 4 columns. Is the 4th column ASCII representation of the data? If so is it clear text or still some compressed form for a simple http request? I expected it to be clear text since it is not https, but it looks scrambled as well.</p></div><div id="comment-38593-info" class="comment-info"><span class="comment-age">(16 Dec '14, 01:02)</span> nckr</div></div><span id="38594"></span><div id="comment-38594" class="comment"><div id="post-38594-score" class="comment-score"></div><div class="comment-text"><blockquote><p>If I select a single TCP packet and look at its TCP segment data</p></blockquote><p>please select the frame with the HTTP response in the info column, as that's the frame where the HTTP dissector has seen all TCP segments required to re-assemble the whole HTTP response and where it is able to do decompression.</p><p>If you select the <strong>TCP segment data</strong> in that frame, you will <strong>still only see compressed data</strong>!!</p><p><img src="https://osqa-ask.wireshark.org/upfiles/tcp_stream_compressed_data_tR04Vlz.png" alt="alt text" /></p><p>However, if you select the <strong>HTTP data</strong> (or the <strong>reassembled TCP segments</strong>), you should see the <strong>HTTP response in cleartext</strong>. See also the tabs at the bottom of the window.</p><p>As the HTTP response can spread over several TCP segments (as in my example), that's how the HTTP dissector (in combination with the TCP dissector) shows the combined data of the response.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/tcp_stream_uncompressed_data.png" alt="alt text" /></p><p>Regards<br />
Kurt</p></div><div id="comment-38594-info" class="comment-info"><span class="comment-age">(16 Dec '14, 02:32)</span> Kurt Knochner ♦</div></div><span id="38599"></span><div id="comment-38599" class="comment"><div id="post-38599-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot for your response! I am now able to see the uncompressed data in clear text!</p></div><div id="comment-38599-info" class="comment-info"><span class="comment-age">(16 Dec '14, 07:56)</span> nckr</div></div></div><div id="comment-tools-38584" class="comment-tools"></div><div class="clear"></div><div id="comment-38584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

