+++
type = "question"
title = "Is there a way to get a timezone from a city or town via the API?"
description = '''Is there an API endpoint that would retrieve a timezone passing the name of a city or town as a parameter? While not all cities or towns have unique names (a quick test would be to google for &quot;list of cities with name Paris&quot;), depending on the API call result, one could easily work around that.'''
date = "2020-02-11T11:10:00Z"
lastmod = "2020-02-14T22:19:00Z"
weight = 73007
keywords = [ "town", "timezone", "city" ]
aliases = [ "/questions/73007" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a way to get a timezone from a city or town via the API?](/questions/73007/is-there-a-way-to-get-a-timezone-from-a-city-or-town-via-the-api)

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
<span id="post-73007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73007-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there an API endpoint that would retrieve a timezone passing the name of a city or town as a parameter? While not all cities or towns have unique names (a quick test would be to google for "list of cities with name Paris"), depending on the API call result, one could easily work around that.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-town" rel="tag" title="see questions tagged &#39;town&#39;">town</span> <span class="post-tag tag-link-timezone" rel="tag" title="see questions tagged &#39;timezone&#39;">timezone</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '20, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/35917d467914e16b1c4a333ff3a559c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gtludwig&#39;s gravatar image" />
<p><span>gtludwig</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gtludwig has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73007" class="comments-container">
&#10;</div>
<div id="comment-tools-73007" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73007-form-container" class="comment-form-container">
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

<span id="73090"></span>

<div id="answer-container-73090" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73090-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-73090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Usually it's a two step process: convert address to coordinates (geocoding), lookup timezone using the coordinates. While <a href="https://nominatim.openstreetmap.org/">https://nominatim.openstreetmap.org/</a> can do the first part it doesn't have the data for the timezone. Well, technically it can be extracted from OSM data but it's complex and hard to maintain. <a href="https://github.com/evansiroky/timezone-boundary-builder">https://github.com/evansiroky/timezone-boundary-builder</a> does that. Then you only have the timezone name, the calculation what time it is in the city is also complex because you need to know if there's daylight saving time, whose rules differ from country to country. Not all APIs can handle coordinates in the ocean (<a href="https://en.wikipedia.org/wiki/Nautical_time).">https://en.wikipedia.org/wiki/Nautical_time).</a></p>
<p>There are a couple of businesses that offer timezone API, check <a href="https://stadiamaps.com/products/geospatial-apis/">https://stadiamaps.com/products/geospatial-apis/</a> , <a href="https://opencagedata.com/">https://opencagedata.com/</a> , <a href="https://timezonedb.com/references/get-time-zone">https://timezonedb.com/references/get-time-zone</a> , <a href="https://www.timeanddate.com/services/api/">https://www.timeanddate.com/services/api/</a></p>
<p>disclaimer: I work for opencagedata</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '20, 22:19</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-73090" class="comments-container">
&#10;</div>
<div id="comment-tools-73090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73090-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73051"></span>

<div id="answer-container-73051" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73051-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>No (if you mean an API provided by the OSMF or any of the "core" OSM services).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '20, 19:23</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-73051" class="comments-container">
&#10;</div>
<div id="comment-tools-73051" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73051-form-container" class="comment-form-container">
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

