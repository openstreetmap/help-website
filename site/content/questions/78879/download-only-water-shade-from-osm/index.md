+++
type = "question"
title = "download only water shade from OSM"
description = '''Hello, I am very new to this topic and maybe my question is a bit dumb. For a private Projekt I am looking for the possibility, to download the rivers and lakes from a bigger area (the alps).  Until now, I alway tried to download the PDF and import the file in my CAD-Program. Unfortunately, this way...'''
date = "2021-02-16T12:50:00Z"
lastmod = "2021-02-25T13:05:00Z"
weight = 78879
keywords = [ "download", "water", "vector" ]
aliases = [ "/questions/78879" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [download only water shade from OSM](/questions/78879/download-only-water-shade-from-osm)

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
<span id="post-78879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78879-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am very new to this topic and maybe my question is a bit dumb. For a private Projekt I am looking for the possibility, to download the rivers and lakes from a bigger area (the alps). Until now, I alway tried to download the PDF and import the file in my CAD-Program. Unfortunately, this way is extremely laborious cause I have to download many small tiles and try to put them together afterwards. So is there the possibility to download a bigger area as a vectorized file, maybe where only the contours of the rivers and lakes are shown?</p>
<p>Thanks for your help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '21, 12:50</strong></p>
<img src="https://secure.gravatar.com/avatar/464f2d8db2faf75e1847f9df75f139f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bast123&#39;s gravatar image" />
<p><span>Bast123</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bast123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78879" class="comments-container">
&#10;</div>
<div id="comment-tools-78879" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78879-form-container" class="comment-form-container">
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

<span id="78880"></span>

<div id="answer-container-78880" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78880-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While Overpass lets you download specific features, downloading all water bodies for the whole Alps could be too taxing for the server (and you might run into timeouts). A failsafe process would be to download the "Alps" data file from <a href="http://download.geofabrik.de/europe/alps.html">http://download.geofabrik.de/europe/alps.html</a> and then</p>
<ul>
<li>either use the <code>osmium</code> command line program to filter out the waterways from that (<code>osmium tag-filter</code>) and then export to a GIS data format with <code>osmium export</code>,</li>
<li>or use <code>osm2pgsql</code> to import the data into a PostGIS database from where you can then export shape files or CSV files as needed</li>
<li>or use <code>ogr2ogr</code> to convert the OSM data to some other GIS format, including DXF</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '21, 13:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78880" class="comments-container">
<span id="79028"></span>
<div id="comment-79028" class="comment">
<div id="post-79028-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello, thank you for your detailed reply. I think I unterstand your proposed method, but I'm a bit lost with the handling of the programs. Which programs (and sub-programs etc.) do I need to install for macOS, so I can use your way of solution?</p>
</div>
<div id="comment-79028-info" class="comment-info">
<span class="comment-age">(25 Feb '21, 12:54)</span> <span class="comment-user userinfo">Bast123</span>
</div>
</div>
<span id="79029"></span>
<div id="comment-79029" class="comment">
<div id="post-79029-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You might get by with installing just the osmium command line tool which claims to be available for macOS but you'll probably have to do some digging for a pre-compiled version - the instructions <a href="https://osmcode.org/osmium-tool/manual.html">https://osmcode.org/osmium-tool/manual.html</a> only link to building the package yourself and that might not be appropriate for your skill level.</p>
</div>
<div id="comment-79029-info" class="comment-info">
<span class="comment-age">(25 Feb '21, 13:05)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-78880" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78880-form-container" class="comment-form-container">
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

