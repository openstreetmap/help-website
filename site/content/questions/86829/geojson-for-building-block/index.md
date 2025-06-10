+++
type = "question"
title = "GeoJSON for building block"
description = '''I know how to get a GeoJSON polygon for a single building and the documentation does explain it well: https://nominatim.org/release-docs/develop/api/Search/#parameters It is also possible to get GeoJSON for regions for example. But are there GeoJSON data (polygons) for building blocks in the databas...'''
date = "2023-02-28T11:12:00Z"
lastmod = "2023-03-09T10:20:00Z"
weight = 86829
keywords = [ "housenumbers", "geojson", "area" ]
aliases = [ "/questions/86829" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [GeoJSON for building block](/questions/86829/geojson-for-building-block)

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
<span id="post-86829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86829-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I know how to get a GeoJSON polygon for a single building and the documentation does explain it well: <a href="https://nominatim.org/release-docs/develop/api/Search/#parameters">https://nominatim.org/release-docs/develop/api/Search/#parameters</a></p>
<p>It is also possible to get GeoJSON for regions for example.</p>
<p>But are there GeoJSON data (polygons) for building blocks in the database, too? And if yes, how can I query them, for example multiple house numbers</p>
<p><em>/search?query=merseburger str. 4,6,8,10,12,14,16,18,20 marzahn</em></p>
<p>Block level might be just be rare in Europe (<a href="https://wiki.openstreetmap.org/wiki/Key:addr:block">this regarding <em>block</em> tag in address</a>)</p>
<p>"The city block, if part of the address. Note that this tag is most often used in places where blocks can have names and not just numbers, and in many cases is specified in addition to a street name. This tag is common in a variety of countries, including India, Egypt, and Kuwait."</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-geojson" rel="tag" title="see questions tagged &#39;geojson&#39;">geojson</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '23, 11:12</strong></p>
<img src="https://secure.gravatar.com/avatar/deb716e809a2dc3415d211ac8f515453?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="toothbrush&#39;s gravatar image" />
<p><span>toothbrush</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="toothbrush has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86829" class="comments-container">
&#10;</div>
<div id="comment-tools-86829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86829-form-container" class="comment-form-container">
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

<span id="86896"></span>

<div id="answer-container-86896" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86896-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't believe there is any in use practice to map blocks as separate objects. So, at least in locations where the addresses are well mapped, I suspect your best bet would be to construct the convex hull of the addresses with the same addr:block or addr:block_number.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '23, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-86896" class="comments-container">
&#10;</div>
<div id="comment-tools-86896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86896-form-container" class="comment-form-container">
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

