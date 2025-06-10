+++
type = "question"
title = "Nominatim with all tags"
description = '''Hi Is there a project which implements both geo-location and reverse geo-location but includes the full OpenStreetMap data and tags (as opposed to Nominatim which only uses some of the tags)? Thanks, Raz'''
date = "2014-06-15T09:50:00Z"
lastmod = "2014-09-15T18:26:00Z"
weight = 33976
keywords = [ "openstreetmap", "reversegeocoding", "nominatim", "geocoding" ]
aliases = [ "/questions/33976" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim with all tags](/questions/33976/nominatim-with-all-tags)

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
<span id="post-33976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33976-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>Is there a project which implements both geo-location and reverse geo-location but includes the full OpenStreetMap data and tags (as opposed to Nominatim which only uses some of the tags)?</p>
<p>Thanks, Raz</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jun '14, 09:50</strong></p>
<img src="https://secure.gravatar.com/avatar/84ebb95a07dd884e34f0170b07b1d652?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RazAlon&#39;s gravatar image" />
<p><span>RazAlon</span><br />
<span class="score" title="61 reputation points">61</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RazAlon has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33976" class="comments-container">
<span id="33977"></span>
<div id="comment-33977" class="comment">
<div id="post-33977-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can't you just run an additional query? The results always include the OSM ID, so it is easy to get all the tags using an additional query to the regular API.</p>
</div>
<div id="comment-33977-info" class="comment-info">
<span class="comment-age">(15 Jun '14, 09:56)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33978"></span>
<div id="comment-33978" class="comment">
<div id="post-33978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, that's a nice idea, I was just wondering of it was already implemented.</p>
</div>
<div id="comment-33978-info" class="comment-info">
<span class="comment-age">(15 Jun '14, 10:24)</span> <span class="comment-user userinfo">RazAlon</span>
</div>
</div>
</div>
<div id="comment-tools-33976" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33976-form-container" class="comment-form-container">
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

<span id="34003"></span>

<div id="answer-container-34003" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34003-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-34003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can take the ID returned by Nominatim to run a query against the API. However do <strong>not</strong> do that in an application that you plan to use productively, as the API is meant mainly for editing! If you have regular need for this kind of lookup, you can set up your own Nominatim database and modify it to return all tags instead of just selected ones.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '14, 14:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-34003" class="comments-container">
<span id="36851"></span>
<div id="comment-36851" class="comment">
<div id="post-36851-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have my own Nominatim instance and Nominatim database, but how would I go about modifying it to return all tags instead of just the default selected ones?</p>
<p>And if all tags are returned, does that mean all tags can be queried against in the search box?</p>
<p>Thanks</p>
</div>
<div id="comment-36851-info" class="comment-info">
<span class="comment-age">(15 Sep '14, 18:26)</span> <span class="comment-user userinfo">olearytd12</span>
</div>
</div>
</div>
<div id="comment-tools-34003" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34003-form-container" class="comment-form-container">
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

