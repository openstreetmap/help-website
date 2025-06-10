+++
type = "question"
title = "To which level of data injected on a OSM can be retirved through API?"
description = '''Take e.g.  https://www.openstreetmap.org/#map=19/18.51160/73.87876 at various zoom levels; we keep getting more and more injected data on map; and at highest zoom level its not only facility or building names but even individual shop/facility in it with icons and even names like a coffee-shop, pharm...'''
date = "2023-01-29T09:55:00Z"
lastmod = "2023-01-29T10:00:00Z"
weight = 86580
keywords = [ "openstreetmap" ]
aliases = [ "/questions/86580" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [To which level of data injected on a OSM can be retirved through API?](/questions/86580/to-which-level-of-data-injected-on-a-osm-can-be-retirved-through-api)

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
<span id="post-86580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86580-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Take e.g. <a href="https://www.openstreetmap.org/#map=19/18.51160/73.87876">https://www.openstreetmap.org/#map=19/18.51160/73.87876</a></p>
<p>at various zoom levels; we keep getting more and more injected data on map; and at highest zoom level its not only facility or building names but even individual shop/facility in it with icons and even names like a coffee-shop, pharmacy, fabrics, restaurant/dining; religious places, optician, hospital. If data is available then it even goes to a level where it identifies individual amenities/facilities in apartment blocks.</p>
<p>Is there any way; all this data can be retrieved making use of API? If yes, some references will be more than appreciated.</p>
<p>Thanks in Advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '23, 09:55</strong></p>
<img src="https://secure.gravatar.com/avatar/b1f2c418c2795c8b17ccf8548e6042a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vijay_k&#39;s gravatar image" />
<p><span>vijay_k</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vijay_k has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86580" class="comments-container">
&#10;</div>
<div id="comment-tools-86580" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86580-form-container" class="comment-form-container">
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

<span id="86581"></span>

<div id="answer-container-86581" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86581-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-86581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The API on openstreetmap.org is the editing API and not suitable for bulk downloads or topical retrievals. To retrieve all OSM data go to planet.openstreetmap.org there are links to extract services for geographic regions linked on the page too.</p>
<p>If you want to retrieve specific data and don't want to filter it out of the previously mentioned complete data, using the overpass API is probably your best bet: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">https://wiki.openstreetmap.org/wiki/Overpass_API</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '23, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-86581" class="comments-container">
&#10;</div>
<div id="comment-tools-86581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86581-form-container" class="comment-form-container">
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

