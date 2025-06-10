+++
type = "question"
title = "osmfilter misses dependent nodes"
description = '''I&#x27;m using osmfilter to extract all ferries from a planet file circa 2nd March 2015. Here is the command I&#x27;m executing: osmfilter planet-latest.o5m --keep=&quot;route=ferry&quot; -o=ferries.o5m  All the relations and dependent ways seem to be in the extract as expected, however very few nodes make it into the ...'''
date = "2015-03-25T01:24:00Z"
lastmod = "2015-03-25T17:44:00Z"
weight = 41897
keywords = [ "osmfilter" ]
aliases = [ "/questions/41897" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [osmfilter misses dependent nodes](/questions/41897/osmfilter-misses-dependent-nodes)

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
<span id="post-41897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41897-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using osmfilter to extract all ferries from a planet file circa 2nd March 2015. Here is the command I'm executing:</p>
<pre><code>osmfilter planet-latest.o5m --keep=&quot;route=ferry&quot; -o=ferries.o5m</code></pre>
<p>All the relations and dependent ways seem to be in the extract as expected, however very few nodes make it into the file. My understanding of osmfilter from the wiki is that it includes all dependent objects (eg. nodes in ways). What am I doing wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Mar '15, 01:24</strong></p>
<img src="https://secure.gravatar.com/avatar/5e708d75f6903e41161294dcc8c2f544?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="milesizzo&#39;s gravatar image" />
<p><span>milesizzo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="milesizzo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41897" class="comments-container">
&#10;</div>
<div id="comment-tools-41897" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41897-form-container" class="comment-form-container">
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

<span id="41919"></span>

<div id="answer-container-41919" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41919-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Indeed your result should contain all relations, their ways and their nodes, because there is the switch "-ignore-dependencies" to drop all child objects like nodes of a way or ways of a relation.</p>
<p>Please try other filter commands on smaller source files with different map objects, just to see whether osmfilter can bring the result in general you want.</p>
<p>If you have succes with smaller data about other ways or map objects, we can track down why this does not work with your ferry routes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Mar '15, 17:44</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-41919" class="comments-container">
&#10;</div>
<div id="comment-tools-41919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41919-form-container" class="comment-form-container">
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

