+++
type = "question"
title = "Actual road length of exported map"
description = '''I have exported a map that represents part of city. I have measured road length with the measurement plugin in JOSM. I have realised that the map that appear in JOSM is bigger than the one I have exported as it seems to includes full length of ways of which I have only selected a part, one of them l...'''
date = "2016-04-13T09:59:00Z"
lastmod = "2016-04-13T13:03:00Z"
weight = 49200
keywords = [ "josm", "length", "newbie", "measurement" ]
aliases = [ "/questions/49200" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Actual road length of exported map](/questions/49200/actual-road-length-of-exported-map)

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
<span id="post-49200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49200-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have exported a map that represents part of city. I have measured road length with the measurement plugin in JOSM. I have realised that the map that appear in JOSM is bigger than the one I have exported as it seems to includes full length of ways of which I have only selected a part, one of them looks like the city limit. As result if I select everything, road length measured by the plugin is much bigger than the measurement obtained when I manually select just the area I have previously exported. I have also tried the osm-length-2.pl script, whose result is the same as when I consider the whole area that appears in JOSM. However, I have realised that when results are detailed, it exists one distance that is not assigned to any road type, is this distance the length of the extra roads that are considered despite not being selected? How can I make sure I get the length of the roads just in the area I choose and export? If possible, I would like to have different road type length detailed, as in osm-length-2.pl results.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-measurement" rel="tag" title="see questions tagged &#39;measurement&#39;">measurement</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Apr '16, 09:59</strong></p>
<img src="https://secure.gravatar.com/avatar/9487434b45dfe8b85603edb437cfd459?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fa__&#39;s gravatar image" />
<p><span>Fa__</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fa__ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Apr '16, 12:32</strong> </span></p>
</div>
</div>
<div id="comments-container-49200" class="comments-container">
&#10;</div>
<div id="comment-tools-49200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49200-form-container" class="comment-form-container">
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

<span id="49210"></span>

<div id="answer-container-49210" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49210-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM is an editor not an analytical tool.</p>
<p>In addition to using PostGIS as suggested by Frederik you can also import data into QGIS which allows the same operations (clipping, filtering &amp; measurement) to be performed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '16, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Apr '16, 21:23</strong> </span></p>
</div>
</div>
<div id="comments-container-49210" class="comments-container">
&#10;</div>
<div id="comment-tools-49210" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49210-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49209"></span>

<div id="answer-container-49209" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49209-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Import your data set into PostGIS with osm2pgsql, then you have full control over what gets counted and how. You could for example take a clipping polygon e.g. the administrative boundary and have all roads clipped at that boundary, with a query similar to this:</p>
<pre><code>SELECT way AS clip
INTO clipping_polygon
FROM planet_osm_polygon
WHERE boundary=&#39;administrative&#39; AND admin_level=&#39;8&#39; and name=&#39;My City&#39;;
&#10;SELECT name, highway, ST_INTERSECTION(way, clip)
INTO clipped_roads
FROM planet_osm_line, clipping_polygon
WHERE ST_INTERSECTS(way, clip) AND highway IS NOT NULL;</code></pre>
<p>Then you could count the total length in metres per highway type like this</p>
<pre><code>SELECT highway, SUM(ST_LENGTH(way::geography))
FROM clipped_roads
GROUP BY highway;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Apr '16, 12:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-49209" class="comments-container">
&#10;</div>
<div id="comment-tools-49209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49209-form-container" class="comment-form-container">
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

