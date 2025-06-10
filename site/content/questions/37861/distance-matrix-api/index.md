+++
type = "question"
title = "Distance matrix API"
description = '''Dears, could you please inform me if there are an Api that can give us the distance between A and B using API? Like Google Distance Matrix API. Thanks.'''
date = "2014-10-22T12:27:00Z"
lastmod = "2021-08-21T09:56:00Z"
weight = 37861
keywords = [ "distance", "api", "matrix" ]
aliases = [ "/questions/37861" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Distance matrix API](/questions/37861/distance-matrix-api)

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
<span id="post-37861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37861-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dears, could you please inform me if there are an Api that can give us the distance between A and B using API? Like Google Distance Matrix API.</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-matrix" rel="tag" title="see questions tagged &#39;matrix&#39;">matrix</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '14, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/8f603fcffa857bf61a6b4777de41d4e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Danil%20Rudakov&#39;s gravatar image" />
<p><span>Danil Rudakov</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Danil Rudakov has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-37861" class="comments-container">
<span id="43225"></span>
<div id="comment-43225" class="comment">
<div id="post-43225-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Someone asked a new question as an answer; that has been moved to <a href="https://help.openstreetmap.org/questions/43223/is-there-any-possibility-to-provide-coordinates-within-a-distancei-mean-defined-travel-time">https://help.openstreetmap.org/questions/43223/is-there-any-possibility-to-provide-coordinates-within-a-distancei-mean-defined-travel-time</a></p>
</div>
<div id="comment-43225-info" class="comment-info">
<span class="comment-age">(26 May '15, 14:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="81402"></span>
<div id="comment-81402" class="comment">
<div id="post-81402-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi guys,</p>
<p>I would like to do the same as the question ask, but is it free ?</p>
</div>
<div id="comment-81402-info" class="comment-info">
<span class="comment-age">(21 Aug '21, 09:56)</span> <span class="comment-user userinfo">hunae</span>
</div>
</div>
</div>
<div id="comment-tools-37861" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37861-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="37865"></span>

<div id="answer-container-37865" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37865-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-37865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, OSRM (Open Source Routing Machine) provides this feature - both for point-to-point queries and for matrices.</p>
<p>See <a href="https://github.com/Project-OSRM/osrm-backend/wiki/Server-api">https://github.com/Project-OSRM/osrm-backend/wiki/Server-api</a>. There is a public instance at router.project-osrm.org which is available for light usage within the terms of use (see the OSRM wiki). An example matrix call would be:</p>
<p><a href="http://router.project-osrm.org/table?loc=29.94,-90.11&amp;loc=30.44,-91.18&amp;loc=30.45,-91.22&amp;loc=30.42,-91.15">http://router.project-osrm.org/table?loc=29.94,-90.11&amp;loc=30.44,-91.18&amp;loc=30.45,-91.22&amp;loc=30.42,-91.15</a></p>
<p>If you have more significant needs, you can set up your own instance of OSRM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '14, 12:48</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Oct '14, 12:49</strong> </span></p>
</div>
</div>
<div id="comments-container-37865" class="comments-container">
<span id="76369"></span>
<div id="comment-76369" class="comment">
<div id="post-76369-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This sounds interesting, is this p2p only? How about for matrices, i.e. m2m? Also, is this using geo coords only? Is there support for addresses? Or a way to identify the geo coords for an address? Thank you...</p>
</div>
<div id="comment-76369-info" class="comment-info">
<span class="comment-age">(31 Aug '20, 15:27)</span> <span class="comment-user userinfo">mwpowelllde</span>
</div>
</div>
</div>
<div id="comment-tools-37865" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37865-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41933"></span>

<div id="answer-container-41933" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41933-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is also the <a href="https://graphhopper.com/#directions-api">GraphHopper Directions API</a> based on OSM data with a <a href="https://graphhopper.com/api/1/docs/matrix/">Matrix API</a> providing times and distances. (Note: I'm the author of GraphHopper)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Mar '15, 21:50</strong></p>
<img src="https://secure.gravatar.com/avatar/fec61c70a4cc98b1e84a5dfbde1e9a6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peatar&#39;s gravatar image" />
<p><span>peatar</span><br />
<span class="score" title="351 reputation points">351</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peatar has one accepted answer">8%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jun '16, 09:15</strong> </span></p>
</div>
</div>
<div id="comments-container-41933" class="comments-container">
&#10;</div>
<div id="comment-tools-41933" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41933-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50242"></span>

<div id="answer-container-50242" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50242-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Dislaimer: I work for iGeolise</p>
<p>The TravelTime API can be used to calculate the true distance from A to B (rather than as the crow flies) as well as calculating the travel time between the two points (plus lots more). Sign up for an <a href="http://www.traveltimeplatform.com/developers/">API key here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jun '16, 10:37</strong></p>
<img src="https://secure.gravatar.com/avatar/c1b700404b5c8214702cde7e22e6fe3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Louisa-maps&#39;s gravatar image" />
<p><span>Louisa-maps</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Louisa-maps has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50242" class="comments-container">
<span id="50243"></span>
<div id="comment-50243" class="comment">
<div id="post-50243-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is the map data based on OSM?</p>
</div>
<div id="comment-50243-info" class="comment-info">
<span class="comment-age">(16 Jun '16, 11:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-50242" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50242-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50516"></span>

<div id="answer-container-50516" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50516-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>as far as i found OSRM only provides a travel-time-matrix (although they call it distance matrix). if i am wrong, please post, because i am looking for distance matrices</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '16, 08:30</strong></p>
<img src="https://secure.gravatar.com/avatar/1d68ceedad9a00addf67556bd2175a5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gemerden&#39;s gravatar image" />
<p><span>gemerden</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gemerden has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50516" class="comments-container">
&#10;</div>
<div id="comment-tools-50516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50516-form-container" class="comment-form-container">
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

