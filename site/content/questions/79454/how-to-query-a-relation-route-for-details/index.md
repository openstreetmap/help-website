+++
type = "question"
title = "How to query a relation (route) for details?"
description = '''Is there a way to get the total distance and distance of the different types of ways that make up a relation such as this one? https://www.openstreetmap.org/relation/2954632 For example I&#x27;d like to know how many kilometers of divided motorway, non-divided primary, etc. make up this route. Do I need ...'''
date = "2021-03-30T19:50:00Z"
lastmod = "2021-03-30T21:27:00Z"
weight = 79454
keywords = [ "overpass", "route", "relations", "query" ]
aliases = [ "/questions/79454" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to query a relation (route) for details?](/questions/79454/how-to-query-a-relation-route-for-details)

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
<span id="post-79454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79454-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to get the total distance and distance of the different types of ways that make up a relation such as this one? <a href="https://www.openstreetmap.org/relation/2954632">https://www.openstreetmap.org/relation/2954632</a></p>
<p>For example I'd like to know how many kilometers of divided motorway, non-divided primary, etc. make up this route. Do I need to hire a programmer or is there an Overpass query that can generate this kind of data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Mar '21, 19:50</strong></p>
<img src="https://secure.gravatar.com/avatar/11803a48d9205fdad68e6bcc3508505a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdchachi&#39;s gravatar image" />
<p><span>mdchachi</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdchachi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79454" class="comments-container">
&#10;</div>
<div id="comment-tools-79454" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79454-form-container" class="comment-form-container">
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

<span id="79458"></span>

<div id="answer-container-79458" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79458-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Some of this information is available with no programming from the Relation Analyzer tool: <a href="http://ra.osmsurround.org/analyzeRelation?relationId=2954632&amp;_noCache=on">http://ra.osmsurround.org/analyzeRelation?relationId=2954632&amp;_noCache=on</a></p>
<p>By downloading the Way Distribution you can see that this example is almost entirely highway=trunk.</p>
<p>Note that the main highway tag in OSM does not necessarily map directly to concepts such as "divided highway", this tends to be quite country-specific.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '21, 21:10</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-79458" class="comments-container">
&#10;</div>
<div id="comment-tools-79458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79458-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="79459"></span>

<div id="answer-container-79459" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79459-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would like to suggest <a href="https://overpass-turbo.eu/s/15BQ">https://overpass-turbo.eu/s/15BQ</a>:</p>
<pre><code>[out:csv(length,highway,oneway)];
relation(2954632)-&gt;.parent;
way(r.parent)[oneway=yes];
for (t[&quot;highway&quot;])
{
  make stat highway=_.val,oneway=set(t[&quot;oneway&quot;]),length=sum(length())/2;
  out;
}
way(r.parent)[oneway!=yes];
for (t[&quot;highway&quot;])
{
  make stat highway=_.val,oneway=set(t[&quot;oneway&quot;]),length=sum(length());
  out;
}</code></pre>
<p>Lines 4 and 10 express that you want to sum by the value of the highway tag and could be replaced by another expression. Lines 3 and 10 ensure that oneways and none-oneways are processes separately. Line 6 has a division by 2 to count oneways only with half of their length.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '21, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-79459" class="comments-container">
&#10;</div>
<div id="comment-tools-79459" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79459-form-container" class="comment-form-container">
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

