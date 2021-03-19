+++
type = "question"
title = "Using AR5212/AR5213 with wireshark in monitor mode."
description = '''I am working with ubuntu 11.10. I am able to setup a monitor device using either iwconfig or airmon-ng, but i am unable to select the monitor mode box in the wireshark capture settings. could anybody help?'''
date = "2012-01-23T08:08:00Z"
lastmod = "2012-01-23T15:05:00Z"
weight = 8564
keywords = [ "ubuntu", "monitor", "ar5213", "ar5212" ]
aliases = [ "/questions/8564" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using AR5212/AR5213 with wireshark in monitor mode.](/questions/8564/using-ar5212ar5213-with-wireshark-in-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8564-score" class="post-score" title="current number of votes">0</div><span id="post-8564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working with ubuntu 11.10.</p><p>I am able to setup a monitor device using either iwconfig or airmon-ng, but i am unable to select the monitor mode box in the wireshark capture settings.</p><p>could anybody help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span> <span class="post-tag tag-link-ar5213" rel="tag" title="see questions tagged &#39;ar5213&#39;">ar5213</span> <span class="post-tag tag-link-ar5212" rel="tag" title="see questions tagged &#39;ar5212&#39;">ar5212</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '12, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/ab54de551bfeb99a23c759dc5a566e2f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="red&#39;s gravatar image" /><p><span>red</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="red has no accepted answers">0%</span></p></div></div><div id="comments-container-8564" class="comments-container"></div><div id="comment-tools-8564" class="comment-tools"></div><div class="clear"></div><div id="comment-8564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8571"></span>

<div id="answer-container-8571" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8571-score" class="post-score" title="current number of votes">0</div><span id="post-8571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just try capturing on the monitor device <em>without</em> checking the monitor mode box. Checking the monitor mode box causes Wireshark to ask libpcap to set up monitor mode; in Linux distributions where libpcap is not linked with libnl, which includes Debian and its derivatives such as Ubuntu, that doesn't work with libpcap 1.1.0 or 1.1.1, as provided with Ubuntu. Therefore, you need to run airmon-ng to set up the monitor device (as libpcap isn't linked with libnl, it won't set up the monitor device itself) and, as the monitor device is already in monitor mode, there's no need to have Wireshark ask libpcap to put it into monitor mode and, in fact, libpcap's attempt to do so won't work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '12, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8571" class="comments-container"></div><div id="comment-tools-8571" class="comment-tools"></div><div class="clear"></div><div id="comment-8571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

