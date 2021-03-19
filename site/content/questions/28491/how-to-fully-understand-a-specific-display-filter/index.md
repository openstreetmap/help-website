+++
type = "question"
title = "how to fully understand a specific display filter?"
description = '''Hi, As we know, we have lots of display filter based on tcp fields or wireshark specific fields. For example, tcp.analysis.flags. But I don&#x27;t where to find the detailed explanation of this display filter.  I can find the description here: http://www.wireshark.org/docs/dfref/t/tcp.html. But it still ...'''
date = "2013-12-30T18:57:00Z"
lastmod = "2014-01-02T23:41:00Z"
weight = 28491
keywords = [ "display_filter" ]
aliases = [ "/questions/28491" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to fully understand a specific display filter?](/questions/28491/how-to-fully-understand-a-specific-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28491-score" class="post-score" title="current number of votes">0</div><span id="post-28491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>As we know, we have lots of display filter based on tcp fields or wireshark specific fields. For example, tcp.analysis.flags. But I don't where to find the detailed explanation of this display filter.</p><p>I can find the description here: <a href="http://www.wireshark.org/docs/dfref/t/tcp.html.">http://www.wireshark.org/docs/dfref/t/tcp.html.</a> But it still doesn't tell me what exactly does tcp.analysis.flags mean. This applies to all of the other display filters or fields.</p><p>could anyone let me know how do you figure it out?</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-display_filter" rel="tag" title="see questions tagged &#39;display_filter&#39;">display_filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '13, 18:57</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p><span>SteveZhou</span><br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Dec '13, 18:58</strong> </span></p></div></div><div id="comments-container-28491" class="comments-container"></div><div id="comment-tools-28491" class="comment-tools"></div><div class="clear"></div><div id="comment-28491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28536"></span>

<div id="answer-container-28536" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28536-score" class="post-score" title="current number of votes">4</div><span id="post-28536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SteveZhou has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In general you should approach this from another angle. If you start by understanding the protocol (by reading the relevant RFC, paper or website, eg. the <a href="http://tcpipguide.com/">TCP/IP guide</a>) then the meanings of the fields become apparent.</p><p>Wireshark adds to this in the form of additional field (so called generated fields, enclosed in square brackets), which express additional analysis of the protocol or session. It is these which you won't find in the RFCs, but should either be described in the <a href="http://wiki.wireshark.org">Wiki</a>, the Users Guide, or in books (like from <a href="http://www.wiresharktraining.com/">WiresharkU</a>). Since we are engineers first, authors second, the documentation lacks here.</p><p>If you understand source code, you can always go back to <a href="https://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-tcp.c">the source</a> and read the code that creates these fields (Pro tip: that's what we do when confronted with such questions). In this case the (generated) field you mentioned is created when one of the (generated) analysis fields is created. So then it can be used as a generic marker to filter packets which have something noteworthy that triggered the creation of a TCP analysis field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '14, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-28536" class="comments-container"><span id="28545"></span><div id="comment-28545" class="comment"><div id="post-28545-score" class="comment-score"></div><div class="comment-text"><p>That's right! Thanks a lot!</p></div><div id="comment-28545-info" class="comment-info"><span class="comment-age">(02 Jan '14, 23:41)</span> <span class="comment-user userinfo">SteveZhou</span></div></div></div><div id="comment-tools-28536" class="comment-tools"></div><div class="clear"></div><div id="comment-28536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

