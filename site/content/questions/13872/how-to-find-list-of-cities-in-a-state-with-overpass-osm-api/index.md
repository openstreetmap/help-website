+++
type = "question"
title = "How to find list of cities in a state with overpass osm api?"
description = '''How can I find list of cities from OSM in particular state or country? Suppose I want to find all the cities in Gujarat state and bbox (boundry values) values of gujarat state can be found here http://nominatim.openstreetmap.org/search?q=gujarat&amp;amp;format=xml So now using overpass API, how can find...'''
date = "2012-06-28T08:36:00Z"
lastmod = "2012-06-28T09:50:00Z"
weight = 13872
keywords = [ "openstreetmap", "overpass", "boundary", "nominatim" ]
aliases = [ "/questions/13872" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to find list of cities in a state with overpass osm api?](/questions/13872/how-to-find-list-of-cities-in-a-state-with-overpass-osm-api)

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
<span id="post-13872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13872-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I find list of cities from OSM in particular state or country?</p>
<p>Suppose I want to find all the cities in Gujarat state and bbox (boundry values) values of gujarat state can be found here <a href="http://nominatim.openstreetmap.org/search?q=gujarat&amp;format=xml">http://nominatim.openstreetmap.org/search?q=gujarat&amp;format=xml</a></p>
<p>So now using overpass API, how can find the list of cities in Gujarat? Please write the query for me. Or tell me any other solution without overpass, if some better solution is available.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '12, 08:36</strong></p>
<img src="https://secure.gravatar.com/avatar/b3013a84207a32bed7ddfad7004100f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravi%20Kotwani&#39;s gravatar image" />
<p><span>Ravi Kotwani</span><br />
<span class="score" title="136 reputation points">136</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravi Kotwani has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13872" class="comments-container">
&#10;</div>
<div id="comment-tools-13872" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13872-form-container" class="comment-form-container">
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

<span id="13874"></span>

<div id="answer-container-13874" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13874-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-13874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ravi Kotwani has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you already have the bounding box from your Nominatim query, and if what you are looking for are nodes tagged <code>place=city</code>, then it is probably easiest to use the XAPI compatibility mode of Overpass:</p>
<pre><code>http://www.overpass-api.de/api/xapi?node[bbox=68.11,20.12,74.48,24.71][place=city]</code></pre>
<p>Note that Overpass expects the bbox as west,south,east,north whereas Nominatim outputs it as south,north,east,west.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '12, 09:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-13874" class="comments-container">
<span id="13876"></span>
<div id="comment-13876" class="comment">
<div id="post-13876-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. I had already tried the same but I was writing the wrong sequence of bbox values. Thanks a lot. Its working find now.</p>
</div>
<div id="comment-13876-info" class="comment-info">
<span class="comment-age">(28 Jun '12, 09:50)</span> <span class="comment-user userinfo">Ravi Kotwani</span>
</div>
</div>
</div>
<div id="comment-tools-13874" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13874-form-container" class="comment-form-container">
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

