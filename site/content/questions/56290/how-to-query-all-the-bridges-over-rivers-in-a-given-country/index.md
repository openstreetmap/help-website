+++
type = "question"
title = "How to query all the bridges over rivers in a given country"
description = '''I am working on a project related to POIs mining and I want to know if there is a way to query all the bridges over rivers for a given country.  What I&#x27;ve done is the following:  [out:json]; (node[&quot;place&quot; = &quot;country&quot;][&quot;int_name&quot; = &quot;Portugal&quot;];way&quot;waterway&quot;=&quot;river&quot;;way&quot;bridge&quot; = &quot;yes&quot;); out; The thin...'''
date = "2017-05-24T16:15:00Z"
lastmod = "2017-05-24T19:05:00Z"
weight = 56290
keywords = [ "query", "tagging", "overpass-ql", "memory" ]
aliases = [ "/questions/56290" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to query all the bridges over rivers in a given country](/questions/56290/how-to-query-all-the-bridges-over-rivers-in-a-given-country)

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
<span id="post-56290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56290-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am working on a project related to POIs mining and I want to know if there is a way to query all the bridges over rivers for a given country.</p>
<p>What I've done is the following:</p>
<p>[out:json]; (node["place" = "country"]["int_name" = "Portugal"];way<span>"waterway"="river"</span>;way<span>"bridge" = "yes"</span>); out;</p>
<p>The thing is that if I increase the radius to cover the hole country I get: runtime error: Query run out of memory using about 2048 MB of RAM</p>
<p>I think that I'm missing s.th but I can't find how to do this in a better way since I'm new in working with QL.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-overpass-ql" rel="tag" title="see questions tagged &#39;overpass-ql&#39;">overpass-ql</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '17, 16:15</strong></p>
<img src="https://secure.gravatar.com/avatar/d9e40d52a77915f9dfaffcf45daac6a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TAYARI&#39;s gravatar image" />
<p><span>TAYARI</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TAYARI has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 May '17, 16:20</strong> </span></p>
</div>
</div>
<div id="comments-container-56290" class="comments-container">
<span id="56291"></span>
<div id="comment-56291" class="comment">
<div id="post-56291-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You will need something like <code>way(around:0)[bridge=yes];</code>, with the rivers as the input to that filter.</p>
<p>Not sure the public server will return all of Portugal at once. You'll have to set a large timeout.</p>
</div>
<div id="comment-56291-info" class="comment-info">
<span class="comment-age">(24 May '17, 17:06)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="56292"></span>
<div id="comment-56292" class="comment">
<div id="post-56292-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, Would you please clarify how to put the rivers as input ? Is it correct in the request that i have mentioned ?</p>
</div>
<div id="comment-56292-info" class="comment-info">
<span class="comment-age">(24 May '17, 17:29)</span> <span class="comment-user userinfo">TAYARI</span>
</div>
</div>
</div>
<div id="comment-tools-56290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56290-form-container" class="comment-form-container">
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

<span id="56294"></span>

<div id="answer-container-56294" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56294-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most of the statements in the QL take an input set and return an output set. They can be explicit, or there is an implicit default set (with each statement overwriting it).</p>
<p>So to make the rivers the input using the default set, that query would just need to be the previous statement.</p>
<p><a href="http://overpass-turbo.eu/s/pgp">Here's a demo using Overpass Turbo</a>. That uses a small bounding box to demonstrate the approach, the script can be modified to search Portugal:</p>
<pre><code>[out:json][timeout:600];
area(3600295480)-&gt;.searchArea;
way[&quot;waterway&quot;](area.searchArea);
way(around:0)[bridge=yes];
out body;
&gt;;
out skel qt;</code></pre>
<p>But the public server rejects the request as too large. One approach to work around that is to use smaller internal regions as the search area and multiple requests.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '17, 18:53</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 May '17, 18:54</strong> </span></p>
</div>
</div>
<div id="comments-container-56294" class="comments-container">
<span id="56295"></span>
<div id="comment-56295" class="comment">
<div id="post-56295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great, thank you. That's what I was looking for and yes, to avoid large requests, I am planning to make a grid of the country and query by cell.</p>
</div>
<div id="comment-56295-info" class="comment-info">
<span class="comment-age">(24 May '17, 19:05)</span> <span class="comment-user userinfo">TAYARI</span>
</div>
</div>
</div>
<div id="comment-tools-56294" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56294-form-container" class="comment-form-container">
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

