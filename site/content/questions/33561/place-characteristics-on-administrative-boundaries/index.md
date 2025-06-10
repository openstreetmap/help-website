+++
type = "question"
title = "Place characteristics on administrative boundaries"
description = '''Background:  http://wiki.openstreetmap.org/wiki/Relation:boundary describes boundary relations, with the parent article http://wiki.openstreetmap.org/wiki/Boundaries explaining:  &#x27;The original accepted usage was to only apply (the boundary) tag to areas. However there now seems to be a consensus of ...'''
date = "2014-05-30T03:29:00Z"
lastmod = "2014-05-31T04:35:00Z"
weight = 33561
keywords = [ "place", "boundary", "administrative", "relations", "tags" ]
aliases = [ "/questions/33561" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Place characteristics on administrative boundaries](/questions/33561/place-characteristics-on-administrative-boundaries)

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
<span id="post-33561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33561-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Background:</p>
<hr />
<p><a href="http://wiki.openstreetmap.org/wiki/Relation:boundary">http://wiki.openstreetmap.org/wiki/Relation:boundary</a> describes boundary relations, with the parent article <a href="http://wiki.openstreetmap.org/wiki/Boundaries">http://wiki.openstreetmap.org/wiki/Boundaries</a> explaining:</p>
<p>'The original accepted usage was to only apply (the boundary) tag to areas. However there now seems to be a consensus of using the boundary key also on linear ways, with relations used to aggregate these ways if needed.'</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Place#Administrative_boundaries">http://wiki.openstreetmap.org/wiki/Place#Administrative_boundaries</a> is the best description I can find of how to do this. It prescribes (one boundary relation) (per administrative boundary), which will have:</p>
<ol>
<li>One or more ways of role 'outer'/'inner', which themselves are tagged with boundary and admin_level tags</li>
<li>Zero or one nodes of role 'admin_centre', for the 'center' of the administrative area</li>
<li>Zero or one nodes of role 'label', indicating where the label for the administrative boundary should be rendered</li>
</ol>
<hr />
<p>As best I've found, none of the above talks about where place related tags <strong>should</strong> go, prescriptively. Obviously we would like to avoid having the same information, possibly with different values, dumped into different places. So! My question is, "in an ideal world", where do tags like the following belong, picking one place for them?</p>
<p>population, ele, name, wikipedia, is_in, gnis, tiger, place</p>
<p>I realize that because both methods are "in the wild", our tools have to expect them to be in either place, and that's not really what I'm asking here. My question is, when a human editor is editing or performing cleanup, do the tags <strong>belong</strong> on the administrative boundary relation itself, or on a point (likely with the 'label' role) meant for this purpose?</p>
<p>Thanks for any insight!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-administrative" rel="tag" title="see questions tagged &#39;administrative&#39;">administrative</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '14, 03:29</strong></p>
<img src="https://secure.gravatar.com/avatar/41e323a2904da3bb06060a206cefc025?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Skybunny&#39;s gravatar image" />
<p><span>Skybunny</span><br />
<span class="score" title="60 reputation points">60</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Skybunny has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 May '14, 03:30</strong> </span></p>
</div>
</div>
<div id="comments-container-33561" class="comments-container">
&#10;</div>
<div id="comment-tools-33561" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33561-form-container" class="comment-form-container">
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

<span id="33564"></span>

<div id="answer-container-33564" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33564-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Those tags, excepting the ele tag as already answered by cartinus, would go on the area describing the place. Whether that's a single closed way surrounding the "place", or a multipolygon combining multiple ways, that's the object defining the place. The constituent boundary ways themselves obviously don't have a population, for example, though some notable ones do have Wikipedia articles (eg. Canada/US, US/Mexico, etc.).</p>
<p>BTW, is_in is generally considered unnecessary now. A determination of whether an object resides within another can be determined from their geographical relationship (ie. the coordinates for this object reside within this other area), so is_in is redundant. It isn't wrong to use it, though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '14, 17:49</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 May '14, 17:49</strong> </span></p>
</div>
</div>
<div id="comments-container-33564" class="comments-container">
<span id="33567"></span>
<div id="comment-33567" class="comment">
<div id="post-33567-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay! I think I gather from this:</p>
<p>When an administrative zone is ONLY specified with a point (typically place imports that need upgrading anyway), then by definition, all tags for are on that point.</p>
<p>However, when the better-refined administrative item now has 'an area', or 'a border relation' (it doesn't matter which), tags related to that (entire) administrative boundary belong on those and should be moved there.</p>
<p>Then it follows, nodes that exist for that administrative boundary relation with the admin_centre or label roles should NOT have those labels.</p>
<p>Have I got this right?</p>
</div>
<div id="comment-33567-info" class="comment-info">
<span class="comment-age">(30 May '14, 21:54)</span> <span class="comment-user userinfo">Skybunny</span>
</div>
</div>
<span id="33571"></span>
<div id="comment-33571" class="comment">
<div id="post-33571-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please don't go around removing them automatically from the admin_centre. (Not that you said so, but...) The values on it could be for the place itself and not the whole administrative area.</p>
</div>
<div id="comment-33571-info" class="comment-info">
<span class="comment-age">(31 May '14, 04:35)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-33564" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33564-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33562"></span>

<div id="answer-container-33562" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33562-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33562-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33562-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'll answer the obvious one below. The rest of your question will most likely invoke a long debate that isn't suitable for this site and should probably be held at the <a href="http://lists.openstreetmap.org/listinfo/tagging">tagging@ mailing list</a>. (See the <a href="https://help.openstreetmap.org/faq/">FAQ</a>.)</p>
<p>Administrative area's don't have a single elevation. Labels are "virtual", so they don't have an elevation at all. Only the admin_centre node can have an elevation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 May '14, 04:33</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-33562" class="comments-container">
&#10;</div>
<div id="comment-tools-33562" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33562-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

