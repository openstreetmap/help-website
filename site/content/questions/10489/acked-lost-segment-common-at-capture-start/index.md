+++
type = "question"
title = "ACKed lost segment (common at capture start)"
description = '''Hi, When I&#x27;m looking at the expert info in a capture&amp;lt;I see these messages: ACKed lost segment (common at capture start) previous segment lost (common at capture start) I&#x27;m running WS 1.4.9 on a VM server. The through put on the interface is avg. 45.8 Mbits/sec for a 5 minute period. Am I running ...'''
date = "2012-04-27T10:47:00Z"
lastmod = "2012-04-27T14:22:00Z"
weight = 10489
keywords = [ "segment", "lost" ]
aliases = [ "/questions/10489" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ACKed lost segment (common at capture start)](/questions/10489/acked-lost-segment-common-at-capture-start)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10489-score" class="post-score" title="current number of votes">0</div><span id="post-10489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>When I'm looking at the expert info in a capture&lt;I see these messages: ACKed lost segment (common at capture start) previous segment lost (common at capture start)</p><p>I'm running WS 1.4.9 on a VM server. The through put on the interface is avg. 45.8 Mbits/sec for a 5 minute period. Am I running into and issue with the interface because wireshark is not talking directly to it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-segment" rel="tag" title="see questions tagged &#39;segment&#39;">segment</span> <span class="post-tag tag-link-lost" rel="tag" title="see questions tagged &#39;lost&#39;">lost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '12, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/5bc47c3051f0b0cd6eb09fcefcb0af54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rayzorx&#39;s gravatar image" /><p><span>Rayzorx</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rayzorx has no accepted answers">0%</span></p></div></div><div id="comments-container-10489" class="comments-container"></div><div id="comment-tools-10489" class="comment-tools"></div><div class="clear"></div><div id="comment-10489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10492"></span>

<div id="answer-container-10492" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10492-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10492-score" class="post-score" title="current number of votes">0</div><span id="post-10492-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you're seeing is that Wireshark has come across acknowledges for packets that it hasn't captured. That can happen at the beginning of a trace file if a conversation has already started (which is quite common), or - and that can be problematic sometimes - it is due to the fact that Wireshark dropped packets.</p><p>Dropped packets are packets that have been transfered and were seen by the network card Wireshark captures on, but it didn't pick it up. Usually the reason is that the write-to-disk speed isn't high enough to cope with the amount of data that has to be captured and written to file. In a VM environment it is more likely to happen than on a single box environment since the write commands have to share bandwidth with the other VMs that are living on the same storage. I guess especially when you're saying you're having 45.8 MBit/s for 5 minutes that there were bursts with much higher speeds that got averaged into a less eyebrow-raising speed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Apr '12, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10492" class="comments-container"></div><div id="comment-tools-10492" class="comment-tools"></div><div class="clear"></div><div id="comment-10492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

