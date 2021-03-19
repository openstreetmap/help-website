+++
type = "question"
title = "4-Bytes Extra between LLC and 802.11 header"
description = '''Hi,   I am analyzing a 802.11n network with various tools using AirPcap Nx cards. In all cases i am seeing 4 extra bytes between LLC-Snap and IEEE-802.11 headers. Most of the tools are failing to recognize traffic properly. wireshark and com-view recognize these 4 extra bytes as LLC header but you c...'''
date = "2012-03-02T14:09:00Z"
lastmod = "2012-03-02T16:32:00Z"
weight = 9317
keywords = [ "airpcap" ]
aliases = [ "/questions/9317" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [4-Bytes Extra between LLC and 802.11 header](/questions/9317/4-bytes-extra-between-llc-and-80211-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9317-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,<br />
</p><p>I am analyzing a 802.11n network with various tools using AirPcap Nx cards. In all cases i am seeing 4 extra bytes between LLC-Snap and IEEE-802.11 headers. Most of the tools are failing to recognize traffic properly. wireshark and com-view recognize these 4 extra bytes as LLC header but you can see the Snap header in raw view. Is there any proper header that can be expected in that place. I was not able to find any thing in the web. The network is running fine.</p></div><div id="question-tags" class="tags-container tags">airpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '12, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/cb9f80abceeb0378e69773bf651f6798?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseemdomaini&#39;s gravatar image" /><p>aseemdomaini<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseemdomaini has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-9317" class="comments-container"></div><div id="comment-tools-9317" class="comment-tools"></div><div class="clear"></div><div id="comment-9317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9320"></span>

<div id="answer-container-9320" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9320-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark might be incorrectly parsing the 802.11 header - it might not be properly recognizing the 802.11n HT Control field, which is 4 bytes long, at the end of the header.</p><p>Could you file a bug at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a> on this, and, if possible, attach one of the captures where you're seeing the problem, so that we can see if that's the problem and, if so, test a fix and, if not, see what else the problem might be?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '12, 16:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9320" class="comments-container"></div><div id="comment-tools-9320" class="comment-tools"></div><div class="clear"></div><div id="comment-9320-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

