+++
type = "question"
title = "How does wireshark detect TCP retransmissions?"
description = '''I was looking at two traces one from the sending side where I saw the original packet and the retransmitted packet. I can understand how wireshark would flag the second packet as a retransmission in the expert info because it would simply need to look for two packet with the same sequence number. Ho...'''
date = "2013-10-03T14:02:00Z"
lastmod = "2013-10-03T14:13:00Z"
weight = 25609
keywords = [ "expert-info", "retransmission", "tcp" ]
aliases = [ "/questions/25609" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How does wireshark detect TCP retransmissions?](/questions/25609/how-does-wireshark-detect-tcp-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25609-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25609-score" class="post-score" title="current number of votes">0</div><span id="post-25609-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was looking at two traces one from the sending side where I saw the original packet and the retransmitted packet. I can understand how wireshark would flag the second packet as a retransmission in the expert info because it would simply need to look for two packet with the same sequence number. However, in second capture where the first packet is missing and I only see the retransmitted packet, I'm wondering how wireshark was able to detect that the packet was a retransmit? Can someone explain how it knows this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-expert-info" rel="tag" title="see questions tagged &#39;expert-info&#39;">expert-info</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '13, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/fc4308015d9c1873c69e1e121587e2f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="a5snc&#39;s gravatar image" /><p><span>a5snc</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="a5snc has no accepted answers">0%</span></p></div></div><div id="comments-container-25609" class="comments-container"></div><div id="comment-tools-25609" class="comment-tools"></div><div class="clear"></div><div id="comment-25609-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25610"></span>

<div id="answer-container-25610" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25610-score" class="post-score" title="current number of votes">0</div><span id="post-25610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sure. If packets are in the correct order, the TCP sequence is either the same (if the previous packet had no content) or greater than the sequence number in the previous packet. So the current sequence number must always be greater or equal to the previous number, and if Wireshark sees a retransmission the sequence number is "old", thus less than the sequence number of the packet it has previously seen (mathematically "monotonically increasing").</p><p>Well, it's a little more complicated than this actually, because a packet arriving after another in the wrong order could also be a simple "Out-of-Order" situation. In Wireshark there is a hard coded limit of 3 milliseconds, after which an "out of order" packet is marked "retransmission" instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '13, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Oct '13, 14:22</strong> </span></p></div></div><div id="comments-container-25610" class="comments-container"></div><div id="comment-tools-25610" class="comment-tools"></div><div class="clear"></div><div id="comment-25610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

