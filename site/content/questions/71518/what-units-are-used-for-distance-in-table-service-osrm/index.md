+++
type = "question"
title = "What units are used for distance in table service osrm?"
description = '''I&#x27;m working on sotring clinics by their distance from subway so I&#x27;m using osrm to get distance for car and for the pedestrian. But I&#x27;ve got lot&#x27;s of annomalies. For example: 55.786112, 49.124035 and 55.786462, 49.124303 (Kazan) Real distance lays between 56m and 210m, but osrm returns number 48,1354...'''
date = "2019-11-07T13:37:00Z"
lastmod = "2022-10-26T00:03:00Z"
weight = 71518
keywords = [ "osrm", "walking", "table", "car", "distance" ]
aliases = [ "/questions/71518" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What units are used for distance in table service osrm?](/questions/71518/what-units-are-used-for-distance-in-table-service-osrm)

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
<span id="post-71518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71518-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working on sotring clinics by their distance from subway so I'm using osrm to get distance for car and for the pedestrian. But I've got lot's of annomalies. For example: 55.786112, 49.124035 and 55.786462, 49.124303 (Kazan)</p>
<p>Real distance lays between 56m and 210m, but osrm returns number 48,135471 for car and 39,995274 for pedestrian. It can't be meters or km but what is it? And durations are also very strange. 101 and 27 seconds.</p>
<p>What's wrong here? Could you help me to get it?</p>
<p>Thank you for your attention.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-walking" rel="tag" title="see questions tagged &#39;walking&#39;">walking</span> <span class="post-tag tag-link-table" rel="tag" title="see questions tagged &#39;table&#39;">table</span> <span class="post-tag tag-link-car" rel="tag" title="see questions tagged &#39;car&#39;">car</span> <span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Nov '19, 13:37</strong></p>
<img src="https://secure.gravatar.com/avatar/0721514992891933009b1eb03a3f95c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Akusoff&#39;s gravatar image" />
<p><span>Akusoff</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Akusoff has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Nov '19, 13:39</strong> </span></p>
</div>
</div>
<div id="comments-container-71518" class="comments-container">
<span id="71519"></span>
<div id="comment-71519" class="comment">
<div id="post-71519-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Any URLs that you might have thought you had in your question are garbled. I suggest that you include:</p>
<p>o The locations in OSM that you're asking about (link to the URLs)</p>
<p>o Details about the OSRM instance that you are using. Is it public or private? What data is in it?</p>
</div>
<div id="comment-71519-info" class="comment-info">
<span class="comment-age">(07 Nov '19, 13:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71518-form-container" class="comment-form-container">
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

<span id="71523"></span>

<div id="answer-container-71523" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71523-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as i know, Unless there is a road or a footpath directly between two points the routing engines seem try use a way ( Path or road) that it close by and may leave a gap between point and the way. so distance will i think be not much use over very short distances. OSRM and Graphopper give reasonable distance measurements in KM over larger distances but do not seem to be useful for this case. But i may be incorrect! see this:-<a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_foot&amp;route=52.3284%2C-0.1772%3B52.3278%2C-0.1728">https://www.openstreetmap.org/directions?engine=fossgis_osrm_foot&amp;route=52.3284%2C-0.1772%3B52.3278%2C-0.1728</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '19, 20:31</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '19, 21:58</strong> </span></p>
</div>
</div>
<div id="comments-container-71523" class="comments-container">
&#10;</div>
<div id="comment-tools-71523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71523-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85995"></span>

<div id="answer-container-85995" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85995-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Distance is supplied in meters. Be sure you are supplying coordinates in long, lat format. This is required when using cUrl</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '22, 00:03</strong></p>
<img src="https://secure.gravatar.com/avatar/9d3d32106ccb9c98fbc2e0af850b8046?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bramyx&#39;s gravatar image" />
<p><span>Bramyx</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bramyx has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85995" class="comments-container">
&#10;</div>
<div id="comment-tools-85995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85995-form-container" class="comment-form-container">
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

