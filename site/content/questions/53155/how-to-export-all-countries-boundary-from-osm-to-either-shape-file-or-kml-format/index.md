+++
type = "question"
title = "How to export all countries boundary from OSM to either Shape File or KML format?"
description = '''I am trying to extract the whole world from OSM on the basis of administrative level (i.e, admin_level=2) using overpass turbo but it is difficult as it doesn&#x27;t allow to download whole world at a single time. So please help me if you have any idea to export only countries boundary.'''
date = "2016-11-29T05:22:00Z"
lastmod = "2016-11-30T04:43:00Z"
weight = 53155
keywords = [ "admin_level" ]
aliases = [ "/questions/53155" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to export all countries boundary from OSM to either Shape File or KML format?](/questions/53155/how-to-export-all-countries-boundary-from-osm-to-either-shape-file-or-kml-format)

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
<span id="post-53155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53155-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to extract the whole world from OSM on the basis of administrative level (i.e, admin_level=2) using overpass turbo but it is difficult as it doesn't allow to download whole world at a single time. So please help me if you have any idea to export only countries boundary.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-admin_level" rel="tag" title="see questions tagged &#39;admin_level&#39;">admin_level</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '16, 05:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d1a918e8d6cb19a127b5912c7288f5ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ro%20Sun&#39;s gravatar image" />
<p><span>Ro Sun</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ro Sun has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Nov '16, 05:23</strong> </span></p>
</div>
</div>
<div id="comments-container-53155" class="comments-container">
&#10;</div>
<div id="comment-tools-53155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53155-form-container" class="comment-form-container">
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

<span id="53161"></span>

<div id="answer-container-53161" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53161-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ro Sun has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can download the OSM planet file and filter out the admin boundaries (see <a href="/questions/47931/filters-in-osmosis-filtering-administrative-boundaries">this answer</a> for example), or you could download from the <a href="https://osm.wno-edv-service.de/boundaries/">boundaries map</a>.</p>
<p>However, if you only want country boundaries then my suspicion is that you do not need the full detail that OSM offers (OSM data follows every smallest zig-zag of the boundary, resulting in very large polygons), and you might also dislike the fact the OSM boundaries don't hug the coastline but include the maritime claims as well. It might be much easier for you to head over to the public domain <a href="http://naturalearthdata.com/">Natural Earth</a> dataset which comes simplified for three different scales.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '16, 06:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-53161" class="comments-container">
&#10;</div>
<div id="comment-tools-53161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53161-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53177"></span>

<div id="answer-container-53177" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53177-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here is the curl command to download the countries border</p>
<pre><code>curl \
  --connect-timeout 10  \
  --retry 10  \
  --retry-delay 10  \
  --retry-max-time 500  \
  -H &quot;Host: overpass-api.de&quot; -H &quot;Content-Type: text/xml&quot;  \
  -d &#39;relation[&quot;admin_level&quot;=&quot;2&quot;];(._;&gt;;); out body;&#39;  \
  http://overpass-api.de/api/interpreter  \
  -o countries-border.osm</code></pre>
<p>And use <a href="https://wiki.openstreetmap.org/wiki/OGR">ogr2ogr</a> to convert osm to shapefile.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '16, 04:43</strong></p>
<img src="https://secure.gravatar.com/avatar/39d75f04e1a21ba653b41ac75ec1b026?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gagan&#39;s gravatar image" />
<p><span>Gagan</span><br />
<span class="score" title="305 reputation points">305</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gagan has 2 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '16, 04:46</strong> </span></p>
</div>
</div>
<div id="comments-container-53177" class="comments-container">
&#10;</div>
<div id="comment-tools-53177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53177-form-container" class="comment-form-container">
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

