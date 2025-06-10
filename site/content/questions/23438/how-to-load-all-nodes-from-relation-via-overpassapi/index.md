+++
type = "question"
title = "How to load all Nodes from Relation via OverpassAPI"
description = '''Hi there. Can anyone tell me how to get all nodes from a relation by rel-id?'''
date = "2013-06-17T08:39:00Z"
lastmod = "2013-06-18T07:05:00Z"
weight = 23438
keywords = [ "overpass", "relation" ]
aliases = [ "/questions/23438" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to load all Nodes from Relation via OverpassAPI](/questions/23438/how-to-load-all-nodes-from-relation-via-overpassapi)

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
<span id="post-23438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23438-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-23438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there. Can anyone tell me how to get all nodes from a relation by rel-id?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jun '13, 08:39</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef3a3c25492438c9f0e5a548a36fa07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ogmios&#39;s gravatar image" />
<p><span>Ogmios</span><br />
<span class="score" title="766 reputation points">766</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ogmios has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-23438" class="comments-container">
<span id="23447"></span>
<div id="comment-23447" class="comment">
<div id="post-23447-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Do you mean nodes directly in the relation, or all nodes recursively (the nodes in ways and relations that are member of the relation you want to fetch).</p>
</div>
<div id="comment-23447-info" class="comment-info">
<span class="comment-age">(17 Jun '13, 09:47)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="23467"></span>
<div id="comment-23467" class="comment">
<div id="post-23467-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nodes directly in the relation</p>
</div>
<div id="comment-23467-info" class="comment-info">
<span class="comment-age">(17 Jun '13, 22:09)</span> <span class="comment-user userinfo">Ogmios</span>
</div>
</div>
</div>
<div id="comment-tools-23438" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23438-form-container" class="comment-form-container">
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

<span id="23474"></span>

<div id="answer-container-23474" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23474-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-23474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please try</p>
<pre><code>rel(ID_OF_RELATION);node(r);out meta;</code></pre>
<p>An <a href="http://overpass-turbo.eu/s/n3">example</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '13, 07:05</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-23474" class="comments-container">
&#10;</div>
<div id="comment-tools-23474" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23474-form-container" class="comment-form-container">
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

