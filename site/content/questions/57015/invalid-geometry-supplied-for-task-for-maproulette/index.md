+++
type = "question"
title = "&quot;Invalid geometry supplied for task&quot; for Maproulette"
description = '''I use this Overpass query to create a Maproulette challenge:  [timeout:50]; (  node[shop](area:3600114938); ); out body geom qt;  It outputs valid nodes and in the &quot;tasks&quot;-section of my challenge, in the table I see lots of entries like this ID Priority Name ... Location Status Actions 2418504 High ...'''
date = "2017-07-11T18:01:00Z"
lastmod = "2017-07-12T14:37:00Z"
weight = 57015
keywords = [ "maproulette", "overpass" ]
aliases = [ "/questions/57015" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["Invalid geometry supplied for task" for Maproulette](/questions/57015/invalid-geometry-supplied-for-task-for-maproulette)

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
<span id="post-57015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57015-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I use <a href="http://overpass-turbo.eu/s/qko">this</a> Overpass query to create a Maproulette challenge:</p>
<pre><code>[timeout:50];
(
    node[shop](area:3600114938);
);
out body geom qt;</code></pre>
<p>It outputs valid nodes and in the "tasks"-section of my challenge, in the table I see lots of entries like this</p>
<pre><code>ID     Priority Name    ...     Location                             Status Actions
2418504 High    360298302       Some({&quot;type&quot;:&quot;Point&quot;,&quot;coordinates&quot;:[5.3182887,60.3855342]}) Created</code></pre>
<p>But when I view the task I get this red errorbox with the error</p>
<pre><code> KO : ColumnName(.location,Some(location))</code></pre>
<p>or</p>
<pre><code>Invalid geometry supplied for task.</code></pre>
<p>depending on where I "view" it from.</p>
<p>Any idea why these geometries are invalid? What do I have to do to get this working?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maproulette" rel="tag" title="see questions tagged &#39;maproulette&#39;">maproulette</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '17, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-57015" class="comments-container">
&#10;</div>
<div id="comment-tools-57015" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57015-form-container" class="comment-form-container">
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

<span id="57021"></span>

<div id="answer-container-57021" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57021-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hey! MapRoulette maintainer here. Did you wait for your challenge to complete building? Its status will change to 'complete' in your challenge list. I can't think of another issue right away, I actually tried a similar (test) challenge for my area just now and it works fine:</p>
<pre><code>node[shop](area:3600198770);
out body geom qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '17, 20:43</strong></p>
<img src="https://secure.gravatar.com/avatar/acea3c9fd5908d7ff09596d16b8724d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mvexel&#39;s gravatar image" />
<p><span>mvexel</span><br />
<span class="score" title="762 reputation points">762</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mvexel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57021" class="comments-container">
<span id="57035"></span>
<div id="comment-57035" class="comment">
<div id="post-57035-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Very strange. I waited until the status showed "complete" and I tried rebuilding. This is the task if you somehow have access to it <a href="http://maproulette.org/ui/admin/list/1023/Challenge/tasks/2653">http://maproulette.org/ui/admin/list/1023/Challenge/tasks/2653</a> or this to view the tasks <a href="http://maproulette.org/view/2653">http://maproulette.org/view/2653</a></p>
</div>
<div id="comment-57035-info" class="comment-info">
<span class="comment-age">(12 Jul '17, 14:37)</span> <span class="comment-user userinfo">FredrikLindseth</span>
</div>
</div>
</div>
<div id="comment-tools-57021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57021-form-container" class="comment-form-container">
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

