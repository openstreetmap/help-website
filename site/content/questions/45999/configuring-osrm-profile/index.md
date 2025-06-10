+++
type = "question"
title = "Configuring OSRM profile"
description = '''I was able to follow the OSRM instructions to extract, prepare and route OSM data for both North-America (Geofabric.de extract) as well as the full planet download from osm.org. For both I used the supplied car.lua profile. Now I am trying to modify the profile (and re-preocess the data) in order to...'''
date = "2015-10-19T21:11:00Z"
lastmod = "2015-12-03T18:51:00Z"
weight = 45999
keywords = [ "osrm", "configuration" ]
aliases = [ "/questions/45999" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Configuring OSRM profile](/questions/45999/configuring-osrm-profile)

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
<span id="post-45999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45999-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-45999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was able to follow the OSRM instructions to extract, prepare and route OSM data for both North-America (Geofabric.de extract) as well as the full planet download from osm.org. For both I used the supplied car.lua profile.</p>
<p>Now I am trying to modify the profile (and re-preocess the data) in order to assign a higher than normal cost to bridges, tunnels and ferries. I am having a hard time finding any instructions related to profile customization.</p>
<p>Any help is highly appreciated! Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-configuration" rel="tag" title="see questions tagged &#39;configuration&#39;">configuration</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '15, 21:11</strong></p>
<img src="https://secure.gravatar.com/avatar/11bcc4eeaac3d976a54cd94839f5ff99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="udoh&#39;s gravatar image" />
<p><span>udoh</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="udoh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45999" class="comments-container">
&#10;</div>
<div id="comment-tools-45999" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45999-form-container" class="comment-form-container">
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

<span id="46955"></span>

<div id="answer-container-46955" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46955-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-46955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You're right. Documentation on Profiles seemed to be missing ...so I've just created it! :</p>
<p><a href="https://github.com/Project-OSRM/osrm-backend/wiki/Profiles">https://github.com/Project-OSRM/osrm-backend/wiki/Profiles</a></p>
<p>I've only been playing with OSRM for a couple of days, so I'm not the most qualified person to be writing the documentation, but hopefully others will jump on this and expand the details.</p>
<p>I'm afraid it doesn't detail how to "assign higher than normal cost to bridges" (not yet) but it might give you some ideas.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '15, 18:11</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-46955" class="comments-container">
<span id="46959"></span>
<div id="comment-46959" class="comment">
<div id="post-46959-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you very much for your answer and for posting the profile instructions on the wiki!! At the moment I am still using the data prepared using the car.lua profile and I haven't looked into this for a while. This will definitely be helpful when I go back to reprocess with a customized profile. Thanks again!</p>
</div>
<div id="comment-46959-info" class="comment-info">
<span class="comment-age">(03 Dec '15, 18:51)</span> <span class="comment-user userinfo">udoh</span>
</div>
</div>
</div>
<div id="comment-tools-46955" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46955-form-container" class="comment-form-container">
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

