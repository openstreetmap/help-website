+++
type = "question"
title = "wetlands and fields not showing up"
description = '''I&#x27;ve tried marking some open fields and wetlands in the middle of forested areas but they are not showing up when I &quot;view&quot;. I am quite new to OSM, so I&#x27;m sure it&#x27;s my fault. How does one mark open fields and/or wetlands?'''
date = "2012-05-14T05:01:00Z"
lastmod = "2012-05-15T03:40:00Z"
weight = 12707
keywords = [ "fields", "wetlands" ]
aliases = [ "/questions/12707" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wetlands and fields not showing up](/questions/12707/wetlands-and-fields-not-showing-up)

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
<span id="post-12707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12707-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've tried marking some open fields and wetlands in the middle of forested areas but they are not showing up when I "view". I am quite new to OSM, so I'm sure it's my fault. How does one mark open fields and/or wetlands?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span> <span class="post-tag tag-link-wetlands" rel="tag" title="see questions tagged &#39;wetlands&#39;">wetlands</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '12, 05:01</strong></p>
<img src="https://secure.gravatar.com/avatar/f082597d1deb5c07637f2401aa41652a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jhp&#39;s gravatar image" />
<p><span>jhp</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jhp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12707" class="comments-container">
&#10;</div>
<div id="comment-tools-12707" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12707-form-container" class="comment-form-container">
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

<span id="12709"></span>

<div id="answer-container-12709" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12709-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At least <a href="https://www.openstreetmap.org/browse/way/163534673">way 163534673</a> is visible to me.</p>
<p>I think the problem is that you didn't wait long enough to let the renderer handle your edits, as described in the FAQ: <a href="https://wiki.openstreetmap.org/wiki/Faq#I_have_just_made_some_changes_to_the_map._How_do_I_get_to_see_my_changes.3F">I have just made some changes to the map. How do I get to see my changes?</a></p>
<p>A potential problem is that you have added overlapping land usages. I if an area is covered by both landuse A and landuse B then, depending of how the renderer is constructed, it may be a matter of coincidence which landuse is rendered over the other. The solution to that is to use a <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">multipolygon relation</a> and for example cut holes in the forest where you put your lakes, meadows etc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '12, 07:44</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-12709" class="comments-container">
<span id="12736"></span>
<div id="comment-12736" class="comment">
<div id="post-12736-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@gnurk</span> Thanks for the response. The asynchronous handling of the edits explained my field change problem, but not the wetland change problem. In the end, I got the wetlands by selecting an area, choosing "advanced" on the properties editing for that area and making sure that the only key value pair was natural = wetland. Having a landuse key/value pair as well seemed to be overriding the natural=wetland pair. Once that was the only pair, it rendered as I expected.</p>
<p>Thanks again for you time and for teaching me about the asynchronous nature of updates.</p>
</div>
<div id="comment-12736-info" class="comment-info">
<span class="comment-age">(15 May '12, 03:40)</span> <span class="comment-user userinfo">jhp</span>
</div>
</div>
</div>
<div id="comment-tools-12709" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12709-form-container" class="comment-form-container">
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

