+++
type = "question"
title = "Need to get current location(road) is public or private"
description = '''I am a developer need to find if the truck is going on-road and off-road for waste management application. So that i need draw a route based on lat and lat. In that i need to find if traveled route(road) is public or private road. If it is possible to get details of route details in OSM or any other...'''
date = "2016-10-25T13:53:00Z"
lastmod = "2016-11-02T06:48:00Z"
weight = 52676
keywords = [ "be-on-road", "trucks" ]
aliases = [ "/questions/52676" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Need to get current location(road) is public or private](/questions/52676/need-to-get-current-locationroad-is-public-or-private)

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
<span id="post-52676-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52676-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52676-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am a developer need to find if the truck is going on-road and off-road for waste management application. So that i need draw a route based on lat and lat. In that i need to find if traveled route(road) is public or private road.</p>
<p>If it is possible to get details of route details in OSM or any other ways to do this. please suggest.Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-be-on-road" rel="tag" title="see questions tagged &#39;be-on-road&#39;">be-on-road</span> <span class="post-tag tag-link-trucks" rel="tag" title="see questions tagged &#39;trucks&#39;">trucks</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '16, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/91bd73cc77435c6bbd0785ec301aae3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ranjeet8530&#39;s gravatar image" />
<p><span>Ranjeet8530</span><br />
<span class="score" title="9 reputation points">9</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ranjeet8530 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52676" class="comments-container">
&#10;</div>
<div id="comment-tools-52676" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52676-form-container" class="comment-form-container">
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

<span id="52678"></span>

<div id="answer-container-52678" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52678-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will first have to match the GPX trace of the truck to the OSM street network. This is often called "map matching", and both well-known OSM routing engines Graphhopper and OSRM support it. You will want to install one of them on your system and load the relevant OSM data into it. Performing the map matching yields a sequence of graph edges (most likely) traversed by the vehicle, and you can then look at the properties of these edges to find out whether they are public or private roads.</p>
<p>NB not all routing engines/routing profiles will even route over private roads - a road marked private without explicit access for motor vehicles will often be ignored for routing. Also, before you even start, perhaps you should ensure that private roads are actually marked as such in OSM in the area you are interested in; otherwise you might as well not bother.</p>
<p>Last not least, remember that in executing this map matching, the resulting list of edges and the public/private information is a database derived from OpenStreetMap and hence subject to the ODbL share alike license, which depending on your exact use case may mean that you have to make the data available under the ODbL license, and make users aware that data comes from OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '16, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-52678" class="comments-container">
<span id="52783"></span>
<div id="comment-52783" class="comment">
<div id="post-52783-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am new to OSM map. I need to implement using javascript for web application Can you please suggest me. How do i start map matching any reference link API.</p>
</div>
<div id="comment-52783-info" class="comment-info">
<span class="comment-age">(02 Nov '16, 04:58)</span> <span class="comment-user userinfo">Ranjeet8530</span>
</div>
</div>
<span id="52787"></span>
<div id="comment-52787" class="comment">
<div id="post-52787-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>"OSM" is essentially just a big pile of data which people have written software to process.</p>
<p>I'd start by looking at previous questions here and elsewhere that mention "graph". You aren't going to find any magic javascript that will solve your problem without you understanding it; you'll have spend a little time understanding how OSM data is represented and how to process it first.</p>
</div>
<div id="comment-52787-info" class="comment-info">
<span class="comment-age">(02 Nov '16, 06:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52678-form-container" class="comment-form-container">
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

