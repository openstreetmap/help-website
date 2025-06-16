+++
type = "question"
title = "DXF to KML or SHP ?"
description = '''Hello,  I have have a georeferenced DXF file (lambert coordinate) and since JOSM couldn’t place it automatically in its right position on the map when I import the DXF file, one solution would be to convert it to KML or SHP, my questions are :  Does the conversion from DXF to KML or SHP is 100% ? I ...'''
date = "2016-05-31T22:37:00Z"
lastmod = "2016-06-01T10:12:00Z"
weight = 49936
keywords = [ "josm", "kml", "dxf" ]
aliases = [ "/questions/49936" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [DXF to KML or SHP ?](/questions/49936/dxf-to-kml-or-shp)

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
<span id="post-49936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49936-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have have a georeferenced DXF file (lambert coordinate) and since JOSM couldn’t place it automatically in its right position on the map when I import the DXF file, one solution would be to convert it to KML or SHP, my questions are :</p>
<ul>
<li>Does the conversion from DXF to KML or SHP is 100% ? I will not have a loss of data from DXF to KML or SHP ?</li>
<li>If I were to choose, which format you suggest to convert to, KML or SHP ?</li>
<li>Do you know why when I import a georeferenced DXF file in JOSM, it is placed on the center of my screen instead in its right position on the map ?</li>
</ul>
<p>I know that my question could be a little vague, should you need any other details or clarifications, please don’t hesitate.</p>
<p>Thank you very much</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-dxf" rel="tag" title="see questions tagged &#39;dxf&#39;">dxf</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 May '16, 22:37</strong></p>
<img src="https://secure.gravatar.com/avatar/f89ea8c4c54f734605b2d989093ced02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Clemapper&#39;s gravatar image" />
<p><span>Clemapper</span><br />
<span class="score" title="86 reputation points">86</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Clemapper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49936" class="comments-container">
<span id="49938"></span>
<div id="comment-49938" class="comment">
<div id="post-49938-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Did you try to contact the authors of the DXF import plugin directly ? See <a href="https://github.com/asrianCron/Dxf-Import">https://github.com/asrianCron/Dxf-Import</a> -&gt; Contributors</p>
</div>
<div id="comment-49938-info" class="comment-info">
<span class="comment-age">(01 Jun '16, 06:10)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-49936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49936-form-container" class="comment-form-container">
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

<span id="49942"></span>

<div id="answer-container-49942" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49942-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-49942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This all depends on the software you use to make the conversion. Ideally all software should manage roundtripable conversions, but this is not often the case, especially with proprietary formats like DXF. The fact that your file appear non-georeferenced in JOSM might be a conversion bug. As for other conversion quality metrics, your best bet is to try it out.</p>
<p>The popular <a href="http://www.gdal.org/">gdal toolkit</a> has a versatile <a href="http://www.gdal.org/gdal_translate.html">conversion tool</a> you should try. If you have Autodesk, you could also open the DXF there and export it to another format.</p>
<p>There's no one-size fits-all for "the best geodata format", it depends on what you want to do. If you're loading it in JOSM, surely the best option is to load it in <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">OSM</a> or <a href="https://wiki.openstreetmap.org/wiki/PBF_Format">PBF</a> format, because it is native to (j)osm. SHP is the lingua franca of vector geodata, but is crufty and has limitations. <a href="https://en.wikipedia.org/wiki/GeoJSON">Geojson/topojson</a> is a modern take on KML-style formats. Gdal has a useful writeup on <a href="http://www.gdal.org/ogr_formats.html">all those formats</a>, and wikipedia can also be interesting.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '16, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-49942" class="comments-container">
<span id="49950"></span>
<div id="comment-49950" class="comment">
<div id="post-49950-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very very much for your help. Are you saying that DXF Import is supposed to automatically place in its correct position on the map ? How would JOSM/DXF Import guess that my DXF file is in Lambert coordinate system ?</p>
</div>
<div id="comment-49950-info" class="comment-info">
<span class="comment-age">(01 Jun '16, 10:12)</span> <span class="comment-user userinfo">Clemapper</span>
</div>
</div>
</div>
<div id="comment-tools-49942" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49942-form-container" class="comment-form-container">
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

