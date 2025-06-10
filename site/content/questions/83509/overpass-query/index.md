+++
type = "question"
title = "overpass query"
description = '''Please I need help. See the code below: query = &quot;way(%s, %s, %s, %s);(._;&amp;gt;;);out geom;&quot; % ( lat_min, lon_min, lat_max, lon_max )[&quot;highway&quot;=&quot;footway&quot;]  result=api.query(query)  My name is to use the four coordinates (lat_min, lon_min, lat_max, lon_max )to create a rectangular boundary for extracti...'''
date = "2022-02-17T15:11:00Z"
lastmod = "2022-02-18T08:43:00Z"
weight = 83509
keywords = [ "overpass-api" ]
aliases = [ "/questions/83509" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [overpass query](/questions/83509/overpass-query)

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
<span id="post-83509-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83509-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83509-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Please I need help. See the code below:</p>
<pre><code>query = &quot;way(%s, %s, %s, %s);(._;&gt;;);out geom;&quot; % ( lat_min, lon_min, lat_max, lon_max )[&quot;highway&quot;=&quot;footway&quot;]
&#10;result=api.query(query)</code></pre>
<p>My name is to use the four coordinates (<code>lat_min</code>, <code>lon_min</code>, <code>lat_max</code>, <code>lon_max</code> )to create a rectangular boundary for extracting particular highway information (e.g. footway), but I kept getting error on the syntax.</p>
<p>Please what are am i doing wrongly?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '22, 15:11</strong></p>
<img src="https://secure.gravatar.com/avatar/d91bc4f974e22ffeb60227442e03aafa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Segunlakata&#39;s gravatar image" />
<p><span>Segunlakata</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Segunlakata has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Feb '22, 16:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span></p>
</div>
</div>
<div id="comments-container-83509" class="comments-container">
<span id="83510"></span>
<div id="comment-83510" class="comment">
<div id="post-83510-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I think you need to provide more information "%s" is not overpass syntax so I presume you are building queries in something like php or python. Can you capture an example of the generated query &amp; show that instead?</p>
</div>
<div id="comment-83510-info" class="comment-info">
<span class="comment-age">(17 Feb '22, 15:32)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="83516"></span>
<div id="comment-83516" class="comment">
<div id="post-83516-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Supplementary information has been provided in a closed question here: <a href="https://help.openstreetmap.org/questions/83512/overpass-api">https://help.openstreetmap.org/questions/83512/overpass-api</a></p>
</div>
<div id="comment-83516-info" class="comment-info">
<span class="comment-age">(18 Feb '22, 08:43)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-83509" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83509-form-container" class="comment-form-container">
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

<span id="83514"></span>

<div id="answer-container-83514" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83514-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know python, but...</p>
<p>If you're making one call:</p>
<pre><code>way(49.89367,-97.212781,49.907792,-97.19422)[highway=footway];
(._;&gt;;);
out geom;</code></pre>
<p>If you need a global <code>bbox</code> for multiple calls</p>
<pre><code>[bbox:49.89367,-97.212781,49.907792,-97.19422];</code></pre>
<p>If you want to define a multi-sided polygon:</p>
<pre><code>way(poly:&quot;51.4591971 -0.9723236 51.7053402 -0.6110287 51.6639446 -0.3961114&quot;)[highway=unclassified];
(._;&gt;;);
out geom;</code></pre>
<p>PS When you next post a question can you provide a routine which doesn't return empty. It makes it hard to determine any errors.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '22, 20:39</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83514" class="comments-container">
&#10;</div>
<div id="comment-tools-83514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83514-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83511"></span>

<div id="answer-container-83511" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83511-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, I am using python. I wrote use this code below and it is working fine for me.</p>
<pre><code>import overpy
import json
from copy import deepcopy
import haversine as hs
import math
&#10;
api = overpy.Overpass()
#generate an intended map boundary for a given coordinates
&#10;result = api.query (f&#39;way(around:100,49.8974309,-97.2033944 )[&quot;highway&quot;=&quot;footway&quot;];(._;&gt;;);out geom;&#39;)</code></pre>
<p>where, radius=100m latitude =49.8974309 longitude=-97.2033944</p>
<p>But now, i do not want to use radius again, rather i want to use four coordinates like a rectangular bounding box to query osm for highway (e.g. footway in particular, in the specified area) using python.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '22, 16:06</strong></p>
<img src="https://secure.gravatar.com/avatar/d91bc4f974e22ffeb60227442e03aafa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Segunlakata&#39;s gravatar image" />
<p><span>Segunlakata</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Segunlakata has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Feb '22, 16:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span></p>
</div>
</div>
<div id="comments-container-83511" class="comments-container">
&#10;</div>
<div id="comment-tools-83511" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83511-form-container" class="comment-form-container">
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

