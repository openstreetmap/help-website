+++
type = "question"
title = "how to combine marker and popup?"
description = '''I show over lon/lat my position with a icon(PIN) on the map....and I want to add a little popup to the marker with some GeoInfo like City and Country....but if I add a normal popup (new OpenLayers.Popup) it only appears on the top left corner of the page, but I want it at my position or next to my i...'''
date = "2010-10-26T08:28:00Z"
lastmod = "2011-04-20T06:38:00Z"
weight = 1315
keywords = [ "marker", "popup", "openlayers", "icon" ]
aliases = [ "/questions/1315" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [how to combine marker and popup?](/questions/1315/how-to-combine-marker-and-popup)

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
<span id="post-1315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1315-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-1315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I show over lon/lat my position with a icon(PIN) on the map....and I want to add a little popup to the marker with some GeoInfo like City and Country....but if I add a normal popup (new OpenLayers.Popup) it only appears on the top left corner of the page, but I want it at my position or next to my icon(Pin) on the map.... can anyone help or tell me what is wrong with my code....</p>
<pre><code>//ADD LAYER MARKERS
var markers = new OpenLayers.Layer.Markers( &quot;Markers&quot; );
    map.addLayer(markers);
    markers.addMarker(new OpenLayers.Marker(lonLat,icon));
&#10;//POPUP
var popup = new OpenLayers.Popup(&quot;test1&quot;,
                             markers.lonLat,
                             null,
                            &quot;GeoInfo&quot;,
                             true);
                  map.addPopup(popup);</code></pre>
<p>like I said it only appears in the TOP LEFT Corner of the map.....and if I change markers.lonLat to new Openlayers.LonLat(5,40) no popup is shown....</p>
<p>and if I change new.Openlayers.Popup to new.Openlayers.Popup.AnchoredBubble oder new.Openlayers.Popup.Anchored no PopUp appers as well :(</p>
<p>Any ideas?!?!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-popup" rel="tag" title="see questions tagged &#39;popup&#39;">popup</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-icon" rel="tag" title="see questions tagged &#39;icon&#39;">icon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Oct '10, 08:28</strong></p>
<img src="https://secure.gravatar.com/avatar/fdbaeffe869eb3d5b5a0eecd14068b44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BabyPowder&#39;s gravatar image" />
<p><span>BabyPowder</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BabyPowder has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Oct '10, 11:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-1315" class="comments-container">
&#10;</div>
<div id="comment-tools-1315" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1315-form-container" class="comment-form-container">
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

<span id="4659"></span>

<div id="answer-container-4659" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4659-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I know that this is fairly old, but I thought I may as well answer it because it comes up a lot in general OpenLayers marker/popup searches quite a lot.</p>
<p>Create a method to add the marker (I use addMarkers) and then within that, create a variable reference to each marker, var marker = new OpenLayers.Marker(ll, etc), then call the .lonlat property of that variable, rather than the layer itself. That way you know you're getting the appropriate projection and all. You might also want to make the popup a child of the marker, so that you can reference each marker's popup easily in the future.</p>
<p>A nice example of popups can be seen here: <a href="http://openlayers.org/dev/examples/popupMatrix.html"></a><a href="http://openlayers.org/dev/examples/popupMatrix.html"></a><a href="http://openlayers.org/dev/examples/popupMatrix.html">http://openlayers.org/dev/examples/popupMatrix.html</a></p>
<p>Check out the source code. It provides a lot of examples, and approaches it a bit differently, although more effectively I feel.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '11, 06:38</strong></p>
<img src="https://secure.gravatar.com/avatar/220f58859dd94d9b4c9026e81c5b5cb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mricci&#39;s gravatar image" />
<p><span>mricci</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mricci has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4659" class="comments-container">
&#10;</div>
<div id="comment-tools-4659" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4659-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1319"></span>

<div id="answer-container-1319" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1319-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a help system for the OpenStreetMap project, but your question is quite a technical one regarding OpenLayers, which is an independent software project. If you don't get any other answers here, you would be better looking at the <a href="http://openlayers.org">OpenLayers</a> site for support queries.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '10, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-1319" class="comments-container">
&#10;</div>
<div id="comment-tools-1319" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1319-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1362"></span>

<div id="answer-container-1362" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1362-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1362-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-1362-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This can be closed.......</p>
<p>somehow I did nothing different in my eyes but today exactly what I wanted to do worked for me.......</p>
<p>this thread can be closed</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Oct '10, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/fdbaeffe869eb3d5b5a0eecd14068b44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BabyPowder&#39;s gravatar image" />
<p><span>BabyPowder</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BabyPowder has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Oct '10, 13:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-1362" class="comments-container">
&#10;</div>
<div id="comment-tools-1362" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1362-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1320"></span>

<div id="answer-container-1320" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1320-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-1320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am using the OpenStreetMap so I thought that I can ask my question here......</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '10, 12:33</strong></p>
<img src="https://secure.gravatar.com/avatar/fdbaeffe869eb3d5b5a0eecd14068b44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BabyPowder&#39;s gravatar image" />
<p><span>BabyPowder</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BabyPowder has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1320" class="comments-container">
<span id="1321"></span>
<div id="comment-1321" class="comment">
<div id="post-1321-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can ask your question here, it's just more likely to get a helpful answer if you ask the people of OpenLayers.</p>
<p>However note that your code never makes a connection between the individual marker and the popup. You're somehow trying to couple the markers layer and the popup instead of the marker and the popup. See the OpenLayers examples page for working code.</p>
</div>
<div id="comment-1321-info" class="comment-info">
<span class="comment-age">(26 Oct '10, 12:55)</span> <span class="comment-user userinfo">Augustus Kling</span>
</div>
</div>
<span id="1324"></span>
<div id="comment-1324" class="comment">
<div id="post-1324-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Example 11 of <a href="http://php-baustelle.de/openlayers/step-by-step/">http://php-baustelle.de/openlayers/step-by-step/</a> might also provide some guidance. However you should rework the variable scope.</p>
</div>
<div id="comment-1324-info" class="comment-info">
<span class="comment-age">(27 Oct '10, 07:08)</span> <span class="comment-user userinfo">Augustus Kling</span>
</div>
</div>
</div>
<div id="comment-tools-1320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1320-form-container" class="comment-form-container">
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

