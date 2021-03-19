+++
type = "question"
title = "Ubuntu, ath9k, monitor and promiscuous mode - can only capture 802.11 protocol traffic"
description = '''I can&#x27;t capture any http traffic, not even my own. Please help.'''
date = "2013-09-03T17:25:00Z"
lastmod = "2013-09-04T17:14:00Z"
weight = 24320
keywords = [ "monitor" ]
aliases = [ "/questions/24320" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Ubuntu, ath9k, monitor and promiscuous mode - can only capture 802.11 protocol traffic](/questions/24320/ubuntu-ath9k-monitor-and-promiscuous-mode-can-only-capture-80211-protocol-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24320-score" class="post-score" title="current number of votes">0</div><span id="post-24320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can't capture any http traffic, not even my own.</p><p>Please help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '13, 17:25</strong></p><img src="https://secure.gravatar.com/avatar/02a4723f6e7b5088504f4464855d4cb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ayush&#39;s gravatar image" /><p><span>Ayush</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ayush has no accepted answers">0%</span></p></div></div><div id="comments-container-24320" class="comments-container"></div><div id="comment-tools-24320" class="comment-tools"></div><div class="clear"></div><div id="comment-24320-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24324"></span>

<div id="answer-container-24324" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24324-score" class="post-score" title="current number of votes">1</div><span id="post-24324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ayush has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark will only recognize 802.11 traffic as being IP traffic (and if it doesn't recognize it as IP traffic, it won't recognize it as TCP traffic, and if it doesn't recognize it as TCP traffic, it won't recognize it as HTTP traffic) if the traffic is either not encrypted (on a non-protected network, not using WEP or WPA/WPA2) or if if it's encrypted but <a href="http://wiki.wireshark.org/HowToDecrypt802.11">Wireshark is configured to decrypt it</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '13, 22:02</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-24324" class="comments-container"><span id="24364"></span><div id="comment-24364" class="comment"><div id="post-24364-score" class="comment-score"></div><div class="comment-text"><p>Guy Harris - I tried entering my comcast xfinity wpa2-psk key but it won't accept (neither is ASCII form nor in HEX). It tells me "Invalid key format". please help.</p></div><div id="comment-24364-info" class="comment-info"><span class="comment-age">(04 Sep '13, 17:14)</span> <span class="comment-user userinfo">Ayush</span></div></div></div><div id="comment-tools-24324" class="comment-tools"></div><div class="clear"></div><div id="comment-24324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

