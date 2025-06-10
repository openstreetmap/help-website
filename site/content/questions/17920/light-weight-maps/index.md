+++
type = "question"
title = "Light weight maps"
description = '''Hi OSM users, My need is to replace Google Maps in an application to an offline maps system. OSM sounds very interesting. The application does not need any detail maps. 500.000 (overview) and 50.000 (detail). Just sample values. The idea is to download map data with less information for a large area...'''
date = "2012-11-23T11:46:00Z"
lastmod = "2012-11-23T12:55:00Z"
weight = 17920
keywords = [ "map", "offline", "android", "light" ]
aliases = [ "/questions/17920" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Light weight maps](/questions/17920/light-weight-maps)

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
<span id="post-17920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17920-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi OSM users,</p>
<p>My need is to replace Google Maps in an application to an offline maps system. OSM sounds very interesting. The application does not need any detail maps. 500.000 (overview) and 50.000 (detail). Just sample values.</p>
<p>The idea is to download map data with less information for a large area. Let say Scandinavia.</p>
<p>As a complete newbie I need to know if this is possible or if I should look in another direction.</p>
<p>Thanks very much in advanced for any information.</p>
<p>Best regards Stephan Cassel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-light" rel="tag" title="see questions tagged &#39;light&#39;">light</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Nov '12, 11:46</strong></p>
<img src="https://secure.gravatar.com/avatar/df5ec1f0f23088b471dcd8c5b7f1af9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SCassel&#39;s gravatar image" />
<p><span>SCassel</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SCassel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Nov '12, 11:49</strong> </span></p>
</div>
</div>
<div id="comments-container-17920" class="comments-container">
&#10;</div>
<div id="comment-tools-17920" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17920-form-container" class="comment-form-container">
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

<span id="17921"></span>

<div id="answer-container-17921" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17921-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SCassel has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For offline use, you´ll need to prerender all the tiles in your desired area. Note that the higher the zoom, the more space you will need to save the tiles. See <a href="http://switch2osm.org/">switch2osm</a> website for an explanation of what tiles are and how to build a dynamic tile server. Then you can just render all the tiles you need, and save them for offline use. Alternatively, you can ask a third-party osm provider like <a href="http://mapbox.com">mapbox</a> to render your tiles, or use a tool like <a href="http://mapbox.com/tilemill/">tillemill</a>.</p>
<p>Once you have your tiles, display them using <a href="http://leafletjs.com/">Leaflet</a>, <a href="http://openlayers.org/">OpenLayers</a>, or some native code in your app.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '12, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-17921" class="comments-container">
<span id="17924"></span>
<div id="comment-17924" class="comment">
<div id="post-17924-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks Vincent for valuable information Br Stephan</p>
</div>
<div id="comment-17924-info" class="comment-info">
<span class="comment-age">(23 Nov '12, 12:55)</span> <span class="comment-user userinfo">SCassel</span>
</div>
</div>
</div>
<div id="comment-tools-17921" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17921-form-container" class="comment-form-container">
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

