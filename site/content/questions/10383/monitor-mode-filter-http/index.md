+++
type = "question"
title = "Monitor Mode Filter HTTP"
description = '''Folowing up http://ask.wireshark.org/questions/8178/capture-packets-in-monitor-mode-option-does-not-work-unable-to-scan-any-http-traffic-other-than-my-own I added an interface to monitor all the traffic on the wireless WPA network and I&#x27;m able to see lots of 802.11 packets. I inserted wy wpa key in ...'''
date = "2012-04-22T09:14:00Z"
lastmod = "2012-04-22T09:33:00Z"
weight = 10383
keywords = [ "http", "monitor", "wpa" ]
aliases = [ "/questions/10383" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor Mode Filter HTTP](/questions/10383/monitor-mode-filter-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10383-score" class="post-score" title="current number of votes">0</div><span id="post-10383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Folowing up <a href="http://ask.wireshark.org/questions/8178/capture-packets-in-monitor-mode-option-does-not-work-unable-to-scan-any-http-traffic-other-than-my-own">http://ask.wireshark.org/questions/8178/capture-packets-in-monitor-mode-option-does-not-work-unable-to-scan-any-http-traffic-other-than-my-own</a></p><p>I added an interface to monitor all the traffic on the wireless WPA network and I'm able to see lots of 802.11 packets.</p><p>I inserted wy wpa key in preferences, enabled the option to decrypt traffic, started sniffing, disconnected a computer from the network and reconnected and lastly acessed a page on youtube with http.</p><p>My problem is that I can't decrypt the http traffic. Why?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span> <span class="post-tag tag-link-wpa" rel="tag" title="see questions tagged &#39;wpa&#39;">wpa</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '12, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/8692496b0784fb7911f8d9eaa54187c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miguel&#39;s gravatar image" /><p><span>miguel</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miguel has no accepted answers">0%</span></p></div></div><div id="comments-container-10383" class="comments-container"></div><div id="comment-tools-10383" class="comment-tools"></div><div class="clear"></div><div id="comment-10383-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10384"></span>

<div id="answer-container-10384" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10384-score" class="post-score" title="current number of votes">0</div><span id="post-10384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If by "Filter HTTP" you mean that, when you did the capture, you used a capture filter that only captured HTTP, such as <code>tcp port 80</code>, then you won't be able to decrypt the traffic because, to quote <a href="http://wiki.wireshark.org/HowToDecrypt802.11">the Wireshark Wiki's "How to decrypt 802.11" page</a>, "WPA and WPA2 use keys derived from an EAPOL handshake to encrypt traffic. Unless <strong>all four</strong> handshake packets are present for the session you're trying to decrypt, Wireshark won't be able to decrypt the traffic. You can use the display filter <strong>eapol</strong> to locate EAPOL packets in your capture."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '12, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10384" class="comments-container"></div><div id="comment-tools-10384" class="comment-tools"></div><div class="clear"></div><div id="comment-10384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

