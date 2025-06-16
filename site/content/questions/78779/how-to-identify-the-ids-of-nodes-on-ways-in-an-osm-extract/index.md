+++
type = "question"
title = "How to identify the id&#x27;s of nodes on ways in an OSM extract?"
description = '''I downloaded an OSM extract via Geofabrik and was expecting to find the nodes that form the ways (defining the shape or &quot;path of the way) in the Points layer using QGIS. However, the points in this layer only define point features. I&#x27;m aware that I can look up individual nodes via http://www.openstr...'''
date = "2021-02-10T14:03:00Z"
lastmod = "2021-02-10T15:26:00Z"
weight = 78779
keywords = [ "ways", "qgis", "nodes", "osm" ]
aliases = [ "/questions/78779" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to identify the id's of nodes on ways in an OSM extract?](/questions/78779/how-to-identify-the-ids-of-nodes-on-ways-in-an-osm-extract)

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
<span id="post-78779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78779-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I downloaded an OSM extract via Geofabrik and was expecting to find the nodes that form the ways (defining the shape or "path of the way) in the Points layer using QGIS. However, the points in this layer only define point features.</p>
<p>I'm aware that I can look up individual nodes via <a href="https://www.openstreetmap.org/node/305293190">https://www.openstreetmap.org/node/305293190</a> for example. But I was wondering whether there is an another way to identify the id's of nodes on ways in the OSM extract, preferably using QGIS.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '21, 14:03</strong></p>
<img src="https://secure.gravatar.com/avatar/152906fc74217eeefa79ad3b652b3380?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="winecity&#39;s gravatar image" />
<p><span>winecity</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="winecity has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Feb '21, 14:08</strong> </span></p>
</div>
</div>
<div id="comments-container-78779" class="comments-container">
&#10;</div>
<div id="comment-tools-78779" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78779-form-container" class="comment-form-container">
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

<span id="78786"></span>

<div id="answer-container-78786" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78786-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can look at the file you downloaded to get that information. For instance with the "<a href="https://docs.osmcode.org/osmium/latest/osmium-show.html">osmium show</a>" command. You can use Osmium also to convert the PBF file you probably downloaded into other formats, for instance the XML format or the OPL format which are both text based so you can look at the data easily.</p>
<p>There are many many other ways to get at that information, but it really depends on what you want to do with it, before we can recommend anything. Also: There are multiple ways to "load" the data into QGIS and you don't say which one you are using.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '21, 15:26</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-78786" class="comments-container">
&#10;</div>
<div id="comment-tools-78786" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78786-form-container" class="comment-form-container">
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

