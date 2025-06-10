+++
type = "question"
title = "How to copy tags from outer way to multi-polygon relation"
description = '''We&#x27;ve got lots of polygons in Massachusetts where the outer way is tagged instead of the relation. Example: http://www.openstreetmap.org/relation/1236669 I&#x27;d like to be able to &quot;cut&quot; the tags from the outer way and &quot;paste&quot; them to the relation in the JOSM Relation Editor window. I can&#x27;t seem do it w...'''
date = "2016-06-26T20:02:00Z"
lastmod = "2017-12-27T19:33:00Z"
weight = 50467
keywords = [ "josm", "multipolygon", "copy-paste", "relation", "tags" ]
aliases = [ "/questions/50467" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to copy tags from outer way to multi-polygon relation](/questions/50467/how-to-copy-tags-from-outer-way-to-multi-polygon-relation)

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
<span id="post-50467-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50467-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50467-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We've got lots of polygons in Massachusetts where the outer way is tagged instead of the relation.</p>
<p>Example: <a href="http://www.openstreetmap.org/relation/1236669">http://www.openstreetmap.org/relation/1236669</a></p>
<p>I'd like to be able to "cut" the tags from the outer way and "paste" them to the relation in the JOSM Relation Editor window. I can't seem do it with the copy tags/paste tags commands.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span> <span class="post-tag tag-link-copy-paste" rel="tag" title="see questions tagged &#39;copy-paste&#39;">copy-paste</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jun '16, 20:02</strong></p>
<img src="https://secure.gravatar.com/avatar/75cc9956f060892f585352e9011cd26e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alan01730&#39;s gravatar image" />
<p><span>Alan01730</span><br />
<span class="score" title="464 reputation points">464</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alan01730 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jun '16, 20:32</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-50467" class="comments-container">
&#10;</div>
<div id="comment-tools-50467" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50467-form-container" class="comment-form-container">
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

<span id="50470"></span>

<div id="answer-container-50470" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50470-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-50470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alan01730 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, select/highlight the tags you want to transfer</p>
<pre><code>copy the selected/highlighted tags
right click and delete the tags from the way
open the relation editor
(in the top half of editor) click on button with the 3 + signs (to Paste tags from buffer)
click OK to close the relation editor
Done.</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '16, 20:42</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-50470" class="comments-container">
<span id="50525"></span>
<div id="comment-50525" class="comment">
<div id="post-50525-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Worked like a charm. I always wondered about those 3 plus signs.</p>
</div>
<div id="comment-50525-info" class="comment-info">
<span class="comment-age">(30 Jun '16, 00:19)</span> <span class="comment-user userinfo">Alan01730</span>
</div>
</div>
<span id="61387"></span>
<div id="comment-61387" class="comment">
<div id="post-61387-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I really wish this could be possible in ID. Its only limited by the fact that you STILL can't do a copy all tags and paste tags function.</p>
</div>
<div id="comment-61387-info" class="comment-info">
<span class="comment-age">(27 Dec '17, 19:33)</span> <span class="comment-user userinfo">Mxdanger</span>
</div>
</div>
</div>
<div id="comment-tools-50470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50470-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50468"></span>

<div id="answer-container-50468" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50468-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>select the relation (not the relation editor window), then you can paste them (e.g. ctrl+shift+v)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jun '16, 20:31</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-50468" class="comments-container">
&#10;</div>
<div id="comment-tools-50468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50468-form-container" class="comment-form-container">
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

