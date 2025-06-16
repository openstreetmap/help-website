+++
type = "question"
title = "Exporting Highway GPS coordinates (lat and long) to database / excel"
description = '''Dear community, I spent soe time researching for my problem&#x27;s solution, but unfortunately I couldn&#x27;t find any. So here&#x27;s what I want to do:   I want to export all highways of German highways (done - with help of e.g. https://help.openstreetmap.org/questions/30692/export-only-roads)   From this OSM f...'''
date = "2017-10-24T14:47:00Z"
lastmod = "2017-10-31T19:09:00Z"
weight = 60270
keywords = [ "excel", "export", "postgresql", "coordinates", "gps" ]
aliases = [ "/questions/60270" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting Highway GPS coordinates (lat and long) to database / excel](/questions/60270/exporting-highway-gps-coordinates-lat-and-long-to-database-excel)

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
<span id="post-60270-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60270-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60270-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear community,</p>
<p>I spent soe time researching for my problem's solution, but unfortunately I couldn't find any.</p>
<p>So here's what I want to do:</p>
<ul>
<li><p>I want to export all highways of German highways (done - with help of e.g. <a href="/questions/30692/export-only-roads)">https://help.openstreetmap.org/questions/30692/export-only-roads)</a></p></li>
<li><p>From this OSM file now I want to export the coordinates (latitude and longitude) to export to a database and then to a file which can be edited with Excel or Stata. (osm2pgrs didn't work for me)</p></li>
<li>Final goal: I have a list of certain coordinates which I want to check whether they're crossed by a highway, e.g. if some of my points are situated on a highway. Thus, eventually I want to match my list with the exported highway coordinates</li>
</ul>
<p>Does my approach makes sense? I'd be glad for any hints and tips, especially how to bring my OSM-file of highways into a list of all coordinates of the highway. Or, if this approach is not senseful at all, please let me know.</p>
<p>Thanks a lot in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-excel" rel="tag" title="see questions tagged &#39;excel&#39;">excel</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Oct '17, 14:47</strong></p>
<img src="https://secure.gravatar.com/avatar/f3d03e82877203f7d8cd3903c178c027?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tom_sen&#39;s gravatar image" />
<p><span>tom_sen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tom_sen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60270" class="comments-container">
&#10;</div>
<div id="comment-tools-60270" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60270-form-container" class="comment-form-container">
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

<span id="60277"></span>

<div id="answer-container-60277" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60277-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is what spatial databases are for. You should load the data into PostGIS with osm2pgsql, create a table with your points in it in PostGIS, and then you can make SQL queries like</p>
<pre><code>SELECT mypoint.name, highway.name
FROM mypoints, planet_osm_line highway
WHERE highway.highway IS NOT NULL
AND ST_DWITHIN(mypoint.geom, highway.geom, 100);</code></pre>
<p>Provided your points are stored in the same projection as the highways this will give you points that are roughly within 100m of a highway, of course you can also reduce that to 10m or 2m.</p>
<p>The "manual" approach you sketched won't work because "the points of the highway", even if you were to extract them, can be hundreds of metres apart; even if one of your test points was bang in the middle of a highway, it could still be 100m away from the nearest "highway point". The spatial database does all the necessary calculations for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '17, 18:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-60277" class="comments-container">
<span id="60381"></span>
<div id="comment-60381" class="comment">
<div id="post-60381-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much, Frederik! That code helped me a lot and thanks for sharing the general approach with me!</p>
</div>
<div id="comment-60381-info" class="comment-info">
<span class="comment-age">(31 Oct '17, 19:09)</span> <span class="comment-user userinfo">tom_sen</span>
</div>
</div>
</div>
<div id="comment-tools-60277" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60277-form-container" class="comment-form-container">
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

