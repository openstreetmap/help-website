+++
type = "question"
title = "Overpass query: how to select certain ways that are in relations"
description = '''Wondering how to write an Overpass query to find ways in cycle route relations that have surface=paved tagged on the way. Here&#x27;s my best effort, which is doing fine getting ways within cycle relations, but is not filtering for ways tagged surface=paved: [out:json][timeout:90]; ( (rel[&quot;route&quot;=&quot;bicycl...'''
date = "2015-06-17T15:32:00Z"
lastmod = "2015-06-18T14:39:00Z"
weight = 43597
keywords = [ "ways", "overpass", "relations", "query" ]
aliases = [ "/questions/43597" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass query: how to select certain ways that are in relations](/questions/43597/overpass-query-how-to-select-certain-ways-that-are-in-relations)

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
<span id="post-43597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43597-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Wondering how to write an Overpass query to find ways in cycle route relations that have surface=paved tagged on the way. Here's my best effort, which is doing fine getting ways within cycle relations, but is not filtering for ways tagged surface=paved:</p>
<pre><code>[out:json][timeout:90];
(
(rel[&quot;route&quot;=&quot;bicycle&quot;]({{bbox}});)-&gt;.cr;
(.cr&gt;;)-&gt;.w;
(way.w[&quot;surface&quot;=&quot;paved&quot;];)-&gt;.sp;
);
.sp out body;
&gt;;
out skel qt;</code></pre>
<p>Note: this question came up on <a href="http://gis.stackexchange.com/questions/151108/an-overpass-query-for-osm-ways-both-part-of-a-relation-and-also-a-specific-tag">GIS StackExchange</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jun '15, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-43597" class="comments-container">
&#10;</div>
<div id="comment-tools-43597" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43597-form-container" class="comment-form-container">
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

<span id="43599"></span>

<div id="answer-container-43599" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43599-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-43599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="neuhausr has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I suggest <a href="http://overpass-turbo.eu/s/9Zf">http://overpass-turbo.eu/s/9Zf</a> instead.</p>
<p>Let's also do a walk-through of the above query:</p>
<p>The parentheses opening in line 2 and closing in line 6 mean that the input of line 8</p>
<pre><code>&gt;;</code></pre>
<p>are the union of the results in lines 3, 4, and 5. In particular, in line 3 we collect all the relations with "route"="bicycle". Thus, the recurse-down collects all the ways that are members of these relations. In line 9, these resulting ways, along also found nodes from these ways, are printed.</p>
<p>To avoid this, you need to remove the parentheses in line 2 and 6. Fruthermore, the parentheses in lines 3, 4, and 5 also have no effect, because there is in each case only a single query inside.</p>
<p>The remaining differences are that I have simplified the different set names to always the default set name. Because some relations may have an enormous extent, I have also added a "({{bbox}})" condition to the "way" query to restrict the results to the given bbox. It would work without, but admittedly slower. To speed up without bounding box, you can use</p>
<pre><code>[out:json][timeout:90];
rel[&quot;route&quot;=&quot;bicycle&quot;]({{bbox}});
way(r);
way._[&quot;surface&quot;=&quot;paved&quot;];
out geom;</code></pre>
<p>This splits the way query into two steps to enforce that the filtering for relation members is applied first.</p>
<p>Please feel free to paste back the content to GIS StackExchange. I consider my answers here as CC0.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jun '15, 17:05</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-43599" class="comments-container">
<span id="43616"></span>
<div id="comment-43616" class="comment">
<div id="post-43616-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks so much, especially for the walk-through pointing out where I went wrong!</p>
</div>
<div id="comment-43616-info" class="comment-info">
<span class="comment-age">(18 Jun '15, 14:39)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-43599" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43599-form-container" class="comment-form-container">
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

