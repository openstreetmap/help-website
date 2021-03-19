+++
type = "question"
title = "What does RST/ACK convey in this capture excerpt?"
description = '''973 24.130685 10.160.119.23 172.16.1.242 TCP 54 **50078 → 443 [RST, ACK] Seq=1180** Ack=1677 Win=0 Len=0 974 24.134424 172.16.1.242 10.160.119.23 TCP 60 **[TCP Dup ACK 967#1] 443 → 50078 [ACK]** Seq=1677 Ack=1179 Win=131328 Len=0 975 24.134557 10.160.119.23 172.16.1.242 TCP 54 50078 → 443 [RST] Seq=...'''
date = "2017-01-06T03:14:00Z"
lastmod = "2017-01-06T09:41:00Z"
weight = 58558
keywords = [ "rst", "rst+ack" ]
aliases = [ "/questions/58558" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What does RST/ACK convey in this capture excerpt?](/questions/58558/what-does-rstack-convey-in-this-capture-excerpt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58558-score" class="post-score" title="current number of votes">0</div><span id="post-58558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>973 24.130685   10.160.119.23   172.16.1.242    TCP 54  **50078 → 443 [RST, ACK] Seq=1180** Ack=1677 Win=0 Len=0
974 24.134424   172.16.1.242    10.160.119.23   TCP 60  **[TCP Dup ACK 967#1] 443 → 50078 [ACK]** Seq=1677 Ack=1179 Win=131328 Len=0
975 24.134557   10.160.119.23   172.16.1.242    TCP 54  50078 → 443 [RST] Seq=1179 Win=0 Len=0
976 24.136172   172.16.1.242    10.160.119.23   TCP 60  443 → 50078 [ACK] Seq=1677 Ack=1180 Win=131328 Len=0
977 24.136275   10.160.119.23   172.16.1.242    TCP 54  50078 → 443 [RST] Seq=1180 Win=0 Len=0
978 24.835189   10.160.119.2    224.0.0.2   HSRP    62  Hello (state Standby)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-rst+ack" rel="tag" title="see questions tagged &#39;rst+ack&#39;">rst+ack</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '17, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/6b0bd7f296155e33e2ba8e076707869e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="implementation&#39;s gravatar image" /><p><span>implementation</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="implementation has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jan '17, 03:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-58558" class="comments-container"></div><div id="comment-tools-58558" class="comment-tools"></div><div class="clear"></div><div id="comment-58558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58564"></span>

<div id="answer-container-58564" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58564-score" class="post-score" title="current number of votes">0</div><span id="post-58564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>We have a client (10.160.119.23) and a server (172.16.1.242). The client made an HTTPS request, which is not shown in the trace file.</p><p>The client acknowledges the arrival of data [Ack=1179, while the ACK flag is set] and want's to terminate the connection [RST].</p><p>Data is still in transit from the server, while the RST is on it's way (packets 974 and 976). As the client has already closed it's socket the two data segments trigger extra Resets.</p><p>A graceful TCP shutdown would require 4 packets:</p><pre><code>          C -&gt; S   FIN
          S -&gt; C   ACK, thank you for your FIN
optional  S -&gt; C   by the way, I still got some data to you
optional  S -&gt; C   blah, blah, blah
          S -&gt; C   FIN
          C -&gt; S   Thank you, good bye</code></pre><p>Terminating the connection makes sure, that the server will not send data after the client tells about the desire to terminate the connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '17, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-58564" class="comments-container"></div><div id="comment-tools-58564" class="comment-tools"></div><div class="clear"></div><div id="comment-58564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

