+++
type = "question"
title = "Is it ok to add recycling material tags without the amenity tag?"
description = '''amenity=recycling will look odd on a point where there is a small container for batteries in an institution that is tagged by that point on the entry to the building, for example. It will keep data compact, but will make life harder for users querying database for recycling points. Were there any di...'''
date = "2014-10-04T10:37:00Z"
lastmod = "2014-10-05T10:57:00Z"
weight = 37298
keywords = [ "amenity", "tagging" ]
aliases = [ "/questions/37298" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is it ok to add recycling material tags without the amenity tag?](/questions/37298/is-it-ok-to-add-recycling-material-tags-without-the-amenity-tag)

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
<span id="post-37298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37298-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>amenity=recycling will look odd on a point where there is a small container for batteries in an institution that is tagged by that point on the entry to the building, for example. It will keep data compact, but will make life harder for users querying database for recycling points. Were there any discussions about this before, I can't find any? Should we update the wiki with the relevant info?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '14, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/1aaaf77e89ed1b496cefd433400ebf27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="int_ua&#39;s gravatar image" />
<p><span>int_ua</span><br />
<span class="score" title="275 reputation points">275</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="int_ua has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37298" class="comments-container">
&#10;</div>
<div id="comment-tools-37298" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37298-form-container" class="comment-form-container">
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

<span id="37309"></span>

<div id="answer-container-37309" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37309-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-37309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="int_ua has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't necessarily have to add the tags to the entrance node but you can't simply omit the <em>amenity=recycling</em> key. If it looks odd then this is a render-specific problem, don't make it a data problem. You should <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">never tag for the renderer</a>.</p>
<p>If someone wants to query OSM for recycling points then it is very important that our data is correct. Visual appearance of the map doesn't really matter for this task.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '14, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-37309" class="comments-container">
<span id="37310"></span>
<div id="comment-37310" class="comment">
<div id="post-37310-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If access to the institution is restricted to e.g. customers then perhaps an access tag on the amenity=recycling node would be valid?</p>
<p>That would also provide another hint that renderers could use in the future.</p>
</div>
<div id="comment-37310-info" class="comment-info">
<span class="comment-age">(05 Oct '14, 10:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-37309" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37309-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37304"></span>

<div id="answer-container-37304" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37304-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi if it’s behind the door, inside the building use the amenity key and add access=no / private and use these attributes, <a href="http://wiki.openstreetmap.org/wiki/DE:Tag:amenity%3Drecycling">http://wiki.openstreetmap.org/wiki/DE:Tag:amenity%3Drecycling</a> Your allowed to make your own proposal to add some tags to the OSM system tags. Take a look here as well <a href="http://wiki.openstreetmap.org/wiki/Proposal">http://wiki.openstreetmap.org/wiki/Proposal</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '14, 00:21</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-37304" class="comments-container">
&#10;</div>
<div id="comment-tools-37304" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37304-form-container" class="comment-form-container">
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

