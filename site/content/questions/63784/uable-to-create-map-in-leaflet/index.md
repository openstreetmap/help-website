+++
type = "question"
title = "uable to create map in leaflet"
description = '''hello   I am following leaflet tutorial to edit simple map ( just doing a testing to make sure it works) i see the map but its Blue screen and then i need to navigate it. but should not the right lat/long be shown when i open the page ?  Please see the picture, https://ibb.co/nko9nd https://ibb.co/m...'''
date = "2018-05-28T11:28:00Z"
lastmod = "2018-05-28T12:12:00Z"
weight = 63784
keywords = [ "leaflet" ]
aliases = [ "/questions/63784" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [uable to create map in leaflet](/questions/63784/uable-to-create-map-in-leaflet)

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
<span id="post-63784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63784-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello I am following leaflet tutorial to edit simple map ( just doing a testing to make sure it works)</p>
<p>i see the map but its Blue screen and then i need to navigate it. but should not the right lat/long be shown when i open the page ? Please see the picture, <a href="https://ibb.co/nko9nd">https://ibb.co/nko9nd</a> <a href="https://ibb.co/mATQSd">https://ibb.co/mATQSd</a></p>
<p>Can any one please tell me what i am doing wrong ? I have added the code here aswell.</p>
<p><a href="https://leafletjs.com/examples/quick-start/">https://leafletjs.com/examples/quick-start/</a></p>
<pre><code>    &lt;!DOCTYPE html PUBLIC &quot;-//W3C//DTD HTML 4.01//EN&quot;&gt;
    &lt;html&gt;
    &lt;head&gt;
      &lt;title&gt;my first map&lt;/title&gt;
      &lt;link rel=&quot;stylesheet&quot; href=&quot;leaflet.css&quot;/&gt;
      &lt;script src=&quot;leaflet.js&quot;&gt;&lt;/script&gt;
&#10;      &lt;style type=&quot;text/css&quot;&gt;
    #mapid { width: 960px;
        height:500px; }
      &lt;/style&gt;
    &lt;/head&gt;
    &lt;body&gt;
&#10;    &lt;div id=&quot;mapid&quot;&gt; &lt;/div&gt;
&#10;    &lt;script&gt;
&#10;    var mymap = L.map(&#39;mapid&#39;).setView([90.4125,
23.8103], 8);
&#10;    L.tileLayer(&#39;http://192.168.1.32/hot/{z}/{x}/{y}.png&#39;,{
        attribution: &#39;Map data &amp;copy; &lt;a href=&quot;https://www.openstreetmap.org/&quot;&gt;OpenStreetMap&lt;/a&gt; contributors, &lt;a href=&quot;https://creativecommons.org/licenses/by-sa/2.0/&quot;&gt;CC-BY-SA&lt;/a&gt;, Imagery © &lt;a href=&quot;https://www.mapbox.com/&quot;&gt;Mapbox&lt;/a&gt;&#39;,
        maxZoom: 12
&#10;    }).addTo(mymap);
&#10;    &lt;/script&gt;
&#10;    &lt;/body&gt;
&#10;    &lt;/html&gt;</code></pre>
<p>Thanks for the help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 May '18, 11:28</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb2a94f867841b58214be09992831d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fosiul&#39;s gravatar image" />
<p><span>fosiul</span><br />
<span class="score" title="96 reputation points">96</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fosiul has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-63784" class="comments-container">
&#10;</div>
<div id="comment-tools-63784" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63784-form-container" class="comment-form-container">
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

<span id="63785"></span>

<div id="answer-container-63785" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63785-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63785-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63785-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fosiul has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try swapping latitude and longitude in setView.</p>
<p>The example has</p>
<pre><code>var mymap = L.map(&#39;mapid&#39;).setView([51.505, -0.09], 13);</code></pre>
<p>which is 51.505 North, 0.09 West. I'm not sure you can have 90.4125 North.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 May '18, 11:49</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 May '18, 11:50</strong> </span></p>
</div>
</div>
<div id="comments-container-63785" class="comments-container">
<span id="63788"></span>
<div id="comment-63788" class="comment">
<div id="post-63788-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks Edloach , I am sure i changed that and tryed but did nto work, but now its working.. now sure what i was doing wrong, but yes its works</p>
<p>Thanks</p>
</div>
<div id="comment-63788-info" class="comment-info">
<span class="comment-age">(28 May '18, 12:12)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
</div>
<div id="comment-tools-63785" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63785-form-container" class="comment-form-container">
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

