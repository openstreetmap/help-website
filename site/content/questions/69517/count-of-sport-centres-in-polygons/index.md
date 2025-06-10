+++
type = "question"
title = "Count of Sport centres in polygons"
description = '''Hi guys, I am a complete newbie, any help would is highly appreciated. I am working with a shapefile of the MSOA regions in the UK and would like to get a count of all the sport centres within each of these regions.  What&#x27;s the best way to approach this using Python? Thanks'''
date = "2019-06-07T08:42:00Z"
lastmod = "2019-06-07T14:00:00Z"
weight = 69517
keywords = [ "shapefile", "sports_centre", "nodes", "count", "uk" ]
aliases = [ "/questions/69517" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Count of Sport centres in polygons](/questions/69517/count-of-sport-centres-in-polygons)

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
<span id="post-69517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69517-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>I am a complete newbie, any help would is highly appreciated. I am working with a shapefile of the MSOA regions in the UK and would like to get a count of all the sport centres within each of these regions.</p>
<p>What's the best way to approach this using Python?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-sports_centre" rel="tag" title="see questions tagged &#39;sports_centre&#39;">sports_centre</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-count" rel="tag" title="see questions tagged &#39;count&#39;">count</span> <span class="post-tag tag-link-uk" rel="tag" title="see questions tagged &#39;uk&#39;">uk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '19, 08:42</strong></p>
<img src="https://secure.gravatar.com/avatar/fba497fa4fcf6bee2c1f134b93dd2233?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bf08&#39;s gravatar image" />
<p><span>bf08</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bf08 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69517" class="comments-container">
&#10;</div>
<div id="comment-tools-69517" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69517-form-container" class="comment-form-container">
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

<span id="69532"></span>

<div id="answer-container-69532" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69532-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A simpler was would be to use QGIS. With a layer of MSOAs and a layer of sports centre centroids (example <a href="http://overpass-turbo.eu/s/JL2">Overpass query</a>) it is a simple Point in Polygon query. In python I would guess you will want to use something like Shapely to manipulate the data (for instance as discussed in this <a href="https://streamhacker.com/2010/03/23/python-point-in-polygon-shapely/">old blog</a> post).</p>
<p>One important caveat is that leisure=sports_centre in OSM is often not equivalent to a council or privately run sports or leisure centre in ordinary UK parlance (i.e., offering a range of sports). It is often used with any sports related facility such as a private rugby club or a <a href="https://www.openstreetmap.org/way/16547827">tennis centre</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '19, 14:00</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-69532" class="comments-container">
&#10;</div>
<div id="comment-tools-69532" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69532-form-container" class="comment-form-container">
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

