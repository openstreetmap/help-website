+++
type = "question"
title = "Best practices for making a Custom Marathon route map"
description = '''I&#x27;m helping my city update their website with a new map of a 5K race. I&#x27;d like to use OSM for the map. Obviously I could screenshot it and exit in a drawing app. But I&#x27;d like to do it the &quot;right way&quot; and end up with an embeddable osm map applet they can use, or export to svg or png. I need to show t...'''
date = "2022-04-29T20:34:00Z"
lastmod = "2022-04-30T08:03:00Z"
weight = 84310
keywords = [ "map", "route", "5k", "marathon" ]
aliases = [ "/questions/84310" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best practices for making a Custom Marathon route map](/questions/84310/best-practices-for-making-a-custom-marathon-route-map)

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
<span id="post-84310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84310-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm helping my city update their website with a new map of a 5K race. I'd like to use OSM for the map. Obviously I could screenshot it and exit in a drawing app. But I'd like to do it the "right way" and end up with an embeddable osm map applet they can use, or export to svg or png.</p>
<p>I need to show the path to run, and the altitude. directional arrows, and I need to be able to force certain street names to show, and perhaps hide others. (I assume this is normally handled automatically, by how zoomed in one is on the map.)</p>
<p>I made a gpx file on osmand that shows the route decently well (aside from the forced visible/notvisible street names. Where should I go from here?</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screenshot_20220428-100620(1).png" alt="osmand screenshot" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-5k" rel="tag" title="see questions tagged &#39;5k&#39;">5k</span> <span class="post-tag tag-link-marathon" rel="tag" title="see questions tagged &#39;marathon&#39;">marathon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '22, 20:34</strong></p>
<img src="https://secure.gravatar.com/avatar/05e87e7fa820adca2ab4d7b297aff3a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="9u2&#39;s gravatar image" />
<p><span>9u2</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="9u2 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-84310" class="comments-container">
&#10;</div>
<div id="comment-tools-84310" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84310-form-container" class="comment-form-container">
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

<span id="84313"></span>

<div id="answer-container-84313" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84313-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are some bits of information missing: should the map be static, or should users be able to zoom and pan?</p>
<p>In any case the usual way to do this is to display the route as a separate "layer" on top of a existing base map source. For example using <a href="https://leafletjs.com/">leaflet</a> for raster map tiles or Mapbox GL / <a href="https://maplibre.org/">MapLibre</a> for vector tiles.</p>
<p>You could choose something as a base map that works well as a background (so not the standard style from openstreetmap.org). If you really need to customize things the easiest solution if probably to modify an existing vector style.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '22, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-84313" class="comments-container">
&#10;</div>
<div id="comment-tools-84313" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84313-form-container" class="comment-form-container">
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

