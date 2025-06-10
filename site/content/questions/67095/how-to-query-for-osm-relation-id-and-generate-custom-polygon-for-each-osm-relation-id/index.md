+++
type = "question"
title = "How to query for OSM Relation ID and generate custom polygon for each OSM Relation ID?"
description = '''I am trying to get a custom polygon for a list of locations. To get the polygon for each item first I need to find each items OSM Relation ID using the searchbox in the https://www.openstreetmap.org and then run that OSM Relation ID through the tool http://polygons.openstreetmap.fr/. That tool will ...'''
date = "2018-12-07T15:47:00Z"
lastmod = "2018-12-13T16:55:00Z"
weight = 67095
keywords = [ "osm", "relation", "polygon" ]
aliases = [ "/questions/67095" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to query for OSM Relation ID and generate custom polygon for each OSM Relation ID?](/questions/67095/how-to-query-for-osm-relation-id-and-generate-custom-polygon-for-each-osm-relation-id)

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
<span id="post-67095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67095-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to get a custom polygon for a list of locations. To get the polygon for each item first I need to find each items OSM Relation ID using the searchbox in the <a href="https://www.openstreetmap.org">https://www.openstreetmap.org</a> and then run that OSM Relation ID through the tool <a href="http://polygons.openstreetmap.fr/.">http://polygons.openstreetmap.fr/.</a> That tool will then generate a polygon to the size I am looking for: <a href="http://polygons.openstreetmap.fr/get_poly.py?id=1216769&amp;params=0.005000-0.002000-0.002000">http://polygons.openstreetmap.fr/get_poly.py?id=1216769&amp;params=0.005000-0.002000-0.002000</a></p>
<p>I would like to query through the OSM Relation database and automatically generate the polygon with the given polygon parameters for each OSM Relation ID retrieved from the query.</p>
<p><strong>Is there a way to automate this process? Where can I find the database that contains the OSM Relation ID and its properties ? Is there an offline tool to convert the OSM Relation ID to my size polygon?</strong></p>
<p>For example: I would like to get the polygon for Miami. To get it I would have to first search the OSM Relation ID of Miami which is 1216769. Then I would use the following link with the id: <a href="http://polygons.openstreetmap.fr/get_poly.py?id=1216769&amp;params=0.005000-0.002000-0.002000">http://polygons.openstreetmap.fr/get_poly.py?id=1216769&amp;params=0.005000-0.002000-0.002000</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Dec '18, 15:47</strong></p>
<img src="https://secure.gravatar.com/avatar/75957ea46d8e0cf2deeb9f85c6b24903?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="the_alamo&#39;s gravatar image" />
<p><span>the_alamo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="the_alamo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '18, 16:04</strong> </span></p>
</div>
</div>
<div id="comments-container-67095" class="comments-container">
&#10;</div>
<div id="comment-tools-67095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67095-form-container" class="comment-form-container">
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

<span id="67121"></span>

<div id="answer-container-67121" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67121-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Alternatively, you could use <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a> to download polygons for administrative boundaries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Dec '18, 07:14</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-67121" class="comments-container">
<span id="67174"></span>
<div id="comment-67174" class="comment">
<div id="post-67174-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is extremely helpful, I can use this as a workaround for now. My only issue with this tool in particular is that I cannot modify the level of detail generated by the export.</p>
</div>
<div id="comment-67174-info" class="comment-info">
<span class="comment-age">(13 Dec '18, 16:55)</span> <span class="comment-user userinfo">the_alamo</span>
</div>
</div>
</div>
<div id="comment-tools-67121" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67121-form-container" class="comment-form-container">
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

