+++
type = "question"
title = "osm data attributes are incomplete after loading into Postgres database"
description = '''Hi everyone, I am new to open street map, I&#x27;m trying to download osm data, load in into Postgres database, and add a postgres layer in QGIS. The problem was that I found that the layer&#x27;s attributes table are incomplete in QGIS, I guess 80% of the attributes are null. I downloaded whole australia dat...'''
date = "2015-04-12T04:57:00Z"
lastmod = "2015-04-12T11:56:00Z"
weight = 42281
keywords = [ "qgis", "attributes", "postgresql", "geofabrik" ]
aliases = [ "/questions/42281" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [osm data attributes are incomplete after loading into Postgres database](/questions/42281/osm-data-attributes-are-incomplete-after-loading-into-postgres-database)

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
<span id="post-42281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42281-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone, I am new to open street map, I'm trying to download osm data, load in into Postgres database, and add a postgres layer in QGIS. The problem was that I found that the layer's attributes table are incomplete in QGIS, I guess 80% of the attributes are null. I downloaded whole australia data in format of .pbf from geofabrik, then using osm2pgsql to put the data in Postgres database (followed tutorial in LearnOSM, <a href="http://learnosm.org/en/osm-data/osm2pgsql/#importing-the-data).">http://learnosm.org/en/osm-data/osm2pgsql/#importing-the-data).</a> I think it maybe something wrong with the default.style file but I don't know how to fix it. I hope someone can help with this, and sorry about my english. :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-attributes" rel="tag" title="see questions tagged &#39;attributes&#39;">attributes</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-geofabrik" rel="tag" title="see questions tagged &#39;geofabrik&#39;">geofabrik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '15, 04:57</strong></p>
<img src="https://secure.gravatar.com/avatar/cd5fec954ed6b0a7958604fb5cb687bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qiqiqi&#39;s gravatar image" />
<p><span>qiqiqi</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qiqiqi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42281" class="comments-container">
&#10;</div>
<div id="comment-tools-42281" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42281-form-container" class="comment-form-container">
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

<span id="42285"></span>

<div id="answer-container-42285" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42285-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is completely normal that for most objects, most columns are <code>null</code>. For example, there might be columns for name, opening hours, reference number, oneway, max speed and so on - how else would they be filled for a post box, or a tree? If you dislike the many "null" columns, have a look at the "hstore" facility that osm2pgsql offers, where it is possible to import all values into a single column; you might want to get rid of some column definitions in default.style then.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '15, 09:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-42285" class="comments-container">
<span id="42290"></span>
<div id="comment-42290" class="comment">
<div id="post-42290-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for answering:)</p>
</div>
<div id="comment-42290-info" class="comment-info">
<span class="comment-age">(12 Apr '15, 11:56)</span> <span class="comment-user userinfo">qiqiqi</span>
</div>
</div>
</div>
<div id="comment-tools-42285" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42285-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42288"></span>

<div id="answer-container-42288" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42288-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nothing wrong there. <code>null</code> is used to signify that "this object does not have this tag", e.g. "There is no <code>name</code> tag for this road in the OSM database". Since osm2pgsql stores all points in one table, and all lines in another table, and all polygons in another table, it has to merge all the OSM objects together. Roads are stored next to footpaths. Building outlines are stored alongside lakes. Buildings will have a <code>building</code> tag (and hence have a non-null value for that column), whereas lakes will not have a <code>building</code> tag, and have <code>null</code> for that column.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '15, 11:33</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-42288" class="comments-container">
<span id="42289"></span>
<div id="comment-42289" class="comment">
<div id="post-42289-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK I got it, thank you very much</p>
</div>
<div id="comment-42289-info" class="comment-info">
<span class="comment-age">(12 Apr '15, 11:56)</span> <span class="comment-user userinfo">qiqiqi</span>
</div>
</div>
</div>
<div id="comment-tools-42288" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42288-form-container" class="comment-form-container">
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

