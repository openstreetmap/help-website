+++
type = "question"
title = "How to configure offline imagery for JOSM?"
description = '''I searched TAGS for OFFLINE and IMAGERY and did not find anything. I am trying to setup JOSM to cache IMAGERY for offline use. Do I have to set higher limits of TILE SIZE under PREFERENCES- IMAGERY PREFERENCES- SETTINGS, WMS Settings, Tile Size to some higher number (eg. 4096?) or MAXIMUM SIZE OF DI...'''
date = "2016-03-02T19:02:00Z"
lastmod = "2016-03-10T22:32:00Z"
weight = 48466
keywords = [ "wms", "tms", "offline", "imagery", "bing" ]
aliases = [ "/questions/48466" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to configure offline imagery for JOSM?](/questions/48466/how-to-configure-offline-imagery-for-josm)

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
<span id="post-48466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48466-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I searched TAGS for OFFLINE and IMAGERY and did not find anything.</p>
<p>I am trying to setup JOSM to cache IMAGERY for offline use. Do I have to set higher limits of TILE SIZE under PREFERENCES- IMAGERY PREFERENCES- SETTINGS, WMS Settings, Tile Size to some higher number (eg. 4096?) or MAXIMUM SIZE OF DISK CACHE in MB to 4096?</p>
<p>And if I set these higher levels, how to I define a AREA or POLYGON to download, and how do I define that I want MOST ZOOM LEVELS (at least from most detail to some higher levels).</p>
<p>When wroking offline, I do not want these map imagery files not to EXPIRE ( I will manually download new imagery when I get online again )</p>
<p>That way I can work OFFLINE with BING, WMS or TMS imagery OFFLINE and it will look like I am online.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wms" rel="tag" title="see questions tagged &#39;wms&#39;">wms</span> <span class="post-tag tag-link-tms" rel="tag" title="see questions tagged &#39;tms&#39;">tms</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-bing" rel="tag" title="see questions tagged &#39;bing&#39;">bing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Mar '16, 19:02</strong></p>
<img src="https://secure.gravatar.com/avatar/aaf8869d4cd5c92ca9831ebf99b07eca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gregcrago&#39;s gravatar image" />
<p><span>gregcrago</span><br />
<span class="score" title="69 reputation points">69</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gregcrago has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48466" class="comments-container">
&#10;</div>
<div id="comment-tools-48466" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48466-form-container" class="comment-form-container">
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

<span id="48479"></span>

<div id="answer-container-48479" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48479-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One technique that I've used before (for mapwarper imagery, which is on a slow server and has a short cache retension policy) is to setup the map on <a href="https://marble.kde.org/">marble</a>, (pre)download the tiles in Marble, and then point JOSM at Marble's cache. This enables pre-downloading an area, and gives you greater control in how long the tiles are kept.</p>
<p>However, you can't setup Bing satellite on Marble, both because of a technical limitation and Bing's TOS restrictions. Try Mapbox imagery instead, which is often just as good or better than Bing, and technically usable in Marble. But you probably have to <a href="https://www.mapbox.com/studio/signup/">setup a Mapbox account</a> to get your own access token for use in Marble, as reusing JOSM's access token probably goes against their TOS.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '16, 11:26</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-48479" class="comments-container">
<span id="48516"></span>
<div id="comment-48516" class="comment">
<div id="post-48516-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you show me the way to point JOSM at Marble's cache? I am using Windows 7, I have found the location of the cache directory. I have tried WMS using <code>file:///c:\yourdirectory\{z}\{x}\{y}.extension</code> scheme with the correct file extension. But it didn't load and threw out errors, please help me the correct way of doing it?</p>
</div>
<div id="comment-48516-info" class="comment-info">
<span class="comment-age">(06 Mar '16, 06:49)</span> <span class="comment-user userinfo">AkuAnakTimur</span>
</div>
</div>
<span id="48540"></span>
<div id="comment-48540" class="comment">
<div id="post-48540-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You need to use TMS, not WMS. Otherwise your config looks fine. I've re-tested this config and can confirm it works:</p>
<p>tms[20]:file:///home/myusername/.local/share/marble/maps/earth/openstreetmap/{zoom}/{x}/{y}.png</p>
<p>Not sure if "z" vs "zoom" makes a difference. You're apparently on Windows so the path is different. Make sure to view the area in Marble first. If it still doesn't work, run josm in a terminal to see what file it is trying to access.</p>
</div>
<div id="comment-48540-info" class="comment-info">
<span class="comment-age">(07 Mar '16, 11:26)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="48616"></span>
<div id="comment-48616" class="comment">
<div id="post-48616-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you fixed the OFFSET error yet? I am waiting to use offline maps, but I am waiting for someone to successfully download aligned maps. Anyone write up a procedure somewhere?</p>
</div>
<div id="comment-48616-info" class="comment-info">
<span class="comment-age">(10 Mar '16, 21:03)</span> <span class="comment-user userinfo">gregcrago</span>
</div>
</div>
<span id="48620"></span>
<div id="comment-48620" class="comment">
<div id="post-48620-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Moved the comment about offsets to <a href="https://help.openstreetmap.org/questions/48585/significant-offset-between-josm-and-marble-for-mapwarper-imagery">its own question</a>.</p>
</div>
<div id="comment-48620-info" class="comment-info">
<span class="comment-age">(10 Mar '16, 22:32)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48479" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48479-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48477"></span>

<div id="answer-container-48477" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48477-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>AFAIK you can't just define a polygon and then automatically download the tiles inside with JOSM. I believe you have to set different preferences according to the kind of imagery (tiles or WMS), and you should (not completely sure, but it used to work like this) disable "auto zoom" for WMS.</p>
<p>I do have these preferences values:</p>
<pre><code>cache.geoimage-thumbnails.expire=-1
cache.geoimage-thumbnails.maxsize=120</code></pre>
<p>I also have this one set: <code>imagery.wms.default_autozoom=false</code> but it doesn't seem to work currently (see <a href="https://josm.openstreetmap.de/ticket/12589#ticket">here</a>)</p>
<p>You should not raise the tile size, but the tile cache size.</p>
<p>One way to use offline tiles is putting them into structured directories on your local disk, following the <code>yourdirectory/{z}/{x}/{y}.png</code> scheme. You can then add this as a layer by pointing to it from the preferences like this: <code>file:///yourdirectory/{z}/{x}/{y}.png</code> on unix-like systems, or similarly on Windows: <code>file:///c:\yourdirectory\{z}\{x}\{y}.png</code>. To get the pictures you can either tile big georeferenced images with gdal or use available tools to download tiles from the web (might not be allowed in many cases).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '16, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Mar '16, 12:04</strong> </span></p>
</div>
</div>
<div id="comments-container-48477" class="comments-container">
&#10;</div>
<div id="comment-tools-48477" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48477-form-container" class="comment-form-container">
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

