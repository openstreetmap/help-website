+++
type = "question"
title = "How to integrate a custom protocol into the telephony analyzer?"
description = '''Hello all, is there a way to register an additional protocol into the telephony analyzer (which may consist in just marking that protocol as a telephony-related one)? I&#x27;ve got a Lua dissector for a home brewed protocol which accompanies SIP in our application, and I would like to see the conversatio...'''
date = "2016-10-27T11:18:00Z"
lastmod = "2016-10-27T12:42:00Z"
weight = 56749
keywords = [ "telephony", "register", "graph" ]
aliases = [ "/questions/56749" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to integrate a custom protocol into the telephony analyzer?](/questions/56749/how-to-integrate-a-custom-protocol-into-the-telephony-analyzer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56749-score" class="post-score" title="current number of votes">0</div><span id="post-56749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>is there a way to register an additional protocol into the telephony analyzer (which may consist in just marking that protocol as a telephony-related one)? I've got a Lua dissector for a home brewed protocol which accompanies SIP in our application, and I would like to see the conversations of this protocol in the telephony flow graph together with SIP and RTP. Given that there is no field common to that protocol and SIP which would allow to unambiguously link their messages together, conversations of that protocol (which uses UDP transport) would have to be listed as separate telephony calls in the call list table where you choose the calls from which the flow graph shall be composed.</p><p>The generic flow graph is fine except that it lacks two important features of the telephony-specific one:</p><ul><li><p>the RTP grouping capability, so each RTP packet is represented by its own line in it, which adds a lot of visual noise,</p></li><li><p>the colorization of related conversations.</p></li></ul></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-telephony" rel="tag" title="see questions tagged &#39;telephony&#39;">telephony</span> <span class="post-tag tag-link-register" rel="tag" title="see questions tagged &#39;register&#39;">register</span> <span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '16, 11:18</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56749" class="comments-container"></div><div id="comment-tools-56749" class="comment-tools"></div><div class="clear"></div><div id="comment-56749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56750"></span>

<div id="answer-container-56750" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56750-score" class="post-score" title="current number of votes">0</div><span id="post-56750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sindy has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No there is no API for this currently. Adding a new protocol requires modifying Wireshark source code (voip_calls.c) and recompiling.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '16, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-56750" class="comments-container"></div><div id="comment-tools-56750" class="comment-tools"></div><div class="clear"></div><div id="comment-56750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

