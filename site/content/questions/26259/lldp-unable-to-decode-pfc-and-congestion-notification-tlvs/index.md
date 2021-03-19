+++
type = "question"
title = "LLDP unable to decode PFC and Congestion Notification TLV&#x27;s"
description = '''Hello all, I am currently running the latest release for Wireshark Version 1.10.2. My problem is both the PFC TLV and the Congestion Notification TLV are not properly decoded e.g. I am seeing unknown subtype 0xb and 0x8 respectively and as a result there is configuration present in either TLV.'''
date = "2013-10-21T12:59:00Z"
lastmod = "2014-04-28T01:42:00Z"
weight = 26259
keywords = [ "lldp" ]
aliases = [ "/questions/26259" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [LLDP unable to decode PFC and Congestion Notification TLV's](/questions/26259/lldp-unable-to-decode-pfc-and-congestion-notification-tlvs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26259-score" class="post-score" title="current number of votes">0</div><span id="post-26259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I am currently running the latest release for Wireshark Version 1.10.2.</p><p>My problem is both the PFC TLV and the Congestion Notification TLV are not properly decoded e.g.</p><p>I am seeing unknown subtype 0xb and 0x8 respectively and as a result there is configuration present in either TLV.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lldp" rel="tag" title="see questions tagged &#39;lldp&#39;">lldp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '13, 12:59</strong></p><img src="https://secure.gravatar.com/avatar/7eeef0ae5b53153c1ffad2943779e320?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MKelly765&#39;s gravatar image" /><p><span>MKelly765</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MKelly765 has no accepted answers">0%</span></p></div></div><div id="comments-container-26259" class="comments-container"></div><div id="comment-tools-26259" class="comment-tools"></div><div class="clear"></div><div id="comment-26259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32234"></span>

<div id="answer-container-32234" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32234-score" class="post-score" title="current number of votes">0</div><span id="post-32234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I just added in the code to support CEE &amp; IEEE DCBx TLVs,</p><p><a href="https://code.wireshark.org/review/#/c/1330/">https://code.wireshark.org/review/#/c/1330/</a> <a href="https://code.wireshark.org/review/#/c/1403">https://code.wireshark.org/review/#/c/1403</a> though there is no support for congestion notification yet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '14, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/dc3e259591231b8a47bb84f568e6ebdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anishbhatt&#39;s gravatar image" /><p><span>anishbhatt</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anishbhatt has no accepted answers">0%</span></p></div></div><div id="comments-container-32234" class="comments-container"></div><div id="comment-tools-32234" class="comment-tools"></div><div class="clear"></div><div id="comment-32234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

