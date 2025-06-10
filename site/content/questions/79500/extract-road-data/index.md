+++
type = "question"
title = "Extract Road Data"
description = '''Hi I need the exact data of a road for a project. Is it possible to read the reference points of a road from OSM? Or rather, where are these reference points located? The goal would be that I then connect these reference points using splines and can then calculate the curvature of the road. For this...'''
date = "2021-04-02T15:28:00Z"
lastmod = "2021-04-02T16:32:00Z"
weight = 79500
keywords = [ "read", "data", "road" ]
aliases = [ "/questions/79500" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract Road Data](/questions/79500/extract-road-data)

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
<span id="post-79500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79500-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I need the exact data of a road for a project. Is it possible to read the reference points of a road from OSM? Or rather, where are these reference points located? The goal would be that I then connect these reference points using splines and can then calculate the curvature of the road. For this it would be important to know where the reference points are located (e.g. in the middle of the road). So that I can start from this one spline then calculate the edges of the road.</p>
<p>Thanks a lot for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-read" rel="tag" title="see questions tagged &#39;read&#39;">read</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Apr '21, 15:28</strong></p>
<img src="https://secure.gravatar.com/avatar/9ad1ee024304620384c7885deae821e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martin912&#39;s gravatar image" />
<p><span>martin912</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martin912 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79500" class="comments-container">
&#10;</div>
<div id="comment-tools-79500" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79500-form-container" class="comment-form-container">
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

<span id="79501"></span>

<div id="answer-container-79501" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79501-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, identify the ID of the OSM "way" object that you want to download. (If the road is long, there might be more than one way object.) Then, download <a href="https://api.openstreetmap.org/api/0.6/way/ID/full">https://api.openstreetmap.org/api/0.6/way/ID/full</a> (where ID is the ID you identified earlier). This returns an XML representation of the road and coordinates for all its nodes (what you call reference points). These will usually be in the middle of the road, but don't rely on accuracy too much since the GPS tracks and aerial imagery we use can easily be a few metres off.</p>
<p>If you want to do this for more than just a few roads, the above method will not work as you will be downloading too much data from the API. In that case, it is easiest to download an .osm.pbf file for the region you are interested in and either process that yourself (with e.g. the Osmium library or pyosmium) or load it into a PostgreSQL database with osm2pgsql and take it from there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Apr '21, 15:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-79501" class="comments-container">
<span id="79504"></span>
<div id="comment-79504" class="comment">
<div id="post-79504-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot!</p>
<p>I just want to do that for a small part of a street. I want to analyze a few different street situtations. Is there a opportunity to read out this nodes from the xml file?</p>
</div>
<div id="comment-79504-info" class="comment-info">
<span class="comment-age">(02 Apr '21, 16:32)</span> <span class="comment-user userinfo">martin912</span>
</div>
</div>
</div>
<div id="comment-tools-79501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79501-form-container" class="comment-form-container">
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

