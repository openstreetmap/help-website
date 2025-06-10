+++
type = "question"
title = "Longitude and latitude of a relation"
description = '''I‘m trying to understand how I can find the long/lat for a given relation. I would like to archive this based on a sql query. Would I need to create a new polygon based on the members polygon and the find the center of that polygon? Looking forward to any tips Thx!'''
date = "2018-02-23T15:07:00Z"
lastmod = "2018-02-24T15:04:00Z"
weight = 62317
keywords = [ "postgresql", "postgis" ]
aliases = [ "/questions/62317" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Longitude and latitude of a relation](/questions/62317/longitude-and-latitude-of-a-relation)

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
<span id="post-62317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62317-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I‘m trying to understand how I can find the long/lat for a given relation. I would like to archive this based on a sql query. Would I need to create a new polygon based on the members polygon and the find the center of that polygon?</p>
<p>Looking forward to any tips</p>
<p>Thx!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Feb '18, 15:07</strong></p>
<img src="https://secure.gravatar.com/avatar/b59231b2ea01633cc4c5936cd117dc84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gabac&#39;s gravatar image" />
<p><span>gabac</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gabac has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Feb '18, 17:12</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-62317" class="comments-container">
&#10;</div>
<div id="comment-tools-62317" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62317-form-container" class="comment-form-container">
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

<span id="62319"></span>

<div id="answer-container-62319" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62319-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-62319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gabac has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Relations (not relationships) are simply lists of other OSM objects (potentially with an associated "role" attribute). The actual meaning/semantics of the relation are dependent on the "type" attribute of the relation.</p>
<p>Examples:</p>
<ul>
<li>type=multipolygon - a list of elements building outer and inner rings of a potentially complex area-like object</li>
<li>type=route - a list of ways and potentially other objects describing a linear connection between two locations (that is a bit simplified)</li>
<li>type=restriction - three elements modelling a turn off from the "from" element that may be allowed or not</li>
</ul>
<p>For all of these it is possible to define a meaningful centroid, however how to exactly do so really depends. Now assuming what you are actually looking at is a multipolygon (or a boundary which for this purpose is essentially the same) and the geometry of the polygons have already been built (don't try to do this yourself, use a library) it is relatively easy because any database with support for spatial values will have built in functions for this.</p>
<p>Unluckily you haven't given any details as to where you are retrieving the relations from in what format and where you intend to store them, so I have to stop here for now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '18, 17:11</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Feb '18, 17:13</strong> </span></p>
</div>
</div>
<div id="comments-container-62319" class="comments-container">
<span id="62370"></span>
<div id="comment-62370" class="comment">
<div id="post-62370-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What I did so far.</p>
<p>I loaded a subsetdata of OSM data via osmosis into my postgres database.</p>
<p>Now lets say we look into following relation (this is supposed to be a relation for a winter resort in Switzerland)</p>
<p>SELECT * FROM relations WHERE id = 6720604</p>
<p>or</p>
<p>SELECT * FROM relation_members WHERE relation_id=6720604</p>
<p>As you see no member_role attribute has been given.</p>
<p>I'm aware that with. e.g. ST_Centroid you can let the DB calculate you the center.</p>
<p>But how do I get a meaningful multi/polygon of the above relationship?</p>
<p>Hope this explains my issue in more detail</p>
</div>
<div id="comment-62370-info" class="comment-info">
<span class="comment-age">(24 Feb '18, 14:31)</span> <span class="comment-user userinfo">gabac</span>
</div>
</div>
<span id="62371"></span>
<div id="comment-62371" class="comment">
<div id="post-62371-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>"But how do I get a meaningful multi/polygon of the above relationship?"</p>
<p>You can't. You need to have a database in which the geometry of the OSM objects have actually been built. The most popular way to do this is to create a database in the osm2pgsql schema and import data to it (while osm2pgsql is mainly intended for rendering, the requirements overlap in this respect).</p>
</div>
<div id="comment-62371-info" class="comment-info">
<span class="comment-age">(24 Feb '18, 14:37)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="62372"></span>
<div id="comment-62372" class="comment">
<div id="post-62372-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh ok I see.</p>
<p>Then I’m now off to the task of understanding osm2psql as well :)</p>
<p>Thx for your help</p>
</div>
<div id="comment-62372-info" class="comment-info">
<span class="comment-age">(24 Feb '18, 15:04)</span> <span class="comment-user userinfo">gabac</span>
</div>
</div>
</div>
<div id="comment-tools-62319" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62319-form-container" class="comment-form-container">
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

