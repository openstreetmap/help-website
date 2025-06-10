+++
type = "question"
title = "How to render a map using of TopoMap data"
description = '''I have downloaded tiles data using of TopoMap tool now i am not able to render the map using of that data in javascript .. can anyone help me to render map I need to show map to client in offline..'''
date = "2015-07-03T10:06:00Z"
lastmod = "2015-07-04T05:43:00Z"
weight = 43941
keywords = [ "topomap" ]
aliases = [ "/questions/43941" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to render a map using of TopoMap data](/questions/43941/how-to-render-a-map-using-of-topomap-data)

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
<span id="post-43941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43941-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have downloaded tiles data using of TopoMap tool now i am not able to render the map using of that data in javascript .. can anyone help me to render map I need to show map to client in offline..</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-topomap" rel="tag" title="see questions tagged &#39;topomap&#39;">topomap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '15, 10:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0ab63d5826eb4caf1559f1d14eaaa877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mayee&#39;s gravatar image" />
<p><span>Mayee</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mayee has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43941" class="comments-container">
<span id="43965"></span>
<div id="comment-43965" class="comment">
<div id="post-43965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Plz. tell us what topomap tool?</p>
</div>
<div id="comment-43965-info" class="comment-info">
<span class="comment-age">(03 Jul '15, 22:31)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="43967"></span>
<div id="comment-43967" class="comment">
<div id="post-43967-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have downloaded TopoMapCreator_Setup1.7.0.16 executable file from <a href="https://sourceforge.net/projects/topomapcreator/">https://sourceforge.net/projects/topomapcreator/</a> URL.This file is used to download tiles from map. It is good tool to download tiles but my problem is i am not able to render map with using of this data.</p>
<p>I think this is not OSM tool.</p>
<p>I want to save some tiles data in cache and with using of that data i need to render map .. If any alternatives are there in OSM offline map please let me know .. My target is to generate map in offline.</p>
</div>
<div id="comment-43967-info" class="comment-info">
<span class="comment-age">(04 Jul '15, 05:43)</span> <span class="comment-user userinfo">Mayee</span>
</div>
</div>
</div>
<div id="comment-tools-43941" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43941-form-container" class="comment-form-container">
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

<span id="43944"></span>

<div id="answer-container-43944" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43944-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-43944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I do not know what the "TopoMap tool" is and where you have downloaded your tiles. If you have downloaded tiles into a directory and these tiles conform to the standard z/x/y.png structure, then you can simply set up a local web page with OpenLayers or Leaflet, and instead of a tile server, you specify a "file: URL" as the location (or indeed any relative URL if the local web page has already been called through a file URL).</p>
<p><a href="http://wiki.openstreetmap.org/wiki/OpenLayers_Local_Tiles_Example">http://wiki.openstreetmap.org/wiki/OpenLayers_Local_Tiles_Example</a> may have an example you can work from.</p>
<p>Note that downloading large amounts of tiles from OSM for offline use is <a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy">not allowed.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jul '15, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-43944" class="comments-container">
&#10;</div>
<div id="comment-tools-43944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43944-form-container" class="comment-form-container">
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

