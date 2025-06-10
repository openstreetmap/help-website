+++
type = "question"
title = "[closed] What is different about these intersections/off-ramps?"
description = '''I am writing software that is trying to find off ramps along the highways. To do this I find ways with a highway value of motorway_link or secondary. I then go through all of the motorway_link ways and see if any of the nd ref=&quot;XXXX&quot; are in common with the secondary ways. This works pretty well, but...'''
date = "2013-09-25T14:28:00Z"
lastmod = "2013-09-25T15:43:00Z"
weight = 26722
keywords = [ "off-ramp", "intersections", "motorway_link" ]
aliases = [ "/questions/26722" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] What is different about these intersections/off-ramps?](/questions/26722/what-is-different-about-these-intersectionsoff-ramps)

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
<span id="post-26722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26722-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am writing software that is trying to find off ramps along the highways. To do this I find ways with a highway value of <code>motorway_link</code> or <code>secondary</code>. I then go through all of the <code>motorway_link</code> ways and see if any of the <code>nd ref="XXXX"</code> are in common with the <code>secondary</code> ways.</p>
<p>This works pretty well, but it doesn't seem to work for all intersections/off-ramps. Here are two examples that don't work:</p>
<ol>
<li><a href="http://www.openstreetmap.org/#map=17/43.42071/-80.28191">http://www.openstreetmap.org/#map=17/43.42071/-80.28191</a></li>
<li><a href="http://www.openstreetmap.org/#map=17/43.44879/-80.17669">http://www.openstreetmap.org/#map=17/43.44879/-80.17669</a></li>
</ol>
<p>And here are two examples that do:</p>
<ol>
<li><a href="http://www.openstreetmap.org/#map=17/43.45355/-80.12442">http://www.openstreetmap.org/#map=17/43.45355/-80.12442</a></li>
<li><a href="http://www.openstreetmap.org/#map=17/43.49124/-79.98727">http://www.openstreetmap.org/#map=17/43.49124/-79.98727</a></li>
</ol>
<p>Can some one explain why the two I listed don't work? Any tricks or steps I need to add to my algorithm to make them work?</p>
<p>EDIT: Here is a HTML file (that uses google maps) that shows all the intersections that I detect: <a href="http://pastie.org/private/wnakelvwdkndpgeafwdg">http://pastie.org/private/wnakelvwdkndpgeafwdg</a></p>
<p>As you can see my algorithm does well, but not not as well as i would like.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-off-ramp" rel="tag" title="see questions tagged &#39;off-ramp&#39;">off-ramp</span> <span class="post-tag tag-link-intersections" rel="tag" title="see questions tagged &#39;intersections&#39;">intersections</span> <span class="post-tag tag-link-motorway_link" rel="tag" title="see questions tagged &#39;motorway_link&#39;">motorway_link</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Sep '13, 14:28</strong></p>
<img src="https://secure.gravatar.com/avatar/1106878994248cf2f1feb27a3f7efc7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pag11123&#39;s gravatar image" />
<p><span>pag11123</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pag11123 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>25 Sep '13, 15:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span></p>
</div>
</div>
<div id="comments-container-26722" class="comments-container">
<span id="26725"></span>
<div id="comment-26725" class="comment">
<div id="post-26725-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your examples seem to be correct in OSM. Maybe you should check again your code. Or publish it for peer review. Perhaps the problem is that some of the intersections are on a first or last node on the way...</p>
</div>
<div id="comment-26725-info" class="comment-info">
<span class="comment-age">(25 Sep '13, 15:30)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-26722" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26722-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Other" by Pieren 25 Sep '13, 15:45

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26726"></span>

<div id="answer-container-26726" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26726-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found the problem, I was ignoring ways without a name.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '13, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/1106878994248cf2f1feb27a3f7efc7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pag11123&#39;s gravatar image" />
<p><span>pag11123</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pag11123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26726" class="comments-container">
&#10;</div>
<div id="comment-tools-26726" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26726-form-container" class="comment-form-container">
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

