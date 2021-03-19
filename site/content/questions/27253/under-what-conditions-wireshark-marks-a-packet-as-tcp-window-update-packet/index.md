+++
type = "question"
title = "Under what conditions Wireshark marks a packet as TCP Window Update packet"
description = '''I understand the TCP window mechanism and that all ACK packets contain advertized Window size which keeps fluctuating. If so, why Wireshark marks certain packets as Window update packet and why is it important to observe? Changing Window sizes is not normal?'''
date = "2013-11-21T22:31:00Z"
lastmod = "2013-11-22T02:04:00Z"
weight = 27253
keywords = [ "tcp_window_update" ]
aliases = [ "/questions/27253" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Under what conditions Wireshark marks a packet as TCP Window Update packet](/questions/27253/under-what-conditions-wireshark-marks-a-packet-as-tcp-window-update-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27253-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27253-score" class="post-score" title="current number of votes">0</div><span id="post-27253-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I understand the TCP window mechanism and that all ACK packets contain advertized Window size which keeps fluctuating. If so, why Wireshark marks certain packets as Window update packet and why is it important to observe? Changing Window sizes is not normal?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp_window_update" rel="tag" title="see questions tagged &#39;tcp_window_update&#39;">tcp_window_update</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '13, 22:31</strong></p><img src="https://secure.gravatar.com/avatar/e14ca2c421c54ea693198e806821f50d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xkgt&#39;s gravatar image" /><p><span>xkgt</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xkgt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '13, 02:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-27253" class="comments-container"></div><div id="comment-tools-27253" class="comment-tools"></div><div class="clear"></div><div id="comment-27253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27254"></span>

<div id="answer-container-27254" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27254-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27254-score" class="post-score" title="current number of votes">2</div><span id="post-27254-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="xkgt has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>The sequence number doesn't change, which means that there is no new data being send</li><li>The acknowledge number doesn't change which means that no new incoming data is acknowledged</li><li>The Window size is different from the one in the previous packet of the same sender</li></ol><p>Basically, all new information the TCP layer of such a packet contains is a different window size.</p><p>And yes, changing window sizes is normal. You often see it when it gets close to zero (or even down to zero) when a higher window size is advertised, which is used to tell the sender to keep going. But a lot of systems also advertise new window sizes even when they're not close to zero, just to let the sender know that they have more buffer space available for incoming packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '13, 22:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Nov '13, 22:48</strong> </span></p></div></div><div id="comments-container-27254" class="comments-container"></div><div id="comment-tools-27254" class="comment-tools"></div><div class="clear"></div><div id="comment-27254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27262"></span>

<div id="answer-container-27262" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27262-score" class="post-score" title="current number of votes">1</div><span id="post-27262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>If so, why Wireshark marks certain packets as Window update packet</p></blockquote><p>see the explanation of <span>@Jasper</span>.</p><blockquote><p>and why is it important to observe? Changing Window sizes is not normal?</p></blockquote><p>A window size change is at least nothing abnormal and thus observing it is not necessary, <strong>unless</strong> the window size drops to zero or you have performance problems of any kind.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '13, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-27262" class="comments-container"></div><div id="comment-tools-27262" class="comment-tools"></div><div class="clear"></div><div id="comment-27262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

