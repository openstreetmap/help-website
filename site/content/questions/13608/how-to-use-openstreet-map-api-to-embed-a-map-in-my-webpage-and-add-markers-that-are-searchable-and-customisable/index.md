+++
type = "question"
title = "how to use openstreet map API to embed a map in my webpage and add markers that are searchable and customisable?"
description = '''Hello I am trying to use openstreetmap to embed a map in my webpage and add markers that are searchable and customisable. Is there an openstreetmap api to achieve this. I have been trying to find it for a long time but could not. '''
date = "2012-06-19T02:18:00Z"
lastmod = "2012-06-19T14:41:00Z"
weight = 13608
keywords = [ "api", "osm" ]
aliases = [ "/questions/13608" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to use openstreet map API to embed a map in my webpage and add markers that are searchable and customisable?](/questions/13608/how-to-use-openstreet-map-api-to-embed-a-map-in-my-webpage-and-add-markers-that-are-searchable-and-customisable)

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
<span id="post-13608-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13608-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13608-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello</p>
<p>I am trying to use openstreetmap to embed a map in my webpage and add markers that are searchable and customisable. Is there an openstreetmap api to achieve this. I have been trying to find it for a long time but could not.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '12, 02:18</strong></p>
<img src="https://secure.gravatar.com/avatar/e2a5920f142e0990758006633db064f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frensforall&#39;s gravatar image" />
<p><span>frensforall</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frensforall has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jul '13, 01:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-13608" class="comments-container">
&#10;</div>
<div id="comment-tools-13608" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13608-form-container" class="comment-form-container">
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

<span id="13612"></span>

<div id="answer-container-13612" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13612-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No. OpenStreetMap is not (and is not aiming to be) a drop-in replacement for something like Google Maps where you load one Javascript API and you get a ton of client-side and server-side features. What OpenStreetMap does is provide the data from which maps, or routing services, or geocoding services, can be built. Actually <em>operating</em> such services is not OSM's core mission, and neither is providing the Javascript that glues it all together. That's probably why you haven't found anything!</p>
<p>But don't despair, it can all be done. You will be using a Javascript library like OpenLayers or Leaflet to display the map and display markers. These libraries are powerful and will certainly allow you to display customized markers but some coding is required if you e.g. want them searchable. They are libraries, not ready-made toolboxes. There's also MapQuest's Open API (<a href="http://developer.mapquest.com/web/products/open/sdk)">http://developer.mapquest.com/web/products/open/sdk)</a> which perhaps comes closest to what you are looking for.</p>
<p>You will also need a tile server - either your own, or someone else's which you have permission to use - to load the map tiles from. The actual loading and displaying is done by the aforementioned library but map tiles don't fall from the sky, somebody has to produce them for you. The openstreetmap.org tile server is available for small-scale use; open.mapquest.com has a free tile server as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '12, 08:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-13612" class="comments-container">
<span id="13622"></span>
<div id="comment-13622" class="comment">
<div id="post-13622-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello</p>
<p>Thank you so much for all the information. could you point me how can i get one. I need a map of a certain place</p>
</div>
<div id="comment-13622-info" class="comment-info">
<span class="comment-age">(19 Jun '12, 14:41)</span> <span class="comment-user userinfo">frensforall</span>
</div>
</div>
</div>
<div id="comment-tools-13612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13612-form-container" class="comment-form-container">
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

