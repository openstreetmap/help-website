+++
type = "question"
title = "User can select neighborhood data through a suggestion box"
description = '''Hi, I am building an app that needs an user to select a preferred neighborhood in US through a suggestion box. Most likely we are NOT going to use maps. From this selection I need a geo location using which my searches will be executed. By default to start with I will retrieve user&#x27;s current locatio...'''
date = "2012-03-17T11:19:00Z"
lastmod = "2012-03-17T14:27:00Z"
weight = 11269
keywords = [ "geolocation", "neighborhood", "suggestion" ]
aliases = [ "/questions/11269" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [User can select neighborhood data through a suggestion box](/questions/11269/user-can-select-neighborhood-data-through-a-suggestion-box)

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
<span id="post-11269-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11269-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11269-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am building an app that needs an user to select a preferred neighborhood in US through a suggestion box. Most likely we are NOT going to use maps. From this selection I need a geo location using which my searches will be executed.</p>
<p>By default to start with I will retrieve user's current location through geo location api and will need to fetch a corresponding address from OSM using this location. In absence of geo location I will use ip based location / address detection.</p>
<p>Can I achieve this with some OSM api or even a data set available (preferred). We are inclined to use lucene's geo spatial searches to achieve this.</p>
<p>Any help will be highly appreciated.</p>
<p>thanks..</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geolocation" rel="tag" title="see questions tagged &#39;geolocation&#39;">geolocation</span> <span class="post-tag tag-link-neighborhood" rel="tag" title="see questions tagged &#39;neighborhood&#39;">neighborhood</span> <span class="post-tag tag-link-suggestion" rel="tag" title="see questions tagged &#39;suggestion&#39;">suggestion</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Mar '12, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/87df4a39429d20d2f6a1c2d2ba7b0ef9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jdevil&#39;s gravatar image" />
<p><span>jdevil</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jdevil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11269" class="comments-container">
&#10;</div>
<div id="comment-tools-11269" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11269-form-container" class="comment-form-container">
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

<span id="11271"></span>

<div id="answer-container-11271" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11271-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11271-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11271-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can try <a href="https://wiki.openstreetmap.org/wiki/Nominatim">nominatim</a>. It is a software for geocoding and reverse geocoding in either xml or json formats. You can run your own instance or use the instances at OpenStreetMap or MapQuest depending on the trafic of your service.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '12, 14:27</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-11271" class="comments-container">
&#10;</div>
<div id="comment-tools-11271" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11271-form-container" class="comment-form-container">
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

