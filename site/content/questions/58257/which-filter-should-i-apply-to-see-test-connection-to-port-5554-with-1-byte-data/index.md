+++
type = "question"
title = "Which filter should i apply to see &#x27;test connection to port 5554 with 1 byte data&#x27; ?"
description = '''Which filter should i apply to see &#x27;test connection to port 5554 with 1 byte data&#x27; ? I have applied filter tcp.dstport==5554 &amp;amp;&amp;amp; tcp.flags.push==1 &amp;amp;&amp;amp; tcp.len == 1OR tcp.dstport==5554 &amp;amp;&amp;amp; tcp.analysis.push_bytes_sent &amp;amp;&amp;amp; tcp.len == 1 . Which filter is right ? Any more sug...'''
date = "2016-12-20T08:53:00Z"
lastmod = "2016-12-20T16:38:00Z"
weight = 58257
keywords = [ "tcp" ]
aliases = [ "/questions/58257" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Which filter should i apply to see 'test connection to port 5554 with 1 byte data' ?](/questions/58257/which-filter-should-i-apply-to-see-test-connection-to-port-5554-with-1-byte-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58257-score" class="post-score" title="current number of votes">0</div><span id="post-58257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Which filter should i apply to see 'test connection to port 5554 with 1 byte data' ? I have applied filter tcp.dstport==5554 &amp;&amp; tcp.flags.push==1 &amp;&amp; tcp.len == 1OR tcp.dstport==5554 &amp;&amp; tcp.analysis.push_bytes_sent &amp;&amp; tcp.len == 1 . Which filter is right ? Any more suggestions ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '16, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/d3738ae6c68f633f63676b889de0a26f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hacksorpratik&#39;s gravatar image" /><p><span>hacksorpratik</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hacksorpratik has no accepted answers">0%</span></p></div></div><div id="comments-container-58257" class="comments-container"></div><div id="comment-tools-58257" class="comment-tools"></div><div class="clear"></div><div id="comment-58257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58263"></span>

<div id="answer-container-58263" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58263-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58263-score" class="post-score" title="current number of votes">1</div><span id="post-58263-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you know the data packet will be sent to port 5554 and you know it will have exactly one byte in the TCP data segment and you know the push bit will be set, then "tcp.dstport==5554 &amp;&amp; tcp.flags.push==1 &amp;&amp; tcp.len==1" should work.</p><p>But before sending the data byte, the connection will need to be established, so why not start by just filtering on "tcp.port==5554" so you can see all the packets on the test connection? You can then add to your filter to narrow it down from there. If the testing system simply makes a connection, sends one data byte, and terminates the connection, then there won't be many packets and it will be easy to pick out the one-byte data packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '16, 16:38</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-58263" class="comments-container"></div><div id="comment-tools-58263" class="comment-tools"></div><div class="clear"></div><div id="comment-58263-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

