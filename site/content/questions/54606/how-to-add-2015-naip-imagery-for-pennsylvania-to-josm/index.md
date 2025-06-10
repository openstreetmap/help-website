+++
type = "question"
title = "How to add 2015 NAIP Imagery for Pennsylvania to JOSM"
description = '''I can&#x27;t speak for all of America&#x27;s Bing imagery, but in Pennsylvania, the imagery is often horribly outdated (5-6+ years old). I&#x27;ve often tried to use USGS Large Scale Imagery, but most of the time it&#x27;s so slow that it&#x27;s unusable, or will just load a handful of tiles and just quit working. (This see...'''
date = "2017-02-10T21:53:00Z"
lastmod = "2017-02-11T17:34:00Z"
weight = 54606
keywords = [ "josm", "imagery", "error" ]
aliases = [ "/questions/54606" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to add 2015 NAIP Imagery for Pennsylvania to JOSM](/questions/54606/how-to-add-2015-naip-imagery-for-pennsylvania-to-josm)

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
<span id="post-54606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54606-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I can't speak for all of America's Bing imagery, but in Pennsylvania, the imagery is often horribly outdated (5-6+ years old). I've often tried to use USGS Large Scale Imagery, but most of the time it's so slow that it's unusable, or will just load a handful of tiles and just quit working. (This seems to be a server-side issue.)</p>
<p>So I tried to add the 2015 NAIP imagery for Pennsylvania, using the tutorial <a href="https://wiki.openstreetmap.org/wiki/National_Agriculture_Imagery_Program">here</a> for the WMS format. I went to <a href="https://gis.apfo.usda.gov/arcgis/rest/services/NAIP">this page</a>, clicked on the <a href="https://gis.apfo.usda.gov/arcgis/rest/services/NAIP/Pennsylvania_2015_1m/ImageServer">Pennsylvania link</a>, and selected WMS at the top left to be taken <a href="https://gis.apfo.usda.gov/arcgis/services/NAIP/Pennsylvania_2015_1m/ImageServer/WMSServer?request=GetCapabilities&amp;service=WMS">here</a>. I then took that URL and followed the directions in JOSM, clicking "Get Layers", selecting "Pennsylvania_2015_1m", and selecting "image/jpeg" as the image format.</p>
<p>After clicking OK on the popup and the Imagery preferences window, I went to add the imagery layer. However, I got a popup about some kind of wrong projection:</p>
<pre><code>The layer gis.apfo.usda.gov: Pennsylvania_2015_1m does not support the new projection EPSG:3857. Supported projections are: CRS:84, EPSG:0, EPSG:4326.
JOSM will use EPSG:4326 to query the server, but results may vary depending on the WMS server
Change the projection again or remove the layer.</code></pre>
<p>After clicking OK to enable the layer anyway, nothing apparent happens. When I zoom all the way out to view the entire world, the right half of the world is black-covered, with what seems to be three tiles appearing to the right of the edge of the world, only appearing as the red error "Error: Could not load image from tile server". At first I thought maybe the offset was just way wrong or something, but zooming in at various places does nothing.</p>
<p>What is going on with this, and why do I get this error despite following the instructions to the letter, with no mention at all of the possibility of this error? How can I make this imagery work in JOSM?</p>
<p>EDIT 1: See comment of mine below...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '17, 21:53</strong></p>
<img src="https://secure.gravatar.com/avatar/d029c1ae266568f5144a63a3b709ca49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roadsguy&#39;s gravatar image" />
<p><span>Roadsguy</span><br />
<span class="score" title="76 reputation points">76</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roadsguy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Feb '17, 04:07</strong> </span></p>
</div>
</div>
<div id="comments-container-54606" class="comments-container">
<span id="54607"></span>
<div id="comment-54607" class="comment">
<div id="post-54607-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I don't have any suggestion for debugging the issue, but I've just checked that the layer does work. Just today I published an attempt to make it easier to add the NAIP layers: <a href="https://maxerickson.github.io/NAIP_Remote/">https://maxerickson.github.io/NAIP_Remote/</a></p>
<p>But it's only really easier if the JOSM remote control is already setup.</p>
</div>
<div id="comment-54607-info" class="comment-info">
<span class="comment-age">(10 Feb '17, 23:39)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="54608"></span>
<div id="comment-54608" class="comment">
<div id="post-54608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="http://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a>, your links work nicely for me!</p>
</div>
<div id="comment-54608-info" class="comment-info">
<span class="comment-age">(11 Feb '17, 03:49)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="54609"></span>
<div id="comment-54609" class="comment">
<div id="post-54609-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That link got me a little farther than I was before. It added a layer that looked exactly like the weird half black, half off-the-world layer I got before, but occasionally while zoomed out I could see the image of Pennsylvania that would flicker on my screen as i panned around. Zooming in would render nothing at that location.</p>
<p>Curiously, this only happens in the option you linked to, maxerickson. Using the straight link from the OP, there's no Pennsylvania visible at all.</p>
<p>EDIT: See <a href="https://www.youtube.com/watch?v=xmNy6HJFZWQ">here</a> for a video demonstration of the problem. (If a picture is worth a thousand words, a video must be worth a million.) This is right after clicking the link in that page, which adds the layer.</p>
</div>
<div id="comment-54609-info" class="comment-info">
<span class="comment-age">(11 Feb '17, 04:07)</span> <span class="comment-user userinfo">Roadsguy</span>
</div>
</div>
<span id="54610"></span>
<div id="comment-54610" class="comment">
<div id="post-54610-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Occasionally the NAIP server is just down for me. Now I get the same error as you do above, but was able to get actual imagery which looks reasonably well aligned to Bing. I looked in PA randomly near Blairsville and Pittsburgh.</p>
</div>
<div id="comment-54610-info" class="comment-info">
<span class="comment-age">(11 Feb '17, 11:18)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
<span id="54611"></span>
<div id="comment-54611" class="comment">
<div id="post-54611-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As of today it's still misaligned and doesn't appear when zoomed in. However, I asked on the josm-dev mailing list, and someone pointed me to the following TMS link for the nationwide NAIP layer:</p>
<p>tms:http://{switch:a,b,c}.tile.openstreetmap.us/usgs_naip/{zoom}/{x}/{y}.jpg</p>
<p>This works fine when added with a high enough max zoom level, and is far more recent than Bing.</p>
</div>
<div id="comment-54611-info" class="comment-info">
<span class="comment-age">(11 Feb '17, 17:34)</span> <span class="comment-user userinfo">Roadsguy</span>
</div>
</div>
</div>
<div id="comment-tools-54606" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54606-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

