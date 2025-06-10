+++
type = "question"
title = "Search with geocoder photon not contains suggestions aeroports"
description = '''Hi ,is there a method to add list of airports to the suggestions for example in france . Thank you in advance.'''
date = "2022-05-09T14:39:00Z"
lastmod = "2022-05-10T10:00:00Z"
weight = 84419
keywords = [ "osrm", "photon", "geocoder" ]
aliases = [ "/questions/84419" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Search with geocoder photon not contains suggestions aeroports](/questions/84419/search-with-geocoder-photon-not-contains-suggestions-aeroports)

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
<span id="post-84419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84419-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi ,is there a method to add list of airports to the suggestions for example in france . Thank you in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-photon" rel="tag" title="see questions tagged &#39;photon&#39;">photon</span> <span class="post-tag tag-link-geocoder" rel="tag" title="see questions tagged &#39;geocoder&#39;">geocoder</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '22, 14:39</strong></p>
<img src="https://secure.gravatar.com/avatar/5f244e94fc71794965555f2b9313df34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aminali1991&#39;s gravatar image" />
<p><span>aminali1991</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aminali1991 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 May '22, 14:39</strong> </span></p>
</div>
</div>
<div id="comments-container-84419" class="comments-container">
&#10;</div>
<div id="comment-tools-84419" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84419-form-container" class="comment-form-container">
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

<span id="84426"></span>

<div id="answer-container-84426" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84426-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Airports are returned with the results, they just usually very low on the importance list. You can explicitly restrict the search to airports using the <code>osm_tag</code> parameter: <a href="https://photon.komoot.io/api?q=fra&amp;osm_tag=aeroway:aerodrome">https://photon.komoot.io/api?q=fra&amp;osm_tag=aeroway:aerodrome</a> You can use the <code>bbox</code> parameter to further restrict the results to a certain area like France.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 May '22, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-84426" class="comments-container">
&#10;</div>
<div id="comment-tools-84426" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84426-form-container" class="comment-form-container">
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

