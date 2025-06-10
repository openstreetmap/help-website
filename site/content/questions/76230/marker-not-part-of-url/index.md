+++
type = "question"
title = "marker not part of URL"
description = '''When attempting to include the marker in the URL when sharing a place, the marker is not part of the URL - toggling the feature does not change the URL. Example: I want to share this place and have the marker included, but it wil not show up: https://www.openstreetmap.org/?mlat=51.02752&amp;amp;mlon=3.7...'''
date = "2020-08-20T08:16:00Z"
lastmod = "2020-08-20T11:11:00Z"
weight = 76230
keywords = [ "bug" ]
aliases = [ "/questions/76230" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [marker not part of URL](/questions/76230/marker-not-part-of-url)

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
<span id="post-76230-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76230-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76230-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When attempting to include the marker in the URL when sharing a place, the marker is not part of the URL - toggling the feature does not change the URL.</p>
<p>Example: I want to share this place and have the marker included, but it wil not show up: <a href="https://www.openstreetmap.org/?mlat=51.02752&amp;mlon=3.70422#map=18/51.02752/3.70422">https://www.openstreetmap.org/?mlat=51.02752&amp;mlon=3.70422#map=18/51.02752/3.70422</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Aug '20, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/65b0b75df78357759b46b53c77742902?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexander%20duytschaever&#39;s gravatar image" />
<p><span>alexander du...</span><br />
<span class="score" title="20 reputation points">20</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexander duytschaever has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76230" class="comments-container">
<span id="76233"></span>
<div id="comment-76233" class="comment">
<div id="post-76233-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am not sure I understand the problem. When I click on your link, I get a map with a blue marker in the centre.</p>
</div>
<div id="comment-76233-info" class="comment-info">
<span class="comment-age">(20 Aug '20, 10:26)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="76234"></span>
<div id="comment-76234" class="comment">
<div id="post-76234-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah indeed...</p>
<p>There is something strange happening: I bookmarked such a link and when opening the bookmark the marker does not appear, that's what makes me wonder whether someone else would see the marker - when you look at the URL there is no information of a possible marker, only a lat/long.</p>
<p>Also, when opening the Share panel, the marker can be shown/hidden just by (un)checking "Include marker", which makes me suspect that users with an OSM account could see a different behaviour from users without an account (and just receive the URL).</p>
<p>Here is another example: <a href="https://www.openstreetmap.org/#map=19/51.02877/3.71016&amp;layers=C">https://www.openstreetmap.org/#map=19/51.02877/3.71016&amp;layers=C</a> - this is the URL in a bookmark; the marker does not show up. When I enable the "Include marker" checkbox, all these bookmarks now show the marker. As far as I know, that checkbox is not set by default, so I wonder if a user without an OSM account will see the marker (even if that's the purpose of the checkbox).</p>
<p>Here is another example: in this URL I did not activate the marker option: <a href="https://www.openstreetmap.org/#map=19/51.02899/3.71075&amp;layers=C">https://www.openstreetmap.org/#map=19/51.02899/3.71075&amp;layers=C</a> as far as I can see , there is NO difference in the URL and I bet you will see the bookmark although I did not enable it.</p>
</div>
<div id="comment-76234-info" class="comment-info">
<span class="comment-age">(20 Aug '20, 10:56)</span> <span class="comment-user userinfo">alexander du...</span>
</div>
</div>
<span id="76236"></span>
<div id="comment-76236" class="comment">
<div id="post-76236-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I was about to say that, your last two examples do not show any marker for me as they do not include mlat and mlon, unlike the first one you posted. As far as I know it does not matter if you have an OSM account or are logged in.</p>
</div>
<div id="comment-76236-info" class="comment-info">
<span class="comment-age">(20 Aug '20, 11:11)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-76230" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76230-form-container" class="comment-form-container">
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

<span id="76235"></span>

<div id="answer-container-76235" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76235-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Update: I see the difference - mlat/mlon has been added.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Aug '20, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/65b0b75df78357759b46b53c77742902?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexander%20duytschaever&#39;s gravatar image" />
<p><span>alexander du...</span><br />
<span class="score" title="20 reputation points">20</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexander duytschaever has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Aug '20, 11:03</strong> </span></p>
</div>
</div>
<div id="comments-container-76235" class="comments-container">
&#10;</div>
<div id="comment-tools-76235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76235-form-container" class="comment-form-container">
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

