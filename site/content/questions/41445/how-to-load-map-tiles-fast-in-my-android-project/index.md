+++
type = "question"
title = "How to load map tiles fast in my android project ?"
description = '''In my app all thing work properly but map not loading.I have try both way offline and online but map not loading.  This is my android code :- MapView map = (MapView) findViewById(R.id.mapView);  map.setMultiTouchControls(true); map.setClickable(true); map.setMinZoomLevel(4); map.getController().setZ...'''
date = "2015-03-02T09:16:00Z"
lastmod = "2015-11-07T11:16:00Z"
weight = 41445
keywords = [ "mapquest", "map", "android", "osm" ]
aliases = [ "/questions/41445" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to load map tiles fast in my android project ?](/questions/41445/how-to-load-map-tiles-fast-in-my-android-project)

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
<span id="post-41445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41445-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my app all thing work properly but map not loading.I have try both way offline and online but map not loading.</p>
<p>This is my android code :-</p>
<pre><code>MapView map = (MapView) findViewById(R.id.mapView); 
map.setMultiTouchControls(true);
map.setClickable(true);
map.setMinZoomLevel(4);
map.getController().setZoom(13);
map.setUseDataConnection(false);
map.setTileSource(TileSourceFactory.MAPQUESTOSM);</code></pre>
<p>I have used <strong>osmdroid-android-4.2.jar, slf4j-android-1.5.8.jar, and OSMBonusPack</strong>. for creating map and map functionality.</p>
<p><strong>And also the tile loading is very 'blocky' and not load</strong></p>
<p>How to load fast map or tile in my android project ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapquest" rel="tag" title="see questions tagged &#39;mapquest&#39;">mapquest</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '15, 09:16</strong></p>
<img src="https://secure.gravatar.com/avatar/6ce327f00b711d021de7bb7928fc5c57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nehalkumar&#39;s gravatar image" />
<p><span>nehalkumar</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nehalkumar has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Mar '15, 06:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-41445" class="comments-container">
<span id="41449"></span>
<div id="comment-41449" class="comment">
<div id="post-41449-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Does the problem persist when switching to a different tile provider? At the moment you seem to be using MapQuest Open.</p>
</div>
<div id="comment-41449-info" class="comment-info">
<span class="comment-age">(02 Mar '15, 11:46)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41445" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41445-form-container" class="comment-form-container">
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

<span id="41550"></span>

<div id="answer-container-41550" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41550-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello there! Wrong party. Try the issue queue for OSMdroid <a href="https://github.com/osmdroid/osmdroid/issues">https://github.com/osmdroid/osmdroid/issues</a></p>
<p>This help forum is all about the OpenStreetMap.org mapping project but not any software you might use to create maps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '15, 16:43</strong></p>
<img src="https://secure.gravatar.com/avatar/5498db8238237d97bf8c2ae2c437f673?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lxbarth&#39;s gravatar image" />
<p><span>lxbarth</span><br />
<span class="score" title="25 reputation points">25</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lxbarth has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '15, 16:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-41550" class="comments-container">
&#10;</div>
<div id="comment-tools-41550" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41550-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46444"></span>

<div id="answer-container-46444" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46444-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-46444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are using map only for marker display purpose use lite map special feature by google map <a href="https://developers.google.com/maps/documentation/android-api/lite">Lite Mode</a></p>
<pre><code>&lt;fragment xmlns:android=&quot;http://schemas.android.com/apk/res/android&quot;
xmlns:map=&quot;http://schemas.android.com/apk/res-auto&quot;
android:name=&quot;com.google.android.gms.maps.MapFragment&quot;
android:id=&quot;@+id/map&quot;
android:layout_width=&quot;match_parent&quot;
android:layout_height=&quot;match_parent&quot;
map:cameraZoom=&quot;13&quot;
map:mapType=&quot;normal&quot;
map:liteMode=&quot;true&quot;/&gt;</code></pre>
<p><strong>map:liteMode="true"</strong> it will make map in lite mode with some <a href="https://support.google.com/maps/answer/3031966?hl=en">limitation</a><br />
AND<br />
For too many marker go with clustering of marker <a href="https://developers.google.com/maps/articles/toomanymarkers?csw=1#markerclusterer">google link</a><br />
clustering will increase readability of map <strong>BEFORE CLUSTER</strong><br />
</p>
<p><span><img src="//i.stack.imgur.com/0rVt5.png" alt="enter image description here" /></span><br />
<strong>AFTER CLUSTER</strong> <span><img src="//i.stack.imgur.com/N5toq.png" alt="enter image description here" /></span></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '15, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/5ae58d49f1080c18402d5ea2a4092f6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tiwari9773&#39;s gravatar image" />
<p><span>tiwari9773</span><br />
<span class="score" title="-2 reputation points">-2</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tiwari9773 has no accepted answers">0%</span> </br></br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Nov '15, 12:46</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></br></p>
</img>
</div>
</div>
<div id="comments-container-46444" class="comments-container">
&#10;</div>
<div id="comment-tools-46444" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46444-form-container" class="comment-form-container">
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

