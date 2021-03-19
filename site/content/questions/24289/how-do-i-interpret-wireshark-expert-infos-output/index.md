+++
type = "question"
title = "How do I interpret Wireshark Expert Infos output?"
description = '''I have used version 1.10.1 to capture a 900 mbyte trace file. The trace file is a download of a resultant data set from a Netezza Data Warehouse query. I have run Wireshark Expert Infos against it and the Notes have recorded 128 Duplicate ACK&#x27;s run a total of 25938 times. Does this indicate a heavil...'''
date = "2013-09-02T15:04:00Z"
lastmod = "2013-09-03T02:56:00Z"
weight = 24289
keywords = [ "infos", "expert" ]
aliases = [ "/questions/24289" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I interpret Wireshark Expert Infos output?](/questions/24289/how-do-i-interpret-wireshark-expert-infos-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24289-score" class="post-score" title="current number of votes">0</div><span id="post-24289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have used version 1.10.1 to capture a 900 mbyte trace file. The trace file is a download of a resultant data set from a Netezza Data Warehouse query. I have run Wireshark Expert Infos against it and the Notes have recorded 128 Duplicate ACK's run a total of 25938 times. Does this indicate a heavily congested network between the laptop and the Server? I am using a 1 Gbit Netgear Switch with port mirroring off a 100 mbyte LAN. I am attaching the output. <img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_Expert_Infos_2.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-infos" rel="tag" title="see questions tagged &#39;infos&#39;">infos</span> <span class="post-tag tag-link-expert" rel="tag" title="see questions tagged &#39;expert&#39;">expert</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '13, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/16c80ca493c77f3486cbb7ff38cc5d3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoberist&#39;s gravatar image" /><p><span>Zoberist</span><br />
<span class="score" title="0 reputation points">0</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoberist has no accepted answers">0%</span></p></img></div></div><div id="comments-container-24289" class="comments-container"></div><div id="comment-tools-24289" class="comment-tools"></div><div class="clear"></div><div id="comment-24289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24291"></span>

<div id="answer-container-24291" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24291-score" class="post-score" title="current number of votes">0</div><span id="post-24291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"the Notes have recorded 128 Duplicate ACK's run a total of 25938 times."</p><p>The "Notes:128 (25938)" indicate that you have 25938 packets with 128 different types of a 'Note' - most of which are duplicate ACKS.</p><p>As a Duplicate ACK combined with the duplicate ACK # is treated as a unique event when in fact it is just an indication of an out-of-order arrival at the receiver, this number is kind of misleading. If you have a large windowsize offered by a receiver and a packet early in the window was dropped or delayed you'll see a dupack with increasing numbers, all reporting the same missing packet. The third dup ack (1095) seen at the sender will will trigger a fast retransmission (956).</p><p>Putting this in perspective: Receiving a 900MB file with only 412 'suspected Retransmissions' doesn't look like a high number to me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '13, 22:06</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Sep '13, 22:19</strong> </span></p></div></div><div id="comments-container-24291" class="comments-container"><span id="24299"></span><div id="comment-24299" class="comment"><div id="post-24299-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much !!!!</p></div><div id="comment-24299-info" class="comment-info"><span class="comment-age">(03 Sep '13, 02:56)</span> <span class="comment-user userinfo">Zoberist</span></div></div></div><div id="comment-tools-24291" class="comment-tools"></div><div class="clear"></div><div id="comment-24291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

