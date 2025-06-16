+++
type = "question"
title = "In JOSM is it possible to see GPX track waypoint details?"
description = '''OK, so I&#x27;ve opened a GPX file in JOSM (called tr1711a.gpx, created by a Garmin eTrex Vista if that&#x27;s relevant). I&#x27;ve downloaded OSM data and can see three layers over at the top-right in JOSM: Data Layer 1 (which seems to contain map data) Markers from tr1611a.gpx tr1611a.gpx I&#x27;d like to start editi...'''
date = "2011-07-16T21:27:00Z"
lastmod = "2020-08-03T10:23:00Z"
weight = 6368
keywords = [ "josm", "gpx", "waypoints" ]
aliases = [ "/questions/6368" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [In JOSM is it possible to see GPX track waypoint details?](/questions/6368/in-josm-is-it-possible-to-see-gpx-track-waypoint-details)

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
<span id="post-6368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6368-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>OK, so I've opened a GPX file in JOSM (called tr1711a.gpx, created by a Garmin eTrex Vista if that's relevant). I've downloaded OSM data and can see three layers over at the top-right in JOSM:</p>
<p>Data Layer 1 (which seems to contain map data) Markers from tr1611a.gpx tr1611a.gpx</p>
<p>I'd like to start editing the map, and in order to do that I'd like to get at the information in the GPX file waypoints, because among other things the symbol used indicates what it's a marker of. For example, the XML for the first one is:</p>
<pre><code>  &lt;wpt lat=&quot;53.1280730&quot; lon=&quot;-1.5204540&quot;&gt;
    &lt;ele&gt;190.0000000&lt;/ele&gt;
    &lt;name&gt;DOA045437&lt;/name&gt;
    &lt;cmt&gt;05-JUL-11 0&lt;/cmt&gt;
    &lt;desc&gt;05-JUL-11 0&lt;/desc&gt;
    &lt;sym&gt;Swimming Area&lt;/sym&gt;
    &lt;extensions&gt;
      &lt;gpxx:WaypointExtension xmlns:gpxx=&quot;http://www.garmin.com/xmlschemas/GpxExtensions/v3&quot;&gt;
        &lt;gpxx:DisplayMode&gt;SymbolAndName&lt;/gpxx:DisplayMode&gt;
      &lt;/gpxx:WaypointExtension&gt;
    &lt;/extensions&gt;
  &lt;/wpt&gt;</code></pre>
<p>(I've used "swimming area" as code to describe whether the road has a footpath / sidewalk on it)</p>
<p>Unfortunately all I see in JOSM is:</p>
<pre><code>x DOA045437 - 05-JUL-11 0</code></pre>
<p>which isn't a lot of help.</p>
<p>Oddly JOSM seems to be trying to display some waypoint symbols (the Garmin "Crossing" one is an example) but still doesn't seem to let you see the actual data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '11, 21:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>22 Oct '15, 09:28</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-6368" class="comments-container">
&#10;</div>
<div id="comment-tools-6368" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6368-form-container" class="comment-form-container">
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

<span id="6369"></span>

<div id="answer-container-6369" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6369-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-6369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>JOSM's gpx markers does not curently receive much artistic love. There are a very <a href="https://josm.openstreetmap.de/browser/josm/trunk/images/markers">limited set</a> of gpx marker icons avalable in JOSM. If you want to find/create new icons feel free to do so and they will probably be avalable in the next JOSM release.</p>
<p>To get your icons into the release add a <a href="https://josm.openstreetmap.de/newticket?type=enhancement&amp;summary=%5Bicons%5Dgpx%20waypoint%20icons">new bug report</a> and attach your icons to that. Make sure that the files are not licensed. A developer will then look at the icons and if they are good he will commit them to the source code where they will be distributed in the next release of JOSM.</p>
<p>For a referance you can see the <a href="https://josm.openstreetmap.de/ticket/5238">ticket</a> that uploaded the first icons.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '11, 23:08</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-6369" class="comments-container">
<span id="6370"></span>
<div id="comment-6370" class="comment">
<div id="post-6370-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks - the icons themselves I'm not too worried about; the contents of the XML tags would do. Is it possible to somehow select a waypoint and see the rest of the data (in addition to either "x DOA045437 - 05-JUL-11 0" or "&lt;icon&gt; DOA045437 - 05-JUL-11 0"?</p>
</div>
<div id="comment-6370-info" class="comment-info">
<span class="comment-age">(16 Jul '11, 23:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="6371"></span>
<div id="comment-6371" class="comment">
<div id="post-6371-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It is not possible to change the way JOSM displays waypoints without chenging parts of JOSM. The changes might not be what the other users want and therefore will not be implemented.</p>
<p>You might want to try replacing "&lt;sym" with "&lt;desc" everywhere within your file. This should make JOSM show the symbol name instead of the description.</p>
</div>
<div id="comment-6371-info" class="comment-info">
<span class="comment-age">(16 Jul '11, 23:42)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
<span id="75993"></span>
<div id="comment-75993" class="comment">
<div id="post-75993-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This answer is outdated, it now works as described by Klumbumbus and you can completely customize the waypoint information display, or choose to show everything</p>
</div>
<div id="comment-75993-info" class="comment-info">
<span class="comment-age">(03 Aug '20, 10:23)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-6369" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6369-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46023"></span>

<div id="answer-container-46023" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46023-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-46023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Waypoit labeling can be customized in the JOSM Preferences -&gt; Display Settings -&gt; GPS Points -&gt; Waypoit labeling (the page which directly opens, when you open the preference window).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Oct '15, 13:10</strong></p>
<img src="https://secure.gravatar.com/avatar/b904d75b8ea950f64710d2a8303cead7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Klumbumbus&#39;s gravatar image" />
<p><span>Klumbumbus</span><br />
<span class="score" title="543 reputation points">543</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Klumbumbus has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-46023" class="comments-container">
<span id="51057"></span>
<div id="comment-51057" class="comment">
<div id="post-51057-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8807/klumbumbus">@Klumbumbus</a> - I can't find this menu within Preferences (JOSM #10526). There are no waypoint labelling options in Preferences &gt; Display settings &gt; GPS Points...</p>
</div>
<div id="comment-51057-info" class="comment-info">
<span class="comment-age">(22 Jul '16, 07:36)</span> <span class="comment-user userinfo">wiltomap</span>
</div>
</div>
<span id="51058"></span>
<div id="comment-51058" class="comment">
<div id="post-51058-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10989/wiltomap"></a><a href="https://help.openstreetmap.org/users/10989/wiltomap">@wiltomap</a> I think you need to select the 'expert mode' box in the bottom left corner of the preferences page, then scroll down to see the 'waypoint labelling' section.</p>
</div>
<div id="comment-51058-info" class="comment-info">
<span class="comment-age">(22 Jul '16, 09:13)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="51060"></span>
<div id="comment-51060" class="comment">
<div id="post-51060-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I had not noticed this checkbox, thanks <a href="https://help.openstreetmap.org/users/7380/nevw"></a><a href="https://help.openstreetmap.org/users/7380/nevw">@nevw</a>! Therefore, I still have a problem with waypoints displaying correctly (cross symbol with label) if I load a local GPX file and not if I download a GPX file from OSM server (no cross symbols and no labels)... I might open a new post on this topic.</p>
</div>
<div id="comment-51060-info" class="comment-info">
<span class="comment-age">(22 Jul '16, 10:02)</span> <span class="comment-user userinfo">wiltomap</span>
</div>
</div>
<span id="75992"></span>
<div id="comment-75992" class="comment">
<div id="post-75992-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I just checked it and it works as described above by Klumbumbus. You go to settings, choose either "everything" from the dropdown, where it then shows name, cmt, sym, ele, desc. and "formatted waypoint offset", or you choose any of these, or "custom" which lets you enter a string what to show (e.g. "{sym} - {name}" to show the symbol and name text.</p>
</div>
<div id="comment-75992-info" class="comment-info">
<span class="comment-age">(03 Aug '20, 10:20)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-46023" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46023-form-container" class="comment-form-container">
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

