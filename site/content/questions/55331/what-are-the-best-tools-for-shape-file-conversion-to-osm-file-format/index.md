+++
type = "question"
title = "What are the best tools for shape file conversion to OSM file format?"
description = '''I just wanna know which tool most suitable to shape file conversion to OSM file. '''
date = "2017-03-29T17:28:00Z"
lastmod = "2017-04-03T21:15:00Z"
weight = 55331
keywords = [ "shape2osm", "conversiontools" ]
aliases = [ "/questions/55331" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What are the best tools for shape file conversion to OSM file format?](/questions/55331/what-are-the-best-tools-for-shape-file-conversion-to-osm-file-format)

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
<span id="post-55331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55331-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just wanna know which tool most suitable to shape file conversion to OSM file.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shape2osm" rel="tag" title="see questions tagged &#39;shape2osm&#39;">shape2osm</span> <span class="post-tag tag-link-conversiontools" rel="tag" title="see questions tagged &#39;conversiontools&#39;">conversiontools</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '17, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/99480e0ac05603b995d9b1f3330566f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MalingaGIS&#39;s gravatar image" />
<p><span>MalingaGIS</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MalingaGIS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55331" class="comments-container">
&#10;</div>
<div id="comment-tools-55331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55331-form-container" class="comment-form-container">
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

<span id="55332"></span>

<div id="answer-container-55332" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55332-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-55332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please understand that we have rules that must be followed for data imports, see <a href="http://wiki.openstreetmap.org/wiki/Import">http://wiki.openstreetmap.org/wiki/Import</a> for details. Under no circumstances should you simply convert a shape file from any external source and upload it to OpenStreetMap without prior discussion. Among other things, such discussion will help you ensure the license is compatible and the tagging is useful.</p>
<p>Having said that, there are a couple of command line tools (shp2osm, polyshp2osm) and there's also the "OpenData" plugin for JOSM that allows you to open shape files in the editor. If you are specifically talking about shape files obtained from HERE and you want to use them to run OSM software with them, try the "Morituri" converter from <a href="https://github.com/knowname/morituri">https://github.com/knowname/morituri</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '17, 19:21</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-55332" class="comments-container">
<span id="55351"></span>
<div id="comment-55351" class="comment">
<div id="post-55351-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much Frederik Ramm, Yeah I was read and understand the OSM import rules. I don't wanna do bulk imports. I just wanna know what are the tools for "Shape2OSM conversion. Recently I am using "OpenData" for JOSM.</p>
<p>Thanks again to you, your answer very useful to me, will check the "Morituri" Converter.</p>
</div>
<div id="comment-55351-info" class="comment-info">
<span class="comment-age">(30 Mar '17, 04:11)</span> <span class="comment-user userinfo">MalingaGIS</span>
</div>
</div>
<span id="55463"></span>
<div id="comment-55463" class="comment">
<div id="post-55463-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... ot see <a href="https://wiki.openstreetmap.org/wiki/Shapefiles">https://wiki.openstreetmap.org/wiki/Shapefiles</a></p>
</div>
<div id="comment-55463-info" class="comment-info">
<span class="comment-age">(03 Apr '17, 21:15)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-55332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55332-form-container" class="comment-form-container">
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

