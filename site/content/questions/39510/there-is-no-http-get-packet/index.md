+++
type = "question"
title = "there is no Http get packet"
description = '''1485 19:02:50.954885 100.69.39.242 54.192.231.117 TCP 1083132446 76 56944 &amp;gt; http [SYN] Seq=1083132446 Win=42340 Len=0 MSS=1460 SACK_PERM=1 TSval=657381 TSecr=0 WS=32 0.004519  1487 19:02:51.036591 54.192.231.117 100.69.39.242 TCP 440232374 1083132447 76 http &amp;gt; 56944 [SYN, ACK] Seq=440232374 Ac...'''
date = "2015-01-30T12:10:00Z"
lastmod = "2015-01-31T12:09:00Z"
weight = 39510
keywords = [ "http", "lost", "get" ]
aliases = [ "/questions/39510" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [there is no Http get packet](/questions/39510/there-is-no-http-get-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39510-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>1485    19:02:50.954885 100.69.39.242   54.192.231.117  TCP 1083132446          76  56944 &gt; http [SYN] Seq=1083132446 Win=42340 Len=0 MSS=1460 SACK_PERM=1 TSval=657381 TSecr=0 WS=32   0.004519    
1487    19:02:51.036591 54.192.231.117  100.69.39.242   TCP 440232374       1083132447  76  http &gt; 56944 [SYN, ACK] Seq=440232374 Ack=1083132447 Win=14480 Len=0 MSS=1400 SACK_PERM=1 TSval=3642018558 TSecr=657381 WS=128  0.000247    0.081706000
1488    19:02:51.036879 100.69.39.242   54.192.231.117  TCP 1083132447      440232375   68  56944 &gt; http [ACK] Seq=1083132447 Ack=440232375 Win=42368 Len=0 TSval=657389 TSecr=3642018558   0.000288    0.000288000
1500    19:03:23.028406 54.192.231.117  100.69.39.242   TCP 440232375       1083132447  68  http &gt; 56944 [FIN, ACK] Seq=440232375 Ack=1083132447 Win=14592 Len=0 TSval=3642021560 TSecr=657389  19.899114   
1501    19:03:23.028629 54.192.231.117  100.69.39.242   TCP 440232375       1083132447  68  [TCP Out-Of-Order] http &gt; 56944 [FIN, ACK] Seq=440232375 Ack=1083132447 Win=14592 Len=0 TSval=3642021582 TSecr=657389   0.000223    
1502    19:03:23.028785 54.192.231.117  100.69.39.242   TCP 440232375       1083132447  68  [TCP Out-Of-Order] http &gt; 56944 [FIN, ACK] Seq=440232375 Ack=1083132447 Win=14592 Len=0 TSval=3642021626 TSecr=657389   0.000156    
1503    19:03:23.028869 54.192.231.117  100.69.39.242   TCP 440232375       1083132447  68  [TCP Out-Of-Order] http &gt; 56944 [FIN, ACK] Seq=440232375 Ack=1083132447 Win=14592 Len=0 TSval=3642021714 TSecr=657389   0.000084    
1504    19:03:23.037363 100.69.39.242   54.192.231.117  TCP 1083132728      440232376   68  [TCP Previous segment not captured] 56944 &gt; http [FIN, ACK] Seq=1083132728 Ack=440232376 Win=42368 Len=0 TSval=660589 TSecr=3642021714  0.008494    0.008957000
1506    19:03:23.091501 54.192.231.117  100.69.39.242   TCP 440232376           56  http &gt; 56944 [RST] Seq=440232376 Win=0 Len=0    0.040445</code></pre><p>There is no http get packet. but We can see here when server is sending [FIN,ACK], it has Seq=440232374, Ack =1083132446. (packet# 1500)</p><p>However when device sends <a href="Packet%20#1506">FIN,ACK</a>, it has Seq=1083132728.</p><p>I think device has sent the data/GET request, but it is not caputured.</p></div><div id="question-tags" class="tags-container tags">http lost get</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '15, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/d7eac629e36e4b13fbdf0d135ff84edb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nikol482&#39;s gravatar image" /><p>nikol482<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nikol482 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jan '15, 12:57</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-39510" class="comments-container"></div><div id="comment-tools-39510" class="comment-tools"></div><div class="clear"></div><div id="comment-39510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39524"></span>

<div id="answer-container-39524" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39524-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks to me like the server closing the session right after the three way handshake, without allowing the client to even sent a GET command. I wrote a blog post about behavior like this, see</p><p><a href="https://blog.packet-foo.com/2014/01/tcp-server-slamming-the-door/">https://blog.packet-foo.com/2014/01/tcp-server-slamming-the-door/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '15, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39524" class="comments-container"><span id="39707"></span><div id="comment-39707" class="comment"><div id="post-39707-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your information, but I wonder How Can I explain sequence number? because there is no http get packet, but sequence number increase 1083132447(packet 1488) to 1083132728(1504)</p></div><div id="comment-39707-info" class="comment-info"><span class="comment-age">(09 Feb '15, 01:01)</span> nikol482</div></div></div><div id="comment-tools-39524" class="comment-tools"></div><div class="clear"></div><div id="comment-39524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

