+++
type = "question"
title = "How to create map tiles from OpenStreetMap offline and display it on Android?"
description = '''What I want is to display a simple offline map using OpenStreetMap. I cannot find in the web the right tools to create map tiles and use it to display a map in Android. I have downloaded different resources but it seems that I don&#x27;t have any idea where to start. I want to integrate images from OpenS...'''
date = "2011-10-04T11:23:00Z"
lastmod = "2011-10-05T16:54:00Z"
weight = 8279
keywords = [ "openstreetmap", "tiles", "android" ]
aliases = [ "/questions/8279" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to create map tiles from OpenStreetMap offline and display it on Android?](/questions/8279/how-to-create-map-tiles-from-openstreetmap-offline-and-display-it-on-android)

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
<span id="post-8279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8279-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What I want is to display a simple offline map using OpenStreetMap. I cannot find in the web the right tools to create map tiles and use it to display a map in Android. I have downloaded different resources but it seems that I don't have any idea where to start. I want to integrate images from OpenStreetMap using JOSM but i don't know if I can use it on Android.</p>
<p>Can I use Mapnik? Your help will a great thank you.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '11, 11:23</strong></p>
<img src="https://secure.gravatar.com/avatar/8e0b172ef5f08ef5cd090db297d0b94f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lordzden&#39;s gravatar image" />
<p><span>lordzden</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lordzden has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>04 Oct '11, 12:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/b1d217a3a6e04cf4654372068beef20d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonas_&#39;s gravatar image" />
<p><span>Jonas_</span><br />
<span class="score" title="662 reputation points">662</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span></p>
</div>
</div>
<div id="comments-container-8279" class="comments-container">
&#10;</div>
<div id="comment-tools-8279" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8279-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="8280"></span>

<div id="answer-container-8280" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8280-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The easiest way I have found to generate tiles is using Maperative.</p>
<p>A quick outline of how to do this is:</p>
<ol>
<li>Go to the area you want downloaded in the map view.</li>
<li>Choose Map&gt;Download OSM Data, this may time out if your area is too big, in this case download an extract for your area and use something like osmosis to extract the bit you want.</li>
<li>It should now render your map using the default style, delete the web map from the sources list and change the style (Map&gt;Switch To Rules) if you want.</li>
<li>Choose Tools&gt;Generate Tiles</li>
<li>Now you have your tiles in the Tiles sub folder.</li>
</ol>
<p>Mapnik should also work but will be more complicated to set up, there are various guides for both programs on the internet. Getting the tiles to display nicely on android is a different problem which I don't have experience with.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Oct '11, 12:34</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb4d30bb6d40cf9b3644ff4f453e5bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quantumstate&#39;s gravatar image" />
<p><span>quantumstate</span><br />
<span class="score" title="455 reputation points">455</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quantumstate has 3 accepted answers">30%</span></p>
</div>
</div>
<div id="comments-container-8280" class="comments-container">
<span id="8281"></span>
<div id="comment-8281" class="comment">
<div id="post-8281-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thank for your answer. Please update if you have more ideas to impart.</p>
</div>
<div id="comment-8281-info" class="comment-info">
<span class="comment-age">(04 Oct '11, 14:55)</span> <span class="comment-user userinfo">lordzden</span>
</div>
</div>
</div>
<div id="comment-tools-8280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8280-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8307"></span>

<div id="answer-container-8307" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8307-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://wiki.openstreetmap.org/wiki/Osmand">OsmAnd</a> is an Android app that can display maps offline and has a Java-written tool called <a href="http://wiki.openstreetmap.org/wiki/OsmAndMapCreator">OsmAndMapCreator</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '11, 11:27</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-8307" class="comments-container">
<span id="8319"></span>
<div id="comment-8319" class="comment">
<div id="post-8319-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>also have a look ath the other question here:</p>
<p><a href="http://help.openstreetmap.org/questions/8238/tool-for-creating-vector-tiles">http://help.openstreetmap.org/questions/8238/tool-for-creating-vector-tiles</a></p>
</div>
<div id="comment-8319-info" class="comment-info">
<span class="comment-age">(05 Oct '11, 16:54)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-8307" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8307-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8295"></span>

<div id="answer-container-8295" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8295-score" class="post-score" title="current number of votes">
-4
</div>
<span id="post-8295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try "Locus" maps - quite a nice app. It can download certain region (rectangular, along the way, or whatever) for later use. Lot of settings.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '11, 07:22</strong></p>
<img src="https://secure.gravatar.com/avatar/33835f537aa80619d0ed9fc9c0431f7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Toofpic&#39;s gravatar image" />
<p><span>Toofpic</span><br />
<span class="score" title="-2 reputation points">-2</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Toofpic has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8295" class="comments-container">
<span id="8303"></span>
<div id="comment-8303" class="comment">
<div id="post-8303-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Please do not use Locus. The app puts too great a strain on OpenStreetMap's servers. Please only use maps that work with downloaded static vector data (e.g. Maperitive) or that have their own servers (e.g. Mapdroyd).</p>
</div>
<div id="comment-8303-info" class="comment-info">
<span class="comment-age">(05 Oct '11, 10:36)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="8304"></span>
<div id="comment-8304" class="comment">
<div id="post-8304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm careful with caching. There's still no good mobile internet plan here, .so most people have to t.hink about cashing. I don't cache i, thanksn high resolution. But I'll check the apps you recommended, thanks. Just like the locus functionality and it's ability to change how frequently the coords are checked. Helps keep battery alive when hiking</p>
</div>
<div id="comment-8304-info" class="comment-info">
<span class="comment-age">(05 Oct '11, 10:51)</span> <span class="comment-user userinfo">Toofpic</span>
</div>
</div>
</div>
<div id="comment-tools-8295" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8295-form-container" class="comment-form-container">
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

