+++
type = "question"
title = "Why can&#x27;t I capture 802.11n data packets?"
description = '''I have two ralink wireless cards (2860) with 802.11a/b/g/n support. I have put these (2 computers) in adhoc mode. I have an atheros (ath9k) wireless card which is in monitor mode listening in the same channel as adhoc network. I can see beacon and acknowledgements getting exchanged, but I am not abl...'''
date = "2012-01-24T13:06:00Z"
lastmod = "2012-10-06T18:05:00Z"
weight = 8587
keywords = [ "wireless", "802.11n", "802.11", "capture-setup" ]
aliases = [ "/questions/8587" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why can't I capture 802.11n data packets?](/questions/8587/why-cant-i-capture-80211n-data-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8587-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two ralink wireless cards (2860) with 802.11a/b/g/n support. I have put these (2 computers) in adhoc mode. I have an atheros (ath9k) wireless card which is in monitor mode listening in the same channel as adhoc network. I can see beacon and acknowledgements getting exchanged, but I am not able to see data packets which are being exchanged in Wireshark. Is there any special configuration that needs to done to capture data packets?</p></div><div id="question-tags" class="tags-container tags">wireless 802.11n 802.11 capture-setup</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '12, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/77672857cadc91c90a6c8e61f8913033?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shashankks&#39;s gravatar image" /><p>shashankks<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shashankks has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jan '12, 13:57</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8587" class="comments-container"></div><div id="comment-tools-8587" class="comment-tools"></div><div class="clear"></div><div id="comment-8587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14750"></span>

<div id="answer-container-14750" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14750-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does "not able to see data packets" mean "your capture has no packets where the IEEE 802.11 header says it's a data packet" or does it mean "your capture has packets where the IEEE 802.11 header says it's a data packet but they're just decoded as IEEE 802.11 packets - not TCP, not UDP, not ARP, etc."?</p><p>If it's the latter, then see my answer to <a href="http://ask.wireshark.org/questions/14684/no-data-packets-when-turning-on-monitor-mode">this question</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '12, 18:05</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-14750" class="comments-container"></div><div id="comment-tools-14750" class="comment-tools"></div><div class="clear"></div><div id="comment-14750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

