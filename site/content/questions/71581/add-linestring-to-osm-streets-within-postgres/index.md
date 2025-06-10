+++
type = "question"
title = "add linestring to osm streets within postgres"
description = '''Here is what I did I have imported streets from OSM into my postgres db with osmosis.  Here is my question After importing the osm data with osmosis, I now wanna add a linestring to the osm streets. Is there a way to edit the linestring in the existing osm schema/structure that osmosis has defined w...'''
date = "2019-11-10T20:31:00Z"
lastmod = "2019-11-11T11:28:00Z"
weight = 71581
keywords = [ "osm", "postgresql", "osmosis" ]
aliases = [ "/questions/71581" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [add linestring to osm streets within postgres](/questions/71581/add-linestring-to-osm-streets-within-postgres)

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
<span id="post-71581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71581-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Here is what I did</strong></p>
<p>I have imported streets from OSM into my postgres db with osmosis.</p>
<p><strong>Here is my question</strong></p>
<p>After importing the osm data with osmosis, I now wanna add a linestring to the osm streets. Is there a way to edit the linestring in the existing osm schema/structure that osmosis has defined within postgres</p>
<p><strong>osm data structure within postgres via osmosis</strong></p>
<p>Postgres is showing me following tables:</p>
<ul>
<li>nodes</li>
<li>ways</li>
<li>way_nodes</li>
<li>relations</li>
<li>relation_members</li>
</ul>
<p>can't figure out the relationship between the tables. I now that the table 'ways' is connected with the table 'way__nodes' via the way_id column.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '19, 20:31</strong></p>
<img src="https://secure.gravatar.com/avatar/9c7e7edebf2afe1bc709df42d5fa7600?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tara&#39;s gravatar image" />
<p><span>Tara</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tara has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Nov '19, 20:32</strong> </span></p>
</div>
</div>
<div id="comments-container-71581" class="comments-container">
<span id="71584"></span>
<div id="comment-71584" class="comment">
<div id="post-71584-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suspect you may be better with an osm2pgsql database rather than an API or snapshot DB (from your comment this looks like a snapshot DB). Depending which osmosis options you used there may well be a column containing line strings in the ways table. Otherwise you need to write (quite) complex queries linking nodes, way_nodes and ways.</p>
</div>
<div id="comment-71584-info" class="comment-info">
<span class="comment-age">(11 Nov '19, 11:28)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71581-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

