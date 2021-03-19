+++
type = "question"
title = "display filter to catch HTTP requests that don&#x27;t have &quot;Referer&quot; header"
description = '''I need to find all the HTTP requests that don&#x27;t have &quot;Referer&quot; header.  I tried the following but it didn&#x27;t catch such a HTTP request. http.referer == &quot;&quot;  Wonder if there is a display filter for it. Thanks. '''
date = "2015-06-03T20:26:00Z"
lastmod = "2015-06-04T06:35:00Z"
weight = 42865
keywords = [ "wireshark" ]
aliases = [ "/questions/42865" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [display filter to catch HTTP requests that don't have "Referer" header](/questions/42865/display-filter-to-catch-http-requests-that-dont-have-referer-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42865-score" class="post-score" title="current number of votes">0</div><span id="post-42865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to find all the HTTP requests that don't have "Referer" header. I tried the following but it didn't catch such a HTTP request.</p><pre><code>http.referer == &quot;&quot;</code></pre><p>Wonder if there is a display filter for it.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '15, 20:26</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-42865" class="comments-container"></div><div id="comment-tools-42865" class="comment-tools"></div><div class="clear"></div><div id="comment-42865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42870"></span>

<div id="answer-container-42870" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42870-score" class="post-score" title="current number of votes">2</div><span id="post-42870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your headline translates to the following display filter.</p><pre><code>http.request == 1 and !http.referer</code></pre><p>Does this do what you want ?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '15, 22:19</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-42870" class="comments-container"><span id="42885"></span><div id="comment-42885" class="comment"><div id="post-42885-score" class="comment-score"></div><div class="comment-text"><p>Yes, it works great. Thanks!</p></div><div id="comment-42885-info" class="comment-info"><span class="comment-age">(04 Jun '15, 06:35)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-42870" class="comment-tools"></div><div class="clear"></div><div id="comment-42870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

