+++
type = "question"
title = "Customised map w/ highway streets in Germany"
description = '''Hi all, I am an absolute beginner at OSM. As I&#x27;d like to visualize at all highways (Autobahn &amp;amp; Bundesfernstrassen) in Germany and add locations to see how close they are to the highways, I&#x27;m not sure how to proceed. Do I have to import a database onto OSM? How to proceed? Many thanks to whoever ...'''
date = "2018-04-10T10:58:00Z"
lastmod = "2018-04-11T22:11:00Z"
weight = 62964
keywords = [ "germany", "traffic", "location", "highway", "map" ]
aliases = [ "/questions/62964" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Customised map w/ highway streets in Germany](/questions/62964/customised-map-w-highway-streets-in-germany)

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
<span id="post-62964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62964-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am an absolute beginner at OSM. As I'd like to visualize at all highways (Autobahn &amp; Bundesfernstrassen) in Germany and add locations to see how close they are to the highways, I'm not sure how to proceed. Do I have to import a database onto OSM? How to proceed?</p>
<p>Many thanks to whoever is willing to help out :)</p>
<p>Best regards!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-germany" rel="tag" title="see questions tagged &#39;germany&#39;">germany</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Apr '18, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a1286aefe2a1f067a0423659e4b88e0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fmus5698&#39;s gravatar image" />
<p><span>fmus5698</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fmus5698 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-62964" class="comments-container">
<span id="62969"></span>
<div id="comment-62969" class="comment">
<div id="post-62969-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>explain more about your project. Which platform? Please clarify your goals: do you want to use OSM or do you want to contribute to OSM (something which is useful for many people)?</p>
</div>
<div id="comment-62969-info" class="comment-info">
<span class="comment-age">(10 Apr '18, 22:48)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="62971"></span>
<div id="comment-62971" class="comment">
<div id="post-62971-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Aseerel4c26,</p>
<p>Thanks for helping out! I'd like to use OSM for a study. There is no given platform, all I'd want to do is setting locations and measure how far they are away from German highways. I hoped to find a layer with highways on it and add the functionality of measuring distances.</p>
<p>Many thanks!</p>
</div>
<div id="comment-62971-info" class="comment-info">
<span class="comment-age">(11 Apr '18, 06:54)</span> <span class="comment-user userinfo">fmus5698</span>
</div>
</div>
<span id="62972"></span>
<div id="comment-62972" class="comment">
<div id="post-62972-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, okay, we are getting closer... :-) The good info: very likely this is possible to do with OSM, because our data is open.</p>
<p>More clarification to be able to guide you in the right direction:</p>
<p>Initially you write about a "map". Do you really want a map? I guess you are talking about measurement of many many locations and you do not want to do this by hand, correct? Likely you do not want a map, but do calculations and routing on the "highway" data.</p>
<p>Furthermore, is "distance" for you the distance of a straight line to the next "highway" location? Or is it a drivable route to it? Or is it a drivable route to the next intersection/connection point (Auffahrt) of a highway?</p>
</div>
<div id="comment-62972-info" class="comment-info">
<span class="comment-age">(11 Apr '18, 07:54)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="62974"></span>
<div id="comment-62974" class="comment">
<div id="post-62974-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Good to hear this should be possible:) Yes I imagined a map would help to visualize the data. At the same time, the data itself is important too. The locations would be set manually as they are not too many. The distance calculations should preferably go along real streets/ highways that means I'd need drivable routes. What should I do? Thanks a lot for your help Aseerel4c26!</p>
</div>
<div id="comment-62974-info" class="comment-info">
<span class="comment-age">(11 Apr '18, 08:12)</span> <span class="comment-user userinfo">fmus5698</span>
</div>
</div>
</div>
<div id="comment-tools-62964" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62964-form-container" class="comment-form-container">
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

<span id="62977"></span>

<div id="answer-container-62977" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62977-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62977-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-62977-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fmus5698 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe making a online map with markers and lines on top is enough for you? Try <a href="https://wiki.openstreetmap.org/wiki/UMap">https://wiki.openstreetmap.org/wiki/UMap</a> and its many options. You can select from many OSM-based map styles. I think routing is not possible there, but you can import routes via gpx files, for example. I guess importing geojson would work, too - if you can find a routing service which produces this format. To create gpx files with routes e.g. <a href="https://graphhopper.com/maps/?point=50.242594%2C8.717651&amp;point=50.287615%2C8.670611&amp;locale=de&amp;vehicle=car&amp;weighting=fastest&amp;elevation=true&amp;use_miles=false&amp;layer=TF%20Neighbourhood">https://graphhopper.com/maps/?point=50.242594%2C8.717651&amp;point=50.287615%2C8.670611&amp;locale=de&amp;vehicle=car&amp;weighting=fastest&amp;elevation=true&amp;use_miles=false&amp;layer=TF%20Neighbourhood</a> can help you. If you want to make your own/custom routing, see <a href="https://wiki.openstreetmap.org/wiki/Routing">https://wiki.openstreetmap.org/wiki/Routing</a> .</p>
<p>If you really want to make an own map (style) out of OSM data, see <a href="https://wiki.openstreetmap.org/wiki/Rendering">https://wiki.openstreetmap.org/wiki/Rendering</a> . This is not easy. To display maps plus markup in a browser, you can use <a href="https://wiki.openstreetmap.org/wiki/Leaflet">https://wiki.openstreetmap.org/wiki/Leaflet</a> .</p>
<p>All that software is free software - so you can adjust and use as you like for your purpose.</p>
<p>It could be that a GIS application like <a href="https://wiki.openstreetmap.org/wiki/QGIS">https://wiki.openstreetmap.org/wiki/QGIS</a> rather suits your needs.</p>
<p>General starting points for using OSM data are <a href="https://wiki.openstreetmap.org/wiki/Using_OpenStreetMap">https://wiki.openstreetmap.org/wiki/Using_OpenStreetMap</a> and <a href="https://wiki.openstreetmap.org/wiki/Use_OpenStreetMap">https://wiki.openstreetmap.org/wiki/Use_OpenStreetMap</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '18, 20:55</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Apr '18, 20:56</strong> </span></p>
</div>
</div>
<div id="comments-container-62977" class="comments-container">
<span id="62978"></span>
<div id="comment-62978" class="comment">
<div id="post-62978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot. I will try out your suggestions!</p>
</div>
<div id="comment-62978-info" class="comment-info">
<span class="comment-age">(11 Apr '18, 21:33)</span> <span class="comment-user userinfo">fmus5698</span>
</div>
</div>
<span id="62979"></span>
<div id="comment-62979" class="comment">
<div id="post-62979-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>fine! :) Please give feedback what you achieved and if you need more answers, please "unaccept" my answer.</p>
</div>
<div id="comment-62979-info" class="comment-info">
<span class="comment-age">(11 Apr '18, 22:11)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62977" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62977-form-container" class="comment-form-container">
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

