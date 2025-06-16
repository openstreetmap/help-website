+++
type = "question"
title = "Share button"
description = '''Hello, I want to add a share button on the map. By clicking it user should able to share current map Image. Such functionality is already given at https://www.openstreetmap.org/#map=2/49.0/124.1. I want to do the same. Can I have small example? Thanks Hardik Pancholi'''
date = "2014-03-24T06:03:00Z"
lastmod = "2014-03-27T16:26:00Z"
weight = 31808
keywords = [ "leaflet", "openlayers", "permanentlink" ]
aliases = [ "/questions/31808" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Share button](/questions/31808/share-button)

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
<span id="post-31808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31808-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I want to add a share button on the map. By clicking it user should able to share current map Image. Such functionality is already given at <a href="https://www.openstreetmap.org/#map=2/49.0/124.1.">https://www.openstreetmap.org/#map=2/49.0/124.1.</a></p>
<p>I want to do the same. Can I have small example?</p>
<p>Thanks Hardik Pancholi</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-permanentlink" rel="tag" title="see questions tagged &#39;permanentlink&#39;">permanentlink</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Mar '14, 06:03</strong></p>
<img src="https://secure.gravatar.com/avatar/460c4bfb836a1948e956127c17005cf9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hardikpancholi85&#39;s gravatar image" />
<p><span>hardikpancho...</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hardikpancholi85 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Mar '14, 10:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-31808" class="comments-container">
&#10;</div>
<div id="comment-tools-31808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31808-form-container" class="comment-form-container">
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

<span id="31823"></span>

<div id="answer-container-31823" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31823-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31823-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31823-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are refering to what we call 'permalink'. This functionality is embedded in the particular webmap library you are using to display the interactive map. So there are different ways on how to enable this kind of functionality on the libs:</p>
<ul>
<li>Leaflet plugin <a href="https://github.com/shramov/leaflet-plugins">https://github.com/shramov/leaflet-plugins</a></li>
<li>OpenLayers <a href="http://openlayers.org/dev/examples/controls.html">http://openlayers.org/dev/examples/controls.html</a></li>
</ul>
<p>Then you just need a piece of JavaScript that triggers that functionality and returns an link wherever you want it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Mar '14, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-31823" class="comments-container">
<span id="31867"></span>
<div id="comment-31867" class="comment">
<div id="post-31867-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello,</p>
<p>You gave very nice example. Using <a href="http://openlayers.org/dev/examples/controls.html">http://openlayers.org/dev/examples/controls.html</a> now I am able to add zooming pane. But in this example there isn't anything related to Share functionality. Can you give some specific example for share?</p>
<p>Thanks</p>
</div>
<div id="comment-31867-info" class="comment-info">
<span class="comment-age">(25 Mar '14, 03:30)</span> <span class="comment-user userinfo">hardikpancho...</span>
</div>
</div>
<span id="31892"></span>
<div id="comment-31892" class="comment">
<div id="post-31892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>click the "permalink" in the right bottom corner. The URL in your browser will change. It typically adds coordinates and depending on the application selected layers, etc. Copy the http-address from your browser's address bar, This is different UI from the Share button you see on OSM.org, but does basically the same.</p>
</div>
<div id="comment-31892-info" class="comment-info">
<span class="comment-age">(25 Mar '14, 16:05)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="31932"></span>
<div id="comment-31932" class="comment">
<div id="post-31932-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hello,</p>
<p>Sorry but I didn't get you. What I want to share functionality same as on <a href="https://www.openstreetmap.org/.">https://www.openstreetmap.org/.</a></p>
<p>In right side menu list there are list of functionality are there. I want to implement share functionality. It will be really good If I can have example.</p>
<p>Thanks</p>
</div>
<div id="comment-31932-info" class="comment-info">
<span class="comment-age">(27 Mar '14, 06:30)</span> <span class="comment-user userinfo">hardikpancho...</span>
</div>
</div>
<span id="31949"></span>
<div id="comment-31949" class="comment">
<div id="post-31949-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>perhaps look at the source code of the main page. All functionality is Javascript and can be examined through your browser. Or look at the source repository for the website (I don't have a link to that)</p>
</div>
<div id="comment-31949-info" class="comment-info">
<span class="comment-age">(27 Mar '14, 16:26)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-31823" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31823-form-container" class="comment-form-container">
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

