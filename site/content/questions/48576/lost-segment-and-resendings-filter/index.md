+++
type = "question"
title = "lost segment and resendings filter?"
description = '''Hi im trying to filter Lost segments and resendings.  How can i filter it on I/O Statistics? Thanks'''
date = "2015-12-16T07:30:00Z"
lastmod = "2015-12-16T08:24:00Z"
weight = 48576
keywords = [ "ask.wireshark.org", "wireshark" ]
aliases = [ "/questions/48576" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [lost segment and resendings filter?](/questions/48576/lost-segment-and-resendings-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48576-score" class="post-score" title="current number of votes">0</div><span id="post-48576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi im trying to filter Lost segments and resendings.</p><p>How can i filter it on I/O Statistics?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ask.wireshark.org" rel="tag" title="see questions tagged &#39;ask.wireshark.org&#39;">ask.wireshark.org</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '15, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/464c35db7abc9a7a3ec7b163eac84d99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marko&#39;s gravatar image" /><p><span>Marko</span><br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marko has no accepted answers">0%</span></p></div></div><div id="comments-container-48576" class="comments-container"></div><div id="comment-tools-48576" class="comment-tools"></div><div class="clear"></div><div id="comment-48576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48579"></span>

<div id="answer-container-48579" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48579-score" class="post-score" title="current number of votes">0</div><span id="post-48579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Where you configure the curves for the graph, configure one to use display filter <code>tcp.analysis.lost_segment</code> and another one to use display filter <code>tcp.analysis.retransmission</code>.</p><p>Just bear in mind that the condition <code>tcp.analysis.lost_segment</code> is true for the first captured packet following the lost segment, so it does not tell you the actual number of lost packets (or even bytes in the lost packets).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '15, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48579" class="comments-container"></div><div id="comment-tools-48579" class="comment-tools"></div><div class="clear"></div><div id="comment-48579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

