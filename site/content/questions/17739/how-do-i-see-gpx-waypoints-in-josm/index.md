+++
type = "question"
title = "How do I see GPX waypoints in JOSM"
description = '''I am trying to map an area from a GPX 1.1 file I collected on a trip (cannot easily return there). The GPX file was generated with OSMTracker for Android™ and contains both &amp;lt;wpt&amp;gt; and &amp;lt;trk&amp;gt;/&amp;lt;trkpt&amp;gt; tags. My &amp;lt;wpt&amp;gt; points contain text descriptions (&amp;lt;name&amp;gt; tags) of map feat...'''
date = "2012-11-16T04:13:00Z"
lastmod = "2013-02-03T07:07:00Z"
weight = 17739
keywords = [ "marker", "josm", "gpx", "waypoints" ]
aliases = [ "/questions/17739" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I see GPX waypoints in JOSM](/questions/17739/how-do-i-see-gpx-waypoints-in-josm)

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
<span id="post-17739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17739-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to map an area from a GPX 1.1 file I collected on a trip (cannot easily return there). The GPX file was generated with <a href="http://osmtracker-android.googlecode.com/">OSMTracker for Android™</a> and contains both &lt;wpt&gt; and &lt;trk&gt;/&lt;trkpt&gt; tags.</p>
<p>My &lt;wpt&gt; points contain text descriptions (&lt;name&gt; tags) of map features such as barriers and roads. Unfortunately the current JOSM doesn't seem to display them in any meaningful way, and all the menu items I can find for the resulting "marker" layer are focused on Audio mapping, which is just so irrelevant.</p>
<p>My searching came up with references to a setting named "Create non-audio markers when reading GPX", but I was unable to find this setting in the actual JOSM user interface. I also came across a lot of (bad) replies about how to set icons for imported Garmin GPX files with &lt;sym&gt; tags, but that is not what I have, just a bunch of plain &lt;name&gt; tags.</p>
<p>I have also tried converting the other GPX layer to a data layer, but it only includes the nameless &lt;trkpt&gt; nodes, not the named &lt;wpt&gt; nodes.</p>
<p>So what is the practical way to import GPX data to JOSM for use as the base of mapping features?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '12, 04:13</strong></p>
<img src="https://secure.gravatar.com/avatar/d148a0fb6c59569b86b2f3062dea5a61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbohmdk&#39;s gravatar image" />
<p><span>jbohmdk</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbohmdk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17739" class="comments-container">
<span id="17767"></span>
<div id="comment-17767" class="comment">
<div id="post-17767-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you would provide the file in question, I'd like to have a look at it. If you don't know how, put it to a one-klick-hoster like this one: <a href="http://ompldr.org/">http://ompldr.org/</a></p>
</div>
<div id="comment-17767-info" class="comment-info">
<span class="comment-age">(18 Nov '12, 17:18)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
<span id="17777"></span>
<div id="comment-17777" class="comment">
<div id="post-17777-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm using GPX OSMTracker for Android along with JOSM (v5576). I'm able to see the way points in JOSM.</p>
<p>The text way point from the gpx file looks as follows :</p>
<pre><code>    &lt; wpt lat=&quot;12.88459012&quot; lon=&quot;77.58261194&quot;&gt;
        &lt; ele&gt;846.7&lt; /ele&gt;
        &lt; time&gt;2012-11-17T12:43:28Z &lt; /time&gt;
        &lt; name&gt;&lt;![CDATA[bus stop]]&gt;&lt; /name&gt;
        &lt; sat&gt;9&lt;/sat&gt;
    &lt; /wpt&gt;</code></pre>
<p>Please ignore the spaces after the "&lt;" symbol, there are adde to make the XML visible. Did you try turning off the imagery or changing the colors of GPS points (Preferences -&gt; Display Settings -&gt; Colors)?</p>
</div>
<div id="comment-17777-info" class="comment-info">
<span class="comment-age">(19 Nov '12, 04:38)</span> <span class="comment-user userinfo">BlueTiger</span>
</div>
</div>
<span id="19441"></span>
<div id="comment-19441" class="comment">
<div id="post-19441-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For info, a couple of related questions - <a href="https://help.openstreetmap.org/questions/6368/in-josm-is-it-possible-to-see-gpx-track-waypoint-details">here</a> and <a href="https://help.openstreetmap.org/questions/7675/josm-is-it-possible-to-convert-an-individual-waypoint-in-a-gpx-file-to-a-node">here</a>.</p>
</div>
<div id="comment-19441-info" class="comment-info">
<span class="comment-age">(30 Jan '13, 12:30)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17739" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17739-form-container" class="comment-form-container">
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

<span id="19548"></span>

<div id="answer-container-19548" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19548-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, sorry for not returning to this forum sooner.</p>
<p>I found my own workaround before any answers came here, this is extremely clumsy, but seemed the only way I could see the waypoints and their names in JOSM:</p>
<ol>
<li>Convert the gpx file from LF to CRLF format with cygwin (only needed on Windows).</li>
<li>Use a text editor to create two copies of the file, one with waypoints only, one with trackpoints only.</li>
<li>Use GPSBabel to convert the wpt-only gpx file to an osm file.</li>
<li>In JOSM, import the waypoint osm file and the trackpoint gpx file as their own layers.</li>
<li>Now do the actual editing.</li>
</ol>
<p>I don't know why it worked for BlueTiger, as my waypoints look the same in the GPX and I was using the same JOSM version at the time. If this was about color settings, then the defaults must have been wrong in that version of JOSM.</p>
<p>As for the two links provided by user SomeOneElse, the first was another Garmin-gpx-symbol post of no relevance, but <a href="https://help.openstreetmap.org/questions/7675/josm-is-it-possible-to-convert-an-individual-waypoint-in-a-gpx-file-to-a-node">the other</a> was very similar to both my problems and solutions, except I cared about all the waypoints in the file, not just one.</p>
<p>I don't think I was using any satellite image overlays during the editing. So I cannot accept Glassman's "answer" as having any relevance.</p>
<p>I cannot retest right now as I don't have a working Java on the PC.</p>
<p>Here are some snippets from one of the (large) files in question:</p>
<pre><code>&lt; ?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; ?&gt;
&lt; gpx xmlns=&quot;http://www.topografix.com/GPX/1/1&quot; version=&quot;1.1&quot; creator=&quot;OSMTracker for Android™ - http://osmtracker-android.googlecode.com/&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot; xsi:schemaLocation=&quot;http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd &quot;&gt;
    &lt; wpt lat=&quot;55.41190083600891&quot; lon=&quot;11.560011318167248&quot;&gt;
        &lt; ele&gt;87.0&lt; /ele&gt;
        &lt; time&gt;2012-10-28T23:24:29Z&lt; /time&gt;
        &lt; name&gt;&lt; ![CDATA[School]]&gt;&lt; /name&gt;
        &lt; cmt&gt;&lt; ![CDATA[Accuracy: 5.0m]]&gt;&lt; /cmt&gt;
        &lt; sat&gt;7&lt; /sat&gt;
        &lt; hdop&gt;1.25&lt; /hdop&gt;
    &lt; /wpt&gt;
...
    &lt; trk&gt;
        &lt; name&gt;&lt; ![CDATA[Tracked with OSMTracker for Android™]]&gt;&lt; /name&gt;
        &lt; cmt&gt;&lt; ![CDATA[Warning: HDOP values aren&#39;t the HDOP as returned by the GPS device. They&#39;re approximated from the location accuracy in meters.]]&gt;&lt; /cmt&gt;
        &lt; trkseg&gt;
            &lt; trkpt lat=&quot;55.411865588216614&quot; lon=&quot;11.560238205932786&quot;&gt;
                &lt; ele&gt;70.0&lt; /ele&gt;
                &lt; time&gt;2012-10-28T23:24:02Z&lt; /time&gt;
                &lt; hdop&gt;8.75&lt; /hdop&gt;
            &lt; /trkpt&gt;
...
        &lt; /trkseg&gt;
    &lt; /trk&gt;
&lt; /gpx&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Feb '13, 07:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d148a0fb6c59569b86b2f3062dea5a61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbohmdk&#39;s gravatar image" />
<p><span>jbohmdk</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbohmdk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19548" class="comments-container">
&#10;</div>
<div id="comment-tools-19548" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19548-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19475"></span>

<div id="answer-container-19475" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19475-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try turning your background image (bing) off. You can also change the color of the gpx trace in Preferences. The light gray is really hard to read. So in Display Preferences, Colors Tab change gps marker to a brighter color. What is displayed is controlled in the GPS Tab. Look for Waypoint labeling.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jan '13, 01:20</strong></p>
<img src="https://secure.gravatar.com/avatar/131090595e5da40681c2f9bfabca395d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Glassman&#39;s gravatar image" />
<p><span>Glassman</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Glassman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19475" class="comments-container">
&#10;</div>
<div id="comment-tools-19475" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19475-form-container" class="comment-form-container">
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

