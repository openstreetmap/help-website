+++
type = "question"
title = "Import only lakes"
description = '''Hello OSMlers For a project, we have created the map of Canton of Zurich, including the lakes. However, it seems as if the lake of Zurich (and all other larger lakes in Switzerland) are not part of the regular osm files that I got on cloudemade for instance. Is there a way to import only lakes into ...'''
date = "2012-03-30T00:12:00Z"
lastmod = "2012-03-30T08:07:00Z"
weight = 11618
keywords = [ "rendering", "lake", "planet_osm", "import" ]
aliases = [ "/questions/11618" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Import only lakes](/questions/11618/import-only-lakes)

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
<span id="post-11618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11618-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello OSMlers</p>
<p>For a project, we have created the map of Canton of Zurich, including the lakes.</p>
<p>However, it seems as if the lake of Zurich (and all other larger lakes in Switzerland) are not part of the regular osm files that I got on cloudemade for instance.</p>
<p>Is there a way to import only lakes into my database with the planet file at hand? What would be the command line tool to use?</p>
<p>Many thanks for your help!</p>
<p>Matthias</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-lake" rel="tag" title="see questions tagged &#39;lake&#39;">lake</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Mar '12, 00:12</strong></p>
<img src="https://secure.gravatar.com/avatar/5d3a061827ff551c76c706055e638475?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matthias_&#39;s gravatar image" />
<p><span>matthias_</span><br />
<span class="score" title="55 reputation points">55</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matthias_ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11618" class="comments-container">
&#10;</div>
<div id="comment-tools-11618" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11618-form-container" class="comment-form-container">
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

<span id="11622"></span>

<div id="answer-container-11622" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11622-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hurray, I managed to do it. Here is how:</p>
<ul>
<li>installed JOSM, Java OpenStreetMap Editor</li>
<li>found the relevant way of Zurich lake first (<a href="http://www.openstreetmap.org/api/0.6/way/120595133)">http://www.openstreetmap.org/api/0.6/way/120595133)</a> and then the relation it belongs to "Zürichsee"</li>
<li>the resulting downloaded collection i did store as an OSM file</li>
<li>merged that osm file into the osm file I already had</li>
<li>and imported the complete OSM file as described on <a href="http://weait.com/content/build-your-own-openstreetmap-server">http://weait.com/content/build-your-own-openstreetmap-server</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '12, 03:34</strong></p>
<img src="https://secure.gravatar.com/avatar/5d3a061827ff551c76c706055e638475?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matthias_&#39;s gravatar image" />
<p><span>matthias_</span><br />
<span class="score" title="55 reputation points">55</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matthias_ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11622" class="comments-container">
<span id="11628"></span>
<div id="comment-11628" class="comment">
<div id="post-11628-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You could also check another provider of planet extracts like Geofabrik or build your own extract of the planet file. There is no reason for big lakes to dissappear in planet extracts (or yes, one could be if the lake is near or outside the planet extraction boundaries)</p>
</div>
<div id="comment-11628-info" class="comment-info">
<span class="comment-age">(30 Mar '12, 08:07)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-11622" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11622-form-container" class="comment-form-container">
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

