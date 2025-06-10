+++
type = "question"
title = "Overpass: Gather information on ways for a given area passing coordinates to query"
description = '''Hello, I am new to OSM. So I apologize if my question is trivial. I would like to gather lenghts of ways in a given rectangle. I am able to search for given area name (for instance Bonn) and it works: [out:csv(length,value)]; area[name=&quot;Bonn&quot;]-&amp;gt;.a; area[name=&quot;Bonn&quot;]-&amp;gt;.b; way[highway](area.a)(a...'''
date = "2023-02-10T07:49:00Z"
lastmod = "2023-02-11T19:38:00Z"
weight = 86663
keywords = [ "overpass", "area", "bbox", "coordinates", "query" ]
aliases = [ "/questions/86663" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: Gather information on ways for a given area passing coordinates to query](/questions/86663/overpass-gather-information-on-ways-for-a-given-area-passing-coordinates-to-query)

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
<span id="post-86663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86663-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am new to OSM. So I apologize if my question is trivial. I would like to gather lenghts of ways in a given rectangle.</p>
<p>I am able to search for given area name (for instance Bonn) and it works:</p>
<pre><code>[out:csv(length,value)];
area[name=&quot;Bonn&quot;]-&gt;.a;
area[name=&quot;Bonn&quot;]-&gt;.b;
way[highway](area.a)(area.b);
for (t[&quot;highway&quot;])
{
  make stat value=_.val,length=sum(length());
  out;
}</code></pre>
<p>But now I would like to to it for a given rectangle (passing coordinates). I tried with this but it does not work:</p>
<pre><code>[out:csv(length,value)];
[bbox:50.6,7.0,50.8,7.3]-&gt;.a;
way[highway](area.a);
for (t[&quot;highway&quot;])
{
  make stat value=_.val,length=sum(length());
  out;
}</code></pre>
<p>And even in this way I still get errors:</p>
<pre><code>[out:csv(length,value)];
[bbox:50.6,7.0,50.8,7.3];
way[highway]({{bbox}});
for (t[&quot;highway&quot;])
{
  make stat value=_.val,length=sum(length());
  out;
}</code></pre>
<p>Could you help me fix this?</p>
<p>Thanks a lot!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span> <span class="post-tag tag-link-bbox" rel="tag" title="see questions tagged &#39;bbox&#39;">bbox</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '23, 07:49</strong></p>
<img src="https://secure.gravatar.com/avatar/1c3403ae47723a065c5350782b05c857?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fregiz&#39;s gravatar image" />
<p><span>Fregiz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fregiz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Feb '23, 07:52</strong> </span></p>
</div>
</div>
<div id="comments-container-86663" class="comments-container">
&#10;</div>
<div id="comment-tools-86663" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86663-form-container" class="comment-form-container">
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

<span id="86680"></span>

<div id="answer-container-86680" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86680-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It was as simple as that:</p>
<pre><code>[out:csv(length,value)];
way[highway](50.6,7.0,50.8,7.3);
for (t[&quot;highway&quot;])
{
  make stat value=_.val,length=sum(length());
  out;
}</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '23, 19:38</strong></p>
<img src="https://secure.gravatar.com/avatar/1c3403ae47723a065c5350782b05c857?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fregiz&#39;s gravatar image" />
<p><span>Fregiz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fregiz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86680" class="comments-container">
&#10;</div>
<div id="comment-tools-86680" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86680-form-container" class="comment-form-container">
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

