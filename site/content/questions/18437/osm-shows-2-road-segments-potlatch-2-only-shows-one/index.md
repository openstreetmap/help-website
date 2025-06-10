+++
type = "question"
title = "OSM shows 2 road segments, Potlatch 2 only shows one"
description = '''If you go here, http://osm.org/go/_~76v6sbP- you&#x27;ll see two road segments that need to be joined. However, when you go into Potlatch 2, it&#x27;s not possible to join them, because only one of the segments is shown! What&#x27;s going on here? If this is a bug, how would I submit a bug report? Thanks'''
date = "2012-12-14T01:23:00Z"
lastmod = "2012-12-16T05:00:00Z"
weight = 18437
keywords = [ "segments", "wrapdateline", "missing" ]
aliases = [ "/questions/18437" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM shows 2 road segments, Potlatch 2 only shows one](/questions/18437/osm-shows-2-road-segments-potlatch-2-only-shows-one)

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
<span id="post-18437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18437-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If you go here,</p>
<p><a href="http://osm.org/go/_~76v6sbP-">http://osm.org/go/_~76v6sbP-</a></p>
<p>you'll see two road segments that need to be joined.</p>
<p>However, when you go into Potlatch 2, it's not possible to join them, because only one of the segments is shown!</p>
<p>What's going on here? If this is a bug, how would I submit a bug report?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-segments" rel="tag" title="see questions tagged &#39;segments&#39;">segments</span> <span class="post-tag tag-link-wrapdateline" rel="tag" title="see questions tagged &#39;wrapdateline&#39;">wrapdateline</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '12, 01:23</strong></p>
<img src="https://secure.gravatar.com/avatar/c19947732a0bfcad4c5b34629179ed7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gpspilot1&#39;s gravatar image" />
<p><span>gpspilot1</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gpspilot1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Dec '12, 02:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span></p>
</div>
</div>
<div id="comments-container-18437" class="comments-container">
<span id="18440"></span>
<div id="comment-18440" class="comment">
<div id="post-18440-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I confirm your observation. Also the eastern part is not visible in the data layer. 1. Maybe the eastern part was deleted in the meantime? 2. Maybe there is some bug due to the longitude of -179.99957 (at the wrap-over to 180°)? Potlatch1 does not even load at that point (error message: "Sorry - I can't get the map for that area. The server said: The latitudes must be between -90.0 and 90.0, and longitudes between -180.0 and 180.0").</p>
</div>
<div id="comment-18440-info" class="comment-info">
<span class="comment-age">(14 Dec '12, 02:18)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="18481"></span>
<div id="comment-18481" class="comment">
<div id="post-18481-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nice observation about the longitude. Here's another observation: the pinkish vertical way found at 180° has been incorrectly designated a "Coastline." Is that just a coincidence, or could that be related to the problem?</p>
</div>
<div id="comment-18481-info" class="comment-info">
<span class="comment-age">(16 Dec '12, 05:00)</span> <span class="comment-user userinfo">gpspilot1</span>
</div>
</div>
</div>
<div id="comment-tools-18437" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18437-form-container" class="comment-form-container">
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

<span id="18443"></span>

<div id="answer-container-18443" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18443-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-18443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is indeed a nice bug. If you open the data layer <a href="http://www.openstreetmap.org/?lat=66.64055&amp;lon=179.99975&amp;zoom=17&amp;layers=M">west</a> from the 180° wrapping you only see way <a href="http://www.openstreetmap.org/browse/way/146443291">146443291</a> and if you open the data layer <a href="http://www.openstreetmap.org/?lat=66.64052&amp;lon=-179.99719&amp;zoom=17&amp;layers=M">east</a> you only see way <a href="http://www.openstreetmap.org/browse/way/146798914">146798914</a>. As Potlatch 1 and Potlatch 2 show a similar behavior the bug seems to be in the API.</p>
<p>I created a <a href="https://trac.openstreetmap.org/ticket/4720">ticket</a> for this issue.</p>
<p><em>edit</em>: seems to be a <a href="https://trac.openstreetmap.org/ticket/1612">known bug</a> for several years.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '12, 07:36</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Dec '12, 08:29</strong> </span></p>
</div>
</div>
<div id="comments-container-18443" class="comments-container">
&#10;</div>
<div id="comment-tools-18443" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18443-form-container" class="comment-form-container">
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

