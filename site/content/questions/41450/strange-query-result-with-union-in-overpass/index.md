+++
type = "question"
title = "Strange query result with union in overpass"
description = '''&amp;lt;query type=&quot;way&quot;&amp;gt; &amp;lt;has-kv k=&quot;int_ref&quot; v=&quot;E 40&quot;/&amp;gt; &amp;lt;/query&amp;gt; &amp;lt;union&amp;gt; &amp;lt;query type =&quot;node&quot;&amp;gt; &amp;lt;bbox-query s=&quot;49.7688&quot; n=&quot;50.1479&quot; e=&quot;22.8337&quot; w=&quot;21.9143&quot;/&amp;gt; &amp;lt;around radius=&quot;4500&quot;/&amp;gt; &amp;lt;has-kv k=&quot;place&quot; v=&quot;town&quot;/&amp;gt; &amp;lt;/query&amp;gt; &amp;lt;query type =&quot;node&quot;&amp;gt; &amp;lt;bbo...'''
date = "2015-03-02T13:43:00Z"
lastmod = "2015-03-03T07:26:00Z"
weight = 41450
keywords = [ "union", "query", "overpass" ]
aliases = [ "/questions/41450" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Strange query result with union in overpass](/questions/41450/strange-query-result-with-union-in-overpass)

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
<span id="post-41450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41450-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<pre><code>&lt;query type=&quot;way&quot;&gt;
&lt;has-kv k=&quot;int_ref&quot; v=&quot;E 40&quot;/&gt;
&lt;/query&gt;
&lt;union&gt;
&lt;query type =&quot;node&quot;&gt;
&lt;bbox-query s=&quot;49.7688&quot; n=&quot;50.1479&quot; e=&quot;22.8337&quot; w=&quot;21.9143&quot;/&gt;
&lt;around radius=&quot;4500&quot;/&gt;
&lt;has-kv k=&quot;place&quot; v=&quot;town&quot;/&gt;
&lt;/query&gt;
&lt;query type =&quot;node&quot;&gt;
&lt;bbox-query s=&quot;49.7688&quot; n=&quot;50.1479&quot; e=&quot;22.8337&quot; w=&quot;21.9143&quot;/&gt;
&lt;around radius=&quot;4500&quot;/&gt;
&lt;has-kv k=&quot;place&quot; v=&quot;city&quot;/&gt;
&lt;/query&gt;
&lt;query type =&quot;node&quot;&gt;
&lt;bbox-query s=&quot;49.7688&quot; n=&quot;50.1479&quot; e=&quot;22.8337&quot; w=&quot;21.9143&quot;/&gt;
&lt;around radius=&quot;4500&quot;/&gt;
&lt;has-kv k=&quot;place&quot; v=&quot;village&quot;/&gt;
&lt;/query&gt;
&lt;/union&gt;
&lt;print/&gt;</code></pre>
<p>The following query should return all the nodes with k value town, village or city withing the given bound box and no more further than 4500 from way referenced E 40. However in xml result there is no "city" values. When I cut out &lt;union&gt; with "town" and "village" query and search only for those with key value "city" then the result is ok . I wonder what is the reason. Regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-union" rel="tag" title="see questions tagged &#39;union&#39;">union</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '15, 13:43</strong></p>
<img src="https://secure.gravatar.com/avatar/c94180557aecf86091ae161baf7ac008?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="huberttt&#39;s gravatar image" />
<p><span>huberttt</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="huberttt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Mar '15, 14:11</strong> </span></p>
</div>
</div>
<div id="comments-container-41450" class="comments-container">
<span id="41459"></span>
<div id="comment-41459" class="comment">
<div id="post-41459-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is really odd. When I ran it as you have written above, I only received town results. If I eliminate town I receive some but not all city and village results.</p>
<pre><code>&lt;query type=&quot;way&quot;&gt;
&lt;has-kv k=&quot;int_ref&quot; v=&quot;E 40&quot;/&gt;
&lt;/query&gt;
&lt;query type=&quot;node&quot;&gt;
&lt;bbox-query s=&quot;49.7688&quot; n=&quot;50.1479&quot; e=&quot;22.8337&quot; w=&quot;21.9143&quot;/&gt;
&lt;around radius=&quot;4500&quot;/&gt;
&lt;has-kv k=&quot;place&quot; regv=&quot;city|village|town&quot;/&gt;
&lt;/query&gt;
&lt;print/&gt;</code></pre>
<p>gives you a more inclusive set of results, but I am not sure if it is right or not.</p>
</div>
<div id="comment-41459-info" class="comment-info">
<span class="comment-age">(03 Mar '15, 00:23)</span> <span class="comment-user userinfo">baghaii</span>
</div>
</div>
<span id="41463"></span>
<div id="comment-41463" class="comment">
<div id="post-41463-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I have already managed to write same code myself. Thank you for your response anyway. I still just don't know where is the problem in my previous query</p>
</div>
<div id="comment-41463-info" class="comment-info">
<span class="comment-age">(03 Mar '15, 07:26)</span> <span class="comment-user userinfo">huberttt</span>
</div>
</div>
</div>
<div id="comment-tools-41450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41450-form-container" class="comment-form-container">
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

<span id="41462"></span>

<div id="answer-container-41462" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41462-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-41462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "around" block in each query is relative to the preceding statement. The query block for "town" looks around the "E40". The next query block looks around the results of the "town" query block and so on. One solution would be to use a variable instead, i.e.:</p>
<pre><code>way[int_ref=&quot;E 40&quot;]-&gt;.e40;
( node(49.768,21.914,50.148,22.834)(around.e40:4500)[place=town];
  node(49.768,21.914,50.148,22.834)(around.e40:4500)[place=city];
  node(49.768,21.914,50.148,22.834)(around.e40:4500)[place=village]; );
out;</code></pre>
<p>This is the query you probably intended.</p>
<p>The other, and probably more efficient solution is the one from the comment of baghaii.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '15, 07:14</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-41462" class="comments-container">
&#10;</div>
<div id="comment-tools-41462" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41462-form-container" class="comment-form-container">
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

