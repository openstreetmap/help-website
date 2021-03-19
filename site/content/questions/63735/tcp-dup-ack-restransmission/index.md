+++
type = "question"
title = "TCP DUP ACK &amp; Restransmission"
description = '''Hi all The wireshark capture seen in the screenshot below is between linux server and charging system, although the operation always succeed; but as you can see there are a lot of Retransmissions  [ACK] always followed by [TCP DUP ACK] then [PSH, ACK] and [TCP Retransmission] before operation succes...'''
date = "2017-10-08T02:45:00Z"
lastmod = "2017-10-08T02:58:00Z"
weight = 63735
keywords = [ "tcpdump", "duplicate", "psh", "packet", "tcp" ]
aliases = [ "/questions/63735" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [TCP DUP ACK & Restransmission](/questions/63735/tcp-dup-ack-restransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63735-score" class="post-score" title="current number of votes">0</div><span id="post-63735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>The wireshark capture seen in the screenshot below is between linux server and charging system, although the operation always succeed; but as you can see there are a lot of Retransmissions [ACK] always followed by [TCP DUP ACK] then [PSH, ACK] and [TCP Retransmission] before operation success. What could be these retransmission ?</p><p><img src="https://i.imgur.com/RnaHUxN.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-psh" rel="tag" title="see questions tagged &#39;psh&#39;">psh</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '17, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/c8881eab5dbb736c501ce6afb7836f6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="T_M_T&#39;s gravatar image" /><p><span>T_M_T</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="T_M_T has no accepted answers">0%</span></p></img></div></div><div id="comments-container-63735" class="comments-container"></div><div id="comment-tools-63735" class="comment-tools"></div><div class="clear"></div><div id="comment-63735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63736"></span>

<div id="answer-container-63736" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63736-score" class="post-score" title="current number of votes">0</div><span id="post-63736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="T_M_T has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like your capture setup captured packets twice, so there are no real problems, just duplicates. See this blog post for details and solutions:</p><p><a href="https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/">https://blog.packet-foo.com/2015/03/tcp-analysis-and-the-five-tuple/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '17, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-63736" class="comments-container"></div><div id="comment-tools-63736" class="comment-tools"></div><div class="clear"></div><div id="comment-63736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

