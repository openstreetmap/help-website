+++
type = "question"
title = "How to permanently implement a new map layer in iD editor?"
description = '''Canton Aargau and Zurich have recently updated aerial imagery. JOSM already implemented them. Now I would like to do the same for iD editor. It looks like as if the change has to be done in this file, but I would need some guidance on how to actually do it.'''
date = "2021-07-03T22:30:00Z"
lastmod = "2021-07-05T15:32:00Z"
weight = 80819
keywords = [ "ideditor", "imagery", "code" ]
aliases = [ "/questions/80819" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to permanently implement a new map layer in iD editor?](/questions/80819/how-to-permanently-implement-a-new-map-layer-in-id-editor)

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
<span id="post-80819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80819-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Canton Aargau and Zurich have recently updated aerial imagery. <a href="https://josm.openstreetmap.de/wiki/Maps/Switzerland#KantonAargau20cmAGIS2020">JOSM already implemented them</a>. Now I would like to do the same for iD editor. It looks like as if the change has to be done in <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/vendor/assets/iD/iD/data/imagery.min.json">this file</a>, but I would need some guidance on how to actually do it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-code" rel="tag" title="see questions tagged &#39;code&#39;">code</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '21, 22:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a6e2839b04b99e35e45d64fe66b9a500?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rene78&#39;s gravatar image" />
<p><span>rene78</span><br />
<span class="score" title="700 reputation points">700</span><span title="29 badges"><span class="badge1">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rene78 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Jul '21, 22:32</strong> </span></p>
</div>
</div>
<div id="comments-container-80819" class="comments-container">
<span id="80821"></span>
<div id="comment-80821" class="comment">
<div id="post-80821-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This seems like a question that might be more appropriate for the iD <a href="https://github.com/openstreetmap/iD/issues">issue tracker</a>.</p>
</div>
<div id="comment-80821-info" class="comment-info">
<span class="comment-age">(04 Jul '21, 03:29)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="80822"></span>
<div id="comment-80822" class="comment">
<div id="post-80822-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Didn't want to do that since it is more of a question and less of an issue. Not sure how happy those developers are with how-to questions on the repo.</p>
<p>But I am going to give it a try if there is no one here, who can answer it.</p>
</div>
<div id="comment-80822-info" class="comment-info">
<span class="comment-age">(04 Jul '21, 09:32)</span> <span class="comment-user userinfo">rene78</span>
</div>
</div>
</div>
<div id="comment-tools-80819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80819-form-container" class="comment-form-container">
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

<span id="80829"></span>

<div id="answer-container-80829" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80829-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80829-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80829-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rene78 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At the moment the iD available on the OpenStreetMap website hasn't been updated in a while. The imagery is currently updated when the editor is updated (there's work to address both of these things).</p>
<p>The definition for the layer needs to be added to <a href="https://github.com/ideditor/imagery-index/tree/main/sources/europe/switzerland">https://github.com/ideditor/imagery-index/tree/main/sources/europe/switzerland</a> and then an iD version using that definition needs to be deployed. The information is already mostly available at <a href="https://github.com/osmlab/editor-layer-index/tree/gh-pages/sources/europe/ch">https://github.com/osmlab/editor-layer-index/tree/gh-pages/sources/europe/ch</a> (iD updates stalled in the middle of the switch over from one index to the other; I'm not sure what the longer term situation will be).</p>
<p>In any case, the work is mostly done, the issue is more that the updates are stalled out (but there's activity to address that).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '21, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-80829" class="comments-container">
&#10;</div>
<div id="comment-tools-80829" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80829-form-container" class="comment-form-container">
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

