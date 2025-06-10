+++
type = "question"
title = "How to tag pedestrian area over a road (or something else)?"
description = '''(I found an old question &quot;How do I tag a skywalk / skyway / sky bridge?&quot; but I could not find the solution.) I tried to map a pedestrian deck (aka pedway) with &quot;area=yes&quot; over something like a road. But it appears at the bottom even with &quot;bridge=yes&quot; and &quot;layer=1&quot; tags. For example, see a pedestrian...'''
date = "2020-07-16T08:58:00Z"
lastmod = "2020-07-17T12:37:00Z"
weight = 75743
keywords = [ "pedestrian" ]
aliases = [ "/questions/75743" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag pedestrian area over a road (or something else)?](/questions/75743/how-to-tag-pedestrian-area-over-a-road-or-something-else)

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
<span id="post-75743-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75743-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75743-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>(I found an old question <a href="https://help.openstreetmap.org/questions/1623/how-do-i-tag-a-skywalk-skyway-sky-bridge">"How do I tag a skywalk / skyway / sky bridge?"</a> but I could not find the solution.)</p>
<p>I tried to map a pedestrian deck (aka pedway) with "area=yes" over something like a road. But it appears at the bottom even with "bridge=yes" and "layer=1" tags.</p>
<p>For example, see <a href="https://www.openstreetmap.org/way/541875201">a pedestrian deck crossing over railways</a>. You see railways and a service road are crossing over the deck, not under it. (This deck does not have "bridge" tag but in my conclusion it does not matter.) You may also notice some underlying railways are tagged with "tunnel=yes" to avoid this behavior, but I am not sure it is the correct way. The another deck without "area" tag is correctly drawn over a road that is about 150m west of this deck (an extention of the same footway).</p>
<p>Another example, <a href="http://www.openstreetmap.org/browse/way/62333303">"Bridge of Sighs", Oxford</a> has similar structure that I wanted to draw, but it is also shown under New College Lane. I expected it to be drawn over the lane. (I know "pedestrian" tag is not used there.)</p>
<p>How do you tag such a structure correctly? Or is this a rendering problem of standard map?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '20, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/884dcae8cae9508f220e2faec70b33e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="geohachi&#39;s gravatar image" />
<p><span>geohachi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="geohachi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75743" class="comments-container">
<span id="75746"></span>
<div id="comment-75746" class="comment">
<div id="post-75746-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd like to remind people to not let iD's "pedestrian area" preset confuse you. <code>highway=pedestrian</code> means it is a pedestrian street that vehicles can physically travel on (but usually legally forbidden). <code>area=yes</code> means vehicles can travel in all directions (think of a wide open square). These should be considered from at least <code>area:highway=pedestrian</code> (meaning it's linear); and since there are stairs and many narrowing obstacles here it may be better to be a <code>highway=footway</code> + <code>area=yes</code>, if not <code>area:highway=footway</code>.</p>
</div>
<div id="comment-75746-info" class="comment-info">
<span class="comment-age">(16 Jul '20, 11:16)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-75743" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75743-form-container" class="comment-form-container">
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

<span id="75760"></span>

<div id="answer-container-75760" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75760-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as I know, the standard map style always renders linear roads/railways above areas. This is not indicative of an error in the data.</p>
<p>The crossing features should be at different layers, and generally, you should either tag the upper feature(s) as a bridge or the lower feature(s) as a tunnel, depending on what matches the situation on the ground. There are some particular features that have more intricate solutions for modelling them (such as buildings, where you could use the tags from Simple 3D Buildings).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '20, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-75760" class="comments-container">
&#10;</div>
<div id="comment-tools-75760" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75760-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75759"></span>

<div id="answer-container-75759" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75759-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, "The layer=* tag is one of several methods used to describe vertical relationships between crossing or overlapping features." Please see <a href="https://wiki.openstreetmap.org/wiki/Key:layer">https://wiki.openstreetmap.org/wiki/Key:layer</a></p>
<p>In the two cases you describe the tag layer=1 is used to show that that feature is above the features it crosses over. The lower features (in the absence of any layer tag) are implied as layer=0, ("Features at layer 0 should not normally have a layer tag.")</p>
<p>The layer tag describes the relationship of crossing features both above and below 0 by positive or negative numbering.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '20, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-75759" class="comments-container">
<span id="75761"></span>
<div id="comment-75761" class="comment">
<div id="post-75761-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think I understand how "layer" works. So you would probably agree the data (tag) are correct. But the rendering is not expected. So my question came up. Thank you.</p>
</div>
<div id="comment-75761-info" class="comment-info">
<span class="comment-age">(17 Jul '20, 12:37)</span> <span class="comment-user userinfo">geohachi</span>
</div>
</div>
</div>
<div id="comment-tools-75759" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75759-form-container" class="comment-form-container">
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

