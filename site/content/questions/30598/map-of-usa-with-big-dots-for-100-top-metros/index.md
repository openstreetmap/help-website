+++
type = "question"
title = "Map of USA with big dots for 100 top metros"
description = '''I want to create a map of the USA that highlights the top 100 metro markets. I want four markets -- New York, Chicago, Washington and Seattle -- to be highlighted in one color and the other 96 markets to be highlighted in another color. This would be the source for the top 100 markets --http://en.wi...'''
date = "2014-02-10T21:01:00Z"
lastmod = "2014-02-11T00:13:00Z"
weight = 30598
keywords = [ "metros", "metromarkets", "top100" ]
aliases = [ "/questions/30598" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Map of USA with big dots for 100 top metros](/questions/30598/map-of-usa-with-big-dots-for-100-top-metros)

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
<span id="post-30598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30598-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to create a map of the USA that highlights the top 100 metro markets. I want four markets -- New York, Chicago, Washington and Seattle -- to be highlighted in one color and the other 96 markets to be highlighted in another color. This would be the source for the top 100 markets --<a href="http://en.wikipedia.org/wiki/List_of_Metropolitan_Statistical_Areas">http://en.wikipedia.org/wiki/List_of_Metropolitan_Statistical_Areas</a></p>
<p>Any tips on how I can do this? Thanks for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-metros" rel="tag" title="see questions tagged &#39;metros&#39;">metros</span> <span class="post-tag tag-link-metromarkets" rel="tag" title="see questions tagged &#39;metromarkets&#39;">metromarkets</span> <span class="post-tag tag-link-top100" rel="tag" title="see questions tagged &#39;top100&#39;">top100</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '14, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/44c986894481ffffc674d136d64639e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomGrubisich&#39;s gravatar image" />
<p><span>TomGrubisich</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomGrubisich has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30598" class="comments-container">
&#10;</div>
<div id="comment-tools-30598" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30598-form-container" class="comment-form-container">
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

<span id="30603"></span>

<div id="answer-container-30603" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30603-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Various methods are possible. You could use an OpenLayers or Leaflet map embedded in a web site (this will be zoomable and pannable) and save your 100 dots in a KML/GeoJSON file which you could create with any suitable editor (among others, Google Earth). Then instruct OpenLayers/Leaflet to display your file.</p>
<p>There are platforms, e.g. Github, where you can simply drop in a GeoJSON file to have it shown as a map.</p>
<p>If you'd rather have an image generated (and not some kind of web map), you'll probably not want to use OSM since it is a much too detailed data set - just create a KML file or Shape file or something with your markers in it, fire up a GIS editor like Quantum GIS, load a background GeoTIFF from somewhere, and put your dots on top.</p>
<p>All these methods will require that you have coordinates for your dots, not just city or region names. If all you have is names, you need to run them through a geocoder first to get coordinates.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '14, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30603" class="comments-container">
<span id="30608"></span>
<div id="comment-30608" class="comment">
<div id="post-30608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also, all methods will require some scripting and/or programming.</p>
</div>
<div id="comment-30608-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 00:13)</span> <span class="comment-user userinfo">jgpacker</span>
</div>
</div>
</div>
<div id="comment-tools-30603" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30603-form-container" class="comment-form-container">
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

