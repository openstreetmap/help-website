+++
type = "question"
title = "What are MDNS and BJNP protocols and how to get rid of there traffic?"
description = '''On my Ubuntu 16.04 Linux desktop computer I see a non-stop traffic in Wireshark about two protocols MDNS and BJNP. See: https://i.imgur.com/wbOcpzO.png What are those two protocols and how to get rid of the non-stop traffic? Thanks'''
date = "2016-10-11T10:43:00Z"
lastmod = "2016-10-11T11:35:00Z"
weight = 56300
keywords = [ "protocol" ]
aliases = [ "/questions/56300" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What are MDNS and BJNP protocols and how to get rid of there traffic?](/questions/56300/what-are-mdns-and-bjnp-protocols-and-how-to-get-rid-of-there-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56300-score" class="post-score" title="current number of votes">0</div><span id="post-56300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On my Ubuntu 16.04 Linux desktop computer I see a non-stop traffic in Wireshark about two protocols MDNS and BJNP. See: <a href="https://i.imgur.com/wbOcpzO.png">https://i.imgur.com/wbOcpzO.png</a></p><p>What are those two protocols and how to get rid of the non-stop traffic? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '16, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/de7aea9d0010523cfc0b1ff65b49c5f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dolphin500&#39;s gravatar image" /><p><span>dolphin500</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dolphin500 has no accepted answers">0%</span></p></div></div><div id="comments-container-56300" class="comments-container"></div><div id="comment-tools-56300" class="comment-tools"></div><div class="clear"></div><div id="comment-56300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56302"></span>

<div id="answer-container-56302" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56302-score" class="post-score" title="current number of votes">0</div><span id="post-56302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Both these protocols are LAN service discovery protocols (MDNS = multicast DNS, BJNP is a prorietary protocol by Canon). Up to their payload some application running on your Ubuntu is searching for any scanner possibly connected to your LAN. You can get rid of this traffic either actually, by disabling that application (or daemon), or just prevent them from being captured by setting a capture filter saying "don't capture UDP packets to/from ports 5353 and 8612.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '16, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Oct '16, 11:36</strong> </span></p></div></div><div id="comments-container-56302" class="comments-container"></div><div id="comment-tools-56302" class="comment-tools"></div><div class="clear"></div><div id="comment-56302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

