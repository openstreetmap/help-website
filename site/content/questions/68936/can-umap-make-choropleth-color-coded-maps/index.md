+++
type = "question"
title = "Can Umap make Choropleth (color coded) maps?"
description = '''Is there any way to use Umap to make a choropleth map? I&#x27;m trying to create a color coded map of registered voters in different counties. I have the KML files of the boundaries there, including the data I need that came from the converted QGIS file. But I cannot find any features to utilize this dat...'''
date = "2019-04-25T04:39:00Z"
lastmod = "2019-05-15T20:01:00Z"
weight = 68936
keywords = [ "umap" ]
aliases = [ "/questions/68936" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can Umap make Choropleth (color coded) maps?](/questions/68936/can-umap-make-choropleth-color-coded-maps)

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
<span id="post-68936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68936-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there any way to use Umap to make a choropleth map? I'm trying to create a color coded map of registered voters in different counties. I have the KML files of the boundaries there, including the data I need that came from the converted QGIS file. But I cannot find any features to utilize this data.</p>
<p>I can make a choropleth map on QGIS with the data, but I want the map to be an interactive, slippy map that I can embed on a website.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '19, 04:39</strong></p>
<img src="https://secure.gravatar.com/avatar/b5127c487b0bb39fad19a167cdb63108?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SocialMapper&#39;s gravatar image" />
<p><span>SocialMapper</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SocialMapper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68936" class="comments-container">
&#10;</div>
<div id="comment-tools-68936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68936-form-container" class="comment-form-container">
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

<span id="68996"></span>

<div id="answer-container-68996" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68996-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the closest you get is a heat map as for example on <a href="https://umap.openstreetmap.fr/en/map/heatmap_111284#14/43.5307/5.4507">this page</a>. I'm afraid a real choropleth map is not possible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '19, 09:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-68996" class="comments-container">
<span id="69189"></span>
<div id="comment-69189" class="comment">
<div id="post-69189-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Apologies for the late reply.</p>
<p>Bummer. Not even if it's already imported with the choropleth symbology in place? I've been trying all of the file formats, and can't get it to import anything beyond just the basic shapefile. Do you know of a file format or export setting that keeps the symbology in place?</p>
<p>My solution for one project was to manually color each section, but this new project has more than 9,000 sections... Are you sure that it's simply not possible? I'm trying really hard to come up with creative solutions. How about even just importing an image, such as a JPEG or PDF, to overlay?</p>
</div>
<div id="comment-69189-info" class="comment-info">
<span class="comment-age">(15 May '19, 01:06)</span> <span class="comment-user userinfo">SocialMapper</span>
</div>
</div>
<span id="69200"></span>
<div id="comment-69200" class="comment">
<div id="post-69200-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I haven't tried it but have a look a <a href="https://github.com/umap-project/umap/issues/494">issue 494</a> on Github. The answer by M-Rick might give you a clue on how to do this.</p>
</div>
<div id="comment-69200-info" class="comment-info">
<span class="comment-age">(15 May '19, 20:01)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-68996" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68996-form-container" class="comment-form-container">
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

