+++
type = "question"
title = "TCP Stream Graph; how to interprete Throughput graph Y-axis unit"
description = '''Does anybody know what&#x27;s the exact unit of the Y-axis in the Throughput Graph ? It shows [B/s] but is it bits or Bytes per second? Thx.'''
date = "2014-05-15T05:40:00Z"
lastmod = "2014-05-22T02:01:00Z"
weight = 32820
keywords = [ "graph_troughput" ]
aliases = [ "/questions/32820" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Stream Graph; how to interprete Throughput graph Y-axis unit](/questions/32820/tcp-stream-graph-how-to-interprete-throughput-graph-y-axis-unit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32820-score" class="post-score" title="current number of votes">0</div><span id="post-32820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anybody know what's the exact unit of the Y-axis in the Throughput Graph ? It shows [B/s] but is it bits or Bytes per second? Thx.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graph_troughput" rel="tag" title="see questions tagged &#39;graph_troughput&#39;">graph_troughput</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '14, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/4fc43c83d14e6cb53bf36dd8013dbcf1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="profke&#39;s gravatar image" /><p><span>profke</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="profke has no accepted answers">0%</span></p></div></div><div id="comments-container-32820" class="comments-container"></div><div id="comment-tools-32820" class="comment-tools"></div><div class="clear"></div><div id="comment-32820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32821"></span>

<div id="answer-container-32821" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32821-score" class="post-score" title="current number of votes">0</div><span id="post-32821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think by convention, capital B refers to bytes and lowercase b refers to bits.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '14, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/32272e9efae0156b7a71e9b634428d14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smp&#39;s gravatar image" /><p><span>smp</span><br />
<span class="score" title="39 reputation points">39</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 May '14, 06:01</strong> </span></p></div></div><div id="comments-container-32821" class="comments-container"><span id="32823"></span><div id="comment-32823" class="comment"><div id="post-32823-score" class="comment-score"></div><div class="comment-text"><p>Well, that should be the case, but I want to be sure.</p></div><div id="comment-32823-info" class="comment-info"><span class="comment-age">(15 May '14, 06:04)</span> <span class="comment-user userinfo">profke</span></div></div><span id="32824"></span><div id="comment-32824" class="comment"><div id="post-32824-score" class="comment-score"></div><div class="comment-text"><p>If you want to be sure, than plot an IO graph, set it to Bytes per second, and then to bits per second, and see which corresponds to the Throughput graph. Note that the Throughput graph shows one stream in one direction, based on the selected packet, whereas the IO graph shows all packet in the trace file, so you will have to apply a display filter so that the IO graph is graphing the same packets as the Throughput graph.</p></div><div id="comment-32824-info" class="comment-info"><span class="comment-age">(15 May '14, 06:16)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="32846"></span><div id="comment-32846" class="comment"><div id="post-32846-score" class="comment-score"></div><div class="comment-text"><p>Well, I have done this before but I don't find a relation between these two type of graphs; in the IO Graph I have an example that shows a peak up to 2Mbyte/s , while on the TCP Troughput graph it peaks to 54MB/s; for whatever the "B" stands for; it doesn't match with the 2MB/s (=16Mb/s) on the IO graph. Hence my question how to interprete the TCP Troughput graph. I think both graphs plot the data on a different way. I've some screenshots to show, but I don't know how to get these into this box.</p></div><div id="comment-32846-info" class="comment-info"><span class="comment-age">(16 May '14, 00:37)</span> <span class="comment-user userinfo">profke</span></div></div></div><div id="comment-tools-32821" class="comment-tools"></div><div class="clear"></div><div id="comment-32821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32865"></span>

<div id="answer-container-32865" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32865-score" class="post-score" title="current number of votes">0</div><span id="post-32865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Follow the steps in <a href="http://ask.wireshark.org/questions/14605/differences-between-io-graph-and-tcpstream-throughput-graph">this answer</a> so that your I/O Graph and TCP Stream Throughput Graph are graphing the same things. Also change the tick interval on the I/O graph to match the Throughput graph as closely as possible. The I/O graph averages the throughput over the tick interval. The Throughput graph uses a 20-segment moving average. Because the time periods are calculated differently, you will probably never get exactly the same results from both graphs, but they should be close.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '14, 16:27</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-32865" class="comments-container"><span id="32975"></span><div id="comment-32975" class="comment"><div id="post-32975-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jim, I will check this out.</p></div><div id="comment-32975-info" class="comment-info"><span class="comment-age">(22 May '14, 02:01)</span> <span class="comment-user userinfo">profke</span></div></div></div><div id="comment-tools-32865" class="comment-tools"></div><div class="clear"></div><div id="comment-32865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

