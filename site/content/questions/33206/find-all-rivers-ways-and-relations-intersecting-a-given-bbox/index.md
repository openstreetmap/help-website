+++
type = "question"
title = "Find all rivers (ways and relations) intersecting a given BBOX?"
description = '''I need to get all the way (waterway=river) and relation (type=waterway) intersecting an area. The &quot;is in&quot; query works only for objects excatly inside an area, right? I&#x27;ve tried the following QL query, but it doesn&#x27;t seem right: (node  (43.7634,11.289,43.7908,11.2153);  way(bn)[&#x27;waterway&#x27;=&#x27;river&#x27;] );...'''
date = "2014-05-15T18:15:00Z"
lastmod = "2014-05-15T19:06:00Z"
weight = 33206
keywords = [ "overpass", "overpass-ql" ]
aliases = [ "/questions/33206" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Find all rivers (ways and relations) intersecting a given BBOX?](/questions/33206/find-all-rivers-ways-and-relations-intersecting-a-given-bbox)

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
<span id="post-33206-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33206-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33206-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to get all the way (waterway=river) and relation (type=waterway) intersecting an area. The "is in" query works only for objects excatly inside an area, right?</p>
<p>I've tried the following QL query, but it doesn't seem right:</p>
<pre><code>(node
    (43.7634,11.289,43.7908,11.2153);
    way(bn)[&#39;waterway&#39;=&#39;river&#39;]
);
out body;</code></pre>
<p>I've also tried:</p>
<pre><code>(node
    (43.7634,11.289,43.7908,11.2153);
    way(bn)[&#39;waterway&#39;=&#39;river&#39;]-&gt;.a
);
(way.a[&#39;waterway&#39;=&#39;river&#39;]-&gt;.b);
.b out;</code></pre>
<p>Probably I don't understand the query syntax correctly...</p>
<p>Giovanni</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '14, 18:15</strong></p>
<img src="https://secure.gravatar.com/avatar/7b040693b6f5a34a7cc8a5f1c69f5bac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giohappy&#39;s gravatar image" />
<p><span>giohappy</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giohappy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jan '16, 19:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-33206" class="comments-container">
&#10;</div>
<div id="comment-tools-33206" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33206-form-container" class="comment-form-container">
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

<span id="33209"></span>

<div id="answer-container-33209" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33209-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This worked fine:</p>
<pre><code>(node
    (43.7634,11.2153,43.7908,11.289);
    way(bn)-&gt;.a
);
(way.a[&#39;waterway&#39;=&#39;river&#39;];&gt;);
out;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '14, 19:06</strong></p>
<img src="https://secure.gravatar.com/avatar/7b040693b6f5a34a7cc8a5f1c69f5bac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giohappy&#39;s gravatar image" />
<p><span>giohappy</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giohappy has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33209" class="comments-container">
&#10;</div>
<div id="comment-tools-33209" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33209-form-container" class="comment-form-container">
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

