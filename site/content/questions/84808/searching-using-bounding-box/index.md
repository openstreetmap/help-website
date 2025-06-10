+++
type = "question"
title = "Searching using bounding box"
description = '''I&#x27;m trying to obtain list of supermarkets in Santa Clara in CA, USA. I&#x27;ve crafted following query: area[name=&quot;California&quot;]-&amp;gt;.state; area[name=&quot;Santa Clara&quot;]-&amp;gt;.city; node(area.state)(area.city)[shop=supermarket]; out;  The problem is with cases that are inside Santa Clara (city) bounding box bu...'''
date = "2022-06-18T08:18:00Z"
lastmod = "2022-06-18T13:42:00Z"
weight = 84808
keywords = [ "overpassapi", "overpass" ]
aliases = [ "/questions/84808" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Searching using bounding box](/questions/84808/searching-using-bounding-box)

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
<span id="post-84808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84808-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to obtain list of supermarkets in Santa Clara in CA, USA. I've crafted following query:</p>
<pre><code>area[name=&quot;California&quot;]-&gt;.state;
area[name=&quot;Santa Clara&quot;]-&gt;.city;
node(area.state)(area.city)[shop=supermarket];
out;</code></pre>
<p>The problem is with cases that are inside Santa Clara (city) <a href="https://www.openstreetmap.org/relation/2221647#map=12/37.3888/-121.9022">bounding box</a> but doesn't have "city" or "state" values in their meta data.</p>
<p>Is there a way to search using bounding box instead of city name?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jun '22, 08:18</strong></p>
<img src="https://secure.gravatar.com/avatar/1246080c1e204d5a4a044bcd7108888a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sebap123&#39;s gravatar image" />
<p><span>sebap123</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sebap123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84808" class="comments-container">
&#10;</div>
<div id="comment-tools-84808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84808-form-container" class="comment-form-container">
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

<span id="84809"></span>

<div id="answer-container-84809" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84809-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sebap123 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There appears to be two problems: 1. You were asking it to return just nodes. 'nwr' (nodes, ways, relations) returns all objects. 2. The <code>out;</code> statement returns all entities (click the Data tab), but only renders nodes. Never been sure if this is a bug or 'Expected behaviour'</p>
<pre><code>area[name=&quot;California&quot;]-&gt;.state;
area[name=&quot;Santa Clara&quot;]-&gt;.city;
nwr(area.state)(area.city)[shop=supermarket];
out center;</code></pre>
<p>If you're going to make repeated use of the routine, I've found it more efficient to directly use the city's id:</p>
<pre><code>area(3602221647);
nwr[shop=supermarket](area);
out center;</code></pre>
<p>Also, take a look at my similar answer which gives you multiple options to do the same thing.</p>
<p><a href="https://help.openstreetmap.org/questions/84723/use-polygon-for-an-overpass-turbo-query">https://help.openstreetmap.org/questions/84723/use-polygon-for-an-overpass-turbo-query</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '22, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jun '22, 23:20</strong> </span></p>
</div>
</div>
<div id="comments-container-84809" class="comments-container">
&#10;</div>
<div id="comment-tools-84809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84809-form-container" class="comment-form-container">
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

