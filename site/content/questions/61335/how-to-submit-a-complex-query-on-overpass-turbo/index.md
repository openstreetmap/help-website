+++
type = "question"
title = "How to submit a complex query on Overpass-Turbo?"
description = '''I&#x27;m trying to submitting a query on Overpass-Turbo site that seems to be complex. I would like to get some historical data so I&#x27;m using date property. The problem is I always get the following error: An error occured during the execution of the overpass query! This is what overpass API returned: run...'''
date = "2017-12-23T18:12:00Z"
lastmod = "2017-12-27T15:36:00Z"
weight = 61335
keywords = [ "date", "statistics", "overpass-turbo", "historical", "history" ]
aliases = [ "/questions/61335" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to submit a complex query on Overpass-Turbo?](/questions/61335/how-to-submit-a-complex-query-on-overpass-turbo)

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
<span id="post-61335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61335-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to submitting a query on <a href="http://overpass-turbo.eu/s/tYr">Overpass-Turbo</a> site that seems to be complex. I would like to get some historical data so I'm using <code>date</code> property.</p>
<p>The problem is I always get the following error:</p>
<p><strong>An error occured during the execution of the overpass query! This is what overpass API returned: runtime error: Query run out of memory using about 2048 MB of RAM.</strong></p>
<p>I even tried to add <code>maxsize</code> property, according to <a href="https://github.com/drolbr/Overpass-API/issues/319">this issue</a>, but It didn't work.</p>
<p>Someone on IRC tells me that I should use <a href="http://download.geofabrik.de/">offline data</a> to make my query, but I cannot figure out how can I use it.</p>
<p>I would like to see how many italian hotels are on OSM every month since 2010 and how they grew, so I can make some statistics about them. How can I reach that purpose with OSM data?</p>
<p>Thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-date" rel="tag" title="see questions tagged &#39;date&#39;">date</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-historical" rel="tag" title="see questions tagged &#39;historical&#39;">historical</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Dec '17, 18:12</strong></p>
<img src="https://secure.gravatar.com/avatar/50334ab2e351e4f5af1917f7f6ef8dc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andreanovenove&#39;s gravatar image" />
<p><span>Andreanovenove</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andreanovenove has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Dec '17, 18:12</strong> </span></p>
</div>
</div>
<div id="comments-container-61335" class="comments-container">
&#10;</div>
<div id="comment-tools-61335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61335-form-container" class="comment-form-container">
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

<span id="61338"></span>

<div id="answer-container-61338" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61338-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Andreanovenove has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've tried the following query with no problem:</p>
<pre><code>[timeout:250];
(
  node(area:3600365331)(newer:&quot;2017-12-01T00:00:00Z&quot;)[&quot;tourism&quot;=&quot;hotel&quot;];
  way(area:3600365331)(newer:&quot;2017-12-01T00:00:00Z&quot;)[&quot;tourism&quot;=&quot;hotel&quot;];
  relation(area:3600365331)(newer:&quot;2017-12-01T00:00:00Z&quot;)[&quot;tourism&quot;=&quot;hotel&quot;];  
);
out meta;</code></pre>
<p>It gives you all nodes, ways and relations tagged as tourism=hotel inside Italy created from the beginning of December 2017. As for now, they are 106 nodes, 53 ways and 1 relation, so 160 new hotels in Italy since 1st December 2017.</p>
<p>If you run the same query with <code>(newer:"2017-11-01T00:00:00Z")</code>, you get all hotels from the beginning of November. Running now the query gave me 223 nodes, 163 ways and 8 relations, so 394 hotels. That means that in November there have been created 394 - 160 = 234 hotels.</p>
<p>Maybe that helps you?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Dec '17, 03:56</strong></p>
<img src="https://secure.gravatar.com/avatar/d45c161edd4b471fd947a7ec574274ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edvac&#39;s gravatar image" />
<p><span>edvac</span><br />
<span class="score" title="665 reputation points">665</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edvac has 4 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-61338" class="comments-container">
<span id="61382"></span>
<div id="comment-61382" class="comment">
<div id="post-61382-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it could be a solution, anyway it is not responding to my question.</p>
</div>
<div id="comment-61382-info" class="comment-info">
<span class="comment-age">(27 Dec '17, 11:00)</span> <span class="comment-user userinfo">Andreanovenove</span>
</div>
</div>
</div>
<div id="comment-tools-61338" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61338-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61384"></span>

<div id="answer-container-61384" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61384-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi:</p>
<p>Sorry, I just focused in solving your task, not your problem with your query and that runtime error. But in fact I hadn't noticed that the query was linked in the first tense of your message...</p>
<p>I was guessing the error with your query was with line</p>
<pre><code>{{geocodeArea:Italy}}-&gt;.searchArea;</code></pre>
<p>That the line gets all Italy data before processing it, that is a lot of data. But I am not sure...</p>
<p>Note also that you shouldn't add the last 2 lines:</p>
<pre><code>&gt;;
out meta qt;</code></pre>
<p>Those lines get the nodes and the ways of all relations as well, and the nodes of all ways. But you are interested in nodes, ways and relations that are tagged as <strong>tourism=hotel</strong> only.</p>
<p>Anyway, I found a good solution for you, much better than my previous answer:</p>
<p>With the following query you get all hotels in Italy at present:</p>
<pre><code>[out:csv(::timestamp)][timeout:150];
(
node[&quot;tourism&quot;=&quot;hotel&quot;](area:3600365331);
way[&quot;tourism&quot;=&quot;hotel&quot;](area:3600365331);
relation[&quot;tourism&quot;=&quot;hotel&quot;](area:3600365331);
);
out meta;</code></pre>
<p>You save the data into a file that you may name like <strong>italianHotels.csv</strong> for example.</p>
<p>Then, to check all hotels created in May 2009 for example, you run this UNIX command:</p>
<pre><code>cat italianHotels.csv | grep &quot;2009-05&quot; | wc -l</code></pre>
<p>That will give you the hotels whose last version is timestamped in May 2009. In our case, we get <strong>24</strong> hotels.</p>
<p>Or you can open the .csv file in a spreadsheet and get all hotels by month and year with functions.</p>
<p>Note that all these gives you the hotels with the last version, not the hotels when they were first created (version=1). For that I don't think it is possible to do it with Overpass...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Dec '17, 15:36</strong></p>
<img src="https://secure.gravatar.com/avatar/d45c161edd4b471fd947a7ec574274ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edvac&#39;s gravatar image" />
<p><span>edvac</span><br />
<span class="score" title="665 reputation points">665</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edvac has 4 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-61384" class="comments-container">
&#10;</div>
<div id="comment-tools-61384" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61384-form-container" class="comment-form-container">
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

