+++
type = "question"
title = "Which TCP Packet does reset the connection ?"
description = '''I´ve got the following TCP-package: 009:38:03.287348 ftp.rus.universityA.com.ftp-data &amp;gt; IPLab.IT.universityB.com.49638: . 62265:63713(1448) ack 1 win 5840 &amp;lt;nop,nop,timestamp 126527920=&quot;&quot; 492903732=&quot;&quot;&amp;gt; (DF) [tos 0x8] (ttl 45, id 43158, len 1500) and I have to figure out, why the next package...'''
date = "2017-01-01T08:35:00Z"
lastmod = "2017-01-02T05:52:00Z"
weight = 58452
keywords = [ "university", "flags", "learning", "tcp", "tcpwindowsize" ]
aliases = [ "/questions/58452" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Which TCP Packet does reset the connection ?](/questions/58452/which-tcp-packet-does-reset-the-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58452-score" class="post-score" title="current number of votes">0</div><span id="post-58452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I´ve got the following TCP-package:</p><pre><code>009:38:03.287348 ftp.rus.universityA.com.ftp-data &gt; IPLab.IT.universityB.com.49638: . 62265:63713(1448) ack 1 win 5840 &lt;nop,nop,timestamp 126527920=&quot;&quot; 492903732=&quot;&quot;&gt; (DF) [tos 0x8] (ttl 45, id 43158, len 1500)</code></pre><p>and I have to figure out, why the next package is aborting/reseting the connection:</p><pre><code>09:38:03.287459 IPLab.IT.universityB.com.49638 &gt; ftp.rus.universityA.com.ftp-data: R. [tcp sum ok] ack 63713 win 63712 &lt;nop,nop,timestamp 492903735=&quot;&quot; 126527917,nop,nop,sack=&quot;&quot; sack=&quot;&quot; 1=&quot;&quot; {65161:65537}=&quot;&quot;&gt; (DF) [tos 0x8] (ttl 64, id 424, len 64)</code></pre><p>This is part of an old exam I am trying to solve. There were other packages but I think I already proved them wrong (ACK-number wasn´t right, wrong source port etc.)<br />
What I dont understand is, all of them carry the "SEQ-Number"(63713) of the first package -1 as "Windows-Size" (63712). The original Windows-Size was 5840.</p><p>Also at first I was looking for a "RST"-Flag but they all got "ACK". So I am kind of confused, why the connection would be reseted.</p><p>Is the connection being reseted because the "Don´t fragment(DF)"-Flag is set and the Windows-Size way too large ?</p><p>Happy New Year<br />
peacemaker</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-university" rel="tag" title="see questions tagged &#39;university&#39;">university</span> <span class="post-tag tag-link-flags" rel="tag" title="see questions tagged &#39;flags&#39;">flags</span> <span class="post-tag tag-link-learning" rel="tag" title="see questions tagged &#39;learning&#39;">learning</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-tcpwindowsize" rel="tag" title="see questions tagged &#39;tcpwindowsize&#39;">tcpwindowsize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jan '17, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/ec66054f9698c5582b82d1718f1da905?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peacemaker&#39;s gravatar image" /><p><span>peacemaker</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peacemaker has one accepted answer">100%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jan '17, 12:54</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-58452" class="comments-container"></div><div id="comment-tools-58452" class="comment-tools"></div><div class="clear"></div><div id="comment-58452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58462"></span>

<div id="answer-container-58462" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58462-score" class="post-score" title="current number of votes">0</div><span id="post-58462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="peacemaker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My bad guys, I just found more information on the back page:</p><p>4508 0040 01a8 4000 4006 c696 c1af 2cfa<br />
8145 0283 c1e6 0014 15fd 1cae 04fc fad7<br />
b014 f8e0 e899 0000 0101 080a 1d61 1d37<br />
078a a9ad 0101 050a 04fd 007f 04fd 01f7<br />
is also given.</p><p>Version = IPv4<br />
IHL = 5 , so the Header is 160 bit (20byte) Protocol = 06, TCP<br />
Because I want to know the TCP-Flags, I ignore the first 20bytes(IP-Header). So the TCP-Package starts at "c1e6", wich is my source-port 49638. The TCP-Flags are the last 6 bits at "b014". 014 in Binary is 0000 0001 0100, so the last 6 bits are 010100.<br />
URG = 0<br />
ACK = 1<br />
PSH = 0<br />
RST = 1<br />
SYN = 0<br />
FIN = 0<br />
</p><p>Finaly I understand why the Connection is reseted [RST] :)</p><p>greetings<br />
peacemaker</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '17, 05:52</strong></p><img src="https://secure.gravatar.com/avatar/ec66054f9698c5582b82d1718f1da905?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peacemaker&#39;s gravatar image" /><p><span>peacemaker</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peacemaker has one accepted answer">100%</span> </br></br></p></div></div><div id="comments-container-58462" class="comments-container"></div><div id="comment-tools-58462" class="comment-tools"></div><div class="clear"></div><div id="comment-58462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

