+++
type = "question"
title = "Promiscuous or monitor?"
description = '''Trying to listen/see traffic between two pieces of equipment from my laptop. I am using a Hub, Wireshark is in promiscuous mode. Yet, I can not see any traffic other that what is going to/from my laptop. The two pieces of equipment are not computers but do have network cards along with assigned IP a...'''
date = "2015-12-29T12:35:00Z"
lastmod = "2015-12-29T14:03:00Z"
weight = 48748
keywords = [ "promiscuous" ]
aliases = [ "/questions/48748" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Promiscuous or monitor?](/questions/48748/promiscuous-or-monitor)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48748-score" class="post-score" title="current number of votes">0</div><span id="post-48748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to listen/see traffic between two pieces of equipment from my laptop. I am using a Hub, Wireshark is in promiscuous mode. Yet, I can not see any traffic other that what is going to/from my laptop. The two pieces of equipment are not computers but do have network cards along with assigned IP addresses. My laptop is running XP with a Broadcom NIC.</p><p>What am I doing wrong?</p><p>Sam</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-promiscuous" rel="tag" title="see questions tagged &#39;promiscuous&#39;">promiscuous</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '15, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/1fdeb60456e010adacfdc60a061663f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ask&#39;s gravatar image" /><p><span>Ask</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ask has no accepted answers">0%</span></p></div></div><div id="comments-container-48748" class="comments-container"></div><div id="comment-tools-48748" class="comment-tools"></div><div class="clear"></div><div id="comment-48748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48749"></span>

<div id="answer-container-48749" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48749-score" class="post-score" title="current number of votes">0</div><span id="post-48749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ask has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you are sure that the two "non-PCs" do talk to each other while you take your capture, my conclusion is that the box you are using may bear a label reading "HUB" but it actually works as a switch. Also, you may have used one of those so-called "rate-adapting" hubs which internally worked as two independent hubs, one 10 Mbit/s and one 100 Mbit/s, and a bridge (switch) between the two.</p><p>Monitor mode of network adaptors is only relevant for wireless adaptors and on these, for operating systems other than Microsoft Windows.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '15, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Dec '15, 12:50</strong> </span></p></div></div><div id="comments-container-48749" class="comments-container"><span id="48751"></span><div id="comment-48751" class="comment"><div id="post-48751-score" class="comment-score"></div><div class="comment-text"><p>sindy, you are exactly right when you typed "my conclusion is that the box you are using may bear a label reading "HUB" but it actually works as a switch", we pulled out an old HUB made in the previous century and everything went to working perfectly.</p><p>Thanks for the response.</p><p>Sam</p></div><div id="comment-48751-info" class="comment-info"><span class="comment-age">(29 Dec '15, 14:03)</span> <span class="comment-user userinfo">Ask</span></div></div></div><div id="comment-tools-48749" class="comment-tools"></div><div class="clear"></div><div id="comment-48749-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

