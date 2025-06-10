+++
type = "question"
title = "An error occurred while loading the map layer &#x27;default&#x27;: , No Attribute type error"
description = '''Hello. While styling my maps in Tilemill I&#x27;ll get a No Attribute Type error when the layers have the attributes like type and name. Then on loading the xml file in Mapnik and running it, I&#x27;ll get An error occurred while loading the map layer &#x27;default&#x27;: boost::filesystem::status: Permission denied: &quot;...'''
date = "2014-12-16T07:38:00Z"
lastmod = "2014-12-16T08:46:00Z"
weight = 39590
keywords = [ "tilemill", "errors", "mapnik" ]
aliases = [ "/questions/39590" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [An error occurred while loading the map layer 'default': , No Attribute type error](/questions/39590/an-error-occurred-while-loading-the-map-layer-default-no-attribute-type-error)

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
<span id="post-39590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39590-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello. While styling my maps in Tilemill I'll get a No Attribute Type error when the layers have the attributes like type and name. Then on loading the xml file in Mapnik and running it, I'll get An error occurred while loading the map layer 'default': boost::filesystem::status: Permission denied: "/home/carol/Documents/MapBox/project/Open_Uganda/layers/Roads/ne_10m_roads.shp". I have tried deleting the 'problematic' layers, but it simply goes to the next one.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tilemill" rel="tag" title="see questions tagged &#39;tilemill&#39;">tilemill</span> <span class="post-tag tag-link-errors" rel="tag" title="see questions tagged &#39;errors&#39;">errors</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '14, 07:38</strong></p>
<img src="https://secure.gravatar.com/avatar/cc0de1b5d71fb7c74799148889048261?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20SSali&#39;s gravatar image" />
<p><span>David SSali</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David SSali has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39590" class="comments-container">
&#10;</div>
<div id="comment-tools-39590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39590-form-container" class="comment-form-container">
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

<span id="39591"></span>

<div id="answer-container-39591" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39591-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39591-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-39591-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is an OpenStreetMap support site. Tilemill is a commercial product made and supported by Mapbox, and any Tilemill specific issues should be <a href="https://www.mapbox.com/help/">raised with them.</a></p>
<p>As for the Mapnik XML - who is Carol and why are you using her files? If the file ne_10m_roads.shp really resides in the given path, then make sure you have access permissions to that. Else open the XML in an editor and search+replace the paths to the shapefiles so that they point to wherever you have saved your shape files to. (Is it possible that you designed the style on one machine and are running it on another, and have only copied the XML and not the supporting shape files?)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '14, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-39591" class="comments-container">
<span id="39593"></span>
<div id="comment-39593" class="comment">
<div id="post-39593-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Tilemill is open source and has been largely abandoned by Mapbox in favour of Mapbox Studio. I don't think it's unreasonable for questions about it to be asked here.</p>
</div>
<div id="comment-39593-info" class="comment-info">
<span class="comment-age">(16 Dec '14, 08:46)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-39591" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39591-form-container" class="comment-form-container">
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

