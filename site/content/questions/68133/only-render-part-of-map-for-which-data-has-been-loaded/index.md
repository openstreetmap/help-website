+++
type = "question"
title = "Only render part of map for which data has been loaded"
description = '''I have successfully setup a tile server and loaded data for one country using the guide found at https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/ When I use this tile server, I do still see the outline of all other countries in the world. The country I loaded data for has ...'''
date = "2019-02-25T10:48:00Z"
lastmod = "2019-02-25T10:59:00Z"
weight = 68133
keywords = [ "country", "outline", "remove" ]
aliases = [ "/questions/68133" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Only render part of map for which data has been loaded](/questions/68133/only-render-part-of-map-for-which-data-has-been-loaded)

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
<span id="post-68133-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68133-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68133-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have successfully setup a tile server and loaded data for one country using the guide found at <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/</a></p>
<p>When I use this tile server, I do still see the outline of all other countries in the world. The country I loaded data for has details.</p>
<p>Is it possible to prevent the country outline to show ?</p>
<p>Thx</p>
<p>Torben</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span> <span class="post-tag tag-link-outline" rel="tag" title="see questions tagged &#39;outline&#39;">outline</span> <span class="post-tag tag-link-remove" rel="tag" title="see questions tagged &#39;remove&#39;">remove</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '19, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/1401ff54baa5e5029003f06629a89efb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TSkov&#39;s gravatar image" />
<p><span>TSkov</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TSkov has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68133" class="comments-container">
&#10;</div>
<div id="comment-tools-68133" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68133-form-container" class="comment-form-container">
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

<span id="68134"></span>

<div id="answer-container-68134" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68134-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TSkov has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The country outlines as well as the land/sea mask come from shape files that you have downloaded as part of the installation procedure. You can modify these shape files either on the command line with ogr2ogr, or in a GUI with QGIS, removing the parts you do not want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '19, 10:59</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68134" class="comments-container">
&#10;</div>
<div id="comment-tools-68134" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68134-form-container" class="comment-form-container">
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

