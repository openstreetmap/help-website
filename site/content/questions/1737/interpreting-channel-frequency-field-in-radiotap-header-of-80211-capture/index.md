+++
type = "question"
title = "Interpreting channel frequency field in Radiotap header of 802.11 capture"
description = '''I have an AirPCap capture. It shows the value 8509 in the channel frequency field of the Radiotap header. Wireshark also displays this as 2437 [channel BG 6]. My question is - how is this value of 8509 interpreted? How does 8509 translate to 2437? I have not found any related information on radiotap...'''
date = "2011-01-13T06:16:00Z"
lastmod = "2011-03-22T07:25:00Z"
weight = 1737
keywords = [ "802.11", "frequency", "radiotap" ]
aliases = [ "/questions/1737" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Interpreting channel frequency field in Radiotap header of 802.11 capture](/questions/1737/interpreting-channel-frequency-field-in-radiotap-header-of-80211-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1737-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an AirPCap capture. It shows the value 8509 in the channel frequency field of the Radiotap header. Wireshark also displays this as 2437 [channel BG 6].</p><p>My question is - how is this value of 8509 interpreted? How does 8509 translate to 2437? I have not found any related information on radiotap.org or other sources.</p><p>Thanks Manish</p></div><div id="question-tags" class="tags-container tags">802.11 frequency radiotap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '11, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/7643b72b28d9a17fe35bdfb3af219688?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="magrawal&#39;s gravatar image" /><p>magrawal<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="magrawal has no accepted answers">0%</span></p></div></div><div id="comments-container-1737" class="comments-container"></div><div id="comment-tools-1737" class="comment-tools"></div><div class="clear"></div><div id="comment-1737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3023"></span>

<div id="answer-container-3023" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3023-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The field is in little-endian format, so 0x8509 actually represents the hexadecimal value of 0x0985. Converting hexadecimal 0x0985 to decimal yields 2437.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '11, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3023" class="comments-container"></div><div id="comment-tools-3023" class="comment-tools"></div><div class="clear"></div><div id="comment-3023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

