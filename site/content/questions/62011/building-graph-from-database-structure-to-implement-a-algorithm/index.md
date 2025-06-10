+++
type = "question"
title = "building graph from database structure to implement A* algorithm"
description = '''I imported an osm file into a postgresql database using osm2pgsql. Now, I want to implement a route/path generating algorithm(routing algo) based on two locations entered by a user. It is not really clear for me where in my database structure I should search for these two points. For example if a us...'''
date = "2018-02-08T03:44:00Z"
lastmod = "2018-02-08T16:59:00Z"
weight = 62011
keywords = [ "graph", "postgresql", "osm2pgsql" ]
aliases = [ "/questions/62011" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [building graph from database structure to implement A\* algorithm](/questions/62011/building-graph-from-database-structure-to-implement-a-algorithm)

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
<span id="post-62011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62011-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I imported an osm file into a postgresql database using osm2pgsql. Now, I want to implement a route/path generating algorithm(routing algo) based on two locations entered by a user. It is not really clear for me where in my database structure I should search for these two points. For example if a user enters as starting point "Airport A" and as end point "Airport B" where should I search for these two locations so I can start implementing my routing algorithm. I need some clear information on how the database is structured and how to create a graph so that i can implement A* algorithm between the 2 points the user has enetered.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '18, 03:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ce6ade958843a42d1148a9569477aa27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="roshansivakumar&#39;s gravatar image" />
<p><span>roshansivakumar</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="roshansivakumar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62011" class="comments-container">
<span id="62017"></span>
<div id="comment-62017" class="comment">
<div id="post-62017-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Using osm2pgsql is not the best way of doing this as it removes connection information between ways. Most routing tools use a separate geocoder to translate from location names to lat/lon. I would recommend using something like osm2pgrouting and PG routing in PostGis.</p>
</div>
<div id="comment-62017-info" class="comment-info">
<span class="comment-age">(08 Feb '18, 16:59)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62011-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

