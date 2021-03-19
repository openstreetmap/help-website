+++
type = "question"
title = "What am I looking at?"
description = '''Trying to learn what I am looking at in wireshark. Clicked statistics and the endpoints after a capture. Under the Ethernet 10, the first node is listed as Dell_70:4b:cf. This confused me as I own nothing I am aware of that was manufactured by Dell. Does this represent equipment? Or something else?'''
date = "2012-03-02T13:46:00Z"
lastmod = "2012-03-02T15:17:00Z"
weight = 9316
keywords = [ "ethernet", "statistics", "endpoints" ]
aliases = [ "/questions/9316" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What am I looking at?](/questions/9316/what-am-i-looking-at)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9316-score" class="post-score" title="current number of votes">0</div><span id="post-9316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to learn what I am looking at in wireshark. Clicked statistics and the endpoints after a capture. Under the Ethernet 10, the first node is listed as Dell_70:4b:cf. This confused me as I own nothing I am aware of that was manufactured by Dell. Does this represent equipment? Or something else?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-endpoints" rel="tag" title="see questions tagged &#39;endpoints&#39;">endpoints</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '12, 13:46</strong></p><img src="https://secure.gravatar.com/avatar/212bc33370d2b74e6aae00616df03a71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mooneierah&#39;s gravatar image" /><p><span>mooneierah</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mooneierah has no accepted answers">0%</span></p></div></div><div id="comments-container-9316" class="comments-container"></div><div id="comment-tools-9316" class="comment-tools"></div><div class="clear"></div><div id="comment-9316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9318"></span>

<div id="answer-container-9318" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9318-score" class="post-score" title="current number of votes">1</div><span id="post-9318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's the network adapter. The first three bytes of the MAC address are the Organizational Unit Identifier (OUI) and identify the manufacturer of the network adapter. You have MAC address name resolution turned on, so Wireshark is translating the OUI to a friendly name. That device may not be a Dell computer, but it has a Dell NIC.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '12, 15:17</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-9318" class="comments-container"></div><div id="comment-tools-9318" class="comment-tools"></div><div class="clear"></div><div id="comment-9318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

