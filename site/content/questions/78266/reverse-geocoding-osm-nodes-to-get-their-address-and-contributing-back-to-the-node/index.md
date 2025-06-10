+++
type = "question"
title = "Reverse geocoding OSM nodes to get their address and contributing back to the node"
description = '''Hello, I would like to extract nodes from OpenStreetMap, but I noticed most of them are just lat lon pairs. I would like to reverse geocode them, possibly with Nominatim. Is there an API way to contrib back the reverse geocoded node data to the node?'''
date = "2021-01-07T17:44:00Z"
lastmod = "2021-01-07T21:28:00Z"
weight = 78266
keywords = [ "latlon", "nodes", "reversegeocoding", "geocoding", "api" ]
aliases = [ "/questions/78266" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reverse geocoding OSM nodes to get their address and contributing back to the node](/questions/78266/reverse-geocoding-osm-nodes-to-get-their-address-and-contributing-back-to-the-node)

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
<span id="post-78266-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78266-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78266-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I would like to extract nodes from OpenStreetMap, but I noticed most of them are just lat lon pairs.</p>
<p>I would like to reverse geocode them, possibly with Nominatim.</p>
<p>Is there an API way to contrib back the reverse geocoded node data to the node?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latlon" rel="tag" title="see questions tagged &#39;latlon&#39;">latlon</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jan '21, 17:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a10be9347637087d655e00a6e9d3655d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giorgio79&#39;s gravatar image" />
<p><span>giorgio79</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giorgio79 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78266" class="comments-container">
&#10;</div>
<div id="comment-tools-78266" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78266-form-container" class="comment-form-container">
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

<span id="78267"></span>

<div id="answer-container-78267" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78267-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78267-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78267-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That would be very bad. Don't do it. Nominatim will sometimes make "best guesses" when doing reverse geocoding, and these guesses must not be used to generate statements about reality and load them into the database. Also, if Nominatim is able to reverse geocode something that is good enough for us, we don't need that information replicated thousands of times with every node!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '21, 18:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-78267" class="comments-container">
<span id="78268"></span>
<div id="comment-78268" class="comment">
<div id="post-78268-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess we can reverse your answer, and ask why reverse geocode a node thousand of times when you can have the address in it once, and reject geocoding if address data exists. If address is a best guess, then it could be indicated.</p>
</div>
<div id="comment-78268-info" class="comment-info">
<span class="comment-age">(07 Jan '21, 18:22)</span> <span class="comment-user userinfo">giorgio79</span>
</div>
</div>
<span id="78269"></span>
<div id="comment-78269" class="comment">
<div id="post-78269-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Without admin boundaries Nominatim makes guesses based on distance which of the surrounding towns and postcode an address belongs to. There's many small flaws like if a road crosses state boundaries a house can get assigned to the wrong state. Such guessed data has no value to be added permanently.</p>
</div>
<div id="comment-78269-info" class="comment-info">
<span class="comment-age">(07 Jan '21, 21:28)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-78267" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78267-form-container" class="comment-form-container">
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

