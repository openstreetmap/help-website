+++
type = "question"
title = "osmcoastline"
description = '''Hello, I have some problems with osmcoastline, hope some can help ! I want to extract the land polygons and want them in shape-format. osmcoastline -V osmcoastline version 2.1.2 Copyright (C) 2012-2016 Jochen Topf jochen@topf.org License: GNU GENERAL PUBLIC LICENSE Version 3 http://gnu.org/licenses/...'''
date = "2020-02-17T08:37:00Z"
lastmod = "2020-02-18T09:07:00Z"
weight = 73110
keywords = [ "osmcoastline" ]
aliases = [ "/questions/73110" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmcoastline](/questions/73110/osmcoastline)

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
<span id="post-73110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73110-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have some problems with osmcoastline, hope some can help ! I want to extract the land polygons and want them in shape-format.</p>
<p>osmcoastline -V osmcoastline version 2.1.2 Copyright (C) 2012-2016 Jochen Topf <a href="mailto:jochen@topf.org">jochen@topf.org</a> License: GNU GENERAL PUBLIC LICENSE Version 3 <a href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>. This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<p>I run osmcoastline: osmcoastline -o coastline.db cyprus-latest.osm.pbf There were 0 warnings. There were 0 errors.</p>
<p>Then I want the output in shape-format: ogr2ogr -f "ESRI Shapefile" land_polygons.shp coastline.db land_polygons FAILURE: Unable to open datasource <code>coastline.db' with the following drivers. -&gt;</code>PCIDSK' + long list of alternative formats</p>
<p>Am I doing something wrong? How to get the data in shape-format ?</p>
<p>Best regards Håvard</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmcoastline" rel="tag" title="see questions tagged &#39;osmcoastline&#39;">osmcoastline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '20, 08:37</strong></p>
<img src="https://secure.gravatar.com/avatar/db5b7b23235694ee1b9ef036a4393416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HaavardHolm&#39;s gravatar image" />
<p><span>HaavardHolm</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HaavardHolm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73110" class="comments-container">
&#10;</div>
<div id="comment-tools-73110" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73110-form-container" class="comment-form-container">
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

<span id="73115"></span>

<div id="answer-container-73115" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73115-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, there are pregenerated coastlines available from <a href="https://osmdata.openstreetmap.de/">here</a>. It might be easier to just use those. Second, your version of osmcoastline is pretty old, I'd suggest using a more current version. Third, it seems osmcoastline did its job and ogr2ogr didn't so this doesn't really have anything to do with osmcoastline, but with ogr2ogr. You left out the most important pieces of information, that is the "long list of alternative formats". You should have a format "SQLite / Spatialite" or something like it in there. If you don't then your version of ogr2ogr doesn't have the necessary driver.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '20, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-73115" class="comments-container">
<span id="73120"></span>
<div id="comment-73120" class="comment">
<div id="post-73120-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you Jochen,</p>
<p>All your comments was to the point. The problem was my ogr2ogr.</p>
<p>Best regards Håvard</p>
</div>
<div id="comment-73120-info" class="comment-info">
<span class="comment-age">(18 Feb '20, 09:07)</span> <span class="comment-user userinfo">HaavardHolm</span>
</div>
</div>
</div>
<div id="comment-tools-73115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73115-form-container" class="comment-form-container">
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

