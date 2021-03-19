+++
type = "question"
title = "Wrong Time"
description = '''When running a capture, the timestamp for the packets captured by WireShark is not the same as the time on the local machine. As a matter of fact, if I run a capture on two machines talking to each other, both captures will have the wrong time, but they are different. Anyone seen this before?'''
date = "2010-12-03T13:23:00Z"
lastmod = "2010-12-03T16:21:00Z"
weight = 1233
keywords = [ "time" ]
aliases = [ "/questions/1233" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wrong Time](/questions/1233/wrong-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1233-score" class="post-score" title="current number of votes">0</div><span id="post-1233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When running a capture, the timestamp for the packets captured by WireShark is not the same as the time on the local machine. As a matter of fact, if I run a capture on two machines talking to each other, both captures will have the wrong time, but they are different.</p><p>Anyone seen this before?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '10, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/aab96b5bbc7d9bfb42153bdf2196e035?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gazoo&#39;s gravatar image" /><p><span>gazoo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gazoo has no accepted answers">0%</span></p></div></div><div id="comments-container-1233" class="comments-container"></div><div id="comment-tools-1233" class="comment-tools"></div><div class="clear"></div><div id="comment-1233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1240"></span>

<div id="answer-container-1240" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1240-score" class="post-score" title="current number of votes">0</div><span id="post-1240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When capturing, Wireshark gets the timestamp data from WinPcap, which gets them from the underlying OS. When reading a capture file, the timestamps (obviously) come from that file's data.</p><p>You can run into differences based on precision (Wireshark natively goes down to nanoseconds, but some capture utilities go no further than microseconds) and accuracy (how accurate were the OS clocks to start with?). You can also see cases where the type of adapter in use skews the timestamps; USB network adapters are notoriously imprecise in this respect. Remember that the timestamps are applied when the OS kernel processes the packet, so any latency along the way (say, the USB bus in the case of those adapters) will be reflected in "poor" timestamps.</p><p>How far off are the timestamps in your case?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '10, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-1240" class="comments-container"></div><div id="comment-tools-1240" class="comment-tools"></div><div class="clear"></div><div id="comment-1240-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

