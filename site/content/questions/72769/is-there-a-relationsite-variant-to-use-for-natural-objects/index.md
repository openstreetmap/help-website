+++
type = "question"
title = "Is there a relation:site variant to use for natural objects?"
description = '''I&#x27;m trying to tag a named grouping of small lakes with a group relation, and although relation:site seems to work, the wiki explicitly states it&#x27;s only for &quot;man-made objects&quot;. I see there&#x27;s a relation:cluster option, but it&#x27;s been in proposal for 5 years, and I haven&#x27;t found a single consumer that r...'''
date = "2020-01-30T04:52:00Z"
lastmod = "2020-01-31T10:51:00Z"
weight = 72769
keywords = [ "group", "tagging", "relations" ]
aliases = [ "/questions/72769" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a relation:site variant to use for natural objects?](/questions/72769/is-there-a-relationsite-variant-to-use-for-natural-objects)

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
<span id="post-72769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72769-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to tag a named grouping of small lakes with a group relation, and although relation:site seems to work, the wiki explicitly states it's only for "man-made objects". I see there's a relation:cluster option, but it's been in proposal for 5 years, and I haven't found a single consumer that renders it.</p>
<p>Is this a "hope it eventually renders someday" situation with relation:cluster, or is it acceptable to force a natural group of features into a 'site' relation - at least temporarily?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-group" rel="tag" title="see questions tagged &#39;group&#39;">group</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jan '20, 04:52</strong></p>
<img src="https://secure.gravatar.com/avatar/31ab4a3a30ec105540eb6d56c8ad98c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GregRetro&#39;s gravatar image" />
<p><span>GregRetro</span><br />
<span class="score" title="354 reputation points">354</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GregRetro has 3 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-72769" class="comments-container">
&#10;</div>
<div id="comment-tools-72769" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72769-form-container" class="comment-form-container">
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

<span id="72771"></span>

<div id="answer-container-72771" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72771-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Why not a multipolygon first? Since they are small, even if they are multipolygons themselves there would not be significant difficulty on grouping their members into a new relation.</p>
<p>Disadvantage:</p>
<ol>
<li>Lost the hierarchy of individual areas in a group of area.</li>
<li>Will create large multipolygons spanning a large area with many members in larger cases.</li>
</ol>
<p>Advantage:</p>
<ol>
<li>Individual members can be easily referenced to be in both the individual area and group of areas.</li>
<li>Easily understood, wide acceptance.</li>
</ol>
<blockquote>
<p>Is this a "hope it eventually renders someday" situation with relation:cluster</p>
</blockquote>
<p>You might be surprised to find that most prominently the Great Lakes (<a href="https://www.openstreetmap.org/relation/1124369)">https://www.openstreetmap.org/relation/1124369)</a> too are tagged as the similar <code>type=group</code>. As long as they are in a relation, you can worry about it later.</p>
<blockquote>
<p>the wiki explicitly states it's only for "man-made objects"</p>
<p>is it acceptable to force a natural group of features into a 'site' relation - at least temporarily?</p>
</blockquote>
<p>That seems to be a misunderstanding and inadequancy on Wiki. A <code>type=site</code> is for grouping all objects in a single "site" (eg all facilities on an individual school campus). A <code>type=cluster</code> in theory is grouping multiple multipolygons (or any object) as one (eg complicated campus areas of a school spread over a city, or a collective bunch of rocks as illustrated in its proposal). I don't see any reason why a <code>type=site</code> can't be used to group natural features.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Jan '20, 07:05</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Jan '20, 07:06</strong> </span></p>
</div>
</div>
<div id="comments-container-72771" class="comments-container">
<span id="72773"></span>
<div id="comment-72773" class="comment">
<div id="post-72773-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wouldn't use a multipolygon for the reasons you gave and also because you would lose the ability to individually tag the lakes.</p>
<p>I would go for the group or cluster relation. I don't see any significant difference between both so chose for yourself.</p>
<p><a href="https://help.openstreetmap.org/users/16887/kovoschiz">@Kovoschiz</a>: A site relation is explictly not "for grouping all objects in a single "site" (eg all facilities on an individual school campus)". That can adequately be described by an area. Sites are used for scattered objects where the area inbetween does not belong to the objects</p>
</div>
<div id="comment-72773-info" class="comment-info">
<span class="comment-age">(30 Jan '20, 10:31)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="72781"></span>
<div id="comment-72781" class="comment">
<div id="post-72781-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I explicitly quotation-marked "site" for his reference. I also believe tags on member areas override the multipolygon tag.</p>
</div>
<div id="comment-72781-info" class="comment-info">
<span class="comment-age">(30 Jan '20, 16:11)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="72786"></span>
<div id="comment-72786" class="comment">
<div id="post-72786-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10133/tzorn">@TZorn</a> But WHY would you go for the group or cluster relation?</p>
<p>One of the individual lakes in the group is named, and a couple are seasonal, so yeah I don't want a multipolygon relation. Each element needs to be distinctive.</p>
<p>Here's the group - currently as a 'site' relation. www.openstreetmap.org/relation/10653013</p>
<p>Looks like site relations don't render much more frequently than clusters.</p>
</div>
<div id="comment-72786-info" class="comment-info">
<span class="comment-age">(30 Jan '20, 21:03)</span> <span class="comment-user userinfo">GregRetro</span>
</div>
</div>
<span id="72794"></span>
<div id="comment-72794" class="comment">
<div id="post-72794-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's a gut thing. As you mentioned site is supposed to be used for man-made objects by the definition in the Wiki. Group and cluster are being used for natural objects.</p>
<p>I'm not sure it's really useful to have these three different yet very similar relation types. But that is another question beyond the scope of this help site.</p>
</div>
<div id="comment-72794-info" class="comment-info">
<span class="comment-age">(31 Jan '20, 10:51)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-72771" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72771-form-container" class="comment-form-container">
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

