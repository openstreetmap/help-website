+++
type = "question"
title = "How to set background imagery in JOSM"
description = '''I found this imagery and I want to use it in JOSM, but I can&#x27;t figure out how to do this. I&#x27;ve add tms:http://geoproxy.s-hertogenbosch.nl/PWArcGIS1/rest/services/externvrij/luchtopname/MapServer/tile/{zoom}/{x}/{y} to the TMS-settings, but all I got was grey tiles that say &quot;data not yet available&quot;. ...'''
date = "2014-02-18T14:23:00Z"
lastmod = "2014-02-18T16:07:00Z"
weight = 30824
keywords = [ "josm", "imagery" ]
aliases = [ "/questions/30824" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to set background imagery in JOSM](/questions/30824/how-to-set-background-imagery-in-josm)

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
<span id="post-30824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30824-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I found <a href="http://geoproxy.s-hertogenbosch.nl/PWArcGIS1/rest/services/externvrij/luchtopname/MapServer?f=jsapi">this</a> imagery and I want to use it in JOSM, but I can't figure out how to do this. I've add <code>tms:</code><a href="http://geoproxy.s-hertogenbosch.nl/PWArcGIS1/rest/services/externvrij/luchtopname/MapServer/tile/%7Bzoom%7D/%7Bx%7D/%7By%7D"><code>http://geoproxy.s-hertogenbosch.nl/PWArcGIS1/rest/services/externvrij/luchtopname/MapServer/tile/{zoom}/{x}/{y}</code></a> to the TMS-settings, but all I got was grey tiles that say "data not yet available".</p>
<p><a href="http://geoproxy.s-hertogenbosch.nl/PWArcGIS1/rest/services/externvrij/luchtopname/MapServer">Here is a page</a> with information that might be usefull for solving this problem.</p>
<p>I guess the problem has something to do with offset and/or different zoom-levels.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '14, 14:23</strong></p>
<img src="https://secure.gravatar.com/avatar/e6b568318790c50409e622ed23c9a211?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="de%20vries&#39;s gravatar image" />
<p><span>de vries</span><br />
<span class="score" title="221 reputation points">221</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="de vries has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30824" class="comments-container">
&#10;</div>
<div id="comment-tools-30824" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30824-form-container" class="comment-form-container">
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

<span id="30826"></span>

<div id="answer-container-30826" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30826-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-30826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="de vries has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is what you have to do:</p>
<ol>
<li>Make absolutely sure that this imagery is a legal source for OSM. If there is any doubt, do not continue.</li>
<li>Start JOSM, go to "Edit-&gt;Preferences" and select the WMS/TMS pane.</li>
<li>Click the "+WMS" button on the lower right.</li>
<li>Enter this URL (found behind the WMS link on your imagery page) into the box at the top: <a href="http://geoproxy.s-hertogenbosch.nl/pwarcgis1/services/externvrij/luchtopname/MapServer/WMSServer?request=GetCapabilities&amp;service=WMS">http://geoproxy.s-hertogenbosch.nl/pwarcgis1/services/externvrij/luchtopname/MapServer/WMSServer?request=GetCapabilities&amp;service=WMS</a></li>
<li>Click "Get Layers", select one that's appropriate, and close the dialog with "OK".</li>
</ol>
<p>Your new layer should now be available as a background layer from the "Imagery" menu.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '14, 16:07</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-30826" class="comments-container">
&#10;</div>
<div id="comment-tools-30826" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30826-form-container" class="comment-form-container">
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

