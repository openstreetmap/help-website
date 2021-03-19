+++
type = "question"
title = "DHCP Request"
description = '''Dear Sir, I am allocating IP addr with DHCP Server to my clients with 300Sec a leased time... I understood renewal time = 50% * leased time, hence After 150 sec i am expecting request from clients to sever for renewal.... But when i captured traffic by wireshark, DHCP request interval from client is...'''
date = "2015-04-15T20:09:00Z"
lastmod = "2015-04-15T21:23:00Z"
weight = 41470
keywords = [ "dhcp" ]
aliases = [ "/questions/41470" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [DHCP Request](/questions/41470/dhcp-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41470-score" class="post-score" title="current number of votes">0</div><span id="post-41470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Sir,</p><p>I am allocating IP addr with DHCP Server to my clients with 300Sec a leased time...</p><p>I understood renewal time = 50% * leased time, hence After 150 sec i am expecting request from clients to sever for renewal....</p><p>But when i captured traffic by wireshark, DHCP request interval from client is not uniform and varying between 117sec to 147sec...</p><p>Why ? What could be the reason???</p><p>Regards M Srinivasa Rao</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '15, 20:09</strong></p><img src="https://secure.gravatar.com/avatar/ce1843f92a1c18db26bc79b3afa9bd50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srinu_bel&#39;s gravatar image" /><p><span>srinu_bel</span><br />
<span class="score" title="20 reputation points">20</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srinu_bel has no accepted answers">0%</span></p></div></div><div id="comments-container-41470" class="comments-container"></div><div id="comment-tools-41470" class="comment-tools"></div><div class="clear"></div><div id="comment-41470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41472"></span>

<div id="answer-container-41472" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41472-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41472-score" class="post-score" title="current number of votes">3</div><span id="post-41472-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See section 4.4.5, "Reacquisition and expiration," of <a href="http://tools.ietf.org/html/rfc2131">RFC 2131</a>, "Dynamic Host Configuration Protocol." Two times, T1 and T2, are defined. T1 is the renewal time. It defaults to 50% of the lease time, but the server can specify a different value.</p><p>The RFC gives two reasons why the client might try to renew its lease at times that are not exactly equal to T1:</p><ol><li>"Times T1 and T2 SHOULD be chosen with some random 'fuzz' around a fixed value, to avoid synchronization of client reacquisition."</li><li>"The client MAY choose to renew or extend its lease prior to T1."</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '15, 21:23</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Apr '15, 13:41</strong> </span></p></div></div><div id="comments-container-41472" class="comments-container"></div><div id="comment-tools-41472" class="comment-tools"></div><div class="clear"></div><div id="comment-41472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

