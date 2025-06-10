+++
type = "question"
title = "Red error tiles in JOSM"
description = '''Since I&#x27;d upgraded to JOSM 3751 from 3701 I get red Error tiles around my local Imagery tiles. I&#x27;m using separate tms-servers for different local map areas but the tiles doesn&#x27;t overlap. The red Error tiles though are overlapping the tiles from other servers. Is there a way to not show the red tiles...'''
date = "2011-01-05T21:28:00Z"
lastmod = "2011-01-23T08:32:00Z"
weight = 2040
keywords = [ "tile", "josm", "imagery", "error" ]
aliases = [ "/questions/2040" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Red error tiles in JOSM](/questions/2040/red-error-tiles-in-josm)

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
<span id="post-2040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2040-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Since I'd upgraded to JOSM 3751 from 3701 I get red Error tiles around my local Imagery tiles. I'm using separate tms-servers for different local map areas but the tiles doesn't overlap. The red Error tiles though are overlapping the tiles from other servers. Is there a way to not show the red tiles?? I'm new to this so maybe I've missed some setting for this.</p>
<p>I also have a problem with cached Imagery tiles. I have a server on my computer for local tiles but when I changed some of them I still get the old images, its not updating from the server. I've tried to Flush tile cache but nothing happens. If I change the menu name for the Imagery then it will use the updated tiles. I've tried to find the cached tiles but no luck...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '11, 21:28</strong></p>
<img src="https://secure.gravatar.com/avatar/f71afeb7ab925cfcfd8a96fd2a9e0401?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Divvi&#39;s gravatar image" />
<p><span>Divvi</span><br />
<span class="score" title="66 reputation points">66</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Divvi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jan '11, 17:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ba4d3e91f235ed21dacc1766b94e26a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richlv&#39;s gravatar image" />
<p><span>Richlv</span><br />
<span class="score" title="1740 reputation points"><span>1.7k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span></p>
</div>
</div>
<div id="comments-container-2040" class="comments-container">
&#10;</div>
<div id="comment-tools-2040" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2040-form-container" class="comment-form-container">
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

<span id="2087"></span>

<div id="answer-container-2087" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2087-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On Unix-like systems Imagery plugin cached tiles will be found in :</p>
<p>~/.josm/plugins/imagery/cache</p>
<p>For the older wmsplugin they will be, unsurprisingly, found in :</p>
<p>~/.josm/plugins/wmsplugin/cache</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '11, 15:48</strong></p>
<img src="https://secure.gravatar.com/avatar/ba4d3e91f235ed21dacc1766b94e26a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richlv&#39;s gravatar image" />
<p><span>Richlv</span><br />
<span class="score" title="1740 reputation points"><span>1.7k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richlv has 5 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-2087" class="comments-container">
&#10;</div>
<div id="comment-tools-2087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2087-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2109"></span>

<div id="answer-container-2109" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2109-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Each server corresponds to a different layer in the Imagery plugin, so make sure you have your layers visible in the right sidebar by pressing Alt+L or clicking the icon that looks like a little stack of paper in the left-hand vertical toolbar. You should see layer names like "Data Layer 1" or "Downloaded GPX Data", and more importantly all your TMS and WMS server layers.</p>
<p>You should then be able to click the little eye icon next to each layer to hide or show it. Sadly there doesn't seem to be a setting for turning off the ugly red error squares.</p>
<p>If only some zoom levels give you red error tiles (sometimes the server won't support 17 or 18 or higher for TMS, for example), try Edit→Preferences (F12), "WMS TMS" tab, and enter a maximum zoom for the problem servers. You may need to purge your cache to see any effect.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '11, 17:41</strong></p>
<img src="https://secure.gravatar.com/avatar/b4a99bb74962d3cedff3e6d591847852?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew%20Chadwick&#39;s gravatar image" />
<p><span>Andrew Chadwick</span><br />
<span class="score" title="1129 reputation points"><span>1.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew Chadwick has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-2109" class="comments-container">
<span id="2141"></span>
<div id="comment-2141" class="comment">
<div id="post-2141-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The server/data layers I use only cover a small area each (no data outside that area). So it's like a jigsaw/picture puzzle. Too bad you can't turn off the error tiles because then I can only work on/see one area at the time...</p>
</div>
<div id="comment-2141-info" class="comment-info">
<span class="comment-age">(10 Jan '11, 22:37)</span> <span class="comment-user userinfo">Divvi</span>
</div>
</div>
</div>
<div id="comment-tools-2109" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2109-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2379"></span>

<div id="answer-container-2379" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2379-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>On the 23.Jan. 2011 I upgraded to JOSM 3751 and had the same symptoms:</p>
<p><strong><em>Red error tiles overlaying the Bing imagery.</em></strong></p>
<p><em>NOTE: I am using a German version of JOSM so the following word translations to English could well be wrong!</em></p>
<p>I went to "Einstellungen" i.e. F12 (Perhaps "Setup" in English) - pressed the WMS TMS button to go to "Einstellungen für Hintergrundebene" (Setup for Backgroud levels) - The list of "Bilddienste" (Picture Services/Providers) was:</p>
<hr />
<p>Bing Sat bing:bing</p>
<p>Bing Sat bing:bing?</p>
<p>LandSat wms:<a href="http://onearth.jpl.nasa.gov/wms.cgi?request=GetMap&amp;layers=global_mosaic&amp;styles=&amp;format=image/jpeg&amp;">http://onearth.jpl.nasa.gov/wms.cgi?request=GetMap&amp;layers=global_mosaic&amp;styles=&amp;format=image/jpeg&amp;</a></p>
<p>LandSat wms:<a href="http://onearth.jpl.nasa.gov/wms.cgi?request=GetMap&amp;layers=global_mosaic&amp;styles=&amp;srs=EPSG:4326&amp;format=image/jpeg">http://onearth.jpl.nasa.gov/wms.cgi?request=GetMap&amp;layers=global_mosaic&amp;styles=&amp;srs=EPSG:4326&amp;format=image/jpeg</a></p>
<p>Landsat (Spiegelserver) wms:<a href="http://irs.gis-lab.info/?layers=landsat&amp;">http://irs.gis-lab.info/?layers=landsat&amp;</a></p>
<p>OpenAerial-Karte <a href="http://wms:http://openaerialmap.org">wms:http://openaerialmap.org</a>/wms/? VERSION=1.0&amp;request=GetMap&amp;layers=world&amp;styles=&amp;srs=EPSG:4326&amp;format=image/jpeg</p>
<p>OpenStreetMap <a href="http://tms:http://tile.openstreetmap.org">tms:http://tile.openstreetmap.org</a>/</p>
<p>Yahoo Sat html:<a href="http://josm.openstreetmap.de/wmsplugin/YahooDirect.html?">http://josm.openstreetmap.de/wmsplugin/YahooDirect.html?</a> -</p>
<hr />
<p>As I could not see the point of the second line <strong>Bing:Bing?</strong> I elimated it and after a JOSM restart Bing imagery worked perfectly!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '11, 08:32</strong></p>
<img src="https://secure.gravatar.com/avatar/cd4569f9fa1aac11eb6b19d6de309ea6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dcp&#39;s gravatar image" />
<p><span>dcp</span><br />
<span class="score" title="721 reputation points">721</span><span title="37 badges"><span class="badge1">●</span><span class="badgecount">37</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dcp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Jan '11, 08:35</strong> </span></p>
</div>
</div>
<div id="comments-container-2379" class="comments-container">
&#10;</div>
<div id="comment-tools-2379" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2379-form-container" class="comment-form-container">
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

