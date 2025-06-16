+++
type = "question"
title = "custom search map integration"
description = '''Hi,  I am working in a real estate site.If customer enters something in a text box, i need to display the openstreet map based on the user queries with markers (For reference: Like this) in a reference site they have done using google map. But client&#x27;s requirement is opensteet map. Where i needs to ...'''
date = "2012-05-21T06:18:00Z"
lastmod = "2012-05-21T13:39:00Z"
weight = 12830
keywords = [ "search", "newbie", "customization" ]
aliases = [ "/questions/12830" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [custom search map integration](/questions/12830/custom-search-map-integration)

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
<span id="post-12830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12830-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I am working in a real estate site.If customer enters something in a text box, i need to display the openstreet map based on the user queries with markers (For reference: <a href="http://www.trulia.com/for_sale/New_York,NY/10000-200000_price/x_map#for_sale/New_York,NY/13_zm/40.777594,40.845410,-74.041093,-73.857140_xy/10000-200000_price/x_map">Like this</a>) in a reference site they have done using google map. But client's requirement is opensteet map. Where i needs to start? Could you please someone can guide me through?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-customization" rel="tag" title="see questions tagged &#39;customization&#39;">customization</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '12, 06:18</strong></p>
<img src="https://secure.gravatar.com/avatar/e5d7a10853a60bd2257989437490cc74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raj&#39;s gravatar image" />
<p><span>Raj</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raj has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12830" class="comments-container">
&#10;</div>
<div id="comment-tools-12830" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12830-form-container" class="comment-form-container">
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

<span id="12832"></span>

<div id="answer-container-12832" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12832-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-12832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Raj has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need:</p>
<ul>
<li>a Javascript library like OpenLayers or Leaflet to display the map</li>
<li>a geocoding service like Nominatim to find the geo-coordinates for a given address</li>
<li>a tile server from which to load map tiles</li>
<li>a little glue coding that puts it all together (get address from user, send to Nominatim, create marker for position returned, display on map)</li>
</ul>
<p>For points 2 and 3 you will either be relying on a service provided by someone else (which may cost money and may be subject to certain usage restrictions) or you will be setting up your own server(s) (which may require considerable resources).</p>
<p>The <a href="http://www.switch2osm.org/">switch2osm.org</a> web site has good resources aimed at people looking for a Google maps replacement.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '12, 07:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '12, 07:49</strong> </span></p>
</div>
</div>
<div id="comments-container-12832" class="comments-container">
<span id="12845"></span>
<div id="comment-12845" class="comment">
<div id="post-12845-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>I tried to implement but i failed. Could you please post some sample code. I mean i don't know how to includes all together (1,2 and 3). Please help me out.</p>
</div>
<div id="comment-12845-info" class="comment-info">
<span class="comment-age">(21 May '12, 13:39)</span> <span class="comment-user userinfo">Raj</span>
</div>
</div>
</div>
<div id="comment-tools-12832" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12832-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12831"></span>

<div id="answer-container-12831" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12831-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-12831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A brief link for a start <a href="https://wiki.openstreetmap.org/wiki/Openlayers_POI_layer_example">https://wiki.openstreetmap.org/wiki/Openlayers_POI_layer_example</a> This is an example how to use OpenLayers to show POIs on top of a OpenStreetMap base map.</p>
<p>The next step is to get that locations from a database: <a href="https://wiki.openstreetmap.org/wiki/OpenLayers_Dynamic_POI">https://wiki.openstreetmap.org/wiki/OpenLayers_Dynamic_POI</a></p>
<p>Note that there are other frameworks too, for example <a href="http://leaflet.cloudmade.com/">Leaflet</a>. It could be even better suited, but I haven't yet used Leaflet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '12, 07:43</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-12831" class="comments-container">
&#10;</div>
<div id="comment-tools-12831" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12831-form-container" class="comment-form-container">
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

