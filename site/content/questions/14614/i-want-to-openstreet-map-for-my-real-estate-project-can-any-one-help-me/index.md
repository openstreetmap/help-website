+++
type = "question"
title = "I want to openstreet map for my real estate project. Can any one help me..?"
description = '''I want to openstreet map for my real estate project. Can any one help me..? I&#x27;m new to this openstreet map. I want do proximity search, nearby search(hotels,Restaurants,hotels,shops, etc) to particular place and i want to show price of each property as a marker like in http://www.trulia.com/real_est...'''
date = "2012-07-26T13:31:00Z"
lastmod = "2013-02-08T13:41:00Z"
weight = 14614
keywords = [ "openstreetmap" ]
aliases = [ "/questions/14614" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [I want to openstreet map for my real estate project. Can any one help me..?](/questions/14614/i-want-to-openstreet-map-for-my-real-estate-project-can-any-one-help-me)

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
<span id="post-14614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14614-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to openstreet map for my real estate project. Can any one help me..? I'm new to this openstreet map. I want do proximity search, nearby search(hotels,Restaurants,hotels,shops, etc) to particular place and i want to show price of each property as a marker like in <a href="http://www.trulia.com/real_estate/New_York-New_York/">http://www.trulia.com/real_estate/New_York-New_York/</a> .. Is i need to buy any api from open street map to customize the map for my needs,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jul '12, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/954504ad2324b1cbc000a0ddc2c2ba1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pramod_ck&#39;s gravatar image" />
<p><span>pramod_ck</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pramod_ck has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14614" class="comments-container">
&#10;</div>
<div id="comment-tools-14614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14614-form-container" class="comment-form-container">
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

<span id="14615"></span>

<div id="answer-container-14615" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14615-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-14615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It sounds as if you might require more, and more customized, help than can be given in this forum. There's a list of professional consultants and service providers on the Wiki: <a href="http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services">http://wiki.openstreetmap.org/wiki/Commercial_OSM_Software_and_Services</a></p>
<p>You don't need to buy anything from OSM however you might have to do some things yourself. Remember, OpenStreetMap is mainly a provider of free data, not a provider of free computing resources. You will need</p>
<ul>
<li>a JavaScript library to display the map and markers on your page (e.g. free OpenLayers, free Leaflet)</li>
<li>a source for the map ("map tiles") to be displayed - if it's for a limited area only then you can make your own tiles, but for larger areas you'll want to either set up your own tile server or use a third-party tile server (free offerings from MapQuest Open, commercial offerings from MapBox and Geofabrik, among others)</li>
<li>a database filled with relevant OSM data to perform your proximity/nearby search (free MapQuest Open Nominatim service might do some but not all of what you need)</li>
<li>someone to write the code that glues it all together</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '12, 13:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '12, 13:50</strong> </span></p>
</div>
</div>
<div id="comments-container-14615" class="comments-container">
<span id="19753"></span>
<div id="comment-19753" class="comment">
<div id="post-19753-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also, OpenStreetMap does not contain data on what properties are for sale or their price.</p>
</div>
<div id="comment-19753-info" class="comment-info">
<span class="comment-age">(08 Feb '13, 13:41)</span> <span class="comment-user userinfo">LivingWithDr...</span>
</div>
</div>
</div>
<div id="comment-tools-14615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14615-form-container" class="comment-form-container">
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

