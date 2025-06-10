+++
type = "question"
title = "Getting street names"
description = '''Hi everyone. How can I get street names from planet_osm_line? I use this query to get: select planet_osm_line.name fromn planet_osm_line where (highway=&#x27;living_street&#x27; or highway=&#x27;motorway&#x27; or highway=&#x27;primary&#x27; or highway=&#x27;proposed&#x27; or highway=&#x27;raceway&#x27; or highway=&#x27;residential&#x27; or highway=&#x27;road&#x27; or ...'''
date = "2012-03-13T07:19:00Z"
lastmod = "2012-03-13T17:09:00Z"
weight = 11154
keywords = [ "query", "streetnames" ]
aliases = [ "/questions/11154" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting street names](/questions/11154/getting-street-names)

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
<span id="post-11154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11154-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone.</p>
<p>How can I get street names from planet_osm_line? I use this query to get:</p>
<pre><code>select planet_osm_line.name fromn planet_osm_line where (highway=&#39;living_street&#39; or highway=&#39;motorway&#39; or highway=&#39;primary&#39; or highway=&#39;proposed&#39; or highway=&#39;raceway&#39; or highway=&#39;residential&#39; or highway=&#39;road&#39; or highway=&#39;secondary&#39; or highway=&#39;tertiary&#39; or highway=&#39;track&#39; or highway=&#39;trunk&#39; or highway=&#39;unclassified&#39; or route=&#39;road&#39;) and LENGTH(Name)&gt;5 group by planet_osm_line.name;</code></pre>
<p>So I got really few names - about 1-2 thousands, but streets rows are about 400 000, that's are more real (where are other names?)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Mar '12, 07:19</strong></p>
<img src="https://secure.gravatar.com/avatar/04a50c0f1ba0dbf4a36e948646b8f47d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zzzzteph&#39;s gravatar image" />
<p><span>zzzzteph</span><br />
<span class="score" title="30 reputation points">30</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zzzzteph has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11154" class="comments-container">
<span id="11157"></span>
<div id="comment-11157" class="comment">
<div id="post-11157-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are multiple possible database schemas possible, depending on which tool and which options you used to load the .osm into postgres. What is you schema ?</p>
</div>
<div id="comment-11157-info" class="comment-info">
<span class="comment-age">(13 Mar '12, 09:15)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="11158"></span>
<div id="comment-11158" class="comment">
<div id="post-11158-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>osm2psql with standart options.</p>
<p>planet_osm_line planet_osm_nodes planet_osm_way planet_osm_polygon</p>
</div>
<div id="comment-11158-info" class="comment-info">
<span class="comment-age">(13 Mar '12, 09:40)</span> <span class="comment-user userinfo">zzzzteph</span>
</div>
</div>
<span id="11172"></span>
<div id="comment-11172" class="comment">
<div id="post-11172-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So, how can I get Street name from database (osm2psql) by its Id using sql query?</p>
</div>
<div id="comment-11172-info" class="comment-info">
<span class="comment-age">(13 Mar '12, 17:09)</span> <span class="comment-user userinfo">zzzzteph</span>
</div>
</div>
</div>
<div id="comment-tools-11154" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11154-form-container" class="comment-form-container">
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

<span id="11155"></span>

<div id="answer-container-11155" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11155-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your query misses some street types that might well have names (e.g. service, cycleway). Other types in your query (motorway, trunk) often don't have names at all, just "ref" numbers. Also, there are places where even residential roads aren't named in OSM because they have been traced from aerial imagery and those who did the tracing lacked the local knowledge to add names.</p>
<p>What is the exact query that you executed (the one quoted in your question is not valid SQL), and on what data set? The number of all rows in planet_osm_lines matching your criteria is about 17.5 million on a current (March 2012) planet database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '12, 07:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-11155" class="comments-container">
<span id="11156"></span>
<div id="comment-11156" class="comment">
<div id="post-11156-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is it. It's for postgresql and it works fine, exept that I didn't get all names.</p>
<p>I use only "roads" street's. My database is only a part of planet_world (Europian part). I need some query with what I can get all roads names(motorway,trunk are not needed).</p>
</div>
<div id="comment-11156-info" class="comment-info">
<span class="comment-age">(13 Mar '12, 07:51)</span> <span class="comment-user userinfo">zzzzteph</span>
</div>
</div>
</div>
<div id="comment-tools-11155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11155-form-container" class="comment-form-container">
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

