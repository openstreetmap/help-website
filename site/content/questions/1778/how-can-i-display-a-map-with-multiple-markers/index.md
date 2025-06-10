+++
type = "question"
title = "How can I display a map with multiple markers?"
description = '''How can I create a multiple markers on openstreetmap? and how can I interact with them with ajax?'''
date = "2010-12-12T11:51:00Z"
lastmod = "2020-12-10T10:12:00Z"
weight = 1778
keywords = [ "marker", "love2020", "ajax", "multiple" ]
aliases = [ "/questions/1778" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How can I display a map with multiple markers?](/questions/1778/how-can-i-display-a-map-with-multiple-markers)

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
<span id="post-1778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1778-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-1778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
4
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How can I create a multiple markers on openstreetmap? and how can I interact with them with ajax?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-love2020" rel="tag" title="see questions tagged &#39;love2020&#39;">love2020</span> <span class="post-tag tag-link-ajax" rel="tag" title="see questions tagged &#39;ajax&#39;">ajax</span> <span class="post-tag tag-link-multiple" rel="tag" title="see questions tagged &#39;multiple&#39;">multiple</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '10, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/e9efbf5b26eb4a5b6d5ab52c13446288?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="godard59&#39;s gravatar image" />
<p><span>godard59</span><br />
<span class="score" title="106 reputation points">106</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="godard59 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Nov '20, 10:24</strong> </span></p>
</div>
</div>
<div id="comments-container-1778" class="comments-container">
&#10;</div>
<div id="comment-tools-1778" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1778-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="1822"></span>

<div id="answer-container-1822" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1822-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-1822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can't add multiple markers on the OpenStreetMap.org homepage. For point &amp; click solutions you might like <a href="http://wiki.openstreetmap.org/wiki/UMap">uMap</a>,<a href="http://geocommons.com/">geocommmons</a>, <a href="http://wiki.openstreetmap.org/wiki/StaticMap">StaticMap</a>, and others, but for more power and flexibility it's worth learning a few javascript tricks:</p>
<p>Check out: <a href="http://harrywood.co.uk/maps/examples/openlayers/marker-popups.view.html">this multiple markers example</a></p>
<ul>
<li>It uses the open source JavaScript library called OpenLayers (<a href="http://harrywood.co.uk/maps/examples/leaflet/marker-array.view.html">There's an equivalent example for leafletJS</a>)</li>
<li>The map is initialised with a basemap layer from the default OpenStreetMap tile server (other tileservers and alternative renderings of OpenStreetMap data are available)</li>
<li>It adds a 'Vector' layer, where the markers are defined.</li>
<li>It needs a <a href="http://funmap.co.uk/examples/openlayers/img/marker.png">marker image</a> file placed in a 'img' folder alongside</li>
<li>It adds three markers. If you were adding more, you might want to do this by defining an array first, and then looping through this as in <a href="http://harrywood.co.uk/maps/examples/openlayers/marker-array.view.html">this example</a></li>
<li>As an exampe of event handling, it detects the event of selecting the marker, and calls 'createPopup'</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '10, 14:39</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Dec '14, 00:19</strong> </span></p>
</div>
</div>
<div id="comments-container-1822" class="comments-container">
<span id="1833"></span>
<div id="comment-1833" class="comment">
<div id="post-1833-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you all, Harry I saw OpenLayers library I Like the example of the three marker, but i need add more. Can you give me an example how to integrate an array in this code ?, Or there is an example on OpenLayers library?</p>
</div>
<div id="comment-1833-info" class="comment-info">
<span class="comment-age">(16 Dec '10, 09:44)</span> <span class="comment-user userinfo">godard59</span>
</div>
</div>
<span id="3359"></span>
<div id="comment-3359" class="comment">
<div id="post-3359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How about you learn javascript or pay somebody to code it for you? Looping over an array in javascript is not really openstreetmap related.</p>
</div>
<div id="comment-3359-info" class="comment-info">
<span class="comment-age">(24 Feb '11, 18:12)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="36853"></span>
<div id="comment-36853" class="comment">
<div id="post-36853-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm updating my old answer here to link to 'uMap' as a newer point and click approach. Also linking my array looping example to answer godard69's question (4 years late!)</p>
</div>
<div id="comment-36853-info" class="comment-info">
<span class="comment-age">(15 Sep '14, 23:40)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
</div>
<div id="comment-tools-1822" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1822-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1779"></span>

<div id="answer-container-1779" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1779-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not yet possible for the slippy map on the front page. But you can check out <a href="http://www.openlayers.org/">OpenLayers</a> which is an open source javascript slippy map that you can deploy on your own site.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '10, 12:05</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Dec '10, 13:28</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span></p>
</div>
</div>
<div id="comments-container-1779" class="comments-container">
&#10;</div>
<div id="comment-tools-1779" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1779-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1817"></span>

<div id="answer-container-1817" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1817-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The short answer is that we don't provide a mechanism to do that directly on the web site, but that doing so isn't hard at all if you have a little web development experience (which it seems you do). All you need to do is use OpenLayers and use OSM as your background layer.</p>
<p>Here's a URL of a talk I prepared for State of the Map US 2010 (but never got to present), which will take you through the basics of web development using OSM:</p>
<p><a href="http://www.emacsen.net/osm/osm-web-tutorial.pdf"></a><a href="http://www.emacsen.net/osm/osm-web-tutorial.pdf"></a><a href="http://www.emacsen.net/osm/osm-web-tutorial.pdf">http://www.emacsen.net/osm/osm-web-tutorial.pdf</a></p>
<p>If you go through that presentation, you should hopefully have a good foundation on how to use OSM on your site.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '10, 11:49</strong></p>
<img src="https://secure.gravatar.com/avatar/5f2082b86cc50d63c05f33f55166df2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emacsen&#39;s gravatar image" />
<p><span>emacsen</span><br />
<span class="score" title="1191 reputation points"><span>1.2k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emacsen has 4 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-1817" class="comments-container">
&#10;</div>
<div id="comment-tools-1817" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1817-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77887"></span>

<div id="answer-container-77887" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77887-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-77887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>step 1 : save your coordinates as json or csv in somewhere and get that link</p>
<p>step 2 : use leaflet or some other library to write codes in html file</p>
<p>step 3 : by using ajax js with above link to fetch data</p>
<p>step 4 : use for loop in the data to do marking (marker in map) automatically</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '20, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/fba989d99dfe0896d7a2401975532200?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kathir_vibes&#39;s gravatar image" />
<p><span>kathir_vibes</span><br />
<span class="score" title="0 reputation points">0</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kathir_vibes has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77887" class="comments-container">
&#10;</div>
<div id="comment-tools-77887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77887-form-container" class="comment-form-container">
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

