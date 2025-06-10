+++
type = "question"
title = "Transform x,y pixel values into lat and long"
description = '''Hi I have a little problem here. I have latitude, longitude and zoom of center of my map window (openstreet map). I have dimension map window. I also have pixel positions of specific events on the map in the window. Can Anyone help me how to convert these pixel positions into latitude and longitude ...'''
date = "2020-07-09T08:24:00Z"
lastmod = "2020-07-09T15:43:00Z"
weight = 75611
keywords = [ "python", "map", "transformation" ]
aliases = [ "/questions/75611" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Transform x,y pixel values into lat and long](/questions/75611/transform-xy-pixel-values-into-lat-and-long)

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
<span id="post-75611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75611-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I have a little problem here. I have latitude, longitude and zoom of center of my map window (openstreet map). I have dimension map window. I also have pixel positions of specific events on the map in the window. Can Anyone help me how to convert these pixel positions into latitude and longitude coordinates or any other coordinate system that I will be able to visualize on different map later ? Here is an illustration of my problem. <img src="https://help.openstreetmap.org/upfiles/Capture_8U84fS2.PNG" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-transformation" rel="tag" title="see questions tagged &#39;transformation&#39;">transformation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '20, 08:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ccc5a8a21df20158837f5cd1ae83b4d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jozef&#39;s gravatar image" />
<p><span>Jozef</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jozef has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-75611" class="comments-container">
&#10;</div>
<div id="comment-tools-75611" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75611-form-container" class="comment-form-container">
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

<span id="75616"></span>

<div id="answer-container-75616" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75616-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75616-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75616-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The projection you are displaying the map in is the so called spherical Mercator projection, you can convert Mercator coordinates to WGS84 lat/lon with the formulas from <a href="https://wiki.openstreetmap.org/wiki/Mercator">https://wiki.openstreetmap.org/wiki/Mercator</a> (you will need to scale from you screen pixels or whatever to Mercator meters but that is a simple exercise left for the reader).</p>
<p>Further note: Mercator latitude coordinates do not actually cover -90° to 90° degrees as your image would suggest.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '20, 12:19</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-75616" class="comments-container">
&#10;</div>
<div id="comment-tools-75616" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75616-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75621"></span>

<div id="answer-container-75621" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75621-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank I have found the solution using this formula (<a href="https://en.wikipedia.org/wiki/Web_Mercator_projection">https://en.wikipedia.org/wiki/Web_Mercator_projection</a> ) <img src="https://help.openstreetmap.org/upfiles/Capture2_0tNpXAS.PNG" alt="alt text" /></p>
<ol>
<li>calculate the x,y position of my center point</li>
<li>transform coordinate system of window to global</li>
<li>inverse transformation</li>
</ol>
<p>code below</p>
<pre><code>def LatLontoXY(lat_center,lon_center,zoom):
    C =(256/(2*pi) )* 2**zoom
&#10;    x=C*(math.radians(lon_center)+pi)
    y=C*(pi-math.log( math.tan(  (pi/4) + math.radians(lat_center)/2    )  ))
&#10;    return x,y
&#10;def xy2LatLon(lat_center,lon_center,zoom,width_internal,height_internal,pxX_internal,pxY_internal):
&#10;    xcenter,ycenter=LatLontoXY(lat_center,lon_center,zoom)
&#10;    xPoint=xcenter- (width_internal/2-pxX_internal)
    ypoint=ycenter -(height_internal/2-pxY_internal)
&#10;
    C = (256 / (2 * pi)) * 2 ** zoom
    M = (xPoint/C)-pi
    N =-(ypoint/C) + pi
&#10;    lon_Point =math.degrees(M)
    lat_Point =math.degrees( (math.atan( math.e**N)-(pi/4))*2 )
&#10;    return lat_Point,lon_Point</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '20, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/ccc5a8a21df20158837f5cd1ae83b4d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jozef&#39;s gravatar image" />
<p><span>Jozef</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jozef has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-75621" class="comments-container">
&#10;</div>
<div id="comment-tools-75621" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75621-form-container" class="comment-form-container">
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

