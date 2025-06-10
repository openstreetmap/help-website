+++
type = "question"
title = "Export roads with maxspeed"
description = '''Hi! I need to export all roads in the netherlands together with their maxspeed. I exported the osm.pbf file through geofabrik.de and imported this in postgresql with osm2psql. However, this data does not contain the maxspeed attribute, is there a method to extract all roads together with their maxsp...'''
date = "2020-11-26T13:37:00Z"
lastmod = "2020-11-26T15:17:00Z"
weight = 77727
keywords = [ "maxspeed", "pbf", "geofabrik" ]
aliases = [ "/questions/77727" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export roads with maxspeed](/questions/77727/export-roads-with-maxspeed)

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
<span id="post-77727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77727-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I need to export all roads in the netherlands together with their maxspeed. I exported the osm.pbf file through geofabrik.de and imported this in postgresql with osm2psql. However, this data does not contain the maxspeed attribute, is there a method to extract all roads together with their maxspeed value for a particular country?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '20, 13:37</strong></p>
<img src="https://secure.gravatar.com/avatar/440770b5459b1dde59b35ece6c02e4e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="faster043&#39;s gravatar image" />
<p><span>faster043</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="faster043 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77727" class="comments-container">
&#10;</div>
<div id="comment-tools-77727" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77727-form-container" class="comment-form-container">
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

<span id="77734"></span>

<div id="answer-container-77734" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77734-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your approach is good. You need to modify osm2pgsql's ".style" file to include a maxspeed column (maxspeed is not required for rendering hence is not part of the default schema) or alternatively use the <code>--hstore</code> option on import which will put all tags into a special "tags" column, and then you'll get the data you are looking for.</p>
<p>(If you're modifying the .style file, you can also throw away anything not related to roads - that will speed up your import and waste less space.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '20, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-77734" class="comments-container">
<span id="77735"></span>
<div id="comment-77735" class="comment">
<div id="post-77735-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! Hstore did it for me</p>
</div>
<div id="comment-77735-info" class="comment-info">
<span class="comment-age">(26 Nov '20, 15:17)</span> <span class="comment-user userinfo">faster043</span>
</div>
</div>
</div>
<div id="comment-tools-77734" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77734-form-container" class="comment-form-container">
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

