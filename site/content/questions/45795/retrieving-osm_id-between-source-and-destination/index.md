+++
type = "question"
title = "retrieving osm_id between source and destination .."
description = '''Hello I have the openstreetmap database , from geofabrik..which contain planet_osm_point.planet_osm_line,Planet_osm_polygon,planet_osm_roads. So now my question is, ST_distance is used to find the distance between source and destination , so how can i retrieve the existing -Nodes(which is -osm_id,na...'''
date = "2015-10-07T23:18:00Z"
lastmod = "2015-10-07T23:31:00Z"
weight = 45795
keywords = [ "postgresql", "planet_osm_ways", "postgis", "planet_osm" ]
aliases = [ "/questions/45795" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [retrieving osm_id between source and destination ..](/questions/45795/retrieving-osm_id-between-source-and-destination)

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
<span id="post-45795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45795-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I have the openstreetmap database , from geofabrik..which contain planet_osm_point.planet_osm_line,Planet_osm_polygon,planet_osm_roads.</p>
<p>So now my question is, ST_distance is used to find the distance between source and destination , so how can i retrieve the existing -Nodes(which is -osm_id,name,Way) between source and destination.in postgre sql</p>
<p>help me please</p>
<p>best regards Kumar</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-planet_osm_ways" rel="tag" title="see questions tagged &#39;planet_osm_ways&#39;">planet_osm_ways</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '15, 23:18</strong></p>
<img src="https://secure.gravatar.com/avatar/b51f82218d5511a6cb08225ee3015f57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kumar45&#39;s gravatar image" />
<p><span>kumar45</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kumar45 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Oct '15, 23:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45795" class="comments-container">
&#10;</div>
<div id="comment-tools-45795" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45795-form-container" class="comment-form-container">
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

<span id="45796"></span>

<div id="answer-container-45796" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45796-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-45796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can retrieve the positions of the nodes from the line geometry but not the OSM ID; the OSM ID has been thrown away during the import because it is not needed for rendering.</p>
<p>If you import with the --slim option, then the OSM IDs of all nodes making up a way will be kept in an array in the planet_osm_ways table. The coordinates of those nodes will be in planet_osm_nodes unless you import with --flatnodes. The tags of those nodes (since you mention "name") are only recorded if they appear in the osm2pgsql style file and in that case, the node will (in addition to being in planet_osm_nodes) also appear in planet_osm_point where the tags are stored.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '15, 23:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-45796" class="comments-container">
&#10;</div>
<div id="comment-tools-45796" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45796-form-container" class="comment-form-container">
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

