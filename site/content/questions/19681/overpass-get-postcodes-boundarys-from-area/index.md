+++
type = "question"
title = "Overpass: Get postcodes-boundarys from area"
description = '''Hello! I try to get all postcodes from a area like &quot;Munich&quot;. I tried: &amp;lt;area-query ref=&quot;3600062428&quot; /&amp;gt;  &amp;lt;recurse type=&quot;node-relation&quot; /&amp;gt;  &amp;lt;query type=&quot;relation&quot;&amp;gt;  &amp;lt;item /&amp;gt;  &amp;lt;has-kv k=&quot;boundary&quot; v=&quot;postal_code&quot;/&amp;gt;  &amp;lt;/query&amp;gt; &amp;lt;print /&amp;gt;  but the result is just emp...'''
date = "2013-02-07T13:39:00Z"
lastmod = "2013-02-21T14:08:00Z"
weight = 19681
keywords = [ "overpass" ]
aliases = [ "/questions/19681" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: Get postcodes-boundarys from area](/questions/19681/overpass-get-postcodes-boundarys-from-area)

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
<span id="post-19681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19681-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!</p>
<p>I try to get all postcodes from a area like "Munich". I tried:</p>
<pre><code>&lt;area-query ref=&quot;3600062428&quot; /&gt;
 &lt;recurse type=&quot;node-relation&quot; /&gt;
 &lt;query type=&quot;relation&quot;&gt;
   &lt;item /&gt;
   &lt;has-kv k=&quot;boundary&quot; v=&quot;postal_code&quot;/&gt;
 &lt;/query&gt;
&lt;print /&gt;</code></pre>
<p>but the result is just empty. Any ideas how to do it? What I need are just the postcodes itself.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '13, 13:39</strong></p>
<img src="https://secure.gravatar.com/avatar/12f399704c1d69150128133157881125?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wuschba&#39;s gravatar image" />
<p><span>wuschba</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wuschba has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Feb '13, 13:40</strong> </span></p>
</div>
</div>
<div id="comments-container-19681" class="comments-container">
&#10;</div>
<div id="comment-tools-19681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19681-form-container" class="comment-form-container">
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

<span id="19744"></span>

<div id="answer-container-19744" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19744-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-19744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wuschba has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, please use "recurse type='up'" instead.</p>
<pre><code>&lt;area-query ref=&quot;3600062428&quot; /&gt;
  &lt;recurse **type=&quot;up&quot;** /&gt;
  &lt;query type=&quot;relation&quot;&gt;
    &lt;item /&gt;
    &lt;has-kv k=&quot;boundary&quot; v=&quot;postal_code&quot; /&gt;
  &lt;/query&gt;
&lt;print /&gt;</code></pre>
<p>Postal code boundaries are made of ways which in turn are made of nodes, so there is no direct connection between the nodes and the relations. For that reason, the recurse node-relation doesn't find anything. By contrast, recurse "up" searches also for these indirect memberships.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '13, 07:42</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Feb '13, 07:44</strong> </span></p>
</div>
</div>
<div id="comments-container-19744" class="comments-container">
<span id="20112"></span>
<div id="comment-20112" class="comment">
<div id="post-20112-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any idea why this won't work in Austria? Apetlon, 3600105619, should have the postcodes: 7132,7143,7161 but the result of the query</p>
<pre><code>node(area:3600105619);
&lt;;
relation._[&quot;boundary&quot;=&quot;postal_code&quot;];
out;</code></pre>
<p>stays empty.</p>
</div>
<div id="comment-20112-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 13:57)</span> <span class="comment-user userinfo">wuschba</span>
</div>
</div>
<span id="20115"></span>
<div id="comment-20115" class="comment">
<div id="post-20115-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Got a 2nd problem: The node for "Ingolstadt" gives me these postcodes: &lt;tag k="postal_code" v="85049,85051,85053,85055,85057"/&gt;</p>
<p>But doing your query on 3600062381, I get much more postcodes. What might be the problem?</p>
</div>
<div id="comment-20115-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 14:08)</span> <span class="comment-user userinfo">wuschba</span>
</div>
</div>
</div>
<div id="comment-tools-19744" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19744-form-container" class="comment-form-container">
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

