+++
type = "question"
title = "Nominatim returns only if query exactly matched data"
description = '''Hi to all, In nominatim, we need to give exact query(string) which are stored in DB.  For example We can get data when search as &quot;guduvancheri&quot;, but cant get data when searching as &quot;guduvanchery&quot; or searching as &quot;guduvancher&quot;. How to fix these type of issues?'''
date = "2015-11-19T14:20:00Z"
lastmod = "2015-11-19T16:40:00Z"
weight = 46713
keywords = [ "openstreetmap", "query", "search", "nominatim", "data" ]
aliases = [ "/questions/46713" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim returns only if query exactly matched data](/questions/46713/nominatim-returns-only-if-query-exactly-matched-data)

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
<span id="post-46713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46713-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all, In nominatim, we need to give exact query(string) which are stored in DB. For example We can get data when search as "guduvancheri", but cant get data when searching as "guduvanchery" or searching as "guduvancher". How to fix these type of issues?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '15, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Nov '15, 14:20</strong> </span></p>
</div>
</div>
<div id="comments-container-46713" class="comments-container">
&#10;</div>
<div id="comment-tools-46713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46713-form-container" class="comment-form-container">
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

<span id="46716"></span>

<div id="answer-container-46716" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46716-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim does not support similarity searches. You might want to look at Photon (<a href="https://github.com/komoot/photon">https://github.com/komoot/photon</a>) which feeds off the Nominatim index and claims to have "typo tolerance":</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '15, 15:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Nov '15, 15:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-46716" class="comments-container">
<span id="46719"></span>
<div id="comment-46719" class="comment">
<div id="post-46719-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>... or see <a href="https://wiki.openstreetmap.org/wiki/Search_engines">https://wiki.openstreetmap.org/wiki/Search_engines</a> where you have at least "Pelias" as another solution.</p>
</div>
<div id="comment-46719-info" class="comment-info">
<span class="comment-age">(19 Nov '15, 16:40)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-46716" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46716-form-container" class="comment-form-container">
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

