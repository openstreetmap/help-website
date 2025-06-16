+++
type = "question"
title = "want to create live map"
description = '''Hi All, I want to create a live map for control cars on road. I am getting confused to implement this idea. My confusion is how to start it there is mapbox and osm i don&#x27;t know which one to use. My requirement are:  I can edit the road for adding custom symbol etc. I can controls the cars on road. i...'''
date = "2017-07-31T07:16:00Z"
lastmod = "2017-07-31T10:04:00Z"
weight = 57360
keywords = [ "tiles", "osm", "mapbox" ]
aliases = [ "/questions/57360" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [want to create live map](/questions/57360/want-to-create-live-map)

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
<span id="post-57360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57360-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All, I want to create a live map for control cars on road. I am getting confused to implement this idea. My confusion is how to start it there is mapbox and osm i don't know which one to use. My requirement are:</p>
<ul>
<li>I can edit the road for adding custom symbol etc.</li>
<li>I can controls the cars on road.</li>
<li>i can see the moving cars like uber</li>
</ul>
<p>i will very thankful if somebody suggest me. thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mapbox" rel="tag" title="see questions tagged &#39;mapbox&#39;">mapbox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '17, 07:16</strong></p>
<img src="https://secure.gravatar.com/avatar/eecd18e88ba24f34288376a42092babe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anuj-786&#39;s gravatar image" />
<p><span>Anuj-786</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anuj-786 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57360" class="comments-container">
&#10;</div>
<div id="comment-tools-57360" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57360-form-container" class="comment-form-container">
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

<span id="57362"></span>

<div id="answer-container-57362" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57362-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57362-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57362-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you are asking for is a larger, commercial-grade system and you will have to do a lot of research yourself, but as a general sketch you are looking for:</p>
<ol>
<li>a background map that simply shows roads, place names and so on; this is usually made from tiles and these tiles are made from OpenStreetMap data; you can install the software that makes these tiles yourself, or you can buy the service from a vendor like Mapbox (see <a href="https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">https://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services</a> for other vendors).</li>
<li>a database in which you keep your own annotations (custom symbols for roads etc.) because you don't want to upload that to OpenStreetMap</li>
<li>a system that collects the vehicle locatios and stores them in a database</li>
<li>a front-end that displays the background map, your annotation overlay, and a vehicle overlay; some tile vendors will have their own libraries you can use, or you could use the Open Source libraries Leaflet or OpenLayers (for a web app)</li>
</ol>
<p>I'm not sure how you want to "control cars on the road" but that componet would also have to be added.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '17, 09:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-57362" class="comments-container">
<span id="57364"></span>
<div id="comment-57364" class="comment">
<div id="post-57364-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hi Frederik, thanks a lot answer. In simple suppose i vane 10 cars and they are in city and i want to controls those cars. controls mean i can see where is my car1, car2 ... car10 and also cane see the moving direction of cars like they are still are runnig.</p>
</div>
<div id="comment-57364-info" class="comment-info">
<span class="comment-age">(31 Jul '17, 10:04)</span> <span class="comment-user userinfo">Anuj-786</span>
</div>
</div>
</div>
<div id="comment-tools-57362" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57362-form-container" class="comment-form-container">
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

