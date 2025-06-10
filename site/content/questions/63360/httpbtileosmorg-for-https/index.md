+++
type = "question"
title = "http://b.tile.osm.org/ for https"
description = '''Hi I&#x27;ve noticed that https sites using http://b.tile.osm.org/ lose the green padlock for pages that include OSM maps. On Firefox, they show the black padlock+alert sign, and the message &quot;Warning: Connection is Not Secure&quot; Wouldn&#x27;t it be a good idea to move http://b.tile.osm.org/ to https://b.tile.os...'''
date = "2018-05-07T10:58:00Z"
lastmod = "2018-05-13T20:57:00Z"
weight = 63360
keywords = [ "padlock", "tiles", "security", "https" ]
aliases = [ "/questions/63360" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [http://b.tile.osm.org/ for https](/questions/63360/httpbtileosmorg-for-https)

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
<span id="post-63360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63360-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I've noticed that https sites using <a href="http://b.tile.osm.org/">http://b.tile.osm.org/</a> lose the green padlock for pages that include OSM maps. On Firefox, they show the black padlock+alert sign, and the message "<strong>Warning: Connection is Not Secure</strong>" Wouldn't it be a good idea to move <a href="http://b.tile.osm.org/">http://b.tile.osm.org/</a> to <a href="https://b.tile.osm.org/">https://b.tile.osm.org/</a> ? Or is there an alternative ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-padlock" rel="tag" title="see questions tagged &#39;padlock&#39;">padlock</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-security" rel="tag" title="see questions tagged &#39;security&#39;">security</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 May '18, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/c4098d5b6efd50677c532c14e2cbcbff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trevoh&#39;s gravatar image" />
<p><span>trevoh</span><br />
<span class="score" title="9 reputation points">9</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trevoh has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63360" class="comments-container">
&#10;</div>
<div id="comment-tools-63360" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63360-form-container" class="comment-form-container">
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

<span id="63363"></span>

<div id="answer-container-63363" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63363-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Stripping http from the source?</p>
<p>src='//b.tile.osm.org'</p>
<p>Let the browser determine the connection type.</p>
<h1 id="edit">Edit</h1>
<p>You'll have to host the JS files yourself to make the change. There are some tile providers that use SSL.</p>
<p>https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png</p>
<p>ESRI: <a href="https://esri.github.io/esri-leaflet/examples/basemap-with-labels.html">https://esri.github.io/esri-leaflet/examples/basemap-with-labels.html</a></p>
<p>MapQuest: <a href="https://otile2-s.mqcdn.com/tiles/1.0.0/map/%7Bz%7D/%7Bx%7D/%7By%7D.png">https://otile2-s.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 May '18, 14:25</strong></p>
<img src="https://secure.gravatar.com/avatar/7dc2ca85ad0fdecfb5c66a390b83180a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gfitz&#39;s gravatar image" />
<p><span>gfitz</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gfitz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 May '18, 00:24</strong> </span></p>
</div>
</div>
<div id="comments-container-63363" class="comments-container">
<span id="63365"></span>
<div id="comment-63365" class="comment">
<div id="post-63365-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Two reactions to gfitz</p>
<ol>
<li>Can't change the source when tiles are called by an external program such as <a href="https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.11/lib/OpenLayers.js">https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.11/lib/OpenLayers.js</a> not directly by website.</li>
</ol>
<p>And 2 Can anyone at osm do anything to get a valid certificate ? Which would be the best solution :)</p>
</div>
<div id="comment-63365-info" class="comment-info">
<span class="comment-age">(07 May '18, 14:38)</span> <span class="comment-user userinfo">trevoh</span>
</div>
</div>
<span id="63367"></span>
<div id="comment-63367" class="comment">
<div id="post-63367-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Check the second edit</p>
</div>
<div id="comment-63367-info" class="comment-info">
<span class="comment-age">(07 May '18, 15:20)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
<span id="63369"></span>
<div id="comment-63369" class="comment">
<div id="post-63369-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png makes the difference. It shows the green padlock, whereas http://{s}.tile.osm.org/{z}/{x}/{y}.png produces the insecure connection warning. Thanks</p>
</div>
<div id="comment-63369-info" class="comment-info">
<span class="comment-age">(07 May '18, 15:59)</span> <span class="comment-user userinfo">trevoh</span>
</div>
</div>
<span id="63370"></span>
<div id="comment-63370" class="comment">
<div id="post-63370-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You are welcome. Please mark as solved if it helped</p>
</div>
<div id="comment-63370-info" class="comment-info">
<span class="comment-age">(07 May '18, 16:09)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
</div>
<div id="comment-tools-63363" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63363-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63447"></span>

<div id="answer-container-63447" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63447-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63447-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63447-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="osm.org">osm.org</a> points to the same place as <a href="openstreetmap.org">openstreetmap.org</a> - it's always just been a shortcut to it. The certificates on those sites is for "(something).openstreetmap.org". If you have a look at the https certificate associated with a random tile such as "<a href="https://a.tile.osm.org/9/253/166.png">https://a.tile.osm.org/9/253/166.png</a>" you'll see that it is for "<a href="http://tile.openstreetmap.org">tile.openstreetmap.org</a>". Clearly this "doesn't match", so you end up with the browser warning.</p>
<p>Back when OpenStreetMap served http tiles no error would occur, though you'd get the same tiles as if you'd asked for <a href="http://b.tile.openstreetmap.org/.">http://b.tile.openstreetmap.org/.</a> Now the same tiles are served, but over https, and the certificate doesn't match.</p>
<p>The question, of course, is why is anything referring to <a href="http://b.tile.osm.org/">http://b.tile.osm.org/</a> in the first place? Presumably someone's defined a tile layer (in e.g. LeafLet or OpenLayers) using that, and it needs to be changed from "<a href="http://osm.org">osm.org</a>" to "<a href="http://openstreetmap.org">openstreetmap.org</a>". If you can let people know where you're getting this error they may be able to investigate further.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '18, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-63447" class="comments-container">
&#10;</div>
<div id="comment-tools-63447" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63447-form-container" class="comment-form-container">
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

