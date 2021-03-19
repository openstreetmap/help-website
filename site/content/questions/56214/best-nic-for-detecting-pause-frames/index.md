+++
type = "question"
title = "Best NIC for detecting Pause Frames"
description = '''We would like to have a foolproof method of detecting pause frames. Now we knwo this is problematic because most mirror port switches terminate Pause frames as do most detecting NIC&#x27;s. However we have network tap so the switch issue is not a problem, the question is how do we get the Pause frame pas...'''
date = "2016-10-07T02:04:00Z"
lastmod = "2016-10-07T06:28:00Z"
weight = 56214
keywords = [ "frame", "pause", "usb" ]
aliases = [ "/questions/56214" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Best NIC for detecting Pause Frames](/questions/56214/best-nic-for-detecting-pause-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56214-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We would like to have a foolproof method of detecting pause frames.</p><p>Now we knwo this is problematic because most mirror port switches terminate Pause frames as do most detecting NIC's.</p><p>However we have network tap so the switch issue is not a problem, the question is how do we get the Pause frame past the detecting NIC?</p><p>Because of security issues, we would like to do this on a independent network, so are there any USB ethernet adaptors that can be adapted to pass pause frames through? In fact what is the best USB ethernet adapter for use with Wireshark</p></div><div id="question-tags" class="tags-container tags">frame pause usb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '16, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/d4231bdb4652613577d419e9c1d86cf9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hammarbytp&#39;s gravatar image" /><p>hammarbytp<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hammarbytp has no accepted answers">0%</span></p></div></div><div id="comments-container-56214" class="comments-container"></div><div id="comment-tools-56214" class="comment-tools"></div><div class="clear"></div><div id="comment-56214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56221"></span>

<div id="answer-container-56221" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56221-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have used this to collect pause frames in the past:</p><p><a href="http://www.hilscher.com/en/products/product-groups/analysis-and-data-acquisition/ethernet-analysis/nanl-b500g-re/">http://www.hilscher.com/en/products/product-groups/analysis-and-data-acquisition/ethernet-analysis/nanl-b500g-re/</a></p><p>This stores the captures in memory and then you download, so the problem you have identified does not exist. Another option that I have used that addresses your specific issue is to use certain Intel chipsets on Linux (newer kernels, I forget the cut-in date). They have some options to allow passing up the FCS and all received frames. To show options:</p><p>ethtool -k &lt;interface&gt;</p><p>Where I would set the featurs:</p><p>rx-fcs: off [fixed]</p><p>rx-all: off</p><p>I can't find a trace to prove that I did it, but I recall that it worked. If you run into trouble I can set it up again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '16, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-56221" class="comments-container"></div><div id="comment-tools-56221" class="comment-tools"></div><div class="clear"></div><div id="comment-56221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

