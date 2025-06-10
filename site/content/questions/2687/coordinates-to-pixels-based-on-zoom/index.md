+++
type = "question"
title = "Coordinates to Pixels based on Zoom"
description = '''I have what I think should be a fairly straight forward question. I have a map that is 1000x700 and has a user specified Zoom and Center Coordinates. I want to be able to find the pixel location of a certain coordinate showing on the map. For example, if I have the following map: http://pafciu17.dev...'''
date = "2011-02-02T16:58:00Z"
lastmod = "2021-10-14T16:38:00Z"
weight = 2687
keywords = [ "zoom", "pixel" ]
aliases = [ "/questions/2687" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Coordinates to Pixels based on Zoom](/questions/2687/coordinates-to-pixels-based-on-zoom)

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
<span id="post-2687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2687-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have what I think should be a fairly straight forward question.</p>
<p>I have a map that is 1000x700 and has a user specified Zoom and Center Coordinates. I want to be able to find the pixel location of a certain coordinate showing on the map.</p>
<p>For example, if I have the following map: <a href="http://pafciu17.dev.openstreetmap.org/?module=map&amp;lon=-89.08805000000001&amp;lat=30.6393&amp;zoom=6.5156731549786215&amp;width=1000.0&amp;height=700.0&amp;type=mapnik&amp;imgType=gif">http://pafciu17.dev.openstreetmap.org/?module=map&amp;lon=-89.08805000000001&amp;lat=30.6393&amp;zoom=6.5156731549786215&amp;width=1000.0&amp;height=700.0&amp;type=mapnik&amp;imgType=gif</a></p>
<p>I would like to be able to locate Fort Worth, Texas on the image (pixel location).</p>
<p>I assume there is some sort of formula for determining the pixel location of a coordinate based on the image size, center coordinate, and zoom factor. Can anyone help me out? Any help is greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span> <span class="post-tag tag-link-pixel" rel="tag" title="see questions tagged &#39;pixel&#39;">pixel</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Feb '11, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/a36c891e7c5533a9297fc6c5afd52ca9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aussiemcgr&#39;s gravatar image" />
<p><span>aussiemcgr</span><br />
<span class="score" title="30 reputation points">30</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aussiemcgr has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2687" class="comments-container">
&#10;</div>
<div id="comment-tools-2687" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2687-form-container" class="comment-form-container">
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

<span id="2688"></span>

<div id="answer-container-2688" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2688-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-2688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The (very) short answer is: Have a look at <a href="http://wiki.openstreetmap.org/wiki/Tilenames">at the wiki</a> and <a href="http://help.openstreetmap.org/questions/747">the question that was asked earlier</a>.</p>
<p>As this does not resolve the submitters question, I'll edit my answer and expand it. For the original example URL we can extract the following parameters: longitude 89.08805 west, latitude 30.6393 north and zoomlevel 6.5156731549786215. (Note that this is a non integer zoomlevel and might break lots of code that only expects integer zoomlevels.) However looking at the output resulting gif it looks like the website truncates the zoomlevel and really uses zoomlevel 6.</p>
<p>Using this really simple java code which would support fractional zoomlevels if needed in the future we can convert lat and long to tile coordinates.</p>
<pre><code>double lon = -89.08805;
double lat = 30.6393;
double zoom = 6; // 6.5156731549786215 would be possible too
&#10;double lon_rad = Math.toRadians(lon);
double lat_rad = Math.toRadians(lat);
double n = Math.pow(2.0, zoom);
&#10;double tileX = ((lon + 180) / 360) * n;
double tileY = (1 - (Math.log(Math.tan(lat_rad) + 1.0/Math.cos(lat_rad)) / Math.PI)) * n / 2.0;
&#10;System.out.println(&quot;tileX = &quot;+tileX+&quot; tileY = &quot;+tileY);</code></pre>
<p>It computes the location of the map center in tile coordinates as:</p>
<pre><code>tileX = 16.162124444444444
tileY = 26.273150713795616</code></pre>
<p>For Forth Worth I'll use <code>longitude 97.3327459 east</code> and <code>latitude 32.753177 north</code> which translates into:</p>
<pre><code>tileX = 14.696400728888888
tileY = 25.831427880285347</code></pre>
<p>So Fort Worth is 1.465723715555556 tiles left and 0.441722833510269 tiles above the map center. To get to pixels all you would have to do is to multiply by 256 pixels per tile. Thus we get the information that Fort Worth is 375 pixels left and 113 pixels above the map center.</p>
<p>Given that the map is 1000 pixels wide and 700 pixels wide this means that Fort Worth is 125 pixels from the left boundary and 237 pixels down from the top.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Feb '11, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Feb '11, 20:28</strong> </span></p>
</div>
</div>
<div id="comments-container-2688" class="comments-container">
<span id="2755"></span>
<div id="comment-2755" class="comment">
<div id="post-2755-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I'm still having trouble. So when I calculate the tiles Fort Worth Airport (Long: -97.0411, Lat: 32.8964) with a zoom of 6, I get tileX = 21 and tileY = 37, which is around Santa Fe, Brazil. I copied and pasted the code you provided above. Why would I get this?</p>
<p>I should be getting a tileX of 14 and a tileY of 25 (based on the url: <a href="http://tile.openstreetmap.org/6/14/25.png">http://tile.openstreetmap.org/6/14/25.png</a>)</p>
<p>Interestingly enough, if I multiply by 175 instead of 256 for Zoom 6 or 160 for a Zoom of 7, it seems to be completely correct. Is that coincidence or does zoom effect the pixels in the image?</p>
</div>
<div id="comment-2755-info" class="comment-info">
<span class="comment-age">(07 Feb '11, 15:31)</span> <span class="comment-user userinfo">aussiemcgr</span>
</div>
</div>
<span id="2792"></span>
<div id="comment-2792" class="comment">
<div id="post-2792-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know what you do but my code outputs "tileX = 14.748248888888888 tileY = 25.801128101180893" for long: -97.0411, Lat: 32.8964, zoom: 6.</p>
<p>And not zoom level does not change the pixels per tile. But it does change the conversion to tile numbers.</p>
</div>
<div id="comment-2792-info" class="comment-info">
<span class="comment-age">(08 Feb '11, 14:29)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="2858"></span>
<div id="comment-2858" class="comment">
<div id="post-2858-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I figured it out. When I powered with the zoom, I was using a double instead of an int. So the powering was adding additional value to the result of the power, thus resulting in the incorrect tiles. If I cast zoom before using it in the power, it works perfectly. Thank you for your help and your patience with me.</p>
</div>
<div id="comment-2858-info" class="comment-info">
<span class="comment-age">(09 Feb '11, 18:36)</span> <span class="comment-user userinfo">aussiemcgr</span>
</div>
</div>
<span id="2859"></span>
<div id="comment-2859" class="comment">
<div id="post-2859-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Using a double there would be right if the image creation site honored fractional zoomlevels. However it doesn't so you have to truncate the zoomlevel to match the result from that website. I'm glad we finally figured that one out.</p>
</div>
<div id="comment-2859-info" class="comment-info">
<span class="comment-age">(09 Feb '11, 18:52)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
</div>
<div id="comment-tools-2688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2688-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4524"></span>

<div id="answer-container-4524" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4524-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>hey, i wanted to ask how do you calculate that for Fort Worth is 1.465723715555556 tiles left and 0.441722833510269 tiles above the map center when you have tileX and tileY, what kind of calculations follow</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Apr '11, 09:44</strong></p>
<img src="https://secure.gravatar.com/avatar/272c92fff39d41712ce7c090b0348145?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anichka&#39;s gravatar image" />
<p><span>anichka</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anichka has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4524" class="comments-container">
<span id="4525"></span>
<div id="comment-4525" class="comment">
<div id="post-4525-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I <em>really</em> hope that you are kidding, but here is the explanation: take the tileX of Forth Worth (14.696400728888888) and substract the tileX of the map center (16.162124444444444). You then get deltaX = 14.696400728888888 - 16.162124444444444 = -1.465723715555556. The X value is increasing left to right so a negative value for the difference means "left of the center". The same method applies to the Y direction.</p>
</div>
<div id="comment-4525-info" class="comment-info">
<span class="comment-age">(15 Apr '11, 10:42)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="82174"></span>
<div id="comment-82174" class="comment">
<div id="post-82174-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why you used these coordinates? based on what?</p>
<p>"For Forth Worth I'll use longitude 97.3327459 east and latitude 32.753177 north which translates into"</p>
</div>
<div id="comment-82174-info" class="comment-info">
<span class="comment-age">(14 Oct '21, 16:38)</span> <span class="comment-user userinfo">Seghier</span>
</div>
</div>
</div>
<div id="comment-tools-4524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4524-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14498"></span>

<div id="answer-container-14498" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14498-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>hey plz how did you found that : Fort Worth is 125 pixels from the left boundary and 237 pixels down from the top.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '12, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/24aa4d4f90668acaca2dafbc9bf3a738?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vaddinDev&#39;s gravatar image" />
<p><span>vaddinDev</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vaddinDev has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14498" class="comments-container">
&#10;</div>
<div id="comment-tools-14498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14498-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64703"></span>

<div id="answer-container-64703" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64703-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I know this is old. But just as vaddinDev, I struggle to understand the conversion to the 100x700 map pixel location. What I think is used for calculation is that the tile is 256 images wide and tall.</p>
<p>So,</p>
<p>for width: 375 x 3 = 1125 =&gt; 1125-1000 = 125 pixels from left of image)</p>
<p>for height: 113 x 4 = 452 =&gt; 452-700 = -247 pixels down from top of image (I think the 237 in the original answer is a typo).</p>
<p>PLEASE correct me if I am stretching the math here!!!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '18, 20:24</strong></p>
<img src="https://secure.gravatar.com/avatar/6efe112f56118bc761a51c8a426e89e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Omi3&#39;s gravatar image" />
<p><span>Omi3</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Omi3 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jul '18, 20:26</strong> </span></p>
</div>
</div>
<div id="comments-container-64703" class="comments-container">
&#10;</div>
<div id="comment-tools-64703" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64703-form-container" class="comment-form-container">
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

