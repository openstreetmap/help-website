+++
type = "question"
title = "Relation members structure for DB"
description = '''How to correctly represent relation members in Mysql DB? I see two variants:  One table &quot;rel_member&quot; with ordered member list of different types with discriminator column. Three tables &quot;rel_member_rel&quot;, &quot;rel_member_way&quot;, &quot;rel_member_node&quot; for each corresponding object type.   For me second variant i...'''
date = "2015-01-17T22:26:00Z"
lastmod = "2015-01-18T01:38:00Z"
weight = 40452
keywords = [ "member", "relations", "mysql" ]
aliases = [ "/questions/40452" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Relation members structure for DB](/questions/40452/relation-members-structure-for-db)

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
<span id="post-40452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40452-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How to correctly represent relation members in Mysql DB? I see two variants:</p>
<ol>
<li>One table "rel_member" with ordered member list of different types with discriminator column.</li>
<li>Three tables "rel_member_rel", "rel_member_way", "rel_member_node" for each corresponding object type.</li>
</ol>
<p>For me second variant is preferable, but does it retain OSM semantics?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-member" rel="tag" title="see questions tagged &#39;member&#39;">member</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jan '15, 22:26</strong></p>
<img src="https://secure.gravatar.com/avatar/1eb35522ff8c4c949ce4c1ac73654649?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikoder&#39;s gravatar image" />
<p><span>ikoder</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikoder has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40452" class="comments-container">
&#10;</div>
<div id="comment-tools-40452" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40452-form-container" class="comment-form-container">
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

<span id="40454"></span>

<div id="answer-container-40454" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40454-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Depends on what you want to achieve. Relations are ordered in OSM so if you ever plan to upload something again, or otherwise accurately represent OSM's data, you will have to retain the order of elements. In your #2, this would have to be implemented as a separate sequencing column.</p>
<p>For most interpretation purposes, e.g. for the drawing of routes or multipolygons, the order does not matter. osm2pgsql, for example, uses a variant of your #1 schema but instead of a discriminator column, stores all member object IDs in a linear list - nodes first, then ways, then relations - and uses only two additional integers to point to the beginning of the way IDs and the beginning of the relation IDs in that list.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jan '15, 01:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-40454" class="comments-container">
&#10;</div>
<div id="comment-tools-40454" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40454-form-container" class="comment-form-container">
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

