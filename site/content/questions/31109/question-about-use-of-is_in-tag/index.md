+++
type = "question"
title = "Question about use of &quot;is_in&quot; tag"
description = '''Hi, I want to tag some amenities inside of a large shopping building with many levels. If I tag a cafe on level=0 how is one to know that this particular cafe &quot;is_in&quot; this building and not, for example, on the sidewalk outside the building? In short, is the &quot;is_in&quot; tag restricted to tagging places i...'''
date = "2014-02-28T02:43:00Z"
lastmod = "2014-02-28T10:27:00Z"
weight = 31109
keywords = [ "tagging", "is_in" ]
aliases = [ "/questions/31109" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Question about use of "is_in" tag](/questions/31109/question-about-use-of-is_in-tag)

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
<span id="post-31109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31109-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to tag some amenities inside of a large shopping building with many levels. If I tag a cafe on level=0 how is one to know that this particular cafe "is_in" this building and not, for example, on the sidewalk outside the building?</p>
<p>In short, is the "is_in" tag restricted to tagging places inside of boundaries or can I use it to say amenity=cafe, name=My Cafe, is_in=My Shopping Mall, level=0</p>
<p>Cheers</p>
<p>Dave</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-is_in" rel="tag" title="see questions tagged &#39;is_in&#39;">is_in</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '14, 02:43</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Feb '14, 02:44</strong> </span></p>
</div>
</div>
<div id="comments-container-31109" class="comments-container">
&#10;</div>
<div id="comment-tools-31109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31109-form-container" class="comment-form-container">
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

<span id="31111"></span>

<div id="answer-container-31111" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31111-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-31111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlaskaDave has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the POI you add is within the area of the large shopping building (presumably drawn as an area anyway), then as this is geographic information it is automatically within the building. You could perhaps add <a href="http://wiki.openstreetmap.org/wiki/Key:addr">address tags</a> though which would make it clearer.</p>
<p><code>is_in</code> isn't really needed for places within well defined boundaries either for similar reasons, though some people still use it - see the second paragraph about when to use it <a href="http://wiki.openstreetmap.org/wiki/Key:is_in">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '14, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-31111" class="comments-container">
<span id="31113"></span>
<div id="comment-31113" class="comment">
<div id="post-31113-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Ed,</p>
<p>Yes, that makes sense. My OSM world is governed a lot (too much sometimes) by the limitations of my GPS receiver, and so is my thinking about these matters sometimes. ;-)</p>
<p>From reading the Wiki, I was aware of the limited need for the is_in tag now that there are boundaries for most administrative areas. But I thought to myself, how will my GPS know where this place is?</p>
<p>Thanks again...</p>
</div>
<div id="comment-31113-info" class="comment-info">
<span class="comment-age">(28 Feb '14, 10:27)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-31111" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31111-form-container" class="comment-form-container">
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

