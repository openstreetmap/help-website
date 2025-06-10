+++
type = "question"
title = "Area relations"
description = '''Hi, I&#x27;m new to OSM so please bear with me. I&#x27;ve used osm2pgsql to produce a dataset from a small osm file (south yorkshire). What I&#x27;m trying to achieve is to be able to determine relationships, so for instance Crookes is a suburb in Sheffield which is a city in the United Kingdom. I thought I was on...'''
date = "2012-05-16T13:41:00Z"
lastmod = "2012-05-16T14:10:00Z"
weight = 12757
keywords = [ "boundaries", "osm", "osm2pgsql" ]
aliases = [ "/questions/12757" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Area relations](/questions/12757/area-relations)

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
<span id="post-12757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12757-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm new to OSM so please bear with me.</p>
<p>I've used osm2pgsql to produce a dataset from a small osm file (south yorkshire). What I'm trying to achieve is to be able to determine relationships, so for instance Crookes is a suburb in Sheffield which is a city in the United Kingdom.</p>
<p>I thought I was on to something when I saw that points that are places are also closed ways and so tried ST_XMax, ST_YMax etc on the way column to determine the bounding box. It seems however that these are just points (as ST_XMax and ST_XMin on place=city,name=Sheffield come back the same).</p>
<p>Am I completely on the wrong track, if so, can anyone point me in the right direction to achieve what I'm looking for?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 May '12, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/cec53541e3ec8e7e78109e3722d5be17?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TBriggs&#39;s gravatar image" />
<p><span>TBriggs</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TBriggs has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12757" class="comments-container">
<span id="12758"></span>
<div id="comment-12758" class="comment">
<div id="post-12758-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think the problem is that I was using planet_osm_points rather than planet_osm_polygons</p>
</div>
<div id="comment-12758-info" class="comment-info">
<span class="comment-age">(16 May '12, 14:10)</span> <span class="comment-user userinfo">TBriggs</span>
</div>
</div>
</div>
<div id="comment-tools-12757" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12757-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

