+++
type = "question"
title = "local map server in tile layer"
description = '''Hi, I have a local tile server which is setup using mapnik. Following code is not working when I add my local map server URL. Please tell me how can I add my local map in below sample code. Is there anything I need to do from serverside? Sample Code: layers: [  new ol.layer.Tile({  source: new ol.so...'''
date = "2017-02-16T11:54:00Z"
lastmod = "2017-02-16T12:08:00Z"
weight = 54673
keywords = [ "map", "local" ]
aliases = [ "/questions/54673" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [local map server in tile layer](/questions/54673/local-map-server-in-tile-layer)

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
<span id="post-54673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54673-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have a local tile server which is setup using mapnik.</p>
<p>Following code is not working when I add my local map server URL.</p>
<p>Please tell me how can I add my local map in below sample code. Is there anything I need to do from serverside?</p>
<p>Sample Code:</p>
<p>layers: [ new ol.layer.Tile({ source: new ol.source.OSM({ url: 'http://testmap.com/{z}/{x}/{y}.png' }) }),</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '17, 11:54</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54673" class="comments-container">
&#10;</div>
<div id="comment-tools-54673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54673-form-container" class="comment-form-container">
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

<span id="54674"></span>

<div id="answer-container-54674" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54674-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54674-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54674-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I assume that you have properly set up either renderd or tirex. If not, do that first. Then you need to have your ModTile directives in the Apache config set accordingly. If you want tiles to be available under / like in your above example, and if your map style is called "osm", then you'd need</p>
<pre><code>AddTileConfig / osm</code></pre>
<p>Read more here: <a href="https://github.com/openstreetmap/mod_tile/blob/master/mod_tile.conf">https://github.com/openstreetmap/mod_tile/blob/master/mod_tile.conf</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '17, 12:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '17, 12:08</strong> </span></p>
</div>
</div>
<div id="comments-container-54674" class="comments-container">
&#10;</div>
<div id="comment-tools-54674" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54674-form-container" class="comment-form-container">
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

