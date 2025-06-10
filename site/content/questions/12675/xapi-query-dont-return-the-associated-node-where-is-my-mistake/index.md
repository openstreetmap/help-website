+++
type = "question"
title = "xapi query don&#x27;t return the associated node =&gt; where is my mistake"
description = '''Hi, I have sent this query to get relations. The server response give me the relations but not the nodes used in this relation. My query is : http://overpass.osm.rambler.ru/cgi/xapi?relation[type=enforcement][bbox=-5.9,42.3,9,51] I want with the relations, the node associated with this relations, no...'''
date = "2012-05-12T08:16:00Z"
lastmod = "2012-05-12T11:46:00Z"
weight = 12675
keywords = [ "query", "xapi" ]
aliases = [ "/questions/12675" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [xapi query don't return the associated node =\> where is my mistake](/questions/12675/xapi-query-dont-return-the-associated-node-where-is-my-mistake)

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
<span id="post-12675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12675-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have sent this query to get relations. The server response give me the relations but not the nodes used in this relation.</p>
<p>My query is : <a href="http://overpass.osm.rambler.ru/cgi/xapi?relation%5Btype=enforcement%5D%5Bbbox=-5.9,42.3,9,51%5D">http://overpass.osm.rambler.ru/cgi/xapi?relation[type=enforcement][bbox=-5.9,42.3,9,51]</a></p>
<p>I want with the relations, the node associated with this relations, not all the node !</p>
<p>what can I add to my query as to have the nodes description ? Where is my mistake ?</p>
<p>Best Regards Michel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '12, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/7c0dfb4787be9ac82896240f6119033e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="michel60&#39;s gravatar image" />
<p><span>michel60</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="michel60 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12675" class="comments-container">
<span id="12676"></span>
<div id="comment-12676" class="comment">
<div id="post-12676-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not really clear what you want, maybe you can ask the question in your own language.</p>
<p>I believe the response I got from that was relevant to the query. (All relations within bbox of type enforcement). I got the nodes related to the relations.</p>
</div>
<div id="comment-12676-info" class="comment-info">
<span class="comment-age">(12 May '12, 09:18)</span> <span class="comment-user userinfo">TheOddOne2</span>
</div>
</div>
</div>
<div id="comment-tools-12675" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12675-form-container" class="comment-form-container">
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

<span id="12682"></span>

<div id="answer-container-12682" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12682-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-12682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To get the relations only, the query</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/xapi?relation[type=enforcement][bbox=-5.9,42.3,9,51]</code></pre>
<p>is fine. If you want something else, you should use Overpass QL to formulate what you want exactly.</p>
<p>Relations only (again):</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=rel[type=enforcement](42.3,-5.9,51,9);out;</code></pre>
<p>Relations and only nodes that are members:</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=(rel[type=enforcement](42.3,-5.9,51,9);node(r););out;</code></pre>
<p>Relations and the node and way members and the nodes belonging to the way members</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=(rel[type=enforcement](42.3,-5.9,51,9);&gt;;);out;</code></pre>
<p>Or if you want to process the data with JOSM or Osmosis, you need meta data. Replace <code>out;</code> by <code>out meta;</code></p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=(rel[type=enforcement](42.3,-5.9,51,9);&gt;;);out meta;</code></pre>
<p>In case your browser has difficulties with spaces in URL:</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=(rel[type=enforcement](42.3,-5.9,51,9);&gt;;);out+meta;</code></pre>
<p>Caution: these queries may take some minutes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '12, 11:46</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-12682" class="comments-container">
&#10;</div>
<div id="comment-tools-12682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12682-form-container" class="comment-form-container">
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

