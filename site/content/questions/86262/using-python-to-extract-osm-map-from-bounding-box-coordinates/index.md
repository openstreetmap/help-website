+++
type = "question"
title = "Using python to extract osm map from bounding box coordinates"
description = '''Hello everyone. I have started working with OSM maps. However, I have been struggling with one issue. Is there any way to extract the OSM map given the set of bounding box coordinates of min and max longitude and latitudes? Please let me know how I can visualize the roads, buildings, and water withi...'''
date = "2022-11-29T12:52:00Z"
lastmod = "2022-12-01T19:09:00Z"
weight = 86262
keywords = [ "python", "visualization", "osmapi_python", "osm", "extraction" ]
aliases = [ "/questions/86262" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using python to extract osm map from bounding box coordinates](/questions/86262/using-python-to-extract-osm-map-from-bounding-box-coordinates)

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
<span id="post-86262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86262-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone. I have started working with OSM maps. However, I have been struggling with one issue. Is there any way to extract the OSM map given the set of bounding box coordinates of min and max longitude and latitudes? Please let me know how I can visualize the roads, buildings, and water within these coordinates as I intend to use it as a semantic segmentation mask for my UAV imagery with the exact bounding box coordinates.</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-visualization" rel="tag" title="see questions tagged &#39;visualization&#39;">visualization</span> <span class="post-tag tag-link-osmapi_python" rel="tag" title="see questions tagged &#39;osmapi_python&#39;">osmapi_python</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-extraction" rel="tag" title="see questions tagged &#39;extraction&#39;">extraction</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '22, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/8afc27ce83b9b8725cb9a2b48ffafebf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dawood&#39;s gravatar image" />
<p><span>Dawood</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dawood has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86262" class="comments-container">
&#10;</div>
<div id="comment-tools-86262" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86262-form-container" class="comment-form-container">
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

<span id="86268"></span>

<div id="answer-container-86268" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86268-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Is there any way to extract the OSM map</p>
</blockquote>
<p>if by map you mean the render on OSM.org, then you don't need to extract anythig.</p>
<p>if by map you mean the data, then it's probably better to download an extract of the are of interest (see <a href="https://download.geofabrik.de/),">https://download.geofabrik.de/),</a> load it in a database, and then use psycopg or any other python-pg library.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '22, 19:00</strong></p>
<img src="https://secure.gravatar.com/avatar/e4587465b2b1b94834e5e625b80a29dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marcos%20Dione&#39;s gravatar image" />
<p><span>Marcos Dione</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marcos Dione has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86268" class="comments-container">
<span id="86269"></span>
<div id="comment-86269" class="comment">
<div id="post-86269-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the reply Marcos. Sorry I am new to this. I want to extract the renders only. Could you explain what do you mean by 'you don't need to extract anything'? Becuase whenever I try to download the render maps from OSM.org usinhg http link, it downloads the osm file instead which I dont require as I need the rendered maps (preferrably without symbols).</p>
</div>
<div id="comment-86269-info" class="comment-info">
<span class="comment-age">(29 Nov '22, 19:10)</span> <span class="comment-user userinfo">Dawood</span>
</div>
</div>
<span id="86270"></span>
<div id="comment-86270" class="comment">
<div id="post-86270-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>I want to extract the renders only</p>
</blockquote>
<p>and</p>
<blockquote>
<p>I need the rendered maps (preferrably without symbols).</p>
</blockquote>
<p>are a little bit contradictory. Let me try to explain:</p>
<p>You can already create web maps that use OSM's tilesas background. This is legal and requires almost no effort from your part. You can also add more data on top. You have probably already seen many of these types of maps. But that means you get the tiles as they are.</p>
<p>If you want to render your own maps, then the effort is quite different. Check <a href="https://switch2osm.org/serving-tiles/">https://switch2osm.org/serving-tiles/</a></p>
</div>
<div id="comment-86270-info" class="comment-info">
<span class="comment-age">(30 Nov '22, 07:15)</span> <span class="comment-user userinfo">Marcos Dione</span>
</div>
</div>
<span id="86274"></span>
<div id="comment-86274" class="comment">
<div id="post-86274-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I understand your answer. However, my requirement is a little different. I have a set of coordinates (min and max lat and long) for a bounding box e.g. east = 13.372295, west = 13.3692166. north = 52.523443, south = 52.5214641 and I want to extract the exact osm map that lies inside these geographic coordinates. However, when I try to extract the map I always receive a tile with the unnecessary area which is outside my bounding box. Please let me know if this is possible. If yes, then how?</p>
</div>
<div id="comment-86274-info" class="comment-info">
<span class="comment-age">(30 Nov '22, 11:24)</span> <span class="comment-user userinfo">Dawood</span>
</div>
</div>
<span id="86288"></span>
<div id="comment-86288" class="comment">
<div id="post-86288-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's quite complex. You first have to convert your LatLon coords into tile numbers. For ZL0 it's easy, because it's always 0,0,0; for ZL1 is not that difficult, having only 4 tiles to select from. But for deeper Zoom Levels, it's a formula like (but not quite) the one in this function:</p>
<p><a href="https://github.com/StyXman/osm-tile-tools/blob/master/map_utils.py#L64">https://github.com/StyXman/osm-tile-tools/blob/master/map_utils.py#L64</a></p>
<p>So first you have to decide which ZL you want, then find the right tiles to download, then do just that. I wish I had a better code to point you to, or more time to do it myself, but with a little bit of luck you can take it from here.</p>
</div>
<div id="comment-86288-info" class="comment-info">
<span class="comment-age">(01 Dec '22, 16:36)</span> <span class="comment-user userinfo">Marcos Dione</span>
</div>
</div>
<span id="86289"></span>
<div id="comment-86289" class="comment">
<div id="post-86289-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I <em>think</em> you just need to further divide the answer by 256 to get the numbers you need.</p>
</div>
<div id="comment-86289-info" class="comment-info">
<span class="comment-age">(01 Dec '22, 17:15)</span> <span class="comment-user userinfo">Marcos Dione</span>
</div>
</div>
</div>
<div id="comment-tools-86268" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86268-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="86290"></span>

<div id="answer-container-86290" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86290-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-86290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames">https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames</a></p>
<p>But please remember, downloading a big amount of tiles is bad, and contradicts <a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Dec '22, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-86290" class="comments-container">
&#10;</div>
<div id="comment-tools-86290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86290-form-container" class="comment-form-container">
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

