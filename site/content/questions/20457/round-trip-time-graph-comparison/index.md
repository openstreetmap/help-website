+++
type = "question"
title = "Round trip time graph comparison"
description = '''Hi  I&#x27;m trying to compare these round trip time graphs. Can anyone explain what is happening here with the two graphs please? https://dl.dropboxusercontent.com/u/39248217/RTT%20CBWFQ.jpg https://dl.dropboxusercontent.com/u/39248217/RTT%20FIFO.jpg Thanks very much Dan'''
date = "2013-04-16T02:31:00Z"
lastmod = "2013-04-17T12:39:00Z"
weight = 20457
keywords = [ "rtt", "statistics", "qos", "tcp", "graphs" ]
aliases = [ "/questions/20457" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Round trip time graph comparison](/questions/20457/round-trip-time-graph-comparison)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20457-score" class="post-score" title="current number of votes">0</div><span id="post-20457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I'm trying to compare these round trip time graphs. Can anyone explain what is happening here with the two graphs please?</p><p><a href="https://dl.dropboxusercontent.com/u/39248217/RTT%20CBWFQ.jpg">https://dl.dropboxusercontent.com/u/39248217/RTT%20CBWFQ.jpg</a> <a href="https://dl.dropboxusercontent.com/u/39248217/RTT%20FIFO.jpg">https://dl.dropboxusercontent.com/u/39248217/RTT%20FIFO.jpg</a></p><p>Thanks very much Dan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtt" rel="tag" title="see questions tagged &#39;rtt&#39;">rtt</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-qos" rel="tag" title="see questions tagged &#39;qos&#39;">qos</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-graphs" rel="tag" title="see questions tagged &#39;graphs&#39;">graphs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '13, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/703db8b1016496f63390abe9cd3275a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dscott1709&#39;s gravatar image" /><p><span>dscott1709</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dscott1709 has no accepted answers">0%</span></p></div></div><div id="comments-container-20457" class="comments-container"></div><div id="comment-tools-20457" class="comment-tools"></div><div class="clear"></div><div id="comment-20457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20463"></span>

<div id="answer-container-20463" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20463-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20463-score" class="post-score" title="current number of votes">0</div><span id="post-20463-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As I already mentioned in your other question</p><pre><code>http://ask.wireshark.org/questions/20456/fifo-vs-cbwfq-throughput-graph-comparison</code></pre><p>it is hard to interpret a graph without any information about the QoS policy used and some information about the rest of the traffic that passed the monitored device (and line).</p><p>So, please add more details about your test environment and your test parameters.</p><p>Regards Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '13, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span></p></div></div><div id="comments-container-20463" class="comments-container"><span id="20507"></span><div id="comment-20507" class="comment"><div id="post-20507-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt</p><p>I'm passing an identical traffic mix of RTP video stream, FTP and ICMP over a 2MB serial between two Cisco routers to compare how each QoS scheme (FIFO and CBWFQ) peforms best and what happens. I've given CBWFQ precedence levels of: RTP 7 FTP 4 ICMP 1</p><p>Does that help to give you more insight into why these graphs are different?</p><p>Cheers Dan</p></div><div id="comment-20507-info" class="comment-info"><span class="comment-age">(17 Apr '13, 03:07)</span> <span class="comment-user userinfo">dscott1709</span></div></div><span id="20532"></span><div id="comment-20532" class="comment"><div id="post-20532-score" class="comment-score"></div><div class="comment-text"><p>see my comment here: <a href="http://ask.wireshark.org/questions/20456/fifo-vs-cbwfq-throughput-graph-comparison">http://ask.wireshark.org/questions/20456/fifo-vs-cbwfq-throughput-graph-comparison</a></p></div><div id="comment-20532-info" class="comment-info"><span class="comment-age">(17 Apr '13, 12:39)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20463" class="comment-tools"></div><div class="clear"></div><div id="comment-20463-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

