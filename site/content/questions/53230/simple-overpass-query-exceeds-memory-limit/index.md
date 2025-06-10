+++
type = "question"
title = "Simple Overpass query exceeds memory limit"
description = '''Hello everyone, I&#x27;m successfully extracting all buildings in a city with the following query  [out:json][timeout:500];area($AREA_ID)-&amp;gt;.searchArea;(way[&quot;building&quot;][&quot;building&quot;!=&quot;no&quot;](area.searchArea););out body;&amp;gt;;out skel qt;  where $AREA_ID is the relation id of the city + 3600000000. It works ...'''
date = "2016-12-03T21:43:00Z"
lastmod = "2016-12-04T01:09:00Z"
weight = 53230
keywords = [ "overpass", "memory", "limit", "query" ]
aliases = [ "/questions/53230" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Simple Overpass query exceeds memory limit](/questions/53230/simple-overpass-query-exceeds-memory-limit)

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
<span id="post-53230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53230-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-53230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>I'm successfully extracting all buildings in a city with the following query</p>
<pre><code>[out:json][timeout:500];area($AREA_ID)-&gt;.searchArea;(way[&quot;building&quot;][&quot;building&quot;!=&quot;no&quot;](area.searchArea););out body;&gt;;out skel qt;</code></pre>
<p>where $AREA_ID is the relation id of the city + 3600000000.</p>
<p>It works for many cities such as Paderborn, Düsseldorf, Frankfurt and Munich. However, it does not work for Cologne, Berlin and Hamburg. The problem is that the query exceeds the memory limit, the default being 2GB. I managed to increase it by using [maxsize: ... ] but it still says "Query run out of memory using about 4845 MB of RAM." and I can't increase the memory limit more on the public overpass servers (and I don't have a private server with more ram).</p>
<p>Is there a way to make this query consume less memory? Why does it even exceed these limits? If 2GB is enough for a city like Munich then almost 5GB should be enough for Cologne (Cologne is smaller than Munich). I've found old posts suggesting to use regular expressions to filter for attributes, but that doesn't seem to make anything better.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span> <span class="post-tag tag-link-limit" rel="tag" title="see questions tagged &#39;limit&#39;">limit</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Dec '16, 21:43</strong></p>
<img src="https://secure.gravatar.com/avatar/d7cfaa9df03174c6590aae81e64b73ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OSM%20noob&#39;s gravatar image" />
<p><span>OSM noob</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OSM noob has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53230" class="comments-container">
&#10;</div>
<div id="comment-tools-53230" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53230-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="53231"></span>

<div id="answer-container-53231" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53231-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-53231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please try the following query:</p>
<pre><code>[out:json][timeout:500];
area($AREA_ID)-&gt;.searchArea;
way(area.searchArea);
way._[&quot;building&quot;][&quot;building&quot;!=&quot;no&quot;];
out; &gt;; out skel qt;</code></pre>
<p>This enforces the order of filtering. It is necessary in this case to first filter for all ways in Cologne, then filter for all buildings. If you count the number of buildings then you will recognize that Cologne has indeed almost double the number of buldings than Munich.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '16, 22:06</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-53231" class="comments-container">
<span id="53234"></span>
<div id="comment-53234" class="comment">
<div id="post-53234-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>works great, thanks</p>
</div>
<div id="comment-53234-info" class="comment-info">
<span class="comment-age">(04 Dec '16, 01:09)</span> <span class="comment-user userinfo">OSM noob</span>
</div>
</div>
</div>
<div id="comment-tools-53231" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53231-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53232"></span>

<div id="answer-container-53232" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53232-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to run this query for more that just a few cities, consider downloading a Germany (or Europe, or World) data file, importing it into a database with osm2pgsql (using a modified import style file that only processes buildings and possibly administrative areas if you need them), and then running SQL queries against that database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '16, 23:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-53232" class="comments-container">
&#10;</div>
<div id="comment-tools-53232" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53232-form-container" class="comment-form-container">
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

