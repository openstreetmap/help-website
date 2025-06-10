+++
type = "question"
title = "Getting road information from lat/lon in OSM"
description = '''I am using osm database imported with osm2pgsql in slim mode. In my current app I have locations of different vehicles in lat lon. I want to get max speed, road name and road type for each location.  So here is the approach I am looking to implement -- for each set of lat lon values find the closest...'''
date = "2017-07-25T16:18:00Z"
lastmod = "2017-07-25T16:18:00Z"
weight = 57269
keywords = [ "maxspeed", "osm", "osm2pgsql", "postgis", "highway" ]
aliases = [ "/questions/57269" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Getting road information from lat/lon in OSM](/questions/57269/getting-road-information-from-latlon-in-osm)

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
<span id="post-57269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57269-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using osm database imported with osm2pgsql in slim mode. In my current app I have locations of different vehicles in lat lon. I want to get max speed, road name and road type for each location.</p>
<p>So here is the approach I am looking to implement</p>
<p>-- for each set of lat lon values find the closest point in <code>planet_osm_points</code></p>
<p>-- find a node in <code>planet_osm_nodes</code> with lat and lon values equal to that of the point's multiplied with 100 (since lat lon in nodes is in integer form)</p>
<p>-- get the node id and find all ways in <code>planet_osm_ways</code> with these nodes and look for tags maxspeed and highway.</p>
<p>-- if max speed is not present use the maxspeed for that road type in that country.</p>
<p>So I have a few questions regarding this scenario</p>
<p>1- Is there a more optimized way of getting these values since I would be doing them for 1-2M records on a daily basis.</p>
<p>2- how can i find road name? which tag represents that?</p>
<p>3- Since I am doing all of this offline. is there any source from where I can get country wise max speed for roads programatically and dump it in my db?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jul '17, 16:18</strong></p>
<img src="https://secure.gravatar.com/avatar/24fb9e633cb135d94e6a9b4cc4fc6d1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aitizazk&#39;s gravatar image" />
<p><span>aitizazk</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aitizazk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57269" class="comments-container">
&#10;</div>
<div id="comment-tools-57269" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57269-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

