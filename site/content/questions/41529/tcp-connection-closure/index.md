+++
type = "question"
title = "TCP connection closure"
description = '''Hi, I have two questions 1) In case of active close, after FIN_WAIT state how much time will it take to close the connection? I understood /proc/sys/net/ipv4/tcp_fin_timeout will decide (default 60 sec) in case of ubuntu and in case of BSD socket implementation 2 * MSL will take... AM I RIGHT ??? Ki...'''
date = "2015-04-17T02:39:00Z"
lastmod = "2015-04-19T09:39:00Z"
weight = 41529
keywords = [ "closure", "connection", "tcp" ]
aliases = [ "/questions/41529" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP connection closure](/questions/41529/tcp-connection-closure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41529-score" class="post-score" title="current number of votes">0</div><span id="post-41529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have two questions</p><p>1) In case of active close, after FIN_WAIT state how much time will it take to close the connection?</p><p>I understood /proc/sys/net/ipv4/tcp_fin_timeout will decide (default 60 sec) in case of ubuntu and in case of BSD socket implementation 2 * MSL will take... AM I RIGHT ??? Kindly Confirm</p><p>2) In case of passive close, similarly after receiving last ack from other terminal how much time will it take to close the connection?</p><p>Can u share some more details on this???</p><p>Regards</p><p>hi Jasper Bongertz,</p><p>1) In Ubuntu 12.XX ver we observed FIN_WAIT time as 60sec and other one is less than one sec is taking... even after modifying /proc/sys/net/ipv4/tcp_fin_timeout, it is not changing...</p><p>2) Using Wireshark, capture traffic, can we get the FIN_WAIT sate time??? i understood, Fin_wait / close states are internals of tcp stack, this info can n't get through captures? AM I RIGHT?<br />
</p><p>regards</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-closure" rel="tag" title="see questions tagged &#39;closure&#39;">closure</span> <span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '15, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/ce1843f92a1c18db26bc79b3afa9bd50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srinu_bel&#39;s gravatar image" /><p><span>srinu_bel</span><br />
<span class="score" title="20 reputation points">20</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srinu_bel has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Apr '15, 20:07</strong> </span></p></div></div><div id="comments-container-41529" class="comments-container"><span id="41574"></span><div id="comment-41574" class="comment"><div id="post-41574-score" class="comment-score"></div><div class="comment-text"><p>From my point of view it could be that you mixed up TIME-WAIT with FIN_WAIT_1/2</p></div><div id="comment-41574-info" class="comment-info"><span class="comment-age">(19 Apr '15, 09:39)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-41529" class="comment-tools"></div><div class="clear"></div><div id="comment-41529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41536"></span>

<div id="answer-container-41536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41536-score" class="post-score" title="current number of votes">1</div><span id="post-41536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>how about you capture your own traffic for a while and simply check what happens? Those timings often depend on stack behavior, so it could be completely different on each system/stack.</p><p>It's always better to try and see what happens than reading design documents, wondering what reality is like. Use Wireshark, capture traffic, verify.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '15, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41536" class="comments-container"><span id="41565"></span><div id="comment-41565" class="comment"><div id="post-41565-score" class="comment-score"></div><div class="comment-text"><p>hi Jasper Bongertz,</p><p>1) In Ubuntu 12.XX ver we observed FIN_WAIT time as 60sec and other one is less than one sec is taking... even after modifying /proc/sys/net/ipv4/tcp_fin_timeout, it is not changing...</p><p>2) Using Wireshark, capture traffic, can we get the FIN_WAIT sate time??? i understood, Fin_wait / close states are internals of tcp stack, this info can n't get through captures? AM I RIGHT?<br />
</p><p>regards</p></div><div id="comment-41565-info" class="comment-info"><span class="comment-age">(18 Apr '15, 20:08)</span> <span class="comment-user userinfo">srinu_bel</span></div></div><span id="41568"></span><div id="comment-41568" class="comment"><div id="post-41568-score" class="comment-score"></div><div class="comment-text"><p>1) No idea, I don't know what the Ubuntu stack does with this.</p><p>Yep, regarding 2) you're right, you need capture and netstat/ss for this. The capture is to check if the tear down isn't done via RST, and to see who tears down the connection. Then you can compare it to what you see on the OS tools.</p></div><div id="comment-41568-info" class="comment-info"><span class="comment-age">(19 Apr '15, 01:55)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-41536" class="comment-tools"></div><div class="clear"></div><div id="comment-41536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

