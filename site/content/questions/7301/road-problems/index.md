+++
type = "question"
title = "road problems"
description = '''I&#x27;m having problems with traffic island grass verges at the side of the road and barriers at the side of the road; can someone tell me how to do these?'''
date = "2011-08-25T13:18:00Z"
lastmod = "2011-08-25T22:13:00Z"
weight = 7301
keywords = [ "traffic", "road" ]
aliases = [ "/questions/7301" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [road problems](/questions/7301/road-problems)

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
<span id="post-7301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7301-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm having problems with traffic island grass verges at the side of the road and barriers at the side of the road; can someone tell me how to do these?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Aug '11, 13:18</strong></p>
<img src="https://secure.gravatar.com/avatar/7264e11bcea28695deb701b17fdbf7b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="darrenrobert&#39;s gravatar image" />
<p><span>darrenrobert</span><br />
<span class="score" title="73 reputation points">73</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="darrenrobert has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Aug '11, 21:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-7301" class="comments-container">
&#10;</div>
<div id="comment-tools-7301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7301-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="7323"></span>

<div id="answer-container-7323" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7323-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For something as small as a patch of grass at the side of a road I don't think that "village_green" is a good answer, because, well, it's not a village green is it?</p>
<p>A few months back "<a href="https://wiki.openstreetmap.org/wiki/Proposed_features/landcover">landcover</a>" was suggested (as an alternative to landuse, so that you could have landuse=foo, landcover=bar. It's a nice idea, but <a href="http://taginfo.openstreetmap.org/tags/landcover=grass#wiki">almost no-one uses landcover=grass</a>.</p>
<p>However, <a href="http://taginfo.openstreetmap.org/tags/surface=grass#wiki">surface=grass</a> probably also works in your case and is much more popular.</p>
<p>For larger grassy items, you might consider <a href="https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dvillage_green">landuse=village_green</a>, <a href="https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dpark">leisure=park</a> or <a href="https://wiki.openstreetmap.org/wiki/Tag:landuse%3Drecreation_ground">landuse=recreation_ground</a> - choose the thing that's most appropriate (or if none of them are, use something else).</p>
<p>One thing that I wouldn't worry about at this stage is how e.g. a grass verge renders in the main Mapnik map - rightly, I don't think that it is concerned with features that small, even at maximum current zoom.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '11, 22:13</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-7323" class="comments-container">
&#10;</div>
<div id="comment-tools-7323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7323-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7302"></span>

<div id="answer-container-7302" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7302-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-7302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For small pieces of city vegetation (too small to be a park, eg. your grass verges) I use <a href="https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dvillage_green">village green</a> even if it is probably not what it is meant for, but it is the closest one. Grass alone suggests that it is grass, not a place covered also with trees and bushes.<br />
</p>
<p>For barriers at side of the road use some of <a href="https://wiki.openstreetmap.org/wiki/Key:barrier">these</a> depending on what kind of barrier there is.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '11, 13:56</strong></p>
<img src="https://secure.gravatar.com/avatar/15c1efc9ebb466f69907a3e85693e739?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LM_1&#39;s gravatar image" />
<p><span>LM_1</span><br />
<span class="score" title="3287 reputation points"><span>3.3k</span></span><span title="33 badges"><span class="badge1">●</span><span class="badgecount">33</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LM_1 has 7 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-7302" class="comments-container">
<span id="7321"></span>
<div id="comment-7321" class="comment">
<div id="post-7321-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It is fine that some do not like this answer, but those who vote it down should give their own (better) answer or at least leave a comment stating what is wrong...</p>
</div>
<div id="comment-7321-info" class="comment-info">
<span class="comment-age">(25 Aug '11, 20:21)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
<span id="7322"></span>
<div id="comment-7322" class="comment">
<div id="post-7322-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>From the wiki, a village green is defined as "An area of common land (usually grass but may also be a lake), in the centre of a village". This clearly does not apply to patches of grass at the side of a road.</p>
<p>It would be more useful to tag it as landuse=grass (if it is mostly grass) or perhaps landuse=meadow (if there are some wildflowers), or natural=scrub or natural=heath (if there are some bushes).</p>
</div>
<div id="comment-7322-info" class="comment-info">
<span class="comment-age">(25 Aug '11, 21:24)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
</div>
<div id="comment-tools-7302" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7302-form-container" class="comment-form-container">
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

