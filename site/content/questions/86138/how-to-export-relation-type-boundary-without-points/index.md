+++
type = "question"
title = "How to export relation type boundary without points?"
description = '''I am trying to export as GeoJson the boundary of the regions of Ghana. My simple query is the following:  [out:json]; area[admin_level=2][name=Ghana]; rel[boundary=administrative][admin_level=4](area); out geom;  My challenge is that when exporting it to GeoJson I do not only get the contour but als...'''
date = "2022-11-11T20:42:00Z"
lastmod = "2023-01-07T18:39:00Z"
weight = 86138
keywords = [ "boundary", "points", "beginner", "geojson", "relations" ]
aliases = [ "/questions/86138" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to export relation type boundary without points?](/questions/86138/how-to-export-relation-type-boundary-without-points)

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
<span id="post-86138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86138-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to export as GeoJson the boundary of the regions of Ghana. My simple query is the following:</p>
<pre><code>[out:json];
area[admin_level=2][name=Ghana];
rel[boundary=administrative][admin_level=4](area);
out geom;</code></pre>
<p>My challenge is that when exporting it to GeoJson I do not only get the contour but also a point or two in each region. Is there a way to get rid of it in the query? Right now, my only workaround is to remove it manually which is very slow.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-points" rel="tag" title="see questions tagged &#39;points&#39;">points</span> <span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Nov '22, 20:42</strong></p>
<img src="https://secure.gravatar.com/avatar/17251d09b89731b82e605ff9ba5b0d6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gmacia&#39;s gravatar image" />
<p><span>gmacia</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gmacia has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86138" class="comments-container">
&#10;</div>
<div id="comment-tools-86138" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86138-form-container" class="comment-form-container">
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

<span id="86451"></span>

<div id="answer-container-86451" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86451-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Those <em>points</em> are the administrative centre of each region and the label of each region. The first are nodes with role <em>admin_centre</em>, and the second are nodes with the role <em>label</em>. See <a href="https://wiki.openstreetmap.org/wiki/Relation:boundary#Relation_members">this wiki page</a> for more info about <em>type=boundary</em> relation members.</p>
<p>You have to use <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Recurse_(n,_w,_r,_bn,_bw,_br)">recurse statements</a> to get rid of those two nodes. One query that works is the following one, but there might be simpler ones:</p>
<pre><code>[out:json][timeout:50];
area[admin_level=2][name=Ghana];
//We put the 16 regions relations in the .allRelations set:
rel[boundary=administrative][admin_level=4](area)-&gt;.allRelations;
//We get only the ways members of the relations, that means, the border ways of the regions,
//and we put them in the .relationWays set:
way(r.allRelations)-&gt;.relationWays;
//And now we get all the nodes of those border ways, and put them in the .waysNodes set:
node(w.relationWays)-&gt;.waysNodes;
//Now we get the union of all the three sets (relations, their ways and those ways nodes):
(
  .allRelations;
  .relationWays;
  .waysNodes;
);
//And we output all data:
out meta;</code></pre>
<p>Note 1: You can't use <strong>out geom;</strong> here, because <strong>out geom;</strong> adds, among others, a sequence of "nd" members with coordinates to all relations, and therefore you would get those nodes you want to get rid of.</p>
<p>Note 2: We could use <strong>out body;</strong> instead of <strong>out meta;</strong> if we are not interested in metadata, like version of objets, changeset id, timestamp, and the user data of the user that last touched the object.</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#out">this wiki page</a> section for more info about the out standalone statement.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '23, 18:39</strong></p>
<img src="https://secure.gravatar.com/avatar/d45c161edd4b471fd947a7ec574274ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edvac&#39;s gravatar image" />
<p><span>edvac</span><br />
<span class="score" title="665 reputation points">665</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edvac has 4 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-86451" class="comments-container">
&#10;</div>
<div id="comment-tools-86451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86451-form-container" class="comment-form-container">
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

