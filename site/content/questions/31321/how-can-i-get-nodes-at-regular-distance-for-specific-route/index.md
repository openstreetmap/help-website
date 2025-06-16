+++
type = "question"
title = "how can i get nodes at regular distance for specific route?"
description = '''hi, As I am new to this field, my question may be very basic. I searched through FAQs but I could not find answer so I decided to take help from you people. I want to get the nodes value for a specific route, lets say 50 meters apart each ? Does open street map provides any tool to do this ? What i ...'''
date = "2014-03-05T13:53:00Z"
lastmod = "2014-03-05T16:21:00Z"
weight = 31321
keywords = [ "usage", "segmentation" ]
aliases = [ "/questions/31321" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how can i get nodes at regular distance for specific route?](/questions/31321/how-can-i-get-nodes-at-regular-distance-for-specific-route)

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
<span id="post-31321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31321-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hi, As I am new to this field, my question may be very basic. I searched through FAQs but I could not find answer so I decided to take help from you people.</p>
<p>I want to get the nodes value for a specific route, lets say 50 meters apart each ? Does open street map provides any tool to do this ? What i am trying to do is that I have one specific bus route. And i can access GPS data from bus after regular times. I want to map GPS Data from the bus to real routes. And in order to do it, i need coordinates of nodes of small road segments where i can map the position of bus. Does Openstreetmap can help me in dividing a specific route into regular distance apart nodes ? If yes, can someone please guide me to starting point ?</p>
<p>Update/clarification: let me try to explain. i have a bus route, i want to divide the route into small segments for example from 1 to 100. At any time, i received GPS data, i map it onto one of the segments calculating the distance from the nodes of the segments to the measured value. Hence at sampling times, i know the position of bus on route. Now I can use this information to predict the location and speed of bus at any time instant. But i need to divide the road into segments, and i need lat/long values for those segments. can anyone guide me to any tool which serve the purpose ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-segmentation" rel="tag" title="see questions tagged &#39;segmentation&#39;">segmentation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '14, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/ef3aac0451cb681fada58de00a045fc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adnanakbr&#39;s gravatar image" />
<p><span>adnanakbr</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adnanakbr has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Mar '14, 16:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-31321" class="comments-container">
<span id="31328"></span>
<div id="comment-31328" class="comment">
<div id="post-31328-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A sketch or more details of your scenario (which route from which source etc) would help to provide you with more infos.<br />
As far as I understand what you are looking for is a <a href="http://www.qgis.org/fi/docs/gentle_gis_introduction/vector_spatial_analysis_buffers.html">buffer around a line/route</a>? That can be realized with most GIS-suites as QGIS for example if you import OSM in an appropriate fileformat (e.g. road network as shp)</p>
</div>
<div id="comment-31328-info" class="comment-info">
<span class="comment-age">(05 Mar '14, 16:00)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-31321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31321-form-container" class="comment-form-container">
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

<span id="31331"></span>

<div id="answer-container-31331" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31331-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a look at <a href="https://wiki.openstreetmap.org/wiki/Nominatim">nominatim</a> or <a href="https://wiki.openstreetmap.org/wiki/OSRM">OSRM</a>. They are examples of reverse geocoders : tools that will return osm objects when you give it lat/lon coordinates. From there you'll know on which osm way the bus currently is, and how long it still has to go on its scheduled route.</p>
<p>I don't think there is anything to win by segmenting the osm ways into smaller chunks. You need to know which ways the bus will take and in which order anyway, so that gives you your distance estimate. If the bus is currently in the middle of an osm way with no nearby node, you can invent a node position on the spot using simple trigonometry.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '14, 16:21</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span> </br></p>
</div>
</div>
<div id="comments-container-31331" class="comments-container">
&#10;</div>
<div id="comment-tools-31331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31331-form-container" class="comment-form-container">
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

