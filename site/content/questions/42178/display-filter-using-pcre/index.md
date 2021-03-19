+++
type = "question"
title = "display filter using PCRE"
description = '''Wonder if it is possible to use regular expression in display filter, for example, I need to find all HTTP requests whose &quot;Host&quot; headers are followed by an IP address instead of host name.  Something like the following PCRE (not perfect, I know): Host: ([&#92;d&#92;.&#92;:]+)&#92;r&#92;n  Thanks.'''
date = "2015-05-07T06:43:00Z"
lastmod = "2015-05-07T08:42:00Z"
weight = 42178
keywords = [ "wireshark" ]
aliases = [ "/questions/42178" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [display filter using PCRE](/questions/42178/display-filter-using-pcre)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42178-score" class="post-score" title="current number of votes">0</div><span id="post-42178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wonder if it is possible to use regular expression in display filter, for example, I need to find all HTTP requests whose "Host" headers are followed by an IP address instead of host name.</p><p>Something like the following PCRE (not perfect, I know):</p><pre><code>Host: ([\d\.\:]+)\r\n</code></pre><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '15, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-42178" class="comments-container"></div><div id="comment-tools-42178" class="comment-tools"></div><div class="clear"></div><div id="comment-42178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42181"></span>

<div id="answer-container-42181" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42181-score" class="post-score" title="current number of votes">2</div><span id="post-42181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The "matches" operator offers PCRE matching. See the <a href="https://www.wireshark.org/docs/man-pages/wireshark-filter.html">filters man page</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '15, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-42181" class="comments-container"><span id="42188"></span><div id="comment-42188" class="comment"><div id="post-42188-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the tip. I used <code>http.host matches "^[\\d\\.\\:]+$" and tcp</code> and it worked well.</p></div><div id="comment-42188-info" class="comment-info"><span class="comment-age">(07 May '15, 08:42)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-42181" class="comment-tools"></div><div class="clear"></div><div id="comment-42181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

