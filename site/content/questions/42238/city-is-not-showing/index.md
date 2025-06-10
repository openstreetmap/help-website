+++
type = "question"
title = "City is not showing"
description = '''I just used OSM to search for the lat long: 37.724917, -121.541556 However, the full address it returned didn&#x27;t have the city (Tracy) in it. How can I get the city?'''
date = "2015-04-10T04:57:00Z"
lastmod = "2015-04-25T18:40:00Z"
weight = 42238
keywords = [ "not_shown", "city", "latlng" ]
aliases = [ "/questions/42238" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [City is not showing](/questions/42238/city-is-not-showing)

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
<span id="post-42238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42238-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just used OSM to search for the lat long: 37.724917, -121.541556</p>
<p>However, the full address it returned didn't have the city (Tracy) in it.</p>
<p>How can I get the city?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not_shown" rel="tag" title="see questions tagged &#39;not_shown&#39;">not_shown</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-latlng" rel="tag" title="see questions tagged &#39;latlng&#39;">latlng</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '15, 04:57</strong></p>
<img src="https://secure.gravatar.com/avatar/ea853ac3cfdbea106b56cb8f6ba96b4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Franco%20L&#39;s gravatar image" />
<p><span>Franco L</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Franco L has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Apr '15, 12:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42238" class="comments-container">
<span id="42585"></span>
<div id="comment-42585" class="comment">
<div id="post-42585-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>convenience link: <a href="https://www.openstreetmap.org/search?query=37.724917%2C+-121.541556">https://www.openstreetmap.org/search?query=37.724917%2C+-121.541556</a> (I assume you mean this search by "used OSM to search")</p>
</div>
<div id="comment-42585-info" class="comment-info">
<span class="comment-age">(25 Apr '15, 12:37)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42238" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42238-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="42239"></span>

<div id="answer-container-42239" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42239-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Franco L has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I assume this is because Tracy is mapped as a <a href="http://www.openstreetmap.org/node/150936809">node</a> To fix this it has to be mapped as a boundary relation.</p>
<p>Similar questions have been asked in the past so you can search here, or maybe someone else will do it for you. (I'm too lazy to do it)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Apr '15, 06:28</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-42239" class="comments-container">
<span id="42247"></span>
<div id="comment-42247" class="comment">
<div id="post-42247-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Although you should leave the node in place and include it in the boundary relation. It is helpful when someone wants to just navigate to the city if the node is place in the town centre.</p>
</div>
<div id="comment-42247-info" class="comment-info">
<span class="comment-age">(10 Apr '15, 14:25)</span> <span class="comment-user userinfo">trigpoint</span>
</div>
</div>
<span id="42586"></span>
<div id="comment-42586" class="comment">
<div id="post-42586-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10816/franco-l"></a><a href="http://help.openstreetmap.org/users/10816/franco-l">@Franco L</a>: for positions closer to the city centre Tracy is returned (you can test with "Where am I?"). I <em>guess</em> that position is too far away from the city centre to guess that it also belongs to the city. We often have the opposite problem, that Nominatim searches for the closest town, finds a node and uses it, although a particular place does not belong to this town. E.g. <a href="/questions/25364/">reverse-geocoding-picks-up-a-distant-housing-estate</a> . Update: not really... I found the boundary relation …</p>
</div>
<div id="comment-42586-info" class="comment-info">
<span class="comment-age">(25 Apr '15, 12:45)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42239" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42239-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42587"></span>

<div id="answer-container-42587" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42587-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See <a href="https://www.openstreetmap.org/relation/112385?mlat=37.724917&amp;mlon=-121.541556">https://www.openstreetmap.org/relation/112385?mlat=37.724917&amp;mlon=-121.541556</a> your position (marker) is outside the boundary of Tracy.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '15, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-42587" class="comments-container">
<span id="42588"></span>
<div id="comment-42588" class="comment">
<div id="post-42588-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>note: I <span>have</span> only added the node to the boundary relation and set outer roles and fixed the wikipedia tags – it was existing before.</p>
</div>
<div id="comment-42588-info" class="comment-info">
<span class="comment-age">(25 Apr '15, 13:02)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42592"></span>
<div id="comment-42592" class="comment">
<div id="post-42592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the help!</p>
</div>
<div id="comment-42592-info" class="comment-info">
<span class="comment-age">(25 Apr '15, 18:40)</span> <span class="comment-user userinfo">Franco L</span>
</div>
</div>
</div>
<div id="comment-tools-42587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42587-form-container" class="comment-form-container">
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

