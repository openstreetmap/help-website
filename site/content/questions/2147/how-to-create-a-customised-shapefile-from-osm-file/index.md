+++
type = "question"
title = "How to create a customised shapefile from OSM file?"
description = '''Hi to all, happy new year. I need to create a shp from .osm, which will also have a column with the name of the user who last edited the object. Provided shapefiles do not include this information. I tried using &#x27;osm2shp&#x27; and &#x27;OSM Data Miner&#x27; softwares, among which the last one seems to be able to d...'''
date = "2011-01-11T12:58:00Z"
lastmod = "2011-01-13T23:03:00Z"
weight = 2147
keywords = [ "customised", "shapefile" ]
aliases = [ "/questions/2147" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to create a customised shapefile from OSM file?](/questions/2147/how-to-create-a-customised-shapefile-from-osm-file)

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
<span id="post-2147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2147-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all, happy new year.</p>
<p>I need to create a shp from .osm, which will also have a column with the name of the user who last edited the object. Provided shapefiles do not include this information. I tried using 'osm2shp' and 'OSM Data Miner' softwares, among which the last one seems to be able to do it, however they both fail (most probably because of lack of memory, I am using an OSM file covering the whole Great Britain). I tried to use osm2pgsql, however installation is so complicated that I couldn't reach the end. Does anyone know any other way? Thanks, Thomas</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-customised" rel="tag" title="see questions tagged &#39;customised&#39;">customised</span> <span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jan '11, 12:58</strong></p>
<img src="https://secure.gravatar.com/avatar/fb5b2c743db9a0c585e3b74522335881?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thomas%20Koukoletsos&#39;s gravatar image" />
<p><span>Thomas Kouko...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thomas Koukoletsos has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2147" class="comments-container">
&#10;</div>
<div id="comment-tools-2147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2147-form-container" class="comment-form-container">
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

<span id="2182"></span>

<div id="answer-container-2182" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2182-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The osmjs utility bundled with Osmium should be able to do what you want. See <a href="https://wiki.openstreetmap.org/wiki/Osmium">https://wiki.openstreetmap.org/wiki/Osmium</a> for some infos. Unfortunately the documentation is a bit sketchy at the moment and you will have to compile the software yourself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '11, 23:03</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-2182" class="comments-container">
&#10;</div>
<div id="comment-tools-2182" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2182-form-container" class="comment-form-container">
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

