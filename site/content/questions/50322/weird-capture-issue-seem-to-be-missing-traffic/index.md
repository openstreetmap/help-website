+++
type = "question"
title = "Weird capture issue - seem to be missing traffic"
description = '''Hi guys I&#x27;ve got a customer running wireshark with what should be a fairly basic set of filters, being: net 10.33.57 and not udp portrange 2530-2550 and not tcp port 445  What&#x27;s really weird, is that for anything outside the 10.33.57 vlan, we&#x27;re only seeing incoming traffic, not outgoing. I&#x27;ve rolle...'''
date = "2016-02-18T20:51:00Z"
lastmod = "2016-05-02T16:33:00Z"
weight = 50322
keywords = [ "capture", "capture-filter", "tshark" ]
aliases = [ "/questions/50322" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Weird capture issue - seem to be missing traffic](/questions/50322/weird-capture-issue-seem-to-be-missing-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50322-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys I've got a customer running wireshark with what should be a fairly basic set of filters, being:</p><pre><code>net 10.33.57 and not udp portrange 2530-2550 and not tcp port 445</code></pre><p>What's really weird, is that for anything outside the 10.33.57 vlan, we're only seeing incoming traffic, not outgoing.<img src="https://osqa-ask.wireshark.org/upfiles/quantel-mozart-quantelvlan_00004_20160219151452.pcap_%5BWireshark_1.12.5_(Git_R_2016-02-19_15-31-17.png" alt="alt text" /></p><p>I've rolled back to a much earlier version of code, but that seems to make no difference. We have had the same issue occur with using the host directive, but can't quite work out why. I'm waiting for confirmation of the software version that the customer is running, but we were previously running 1.12 and have recently updated to v2 dev release across the board.</p></div><div id="question-tags" class="tags-container tags">capture capture-filter tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '16, 20:51</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p>Scott Harman<br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span></p></img></div></div><div id="comments-container-50322" class="comments-container"></div><div id="comment-tools-50322" class="comment-tools"></div><div class="clear"></div><div id="comment-50322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52163"></span>

<div id="answer-container-52163" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52163-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Span to capture VLAN traffic was incorrectly configured</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '16, 16:33</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p>Scott Harman<br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span></p></div></div><div id="comments-container-52163" class="comments-container"></div><div id="comment-tools-52163" class="comment-tools"></div><div class="clear"></div><div id="comment-52163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

