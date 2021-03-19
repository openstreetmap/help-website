+++
type = "question"
title = "Capturing with AirPcap and seeing only 802.11 protocol, not TCP or HTTP or..."
description = '''I have a new laptop which i downloaded Wireshark 2.05 to and i have my AirPcap cards. Although when i perform a capture i only receive 802.11 traffic in the protocol list. Why am i not capturing TCP, HTTP, etc? and how do i remedy this?'''
date = "2016-08-25T22:34:00Z"
lastmod = "2016-08-28T20:23:00Z"
weight = 55122
keywords = [ "capture" ]
aliases = [ "/questions/55122" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing with AirPcap and seeing only 802.11 protocol, not TCP or HTTP or...](/questions/55122/capturing-with-airpcap-and-seeing-only-80211-protocol-not-tcp-or-http-or)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55122-score" class="post-score" title="current number of votes">0</div><span id="post-55122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a new laptop which i downloaded Wireshark 2.05 to and i have my AirPcap cards. Although when i perform a capture i only receive 802.11 traffic in the protocol list. Why am i not capturing TCP, HTTP, etc? and how do i remedy this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '16, 22:34</strong></p><img src="https://secure.gravatar.com/avatar/b991d1c061a8d97973cd71b4da380a8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blackwater&#39;s gravatar image" /><p><span>blackwater</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blackwater has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Aug '16, 20:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-55122" class="comments-container"></div><div id="comment-tools-55122" class="comment-tools"></div><div class="clear"></div><div id="comment-55122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55142"></span>

<div id="answer-container-55142" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55142-score" class="post-score" title="current number of votes">0</div><span id="post-55142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are many possible root causes - from insufficient hardware to software configuration. WiFi sniffing is hard. The remedy will depend on the root cause and your description is not sufficient to determine root cause. Since you are using an AirPcap, monitor+promiscuous mode should work, so that's likely not the issue. I'll guess that the issue is that the data packets are encrypted, but that is only a guess.</p><p>This is a common issue - have you searched here or used google? Some links for you to get started:</p><ul><li><a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a></li><li><a href="https://ask.wireshark.org/questions/54433/why-cant-i-capture-data-packets-in-monitor-mode?page=1&amp;focusedAnswerId=54437#54437">https://ask.wireshark.org/questions/54433/why-cant-i-capture-data-packets-in-monitor-mode?page=1&amp;focusedAnswerId=54437#54437</a></li><li><a href="https://ask.wireshark.org/questions/54835/having-issues-capturing-http-traffic-on-my-network">https://ask.wireshark.org/questions/54835/having-issues-capturing-http-traffic-on-my-network</a></li><li><a href="https://ask.wireshark.org/questions/54790/capturing-data-in-monitor-mode?page=1&amp;focusedAnswerId=54791#54791">https://ask.wireshark.org/questions/54790/capturing-data-in-monitor-mode?page=1&amp;focusedAnswerId=54791#54791</a></li></ul><p>and plenty of others.</p><p>The quickest way for resolution is to post a publicly accessible trace file for the members here to review. That will help them know exactly what you are seeing, then can point you in the right direction.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '16, 12:04</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '16, 12:05</strong> </span></p></div></div><div id="comments-container-55142" class="comments-container"></div><div id="comment-tools-55142" class="comment-tools"></div><div class="clear"></div><div id="comment-55142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55154"></span>

<div id="answer-container-55154" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55154-score" class="post-score" title="current number of votes">0</div><span id="post-55154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Although when i perform a capture i only receive 802.11 traffic in the protocol list. Why am i not capturing TCP, HTTP, etc?</p></blockquote><p>Probably because you're capturing on a "protected" network, i.e. a network where traffic is encrypted with WEP or WPA/WPA2, which means that you'll only see higher-level protocols if the traffic can be decrypted.</p><p>That means you will need to provide the password for the network to Wireshark. See <a href="https://wiki.wireshark.org/HowToDecrypt802.11">the Wireshark Wiki's "How to decrypt 802.11" page</a> for information on how to do that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '16, 20:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-55154" class="comments-container"></div><div id="comment-tools-55154" class="comment-tools"></div><div class="clear"></div><div id="comment-55154-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

