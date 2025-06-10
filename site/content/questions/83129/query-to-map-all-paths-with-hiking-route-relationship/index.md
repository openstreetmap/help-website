+++
type = "question"
title = "Query-to-Map: All paths with Hiking Route relationship"
description = '''I am looking to form a Query-to-Map statement that will show all the Paths within a specified Bounding Box that have a given Hiking Route relationship (= &quot;Lake Hopatcong Trail&quot;). Would someone suggest the appropriate syntax?  If there is an alternate approach, I am &quot;all ears&quot;.  --Thanks'''
date = "2022-01-20T15:44:00Z"
lastmod = "2022-01-21T15:06:00Z"
weight = 83129
keywords = [ "overpass", "route", "query-to-map", "overpass-turbo", "hiking" ]
aliases = [ "/questions/83129" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Query-to-Map: All paths with Hiking Route relationship](/questions/83129/query-to-map-all-paths-with-hiking-route-relationship)

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
<span id="post-83129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83129-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking to form a Query-to-Map statement that will show all the Paths within a specified Bounding Box that have a given Hiking Route relationship (= "Lake Hopatcong Trail"). Would someone suggest the appropriate syntax?</p>
<p>If there is an alternate approach, I am "all ears".</p>
<p>--Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-query-to-map" rel="tag" title="see questions tagged &#39;query-to-map&#39;">query-to-map</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-hiking" rel="tag" title="see questions tagged &#39;hiking&#39;">hiking</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jan '22, 15:44</strong></p>
<img src="https://secure.gravatar.com/avatar/63e6efaf5ae5774b948eb0e6bf40c84f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob009&#39;s gravatar image" />
<p><span>Rob009</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob009 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jan '22, 15:07</strong> </span></p>
</div>
</div>
<div id="comments-container-83129" class="comments-container">
&#10;</div>
<div id="comment-tools-83129" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83129-form-container" class="comment-form-container">
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

<span id="83142"></span>

<div id="answer-container-83142" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83142-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A Reddit user suggested using "Overpass turbo" for this query. Here is a link to the query: <a href="https://overpass-turbo.eu/s/1fhW">https://overpass-turbo.eu/s/1fhW</a></p>
<pre><code>/*
This query looks for nodes, ways and relations 
with the given key/value combination.
Choose your region and hit the Run button above!
*/
[out:json][timeout:25];
// gather results
(
  // query part
  relation[&quot;name&quot;=&quot;Lake Hopatcong Trail&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jan '22, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/63e6efaf5ae5774b948eb0e6bf40c84f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob009&#39;s gravatar image" />
<p><span>Rob009</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob009 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83142" class="comments-container">
&#10;</div>
<div id="comment-tools-83142" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83142-form-container" class="comment-form-container">
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

