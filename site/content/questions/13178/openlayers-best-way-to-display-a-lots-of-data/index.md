+++
type = "question"
title = "OpenLayers - best way to display a lots of data?"
description = '''Hello, I have a slippy map over which I want to display a overlay with some highways. I have a PHP script that is getting filtered data from my local Overpass API server, send that data to OpenLayers and then visualise it in a Vector layer with a basic styling (red, yellow or green line color, based...'''
date = "2012-06-01T07:07:00Z"
lastmod = "2012-06-01T10:09:00Z"
weight = 13178
keywords = [ "performance", "openlayers" ]
aliases = [ "/questions/13178" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [OpenLayers - best way to display a lots of data?](/questions/13178/openlayers-best-way-to-display-a-lots-of-data)

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
<span id="post-13178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13178-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have a slippy map over which I want to display a overlay with some highways. I have a PHP script that is getting filtered data from my local Overpass API server, send that data to OpenLayers and then visualise it in a Vector layer with a basic styling (red, yellow or green line color, based on the smoothness tag of the highway). It works, but it doesn't scale well when there is a lot of data to be displayed. I'm talking for about 2600 ways composed of 83000 nodes. The SVG render is struggling even on comparatively new computers.</p>
<p>I don't need any fancy interactive features, the goal is just to display that data.</p>
<p>I'm thinking of a way to render transparent tiles with these ways and then just load these tiles as overlay in OpenLayers (maybe with TMS layer?). Maybe Mapnik is going to be useful here?</p>
<p>What will be the best way to display such a load?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jun '12, 07:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span></p>
</div>
</div>
<div id="comments-container-13178" class="comments-container">
&#10;</div>
<div id="comment-tools-13178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13178-form-container" class="comment-form-container">
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

<span id="13179"></span>

<div id="answer-container-13179" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13179-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ivanatora has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you've already figured out, this is too much vector data for a browser. So your best bet is definetely to convert the vector data to something raster, and mapnik is a good way to do so. I don't know what kind of data your Overpass API can generate, but if you've got the data in a Postgis database, UMN Mapserver would also be a possibility to deliver the data as a WMS layer for OpenLayers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '12, 07:51</strong></p>
<img src="https://secure.gravatar.com/avatar/30b87850d86c99d1c4f1f72c9abaeb52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frabron&#39;s gravatar image" />
<p><span>frabron</span><br />
<span class="score" title="361 reputation points">361</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frabron has 2 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-13179" class="comments-container">
&#10;</div>
<div id="comment-tools-13179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13179-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13184"></span>

<div id="answer-container-13184" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13184-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Duplicate_nodes_map">duplicate nodes map</a> is an example of a map where a lot of vector data is first rendered onto transparent tiles and then sent to the browser.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '12, 10:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-13184" class="comments-container">
&#10;</div>
<div id="comment-tools-13184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13184-form-container" class="comment-form-container">
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

