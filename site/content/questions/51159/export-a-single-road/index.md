+++
type = "question"
title = "Export A Single Road"
description = '''Is it possible to export a single road? If so, how? I am able to successfully export all roads for a given area, but I would rather do 1 road at a time. Please let me know and thank you in advance!'''
date = "2016-07-28T21:43:00Z"
lastmod = "2016-08-02T10:11:00Z"
weight = 51159
keywords = [ "single", "export", "road" ]
aliases = [ "/questions/51159" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export A Single Road](/questions/51159/export-a-single-road)

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
<span id="post-51159-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51159-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51159-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to export a single road? If so, how? I am able to successfully export all roads for a given area, but I would rather do 1 road at a time. Please let me know and thank you in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-single" rel="tag" title="see questions tagged &#39;single&#39;">single</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jul '16, 21:43</strong></p>
<img src="https://secure.gravatar.com/avatar/f44fc4174417a0a08ecb804006858086?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TonesJones&#39;s gravatar image" />
<p><span>TonesJones</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TonesJones has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51159" class="comments-container">
<span id="51179"></span>
<div id="comment-51179" class="comment">
<div id="post-51179-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Do you have a specific reason for downloading roads one by one? Usually it more efficient to fetch multiple roads in one go, rather than downloading them one by one (assuming you want to download all roads in an area anyway and your area is not too large).</p>
</div>
<div id="comment-51179-info" class="comment-info">
<span class="comment-age">(30 Jul '16, 18:47)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="51196"></span>
<div id="comment-51196" class="comment">
<div id="post-51196-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can also <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#Multi_fetch:_GET_.2Fapi.2F0.6.2F.5Bnodes.7Cways.7Crelations.5D.3F.23parameters">download multiple objects in one go using their id</a> rather than using a bounding box.</p>
</div>
<div id="comment-51196-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 10:11)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51159" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51159-form-container" class="comment-form-container">
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

<span id="51161"></span>

<div id="answer-container-51161" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51161-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can fetch elements by id using Overpass API:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_element_id">http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#By_element_id</a></p>
<p>The simplest script to retrieve a way would be something like this:</p>
<pre><code>way(17500233);
out geom;</code></pre>
<p>Here's that query in Overpass Turbo, an IDE for Overpass API:</p>
<p><a href="http://overpass-turbo.eu/s/hyA">http://overpass-turbo.eu/s/hyA</a></p>
<p>You can use it to experiment and see if Overpass is suitable for your needs. Once you have your query worked out, you can fetch the ways directly from Overpass API.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '16, 22:09</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-51161" class="comments-container">
<span id="51164"></span>
<div id="comment-51164" class="comment">
<div id="post-51164-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Alternatively just use the the <a href="https://wiki.openstreetmap.org/wiki/API">(editing) API</a>: <a href="https://www.openstreetmap.org/api/0.6/way/17500233/full">https://www.openstreetmap.org/api/0.6/way/17500233/full</a></p>
</div>
<div id="comment-51164-info" class="comment-info">
<span class="comment-age">(29 Jul '16, 07:55)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="51195"></span>
<div id="comment-51195" class="comment">
<div id="post-51195-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Remember that one "road" in everyday speech can be made of multiple "ways" in OSM data. Overpass could help downloading all ways of one "road" but you'll have to tweak the query on a case by case basis.</p>
</div>
<div id="comment-51195-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 10:07)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51161-form-container" class="comment-form-container">
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

