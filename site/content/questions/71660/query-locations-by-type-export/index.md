+++
type = "question"
title = "Query locations by type, export?"
description = '''Hi! Is there a way to query malls within a certain geographic area, and export a list, perhaps as a CSV?'''
date = "2019-11-15T22:23:00Z"
lastmod = "2019-11-16T13:19:00Z"
weight = 71660
keywords = [ "filter", "query", "csv", "export" ]
aliases = [ "/questions/71660" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Query locations by type, export?](/questions/71660/query-locations-by-type-export)

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
<span id="post-71660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71660-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi! Is there a way to query malls within a certain geographic area, and export a list, perhaps as a CSV?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '19, 22:23</strong></p>
<img src="https://secure.gravatar.com/avatar/edd82d90e8c1e9037f6b86c3bbfe7d56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NickMoreau&#39;s gravatar image" />
<p><span>NickMoreau</span><br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NickMoreau has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-71660" class="comments-container">
&#10;</div>
<div id="comment-tools-71660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71660-form-container" class="comment-form-container">
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

<span id="71661"></span>

<div id="answer-container-71661" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71661-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass-API is good for this type of query. <a href="http://overpass-turbo.eu/s/O8x">Here's a quick example</a> using Overpass Turbo to select the area of the query:</p>
<pre><code>[out:csv(name,::lat,::lon)][bbox:{{bbox}}];
nwr[shop=mall];
out center;</code></pre>
<p>It may be necessary to add more tags to really find all malls, depending on how they are tagged in the area of interest. This can be done by replacing the <code>nwr[shop=mall];</code> line with a union. For example, this query also returns areas tagged as commercial landuse:</p>
<pre><code>[out:csv(name,::lat,::lon)][bbox:{{bbox}}];
(
  nwr[shop=mall];
  nwr[landuse=commercial];
);
out center;</code></pre>
<p>You may also want to add additional tags to the <code>csv()</code> block. Each one will show up as a column in the result.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '19, 23:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-71661" class="comments-container">
<span id="71667"></span>
<div id="comment-71667" class="comment">
<div id="post-71667-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Wonderful, thank you! I'll try this out.</p>
<p>I have minimal coding experience -- enough to understand and modify your code, but not enough to start from scratch -- so I'm extremely grateful for your help.</p>
</div>
<div id="comment-71667-info" class="comment-info">
<span class="comment-age">(16 Nov '19, 13:00)</span> <span class="comment-user userinfo">NickMoreau</span>
</div>
</div>
<span id="71668"></span>
<div id="comment-71668" class="comment">
<div id="post-71668-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For a beginner the wizard on the Overpass Turbo does a good job. Open the wizard, fill in what you are looking for, "mall" in your case, and klick create query. Then run it.</p>
</div>
<div id="comment-71668-info" class="comment-info">
<span class="comment-age">(16 Nov '19, 13:19)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-71661" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71661-form-container" class="comment-form-container">
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

