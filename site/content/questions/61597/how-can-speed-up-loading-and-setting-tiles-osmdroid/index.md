+++
type = "question"
title = "How can speed up loading and setting tiles - OSMDROID"
description = '''Hi to every one, i&#x27;m creating an app android that load a grib data from file and set the color of tiles from grib data that i loaded. But this code is very slow. How can speed up this? try {  gribFileTileSource.setRecord(1);  for (int j=0;j&amp;lt;tileSize;j++) {  lat=minLat+j*dLat;  for (int i=0;i&amp;lt;t...'''
date = "2018-01-12T10:55:00Z"
lastmod = "2018-01-12T12:46:00Z"
weight = 61597
keywords = [ "android", "osmdroid", "java" ]
aliases = [ "/questions/61597" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can speed up loading and setting tiles - OSMDROID](/questions/61597/how-can-speed-up-loading-and-setting-tiles-osmdroid)

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
<span id="post-61597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61597-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi to every one, i'm creating an app android that load a grib data from file and set the color of tiles from grib data that i loaded. But this code is very slow. How can speed up this?</p>
<pre><code>try {
                gribFileTileSource.setRecord(1);
                for (int j=0;j&lt;tileSize;j++) {
                    lat=minLat+j*dLat;
                    for (int i=0;i&lt;tileSize;i++) {
                        lon=minLon+i*dLon;
                        //Log.d(LOG_TAG,&quot;lon:&quot;+lon+&quot; lat:&quot;+lat);
                        u=gribFileTileSource.getValue(lat,lon);
                        color=gribFileTileSource.getColor(u);
                        bitmap.setPixel(i,tileSize-j-1,color);
                    }
                }
thanks in advance</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jan '18, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/e223fecb7d889290f2829b9b4b6f0b21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pasquale22&#39;s gravatar image" />
<p><span>Pasquale22</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pasquale22 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61597" class="comments-container">
<span id="61602"></span>
<div id="comment-61602" class="comment">
<div id="post-61602-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>At first glance perhaps <a href="https://gis.stackexchange.com/questions/">https://gis.stackexchange.com/questions/</a> would be more likely to find someone who can answer a question like this?</p>
</div>
<div id="comment-61602-info" class="comment-info">
<span class="comment-age">(12 Jan '18, 12:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-61597" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61597-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

