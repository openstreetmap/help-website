+++
type = "question"
title = "Thatcham level crossing revert"
description = '''Hello. In changeset 78591704, the area around Thatcham level crossing/railway station was modified so that the editor&#x27;s sat nav would work. The changes have led to some oddities - the side roads are disconnected, there is a gate on a platform, odd maxspeed etc. The editor has made a number of edits ...'''
date = "2019-12-22T08:58:00Z"
lastmod = "2019-12-28T20:24:00Z"
weight = 72202
keywords = [ "revert", "railway", "thatcham" ]
aliases = [ "/questions/72202" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Thatcham level crossing revert](/questions/72202/thatcham-level-crossing-revert)

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
<span id="post-72202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72202-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello.</p>
<p>In changeset 78591704, the area around Thatcham level crossing/railway station was modified so that the editor's sat nav would work. The changes have led to some oddities - the side roads are disconnected, there is a gate on a platform, odd maxspeed etc. The editor has made a number of edits to this and possibly some other level crossings in the area with comments implying that their satnav won't route them through level crossings. See for example <a href="https://www.openstreetmap.org/changeset/67170360">https://www.openstreetmap.org/changeset/67170360</a> where bizarrely everything except motor vehicles was forbidden - fortunately my journey planner ignores access tags on nodes.</p>
<p>I contacted the editor but received no reply. It would be easier to revert than try to correct the errors introduced in the changeset. If someone could revert the changeset, then I propose to remove the barrier=gate nodes (if they haven't already been removed) and replace with crossing:barrier on the level crossing nodes.</p>
<p>Jon</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span> <span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span> <span class="post-tag tag-link-thatcham" rel="tag" title="see questions tagged &#39;thatcham&#39;">thatcham</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Dec '19, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/cf4d0ea359df782ea8261afa0ad88d1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jpennycook&#39;s gravatar image" />
<p><span>jpennycook</span><br />
<span class="score" title="71 reputation points">71</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jpennycook has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Dec '19, 09:05</strong> </span></p>
</div>
</div>
<div id="comments-container-72202" class="comments-container">
&#10;</div>
<div id="comment-tools-72202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72202-form-container" class="comment-form-container">
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

<span id="72258"></span>

<div id="answer-container-72258" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72258-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-72258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jpennycook has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Jon,</p>
<p>No problem I've reverted changesets 78592218,78591769 and78591704. You can make the changes to the crossings now, (I did see your OpenStreetCam pictures) any barriers would have to be on all 6 crossing points. Wiki page <a href="https://wiki.openstreetmap.org/wiki/Tag:railway%3Dlevel_crossing">https://wiki.openstreetmap.org/wiki/Tag:railway%3Dlevel_crossing</a> has info on tagging different types of crossing barriers. If you need any help please just ask.</p>
<p>Happy Mapping in the New Year. Regards Bernard.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Dec '19, 18:17</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-72258" class="comments-container">
<span id="72211"></span>
<div id="comment-72211" class="comment">
<div id="post-72211-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi, I've previously tried to contact kaj1970 through changeset comments with no success.</p>
<p>In order to revert/remedy changeset 78591704 you would have to revert the later two changesets #78591769 and #78592218, there would then be two conflicts to resolve. Reverting changeset 78591704 on its own results in five conflicts. I can make the reverts if you wish.</p>
<p>Mapillary images indicate that there are what look to be a barrier across the footpath, rpad and cycleway.</p>
<p>What do you think?</p>
<p>Bernard</p>
</div>
<div id="comment-72211-info" class="comment-info">
<span class="comment-age">(22 Dec '19, 20:30)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="72256"></span>
<div id="comment-72256" class="comment">
<div id="post-72256-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Bernard.</p>
<p>Thanks for your reply - unfortunately Christmas distracted me otherwise I would have replied sooner!</p>
<p>The level crossing is a typical one with a single "barrier=lift gate" at either side which blocks both the road and the pavements, and lights like the ones in the photo at <a href="https://wiki.openstreetmap.org/wiki/Tag:railway%3Dlevel_crossing">level crossing</a>. I've got some poor quality OpenStreetCam footage from when I was experimenting with a bicycle handlebar mount for my phone, but it only covers the car park and the road to the north of the level crossing.</p>
<p>Yes - I think those two changesets would also need to be reverted. I'm afraid that I would cause more harm than good if I tried to revert anything myself, so if you can make the reverts, that would be great.</p>
<p>On an unrelated note, I believe you've fixed problems in some of my changesets in the past - thanks for doing that.</p>
<p>Jon</p>
</div>
<div id="comment-72256-info" class="comment-info">
<span class="comment-age">(28 Dec '19, 15:12)</span> <span class="comment-user userinfo">jpennycook</span>
</div>
</div>
<span id="72264"></span>
<div id="comment-72264" class="comment">
<div id="post-72264-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Bernard, and happy new year to you too.</p>
<p>Jon</p>
</div>
<div id="comment-72264-info" class="comment-info">
<span class="comment-age">(28 Dec '19, 20:24)</span> <span class="comment-user userinfo">jpennycook</span>
</div>
</div>
</div>
<div id="comment-tools-72258" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72258-form-container" class="comment-form-container">
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

