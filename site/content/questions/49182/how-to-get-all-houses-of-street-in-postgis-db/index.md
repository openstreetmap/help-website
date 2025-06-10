+++
type = "question"
title = "How to get all houses of street in postgis db?"
description = '''I am tired of seeking a solution. :/ Help plz. public | planet_osm_line   public | planet_osm_nodes   public | planet_osm_point   public | planet_osm_polygon   public | planet_osm_rels   public | planet_osm_roads   public | planet_osm_ways  I&#x27;ve seen a lot of docs but yet I could&#x27;t do it.'''
date = "2016-04-11T16:35:00Z"
lastmod = "2016-04-12T10:08:00Z"
weight = 49182
keywords = [ "house", "street", "postgis" ]
aliases = [ "/questions/49182" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get all houses of street in postgis db?](/questions/49182/how-to-get-all-houses-of-street-in-postgis-db)

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
<span id="post-49182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49182-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am tired of seeking a solution. :/ Help plz.</p>
<p>public | planet_osm_line<br />
public | planet_osm_nodes<br />
public | planet_osm_point<br />
public | planet_osm_polygon<br />
public | planet_osm_rels<br />
public | planet_osm_roads<br />
public | planet_osm_ways</p>
<p>I've seen a lot of docs but yet I could't do it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-house" rel="tag" title="see questions tagged &#39;house&#39;">house</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '16, 16:35</strong></p>
<img src="https://secure.gravatar.com/avatar/67d248472d355604a4ed180d977df6e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SpbSprut&#39;s gravatar image" />
<p><span>SpbSprut</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SpbSprut has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '16, 16:40</strong> </span></p>
</div>
</div>
<div id="comments-container-49182" class="comments-container">
&#10;</div>
<div id="comment-tools-49182" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49182-form-container" class="comment-form-container">
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

<span id="49184"></span>

<div id="answer-container-49184" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49184-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-49184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is not necessarily a direct link between houses and streets in OSM. The following situations are frequent:</p>
<ul>
<li>house is mapped without a street address (<code>addr:street</code> tag) or relation (<code>type=associated_street</code>)</li>
<li>house has a street address tag</li>
<li>house is part of an associated_street relation</li>
</ul>
<p>Unfortunately addr:street tags are not imported by default when you run osm2pgsql; you need to add that column to the config file or import with <code>--hstore</code>. Then you can do something like</p>
<pre><code>SELECT way 
FROM planet_osm_polygon 
WHERE tags-&gt;&#39;addr:street&#39;=&#39;My Street&#39;</code></pre>
<p>You'll probably also want to check for <code>tags-&gt;'addr:city'</code> or for being contained in a certain administrative polygon. Accessing relations is possible when you have used <code>--slim</code> but difficult; it requires looking up the way ID of the house in question in the planet_osm_rels table. A simple alternative is loading all houses in a certain, small distance from a street like</p>
<pre><code>SELECT h.way
FROM planet_osm_polygon h, planet_osm_line s
WHERE s.highway IS NOT NULL and s.name=&#39;My Street&#39;
AND ST_DWITHIN(s.way, h.way, 50)</code></pre>
<p>This will of course also find houses belonging to other streets within the specified distance.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '16, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-49184" class="comments-container">
<span id="49193"></span>
<div id="comment-49193" class="comment">
<div id="post-49193-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much!</p>
<p>SELECT way FROM planet_osm_polygon WHERE tags-&gt;'addr:street'='My Street'</p>
<p>it works for me</p>
</div>
<div id="comment-49193-info" class="comment-info">
<span class="comment-age">(12 Apr '16, 10:08)</span> <span class="comment-user userinfo">SpbSprut</span>
</div>
</div>
</div>
<div id="comment-tools-49184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49184-form-container" class="comment-form-container">
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

