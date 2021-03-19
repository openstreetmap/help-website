+++
type = "question"
title = "How to call own dissector again?"
description = '''Is it possible to call the own dissector again? The protocol that i want to dissect, starts sometimes again in the same packet. Is there a good way to call the dissector again or are there other ways?'''
date = "2013-01-15T07:39:00Z"
lastmod = "2013-01-17T11:09:00Z"
weight = 17699
keywords = [ "again", "call_dissector", "twice" ]
aliases = [ "/questions/17699" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to call own dissector again?](/questions/17699/how-to-call-own-dissector-again)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17699-score" class="post-score" title="current number of votes">0</div><span id="post-17699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to call the own dissector again? The protocol that i want to dissect, starts sometimes again in the same packet. Is there a good way to call the dissector again or are there other ways?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-again" rel="tag" title="see questions tagged &#39;again&#39;">again</span> <span class="post-tag tag-link-call_dissector" rel="tag" title="see questions tagged &#39;call_dissector&#39;">call_dissector</span> <span class="post-tag tag-link-twice" rel="tag" title="see questions tagged &#39;twice&#39;">twice</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '13, 07:39</strong></p><img src="https://secure.gravatar.com/avatar/2620e86c76c9beb19f83a8785f0bda85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sphinxs&#39;s gravatar image" /><p><span>sphinxs</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sphinxs has no accepted answers">0%</span></p></div></div><div id="comments-container-17699" class="comments-container"></div><div id="comment-tools-17699" class="comment-tools"></div><div class="clear"></div><div id="comment-17699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17731"></span>

<div id="answer-container-17731" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17731-score" class="post-score" title="current number of votes">1</div><span id="post-17731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you mean that, in whatever lower-level protocol your protocol runs atop, a single lower-level protocol packet can contain more than one packet for your protocol, the way you should, in general, do that is to have your dissector loop through the contents of the lower-level protocol packet's payload (that's what's in the tvbuff it's handed) and keep dissecting packets until it runs out.</p><p>Note that if the lower-level protocol is TCP, that task is more complicated, as you can have multiple higher-level protocol packets within one TCP packet (TCP segment), you can have multiple TCP packets contain <em>one</em> higher-level protocol packet, and you can have both. If your protocol runs atop TCP, and each packet in your protocol is at least <em>N</em> bytes long for some value of <em>N</em> &gt; 0, and if the first <em>N</em> bytes contain enough information to determine how long the packet is, you can have your protocol's dissector call <code>tcp_dissect_pdus()</code>, which will handle the details for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '13, 20:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-17731" class="comments-container"><span id="17756"></span><div id="comment-17756" class="comment"><div id="post-17756-score" class="comment-score"></div><div class="comment-text"><p>Thank's for the fast reply. Unfortunately the protocol has no length field, is starts and ends with an specific sequence with N messages in between. Should i use a function like the one from 2.7.2 in the developers.readme, to reassembly the TCP segments? Or should is use the functions from reassemble.h ?</p></div><div id="comment-17756-info" class="comment-info"><span class="comment-age">(17 Jan '13, 11:09)</span> <span class="comment-user userinfo">sphinxs</span></div></div></div><div id="comment-tools-17731" class="comment-tools"></div><div class="clear"></div><div id="comment-17731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

