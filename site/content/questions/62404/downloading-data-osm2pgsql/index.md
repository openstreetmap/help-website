+++
type = "question"
title = "Downloading data osm2pgsql"
description = '''I uploaded a large *.osm file. Now from it you need to import into the postgis data having amenity = parking in my table. Import only polygons. Polygons must be imported into the &quot;polygon&quot; field. All other fields in the table will be populated with default values. Tell me, can this be done with osm2...'''
date = "2018-02-26T14:26:00Z"
lastmod = "2018-02-27T10:04:00Z"
weight = 62404
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/62404" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Downloading data osm2pgsql](/questions/62404/downloading-data-osm2pgsql)

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
<span id="post-62404-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62404-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62404-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I uploaded a large *.osm file. Now from it you need to import into the postgis data having amenity = parking in my table. Import only polygons. Polygons must be imported into the "polygon" field. All other fields in the table will be populated with default values. Tell me, can this be done with osm2pgsql</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Feb '18, 14:26</strong></p>
<img src="https://secure.gravatar.com/avatar/0e6b9dc16e897e8916e6cc185c397403?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kas_kas&#39;s gravatar image" />
<p><span>kas_kas</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kas_kas has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62404" class="comments-container">
&#10;</div>
<div id="comment-tools-62404" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62404-form-container" class="comment-form-container">
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

<span id="62434"></span>

<div id="answer-container-62434" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62434-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-62434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What osm2pgsql imports in to the target database is determined by its "style file" (additionally you can use LUA to manipulate data pre-writing to the DB).</p>
<p>See <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql#Import_style">https://wiki.openstreetmap.org/wiki/Osm2pgsql#Import_style</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Feb '18, 10:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-62434" class="comments-container">
&#10;</div>
<div id="comment-tools-62434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62434-form-container" class="comment-form-container">
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

