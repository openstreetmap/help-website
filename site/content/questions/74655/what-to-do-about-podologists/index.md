+++
type = "question"
title = "What to do about podologists?"
description = '''I currently want to add a podologist, and I have no idea which tags to use. After some Research, I am not even sure that this term is clearly delineated from a podiatrist, some info is here - it seems that a podiatrist performs surgery while a podologist doesn&#x27;t, so I don&#x27;t know if it&#x27;s appropriate ...'''
date = "2020-05-07T14:05:00Z"
lastmod = "2020-05-11T07:59:00Z"
weight = 74655
keywords = [ "doctor", "key", "healthcare" ]
aliases = [ "/questions/74655" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What to do about podologists?](/questions/74655/what-to-do-about-podologists)

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
<span id="post-74655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74655-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I currently want to add a podologist, and I have no idea which tags to use.<br />
After some Research, I am not even sure that this term is clearly delineated from a podiatrist, some info is <a href="https://pedimanie.com/who-is-a-podologist-what-does-a-foot-doctor-do/">here</a> - it seems that a podiatrist performs surgery while a podologist doesn't, so I don't know if it's appropriate to put a podologist under healthcare=podiatrist.</p>
<p>Here are a few variants I have seen:</p>
<ul>
<li>There is <a href="https://wiki.openstreetmap.org/wiki/Item:Q17925">office=podologist</a> which is used quite frequently but tends to be combined with other things such as shop=medical (<a href="https://www.openstreetmap.org/node/1829749624">example</a>) - quite often these nodes also have <a href="https://www.openstreetmap.org/node/4528379933">no</a> <a href="https://www.openstreetmap.org/node/5394595270">healthcare</a> <a href="https://www.openstreetmap.org/node/5433765343">tag</a> <a href="https://www.openstreetmap.org/node/4350845368">at</a> <a href="https://www.openstreetmap.org/node/4691427132">all</a>.</li>
<li>For <em>healthcare:specialty</em>, there is podiatry, podiatrist and podologist - which makes me wonder which one should be used - I doubt it makes sense to have all three in use</li>
<li>For <em>healthcare</em>, usually podiatrist is used, but I have sometimes seen doctor as well</li>
<li><a href="https://www.openstreetmap.org/node/6471083973">This</a> is the only node in the world with healthcare=podologist</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-doctor" rel="tag" title="see questions tagged &#39;doctor&#39;">doctor</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span> <span class="post-tag tag-link-healthcare" rel="tag" title="see questions tagged &#39;healthcare&#39;">healthcare</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 May '20, 14:05</strong></p>
<img src="https://secure.gravatar.com/avatar/09f491ff872d3ed578d7e246d1bf30cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xerusf&#39;s gravatar image" />
<p><span>xerusf</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xerusf has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-74655" class="comments-container">
&#10;</div>
<div id="comment-tools-74655" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74655-form-container" class="comment-form-container">
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

<span id="74726"></span>

<div id="answer-container-74726" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74726-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-74726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="xerusf has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>AFAIK the main difference is between (medical) doctors that practice podiatry as a speciality and other foot-related healthcare occupations (for example creating medical shoe inlays). The wiki would seem to support this view so</p>
<p>amenity=doctors, healthcare=doctor, healthcare:speciality=podiatry for medical doctors</p>
<p>healthcare=podiatrist for none-medical doctors, potentially with other tags if associated with a shop or similar.</p>
<p>The added complication seems to be that in some regions of the world the lines are not drawn so clearly.</p>
<p>The healthcare tagging is "relatively" recent so you are bound to find old and not differentiated tagging.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '20, 07:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-74726" class="comments-container">
&#10;</div>
<div id="comment-tools-74726" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74726-form-container" class="comment-form-container">
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

