+++
type = "question"
title = "gpx file does not display waypoints in josm"
description = '''Hi, I&#x27;ve tried both OSMTracker and OpenGPSTracker for Android to generate gpx files. On opening them with josm version 3966-1 I cannot see any waypoints, just the grey line of my track which is apparently uneditable. Here a sample of my gpx file:  &amp;lt;gpx version=&quot;1.1&quot; creator=&quot;nl.sogeti.android.gps...'''
date = "2011-03-27T20:47:00Z"
lastmod = "2011-04-24T19:57:00Z"
weight = 4138
keywords = [ "uneditable", "gpx", "waypoints" ]
aliases = [ "/questions/4138" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [gpx file does not display waypoints in josm](/questions/4138/gpx-file-does-not-display-waypoints-in-josm)

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
<span id="post-4138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4138-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've tried both OSMTracker and OpenGPSTracker for Android to generate gpx files. On opening them with josm version 3966-1 I cannot see any waypoints, just the grey line of my track which is apparently uneditable.</p>
<p>Here a sample of my gpx file:</p>
&lt;gpx version="1.1" creator="nl.sogeti.android.gpstracker" xsi:schemalocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/gpx/1/1/gpx.xsd" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:gpx10="http://www.topografix.com/GPX/1/0" xmlns:ogt10="http://gpstracker.android.sogeti.nl/GPX/1/0"&gt; &lt;metadata&gt; &lt;time&gt;2011-03-01T14:17:31Z&lt;/time&gt; &lt;/metadata&gt; &lt;trk&gt; &lt;name&gt;Track 2011-03-01 15:17&lt;/name&gt; &lt;trkseg&gt; &lt;trkpt lat="47.6107058" lon="10.6137722"&gt; &lt;ele&gt;863.2999877929688&lt;/ele&gt; &lt;time&gt;2011-03-01T14:17:36Z&lt;/time&gt; &lt;extensions&gt; &lt;gpx10:speed&gt;1.1180340051651&lt;/gpx10:speed&gt; &lt;ogt10:accuracy&gt;13.0&lt;/ogt10:accuracy&gt; &lt;gpx10:course&gt;359.5&lt;/gpx10:course&gt;&lt;/extensions&gt; &lt;/trkpt&gt; . . .
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-uneditable" rel="tag" title="see questions tagged &#39;uneditable&#39;">uneditable</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Mar '11, 20:47</strong></p>
<img src="https://secure.gravatar.com/avatar/958f1e50af882f4c8181f61291764efd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="toad&#39;s gravatar image" />
<p><span>toad</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="toad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4138" class="comments-container">
&#10;</div>
<div id="comment-tools-4138" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4138-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="4139"></span>

<div id="answer-container-4139" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4139-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If i remember right the OSMTracker generates two different files for waypoints and trackspoints, like YYYYMMDD_HHMMSS-wp.gpx and YYYYMMDD_HHMMSS-tp.gpx. Are you sure you haven't missed to transfer and open the wp.gpx-file in JOSM?</p>
<p>Apparently the gpx-file above has no waypoints because there are no wpt-entries in it.</p>
<p>Generally there is no problem to have both trackpoints and waypoints in the same gpx-file, but it's convenient to have them separated because then you can toggle them individually in JOSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '11, 21:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Mar '11, 21:30</strong> </span></p>
</div>
</div>
<div id="comments-container-4139" class="comments-container">
<span id="4160"></span>
<div id="comment-4160" class="comment">
<div id="post-4160-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>JOSM creates separate layers for track and waypoints when reading in a GPX file containing both. It does that for me anyway.</p>
</div>
<div id="comment-4160-info" class="comment-info">
<span class="comment-age">(28 Mar '11, 22:19)</span> <span class="comment-user userinfo">tongro</span>
</div>
</div>
</div>
<div id="comment-tools-4139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4139-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4161"></span>

<div id="answer-container-4161" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4161-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know Open GPS Tracker, but regarding editing GPS traces in JOSM, it can be done. Right-click the GPX trace layer, select "convert to data layer", and the trace can now be edited. To convert it back to GPX, right-click the layer and select either "convert to GPX" or "export to GPX".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '11, 22:28</strong></p>
<img src="https://secure.gravatar.com/avatar/a8992ad9a83eacdd6388ed265d3f6921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tongro&#39;s gravatar image" />
<p><span>tongro</span><br />
<span class="score" title="701 reputation points">701</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tongro has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4161" class="comments-container">
<span id="4162"></span>
<div id="comment-4162" class="comment">
<div id="post-4162-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Tongro, you got the gist of what I was trying to do and say - many thanks!</p>
<p>I remember trying that option before and shying away from it because of the warning it gives. This time I ignored it and, weyhey, it worked :)</p>
</div>
<div id="comment-4162-info" class="comment-info">
<span class="comment-age">(28 Mar '11, 22:44)</span> <span class="comment-user userinfo">toad</span>
</div>
</div>
</div>
<div id="comment-tools-4161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4161-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4140"></span>

<div id="answer-container-4140" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4140-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for your quick answer.</p>
<p>Here is what I do: - stop tracking - select "share track" - send it to my email address</p>
<p>I've checked settings of both applications but do not see any reference to "waypoints" as such apart from how often I want to log my position. I double checked the files on my SD card and none of them have waypoints, only trackpoints!?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '11, 21:58</strong></p>
<img src="https://secure.gravatar.com/avatar/958f1e50af882f4c8181f61291764efd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="toad&#39;s gravatar image" />
<p><span>toad</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="toad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4140" class="comments-container">
<span id="4143"></span>
<div id="comment-4143" class="comment">
<div id="post-4143-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've never used Open GPS tracker, but from the screen shots at <a href="http://code.google.com/p/open-gpstracker/wiki/ScreenShots">http://code.google.com/p/open-gpstracker/wiki/ScreenShots</a> i guess that the Make Note-button is the one that creates waypoints. Have you used that button, or why do you expect some waypoints to be in the export?</p>
</div>
<div id="comment-4143-info" class="comment-info">
<span class="comment-age">(27 Mar '11, 22:39)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
</div>
<div id="comment-tools-4140" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4140-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4780"></span>

<div id="answer-container-4780" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4780-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Take your tcx file from the garmin and convert it to gpx using <a href="http://www.gpsvisualizer.com/">http://www.gpsvisualizer.com/</a> and then it should load properly in JOSM</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '11, 19:57</strong></p>
<img src="https://secure.gravatar.com/avatar/bbd68bc504bdcec00ca29d29931f9558?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hotbelgo&#39;s gravatar image" />
<p><span>Hotbelgo</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hotbelgo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4780" class="comments-container">
&#10;</div>
<div id="comment-tools-4780" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4780-form-container" class="comment-form-container">
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

