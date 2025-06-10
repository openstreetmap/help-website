+++
type = "question"
title = "Extracting administrative boundary within an area"
description = '''Hello, I&#x27;m willing to extract administrative boundaries from level 1 to level 11 within a country using Overpass API. I&#x27;m using Overpass area object to filter the search. I need help to understand why this query (https://overpass-turbo.eu/s/1HwX) is retrieving the administrative boundary level 2 of ...'''
date = "2024-02-19T09:34:00Z"
lastmod = "2024-02-19T23:14:00Z"
weight = 88247
keywords = [ "overpassapi", "overpass", "admin_boundary", "area" ]
aliases = [ "/questions/88247" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting administrative boundary within an area](/questions/88247/extracting-administrative-boundary-within-an-area)

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
<span id="post-88247-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88247-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-88247-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm willing to extract administrative boundaries from level 1 to level 11 within a country using Overpass API. I'm using Overpass area object to filter the search. I need help to understand why this query (<a href="https://overpass-turbo.eu/s/1HwX)">https://overpass-turbo.eu/s/1HwX)</a> is retrieving the administrative boundary level 2 of Italy and Netherlands while I was expecting to only get the one for France.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '24, 09:34</strong></p>
<img src="https://secure.gravatar.com/avatar/4bded1989bb49f71f492bf4738e73fb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="picote&#39;s gravatar image" />
<p><span>picote</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="picote has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-88247" class="comments-container">
&#10;</div>
<div id="comment-tools-88247" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88247-form-container" class="comment-form-container">
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

<span id="88248"></span>

<div id="answer-container-88248" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88248-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-88248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, to answer your query - you were getting caught up in duplication:</p>
<pre><code>rel[admin_level=2][name=France];
out geom;</code></pre>
<p>This returns all of France's territories. You may wish to use this relation: <a href="http://"></a><a href="https://www.openstreetmap.org/relation/1403916#map=5/44.980/5.537">https://www.openstreetmap.org/relation/1403916#map=5/44.980/5.537</a></p>
<p>As you eventually want to return all admin_levels, I recommend downloading from <a href="http://"></a><a href="https://osm-boundaries.com/">https://osm-boundaries.com/</a> as direct calls would heavily burden the Overpass server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '24, 12:37</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-88248" class="comments-container">
<span id="88249"></span>
<div id="comment-88249" class="comment">
<div id="post-88249-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer and for redirecting me to the right tool. By reading more carefuly the documentation (<a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative#Administrative_boundary_in_case_of_disputes),">https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dadministrative#Administrative_boundary_in_case_of_disputes),</a> I now understand that administrative boundaries may overlap due to conflict or agreement to administer area together.</p>
</div>
<div id="comment-88249-info" class="comment-info">
<span class="comment-age">(19 Feb '24, 23:14)</span> <span class="comment-user userinfo">picote</span>
</div>
</div>
</div>
<div id="comment-tools-88248" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88248-form-container" class="comment-form-container">
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

