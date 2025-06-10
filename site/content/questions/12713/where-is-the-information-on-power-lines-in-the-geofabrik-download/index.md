+++
type = "question"
title = "where is the information on power lines in the geofabrik download"
description = '''Hi, I was looking at the OSM data online and can clearly see that in my area are also power lines digitized. However, when I download OSM data from one of the servers and load them in a GIS I cant find points for the poles nor polylines re sampling the data shown on osm.org. I particularly downloade...'''
date = "2012-05-14T11:19:00Z"
lastmod = "2012-05-14T11:51:00Z"
weight = 12713
keywords = [ "download", "geofabrik", "power" ]
aliases = [ "/questions/12713" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [where is the information on power lines in the geofabrik download](/questions/12713/where-is-the-information-on-power-lines-in-the-geofabrik-download)

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
<span id="post-12713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12713-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I was looking at the OSM data online and can clearly see that in my area are also power lines digitized. However, when I download OSM data from one of the servers and load them in a GIS I cant find points for the poles nor polylines re sampling the data shown on osm.org. I particularly downloaded data for Denmark from <a href="http://download.geofabrik.de/osm/europe/">http://download.geofabrik.de/osm/europe/</a></p>
<p>Are does information not distributed or can somebody tell me where to find them?</p>
<p>Cheers Thomas</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span> <span class="post-tag tag-link-power" rel="tag" title="see questions tagged &#39;power&#39;">power</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '12, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/483fc8a0c0314f51c70d807f21a1757a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomDK&#39;s gravatar image" />
<p><span>TomDK</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomDK has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Dec '16, 13:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-12713" class="comments-container">
&#10;</div>
<div id="comment-tools-12713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12713-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="12716"></span>

<div id="answer-container-12716" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12716-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-12716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TomDK has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The free shapefile downloads on download.geofabrik.de only contain the most important features from OSM; powerlines are not included.</p>
<p>The .osm.bz2 and .osm.pbf files from the same site, on the other hand, contain the full OSM data.</p>
<p>Anyone making shapefiles must select which features to export; it is impossible to export "all" features.</p>
<p>There are several ways to get powerlines into your GIS system:</p>
<ul>
<li>make your own shapefiles, or have someone do that for you; common utilities for this are osm2shp or osmjs.</li>
<li>import data into a PostGIS database using osm2pgsql and point your GIS system to that database (requires support for talking to PostGIS, available e.g. in Quantum GIS);</li>
<li>load OSM data directly into your GIS system (requires support for OSM data format, available e.g. in Quantum GIS and ArcGIS)</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '12, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-12716" class="comments-container">
&#10;</div>
<div id="comment-tools-12716" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12716-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12715"></span>

<div id="answer-container-12715" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12715-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On osm.org, move the map so that an electricity pole is on the map. Here's an example:</p>
<p><a href="http://www.openstreetmap.org/?lat=53.27938&amp;lon=-1.3337&amp;zoom=17&amp;layers=M">http://www.openstreetmap.org/?lat=53.27938&amp;lon=-1.3337&amp;zoom=17&amp;layers=M</a></p>
<p>Zoom in.</p>
<p>Select "browse map data" from the "edit" menu (select the little triangle on the right to get the menu).</p>
<p>The electricity pole will be shown by a green dot. Click it.</p>
<p>Click "details" to the right of the node number. You can now see what it's tagged as an who added it (and the node number to look for in your "Denmark" extract).</p>
<p>Repeat the process for the polyline ("way") representing the cable.</p>
<p>On that example of mine, the poles are "<a href="http://wiki.openstreetmap.org/wiki/Tag:power%3Dtower">power=tower</a>" and the cables "<a href="http://wiki.openstreetmap.org/wiki/Tag:power%3Dline">power=line</a>".</p>
<p>If this doesn't work for you perhaps you could post a permalink to the area where you can see power lines but can't get data for?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '12, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-12715" class="comments-container">
&#10;</div>
<div id="comment-tools-12715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12715-form-container" class="comment-form-container">
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

