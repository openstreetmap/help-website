+++
type = "question"
title = "Tagging Question"
description = '''I&#x27;ve been adding businesses on my morning commute to the map. I recently added a &quot;bikini club&quot; called Soft Tails. (This is in Volusia County, Florida, USA, site of two major motorcycle rallies every year, so the name is a pun.) I&#x27;ve added it as a bar, but I&#x27;m not sure if that&#x27;s really the best desig...'''
date = "2020-11-13T16:38:00Z"
lastmod = "2020-11-13T23:32:00Z"
weight = 77538
keywords = [ "bar", "adult", "tagging" ]
aliases = [ "/questions/77538" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging Question](/questions/77538/tagging-question)

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
<span id="post-77538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77538-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been adding businesses on my morning commute to the map. I recently added a "bikini club" called Soft Tails. (This is in Volusia County, Florida, USA, site of two major motorcycle rallies every year, so the name is a pun.) I've added it as a bar, but I'm not sure if that's really the best designation for it.</p>
<p>Is there a tag for "adult" establishments so it can be differentiated from normal bars? Or should it be listed as something other than a bar?</p>
<p>This would also apply to certain types of theaters, video establishments, and massage parlors. I don't think we should leave them blank since they do exist, but it might be nice to separate them out so that a tourist doesn't go to someplace they don't want to go.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bar" rel="tag" title="see questions tagged &#39;bar&#39;">bar</span> <span class="post-tag tag-link-adult" rel="tag" title="see questions tagged &#39;adult&#39;">adult</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Nov '20, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/2cfd0bb46691a581540c6bc9403b674f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikC&#39;s gravatar image" />
<p><span>FredrikC</span><br />
<span class="score" title="118 reputation points">118</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikC has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77538" class="comments-container">
&#10;</div>
<div id="comment-tools-77538" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77538-form-container" class="comment-form-container">
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

<span id="77542"></span>

<div id="answer-container-77542" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77542-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-77542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If there's legal restriction, <code>min_age=18</code> (how ever your local laws regulate) is possible. There's ~1k <code>amenity=stripclub</code>, 300 <code>amenity=swingerclub</code> to be specific for some.</p>
<p><code>*:for=adult</code> would be ambiguous. With <code>shop=erotic</code> and <code>books=erotic</code> (and a peculiar 2 <code>massage=erotic</code> instances on <code>shop=massage</code>) being standard, a general <code>theme=erotic</code> may fit some of these. If paid sex service is offered, it should likely be a direct <code>amenity=brothel</code> (or perhaps at least <code>brothel=yes</code> if say optional or hidden inside).</p>
<p>For <code>amenity=cinema</code>, ~1k <code>cinema:3D=</code> outnumbers the ~40 <code>cinema=</code>. The 1 <code>cinema=erotic</code> may not be strong enough. For <code>shop=video</code>, <code>video=</code> is basically links to actual videos (the 5 poor style <code>video:type=</code> among other properly defined sub-keys, with 1 aforementioned ambiguous <code>video:type=adult</code>, is unconvincing).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '20, 23:32</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '20, 23:55</strong> </span></p>
</div>
</div>
<div id="comments-container-77542" class="comments-container">
&#10;</div>
<div id="comment-tools-77542" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77542-form-container" class="comment-form-container">
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

