+++
type = "question"
title = "tshark could not decode HTTP response packet while wireshark can"
description = '''When using display filter -Y &quot;http&quot; in tshark, I can only see HTTP request packet is recognized. But I can see more packets are decoded as HTTP, including HTTP response. Any idea why?Output from tshark with display filter ken@ubuntu:~$ tshark -2 -r saegw_1501_sgi_tencent_10.146.76.166_52393 -Y &quot;http...'''
date = "2017-06-04T22:12:00Z"
lastmod = "2017-07-03T15:24:00Z"
weight = 61780
keywords = [ "tshark" ]
aliases = [ "/questions/61780" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [tshark could not decode HTTP response packet while wireshark can](/questions/61780/tshark-could-not-decode-http-response-packet-while-wireshark-can)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61780-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When using display filter -Y "http" in tshark, I can only see HTTP request packet is recognized. But I can see more packets are decoded as HTTP, including HTTP response. Any idea why?Output from tshark with display filter</p><pre><code>[email protected]:~$ tshark  -2 -r  saegw_1501_sgi_tencent_10.146.76.166_52393 -Y &quot;http&quot;  4 0.054650003 10.146.76.166 -&gt; 120.198.235.230 HTTP 529 GET /ugcyd.qq.com/flv/127/231/v0502uq4ahg.mp4?vkey=75DF20654722E963E5C21D63B5C1C853B033B9EB61D12A1447B279A0178D8AA5031D835EE305A7BF27EC922208D6E67D428D28C8659784399C3E3BC4A839491A274672412A3E710DCA3B7D431B9AA60F0BC13BDB24E06216&amp;sha=&amp;level=3&amp;br=200&amp;fmt=mp4&amp;sdtfrom=v3040&amp;platform=30403&amp;fohost=ugcyd.qq.com HTTP/1.1</code></pre><p>output from tshark without display filter</p><pre><code>[email protected]:~$ tshark  -2 -r  saegw_1501_sgi_tencent_10.146.76.166_52393   1 0.000000000 10.146.76.166 -&gt; 120.198.235.230 TCP 82 52393 &gt; http [SYN] Seq=0 Win=37500 Len=0 MSS=1400 WS=8 TSval=856798291 TSecr=0 SACK_PERM=1
2 0.004892857 120.198.235.230 -&gt; 10.146.76.166 TCP 70 http &gt; 52393 [SYN, ACK] Seq=0 Ack=1 Win=14600 Len=0 MSS=1460 SACK_PERM=1 WS=1024
3 0.036579926 10.146.76.166 -&gt; 120.198.235.230 TCP 64 52393 &gt; http [ACK] Seq=1 Ack=1 Win=300000 Len=0
4 0.054650003 10.146.76.166 -&gt; 120.198.235.230 HTTP 529 GET /ugcyd.qq.com/flv/127/231/v0502uq4ahg.mp4?vkey=75DF20654722E963E5C21D63B5C1C853B033B9EB61D12A1447B279A0178D8AA5031D835EE305A7BF27EC922208D6E67D428D28C8659784399C3E3BC4A839491A274672412A3E710DCA3B7D431B9AA60F0BC13BDB24E06216&amp;sha=&amp;level=3&amp;br=200&amp;fmt=mp4&amp;sdtfrom=v3040&amp;platform=30403&amp;fohost=ugcyd.qq.com HTTP/1.1
5 0.059337563 120.198.235.230 -&gt; 10.146.76.166 TCP 64 http &gt; 52393 [ACK] Seq=1 Ack=472 Win=16384 Len=0  
6 0.080402874 10.146.76.166 -&gt; 120.198.235.230 TCP 64 52393 &gt; http [RST, ACK] Seq=472 Ack=1 Win=30800 Len=0
7 0.084795120 120.198.235.230 -&gt; 10.146.76.166 TCP 389 [TCP segment of a reassembled PDU]
8 0.084819791 120.198.235.230 -&gt; 10.146.76.166 TCP 1458 [TCP segment of a reassembled PDU]
9 0.084841385 120.198.235.230 -&gt; 10.146.76.166 TCP 4258 [TCP segment of a reassembled PDU]
10 0.084864582 120.198.235.230 -&gt; 10.146.76.166 TCP 5658 [TCP segment of a reassembled PDU]
11 0.084900198 120.198.235.230 -&gt; 10.146.76.166 TCP 1458 [TCP segment of a reassembled PDU]
12 0.084927495 120.198.235.230 -&gt; 10.146.76.166 TCP 7058 [TCP segment of a reassembled PDU]
13 0.084950495 120.198.235.230 -&gt; 10.146.76.166 TCP 1458 [TCP segment of a reassembled PDU]
14 0.089734953 10.146.76.166 -&gt; 120.198.235.230 TCP 64 52393 &gt; http [RST] Seq=472 Win=0 Len=0</code></pre></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '17, 22:12</strong></p><img src="https://secure.gravatar.com/avatar/b699dbe360b63977a6678902ae0cb725?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tong1125&#39;s gravatar image" /><p>tong1125<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tong1125 has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jun '17, 02:17</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-61780" class="comments-container"></div><div id="comment-tools-61780" class="comment-tools"></div><div class="clear"></div><div id="comment-61780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="62390"></span>

<div id="answer-container-62390" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62390-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It turns out I made a silly mistake. I disable "allow subdissector to reassemble TCP streams" on Windows, but I forgot the do the same thing on Linux host.</p><p>Btw, wireshark preference file locates at ~/.config/wireshark</p><p>If you are not able to find the preference file, you can use tshark -o top.desegment_tcp_stream to disable it</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '17, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/b699dbe360b63977a6678902ae0cb725?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tong1125&#39;s gravatar image" /><p>tong1125<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tong1125 has one accepted answer">100%</span></p></div></div><div id="comments-container-62390" class="comments-container"></div><div id="comment-tools-62390" class="comment-tools"></div><div class="clear"></div><div id="comment-62390-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61782"></span>

<div id="answer-container-61782" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61782-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The display filter <code>-Y http</code> will limit output to those packets that are dissected as HTTP. As you can see from the second output, only one packet, the "GET" request has been dissected as HTTP.</p><p>All the other packets have been dissected as TCP as they either don't contain any HTTP data, or are fragments of an HTTP message and only the final packet that completes the HTTP response will be dissected as HTTP and show up with an HTTP display filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '17, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61782" class="comments-container"><span id="61783"></span><div id="comment-61783" class="comment"><div id="post-61783-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the feedback. My concern is wireshark GUI can recognize those TCP segments as HTTP, but tshark CLI could not.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/QQ20170605194319.jpg" width="640" /></p><p>How can I get the filtered output like GUI in tshark?</p></div><div id="comment-61783-info" class="comment-info"><span class="comment-age">(05 Jun '17, 04:48)</span> tong1125</div></div><span id="61785"></span><div id="comment-61785" class="comment"><div id="post-61785-score" class="comment-score"></div><div class="comment-text"><p>Try adding <code>-2</code> to the tshark command line.</p></div><div id="comment-61785-info" class="comment-info"><span class="comment-age">(05 Jun '17, 05:20)</span> grahamb ♦</div></div><span id="61797"></span><div id="comment-61797" class="comment"><div id="post-61797-score" class="comment-score"></div><div class="comment-text"><p>-2 is already included, it doesnt work.</p></div><div id="comment-61797-info" class="comment-info"><span class="comment-age">(05 Jun '17, 23:33)</span> tong1125</div></div><span id="61800"></span><div id="comment-61800" class="comment"><div id="post-61800-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DopBox etc?</p></div><div id="comment-61800-info" class="comment-info"><span class="comment-age">(06 Jun '17, 02:27)</span> grahamb ♦</div></div><span id="61811"></span><div id="comment-61811" class="comment"><div id="post-61811-score" class="comment-score"></div><div class="comment-text"><p>Here comes the pcap, thanks</p><p><a href="https://drive.google.com/file/d/0B3Lqaled8eVCZlg1cXNYOU1FeGc/view?usp=sharing">https://drive.google.com/file/d/0B3Lqaled8eVCZlg1cXNYOU1FeGc/view?usp=sharing</a></p></div><div id="comment-61811-info" class="comment-info"><span class="comment-age">(06 Jun '17, 19:32)</span> tong1125</div></div><span id="61822"></span><div id="comment-61822" class="comment not_top_scorer"><div id="post-61822-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark and tshark are you using?</p></div><div id="comment-61822-info" class="comment-info"><span class="comment-age">(07 Jun '17, 04:04)</span> grahamb ♦</div></div><span id="61888"></span><div id="comment-61888" class="comment not_top_scorer"><div id="post-61888-score" class="comment-score"></div><div class="comment-text"><p>Tshark version is <img src="https://osqa-ask.wireshark.org/upfiles/QNHY9CL6.png" alt="alt text" /></p><p>And wireshark GUI version is <img src="https://osqa-ask.wireshark.org/upfiles/GQAU7L8MI@EH3DSC7Q_7DHA.png" alt="alt text" /></p></div><div id="comment-61888-info" class="comment-info"><span class="comment-age">(09 Jun '17, 01:19)</span> tong1125</div></div><span id="61903"></span><div id="comment-61903" class="comment not_top_scorer"><div id="post-61903-score" class="comment-score"></div><div class="comment-text"><p>Upgrade the wireshark to 2.2.6 on Windows, it is still working.maybe only Linux has problem?</p></div><div id="comment-61903-info" class="comment-info"><span class="comment-age">(09 Jun '17, 05:16)</span> tong1125</div></div><span id="61905"></span><div id="comment-61905" class="comment not_top_scorer"><div id="post-61905-score" class="comment-score"></div><div class="comment-text"><p>So tshark on Windows works for you?</p></div><div id="comment-61905-info" class="comment-info"><span class="comment-age">(09 Jun '17, 06:12)</span> grahamb ♦</div></div></div><div id="comment-tools-61782" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-61782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62484"></span>

<div id="answer-container-62484" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62484-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you possibly forgetting to input the profile in tshark? If your using a specific profile in the GUI where you have the TCP settings to allow you to see HTTP, make sure to specify that same profile in tshark, else it will use the default like below.</p><p>tshark -r test.pcap -Y http.response -Tfields -e frame.number -e http.response.code -e http.time -C tcp-tshoot</p><p>C:\ tshark -r 90_streams.pcap -Y http.response -Tfields -e frame.number -e http.response.code -e http.time -C tcp-tshoot 5 200 0.025068000 49 200 0.022251000 55 200 0.194137000 75 200 0.243763000 103 200 0.250902000 132 200 0.029903000 142 200 0.039818000</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '17, 15:24</strong></p><img src="https://secure.gravatar.com/avatar/8234281d80d46cc33dc8ba9dbdd33aa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sneak2k2&#39;s gravatar image" /><p>Sneak2k2<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sneak2k2 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-62484" class="comments-container"></div><div id="comment-tools-62484" class="comment-tools"></div><div class="clear"></div><div id="comment-62484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

