+++
type = "question"
title = "What tagging should be used for a Temporary closure of pub?"
description = '''I walked past a pub yesterday, which was closed and covered in scaffolding. It turns out it was damaged by a fire in March, but will reopen - at an unspecified date - when the damage inside has been repaired. I&#x27;m struggling to see what tags can be used to reflect this situation.  &quot;Disused&quot; seems a b...'''
date = "2022-04-29T12:03:00Z"
lastmod = "2022-04-30T11:52:00Z"
weight = 84302
keywords = [ "construction", "disused", "pub" ]
aliases = [ "/questions/84302" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What tagging should be used for a Temporary closure of pub?](/questions/84302/what-tagging-should-be-used-for-a-temporary-closure-of-pub)

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
<span id="post-84302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84302-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I walked past a pub yesterday, which was closed and covered in scaffolding. It turns out it was damaged by a fire in March, but will reopen - at an unspecified date - when the damage inside has been repaired. I'm struggling to see what tags can be used to reflect this situation.</p>
<p>"Disused" seems a bit strong, as that to me would be if it had just closed down permanently. "Construction area" also feels wrong, as that would imply that the pub was being rebuilt, when the outside is still more or less "visually" fine.</p>
<p>I'm tempted to just change the name of pub to "The Kings Arms - temporarily closed", so that at least people will be able to see this on rendered maps...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-construction" rel="tag" title="see questions tagged &#39;construction&#39;">construction</span> <span class="post-tag tag-link-disused" rel="tag" title="see questions tagged &#39;disused&#39;">disused</span> <span class="post-tag tag-link-pub" rel="tag" title="see questions tagged &#39;pub&#39;">pub</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '22, 12:03</strong></p>
<img src="https://secure.gravatar.com/avatar/1ece74e1adbd49c1a9f05765c5d9f39a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mikey%20Co&#39;s gravatar image" />
<p><span>Mikey Co</span><br />
<span class="score" title="131 reputation points">131</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mikey Co has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84302" class="comments-container">
&#10;</div>
<div id="comment-tools-84302" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84302-form-container" class="comment-form-container">
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

<span id="84305"></span>

<div id="answer-container-84305" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84305-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-84305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could use <code>opening_hours=closed</code> (or, probably less good, <code>operational_status=closed</code>).</p>
<p>You could also add a <code>note=</code> tag to let other mappers know why you've used this rather than <code>disused:amenity=pub</code>, and perhaps also a <code>fixme=</code> or OSM note to remind you/others to come back and survey it!</p>
<p>Please don't change the name tag - the name of the pub is not "temporarily closed" and there are other consumers that use name tags, e.g. geocoders, routers and many forms of spatial analysis.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '22, 12:36</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Apr '22, 12:37</strong> </span></p>
</div>
</div>
<div id="comments-container-84305" class="comments-container">
<span id="84308"></span>
<div id="comment-84308" class="comment">
<div id="post-84308-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I was going to include a note and fixme, but changing the opening hours is still not that informative for someone just looking at the main OSM renders or websites which sit over OSM and don't allow you to drill down into the detail of the premises.</p>
<p>To such users it will still look like an open pub</p>
</div>
<div id="comment-84308-info" class="comment-info">
<span class="comment-age">(29 Apr '22, 15:08)</span> <span class="comment-user userinfo">Mikey Co</span>
</div>
</div>
<span id="84316"></span>
<div id="comment-84316" class="comment">
<div id="post-84316-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"changing the opening hours is still not that informative for someone just looking at the main OSM renders..." you can't really cater to every use case. The likes of OsmAnd highlight opening hours if anyone nearby searches for it.</p>
</div>
<div id="comment-84316-info" class="comment-info">
<span class="comment-age">(30 Apr '22, 11:52)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-84305" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84305-form-container" class="comment-form-container">
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

