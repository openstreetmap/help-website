+++
type = "question"
title = "Do I need to use any third party services to implement OSM on my website?"
description = '''Hi, I need to create a static map with a marker on my web site and dynamic one with multiple markers and zoom/drag/put/remove marker capabilities. Is it necessary to use any third party services to implement OSM with all these functions on my website?    If yes :  What would be the cheapest and best...'''
date = "2018-06-29T16:22:00Z"
lastmod = "2018-07-04T23:11:00Z"
weight = 64445
keywords = [ "openstreetmap", "staticmap", "requests", "dynamic", "3rd_party" ]
aliases = [ "/questions/64445" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Do I need to use any third party services to implement OSM on my website?](/questions/64445/do-i-need-to-use-any-third-party-services-to-implement-osm-on-my-website)

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
<span id="post-64445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64445-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I need to create a static map with a marker on my web site and dynamic one with multiple markers and zoom/drag/put/remove marker capabilities.</p>
<p>Is it necessary to use any third party services to implement OSM with all these functions on my website?</p>
<ul>
<li><p>If yes : What would be the cheapest and best for commercial purposes? I need to make around a million requests to maps API per month.</p></li>
<li><p>If not : Could you please provide a link to a tutorial or documentation of OSM with instruction on how to use static and dynamic map on my website?</p></li>
</ul>
<p>I would really appreciate your help. Thank you in advance!</p>
<p>Looking forward to hearing from you.</p>
<p>Best, Nikita</p>
<p>Related Question: <a href="/questions/64437/is-there-a-request-limit-for-static-maps?">https://help.openstreetmap.org/questions/64437/is-there-a-request-limit-for-static-maps?</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-staticmap" rel="tag" title="see questions tagged &#39;staticmap&#39;">staticmap</span> <span class="post-tag tag-link-requests" rel="tag" title="see questions tagged &#39;requests&#39;">requests</span> <span class="post-tag tag-link-dynamic" rel="tag" title="see questions tagged &#39;dynamic&#39;">dynamic</span> <span class="post-tag tag-link-3rd_party" rel="tag" title="see questions tagged &#39;3rd_party&#39;">3rd_party</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jun '18, 16:22</strong></p>
<img src="https://secure.gravatar.com/avatar/5a8b5e73f79dacc67f289a47f187b4d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nikita_And&#39;s gravatar image" />
<p><span>Nikita_And</span><br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nikita_And has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64445" class="comments-container">
&#10;</div>
<div id="comment-tools-64445" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64445-form-container" class="comment-form-container">
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

<span id="64447"></span>

<div id="answer-container-64447" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64447-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-64447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can implement a dynamic ("slippy") map using a suitable Javascript library like Leaflet or OpenLayers without any third-party services.</p>
<p>OpenStreetMap does not offer a static map feature, so you will have to employ a third-party service for that, or host a static map yourself (some disk space and PHP required, but Open Source implementations exist). Simple static map implementations are based on downloading tiles, so you'll still depend on OpenStreetMap tiles.</p>
<p>If you plan to make a lot of requests, you should consider producing your own tiles or paying someone for producing these tiles, so as not to overload the donation and volunteer operated OpenStreetMap infrastructure - especially if you are using OSM in a commercial context. "A million requests per month" qualifies as "a lot".</p>
<p>The web site switch2osm.org explains how to set up your own tile server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '18, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-64447" class="comments-container">
<span id="64449"></span>
<div id="comment-64449" class="comment">
<div id="post-64449-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much for the quick answer!</p>
<p>Could you please tell me, does it mean that Leaflet.js and OpenStreetMaps are completely free? Do they have any request limits?</p>
<p>Does it mean I can host a dynamic("slippy") map on my website with unlimited number of request?</p>
<p>Thank you!</p>
</div>
<div id="comment-64449-info" class="comment-info">
<span class="comment-age">(29 Jun '18, 17:02)</span> <span class="comment-user userinfo">Nikita_And</span>
</div>
</div>
<span id="64450"></span>
<div id="comment-64450" class="comment">
<div id="post-64450-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Leaflet and OpenLayers are just JavaScript libraries. You can download them and put the files in your web directory and never access a remote server again. They don't have request limits because they are just the code that displays tiles. The request limits come from the servers that <em>provide</em> tiles. If you produce the tiles yourself, with your own tile server, set up using open source software as outlined on switch2osm.org, then you can make as many requests as your server can handle. Only if you use servers run by other people will there be limits on how much you can use them.</p>
</div>
<div id="comment-64450-info" class="comment-info">
<span class="comment-age">(29 Jun '18, 17:15)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="64542"></span>
<div id="comment-64542" class="comment">
<div id="post-64542-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've not tried it, but in Leaflet there may be a way to disable all the zooming features. If you set the panning boundaries to the size of your map's frame it should effectively make it static.</p>
</div>
<div id="comment-64542-info" class="comment-info">
<span class="comment-age">(04 Jul '18, 23:11)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-64447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64447-form-container" class="comment-form-container">
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

