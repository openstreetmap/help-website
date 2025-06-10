+++
type = "question"
title = "Import single track entry as POI"
description = '''I have a gpx file with a single point, I&#x27;d like to import to OSM as a POI The file from my app looks like (from GPSLogger)  &amp;lt;trk&amp;gt; &amp;lt;trkseg&amp;gt; &amp;lt;trkpt lat=&quot;-XX.XXX&quot; lon=&quot;XXX.XXXXXX&quot;&amp;gt; &amp;lt;ele&amp;gt;99.0&amp;lt;/ele&amp;gt; &amp;lt;speed&amp;gt;0.0&amp;lt;/speed&amp;gt; &amp;lt;hdop&amp;gt;30.0&amp;lt;/hdop&amp;gt; &amp;lt;src&amp;gt;gps&amp;...'''
date = "2013-09-11T00:47:00Z"
lastmod = "2013-09-11T13:52:00Z"
weight = 26260
keywords = [ "gpx", "poi" ]
aliases = [ "/questions/26260" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Import single track entry as POI](/questions/26260/import-single-track-entry-as-poi)

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
<span id="post-26260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26260-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a gpx file with a single point, I'd like to import to OSM as a POI</p>
<p>The file from my app looks like (from GPSLogger)</p>
<p><code> &lt;trk&gt; &lt;trkseg&gt; &lt;trkpt lat="-XX.XXX" lon="XXX.XXXXXX"&gt; &lt;ele&gt;99.0&lt;/ele&gt; &lt;speed&gt;0.0&lt;/speed&gt; &lt;hdop&gt;30.0&lt;/hdop&gt; &lt;src&gt;gps&lt;/src&gt; &lt;sat&gt;6&lt;/sat&gt; &lt;time&gt;2013-09-10T18:52:02Z&lt;/time&gt; &lt;/trkpt&gt; </code></p>
<p>When I load this gpx file into OSM it takes me to the point, but there is no marker there.</p>
<p>How can I modify the file to be a POI? does gpsbabel support this ?</p>
<p>I've tried</p>
<pre><code>$&gt;gpsbabel -i gpx  -f infile.gpx -x transform,rte=wpt -o gpx -F route.gpx</code></pre>
<p>but this doesn't seem to help</p>
<p>My goal is to log tree locations , along with notes on their species, so I would go to the site, mark the tree, then hit "log single location", the app then saves a gpx, I can convert all of these files at one go after the fact if necessary.</p>
<p>Cheers, Tim</p>
<p>NOTE: I edited to fix my previously broken gpsbabel command line and attempted to fix to display xml correctly</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '13, 00:47</strong></p>
<img src="https://secure.gravatar.com/avatar/55f24a02ed681bc622c509f0e4a3d9ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iondiode&#39;s gravatar image" />
<p><span>iondiode</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iondiode has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '13, 02:52</strong> </span></p>
</div>
</div>
<div id="comments-container-26260" class="comments-container">
<span id="26261"></span>
<div id="comment-26261" class="comment">
<div id="post-26261-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: you can insert XML here. Indent the code with one tab (4 spaces would also work). Use a advanced (not notepad) text editor to easily indent. See <a href="/questions/25095/whats-wrong-with-my-pseudo-waypoint-fake-trackpoint-gpx-file-expected-state-trackpoint-got-state-unknown-xml-parser">that other question</a> for example. Note that the preview feature is showing a wrong preview.</p>
</div>
<div id="comment-26261-info" class="comment-info">
<span class="comment-age">(11 Sep '13, 01:10)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="26285"></span>
<div id="comment-26285" class="comment">
<div id="post-26285-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It would clarify to others if you could explain what you mean by "load this gpx file into OSM" and "drops a waypoint in OSM". How/where?</p>
</div>
<div id="comment-26285-info" class="comment-info">
<span class="comment-age">(11 Sep '13, 13:52)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26260-form-container" class="comment-form-container">
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

<span id="26262"></span>

<div id="answer-container-26262" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26262-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>arg! I hate answering my own question, but I think this was just an issue with my gpsbabel command</p>
<pre><code>$&gt;gpsbabel -i gpx  -f infile.gpx -x transform,trk=wpt -o gpx -F route.gpx</code></pre>
<p>drops a waypoint in OSM, which makes sense "transform my track into a list of waypoints" not the "rte" as I didn't have one.</p>
<p>Sorry to bother</p>
<p>Cheers, Tim</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '13, 02:56</strong></p>
<img src="https://secure.gravatar.com/avatar/55f24a02ed681bc622c509f0e4a3d9ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iondiode&#39;s gravatar image" />
<p><span>iondiode</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iondiode has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26262" class="comments-container">
<span id="26282"></span>
<div id="comment-26282" class="comment">
<div id="post-26282-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>To upload a .gpx to OSM it used to have to have at least one valid trackpoint in it (regardless of how many valid waypoints it had). Has that changed?</p>
</div>
<div id="comment-26282-info" class="comment-info">
<span class="comment-age">(11 Sep '13, 13:08)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26262" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26262-form-container" class="comment-form-container">
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

