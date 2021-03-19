+++
type = "question"
title = "How can I filter by website names?"
description = '''How can I filter capture by website names? I would like to filter capture by source or destination website contains function and/or exact name. Thank you, Ron'''
date = "2014-06-18T12:21:00Z"
lastmod = "2014-06-20T11:20:00Z"
weight = 33938
keywords = [ "capture", "websites" ]
aliases = [ "/questions/33938" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I filter by website names?](/questions/33938/how-can-i-filter-by-website-names)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33938-score" class="post-score" title="current number of votes">0</div><span id="post-33938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I filter capture by website names? I would like to filter capture by source or destination website contains function and/or exact name. Thank you, Ron</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-websites" rel="tag" title="see questions tagged &#39;websites&#39;">websites</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '14, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/646736825e4e344b647df8154466a4c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ronmaagero&#39;s gravatar image" /><p><span>ronmaagero</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ronmaagero has no accepted answers">0%</span></p></div></div><div id="comments-container-33938" class="comments-container"></div><div id="comment-tools-33938" class="comment-tools"></div><div class="clear"></div><div id="comment-33938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33939"></span>

<div id="answer-container-33939" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33939-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33939-score" class="post-score" title="current number of votes">0</div><span id="post-33939-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ronmaagero has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can apply the following display filters to the captured traffic:</p><p>http.host=="<em>exact.name.here</em>"</p><p>http.host contains "<em>partial.name.here</em>"</p><p>Both of those filters are case-sensitive. You can also do a case-insensitive search using the "matches" display filter operator with the regular expressions "(?i)" operator, but you will have to either escape any periods or make them a character class:</p><p>http.host matches "(?i)web\.site\.name"</p><p>http.host matches "(?i) web[.]site[.]name"</p><p>The "(?i)" regular expression operator makes the search case-insensitive.</p><p>The http.host field exists in HTTP request packets and contains the name of the web site that was requested. Keep in mind that we can have shared hosting, so we can't tell from the IP address alone what web site a user was browsing to.</p><p>An HTTP response does not contain an equivalent field, so you can't tell from the response packets alone what web site the response was from.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '14, 13:56</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-33939" class="comments-container"><span id="33997"></span><div id="comment-33997" class="comment"><div id="post-33997-score" class="comment-score"></div><div class="comment-text"><p>Jim, Thank You so much for the quick response. Ron Maagero</p></div><div id="comment-33997-info" class="comment-info"><span class="comment-age">(20 Jun '14, 11:20)</span> <span class="comment-user userinfo">ronmaagero</span></div></div></div><div id="comment-tools-33939" class="comment-tools"></div><div class="clear"></div><div id="comment-33939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

