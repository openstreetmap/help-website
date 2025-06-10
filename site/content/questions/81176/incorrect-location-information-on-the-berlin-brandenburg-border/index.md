+++
type = "question"
title = "Incorrect location information on the Berlin / Brandenburg border"
description = '''Hello, I noticed an incorrect place name or map display. When I click on the map, the tooltip for the marker shows me the location of Brandenburg for the following coordinates, even though the marker in Berlin is set on the map after the border has passed. lat: 52.63870540666738 lng: 13.390896320343...'''
date = "2021-08-03T08:24:00Z"
lastmod = "2021-08-03T11:24:00Z"
weight = 81176
keywords = [ "coordinate", "border", "nominatim", "osm", "berlin-brandenburg" ]
aliases = [ "/questions/81176" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Incorrect location information on the Berlin / Brandenburg border](/questions/81176/incorrect-location-information-on-the-berlin-brandenburg-border)

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
<span id="post-81176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81176-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I noticed an incorrect place name or map display. When I click on the map, the tooltip for the marker shows me the location of Brandenburg for the following coordinates, even though the marker in Berlin is set on the map after the border has passed.</p>
<p>lat: 52.63870540666738 lng: 13.390896320343018 52 ° 38 '19.3395' 'N. 13 ° 23 '27.2268' 'E.</p>
<p>This is a big problem for us because the information provided by our users to these coordinates is assigned to a wrong state and thus makes our data analysis incorrect. I don't know how we can correct the location information or whether it is perhaps an old border line. What should I do?</p>
<p>Many greetings Fredo</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-coordinate" rel="tag" title="see questions tagged &#39;coordinate&#39;">coordinate</span> <span class="post-tag tag-link-border" rel="tag" title="see questions tagged &#39;border&#39;">border</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-berlin-brandenburg" rel="tag" title="see questions tagged &#39;berlin-brandenburg&#39;">berlin-brandenburg</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '21, 08:24</strong></p>
<img src="https://secure.gravatar.com/avatar/8dac6063e4b3913efa6a535fe2775b6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pleppo&#39;s gravatar image" />
<p><span>Pleppo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pleppo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81176" class="comments-container">
&#10;</div>
<div id="comment-tools-81176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81176-form-container" class="comment-form-container">
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

<span id="81178"></span>

<div id="answer-container-81178" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81178-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim's reverse search algorithm looks for the nearest named map feature, but for the lookup of parent boundaries at the street associated with the map feature. It doesn't re-evaluate if the city, state, country is different, e.g. when the street crosses a boundary. I'm not saying that's correct, just describing the current logic. It's tracked at <a href="https://github.com/osm-search/Nominatim/issues/785">https://github.com/osm-search/Nominatim/issues/785</a></p>
<p><a href="https://nominatim.openstreetmap.org/ui/reverse.html?lat=52.63870540666738&amp;lon=13.39089632034301&amp;zoom=18">https://nominatim.openstreetmap.org/ui/reverse.html?lat=52.63870540666738&amp;lon=13.39089632034301&amp;zoom=18</a> returns "Kalktuffgelände am Tegeler Fließ, Mönchmühlenstraße, Musikerviertel, Schildow, Mönchmühle, Mühlenbecker Land, Oberhavel, Brandenburg, 16552, Germany" Looking at the address list <a href="https://nominatim.openstreetmap.org/ui/details.html?osmtype=R&amp;osmid=8143017&amp;class=leisure">https://nominatim.openstreetmap.org/ui/details.html?osmtype=R&amp;osmid=8143017&amp;class=leisure</a> we can see the associated street Mönchmühlenstraße (<a href="https://www.openstreetmap.org/way/30109060)">https://www.openstreetmap.org/way/30109060)</a> is across the border in Brandenburg. It's not a good match but there aren't other named streets closer by.</p>
<p>It makes sense to report the example at <a href="https://github.com/osm-search/Nominatim/issues/new/choose">https://github.com/osm-search/Nominatim/issues/new/choose</a> because maybe a nature reserve shouldn't be assigned a nearest road.</p>
<p>If you have control over the request sent to Nominatim you can try using the 'zoom' parameter. For example setting it to 5 (state level) will return Berlin. <a href="https://nominatim.openstreetmap.org/ui/reverse.html?lat=52.63870540666738&amp;lon=13.39089632034301&amp;zoom=5">https://nominatim.openstreetmap.org/ui/reverse.html?lat=52.63870540666738&amp;lon=13.39089632034301&amp;zoom=5</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '21, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-81178" class="comments-container">
<span id="81179"></span>
<div id="comment-81179" class="comment">
<div id="post-81179-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanx for the Information! :-)</p>
<p>Fredo</p>
</div>
<div id="comment-81179-info" class="comment-info">
<span class="comment-age">(03 Aug '21, 11:24)</span> <span class="comment-user userinfo">Pleppo</span>
</div>
</div>
</div>
<div id="comment-tools-81178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81178-form-container" class="comment-form-container">
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

