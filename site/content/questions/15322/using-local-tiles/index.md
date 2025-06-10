+++
type = "question"
title = "[closed] Using local tiles"
description = '''Hi, I have created local tiles using Mapnik. Now I want to display the local tiles on a webpage(JSP Running on tomcat). I have tried html code and it works fine. But it does not work in JSP. Can anybody help me in this?'''
date = "2012-08-21T11:47:00Z"
lastmod = "2012-08-22T12:34:00Z"
weight = 15322
keywords = [ "on", "tiles", "local", "jsp" ]
aliases = [ "/questions/15322" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Using local tiles](/questions/15322/using-local-tiles)

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
<span id="post-15322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15322-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have created local tiles using Mapnik. Now I want to display the local tiles on a webpage(JSP Running on tomcat). I have tried html code and it works fine. But it does not work in JSP. Can anybody help me in this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-on" rel="tag" title="see questions tagged &#39;on&#39;">on</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-local" rel="tag" title="see questions tagged &#39;local&#39;">local</span> <span class="post-tag tag-link-jsp" rel="tag" title="see questions tagged &#39;jsp&#39;">jsp</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Aug '12, 11:47</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>22 Aug '12, 12:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span></p>
</div>
</div>
<div id="comments-container-15322" class="comments-container">
<span id="15323"></span>
<div id="comment-15323" class="comment">
<div id="post-15323-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain what doesn't work and provide some error messages or log entries if possible?</p>
</div>
<div id="comment-15323-info" class="comment-info">
<span class="comment-age">(21 Aug '12, 12:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="15328"></span>
<div id="comment-15328" class="comment">
<div id="post-15328-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>var newLayer = new OpenLayers.Layer.OSM("Local Tiles", "tiles/${z}/${x}/${y}.png", {numZoomLevels: 19, alpha: true, isBaseLayer: false}); map.addLayer(newLayer);</p>
<p>This code works fine in html file and the map tiles are opening. But the same code does not open any map image in jsp code. Only pink background is displayed. And if I move the mouse, it displayes lat long attributes also.</p>
</div>
<div id="comment-15328-info" class="comment-info">
<span class="comment-age">(21 Aug '12, 12:20)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="15329"></span>
<div id="comment-15329" class="comment">
<div id="post-15329-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I check by view source option of browser, it shows tile path as tiles///.png</p>
</div>
<div id="comment-15329-info" class="comment-info">
<span class="comment-age">(21 Aug '12, 12:21)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="15365"></span>
<div id="comment-15365" class="comment">
<div id="post-15365-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've closed this question as you have opened another one with more details.</p>
</div>
<div id="comment-15365-info" class="comment-info">
<span class="comment-age">(22 Aug '12, 12:34)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
</div>
<div id="comment-tools-15322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15322-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by NicolasDumoulin 22 Aug '12, 12:34

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15333"></span>

<div id="answer-container-15333" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15333-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you sure that your Java EE server is configured to serve static files from the directory containing your tiles? Can you access directly to a tile, by bypassing your jsp page?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '12, 14:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-15333" class="comments-container">
<span id="15334"></span>
<div id="comment-15334" class="comment">
<div id="post-15334-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I can access the tiles using html sample code given on link below. <a href="http://wiki.openstreetmap.org/wiki/OpenLayers_Local_Tiles_Example.">http://wiki.openstreetmap.org/wiki/OpenLayers_Local_Tiles_Example.</a></p>
<p>Only if I add the same code in a jsp page, it does not display the images, but on mouse over, lat long is displayed.</p>
</div>
<div id="comment-15334-info" class="comment-info">
<span class="comment-age">(21 Aug '12, 14:31)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="15335"></span>
<div id="comment-15335" class="comment">
<div id="post-15335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But do you access this html page with your java EE server? BTW, which server do you use?</p>
<p>If you can access directly to tiles with your webserver, you should look at the html code served from your JSP in your browser.</p>
</div>
<div id="comment-15335-info" class="comment-info">
<span class="comment-age">(21 Aug '12, 14:35)</span> <span class="comment-user userinfo">NicolasDumoulin</span>
</div>
</div>
<span id="15336"></span>
<div id="comment-15336" class="comment">
<div id="post-15336-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am using tomcat server.</p>
</div>
<div id="comment-15336-info" class="comment-info">
<span class="comment-age">(21 Aug '12, 14:37)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
</div>
<div id="comment-tools-15333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15333-form-container" class="comment-form-container">
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

