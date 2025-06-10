+++
type = "question"
title = "Is there a definable distinction bitween the &quot;old&quot; and &quot;new&quot; multipolygon styles?"
description = '''Comparing the old and current OSM Wiki documentation I cannot find clear/definable difference between the old and the new (&quot;modern&quot;) multipolygon descriptions except that the &quot;old&quot; style had no area-type tag, while the &quot;new&quot; style must have it, on the relation level. However, in some app related doc...'''
date = "2017-07-14T09:23:00Z"
lastmod = "2017-07-14T10:11:00Z"
weight = 57085
keywords = [ "styles", "new", "old", "multipolygon" ]
aliases = [ "/questions/57085" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a definable distinction bitween the "old" and "new" multipolygon styles?](/questions/57085/is-there-a-definable-distinction-bitween-the-old-and-new-multipolygon-styles)

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
<span id="post-57085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57085-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Comparing the old and current OSM Wiki documentation I cannot find clear/definable difference between the old and the new ("modern") multipolygon descriptions except that the "old" style had no area-type tag, while the "new" style must have it, on the relation level. However, in some app related documents there are examples qualified as "...One particular sub-variant is that inner ways have the same tags as the outer ways..." (<a href="https://goo.gl/rwn2F3">https://goo.gl/rwn2F3</a> Inner way has same tags) indicating that there are many other old styles as well.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-styles" rel="tag" title="see questions tagged &#39;styles&#39;">styles</span> <span class="post-tag tag-link-new" rel="tag" title="see questions tagged &#39;new&#39;">new</span> <span class="post-tag tag-link-old" rel="tag" title="see questions tagged &#39;old&#39;">old</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '17, 09:23</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-57085" class="comments-container">
&#10;</div>
<div id="comment-tools-57085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57085-form-container" class="comment-form-container">
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

<span id="57086"></span>

<div id="answer-container-57086" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57086-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Old-style multipolygons have the area tags on the outer ways, this is now deprecated and does not work any more on the main OSM map style. New-style multipolygons have the area tags on the relation. There are all sorts of special cases with tags also on inner ways or both on outer ways and on the relations which makes this even more complicated. This is the reason why we had to get rid of it.</p>
<p>Now there is only one simple way to tag things: Every tags "belongs" only to the object it is actually on. A tag on a way describes what this way is about, the tags don't influence the relations this way might be in. A tag on a relation describes what this relation is about. The tags on the members of a relation don't change what a relation is about, only the members geometry is used on the relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '17, 10:11</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-57086" class="comments-container">
&#10;</div>
<div id="comment-tools-57086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57086-form-container" class="comment-form-container">
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

