+++
type = "question"
title = "Add new column value"
description = '''Hello, I would like to extract the value of a field and print it in a column (which is definitly shorter than look for the value into the packet). For instance I&#x27;d like to add a column named &quot;SGSN IP@&quot; which value is &quot;radius.3GPP_SGSN_Address&quot;. Do you know if this is already possible? Thank you'''
date = "2010-12-24T02:48:00Z"
lastmod = "2010-12-24T03:38:00Z"
weight = 1477
keywords = [ "columns" ]
aliases = [ "/questions/1477" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Add new column value](/questions/1477/add-new-column-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1477-score" class="post-score" title="current number of votes">1</div><span id="post-1477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I would like to extract the value of a field and print it in a column (which is definitly shorter than look for the value into the packet).</p><p>For instance I'd like to add a column named "SGSN <span class="__cf_email__" data-cfemail="41081101">[email protected]</span>" which value is "radius.3GPP_SGSN_Address".</p><p>Do you know if this is already possible?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Dec '10, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/b2f471d415d4d49330d7728fb95e840f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mxcarron&#39;s gravatar image" /><p><span>mxcarron</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mxcarron has no accepted answers">0%</span></p></div></div><div id="comments-container-1477" class="comments-container"></div><div id="comment-tools-1477" class="comment-tools"></div><div class="clear"></div><div id="comment-1477-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1479"></span>

<div id="answer-container-1479" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1479-score" class="post-score" title="current number of votes">3</div><span id="post-1479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Even easier in 1.4 of Wireshark is to find a frame containing the field, right click on the field in the packet details and select Display as Column</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '10, 03:38</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1479" class="comments-container"></div><div id="comment-tools-1479" class="comment-tools"></div><div class="clear"></div><div id="comment-1479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1478"></span>

<div id="answer-container-1478" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1478-score" class="post-score" title="current number of votes">2</div><span id="post-1478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I finally found it.</p><p>Go to : Edit &gt; Preferences &gt; Columns Then "add" a new column and select "custom" (This is what I missed at first) and add in my case : "radius.3GPP_SGSN_Address".</p><p>Hope this help :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '10, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/b2f471d415d4d49330d7728fb95e840f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mxcarron&#39;s gravatar image" /><p><span>mxcarron</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mxcarron has no accepted answers">0%</span></p></div></div><div id="comments-container-1478" class="comments-container"></div><div id="comment-tools-1478" class="comment-tools"></div><div class="clear"></div><div id="comment-1478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

