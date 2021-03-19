+++
type = "question"
title = "GSM SMS Call Flow invoke forwardSM"
description = '''Hi i have taken a SMS trace at STP side. I have seen 2 invoke forwardSM Packet and and check the OPCODE for both one of them have opcode 44 which is mt-forwardSM and one contain OPCODE 46 -mo-forwardSM .  i want to know how this is possible in single invoke forwardSM packet.'''
date = "2014-01-18T22:40:00Z"
lastmod = "2014-01-19T20:18:00Z"
weight = 29010
keywords = [ "sms", "-", "gsm", "flow", "call" ]
aliases = [ "/questions/29010" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [GSM SMS Call Flow invoke forwardSM](/questions/29010/gsm-sms-call-flow-invoke-forwardsm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29010-score" class="post-score" title="current number of votes">0</div><span id="post-29010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi i have taken a SMS trace at STP side. I have seen 2 invoke forwardSM Packet and and check the OPCODE for both one of them have opcode 44 which is mt-forwardSM and one contain OPCODE 46 -mo-forwardSM . i want to know how this is possible in single invoke forwardSM packet.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sms" rel="tag" title="see questions tagged &#39;sms&#39;">sms</span> <span class="post-tag tag-link--" rel="tag" title="see questions tagged &#39;-&#39;">-</span> <span class="post-tag tag-link-gsm" rel="tag" title="see questions tagged &#39;gsm&#39;">gsm</span> <span class="post-tag tag-link-flow" rel="tag" title="see questions tagged &#39;flow&#39;">flow</span> <span class="post-tag tag-link-call" rel="tag" title="see questions tagged &#39;call&#39;">call</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '14, 22:40</strong></p><img src="https://secure.gravatar.com/avatar/44a66e03ac895cd48c2cd7f2f9355044?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gaurav&#39;s gravatar image" /><p><span>Gaurav</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gaurav has no accepted answers">0%</span></p></div></div><div id="comments-container-29010" class="comments-container"></div><div id="comment-tools-29010" class="comment-tools"></div><div class="clear"></div><div id="comment-29010-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29025"></span>

<div id="answer-container-29025" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29025-score" class="post-score" title="current number of votes">0</div><span id="post-29025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's definitely possible to see both in a single IP packet if both messages would be being sent to the same next-hop point code by the STP. Most, and virtually every implementation of SS7 over IP will have multiple SS7 messages, even for multiple applications (INAP, ISUP, MAP, etc.), aggregated into one IP packet if it's between the same two point codes (multi-streaming).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '14, 20:18</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jan '14, 20:24</strong> </span></p></div></div><div id="comments-container-29025" class="comments-container"></div><div id="comment-tools-29025" class="comment-tools"></div><div class="clear"></div><div id="comment-29025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

