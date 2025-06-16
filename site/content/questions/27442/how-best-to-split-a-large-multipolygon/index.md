+++
type = "question"
title = "How best to split a large multipolygon"
description = '''I&#x27;m mapping in northern Thailand and have come across this problem frequently as of late. Back before there was high resolution imagery available for this region many OSM mappers drew large contiguous blocks of forest using only very low-res imagery as a guide. They created them as multipolygons to ...'''
date = "2013-10-23T15:21:00Z"
lastmod = "2020-01-25T10:41:00Z"
weight = 27442
keywords = [ "splitting", "relations", "multipolygon" ]
aliases = [ "/questions/27442" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How best to split a large multipolygon](/questions/27442/how-best-to-split-a-large-multipolygon)

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
<span id="post-27442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27442-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm mapping in northern Thailand and have come across this problem frequently as of late. Back before there was high resolution imagery available for this region many OSM mappers drew large contiguous blocks of forest using only very low-res imagery as a guide. They created them as multipolygons to allow for the eventual addition of unwooded areas.</p>
<p>Now, there is high quality aerial photography that reveals the truth of the situation -- the wooded areas are anything but contiguous. The multipolygons often need to be drastically altered or redrawn to allow for river valleys, cities, and areas of intense agriculture that are not wooded and were previously not discernible. The particular case I'm asking about can be seen in the link below. I want to split the section of wood situated just north of the Kok River off the big multipolygon but am unsure how to proceed.</p>
<p><a href="https://www.openstreetmap.org/#map=14/20.0538/99.5079&amp;layers=N">https://www.openstreetmap.org/#map=14/20.0538/99.5079&amp;layers=N</a></p>
<p>The white area is already an inner polygon, Way: 187645495, while the most outer one is AFAIK, Relation 1,999,865, a monster multipolygon that covers a huge area. I'm unsure how to proceed because I want the wooded area to remain as such but I would like to show that it is, in reality, an isolated wooded area north of the river.</p>
<p>I have mucked about with these things before and after suffering through having to hand fix dozens of conflicts, I'm a bit gun shy.</p>
<p>Thanks for your help...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-splitting" rel="tag" title="see questions tagged &#39;splitting&#39;">splitting</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '13, 15:21</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-27442" class="comments-container">
&#10;</div>
<div id="comment-tools-27442" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27442-form-container" class="comment-form-container">
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

<span id="72672"></span>

<div id="answer-container-72672" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72672-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a <a href="https://wiki.openstreetmap.org/wiki/PolygonCutOut">JOSM plugin PolygonCutOut</a> for splitting multipolygons. See also <a href="https://josm.openstreetmap.de/ticket/18295#comment:18">https://josm.openstreetmap.de/ticket/18295#comment:18</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jan '20, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c03139d4c6dce4328bd61a316e897f7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pangoSE&#39;s gravatar image" />
<p><span>pangoSE</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pangoSE has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jan '20, 10:41</strong> </span></p>
</div>
</div>
<div id="comments-container-72672" class="comments-container">
&#10;</div>
<div id="comment-tools-72672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72672-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27445"></span>

<div id="answer-container-27445" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27445-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a big judgment call on your part, in particular on how much time and energy you want to invest. In general, it seems like that giant multipolygon needs to get broken up sooner or later, and continue to get broken up as detail is added.</p>
<p>What I would probably do is to split the outer way, and the big inner way, for example into upper and lower parts. Then you could connect the upper part of the outer way with the upper part of the inner way, and the lower part of the outer way with the lower part of the inner way. Then you can create new relations for the upper and lower ways as necessary, or just merge them and get rid of the multipolygon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '13, 16:31</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-27445" class="comments-container">
<span id="27459"></span>
<div id="comment-27459" class="comment">
<div id="post-27459-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, I do have time to invest in doing what you suggest but let me ask one further question before I begin. Should I be able to "see" the entire outer multipolygon before attempting the split, that is, should I have the entire thing in my browser window?</p>
<p>I need to learn how to do this as a general case because, as I pointed out, there are many more of these giants in need of taming.</p>
</div>
<div id="comment-27459-info" class="comment-info">
<span class="comment-age">(24 Oct '13, 04:40)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="27476"></span>
<div id="comment-27476" class="comment">
<div id="post-27476-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You don't need to see the whole thing. What you'd need to do, though, is to make sure your ways are closed. If you merge them into a single way, the editor might have cues. For ex in P2, the directional line in the toolbox becomes two circular arrows, I think there's more advanced checks in JOSM. There are also QA tools that can help with that sort of thing, like the Multipolygon check in OSM Inspector (<a href="http://tinyurl.com/lm7ctoh)">http://tinyurl.com/lm7ctoh)</a> but that refreshes daily at best. A broken multipolygon (ie with a gap) often will not render, so that's another clue something's amiss.</p>
</div>
<div id="comment-27476-info" class="comment-info">
<span class="comment-age">(24 Oct '13, 19:21)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="27480"></span>
<div id="comment-27480" class="comment">
<div id="post-27480-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wrote something about adding detail to large multipolygons without losing its history <a href="http://addictedtoosm.wordpress.com/2013/10/17/suavizacao-de-tracados-sem-perda-de-historico/">here</a> (in Portuguese!). Please tell me if it is inappropriate to post this kind of link here (and I'll delete the comment...) - too little time to translate into english and post the images.</p>
</div>
<div id="comment-27480-info" class="comment-info">
<span class="comment-age">(24 Oct '13, 20:07)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
</div>
<div id="comment-tools-27445" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27445-form-container" class="comment-form-container">
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

