+++
type = "question"
title = "Where are the baselayers and overlays defind in osm ?"
description = '''In top right corner there is a &quot;+&quot; menu that has a lot of baselayers and overlays. Where is that menu defined?'''
date = "2011-11-16T15:41:00Z"
lastmod = "2011-11-17T14:18:00Z"
weight = 9036
keywords = [ "osm", "openlayers" ]
aliases = [ "/questions/9036" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Where are the baselayers and overlays defind in osm ?](/questions/9036/where-are-the-baselayers-and-overlays-defind-in-osm)

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
<span id="post-9036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9036-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In top right corner there is a "+" menu that has a lot of baselayers and overlays. Where is that menu defined?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '11, 15:41</strong></p>
<img src="https://secure.gravatar.com/avatar/dc9b01669c0702f230fa57c384b947a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexz&#39;s gravatar image" />
<p><span>alexz</span><br />
<span class="score" title="225 reputation points">225</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9036" class="comments-container">
&#10;</div>
<div id="comment-tools-9036" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9036-form-container" class="comment-form-container">
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

<span id="9039"></span>

<div id="answer-container-9039" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9039-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9039-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-9039-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The main bit of javascript for doing this is a map.js file. In the rails app on github, you can find this under '<a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/app/assets/javascripts">/app/assets/map.js.erb</a>'</p>
<p>OpenLayers has some built-in pre-packaging of definitions of OpenStreetMap layers. We have a local (modified?) <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/public/openlayers/OpenStreetMap.js">copy of this in our repo here</a> ...but this comes <em>with</em> OpenLayers.</p>
<p>But perhaps you're looking for more basic information: The OpenStreetMap front page uses OpenLayers, but it is not the easiest place to learn about how to invoke OpenLayers. Here's <a href="http://harrywood.co.uk/maps/examples/openlayers/many-layers.html">an easier example of invoking OpenLayers with many layers</a> (do 'view source' to see how that works)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '11, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '11, 16:11</strong> </span></p>
</div>
</div>
<div id="comments-container-9039" class="comments-container">
<span id="9055"></span>
<div id="comment-9055" class="comment">
<div id="post-9055-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for that but i was looking for the definition of the menu itself. I want to add there a new layer: the marker's layer, the one that is activated when the request has mlon and mlat values. I use it to add some popup markers. I want that layer to be in the menu too.</p>
</div>
<div id="comment-9055-info" class="comment-info">
<span class="comment-age">(17 Nov '11, 07:29)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
</div>
<div id="comment-tools-9039" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9039-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9069"></span>

<div id="answer-container-9069" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9069-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9069-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-9069-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The '+' is a standard feature of OpenLayers, which is one of the javascript libraries that can be used to present a movable map (slippy map) on a web page. An alternate library is Leaflet; read more at <a href="http://leaflet.cloudmade.com">http://leaflet.cloudmade.com</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '11, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-9069" class="comments-container">
<span id="9075"></span>
<div id="comment-9075" class="comment">
<div id="post-9075-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thx, but i don't want to implement a different technology.</p>
</div>
<div id="comment-9075-info" class="comment-info">
<span class="comment-age">(17 Nov '11, 14:18)</span> <span class="comment-user userinfo">alexz</span>
</div>
</div>
</div>
<div id="comment-tools-9069" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9069-form-container" class="comment-form-container">
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

