+++
type = "question"
title = "How can i select all information inside a BBox with the least possible amount that is outside"
description = '''Hi, i really want to get the Data that is inside a BBox but the least count possible that is NOT inside. ATM I&#x27;am using something like: (relation(south,west,north,east);way(south,west,north,east);node(south,west,north,east););( ._; &amp;gt;; );out meta;  It returns everything that is inside but way too ...'''
date = "2018-01-30T17:22:00Z"
lastmod = "2018-02-21T12:37:00Z"
weight = 61906
keywords = [ "overpass-ql" ]
aliases = [ "/questions/61906" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can i select all information inside a BBox with the least possible amount that is outside](/questions/61906/how-can-i-select-all-information-inside-a-bbox-with-the-least-possible-amount-that-is-outside)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61906-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, i really want to get the Data that is inside a BBox but the least count possible that is NOT inside. ATM I'am using something like:</p>
<pre><code>(relation(south,west,north,east);way(south,west,north,east);node(south,west,north,east););( ._; &gt;; );out meta;</code></pre>
<p>It returns everything that is inside but way too much that i don't need. Is there a fast way to reduce this select to those entries that are (mostly) only inside the Bbox?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '18, 17:22</strong></p>
<img src="https://secure.gravatar.com/avatar/b8c76fe328ec182149b4cb8c7e413b88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xep84&#39;s gravatar image" />
<p><span>xep84</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xep84 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61906" class="comments-container">
<span id="62248"></span>
<div id="comment-62248" class="comment">
<div id="post-62248-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes and thanks.</p>
</div>
<div id="comment-62248-info" class="comment-info">
<span class="comment-age">(21 Feb '18, 12:37)</span> <span class="comment-user userinfo">xep84</span>
</div>
</div>
</div>
<div id="comment-tools-61906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61906-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61908"></span>

<div id="answer-container-61908" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61908-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-61908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>are you referring to objects that are only partially in your BBox, but are still returned completely ? AFAIK, OverPass cannot split objects and will return e.g. complete ways when they have at least 1 node in the BBox, even when all the others are not.</p>
<p>Thus you will have to do that yourself</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '18, 04:17</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-61908" class="comments-container">
&#10;</div>
<div id="comment-tools-61908" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61908-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

