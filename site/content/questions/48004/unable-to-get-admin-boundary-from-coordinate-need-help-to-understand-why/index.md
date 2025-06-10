+++
type = "question"
title = "Unable to get admin boundary from coordinate. Need help to understand why"
description = '''Hi, I cannot understand how I shall fix the error that causes the admin boundary that should cover the coordinate in the link below: http://www.openstreetmap.org/query?lat=57.7585&amp;amp;lon=12.2652 It should belong to &quot;Lerums kommun&quot; Admin level 07. It does exist, but the query cannot find it. What is...'''
date = "2016-02-08T22:34:00Z"
lastmod = "2016-02-09T13:55:00Z"
weight = 48004
keywords = [ "incorrect", "boundary", "osm", "error" ]
aliases = [ "/questions/48004" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to get admin boundary from coordinate. Need help to understand why](/questions/48004/unable-to-get-admin-boundary-from-coordinate-need-help-to-understand-why)

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
<span id="post-48004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48004-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I cannot understand how I shall fix the error that causes the admin boundary that should cover the coordinate in the link below:</p>
<p><a href="http://www.openstreetmap.org/query?lat=57.7585&amp;lon=12.2652">http://www.openstreetmap.org/query?lat=57.7585&amp;lon=12.2652</a></p>
<p>It should belong to "Lerums kommun" Admin level 07. It does exist, but the query cannot find it.</p>
<p>What is wrong with the administrative border, and how do I correct it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-incorrect" rel="tag" title="see questions tagged &#39;incorrect&#39;">incorrect</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '16, 22:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7d879d68e986486305a0f1be2bb9e2fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SunYour&#39;s gravatar image" />
<p><span>SunYour</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SunYour has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48004" class="comments-container">
&#10;</div>
<div id="comment-tools-48004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48004-form-container" class="comment-form-container">
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

<span id="48021"></span>

<div id="answer-container-48021" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48021-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The area is missing from the <a href="http://overpass-api.de/">Overpass server</a> used to generate those query results.</p>
<p>That server is also the default on <a href="http://overpass-turbo.eu/">Overpass-Turbo</a>, so it's straightforward to check what data is present. This script should find the area:</p>
<pre><code>area(3600935550);
out geom;</code></pre>
<p>But returns nothing. A nearby area is found:</p>
<pre><code>area(3600935649);
out geom;</code></pre>
<p>And the relation is present:</p>
<pre><code>rel(935550);
out geom;</code></pre>
<p>So for some reason the Overpass server did not generate an area from that specific relation. Overpass areas are updated less frequently than the rest of the data, and there is a recent edit to some of the member ways of the missing area:</p>
<p><a href="https://www.openstreetmap.org/changeset/37092451">https://www.openstreetmap.org/changeset/37092451</a></p>
<p>So you might only need to wait until the next time areas are refreshed on the Overpass server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '16, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Feb '16, 18:24</strong> </span></p>
</div>
</div>
<div id="comments-container-48021" class="comments-container">
&#10;</div>
<div id="comment-tools-48021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48021-form-container" class="comment-form-container">
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

