+++
type = "question"
title = "&quot;http.host&quot; and &quot;http.request.full_uri&quot; filter"
description = '''I&#x27;m making a very minimalistic wireshark profile, so someone without much technical knowledge can get a quick overview of http and ssl/tls traffic (&quot;non-technical&quot; information). QUESTION 1 Right now I have the following columns; No. | Protocol | http.referer | http.host | Info | ssl.handshake.extens...'''
date = "2016-07-12T07:12:00Z"
lastmod = "2016-07-12T22:34:00Z"
weight = 54006
keywords = [ "columns", "display-filter" ]
aliases = [ "/questions/54006" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["http.host" and "http.request.full\_uri" filter](/questions/54006/httphost-and-httprequestfull_uri-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54006-score" class="post-score" title="current number of votes">0</div><span id="post-54006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm making a very minimalistic wireshark profile, so someone without much technical knowledge can get a quick overview of http and ssl/tls traffic ("non-technical" information).</p><p><strong>QUESTION 1</strong></p><p>Right now I have the following columns;</p><pre><code>No. | Protocol | http.referer | http.host | Info | ssl.handshake.extensions_server_name | http.request.full_uri</code></pre><p>My question is, does the last filter (http.request.full_uri) always show the host that is also displayed with the http.host filter?</p><p>Or is/can there be a difference between: "http.host" and "http.request.full_uri"? Otherwise I can just use the full_uri filter without the separate host filter.</p><p><strong>QUESTION 2</strong></p><p>Is the filter "ssl.handshake.extensions_server_name" the only one that shows some 'understandable' information about encrypted traffic? And what exactly is the role of this server name and why is this not encrypted?</p><p>Any other ideas about filters that show this "low-level" information is also appreciated.</p><p>Thanks! Danny</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '16, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/1bd7aa9ec4636e9d234ddfb63bb15f85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r00t070&#39;s gravatar image" /><p><span>r00t070</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r00t070 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jul '16, 08:14</strong> </span></p></div></div><div id="comments-container-54006" class="comments-container"></div><div id="comment-tools-54006" class="comment-tools"></div><div class="clear"></div><div id="comment-54006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54015"></span>

<div id="answer-container-54015" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54015-score" class="post-score" title="current number of votes">1</div><span id="post-54015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The http.request.full_uri field is the http.host field concatenated with the http.request.uri field, so yes, http.request.full_uri will always show the same host as the http.host field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '16, 22:34</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-54015" class="comments-container"></div><div id="comment-tools-54015" class="comment-tools"></div><div class="clear"></div><div id="comment-54015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

