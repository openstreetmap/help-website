+++
type = "question"
title = "How can i change zoom level dynamically in OpenLayers?"
description = '''I need to change zoom level dynamically in openstreet map according to displayed number of markers, means if there is only one location is marked i need more zoom and if there is more than one locations are marked i need zoom level is less( because i want to see all markers).I&#x27;m using OpenLayers lib...'''
date = "2012-07-31T05:57:00Z"
lastmod = "2012-08-28T12:40:00Z"
weight = 14713
keywords = [ "latitude", "javascript", "openlayers", "zoom" ]
aliases = [ "/questions/14713" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can i change zoom level dynamically in OpenLayers?](/questions/14713/how-can-i-change-zoom-level-dynamically-in-openlayers)

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
<span id="post-14713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14713-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to change zoom level dynamically in openstreet map according to displayed number of markers, means if there is only one location is marked i need more zoom and if there is more than one locations are marked i need zoom level is less( because i want to see all markers).I'm using OpenLayers library. Can any one help me..? Thanks in adavace...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '12, 05:57</strong></p>
<img src="https://secure.gravatar.com/avatar/954504ad2324b1cbc000a0ddc2c2ba1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pramod_ck&#39;s gravatar image" />
<p><span>pramod_ck</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pramod_ck has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jul '12, 13:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-14713" class="comments-container">
<span id="14718"></span>
<div id="comment-14718" class="comment">
<div id="post-14718-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm guessing that you're using a Javascript library to display OpenStreetMap tiles (perhaps one of the ones mentioned <a href="http://switch2osm.org/using-tiles/">here</a>)?</p>
<p>A bit more information about what you're trying to do would help.</p>
</div>
<div id="comment-14718-info" class="comment-info">
<span class="comment-age">(31 Jul '12, 11:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="14719"></span>
<div id="comment-14719" class="comment">
<div id="post-14719-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ya, I'm using OpenLayers library only. The problem is we want to display several markers on a map and want to calculate the optimal zoom-level like Google Maps does. We already calculated the centerpoint of the map but now we have a hard time to calculate the correct zoomlevel to display the whole markers..</p>
</div>
<div id="comment-14719-info" class="comment-info">
<span class="comment-age">(31 Jul '12, 11:54)</span> <span class="comment-user userinfo">pramod_ck</span>
</div>
</div>
<span id="14720"></span>
<div id="comment-14720" class="comment">
<div id="post-14720-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Which javascript library? OpenLayers or Leaflet? (you should edit your question to supply more details)</p>
</div>
<div id="comment-14720-info" class="comment-info">
<span class="comment-age">(31 Jul '12, 12:18)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
<span id="14721"></span>
<div id="comment-14721" class="comment">
<div id="post-14721-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm using OpenLayers library..</p>
</div>
<div id="comment-14721-info" class="comment-info">
<span class="comment-age">(31 Jul '12, 12:20)</span> <span class="comment-user userinfo">pramod_ck</span>
</div>
</div>
</div>
<div id="comment-tools-14713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14713-form-container" class="comment-form-container">
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

<span id="14716"></span>

<div id="answer-container-14716" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14716-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is more an OpenLayers question than an OpenStreetMap question. See openlayers.org for means to get help. What you probably want to do is use OpenLayers' "zoomToExtent" function, using an extent that you have created with reference to the sum of all your markers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '12, 10:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-14716" class="comments-container">
<span id="14717"></span>
<div id="comment-14717" class="comment">
<div id="post-14717-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Frederik Ramm</span>, Thanks. Actually i'm very new to this.. So first i need to define the bounds right..?</p>
</div>
<div id="comment-14717-info" class="comment-info">
<span class="comment-age">(31 Jul '12, 10:25)</span> <span class="comment-user userinfo">pramod_ck</span>
</div>
</div>
</div>
<div id="comment-tools-14716" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14716-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15577"></span>

<div id="answer-container-15577" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15577-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15577-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15577-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can take a look at this <a href="http://help.openstreetmap.org/questions/15152/openlayers-marker-for-start-of-gpx-track-and-centering-the-map-on-the-trace">other question</a>.</p>
<p>For zooming on your markers (the zoom will automatically be computed), you have to invoke zoomToExtent as said Frederik: map.zoomToExtent(markersLayer.getDataExtent());</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Aug '12, 12:40</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-15577" class="comments-container">
&#10;</div>
<div id="comment-tools-15577" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15577-form-container" class="comment-form-container">
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

