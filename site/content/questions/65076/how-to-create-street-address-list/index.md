+++
type = "question"
title = "How to create Street Address List"
description = '''I can write an overpass turbo wizard query to find all the street addresses in my town. I would like to export the list as a csv file. Can anyone help?'''
date = "2018-08-02T10:07:00Z"
lastmod = "2018-08-02T11:07:00Z"
weight = 65076
keywords = [ "overpass-turbo" ]
aliases = [ "/questions/65076" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to create Street Address List](/questions/65076/how-to-create-street-address-list)

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
<span id="post-65076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65076-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I can write an overpass turbo wizard query to find all the street addresses in my town. I would like to export the list as a csv file. Can anyone help?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '18, 10:07</strong></p>
<img src="https://secure.gravatar.com/avatar/75cc9956f060892f585352e9011cd26e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alan01730&#39;s gravatar image" />
<p><span>Alan01730</span><br />
<span class="score" title="464 reputation points">464</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alan01730 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65076" class="comments-container">
&#10;</div>
<div id="comment-tools-65076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65076-form-container" class="comment-form-container">
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

<span id="65077"></span>

<div id="answer-container-65077" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65077-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass-API has a <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#CSV_output_mode">csv output mode</a>.</p>
<p>An setting like <code>[out:csv(::lat, ::lon, "addr:housenumber","addr:unit","addr:street","addr:postcode","addr:city")];</code> will request csv output with the fields there (empty values if a given OSM object does't have the tag).</p>
<p>You'd probably want to look through the data you are retrieving and include more tags than that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '18, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-65077" class="comments-container">
<span id="65079"></span>
<div id="comment-65079" class="comment">
<div id="post-65079-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Just as a clarification: OSM currently uses postal addresses in the addr:* tags, these may be in particular different from the concept of a "street address" particularly in that addr:city should refer to the postal city and not the actual administrative unit/place the address is located in.</p>
</div>
<div id="comment-65079-info" class="comment-info">
<span class="comment-age">(02 Aug '18, 11:07)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65077" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65077-form-container" class="comment-form-container">
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

