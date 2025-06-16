+++
type = "question"
title = "Creating and splitting a multipolygon"
description = '''I want to create a multipolygon water area. I have two lagoons that are outlined with NOAA Shoreline including central islands. The area is already a multipolygon but the two lagoons are not separated. I want to separate them. I&#x27;ve tried drawing a line and connecting it to the shoreline vector but I...'''
date = "2013-06-06T18:50:00Z"
lastmod = "2013-06-06T20:42:00Z"
weight = 23080
keywords = [ "water", "editing", "multipolygon" ]
aliases = [ "/questions/23080" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Creating and splitting a multipolygon](/questions/23080/creating-and-splitting-a-multipolygon)

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
<span id="post-23080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23080-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-23080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to create a multipolygon water area. I have two lagoons that are outlined with NOAA Shoreline including central islands. The area is already a multipolygon but the two lagoons are not separated. I want to separate them. I've tried drawing a line and connecting it to the shoreline vector but I can't figure out how to partition of each separate lagoon.</p>
<p>There is also a large bay that I want to close off from the ocean that is lined with NOAA shoreline vector that is not set as a multipolygon area.</p>
<p>Basically, How do I create a multipolygon using existing vectors plus a new connecting vector, and how do I split an existing multipolygon into to separate multipolygons?</p>
<p>Can this be done using the ID editor or potlatch2?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '13, 18:50</strong></p>
<img src="https://secure.gravatar.com/avatar/7143b29ac9808a03164d7434b74ee8a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EGhost57&#39;s gravatar image" />
<p><span>EGhost57</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EGhost57 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-23080" class="comments-container">
&#10;</div>
<div id="comment-tools-23080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23080-form-container" class="comment-form-container">
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

<span id="23081"></span>

<div id="answer-container-23081" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-23081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-23081-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-23081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can do it with Potlatch2, but not (yet) with iD.</p>
<p>If you have a look at <a href="https://wiki.openstreetmap.org/wiki/Multipolygon">this page</a>, and read down to the "Potlatch 2 example", you should see some pictures that explain the basic process. To do what you're trying to do, you'll also need to split and rejoin some ways too.</p>
<p>Your area is slightly complicated because you're dealing with coastline, which doesn't get updated as often on the "standard" map rendering as other features (see some of <a href="https://help.openstreetmap.org/search/?q=coastline&amp;Submit=Search&amp;t=question">these previous questions</a> for details).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '13, 19:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-23081" class="comments-container">
<span id="23084"></span>
<div id="comment-23084" class="comment">
<div id="post-23084-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for pointing me in the right direction. As a beginner I am extremely impressed with the helpfulness of the community thus far.</p>
</div>
<div id="comment-23084-info" class="comment-info">
<span class="comment-age">(06 Jun '13, 20:42)</span> <span class="comment-user userinfo">EGhost57</span>
</div>
</div>
</div>
<div id="comment-tools-23081" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-23081-form-container" class="comment-form-container">
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

