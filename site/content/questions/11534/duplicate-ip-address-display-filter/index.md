+++
type = "question"
title = "duplicate IP address display filter"
description = '''In expert info, I have found two warnings about duplicate IP addresses. Ofcourse, the customer thinks I&#x27;m crazy (&quot;Not on my network!&quot;) so I took some screenshots showing his this. The only way I was able to show him both in the same screen was to build the filter using the &quot;or&quot; for both IP address w...'''
date = "2012-06-01T08:30:00Z"
lastmod = "2012-06-01T13:27:00Z"
weight = 11534
keywords = [ "filter", "duplicate" ]
aliases = [ "/questions/11534" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [duplicate IP address display filter](/questions/11534/duplicate-ip-address-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11534-score" class="post-score" title="current number of votes">0</div><span id="post-11534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In expert info, I have found two warnings about duplicate IP addresses. Ofcourse, the customer thinks I'm crazy ("Not on my network!") so I took some screenshots showing his this. The only way I was able to show him both in the same screen was to build the filter using the "or" for both IP address warns. expert.message == "Duplicate IP address configured (192.168.0.23)"</p><p>Is there a way to create the filter just on duplicates in general without having to spell each IP out?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '12, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p><span>EricKnaus</span><br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div></div><div id="comments-container-11534" class="comments-container"></div><div id="comment-tools-11534" class="comment-tools"></div><div class="clear"></div><div id="comment-11534-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11535"></span>

<div id="answer-container-11535" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11535-score" class="post-score" title="current number of votes">0</div><span id="post-11535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="EricKnaus has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes. Use the "contains" operator to match the part of the expert info message that doesn't have the IP address. Try this display filter:</p><p>expert.message contains "Duplicate IP address"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '12, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-11535" class="comments-container"><span id="11548"></span><div id="comment-11548" class="comment"><div id="post-11548-score" class="comment-score"></div><div class="comment-text"><p>Jim - Thanks!</p></div><div id="comment-11548-info" class="comment-info"><span class="comment-age">(01 Jun '12, 13:27)</span> <span class="comment-user userinfo">EricKnaus</span></div></div></div><div id="comment-tools-11535" class="comment-tools"></div><div class="clear"></div><div id="comment-11535-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

