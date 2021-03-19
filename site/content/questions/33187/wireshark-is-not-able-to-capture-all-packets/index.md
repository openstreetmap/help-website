+++
type = "question"
title = "wireshark is not able to capture all packets"
description = '''HI when I am capturing packets on my lan card, i don&#x27;t see all packets captured i don&#x27;t see dns packets, response packets from destination servers These packets are captured in other laptops. Is there any settings issue? BR Tanmay'''
date = "2014-05-29T23:59:00Z"
lastmod = "2014-05-30T07:38:00Z"
weight = 33187
keywords = [ "windows" ]
aliases = [ "/questions/33187" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark is not able to capture all packets](/questions/33187/wireshark-is-not-able-to-capture-all-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33187-score" class="post-score" title="current number of votes">0</div><span id="post-33187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI</p><p>when I am capturing packets on my lan card, i don't see all packets captured i don't see dns packets, response packets from destination servers These packets are captured in other laptops. Is there any settings issue?</p><p>BR Tanmay</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '14, 23:59</strong></p><img src="https://secure.gravatar.com/avatar/ec839d7a4e275256eff4cdfab091ddbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tantmay&#39;s gravatar image" /><p><span>tantmay</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tantmay has no accepted answers">0%</span></p></div></div><div id="comments-container-33187" class="comments-container"></div><div id="comment-tools-33187" class="comment-tools"></div><div class="clear"></div><div id="comment-33187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33202"></span>

<div id="answer-container-33202" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33202-score" class="post-score" title="current number of votes">0</div><span id="post-33202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>These packets are captured in other laptops.</p></blockquote><p>If only one system is affected, chances are that there is some kind of security software on that system which prevents Wireshark from seeing the whole traffic. We have seen this here whith the following classes of software</p><ul><li>AV clients</li><li>Desktop Firewalls</li><li>VPN clients</li><li>Endpoint Security (especially Symantec)</li><li>Network Filter Drivers like: <strong>DNE LightWeight Filter</strong> and <strong>Trend Micro LightWeight Filter</strong> (uncheck them on the adapter)</li></ul><p>See the questions with the following tags: <a href="http://ask.wireshark.org/tags/?q=outbound">outbound</a> and/or <a href="http://ask.wireshark.org/tags/?q=outgoing">outgoing</a>. Although your problem seems to be related to <strong>incoming</strong> traffic, the problem might be caused by the same class of software!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '14, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33202" class="comments-container"></div><div id="comment-tools-33202" class="comment-tools"></div><div class="clear"></div><div id="comment-33202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

