+++
type = "question"
title = "How can I get OSM data to work on my Garmin Nuvi 260?"
description = '''Hi, I&#x27;m trying to get OSM data loaded onto my Garmin Nuvi 260. I downloaded data from http://www.osmmaps.com/maps/united-states , extracted it, and put the contents on a freshly FAT32 formatted 8GB microSD card. The contents are as follows (/Volumes/NUVI is the mountpoint on my machine, &quot;Garmin&quot; is ...'''
date = "2013-11-28T22:57:00Z"
lastmod = "2013-12-19T03:55:00Z"
weight = 28592
keywords = [ "260", "nuvi" ]
aliases = [ "/questions/28592" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I get OSM data to work on my Garmin Nuvi 260?](/questions/28592/how-can-i-get-osm-data-to-work-on-my-garmin-nuvi-260)

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
<span id="post-28592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28592-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to get OSM data loaded onto my Garmin Nuvi 260. I downloaded data from <a href="http://www.osmmaps.com/maps/united-states">http://www.osmmaps.com/maps/united-states</a> , extracted it, and put the contents on a freshly FAT32 formatted 8GB microSD card. The contents are as follows (/Volumes/NUVI is the mountpoint on my machine, "Garmin" is in the root of the SD card):</p>
<pre><code>/Volumes/NUVI
/Volumes/NUVI/._.Trashes
/Volumes/NUVI/.Trashes
/Volumes/NUVI/.fseventsd
/Volumes/NUVI/.fseventsd/fseventsd-uuid
/Volumes/NUVI/Garmin
/Volumes/NUVI/Garmin/gmapsupp.img   &lt;--- the 3.3GB file from OSM
/Volumes/NUVI/Garmin/._gmapsupp.img</code></pre>
<p>When I insert the card into my Nuvi 260 and power it on, I see a green progress bar on the boot screen of the Nuvi (which I don't see under normal operation, eg without the SD card). After powering on, which takes ~30 seconds, I open the maps/map info options, and unfortunately do not see the OSM data; I only see the stock "City Navigator North America NT 2009".</p>
<p>Any suggestions on things I might have missed along the way?</p>
<p>Thanks so much!</p>
<p>nuvi 260, Software Version 2.80</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-260" rel="tag" title="see questions tagged &#39;260&#39;">260</span> <span class="post-tag tag-link-nuvi" rel="tag" title="see questions tagged &#39;nuvi&#39;">nuvi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Nov '13, 22:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a3d6887041bc564a5d60cdc811ae4ef9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jedediah&#39;s gravatar image" />
<p><span>jedediah</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jedediah has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28592" class="comments-container">
<span id="28594"></span>
<div id="comment-28594" class="comment">
<div id="post-28594-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't own a Garmin, but maybe you need to work with a '/map/gsupmap?.img' as suggested for Nüvi 2350? <a href="https://wiki.openstreetmap.org/wiki/Garmin#N.C3.BCvi_series">https://wiki.openstreetmap.org/wiki/Garmin#N.C3.BCvi_series</a></p>
</div>
<div id="comment-28594-info" class="comment-info">
<span class="comment-age">(29 Nov '13, 08:53)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="28597"></span>
<div id="comment-28597" class="comment">
<div id="post-28597-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Garmin/gmapsupp.img should be ok, no other names are allowed as far as I know, btw what is this file ._gmapsupp.img doing there?</p>
</div>
<div id="comment-28597-info" class="comment-info">
<span class="comment-age">(29 Nov '13, 11:18)</span> <span class="comment-user userinfo">ligfietser</span>
</div>
</div>
<span id="28605"></span>
<div id="comment-28605" class="comment">
<div id="post-28605-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>(from reading the question, the questioner has already done this bit, but for the benefit of anyone else coming here):</p>
<p>After installing a new map, you'll probably need to turn it on.</p>
<p>On the Nuvi 1300 in front of me, I have to select "tools / settings / map / info" and ensure that the box next to the map that you want to use is ticked.</p>
</div>
<div id="comment-28605-info" class="comment-info">
<span class="comment-age">(29 Nov '13, 15:45)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28592" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28592-form-container" class="comment-form-container">
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

<span id="28596"></span>

<div id="answer-container-28596" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28596-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28596-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-28596-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jedediah has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe your nüvi wont accept large SDHC cards (my 310 only accepts cards with max 2 Gb capacity)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Nov '13, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/0f5ffc3756c4662b9dfad80b7665ac6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ligfietser&#39;s gravatar image" />
<p><span>ligfietser</span><br />
<span class="score" title="2894 reputation points"><span>2.9k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="57 badges"><span class="bronze">●</span><span class="badgecount">57</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ligfietser has 8 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Nov '13, 11:16</strong> </span></p>
</div>
</div>
<div id="comments-container-28596" class="comments-container">
<span id="28598"></span>
<div id="comment-28598" class="comment">
<div id="post-28598-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Btw, latest firmware is v. 5.10 <a href="http://www8.garmin.com/support/download_details.jsp?id=3665">http://www8.garmin.com/support/download_details.jsp?id=3665</a></p>
</div>
<div id="comment-28598-info" class="comment-info">
<span class="comment-age">(29 Nov '13, 12:09)</span> <span class="comment-user userinfo">ligfietser</span>
</div>
</div>
<span id="28606"></span>
<div id="comment-28606" class="comment">
<div id="post-28606-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That'd be my guess as well. See also:</p>
<p><a href="https://groups.google.com/forum/#!topic/alt.satellite.gps.garmin/_LIdi5fXDpA">https://groups.google.com/forum/#!topic/alt.satellite.gps.garmin/_LIdi5fXDpA</a></p>
</div>
<div id="comment-28606-info" class="comment-info">
<span class="comment-age">(29 Nov '13, 15:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="29181"></span>
<div id="comment-29181" class="comment">
<div id="post-29181-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Thanks!</p>
<p>I ended up using <a href="http://garmin.openstreetmap.nl/">http://garmin.openstreetmap.nl/</a> to build a map that was relevant to my area and fit within 2GB.</p>
</div>
<div id="comment-29181-info" class="comment-info">
<span class="comment-age">(19 Dec '13, 03:55)</span> <span class="comment-user userinfo">jedediah</span>
</div>
</div>
</div>
<div id="comment-tools-28596" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28596-form-container" class="comment-form-container">
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

