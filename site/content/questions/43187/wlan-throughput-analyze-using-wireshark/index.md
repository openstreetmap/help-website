+++
type = "question"
title = "WLAN throughput analyze using wireshark"
description = '''what are all the things need to check in wireshark log if my WLAN throughput is reduced than normal rate.'''
date = "2015-06-15T08:25:00Z"
lastmod = "2015-06-15T10:45:00Z"
weight = 43187
keywords = [ "802.11", "wifi", "wlan", "802.11n" ]
aliases = [ "/questions/43187" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WLAN throughput analyze using wireshark](/questions/43187/wlan-throughput-analyze-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43187-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>what are all the things need to check in wireshark log if my WLAN throughput is reduced than normal rate.</p></div><div id="question-tags" class="tags-container tags">802.11 wifi wlan 802.11n</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '15, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/c129ee92284298a5443505b3f6310e60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Deva%20Nathan&#39;s gravatar image" /><p>Deva Nathan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Deva Nathan has no accepted answers">0%</span></p></div></div><div id="comments-container-43187" class="comments-container"><span id="43188"></span><div id="comment-43188" class="comment"><div id="post-43188-score" class="comment-score"></div><div class="comment-text"><p>Are you asking about how to find the user throughput or the connection data rate to the WLAN?</p></div><div id="comment-43188-info" class="comment-info"><span class="comment-age">(15 Jun '15, 08:54)</span> Amato_C</div></div></div><div id="comment-tools-43187" class="comment-tools"></div><div class="clear"></div><div id="comment-43187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43196"></span>

<div id="answer-container-43196" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43196-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are lots of things you could look at. But in Wireshark, I would start with Layer 3 Retries.</p><p>Display filter; "<code>wlan.fc.retry == 1</code>" You want this to be less than 10%, the lower the better.</p><p>Of course don't forget the WLAN basics; Signal Strength S/N Ratio Interference / Noise Data rates</p><p>Also look out for Dissociation / Deauthentication. Someone may be bumping you off your network!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '15, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/e4a81395f6649e064887d7f57ee653eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chillypenguin&#39;s gravatar image" /><p>chillypenguin<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chillypenguin has one accepted answer">25%</span></p></div></div><div id="comments-container-43196" class="comments-container"></div><div id="comment-tools-43196" class="comment-tools"></div><div class="clear"></div><div id="comment-43196-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

