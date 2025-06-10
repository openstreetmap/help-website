+++
type = "question"
title = "Openstreetmaps api for Java Platform/ Get congestion details from Traffic Message Channels"
description = '''Hi, I am developing a standalone application for traffic congestion analysis in java platform using maps. Can you please guide if there is a way to query your server to get congestion details of a particular traffic message channel (TMC) in a given location. Congestion details can be in terms of lik...'''
date = "2016-08-08T14:32:00Z"
lastmod = "2016-08-08T15:34:00Z"
weight = 51304
keywords = [ "usage", "traffic", "api", "java" ]
aliases = [ "/questions/51304" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Openstreetmaps api for Java Platform/ Get congestion details from Traffic Message Channels](/questions/51304/openstreetmaps-api-for-java-platform-get-congestion-details-from-traffic-message-channels)

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
<span id="post-51304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51304-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am developing a standalone application for traffic congestion analysis in java platform using maps. Can you please guide if there is a way to query your server to get congestion details of a particular traffic message channel (TMC) in a given location. Congestion details can be in terms of like average speed or color code of traffic severity. Please if you can provide information on this.</p>
<p>Also, Is there a user term agreement or similar that would describe permitted uses of your data…? Are there any restrictions on the use/storage of the data and images from your servers?</p>
<p>Appreciate your response.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Aug '16, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/1bf0c6b56abebe0b98300a30cadbd0f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Deep_Shank&#39;s gravatar image" />
<p><span>Deep_Shank</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Deep_Shank has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Aug '16, 19:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-51304" class="comments-container">
&#10;</div>
<div id="comment-tools-51304" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51304-form-container" class="comment-form-container">
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

<span id="51305"></span>

<div id="answer-container-51305" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51305-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap doesn't have dynamic data like current traffic flows. You will have to find other sources for this. Check out opentraffic.io which is still in its infancy but aims to provide what you are looking for.</p>
<p>Use of our data is governed by the Open Database License, see the <a href="http://wiki.osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ">FAQ on the OSMF wiki</a>. Our server API is intended for editing only; if you want to run live queries against a production machine, set up the production machine yourself and feed it with a planet import and differential updates.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '16, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-51305" class="comments-container">
&#10;</div>
<div id="comment-tools-51305" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51305-form-container" class="comment-form-container">
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

