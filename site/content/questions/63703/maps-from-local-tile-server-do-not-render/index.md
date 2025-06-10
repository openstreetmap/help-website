+++
type = "question"
title = "Maps from local tile server do not render"
description = '''I worked through the excellent guide on installing a tile server in Ubuntu 18.04. Frankly, this is one of the best guides I’ve ever used, and I’ve slogged through quite a few over the years. I ran into a couple of block walls at the end though. First, I want to say everything installed without any n...'''
date = "2018-05-24T17:44:00Z"
lastmod = "2019-11-17T02:04:00Z"
weight = 63703
keywords = [ "rendering", "humanitarian", "mod_tile", "tile_server" ]
aliases = [ "/questions/63703" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Maps from local tile server do not render](/questions/63703/maps-from-local-tile-server-do-not-render)

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
<span id="post-63703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63703-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I worked through the excellent guide on installing a tile server in Ubuntu 18.04. Frankly, this is one of the best guides I’ve ever used, and I’ve slogged through quite a few over the years.</p>
<p>I ran into a couple of block walls at the end though. First, I want to say everything installed without any noted errors. I did get a ton of warnings (like this: Warning: amenity-points.mss:2468:6 Styles do not match layer selector .text-low-zoom.) when running carto, but that seems to be about all.</p>
<p>I installed the Switcheroo Redirector extension in Chrome and pointed things towards my public ip address, but I keep getting Content Security Policy notices:</p>
<pre><code>Refused to load the image &#39;&lt;URL&gt;&#39; because it violates the following Content Security Policy directive: &quot;img-src &#39;self&#39; data: &lt;URL&gt; *.wp.com *.tile.openstreetmap.org *.tile.thunderforest.com *.openstreetmap.fr piwik.openstreetmap.org developer.mapquest.com”.</code></pre>
<p>Initially I thought this issue was related to my server (I’m no expert on CSP!) so I added mod_headers and added very permissive policy directives. Chrome continued to refuse to load the Humanitarian Layer, but it does load the other three layers. I’ve since concluded the CPS notifications were coming from OpenStreetMap instead.</p>
<p>I also threw together some html/css/javascript and used Leaflet to display a page. I did this with MapBox and it worked, so I’m confident my test code is acceptable. But, when I try to point towards my own server (same platform at this point), all I can get is a blank screen showing the map canvas without any graphics:</p>
<p><img src="https://help.openstreetmap.org/upfiles/PastedGraphic-1.png" alt="alt text" /></p>
<p>This occurs in both Chrome and Safari; neither browser reports any errors, all statuses are 200.</p>
<p>Syslog during an Apache start: May 24 07:59:58 ubuntu systemd<a href="https://help.openstreetmap.org/upfiles/PastedGraphic-1.png">1</a>: Starting The Apache HTTP Server... May 24 07:59:58 ubuntu apachectl[95797]: [Thu May 24 07:59:58.490304 2018] [tile:notice] [pid 95800:tid 140608967183296] Loading tile config ajt at /hot/ for zooms 0 - 20 from tile directory /var/lib/mod_tile with extension .png and mime type image/png May 24 07:59:58 ubuntu systemd<a href="https://help.openstreetmap.org/upfiles/PastedGraphic-1.png">1</a>: Started The Apache HTTP Server.</p>
<p>Contents of /var/lib/mod_tile/ajt:</p>
<p><img src="https://help.openstreetmap.org/upfiles/PastedGraphic-2.png" alt="alt text" /></p>
<p>I’m not sure how many of these directories should be here? I do want to say that when I try to use this link in Chrome w/ the extension, and I get the CSP notifications, if I click on one of the PNGs shown in the notification, I will get a tile to load and display. And, an additional folder gets created under /var/lib/mod_tile/ajt. I assume from this that my actual renderer works?</p>
<p>Does this mean my problem is in how my Apache server is handing off the work to the tile server? Is my mod_tile broken?</p>
<p>Here is my output from <a href="http://ipaddress/mod_tile">http://ipaddress/mod_tile</a> after loading two png files using the method I described two paragraphs above.</p>
<pre><code>NoResp200: 2
NoResp304: 0
NoResp404: 0
NoResp503: 0
NoResp5XX: 0
NoRespOther: 0
NoFreshCache: 1
NoOldCache: 0
NoVeryOldCache: 0
NoFreshRender: 1
NoOldRender: 0
NoVeryOldRender: 0
NoRespZoom00: 0
NoRespZoom01: 0
NoRespZoom02: 0
NoRespZoom03: 0
NoRespZoom04: 0
NoRespZoom05: 0
NoRespZoom06: 0
NoRespZoom07: 0
NoRespZoom08: 0
NoRespZoom09: 0
NoRespZoom10: 0
NoRespZoom11: 0
NoRespZoom12: 0
NoRespZoom13: 0
NoRespZoom14: 2
NoRespZoom15: 0
NoRespZoom16: 0
NoRespZoom17: 0
NoRespZoom18: 0
NoRespZoom19: 0
NoRespZoom20: 0
NoTileBufferReads: 2
DurationTileBufferReads: 126
NoTileBufferReadZoom00: 0
DurationTileBufferReadZoom00: 0
NoTileBufferReadZoom01: 0
DurationTileBufferReadZoom01: 0
NoTileBufferReadZoom02: 0
DurationTileBufferReadZoom02: 0
NoTileBufferReadZoom03: 0
DurationTileBufferReadZoom03: 0
NoTileBufferReadZoom04: 0
DurationTileBufferReadZoom04: 0
NoTileBufferReadZoom05: 0
DurationTileBufferReadZoom05: 0
NoTileBufferReadZoom06: 0
DurationTileBufferReadZoom06: 0
NoTileBufferReadZoom07: 0
DurationTileBufferReadZoom07: 0
NoTileBufferReadZoom08: 0
DurationTileBufferReadZoom08: 0
NoTileBufferReadZoom09: 0
DurationTileBufferReadZoom09: 0
NoTileBufferReadZoom10: 0
DurationTileBufferReadZoom10: 0
NoTileBufferReadZoom11: 0
DurationTileBufferReadZoom11: 0
NoTileBufferReadZoom12: 0
DurationTileBufferReadZoom12: 0
NoTileBufferReadZoom13: 0
DurationTileBufferReadZoom13: 0
NoTileBufferReadZoom14: 2
DurationTileBufferReadZoom14: 126
NoTileBufferReadZoom15: 0
DurationTileBufferReadZoom15: 0
NoTileBufferReadZoom16: 0
DurationTileBufferReadZoom16: 0
NoTileBufferReadZoom17: 0
DurationTileBufferReadZoom17: 0
NoTileBufferReadZoom18: 0
DurationTileBufferReadZoom18: 0
NoTileBufferReadZoom19: 0
DurationTileBufferReadZoom19: 0
NoTileBufferReadZoom20: 0
DurationTileBufferReadZoom20: 0
NoRes200Layer/hot/: 2
NoRes404Layer/hot/: 0</code></pre>
<p>I’m concluding from this that my web server is not handing off to mod_tile, but I don’t know why, nor am I sure what troubleshooting step I can take next.</p>
<p>Any help would be greatly appreciated! I hope to hear back from you soon. In the meantime, I’ll start trying to look closer at mod_tile, and running renderd with more logging.</p>
<p>UPDATE:</p>
<p>I installed and configure munin to provide stats. I'm getting nothing from renderd:</p>
<p><img src="https://help.openstreetmap.org/upfiles/renderd_output.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-humanitarian" rel="tag" title="see questions tagged &#39;humanitarian&#39;">humanitarian</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-tile_server" rel="tag" title="see questions tagged &#39;tile_server&#39;">tile_server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '18, 17:44</strong></p>
<img src="https://secure.gravatar.com/avatar/9d2fa479c7f7984fd8fd435b2badbc4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tim_rohrer&#39;s gravatar image" />
<p><span>tim_rohrer</span><br />
<span class="score" title="81 reputation points">81</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tim_rohrer has one accepted answer">100%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 May '18, 19:50</strong> </span></p>
</div>
</div>
<div id="comments-container-63703" class="comments-container">
<span id="63706"></span>
<div id="comment-63706" class="comment">
<div id="post-63706-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've added an answer at <a href="https://help.openstreetmap.org/questions/63690/tiles-not-creating">https://help.openstreetmap.org/questions/63690/tiles-not-creating</a> - based largely on what you have found out!</p>
<p>In your case the fact that tiles are getting generated (as the "ls -al" shows) means that the link to mod_tile is working, but as you've since found the CSP (I think) is stopping Chromium from serving tiles.</p>
</div>
<div id="comment-63706-info" class="comment-info">
<span class="comment-age">(24 May '18, 18:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63713"></span>
<div id="comment-63713" class="comment">
<div id="post-63713-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately, when I created my own leaflet-based site, and tested against my local server, I still only get the blank screen shown above.</p>
<p>In my server, CSP is not active. No errors or issues are noted in the browser.</p>
<p>I'm still working to pore through more logs, but not getting much to speak of.</p>
</div>
<div id="comment-63713-info" class="comment-info">
<span class="comment-age">(24 May '18, 19:02)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="63718"></span>
<div id="comment-63718" class="comment">
<div id="post-63718-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does your leaflet-based site work with osm's tile servers?</p>
</div>
<div id="comment-63718-info" class="comment-info">
<span class="comment-age">(24 May '18, 20:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63719"></span>
<div id="comment-63719" class="comment">
<div id="post-63719-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tested against MapBox, yes I'm confident my code is acceptable. Do you think there is something different that should cause me to try and point towards osm's tile servers directly?</p>
<p>I'm in the process of redownloading shape files since, well, I don't know what else to try.</p>
</div>
<div id="comment-63719-info" class="comment-info">
<span class="comment-age">(24 May '18, 20:54)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="63742"></span>
<div id="comment-63742" class="comment">
<div id="post-63742-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I still have not gotten this figured out, and mucking with the shape files made things worse. I've started over, and we'll see how it goes.</p>
<p>I'm still curious about the warnings I get with carto, although I've been told those shouldn't be a factor.</p>
<p>On a related note, what are the roles of the .lua and .style files used in the osm2pgsql process? Do they contain data that is actually imported into the gis database? Ultimately, if there is a problem with the openstreetmap-carto configuration, does that mean the database needs to be regenerated?</p>
<p>Any known tests for this?</p>
</div>
<div id="comment-63742-info" class="comment-info">
<span class="comment-age">(25 May '18, 19:07)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="63743"></span>
<div id="comment-63743" class="comment not_top_scorer">
<div id="post-63743-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The .style file (such as <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.style">this one</a>) determines what database columns are created, and the .lua file (such as <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/openstreetmap-carto.lua">here</a>) allows fine-grained control over data as it is imported.</p>
<p>I've you've been using the lua transforms to move OSM data into a different column then yes, you might need to reload data after changing a .lua file. If you've not changed that you won't need to, though.</p>
<p>The bit of the <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">switch2osm guide</a> that says "Point a web browser at: <a href="http://yourserveripaddress/hot/0/0/0.png">http://yourserveripaddress/hot/0/0/0.png"</a> is the basic test to check that your tile server's working.</p>
<p>Another thing that you might try is (on one session) "sudo tail -f /var/log/syslog" and on another "sudo /etc/init.d/renderd restart"</p>
</div>
<div id="comment-63743-info" class="comment-info">
<span class="comment-age">(25 May '18, 21:34)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63751"></span>
<div id="comment-63751" class="comment not_top_scorer">
<div id="post-63751-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>. I just set up another server and ran through the setup process. Basically the same, although I created a different user.</p>
<p>I am able to display the /hot/0/0/0.png, so I'm glad to hear your comment there.</p>
<p>Maybe I need to start a new question and post some code, but I've run my JS against MapBox and it works. So, that leads me to think my URL template is wrong/misunderstood? The forms I've tried that don't produce errors include: http://&lt;internalip&gt;/#map=13/40.3743/49.7134 and http://&lt;internalip&gt;#map=13/40.373/49.7134.</p>
<p>To confirm, I should be able to files served up to the user on the node as the tile server, correct?</p>
</div>
<div id="comment-63751-info" class="comment-info">
<span class="comment-age">(26 May '18, 02:18)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
</div>
<div id="comment-tools-63703" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63703-form-container" class="comment-form-container">
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

<span id="63752"></span>

<div id="answer-container-63752" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63752-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am happy to report I figured it out. As <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> pointed out, the successful loading of <code>0/0/0.png</code> is a good indication that the tile server is working. This caused me to return to look closer at the leaflet.js code I had cobbled together. In hindsight, I think I should have caught this earlier.</p>
<p>The URL Template is where I found my error. Although I didn't see this in the leaflet.js documentation, the lat, lng, and zoom values are automatically picked up from the <code>setView</code> function of <code>L.map</code>, and are not explicitly stated in <code>L.tileLayer</code>. In fact, <code>L.tileLayer</code> is (as it does say in the documentation) a template; it turns out it is one that automatically (if you will) populates.</p>
<p>Perhaps this will be of help to someone in the future.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 May '18, 05:07</strong></p>
<img src="https://secure.gravatar.com/avatar/9d2fa479c7f7984fd8fd435b2badbc4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tim_rohrer&#39;s gravatar image" />
<p><span>tim_rohrer</span><br />
<span class="score" title="81 reputation points">81</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tim_rohrer has one accepted answer">100%</span></p>
</img>
</div>
</div>
<div id="comments-container-63752" class="comments-container">
<span id="71679"></span>
<div id="comment-71679" class="comment">
<div id="post-71679-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So what should I do to correct this? I'm having the same issues but didn't understood how to solve it.</p>
</div>
<div id="comment-71679-info" class="comment-info">
<span class="comment-age">(16 Nov '19, 19:40)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
<span id="71680"></span>
<div id="comment-71680" class="comment">
<div id="post-71680-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Carlos, do you have a public link to your setup to inspect you leaflet code? That would be the easiest way to help you out. Otherwise (if it's small) just post your leaflet code here or at paste bin or somewhere were we can have a look.</p>
</div>
<div id="comment-71680-info" class="comment-info">
<span class="comment-age">(16 Nov '19, 20:40)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="71683"></span>
<div id="comment-71683" class="comment">
<div id="post-71683-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The Leaflet file is the raw one used by the tutorial <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/</a></p>
<p>I just posted my question in another topic to don't make a mess <a href="https://help.openstreetmap.org/questions/71682/private-tile-server-not-rendering">https://help.openstreetmap.org/questions/71682/private-tile-server-not-rendering</a></p>
</div>
<div id="comment-71683-info" class="comment-info">
<span class="comment-age">(17 Nov '19, 02:04)</span> <span class="comment-user userinfo">carlosguedes</span>
</div>
</div>
</div>
<div id="comment-tools-63752" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63752-form-container" class="comment-form-container">
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

