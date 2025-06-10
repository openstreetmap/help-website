+++
type = "question"
title = "Is there a WMS layer I can add for North America satellite imagery for offline use in JOSM?"
description = '''I am trying to download OFFLINE satellite imagery for North America and I read that BING maps will not allow you to do this. Has anyone downloaded SATELLITE IMAGERY for North America? I can download orthoimagery from the NATIONAL MAP, very detailed, for free. I would just like a mechanism built into...'''
date = "2016-03-10T21:29:00Z"
lastmod = "2016-03-12T02:41:00Z"
weight = 48618
keywords = [ "download", "josm", "satellite", "imagery", "offline" ]
aliases = [ "/questions/48618" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a WMS layer I can add for North America satellite imagery for offline use in JOSM?](/questions/48618/is-there-a-wms-layer-i-can-add-for-north-america-satellite-imagery-for-offline-use-in-josm)

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
<span id="post-48618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48618-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to download OFFLINE satellite imagery for North America and I read that BING maps will not allow you to do this. Has anyone downloaded SATELLITE IMAGERY for North America?</p>
<p>I can download orthoimagery from the NATIONAL MAP, very detailed, for free. I would just like a mechanism built into JOSM that incorporates these features. Or is JOSM an ON-LINE only program?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-satellite" rel="tag" title="see questions tagged &#39;satellite&#39;">satellite</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Mar '16, 21:29</strong></p>
<img src="https://secure.gravatar.com/avatar/aaf8869d4cd5c92ca9831ebf99b07eca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gregcrago&#39;s gravatar image" />
<p><span>gregcrago</span><br />
<span class="score" title="69 reputation points">69</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gregcrago has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Mar '16, 22:16</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-48618" class="comments-container">
&#10;</div>
<div id="comment-tools-48618" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48618-form-container" class="comment-form-container">
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

<span id="48626"></span>

<div id="answer-container-48626" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48626-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM has a <a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/ImportImagePlugin">plugin that can read and display georeferenced imagery.</a> This will likely only work with smaller images.</p>
<p>If you want to download and use detailed imagery for a whole state or the whole US, you'd have to set up your own, local WMS server (e.g. UMN Map Server, Geoserver, QGIS server) to serve that imagery to JOSM. The WMS provides the indexing (and often also caching) required to cope with the large amount of data. You'll have to install the WMS and configure your imagery as a data source, set the right projection etc., and then you can access the WMS from JOSM. You won't need the Internet after you have that set up.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '16, 06:48</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Mar '16, 22:21</strong> </span></p>
</div>
</div>
<div id="comments-container-48626" class="comments-container">
<span id="48630"></span>
<div id="comment-48630" class="comment">
<div id="post-48630-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Since JOSM downloads imagery while I am using it, why can't it be configured to CACHE a boundary or polygon area and download it and keep it available for offline use?</p>
</div>
<div id="comment-48630-info" class="comment-info">
<span class="comment-age">(11 Mar '16, 14:06)</span> <span class="comment-user userinfo">gregcrago</span>
</div>
</div>
<span id="48634"></span>
<div id="comment-48634" class="comment">
<div id="post-48634-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Because doing so may well violate the usage terms of the map provider.</p>
</div>
<div id="comment-48634-info" class="comment-info">
<span class="comment-age">(11 Mar '16, 20:08)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48626" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48626-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48636"></span>

<div id="answer-container-48636" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48636-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>USGS Provides WMS endpoints for the many National Map layers:</p>
<p><a href="http://viewer.nationalmap.gov/services/">http://viewer.nationalmap.gov/services/</a></p>
<p>They have a help page:</p>
<p><a href="http://viewer.nationalmap.gov/help/HowTo.htm">http://viewer.nationalmap.gov/help/HowTo.htm</a></p>
<p>It mentions "There are no use restrictions on these services." I guess the layers under "Base Maps (Cached)" will be faster to download.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '16, 02:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-48636" class="comments-container">
&#10;</div>
<div id="comment-tools-48636" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48636-form-container" class="comment-form-container">
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

