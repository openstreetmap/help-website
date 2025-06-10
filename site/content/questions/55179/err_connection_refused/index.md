+++
type = "question"
title = "ERR_CONNECTION_REFUSED"
description = '''Hi, this evening i was accessing the RESTful webservice from Openstreetmap via this URL: http://nominatim.openstreetmap.org/search/%3CThe%20Open%20University%3E?format=json&amp;amp;countrycode=gb, after about 50 requests or so I ended up being given the ERR_CONNECTION_REFUSED from the server.  anyone go...'''
date = "2017-03-18T18:32:00Z"
lastmod = "2017-03-18T21:19:00Z"
weight = 55179
keywords = [ "nominatim" ]
aliases = [ "/questions/55179" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ERR_CONNECTION_REFUSED](/questions/55179/err_connection_refused)

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
<span id="post-55179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55179-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, this evening i was accessing the RESTful webservice from Openstreetmap via this URL: <a href="http://nominatim.openstreetmap.org/search/%3CThe%20Open%20University%3E?format=json&amp;countrycode=gb,">http://nominatim.openstreetmap.org/search/%3CThe%20Open%20University%3E?format=json&amp;countrycode=gb,</a> after about 50 requests or so I ended up being given the ERR_CONNECTION_REFUSED from the server.</p>
<p>anyone got a clue how long this lasts? working on a project :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Mar '17, 18:32</strong></p>
<img src="https://secure.gravatar.com/avatar/f1ae626f08909c18d0daa52b783ab8ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nyn&#39;s gravatar image" />
<p><span>nyn</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nyn has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '17, 08:12</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-55179" class="comments-container">
&#10;</div>
<div id="comment-tools-55179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55179-form-container" class="comment-form-container">
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

<span id="55180"></span>

<div id="answer-container-55180" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55180-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sounds like you were detected <a href="https://operations.osmfoundation.org/policies/nominatim/">violating their usage policy</a>, probably by exceeding one query per second. I don't know how long it will be before your IP will be allowed again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Mar '17, 21:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-55180" class="comments-container">
&#10;</div>
<div id="comment-tools-55180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55180-form-container" class="comment-form-container">
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

