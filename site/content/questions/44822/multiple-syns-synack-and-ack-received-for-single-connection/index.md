+++
type = "question"
title = "Multiple syn&#x27;s ,syn/ack and ack received for single connection?"
description = '''I have a scenario, I&#x27;m analyzing ssl (decrpyt) traffic to my webserver. I&#x27;m investigating server and end-to-end delay issues. In between this I&#x27;m stuck at following traffic pattern for which I need some advice/suggestion. The patter shows:-  client server src port 1 -&amp;gt; 80 (syn) src port 2 -&amp;gt; 8...'''
date = "2015-08-04T08:03:00Z"
lastmod = "2015-08-04T08:48:00Z"
weight = 44822
keywords = [ "ssl", "analysis", "syn", "tcp" ]
aliases = [ "/questions/44822" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Multiple syn's ,syn/ack and ack received for single connection?](/questions/44822/multiple-syns-synack-and-ack-received-for-single-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44822-score" class="post-score" title="current number of votes">0</div><span id="post-44822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a scenario, I'm analyzing ssl (decrpyt) traffic to my webserver. I'm investigating server and end-to-end delay issues. In between this I'm stuck at following traffic pattern for which I need some advice/suggestion. The patter shows:-</p><pre><code> client       server
src port 1 -&gt; 80 (syn)
src port 2 -&gt; 80 (syn)
src port 3 -&gt; 80 (syn)
src port 4 -&gt; 80 (syn)
.....

 server        client
src port 80 -&gt; 1  (syn/ack)
src port 80 -&gt; 2  (syn/ack)

client         server
src port 1 -&gt; 80  (ack)
src port 2 -&gt; 80  (ack)</code></pre><p>After, complete of handshake I see <code>"http get request"</code> from client. My issues is:-</p><ol><li>why are multiple syns send from client to server from different source port</li><li>why server choose to reply on NOT all ports mainly the syn/ack is received by first 3 ports.</li><li>Multiple acks to different ports?</li></ol><p>a sample SYN request just for analysis looks like</p><p>"694 47.583499000 192.168.1.56 192.168.1.22 TCP 66 0.000173000 50844→80 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1"</p><p>Please help me understand this behavior.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '15, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/a5e36ef8cc4416aa199a3a82dcb1deb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lazerz&#39;s gravatar image" /><p><span>lazerz</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lazerz has no accepted answers">0%</span></p></div></div><div id="comments-container-44822" class="comments-container"></div><div id="comment-tools-44822" class="comment-tools"></div><div class="clear"></div><div id="comment-44822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44824"></span>

<div id="answer-container-44824" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44824-score" class="post-score" title="current number of votes">1</div><span id="post-44824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lazerz has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>That depends on the implementation of your client.</li><li>The server may have only so many processes/threads/workers available to handle connections.</li><li>Each SYN from an IP:port is a new (TCP) connection, therefore requires it's own ACK.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '15, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-44824" class="comments-container"><span id="44825"></span><div id="comment-44825" class="comment"><div id="post-44825-score" class="comment-score"></div><div class="comment-text"><p>This being said,I'm experiencing same behavior from different machines, as for load on server in that case why i'm not seeing timeout or retransmissions etc?</p></div><div id="comment-44825-info" class="comment-info"><span class="comment-age">(04 Aug '15, 08:48)</span> <span class="comment-user userinfo">lazerz</span></div></div></div><div id="comment-tools-44824" class="comment-tools"></div><div class="clear"></div><div id="comment-44824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

