+++
type = "question"
title = "How do I map a building with &quot;holes&quot; and parts?"
description = '''So, I want to map a building which has an inner courtyard, and parts, which have different properties. I made a relation which has type=multipolygon and building=hospital (because it&#x27;s a hospital building). Now, the outer line has no tags, and is in the relation as outer. The courtyard, also has no ...'''
date = "2017-11-14T06:29:00Z"
lastmod = "2017-11-15T15:48:00Z"
weight = 60603
keywords = [ "building", "part", "relations", "multipolygon" ]
aliases = [ "/questions/60603" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I map a building with "holes" and parts?](/questions/60603/how-do-i-map-a-building-with-holes-and-parts)

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
<span id="post-60603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60603-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-60603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So, I want to map a building which has an inner courtyard, and parts, which have different properties.</p>
<p>I made a relation which has <code>type=multipolygon</code> and <code>building=hospital</code> (because it's a hospital building).</p>
<p>Now, the outer line has no tags, and is in the relation as <code>outer</code>. The courtyard, also has no tags, and is in the relation as <code>inner</code>. So far so good.</p>
<p>The part of the building with different properties, touches the outer ring on some sections. It has a couple tags, like <code>building:levels=2</code>, and <code>roof:shape=gabled</code>, etc.</p>
<p>It is in the relation as <code>part</code>, but now I'm getting an error in JOSM:</p>
<blockquote>
<p>Multipolygon outer way shares segment(s) with other ring (1)</p>
</blockquote>
<p>So I know how to make buildings made up of several parts, and I also know how to make buildings with pateos, and other "holes", etc. But combining the two seems a bit like an impossibility, because for a building with holes, the relation is a <code>type=multipolygon</code>, and <code>type=building</code> if it's a building that consists of several parts.</p>
<p>So how do I go about this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-part" rel="tag" title="see questions tagged &#39;part&#39;">part</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '17, 06:29</strong></p>
<img src="https://secure.gravatar.com/avatar/fb7188d8be002ece64870dffe9ec6fa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="polemon&#39;s gravatar image" />
<p><span>polemon</span><br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="polemon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60603" class="comments-container">
<span id="60604"></span>
<div id="comment-60604" class="comment">
<div id="post-60604-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>what if you do not add building:parts to the multipolygon ? Would that be wrong ?</p>
</div>
<div id="comment-60604-info" class="comment-info">
<span class="comment-age">(14 Nov '17, 06:38)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="60606"></span>
<div id="comment-60606" class="comment">
<div id="post-60606-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was once stuck on something similar and for adding to the building relation I used the "outer" (yes it has no tag) of the multipolygon. I don't know if I did it correctly but everything renders well.</p>
</div>
<div id="comment-60606-info" class="comment-info">
<span class="comment-age">(14 Nov '17, 08:46)</span> <span class="comment-user userinfo">Privatemajory</span>
</div>
</div>
<span id="60623"></span>
<div id="comment-60623" class="comment">
<div id="post-60623-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a> that'exactly how I left things right now. As for whether that's correct or not: I have no idea. I'd imagine the <code>building:part</code> object should be also part of the relation, but I really don't know. It seems to work wouth having the building part added to the relation. It's just that I've seen it being part of the relation in other buildings, hence I thought that's the correct way of going about this.</p>
</div>
<div id="comment-60623-info" class="comment-info">
<span class="comment-age">(14 Nov '17, 23:13)</span> <span class="comment-user userinfo">polemon</span>
</div>
</div>
</div>
<div id="comment-tools-60603" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60603-form-container" class="comment-form-container">
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

<span id="60631"></span>

<div id="answer-container-60631" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60631-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-60631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="polemon has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot use one relation as a building relation and a multipolygon relation at the same time. Instead, after creating your multipolygon, you would need to create a second relation, this time using <code>type=building</code> instead of <code>type=multipolygon</code>. Add the multipolygon relation, not the outer way, as the <code>outline</code> member.</p>
<p>Note, however, that building relations are optional (and indeed unnecessary) for almost all buildings – see my <a href="/questions/60330/how-do-you-create-a-relation-between-a-building-and-3d-building-parts/60332">answer</a> to a related question. So you can probably avoid the problem by simply not using one. :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '17, 15:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-60631" class="comments-container">
&#10;</div>
<div id="comment-tools-60631" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60631-form-container" class="comment-form-container">
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

