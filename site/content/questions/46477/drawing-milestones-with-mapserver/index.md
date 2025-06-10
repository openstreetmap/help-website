+++
type = "question"
title = "Drawing milestones with mapserver"
description = '''I am trying doing it in two ways and failing both. I am drawing maps with OSM data and a database imported by imposm. The issue is that I have no milestones in the database. Is there anyway to get them into the database? I have seen the imposm-mapping.py that is the one mapping from OSM data to the ...'''
date = "2015-11-09T12:56:00Z"
lastmod = "2015-11-09T16:21:00Z"
weight = 46477
keywords = [ "mapserver", "nominatim", "osm", "imposm", "milestones" ]
aliases = [ "/questions/46477" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Drawing milestones with mapserver](/questions/46477/drawing-milestones-with-mapserver)

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
<span id="post-46477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46477-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying doing it in two ways and failing both.</p>
<p>I am drawing maps with OSM data and a database imported by imposm. The issue is that I have no milestones in the database. Is there anyway to get them into the database? I have seen the imposm-mapping.py that is the one mapping from OSM data to the imposm datamodel but I found no documentation on it.</p>
<p>I am also doing some tests with nominatim database and in "place" table I filter by "class=highway" and "type=milestone" but less than 300 milestones found to all spain (I am using spain-last). Maybe I am missing the way of getting milestones from nominatim. Should I use another filter or could milestones be taged other way?</p>
<p>Does anyone drawn milestones using Nominatim datamodel?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapserver" rel="tag" title="see questions tagged &#39;mapserver&#39;">mapserver</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-imposm" rel="tag" title="see questions tagged &#39;imposm&#39;">imposm</span> <span class="post-tag tag-link-milestones" rel="tag" title="see questions tagged &#39;milestones&#39;">milestones</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Nov '15, 12:56</strong></p>
<img src="https://secure.gravatar.com/avatar/8ff71fc907067296fbfac86e637faa50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juanma%20MR&#39;s gravatar image" />
<p><span>Juanma MR</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juanma MR has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46477" class="comments-container">
<span id="46479"></span>
<div id="comment-46479" class="comment">
<div id="post-46479-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>According to this <a href="http://overpass-turbo.eu/s/cyq">Overpass API query</a> there are currently 551 nodes tagged as highway=milestone in Spain. Don't expect every existing milestone to be mapped in OSM, most people don't really care about or need them.</p>
</div>
<div id="comment-46479-info" class="comment-info">
<span class="comment-age">(09 Nov '15, 14:17)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="46480"></span>
<div id="comment-46480" class="comment">
<div id="post-46480-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I for one adore milestones and have tagged many of them in Thailand. I use highway=milestone and add a tag for distance and tags for inscriptions in both Thai and English if one is present. I especially like the ones that indicate the beginning of a highway, those that have a distance of 0 km marked on them. I've tagged 231 of those so far.</p>
</div>
<div id="comment-46480-info" class="comment-info">
<span class="comment-age">(09 Nov '15, 16:21)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-46477" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46477-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

