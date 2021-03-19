+++
type = "question"
title = "How to capture HTTP data from WiFi devices?"
description = '''Hello guys, my network is configured like this Internet ------ Wireless Router -- (WiFi)-- Laptop and SmartPhone I want to run Wireshark on Laptop and capture HTTP packets from the SmartPhone sent to/from Internet. If I use monitor mode I can only capture 802.11 packtes, but no HTTP protocol. How ca...'''
date = "2014-11-06T10:05:00Z"
lastmod = "2014-11-07T15:28:00Z"
weight = 37625
keywords = [ "wifi", "wireshark" ]
aliases = [ "/questions/37625" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture HTTP data from WiFi devices?](/questions/37625/how-to-capture-http-data-from-wifi-devices)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37625-score" class="post-score" title="current number of votes">0</div><span id="post-37625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello guys,</p><p>my network is configured like this</p><p>Internet ------ Wireless Router -- (WiFi)-- Laptop and SmartPhone</p><p>I want to run Wireshark on Laptop and capture HTTP packets from the SmartPhone sent to/from Internet. If I use monitor mode I can only capture 802.11 packtes, but no HTTP protocol. How can I see it?</p><p>Thank you for the help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '14, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/d7d880f6c9de6da71e3fb9f8514b629a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stilozu&#39;s gravatar image" /><p><span>stilozu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stilozu has no accepted answers">0%</span></p></div></div><div id="comments-container-37625" class="comments-container"></div><div id="comment-tools-37625" class="comment-tools"></div><div class="clear"></div><div id="comment-37625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37674"></span>

<div id="answer-container-37674" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37674-score" class="post-score" title="current number of votes">0</div><span id="post-37674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You're probably capturing on a "protected" network, using WEP or WPA/WPA2, so you'll have to provide the password for the network to Wireshark and, if it's using WPA/WPA2, capture the initial handshake between the phone and the access point, which means you may have to turn the phone off, start Wireshark, and then turn the phone on again. See <a href="http://wiki.wireshark.org/HowToDecrypt802.11">the "How to decrypt 802.11" page in the Wireshark Wiki</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '14, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-37674" class="comments-container"></div><div id="comment-tools-37674" class="comment-tools"></div><div class="clear"></div><div id="comment-37674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

