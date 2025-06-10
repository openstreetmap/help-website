+++
type = "question"
title = "how to disable dragging,when reach top or bottom"
description = '''Hi to all, I am using Openstreetmap with leaflet. 1.In zoom level 1, There is some empty space in bottom &amp;amp; top, but horizontally map tiles are repeated. But my markers shown in a single map.(refer image1.png). Is there any option to show markers in all maps shown, or How to load or show a single...'''
date = "2015-07-29T08:04:00Z"
lastmod = "2015-08-24T12:03:00Z"
weight = 44498
keywords = [ "openstreetmap", "leaflet", "tiles", "dragging", "zoom" ]
aliases = [ "/questions/44498" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to disable dragging,when reach top or bottom](/questions/44498/how-to-disable-draggingwhen-reach-top-or-bottom)

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
<span id="post-44498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44498-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to all,</p>
<p>I am using Openstreetmap with leaflet.</p>
<p>1.In zoom level 1, There is some empty space in bottom &amp; top, but horizontally map tiles are repeated. But my markers shown in a single map.(refer <img src="http://help.openstreetmap.org/upfiles/image1_V2IGi1l.png" alt="alt text" />image1.png).</p>
<p>Is there any option to show markers in all maps shown, or How to load or show a single map?</p>
<p>2.In other zoom levels, i want to disable drag when reach bottom or top of the map. Because after reach bottom or top, it will show empty spaces only(refer <img src="http://help.openstreetmap.org/upfiles/image2_T8tGJ7w.png" alt="alt text" />image2.png)</p>
<p>Note: In google maps it is working fine(cant drag when reach top/bottom).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-dragging" rel="tag" title="see questions tagged &#39;dragging&#39;">dragging</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jul '15, 08:04</strong></p>
<img src="https://secure.gravatar.com/avatar/1ffa52ca3632b5a0cf02b51459b7529b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajavelu_M&#39;s gravatar image" />
<p><span>Rajavelu_M</span><br />
<span class="score" title="253 reputation points">253</span><span title="45 badges"><span class="badge1">●</span><span class="badgecount">45</span></span><span title="48 badges"><span class="silver">●</span><span class="badgecount">48</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajavelu_M has one accepted answer">33%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jul '15, 08:06</strong> </span></p>
</div>
</div>
<div id="comments-container-44498" class="comments-container">
<span id="44563"></span>
<div id="comment-44563" class="comment">
<div id="post-44563-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I found answer for how to disable drag?</p>
<p>map.dragging.disable();</p>
<p>But, still i dont know, how to find the map reached the top or bottom?</p>
</div>
<div id="comment-44563-info" class="comment-info">
<span class="comment-age">(31 Jul '15, 08:15)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="44589"></span>
<div id="comment-44589" class="comment">
<div id="post-44589-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also tried as map.setMaxBounds([[51.490, -0.122], [51.510, -0.028]]); for disable drag when reach top/bottom. But not working(map cant drag horizontally)</p>
</div>
<div id="comment-44589-info" class="comment-info">
<span class="comment-age">(03 Aug '15, 06:47)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
</div>
<div id="comment-tools-44498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44498-form-container" class="comment-form-container">
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

<span id="44774"></span>

<div id="answer-container-44774" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44774-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've used these settings (coords changed to yours):</p>
<pre><code>    var southwest = L.latLng(51.490, -0.122),
        northeast = L.latLng(51.510, -0.028),
        bounds = L.latLngBounds(southwest, northeast);
&#10;    var map = L.map(&#39;map&#39;, {
        zoom: 8,
        maxZoom: 18,
        maxBounds: bounds
    });
&#10;    map.fitBounds(bounds);</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '15, 10:22</strong></p>
<img src="https://secure.gravatar.com/avatar/021eca37311c7e7fbf127a22a862b50d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Protect%20OSM&#39;s gravatar image" />
<p><span>Protect OSM</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Protect OSM has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-44774" class="comments-container">
<span id="44780"></span>
<div id="comment-44780" class="comment">
<div id="post-44780-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Still its not working to me. Can you give in fiddle, or full source(with html).</p>
</div>
<div id="comment-44780-info" class="comment-info">
<span class="comment-age">(16 Aug '15, 07:27)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="44892"></span>
<div id="comment-44892" class="comment">
<div id="post-44892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for my late answer. Here's a demo:</p>
<p><a href="http://www.protectosm.com/demo-disabled-dragging/">http://www.protectosm.com/demo-disabled-dragging/</a></p>
</div>
<div id="comment-44892-info" class="comment-info">
<span class="comment-age">(24 Aug '15, 11:43)</span> <span class="comment-user userinfo">Protect OSM</span>
</div>
</div>
<span id="44893"></span>
<div id="comment-44893" class="comment">
<div id="post-44893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/11189/protect-osm">@Protect OSM</a>: I think you are mis-understand my question, Actually i need to disable drag when my drag reach bottom/top of the map. Currently i can drag when reach top/bottom of map, but it shows empty page.</p>
</div>
<div id="comment-44893-info" class="comment-info">
<span class="comment-age">(24 Aug '15, 11:50)</span> <span class="comment-user userinfo">Rajavelu_M</span>
</div>
</div>
<span id="44894"></span>
<div id="comment-44894" class="comment">
<div id="post-44894-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I "overdrag" the map it shows eveything perfectly but on "drop" it bounces back fitting the original bounds.</p>
<p>(<a href="http://i.imgur.com/x41dtJg.jpg">http://i.imgur.com/x41dtJg.jpg</a> - cursor was over the "Leaflet" copyright in the bottom, right.)</p>
<p>If it's not working at you like this, there's something wrong.</p>
<p>Could you please give a link to your site?</p>
</div>
<div id="comment-44894-info" class="comment-info">
<span class="comment-age">(24 Aug '15, 12:03)</span> <span class="comment-user userinfo">Protect OSM</span>
</div>
</div>
</div>
<div id="comment-tools-44774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44774-form-container" class="comment-form-container">
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

