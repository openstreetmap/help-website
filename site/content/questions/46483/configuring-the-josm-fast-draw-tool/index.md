+++
type = "question"
title = "Configuring the JOSM fast draw tool"
description = '''I&#x27;m using the fast draw tool to trace islands and ponds but am having a hard time adjusting it. There are parameters one can alter to try to get a useful density of points but they don&#x27;t seem to work. I always get too many points no matter what setting I use for starting Epsilon or Epsilon Multiplie...'''
date = "2015-11-10T03:45:00Z"
lastmod = "2015-11-11T09:52:00Z"
weight = 46483
keywords = [ "tracing", "fast_draw", "tools", "drawing", "josm" ]
aliases = [ "/questions/46483" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Configuring the JOSM fast draw tool](/questions/46483/configuring-the-josm-fast-draw-tool)

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
<span id="post-46483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46483-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using the fast draw tool to trace islands and ponds but am having a hard time adjusting it. There are parameters one can alter to try to get a useful density of points but they don't seem to work. I always get too many points no matter what setting I use for starting Epsilon or Epsilon Multiplier. Even changing the Max points per kilometer has little or no effect that I can see.</p>
<p>If I then chose "autosimplify" the tool removes too many points and I'm left with only a rough approximation of my tracing. If I choose "Save as is" in the fast draw tool and then simplify in JOSM using [shift]-Y that also removes way too many points.</p>
<p>I love the fast draw tool concept but am unable to use it the way I would like. Does anyone have any experience with the tool or suggestions about how to make it perform better?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tracing" rel="tag" title="see questions tagged &#39;tracing&#39;">tracing</span> <span class="post-tag tag-link-fast_draw" rel="tag" title="see questions tagged &#39;fast_draw&#39;">fast_draw</span> <span class="post-tag tag-link-tools" rel="tag" title="see questions tagged &#39;tools&#39;">tools</span> <span class="post-tag tag-link-drawing" rel="tag" title="see questions tagged &#39;drawing&#39;">drawing</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '15, 03:45</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-46483" class="comments-container">
&#10;</div>
<div id="comment-tools-46483" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46483-form-container" class="comment-form-container">
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

<span id="46489"></span>

<div id="answer-container-46489" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46489-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It doesn't seem to be present by default, but it should be possible to make the JOSM simplify less aggressive:</p>
<p><a href="http://josm.openstreetmap.de/wiki/Help/Action/SimplifyWay">http://josm.openstreetmap.de/wiki/Help/Action/SimplifyWay</a></p>
<p>I haven't used the tool; Does the step using the up/down keys not change the number of points? That's how I read this bit of documentation:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/FastDraw#Simplification_detailed_description">https://wiki.openstreetmap.org/wiki/JOSM/Plugins/FastDraw#Simplification_detailed_description</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Nov '15, 12:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-46489" class="comments-container">
<span id="46520"></span>
<div id="comment-46520" class="comment">
<div id="post-46520-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Max,</p>
<p>Thanks for the help. I've been experimenting with changing the controlling parameter in JOSM's Advanced Preferences for Simplify Way and found that lowering <em>simplify-way.max-error</em> from 3.0 to 1.0 helps.</p>
<p>As for the fastdraw tool, there are so many fastdraw parameters in Advanced Preferences that fiddling with them will take quite a bit of time. The documentation is not very well written so it's only a rough guide to tuning it.</p>
<p>I came across another tool called Simplify Area that is supposedly able to do the same thing as Simplify Line but has more tuning parameters. Unfortunately the brief descriptive notes don't tell you how to go about doing that.</p>
<p>Here are the Simplify Area parameters and their default values:</p>
<p>simplify-area.angle.factor=1.0</p>
<p>simplify-area.angle.threshold=10.0</p>
<p>simplify-area.area.factor=1.0</p>
<p>simplify-area.area.threshold=5.0</p>
<p>simplify-area.dist.factor=3.0</p>
<p>simplify-area.dist.threshold=3.0</p>
<p>simplify-area.merge.threshold=0.2</p>
<p>I will try various settings and report back here if I can figure out how to use that tool.</p>
</div>
<div id="comment-46520-info" class="comment-info">
<span class="comment-age">(11 Nov '15, 00:51)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="46526"></span>
<div id="comment-46526" class="comment">
<div id="post-46526-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>And then after reading the Fastdraw Simplification_detailed_description again and doing some experimenting, I found that the arrow keys do work as stated if you apply them <em>after pressing Enter but before deselecting</em> the way. Pressing up-arrow repeatedly restores points discarded during the simplification in stages. The down arrow reverses the effect.</p>
</div>
<div id="comment-46526-info" class="comment-info">
<span class="comment-age">(11 Nov '15, 09:52)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-46489" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46489-form-container" class="comment-form-container">
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

