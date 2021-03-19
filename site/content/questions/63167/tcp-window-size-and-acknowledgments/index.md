+++
type = "question"
title = "TCP Window Size and Acknowledgments"
description = '''Hey guys hoping someone can set me straight... I&#x27;m doing some study on TCP and understand that after a sending host sends a receiver an amount of data which fills the receiving hosts TCP window it must then wait for an acknowledgement from the receiver before sending another series of segments to fi...'''
date = "2017-07-27T03:03:00Z"
lastmod = "2017-07-27T03:30:00Z"
weight = 63167
keywords = [ "tcp" ]
aliases = [ "/questions/63167" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Window Size and Acknowledgments](/questions/63167/tcp-window-size-and-acknowledgments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63167-score" class="post-score" title="current number of votes">0</div><span id="post-63167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys hoping someone can set me straight...</p><p>I'm doing some study on TCP and understand that after a sending host sends a receiver an amount of data which fills the receiving hosts TCP window it must then wait for an acknowledgement from the receiver before sending another series of segments to fill the receivers window size.</p><p>When capturing file transfers in Wireshark I'm not seeing this behavior. For instance in a capture I did the receivers calculated window size was 262144 as show in Wire shark. The receiver sent back an acknowledgement when it received 40320 bytes.</p><p>Help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '17, 03:03</strong></p><img src="https://secure.gravatar.com/avatar/6bbcddb382ce0c19dd0cc6c2bea90244?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisBell&#39;s gravatar image" /><p><span>ChrisBell</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisBell has no accepted answers">0%</span></p></div></div><div id="comments-container-63167" class="comments-container"></div><div id="comment-tools-63167" class="comment-tools"></div><div class="clear"></div><div id="comment-63167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="63168"></span>

<div id="answer-container-63168" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63168-score" class="post-score" title="current number of votes">0</div><span id="post-63168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure if this is what confuses you, but the receiver can ACK incoming packets at any point in time (usually every 2nd packet is acknowledged to keep a good flow going).</p><p>If the receiver would wait with the acknowledgement until the full window has been received it would stop the communication cold until the ACK has traveled all the way back to the sender, silencing the flow for the full Round Trip Time - this would be highly inefficient. This is why packets are constantly acknowledged, and not only when the window has been filled up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '17, 03:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-63168" class="comments-container"></div><div id="comment-tools-63168" class="comment-tools"></div><div class="clear"></div><div id="comment-63168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63170"></span>

<div id="answer-container-63170" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63170-score" class="post-score" title="current number of votes">0</div><span id="post-63170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you've got properly the idea of window scaling so incorrect interpretation of the window size information is not the source of your confusion, your misconception seems to be that the receiver must not send an ACK until the receiving buffer is full.</p><p>In fact, the window is there to facilitate making use of the available bandwidth on links with long round-trip delay. So you can send up to the window size of bytes without waiting for ACK, and each new ACK tells you (on top of other information) what the window size was when this ACK was being sent. And the receiving side may and should send ACK much more frequently than just after having the window fully used, even if it doesn't send any own data in opposite direction. It is just that you need not wait for an ack for every single packet, as in such case, the throughput would be heavily affected by the round trip delay.</p><p>The window is actually a buffer between the TCP stack and the receiving application. So if the receiving application is busy and doesn't pick up the received data from the buffer, you may get an ACK saying that the window size is 0, which is equivalent to X-off. And when the application fetches some data, creating some free space in the buffer, you'll get another ACK for the same sequence number but with non-zero window size, which is equivalent to X-on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '17, 03:30</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-63170" class="comments-container"></div><div id="comment-tools-63170" class="comment-tools"></div><div class="clear"></div><div id="comment-63170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

