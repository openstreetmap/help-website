+++
type = "question"
title = "Super-relation best practice"
description = '''I need to reference the Bon Secour National Wildlife Refuge, which consists of several components:  http://www.openstreetmap.org/relation/2644324 http://www.openstreetmap.org/relation/2644325 http://www.openstreetmap.org/relation/2644326 http://www.openstreetmap.org/relation/2644327 http://www.opens...'''
date = "2017-04-12T00:47:00Z"
lastmod = "2017-04-12T21:50:00Z"
weight = 55575
keywords = [ "relations", "super-relations" ]
aliases = [ "/questions/55575" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Super-relation best practice](/questions/55575/super-relation-best-practice)

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
<span id="post-55575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55575-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-55575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to reference the <a href="https://en.wikipedia.org/wiki/Bon_Secour_National_Wildlife_Refuge">Bon Secour National Wildlife Refuge</a>, which consists of several components:</p>
<ol>
<li><a href="http://www.openstreetmap.org/relation/2644324">http://www.openstreetmap.org/relation/2644324</a></li>
<li><a href="http://www.openstreetmap.org/relation/2644325">http://www.openstreetmap.org/relation/2644325</a></li>
<li><a href="http://www.openstreetmap.org/relation/2644326">http://www.openstreetmap.org/relation/2644326</a></li>
<li><a href="http://www.openstreetmap.org/relation/2644327">http://www.openstreetmap.org/relation/2644327</a></li>
<li><a href="http://www.openstreetmap.org/node/359003045">http://www.openstreetmap.org/node/359003045</a></li>
</ol>
<p>I planned on creating a <a href="http://wiki.openstreetmap.org/wiki/Super-Relation">super-relation</a> to reference the relations defined, above, and then removing the node reference.</p>
<p>I therefore created super-relation: <a href="http://www.openstreetmap.org/relation/7152437">http://www.openstreetmap.org/relation/7152437</a></p>
<p>That super-relation is not, however, searchable in nominatim and the OSM web client does not highlight the underlying ways as one might expect. Consequently, I have not removed the node.</p>
<p>I would like to confirm that the super-relation node definition is acceptable and open this issue up to folks for recommendation*.</p>
<p>Thanks.</p>
<p>* e.g. remove the super-relation and associate the relation directly with the underlying ways - which could be argued loses topology information.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-super-relations" rel="tag" title="see questions tagged &#39;super-relations&#39;">super-relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '17, 00:47</strong></p>
<img src="https://secure.gravatar.com/avatar/fb21edcf78d1b7e3be00b6d31d7dd0e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="snodnipper&#39;s gravatar image" />
<p><span>snodnipper</span><br />
<span class="score" title="126 reputation points">126</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="snodnipper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55575" class="comments-container">
&#10;</div>
<div id="comment-tools-55575" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55575-form-container" class="comment-form-container">
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

<span id="55577"></span>

<div id="answer-container-55577" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55577-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-55577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="snodnipper has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no established convention for super-relations. There are some programs that do something with relations of relations in some specialized cases, but there is no such thing as a generally defined and accepted "super relation" so there is no best-practice here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '17, 08:28</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '17, 08:28</strong> </span></p>
</div>
</div>
<div id="comments-container-55577" class="comments-container">
<span id="55587"></span>
<div id="comment-55587" class="comment">
<div id="post-55587-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'll raise it as an issue with nominatim. I can imagine there could be issues with circular references with relations <em>but</em> in principle I believe super-relations should be searchable.</p>
</div>
<div id="comment-55587-info" class="comment-info">
<span class="comment-age">(12 Apr '17, 21:50)</span> <span class="comment-user userinfo">snodnipper</span>
</div>
</div>
</div>
<div id="comment-tools-55577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55577-form-container" class="comment-form-container">
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

