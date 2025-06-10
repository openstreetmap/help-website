+++
type = "question"
title = "Local Overpass Server not Generating Areas"
description = '''Some areas are not generating on my local overpass server. This results in queries using &quot;is_in&quot; and &quot;map_to_area&quot; not giving the proper results. One such area is the area corresponding to this relation (Nicaragua province, NI-AS). Running an &quot;is_in&quot; query with features inside of this province does ...'''
date = "2021-09-24T21:34:00Z"
lastmod = "2021-09-27T16:56:00Z"
weight = 81944
keywords = [ "overpass", "database" ]
aliases = [ "/questions/81944" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Local Overpass Server not Generating Areas](/questions/81944/local-overpass-server-not-generating-areas)

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
<span id="post-81944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81944-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Some areas are not generating on my local overpass server. This results in queries using "is_in" and "map_to_area" not giving the proper results. One such area is the area corresponding to <a href="https://www.openstreetmap.org/relation/2195081#map=9/12.1803/-84.0289">this</a> relation (Nicaragua province, NI-AS). Running an "is_in" query with features inside of this province does not return the area, and "map_to_area" using that relation does not return an area either.</p>
<p>The area creation script ran without error and there's many other areas that are working fine, so I'm lost as to why this area would not exist for me. I don't think this is due to any broken geometry of the relation either, since it does not show up as such.</p>
<p>I've tried re-running the area creation script and downloading an extract of Nicaragua and applying it to the database, neither of which did anything. Here's the query that I've been running as I've tried to fix this (gives proper results using a public server but no results on my private one):</p>
<pre><code>nwr[&quot;ISO3166-2&quot;=&quot;NI-AS&quot;];
map_to_area;
out geom;</code></pre>
<p>Any help would be appreciated, thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Sep '21, 21:34</strong></p>
<img src="https://secure.gravatar.com/avatar/90c1a2a6f8b3789f0622ae27f3d92bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nbreden&#39;s gravatar image" />
<p><span>nbreden</span><br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nbreden has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81944" class="comments-container">
&#10;</div>
<div id="comment-tools-81944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81944-form-container" class="comment-form-container">
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

<span id="81952"></span>

<div id="answer-container-81952" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81952-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81952-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81952-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's unclear what your problem is. What output are you expecting, &amp; what are you receiving?</p>
<pre><code>area[&quot;ISO3166-2&quot;=&quot;NI-AS&quot;];
out geom;</code></pre>
<p>and</p>
<pre><code>rel[&quot;ISO3166-2&quot;=&quot;NI-AS&quot;];
map_to_area;
out geom;</code></pre>
<p>both return the data below, as expected, using OPT.</p>
<p><img src="https://help.openstreetmap.org/upfiles/Capture_ImTZKN2.JPG" alt="alt text" /></p>
<p>This returns the geometry</p>
<pre><code>rel[&quot;ISO3166-2&quot;=&quot;NI-AS&quot;];
out geom;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '21, 15:40</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</img>
</div>
</div>
<div id="comments-container-81952" class="comments-container">
<span id="81985"></span>
<div id="comment-81985" class="comment">
<div id="post-81985-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry if it was unclear, I'm saying that the above queries return <em>nothing</em> on my local server and I don't know how to fix it. The reason for this, I assume, is that the area for NI-AS does not exist on my local server.</p>
</div>
<div id="comment-81985-info" class="comment-info">
<span class="comment-age">(27 Sep '21, 16:56)</span> <span class="comment-user userinfo">nbreden</span>
</div>
</div>
</div>
<div id="comment-tools-81952" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81952-form-container" class="comment-form-container">
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

