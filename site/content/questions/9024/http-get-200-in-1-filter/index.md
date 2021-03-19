+++
type = "question"
title = "HTTP GET &amp; 200 in 1 filter"
description = '''Trying this filter but getting error msg, any idea how can I put GET and 200 in 1 filter. http.request.method == &quot;GET&quot; and http.response.code == 200 Thank you'''
date = "2012-02-15T08:12:00Z"
lastmod = "2012-02-15T08:26:00Z"
weight = 9024
keywords = [ "http" ]
aliases = [ "/questions/9024" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP GET & 200 in 1 filter](/questions/9024/http-get-200-in-1-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9024-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying this filter but getting error msg, any idea how can I put GET and 200 in 1 filter. http.request.method == "GET" and http.response.code == 200</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '12, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/742ef72410cbfe5b1faa604d3a1bc44d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ezat&#39;s gravatar image" /><p>Ezat<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ezat has no accepted answers">0%</span></p></div></div><div id="comments-container-9024" class="comments-container"><span id="9025"></span><div id="comment-9025" class="comment"><div id="post-9025-score" class="comment-score"></div><div class="comment-text"><p>Sorry guys I found it in Sake respond to 1 of the questions in HTTP tad as follows. http and (http.request.method == "GET" || http.response.code == 200)</p><p>Thanks again</p></div><div id="comment-9025-info" class="comment-info"><span class="comment-age">(15 Feb '12, 08:18)</span> Ezat</div></div></div><div id="comment-tools-9024" class="comment-tools"></div><div class="clear"></div><div id="comment-9024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9027"></span>

<div id="answer-container-9027" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9027-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>those are 2 different packets, so you should use an 'or' instead of an' and' ie http.request.method == "GET" or http.response.code == 200</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '12, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/dbc4d8cb6be85bd586ca4bf211e1337c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thetechfirm&#39;s gravatar image" /><p>thetechfirm<br />
<span class="score" title="64 reputation points">64</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thetechfirm has no accepted answers">0%</span></p></div></div><div id="comments-container-9027" class="comments-container"></div><div id="comment-tools-9027" class="comment-tools"></div><div class="clear"></div><div id="comment-9027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

