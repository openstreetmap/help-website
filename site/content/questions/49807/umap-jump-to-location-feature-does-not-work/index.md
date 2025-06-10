+++
type = "question"
title = "Umap: Jump to location-feature does not work"
description = '''Hi. I am very satisfied with the features in the Umap-interface, but I cannot see how to jump to a specific address or location. The &quot;jump to location&quot;-button does nothing. Am I missing something? When I need to find the loaction of an address, I search in Google maps and compare the maps (Not very ...'''
date = "2016-05-23T14:36:00Z"
lastmod = "2022-10-01T00:03:00Z"
weight = 49807
keywords = [ "umap", "location" ]
aliases = [ "/questions/49807" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Umap: Jump to location-feature does not work](/questions/49807/umap-jump-to-location-feature-does-not-work)

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
<span id="post-49807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49807-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. I am very satisfied with the features in the Umap-interface, but I cannot see how to jump to a specific address or location. The "jump to location"-button does nothing. Am I missing something? When I need to find the loaction of an address, I search in Google maps and compare the maps (Not very practical :-) )</p>
<p>Best Regards Christoffer</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '16, 14:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0bbc822b68c4dec9d128df68fe631858?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="claubel&#39;s gravatar image" />
<p><span>claubel</span><br />
<span class="score" title="30 reputation points">30</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="claubel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49807" class="comments-container">
<span id="49808"></span>
<div id="comment-49808" class="comment">
<div id="post-49808-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you in https? Search has been refactored in the incoming version BTW.</p>
</div>
<div id="comment-49808-info" class="comment-info">
<span class="comment-age">(23 May '16, 21:59)</span> <span class="comment-user userinfo">ybon</span>
</div>
</div>
</div>
<div id="comment-tools-49807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49807-form-container" class="comment-form-container">
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

<span id="49814"></span>

<div id="answer-container-49814" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49814-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="claubel has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>(based on what ybon says:) in case you are accessing umap via https, then your browser might block the location search request to <a href="http://open.mapquestapi.com">http://open.mapquestapi.com</a> 's nominatim service which gets called by umap if you enter a search term into the small box (e.g. "London") and then hit enter. Try to access via http or <a href="https://support.mozilla.org/en-US/kb/mixed-content-blocking-firefox">disable the mixed content blocking</a> ("Click the shield icon Mixed Content Shield in the address bar, click Options and choose Disable protection for now."). At least this happens for me in current Firefox 46 on umap.openstreetmap.fr.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '16, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 May '16, 09:00</strong> </span></p>
</div>
</div>
<div id="comments-container-49814" class="comments-container">
<span id="49826"></span>
<div id="comment-49826" class="comment">
<div id="post-49826-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you very much. I am using Chrome, and it is absolutely correct: The default https access blocked the location search. I switched to http, and then it worked.</p>
<p>To be more accurate: I found out that I could pres the "shield icon" in the chrome address bar. That gives access to running scripts at the specifiv website.</p>
</div>
<div id="comment-49826-info" class="comment-info">
<span class="comment-age">(25 May '16, 09:02)</span> <span class="comment-user userinfo">claubel</span>
</div>
</div>
</div>
<div id="comment-tools-49814" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49814-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49813"></span>

<div id="answer-container-49813" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49813-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>very strange ... it works for me is easy write the name and the zoom is automatically...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '16, 15:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ea909f2d2dbc8d263c8bb2a0c3259217?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bubix&#39;s gravatar image" />
<p><span>bubix</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bubix has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49813" class="comments-container">
&#10;</div>
<div id="comment-tools-49813" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49813-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85773"></span>

<div id="answer-container-85773" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85773-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>hi, i have the same issue i have checked and the problem looks the umap iframe... it is not https and for this reason the browser doese not provide location</p>
<p>below the same map, the first from umap webiste, the second from share frame</p>
<p><a href="https://umap.openstreetmap.fr/it/map/architecture-around-me_814107#6/45.468/9.218">https://umap.openstreetmap.fr/it/map/architecture-around-me_814107#6/45.468/9.218</a></p>
<p><a href="http://u.osmfr.org/m/814107/">http://u.osmfr.org/m/814107/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Oct '22, 00:03</strong></p>
<img src="https://secure.gravatar.com/avatar/589cf0fabfa5d7c21123bb4a86a938b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="APagliuca&#39;s gravatar image" />
<p><span>APagliuca</span><br />
<span class="score" title="11 reputation points">11</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="APagliuca has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85773" class="comments-container">
&#10;</div>
<div id="comment-tools-85773" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85773-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81350"></span>

<div id="answer-container-81350" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81350-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-81350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In 2021 it doesn't work :(</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '21, 16:21</strong></p>
<img src="https://secure.gravatar.com/avatar/7e3a0d3dbb6c1cab3286de2ffc8acd95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Finster2308&#39;s gravatar image" />
<p><span>Finster2308</span><br />
<span class="score" title="8 reputation points">8</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Finster2308 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81350" class="comments-container">
&#10;</div>
<div id="comment-tools-81350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81350-form-container" class="comment-form-container">
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

