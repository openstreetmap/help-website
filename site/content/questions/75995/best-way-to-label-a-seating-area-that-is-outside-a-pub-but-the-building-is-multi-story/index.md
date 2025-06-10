+++
type = "question"
title = "Best way to label a seating area that is outside a pub, but the building is multi-story"
description = '''I am looking to add a small on-street seating area that is outside the pub &quot;the cask and barrel&quot; at 55.95906/-3.19026 and to have that seating area associated with the cask and barrel at a data level. Reading some other questions a suggestion was to draw the building around the whole area, however t...'''
date = "2020-08-03T22:51:00Z"
lastmod = "2020-08-04T19:27:00Z"
weight = 75995
keywords = [ "outdoor_seating", "pub" ]
aliases = [ "/questions/75995" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Best way to label a seating area that is outside a pub, but the building is multi-story](/questions/75995/best-way-to-label-a-seating-area-that-is-outside-a-pub-but-the-building-is-multi-story)

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
<span id="post-75995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75995-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am looking to add a small on-street seating area that is outside the pub "the cask and barrel" at <a href="https://www.openstreetmap.org/node/333159410">55.95906/-3.19026</a> and to have that seating area associated with the cask and barrel at a data level.</p>
<p>Reading some other questions a suggestion was to draw the building around the whole area, however the building is multi-story and above the pub is residential buildings, and adjusting the outline of the whole building feels wrong. I am not sure if multiple overlapping polygons is appropriate i.e. one polygon for the ground floor only excluding the outdoor area and marked as building, and one for the whole ground floor area that includes the outdoors and one polygon for first floor level and above (UK), but that seems a bit of a hassle.</p>
<p>I considered drawing a separate polygon area and associating it with the pub somehow. I'd like to avoid adding the area but not associating it with the specific pub.</p>
<p>The above is in addition to marking the outside area as leisure=outdoor_seating and the pub as outdoor_seating=yes, which seems correct.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-outdoor_seating" rel="tag" title="see questions tagged &#39;outdoor_seating&#39;">outdoor_seating</span> <span class="post-tag tag-link-pub" rel="tag" title="see questions tagged &#39;pub&#39;">pub</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '20, 22:51</strong></p>
<img src="https://secure.gravatar.com/avatar/b6e23fb0d90d55daddfcb2de6364ad66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davidxmiller&#39;s gravatar image" />
<p><span>davidxmiller</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davidxmiller has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Aug '20, 23:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-75995" class="comments-container">
&#10;</div>
<div id="comment-tools-75995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75995-form-container" class="comment-form-container">
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

<span id="75999"></span>

<div id="answer-container-75999" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75999-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd add a "outdoor_seating=yes" to the bar node, then I'll add a "leisure=outdoor_seating" area where the outdoor seating space is and add a operator tag to the area using the same name of the bar.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '20, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/e3dbac44db8deb4b09af6e6df914de1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mannivu&#39;s gravatar image" />
<p><span>Mannivu</span><br />
<span class="score" title="1084 reputation points"><span>1.1k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mannivu has 3 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-75999" class="comments-container">
<span id="76001"></span>
<div id="comment-76001" class="comment">
<div id="post-76001-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you for the suggestion! Do you know if there is a way to associated it more strongly with the exact pub at the level of the data? I agree it would be obvious to human looking at it that an outdoor area very close to a pub that was operated by a pub with the same name is a very close association, I was wondering if there is a way to link directly (rather than through association of the same name) with the pub?</p>
</div>
<div id="comment-76001-info" class="comment-info">
<span class="comment-age">(04 Aug '20, 16:00)</span> <span class="comment-user userinfo">davidxmiller</span>
</div>
</div>
<span id="76002"></span>
<div id="comment-76002" class="comment">
<div id="post-76002-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Other than the combinations indicated <a href="https://wiki.openstreetmap.org/wiki/Tag:leisure%3Doutdoor_seating">in the wiki</a> I don't think there's some way to link directly the POI and the area.</p>
</div>
<div id="comment-76002-info" class="comment-info">
<span class="comment-age">(04 Aug '20, 16:32)</span> <span class="comment-user userinfo">Mannivu</span>
</div>
</div>
<span id="76006"></span>
<div id="comment-76006" class="comment">
<div id="post-76006-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ok thanks :)</p>
</div>
<div id="comment-76006-info" class="comment-info">
<span class="comment-age">(04 Aug '20, 19:27)</span> <span class="comment-user userinfo">davidxmiller</span>
</div>
</div>
</div>
<div id="comment-tools-75999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75999-form-container" class="comment-form-container">
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

