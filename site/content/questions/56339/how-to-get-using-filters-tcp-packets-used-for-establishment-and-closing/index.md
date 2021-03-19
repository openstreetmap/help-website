+++
type = "question"
title = "How to get (using filters) TCP packets used for establishment and closing"
description = '''Hi, I am aware of three-way handshake protocol in TCP and how SYN, SYN_ACK and FIN helps identify the stages of establishment and teardown. Is there any filter (in wireshark) I can use to get these (ones for establishment) and (ones for teardown) seperately from data packets?'''
date = "2016-10-13T09:58:00Z"
lastmod = "2016-10-13T10:34:00Z"
weight = 56339
keywords = [ "tcp" ]
aliases = [ "/questions/56339" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get (using filters) TCP packets used for establishment and closing](/questions/56339/how-to-get-using-filters-tcp-packets-used-for-establishment-and-closing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56339-score" class="post-score" title="current number of votes">0</div><span id="post-56339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am aware of three-way handshake protocol in TCP and how SYN, SYN_ACK and FIN helps identify the stages of establishment and teardown. Is there any filter (in wireshark) I can use to get these (ones for establishment) and (ones for teardown) seperately from data packets?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '16, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/ca8b8c7a2ba67e8d76a112c7f1c15369?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="learner_tcp&#39;s gravatar image" /><p><span>learner_tcp</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="learner_tcp has no accepted answers">0%</span></p></div></div><div id="comments-container-56339" class="comments-container"></div><div id="comment-tools-56339" class="comment-tools"></div><div class="clear"></div><div id="comment-56339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56340"></span>

<div id="answer-container-56340" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56340-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56340-score" class="post-score" title="current number of votes">0</div><span id="post-56340-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not easily as filters only determine if a particular packet should be displayed or not depending on fields (real or synthesized) in that packet. This makes it difficult to display the final ACK for the connection establishment and teardown as they don't look different from any other ACK. If you have relative sequence numbers on the final ACK for establishment can be located as it will have a sequence number and ack value of 1. This gives a filter of:</p><pre><code>(tcp.flags.syn == 1) || (tcp.flags.ack == 1 &amp;&amp; (tcp.seq == 1) &amp;&amp; (tcp.ack == 1)) || (tcp.flags.fin == 1)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '16, 10:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Oct '16, 10:34</strong> </span></p></div></div><div id="comments-container-56340" class="comments-container"></div><div id="comment-tools-56340" class="comment-tools"></div><div class="clear"></div><div id="comment-56340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

