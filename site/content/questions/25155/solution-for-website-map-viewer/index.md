+++
type = "question"
title = "Solution for website map viewer"
description = '''Hi, For a small community website I want to display POIs which are dynamically loaded from a webserver backend. This POI data does not come from OSM. When the map is zoomed or the focused region is changed, new POI data should be loaded from the server which replaces the old POIs. The POI images are...'''
date = "2013-08-10T10:58:00Z"
lastmod = "2013-08-12T05:49:00Z"
weight = 25155
keywords = [ "facilmap", "poi", "openlayers", "slippymap", "dynamic" ]
aliases = [ "/questions/25155" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Solution for website map viewer](/questions/25155/solution-for-website-map-viewer)

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
<span id="post-25155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25155-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>For a small community website I want to display POIs which are dynamically loaded from a webserver backend. This POI data does not come from OSM. When the map is zoomed or the focused region is changed, new POI data should be loaded from the server which replaces the old POIs. The POI images are a custom images. When a POI is clicked, then a pop-over should be shown with some (aribitrary) details of the POI.</p>
<p>Other requirements:</p>
<ul>
<li>Search on the map using Nominatim (<a href="http://wiki.openstreetmap.org/wiki/Nominatim)">http://wiki.openstreetmap.org/wiki/Nominatim)</a></li>
<li>Support for other layers beside Mapnik, such as OpenCyclemap, and Google Maps satellite data</li>
</ul>
<p>I think this is very straight forward stuff which is very common and often seen on various websites. Thus, before I start from "scratch" building a solution with OpenLayers I have done some research of existing solutions but interestingly, I have only found FacilMap (<a href="http://wiki.openstreetmap.org/wiki/FacilMap)">http://wiki.openstreetmap.org/wiki/FacilMap)</a> which supports many map providers, as well as Nominatim.</p>
<p>Are there any other projects which offer the feature range described above?</p>
<p>Regards,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-facilmap" rel="tag" title="see questions tagged &#39;facilmap&#39;">facilmap</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-slippymap" rel="tag" title="see questions tagged &#39;slippymap&#39;">slippymap</span> <span class="post-tag tag-link-dynamic" rel="tag" title="see questions tagged &#39;dynamic&#39;">dynamic</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '13, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/73ebf88028ec0c6df8f7b0cf913dd67f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hynx&#39;s gravatar image" />
<p><span>hynx</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hynx has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Aug '13, 10:59</strong> </span></p>
</div>
</div>
<div id="comments-container-25155" class="comments-container">
&#10;</div>
<div id="comment-tools-25155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25155-form-container" class="comment-form-container">
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

<span id="25209"></span>

<div id="answer-container-25209" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25209-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hynx has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe you can also have a look at the framework <a href="http://leafletjs.com">leaflet</a>.</p>
<p>This solution is now used for the main site openstreetmap.org as well.</p>
<p>You can find some examples and documentation at its mentioned website.</p>
<p>Elswise I can only recommend to browse the OSM wiki to find website solutions fitting your aims, and try to recycle some code. There is a listing of websites using OSM related frameworks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '13, 19:50</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-25209" class="comments-container">
<span id="25218"></span>
<div id="comment-25218" class="comment">
<div id="post-25218-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have experimented with leaflet over the weekend and it is pretty solid and easy to use. At the moment I am still trying to get dynamic loading of markers to get work.</p>
</div>
<div id="comment-25218-info" class="comment-info">
<span class="comment-age">(12 Aug '13, 05:49)</span> <span class="comment-user userinfo">hynx</span>
</div>
</div>
</div>
<div id="comment-tools-25209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25209-form-container" class="comment-form-container">
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

