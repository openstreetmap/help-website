+++
type = "question"
title = "overpass query roads within polygon"
description = '''Hi, I&#x27;m trying to get a list of roads within a community, but I get a timeout error when I try this. On very small queries it does work (e.g. highway=path). And on bbox too. Is this particular to querying within areas? [out:json][timeout:25];  ( area[&quot;name&quot;=&quot;Halle&quot;][admin_level=8]; )-&amp;gt;.a; (  way[...'''
date = "2017-05-11T10:35:00Z"
lastmod = "2017-05-11T18:33:00Z"
weight = 56122
keywords = [ "overpass" ]
aliases = [ "/questions/56122" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [overpass query roads within polygon](/questions/56122/overpass-query-roads-within-polygon)

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
<span id="post-56122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56122-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to get a list of roads within a community, but I get a timeout error when I try this. On very small queries it does work (e.g. highway=path). And on bbox too. Is this particular to querying within areas?</p>
<pre><code>[out:json][timeout:25];
  ( area[&quot;name&quot;=&quot;Halle&quot;][admin_level=8]; )-&gt;.a;
(
  way[&quot;highway&quot;][&quot;name&quot;](area.a);
(area.a)
);
out body;
&gt;;
out skel qt;`</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 May '17, 10:35</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> reverted <strong>11 May '17, 15:35</strong> </span></p>
</div>
</div>
<div id="comments-container-56122" class="comments-container">
&#10;</div>
<div id="comment-tools-56122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56122-form-container" class="comment-form-container">
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

<span id="56123"></span>

<div id="answer-container-56123" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56123-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="joost schouppe has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can't offer an underlying explanation as to why, but the timeout is related to the area query returning multiple areas. A workaround is to request a specific area, like: <code>area(3600206480)-&gt;.a;</code>.</p>
<p>Use pivot to inspect the results of an area query:</p>
<pre><code>[out:json][timeout:25];
area[&quot;name&quot;=&quot;Halle&quot;][admin_level=8]-&gt;.a;
(way(pivot.a);
rel(pivot.a););
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '17, 11:08</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-56123" class="comments-container">
<span id="56124"></span>
<div id="comment-56124" class="comment">
<div id="post-56124-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Increasing the allowed time usually works too (i.e. set timeout:250 instead of timeout:25)</p>
</div>
<div id="comment-56124-info" class="comment-info">
<span class="comment-age">(11 May '17, 11:53)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="56130"></span>
<div id="comment-56130" class="comment">
<div id="post-56130-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes, a larger time-out did the trick in this case. But I somehow missed clicking the zoom to data, so I didn't see there were more Halle in the world. My first try to limit the results to Flemish communities did not seem to work though... ( area["name"="Vlaanderen"]["admin_level"="4"]; )-&gt;.b; ( area["name"="Halle"]<a href="area.b">admin_level=8</a>; )-&gt;.a;</p>
</div>
<div id="comment-56130-info" class="comment-info">
<span class="comment-age">(11 May '17, 15:56)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="56133"></span>
<div id="comment-56133" class="comment">
<div id="post-56133-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, found it: you need to first create areas, then require your results to be in both areas simultaniously: <a href="http://overpass-turbo.eu/s/oYf">http://overpass-turbo.eu/s/oYf</a></p>
</div>
<div id="comment-56133-info" class="comment-info">
<span class="comment-age">(11 May '17, 18:16)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="56134"></span>
<div id="comment-56134" class="comment">
<div id="post-56134-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know the performance but worry about the <code>way[highway](area.b)</code> query being expensive. An alternative way to find the inner area is to use a map_to_area query: <a href="http://overpass-turbo.eu/s/oYg">http://overpass-turbo.eu/s/oYg</a></p>
<p>It's a known issue that area limiters don't work on area queries.</p>
</div>
<div id="comment-56134-info" class="comment-info">
<span class="comment-age">(11 May '17, 18:33)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-56123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56123-form-container" class="comment-form-container">
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

