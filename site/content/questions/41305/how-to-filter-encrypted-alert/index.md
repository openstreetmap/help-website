+++
type = "question"
title = "How to filter &quot;encrypted alert&quot; ?"
description = '''is there any filter expression?'''
date = "2015-04-08T17:32:00Z"
lastmod = "2015-04-09T13:16:00Z"
weight = 41305
keywords = [ "encrypted", "alert" ]
aliases = [ "/questions/41305" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter "encrypted alert" ?](/questions/41305/how-to-filter-encrypted-alert)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41305-score" class="post-score" title="current number of votes">0</div><span id="post-41305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>is there any filter expression?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encrypted" rel="tag" title="see questions tagged &#39;encrypted&#39;">encrypted</span> <span class="post-tag tag-link-alert" rel="tag" title="see questions tagged &#39;alert&#39;">alert</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '15, 17:32</strong></p><img src="https://secure.gravatar.com/avatar/bc5ed1bdefceb1ba8ec1704ca17848f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoho&#39;s gravatar image" /><p><span>hoho</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoho has no accepted answers">0%</span></p></div></div><div id="comments-container-41305" class="comments-container"><span id="41308"></span><div id="comment-41308" class="comment"><div id="post-41308-score" class="comment-score"></div><div class="comment-text"><p>ssl.alert_message should work??</p></div><div id="comment-41308-info" class="comment-info"><span class="comment-age">(08 Apr '15, 22:44)</span> <span class="comment-user userinfo">koundi</span></div></div></div><div id="comment-tools-41305" class="comment-tools"></div><div class="clear"></div><div id="comment-41305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41333"></span>

<div id="answer-container-41333" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41333-score" class="post-score" title="current number of votes">2</div><span id="post-41333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If wireshark already knows that the traffic is ssl protocol then<br />
</p><pre><code>ssl.record.length &gt; 2 and ssl.record.content_type == 21</code></pre><p>should do the trick, given that other alerts are only 2 bytes long<br />
A more generic filter should be<br />
</p><pre><code>tcp.len&gt;7 and ((tcp[12,20:2]==50:1503 and tcp[22]&lt;=3)||(tcp[12,32:2]==80:1503 and tcp[34]&lt;=3))</code></pre><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '15, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-41333" class="comments-container"></div><div id="comment-tools-41333" class="comment-tools"></div><div class="clear"></div><div id="comment-41333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

