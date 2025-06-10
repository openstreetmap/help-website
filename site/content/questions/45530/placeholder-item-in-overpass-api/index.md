+++
type = "question"
title = "Placeholder item in overpass API"
description = '''Say I have a simple query that may or may not give a result. (and only one result, say with out 1) It runs fast, so I bundle them together into a single query. But the problem is that sometimes it will not return a result, so is there a simple solution to this? It would be easy if I there was a plac...'''
date = "2015-09-23T19:34:00Z"
lastmod = "2015-09-23T20:16:00Z"
weight = 45530
keywords = [ "overpass", "placeholder" ]
aliases = [ "/questions/45530" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Placeholder item in overpass API](/questions/45530/placeholder-item-in-overpass-api)

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
<span id="post-45530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45530-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Say I have a simple query that may or may not give a result. (and only one result, say with <code>out 1</code>) It runs fast, so I bundle them together into a single query. But the problem is that sometimes it will not return a result, so is there a simple solution to this? It would be easy if I there was a placeholder item in OSM, like this:</p>
<pre><code>query goes here
way(0);</code></pre>
<p>So that when processing the output, you could detect the placeholder.</p>
<p>Is there any nice way to do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-placeholder" rel="tag" title="see questions tagged &#39;placeholder&#39;">placeholder</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '15, 19:34</strong></p>
<img src="https://secure.gravatar.com/avatar/887e8dcd0dc913a9516e6ad0f5ab5a56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CrazyDave2345&#39;s gravatar image" />
<p><span>CrazyDave2345</span><br />
<span class="score" title="55 reputation points">55</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CrazyDave2345 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45530" class="comments-container">
&#10;</div>
<div id="comment-tools-45530" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45530-form-container" class="comment-form-container">
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

<span id="45531"></span>

<div id="answer-container-45531" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45531-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-45531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="CrazyDave2345 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all, a quick and dirty approach similar to your post.</p>
<pre><code>node(1);out ids;</code></pre>
<p>This will add a one liner to your query result, regardless of whether there was some result or not.</p>
<pre><code>  &lt;node id=&quot;1&quot;/&gt;</code></pre>
<p>It shouldn't add too much overhead, after all.</p>
<p>There's one potential issue with that approach, though: if some mapper happens to delete that node #1, your marker is gone and you'll have to find some other available node. Of course, your normal query result also shouldn't produce a result, which looks like the marker, otherwise you cannot tell the both of them apart any longer.</p>
<p>The <strong>recommended approach</strong> involves the use of <code>out count;</code>. In the following example, we will first print all the buildings in the current bbox, followed by a total count:</p>
<pre><code>[bbox:{{bbox}}];
way[building];
out geom;
out count;</code></pre>
<p>Assuming there are no buildings in your bbox, you will still get the following summary information:</p>
<pre><code>  &lt;count total=&quot;0&quot; nodes=&quot;0&quot; ways=&quot;0&quot; relations=&quot;0&quot; areas=&quot;0&quot;/&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '15, 19:56</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Sep '15, 20:09</strong> </span></p>
</div>
</div>
<div id="comments-container-45531" class="comments-container">
<span id="45533"></span>
<div id="comment-45533" class="comment">
<div id="post-45533-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Number two worked for me, thanks!</p>
</div>
<div id="comment-45533-info" class="comment-info">
<span class="comment-age">(23 Sep '15, 20:16)</span> <span class="comment-user userinfo">CrazyDave2345</span>
</div>
</div>
</div>
<div id="comment-tools-45531" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45531-form-container" class="comment-form-container">
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

