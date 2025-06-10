+++
type = "question"
title = "does not load well without the inspector"
description = '''Hi! The map is displayed correctly only if I open the code inspector. Why? If I don&#x27;t open the inspector it only loads one image, without centering and the others are grayed out.'''
date = "2021-06-07T11:45:00Z"
lastmod = "2021-06-07T14:17:00Z"
weight = 80449
keywords = [ "openstreetmap", "inspector" ]
aliases = [ "/questions/80449" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [does not load well without the inspector](/questions/80449/does-not-load-well-without-the-inspector)

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
<span id="post-80449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80449-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! The map is displayed correctly only if I open the code inspector. Why? If I don't open the inspector it only loads one image, without centering and the others are grayed out.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-inspector" rel="tag" title="see questions tagged &#39;inspector&#39;">inspector</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '21, 11:45</strong></p>
<img src="https://secure.gravatar.com/avatar/d802ed787d1cd07d08bec09c5922006d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lilu44&#39;s gravatar image" />
<p><span>Lilu44</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lilu44 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80449" class="comments-container">
<span id="80450"></span>
<div id="comment-80450" class="comment">
<div id="post-80450-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain a bit more about where you see this problem? What sort of machine are you using? Which operating system is it using? Which web browser? Which version?</p>
</div>
<div id="comment-80450-info" class="comment-info">
<span class="comment-age">(07 Jun '21, 12:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="80451"></span>
<div id="comment-80451" class="comment">
<div id="post-80451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I load the map it doesn't center it inside the div, just an image appears. Then I open the inspector and load the other images and center the map inside the div. I use an Ubuntu 20 operating system, and I see the map from the Mozilla Firefox 1.0 browser. Thanks for your reply.</p>
</div>
<div id="comment-80451-info" class="comment-info">
<span class="comment-age">(07 Jun '21, 12:17)</span> <span class="comment-user userinfo">Lilu44</span>
</div>
</div>
<span id="80452"></span>
<div id="comment-80452" class="comment">
<div id="post-80452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to confirm - you're just browsing to "https://www.openstreetmap.org" , you're not trying to do anything "clever" like trying to embed <a href="https://www.openstreetmap.org">https://www.openstreetmap.org</a> as part of a different website?</p>
<p>There is no "Ubuntu 20", but presumably your are using "Ubuntu 20.04" or "Ubuntu 20.10".</p>
<p>Are you really using verion 1.0 of Firefox? This seems unlikely.</p>
</div>
<div id="comment-80452-info" class="comment-info">
<span class="comment-age">(07 Jun '21, 12:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="80453"></span>
<div id="comment-80453" class="comment">
<div id="post-80453-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok I think I have not explained myself well. I am using Leaflet and I access openstreetmap. This is the code: var map = L.map ( "map", { center: [markers [0] [1], markers [0] [2]], zoom: 10, zoomControl: true, preferCanvas: false, } );</p>
<p>var tile_layer = L.tileLayer ( "https: // {s} .tile.openstreetmap.org / {z} / {x} / {y} .png", {"attribution": "Data by \ u0026copy; \ u003ca href = \" http: //openstreetmap.org \ "\ u003eOpenStreetMap \ u003c / a \ u003e, under \ u003ca href = \" http: //www.openstreetmap. org / copyright \ "\ u003eODbL \ u003c / a \ u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false} ) .addTo (mapper);</p>
<p>And I think the problem is in openstreetmap.org.</p>
</div>
<div id="comment-80453-info" class="comment-info">
<span class="comment-age">(07 Jun '21, 12:50)</span> <span class="comment-user userinfo">Lilu44</span>
</div>
</div>
<span id="80455"></span>
<div id="comment-80455" class="comment">
<div id="post-80455-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you want to compare your code with some that works have a look at <a href="https://github.com/SomeoneElseOSM/mod_tile/blob/switch2osm/extra/sample_leaflet.html">https://github.com/SomeoneElseOSM/mod_tile/blob/switch2osm/extra/sample_leaflet.html</a> .</p>
</div>
<div id="comment-80455-info" class="comment-info">
<span class="comment-age">(07 Jun '21, 14:17)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-80449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80449-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

