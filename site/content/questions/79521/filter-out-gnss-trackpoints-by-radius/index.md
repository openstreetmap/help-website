+++
type = "question"
title = "Filter out GNSS trackpoints by radius"
description = '''Intro I&#x27;m doing first steps to create high precision GNSS tracks with a u-blox ZED-F9P multiband receiver. Currently I use gpspipe (from gpsd). Here is an example of real NMEA track: {&quot;class&quot;:&quot;VERSION&quot;,&quot;release&quot;:&quot;3.20&quot;,&quot;rev&quot;:&quot;3.20&quot;,&quot;proto_major&quot;:3,&quot;proto_minor&quot;:14} {&quot;class&quot;:&quot;DEVICES&quot;,&quot;devices&quot;:[{&quot;cl...'''
date = "2021-04-03T13:45:00Z"
lastmod = "2021-04-03T22:42:00Z"
weight = 79521
keywords = [ "gpsbabel", "gpsd", "nmea", "ublox" ]
aliases = [ "/questions/79521" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter out GNSS trackpoints by radius](/questions/79521/filter-out-gnss-trackpoints-by-radius)

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
<span id="post-79521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79521-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<h2 id="intro">Intro</h2>
<p>I'm doing first steps to create <a href="https://forum.openstreetmap.org/viewtopic.php?id=71718">high precision GNSS tracks</a> with a u-blox ZED-F9P multiband receiver. Currently I use <code>gpspipe</code> (from <code>gpsd</code>). Here is an example of real NMEA track:</p>
<p><code>{"class":"VERSION","release":"3.20","rev":"3.20","proto_major":3,"proto_minor":14} {"class":"DEVICES","devices":[{"class":"DEVICE","path":"/dev/ttyACM0","driver":"u-blox","subtype":"SW EXT CORE 1.00 (f10c36),HW 00190000","subtype1":",ROM BASE 0x118B2060,FWVER=HPG 1.13,PROTVER=27.12,MOD=ZED-F9P,GPS;GLO;GAL;BDS,SBAS;QZSS","activated":"2021-04-01T11:50:12.016Z","flags":1,"native":1,"bps":9600,"parity":"N","stopbits":1,"cycle":1.00,"mincycle":0.25}]} {"class":"WATCH","enable":true,"json":false,"nmea":true,"raw":0,"scaled":false,"timing":false,"split24":false,"pps":false} $GPZDA,115012.00,01,04,2021,00,00*64 $GPGGA,115012.00,5103.5795,N,01703.3372,E,2,25,0.55,126.10,M,17.230,M,,*64 $GPRMC,115012.00,A,5103.5795,N,01703.3372,E,13.6069,164.911,010421,-4.8,W*63 $GPGSA,A,3,2,6,12,24,25,29,32,,,,,,1.0,0.6,0.9*30 $GPGBS,115012.00,25.105,44.195,0.968,,,,*4E $GPZDA,115013.00,01,04,2021,00,00*65 $GPGGA,115013.00,5103.5760,N,01703.3387,E,2,25,0.55,126.08,M,17.230,M,,*6C $GPRMC,115013.00,A,5103.5760,N,01703.3387,E,13.1715,164.703,010421,-4.8,W*64 $GPGSA,A,3,2,6,12,24,25,29,32,,,,,,1.0,0.6,0.9*30 $GPGBS,115013.00,25.105,44.195,0.967,,,,*40 $GPZDA,115014.00,01,04,2021,00,00*62 $GPGGA,115014.00,5103.5725,N,01703.3402,E,2,25,0.51,126.04,M,17.230,M,,*68 $GPRMC,115014.00,A,5103.5725,N,01703.3402,E,12.8877,165.760,010421,-4.8,W*6F</code></p>
<p>Then I filter points by minimal HDOP and by number of satellites and save file in GPX format: <code>gpsbabel -t -i nmea -f gpspipe_2021-04-01.nmea -x discard,hdop=2 -x discard,sat=12 -o gpx -F gpspipe_2021-04-01_hdop2_sat12.gpx</code></p>
<h2 id="task">Task</h2>
<p>I want to remove some "noise" in the radius of 100 meters from my start point. I tried such command: <code>gpsbabel -t -i gpx -f gpspipe_2021-04-01_hdop2_sat12.gpx -x radius,distance=0.1K,lat=51.XXXX,lon=17.XXXX,nosort,exclude -o gpx -F gpspipe_2021-04-01_filtered.gpx</code></p>
<h2 id="problem">Problem</h2>
<p>But this command doesn't filter anything.</p>
<p>As I understand, I have to use <a href="https://wiki.openstreetmap.org/wiki/GPSBabel/Using_filters#Exclude_points_within_given_radius_.28ie._privacy_issue.29">this chain of filters</a>:</p>
<p><code>gpsbabel -i gpx -f in.gpx \ -x transform,wpt=trk,del \ -x radius,distance=1.1K,lat=40.01,lon=10.001,nosort,exclude \ -x transform,trk=wpt,del \ -o gpx -F out.gpx</code></p>
<p>But this creates a lot of useless information for almost <strong>every</strong> trackpoint:</p>
<p><code>&lt;name&gt;WPT612&lt;/name&gt; &lt;cmt&gt;WPT612&lt;/cmt&gt; &lt;desc&gt;WPT612&lt;/desc&gt;</code></p>
<p>Of course I can remove them by <code>sed</code> or some other tools.</p>
<h2 id="question">Question</h2>
<p>Maybe there is a better way to filter out trackpoints and do not lose information and do not generate useless tags?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gpsbabel" rel="tag" title="see questions tagged &#39;gpsbabel&#39;">gpsbabel</span> <span class="post-tag tag-link-gpsd" rel="tag" title="see questions tagged &#39;gpsd&#39;">gpsd</span> <span class="post-tag tag-link-nmea" rel="tag" title="see questions tagged &#39;nmea&#39;">nmea</span> <span class="post-tag tag-link-ublox" rel="tag" title="see questions tagged &#39;ublox&#39;">ublox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Apr '21, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/d16888595c6a4036ec8468e5c03d68bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vazhnov%20Alexey&#39;s gravatar image" />
<p><span>Vazhnov Alexey</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vazhnov Alexey has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Apr '21, 16:38</strong> </span></p>
</div>
</div>
<div id="comments-container-79521" class="comments-container">
<span id="79524"></span>
<div id="comment-79524" class="comment">
<div id="post-79524-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No solution with current GPSBabel code: <a href="https://github.com/gpsbabel/gpsbabel/issues/378">https://github.com/gpsbabel/gpsbabel/issues/378</a></p>
</div>
<div id="comment-79524-info" class="comment-info">
<span class="comment-age">(03 Apr '21, 18:19)</span> <span class="comment-user userinfo">Vazhnov Alexey</span>
</div>
</div>
</div>
<div id="comment-tools-79521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79521-form-container" class="comment-form-container">
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

<span id="79528"></span>

<div id="answer-container-79528" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79528-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Temporary solution:</p>
<p><code>sed -i -E -- '/\&lt;name\&gt;|\&lt;cmt\&gt;|\&lt;desc\&gt;/d' gpspipe_2021-04-01_filtered.gpx</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Apr '21, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/d16888595c6a4036ec8468e5c03d68bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vazhnov%20Alexey&#39;s gravatar image" />
<p><span>Vazhnov Alexey</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vazhnov Alexey has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79528" class="comments-container">
&#10;</div>
<div id="comment-tools-79528" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79528-form-container" class="comment-form-container">
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

