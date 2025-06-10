+++
type = "question"
title = "polygon as global area for overpass query"
description = '''I have been trying to provide a polygon with an array of coordinates as a global parameter for my overpass query. But the query is through syntax error. [bbox:poly:&quot;50.7 7.1 50.7 7.2 50.75 7.15&quot;]; node[amenity=cafe]; out;  Error: line 1: parse error: &#x27;,&#x27; or &#x27;]&#x27; expected - &#x27;:&#x27; found. Error: line 1: s...'''
date = "2018-11-29T13:37:00Z"
lastmod = "2018-11-29T13:37:00Z"
weight = 66988
keywords = [ "overpass", "overpass-ql", "polygon", "bounding-polygon", "area" ]
aliases = [ "/questions/66988" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [polygon as global area for overpass query](/questions/66988/polygon-as-global-area-for-overpass-query)

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
<span id="post-66988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66988-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been trying to provide a polygon with an array of coordinates as a global parameter for my overpass query. But the query is through syntax error.</p>
<pre><code>[bbox:poly:&quot;50.7 7.1 50.7 7.2 50.75 7.15&quot;];
node[amenity=cafe];
out;</code></pre>
<p>Error: line 1: parse error: ',' or ']' expected - ':' found. Error: line 1: static error: A bounding box needs four comma-separated values. Error: line 1: static error: A bounding box needs four comma-separated values. Error: line 1: static error: A bounding box needs four comma-separated values. Error: line 1: parse error: ';' expected - ']' found.</p>
<p>Providing a bounding box instead works as expected.</p>
<pre><code>[bbox:50.7,7.1,50.75,7.25];
node[amenity=cafe];
out;</code></pre>
<p>It also works when the polygon is given in-line,</p>
<pre><code>node[amenity=cafe](poly:&quot;50.7 7.1 50.7 7.2 50.75 7.15&quot;);
out;</code></pre>
<p>(as suggested in <a href="https://dev.overpass-api.de/blog/bounding_boxes.html">this tutorial</a>)</p>
<p>As final attemp when below query was tried no error was given but also the result was blank.</p>
<pre><code>area[&quot;50.7 7.1 50.7 7.2 50.75 7.15&quot;];
node[amenity=cafe](area);
out;</code></pre>
<p>Is it possible to give a polygon instead of bounding box as a globle parameter in an Overpass query. Could not find any documentation over the Overpass wiki pages that supports the thing I am trying here.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-bounding-polygon" rel="tag" title="see questions tagged &#39;bounding-polygon&#39;">bounding-polygon</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Nov '18, 13:37</strong></p>
<img src="https://secure.gravatar.com/avatar/ef1bb309497d56d45a23249ef5fdff4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user1894&#39;s gravatar image" />
<p><span>user1894</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user1894 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66988" class="comments-container">
&#10;</div>
<div id="comment-tools-66988" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66988-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

