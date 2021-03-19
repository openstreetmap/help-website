+++
type = "question"
title = "TCP MSS in uplink and downlink speed"
description = '''Hi experts,  I want to understand MSS impact in uplink and downlink speed. While I understand lower MSS size i.e. mss &amp;lt; 1460 will directly impact heavy data transfers &amp;amp; may add certain delay as well as addition CPU cycles on resepctive nodes - I want to understand -   in a single TCP stream -...'''
date = "2017-10-01T21:45:00Z"
lastmod = "2017-10-02T23:59:00Z"
weight = 63683
keywords = [ "performance", "mss", "tcp" ]
aliases = [ "/questions/63683" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TCP MSS in uplink and downlink speed](/questions/63683/tcp-mss-in-uplink-and-downlink-speed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63683-score" class="post-score" title="current number of votes">0</div><span id="post-63683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi experts,</p><p>I want to understand MSS impact in uplink and downlink speed. While I understand lower MSS size i.e. mss &lt; 1460 will directly impact heavy data transfers &amp; may add certain delay as well as addition CPU cycles on resepctive nodes - I want to understand -</p><ol><li><p>in a single TCP stream - is there separate MSS value for uplink and downlink both ? From RFC I could find following information. I want to understand how practical these guidelines are ? Does vendor necessarily implement distinct MSS configurations for uplink &amp; downlink respectively ?</p><p>RFC 879 :</p><pre><code>    3.  The TCP Maximum Segment Size Option

       TCP provides an option that may be used at the time a connection is
       established (only) to indicate the maximum size TCP segment that can
       be accepted on that connection.  This Maximum Segment Size (MSS)
       announcement (often mistakenly called a negotiation) is sent from the
       data receiver to the data sender and says &quot;I can accept TCP segments
       up to size X&quot;. The size (X) may be larger or smaller than the
       default.  The MSS can be used completely independently in each
       direction of data flow.  The result may be quite different maximum
       sizes in the two directions</code></pre></li><li><p>If we reduce MSS size to 1360 (for ex.) what could be possible impact ?</p></li><li>How should I measure this impact for analysis ? Any possible hints on criteria ?</li><li>Is it possible to see slow uplink speed as compared to reasonable downlink speed on the same TCP stream ? What could be possible reasons ?</li></ol><p>Regards, Vijay</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-mss" rel="tag" title="see questions tagged &#39;mss&#39;">mss</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '17, 21:45</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p><span>Vijay Gharge</span><br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div></div><div id="comments-container-63683" class="comments-container"></div><div id="comment-tools-63683" class="comment-tools"></div><div class="clear"></div><div id="comment-63683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63686"></span>

<div id="answer-container-63686" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63686-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63686-score" class="post-score" title="current number of votes">1</div><span id="post-63686-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Vijay Gharge has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Both endpoints signal their MSS in the SYN or SYN/ACK packet, which is deducted from the local MTU. While not exactly a negotiation, both will use the lower of the two MSS values automatically, because it wouldn't make any sense to send more than what can either MTU allows (which would require fragmentation otherwise).</li><li>Less data transfer efficiency compared to 1460 for example, so the maximum bandwidth will be lower</li><li>My main criteria would be "MBit per second throughput", averaged over the whole data transfer. It should be higher for 1460 compared to 1360.</li><li>First of all, most connections are very asymmetric - sending a request takes a small amount of bandwidth while receiving the requested data my be using a huge amount of bandwidth. This makes it hard to compare speeds. I'd normally go and check for signs of trouble in the TCP stream: long delta times between packets, packet loss, DUP ACKs, etc.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '17, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-63686" class="comments-container"><span id="63696"></span><div id="comment-63696" class="comment"><div id="post-63696-score" class="comment-score"></div><div class="comment-text"><p>thanks for response. This helps a lot.</p></div><div id="comment-63696-info" class="comment-info"><span class="comment-age">(02 Oct '17, 23:59)</span> <span class="comment-user userinfo">Vijay Gharge</span></div></div></div><div id="comment-tools-63686" class="comment-tools"></div><div class="clear"></div><div id="comment-63686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

