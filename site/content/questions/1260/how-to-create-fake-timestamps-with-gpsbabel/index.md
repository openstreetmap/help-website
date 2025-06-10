+++
type = "question"
title = "How to create fake timestamps with gpsbabel?"
description = '''I am trying to use the below command to process some NMEA files, but it&#x27;s resulting in trackfilter-init: Track points badly ordered (timestamp)! ../gpsbabel/gpsbabel &#92;  -i nmea -f $DATE.nmea &#92;  -x track,pack,sdistance=0.5k,faketime=f19780705200000+2 &#92;  -x transform,wpt=trk,del &#92;  -x radius,distance=...'''
date = "2010-10-22T02:10:00Z"
lastmod = "2010-10-22T05:20:00Z"
weight = 1260
keywords = [ "gpsbabel", "timestamps", "faketime" ]
aliases = [ "/questions/1260" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to create fake timestamps with gpsbabel?](/questions/1260/how-to-create-fake-timestamps-with-gpsbabel)

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
<span id="post-1260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1260-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-1260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to use the below command to process some NMEA files, but it's resulting in <code>trackfilter-init: Track points badly ordered (timestamp)!</code></p>
<pre><code>../gpsbabel/gpsbabel \
    -i nmea -f $DATE.nmea \
    -x track,pack,sdistance=0.5k,faketime=f19780705200000+2 \
    -x transform,wpt=trk,del \
    -x radius,distance=20K,lat=-31.995815,lon=115.73512,nosort,exclude \
    -x transform,trk=wpt,del \
    -o gpx -F $DATE.gpx</code></pre>
<p>Can anyone shed some light on what I'm doing wrong?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gpsbabel" rel="tag" title="see questions tagged &#39;gpsbabel&#39;">gpsbabel</span> <span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span> <span class="post-tag tag-link-faketime" rel="tag" title="see questions tagged &#39;faketime&#39;">faketime</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '10, 02:10</strong></p>
<img src="https://secure.gravatar.com/avatar/51b9455e1dba4db831de473436c989f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samwilson&#39;s gravatar image" />
<p><span>samwilson</span><br />
<span class="score" title="336 reputation points">336</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samwilson has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-1260" class="comments-container">
&#10;</div>
<div id="comment-tools-1260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1260-form-container" class="comment-form-container">
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

<span id="1264"></span>

<div id="answer-container-1264" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1264-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-1264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Okay, I've got it all sorted. It seems a bit hacky, so if anyone's got any suggestions I'm open to them.</p>
<pre><code>../gpsbabel/gpsbabel \
    -D -w -t \
    -i nmea -f $DATE.nmea \
    -x track,faketime=f19700101000001+1 \
    -x track,faketime=19700101000001 \
    -x track,move=+1s \
    -x track,pack,sdistance=3k \
    -x transform,wpt=trk,del \
    -x radius,distance=20K,lat=-31.995815,lon=115.73512,nosort,exclude \
    -x transform,trk=wpt,del \
    -o gpx -F $DATE.gpx</code></pre>
<p>This</p>
<ul>
<li>modifies all timestamps (the two <code>faketime</code> filters are because the first one removes the <code>&lt;time&gt;</code> element from the first trackpoint; weird);</li>
<li>then splits into separate track segments where points are more than 3km apart;</li>
<li>and lastly deletes everything within 20km of (roughly) the mouth of the Swan River (i.e. metro stuff that is already well-mapped).</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '10, 05:20</strong></p>
<img src="https://secure.gravatar.com/avatar/51b9455e1dba4db831de473436c989f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samwilson&#39;s gravatar image" />
<p><span>samwilson</span><br />
<span class="score" title="336 reputation points">336</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samwilson has one accepted answer">20%</span></p>
</div>
</div>
<div id="comments-container-1264" class="comments-container">
&#10;</div>
<div id="comment-tools-1264" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1264-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1262"></span>

<div id="answer-container-1262" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1262-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is suggested to use</p>
<p>-x track,start=19700101000000</p>
<p>to start a track file timestamp at 1970 Jan 01, 00:00:00 in the new OpenStreetMap book by Jonathan Bennett. This example is from a free chapter, here.</p>
<p><a href="http://www.packtpub.com/article/openstreetmap-gathering-data-using-gps">http://www.packtpub.com/article/openstreetmap-gathering-data-using-gps</a></p>
<p>Both new OSM books are worth having. <a href="http://weait.com/content/two-new-osm-books">http://weait.com/content/two-new-osm-books</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '10, 02:47</strong></p>
<img src="https://secure.gravatar.com/avatar/d90ea04df82d77f534659f08894dd889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Weait&#39;s gravatar image" />
<p><span>Richard Weait</span><br />
<span class="score" title="3044 reputation points"><span>3.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="34 badges"><span class="silver">●</span><span class="badgecount">34</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Weait has 8 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-1262" class="comments-container">
<span id="1263"></span>
<div id="comment-1263" class="comment">
<div id="post-1263-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I saw that page, but I think <code>start</code> is just to tell it to ignore times before that date. I tried whittling down my command, and am getting <code>'faketime=f19700101000000' is an unknown option to track.</code> So I think I might just give up on changing the timestamps!</p>
</div>
<div id="comment-1263-info" class="comment-info">
<span class="comment-age">(22 Oct '10, 03:13)</span> <span class="comment-user userinfo">samwilson</span>
</div>
</div>
</div>
<div id="comment-tools-1262" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1262-form-container" class="comment-form-container">
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

