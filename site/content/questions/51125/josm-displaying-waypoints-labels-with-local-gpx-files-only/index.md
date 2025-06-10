+++
type = "question"
title = "JOSM displaying waypoints labels with local GPX files only?"
description = '''I&#x27;d like to display waypoints labels for a GPX file inside JOSM. This post could be considered as a duplicate of this post but it is more about local vs. uploaded GPX files and the way that waypoints display in JOSM. I have uploaded on OSM server a GPX file containing both tracks and waypoints (see ...'''
date = "2016-07-27T08:31:00Z"
lastmod = "2016-07-28T09:31:00Z"
weight = 51125
keywords = [ "josm", "gpx", "waypoints" ]
aliases = [ "/questions/51125" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM displaying waypoints labels with local GPX files only?](/questions/51125/josm-displaying-waypoints-labels-with-local-gpx-files-only)

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
<span id="post-51125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51125-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to display waypoints labels for a GPX file inside JOSM. This post could be considered as a duplicate of <a href="https://help.openstreetmap.org/questions/37093/josm-gpx-not-displaying-waypoints">this post</a> but it is more about local vs. uploaded GPX files and the way that waypoints display in JOSM.</p>
<p>I have uploaded on OSM server a GPX file containing both tracks and waypoints (<a href="https://www.openstreetmap.org/user/wiltomap/traces">see here</a> for testing, file name is <code>boulingrin_poitiers.gpx</code>). Waypoints are labelled with <code>name</code> tags (id number) and <code>desc</code> tags (custom name). JOSM perfectly displays either <code>name</code> or <code>desc</code> fields if I load the GPX file from my computer. On the other hand, it does not if I download the file in JOSM from OSM server. JOSM preferences for GPS Points are set identically for both cases...</p>
<p>Could anybody try my file or have an idea on this issue?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jul '16, 08:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0392d1e09809dd296ca425cb4d5f9996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiltomap&#39;s gravatar image" />
<p><span>wiltomap</span><br />
<span class="score" title="111 reputation points">111</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiltomap has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jul '16, 08:31</strong> </span></p>
</div>
</div>
<div id="comments-container-51125" class="comments-container">
<span id="51131"></span>
<div id="comment-51131" class="comment">
<div id="post-51131-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For info what I see when I invoke "edit" from the traces list (with JOSM running and remote control enabled, and when on the http osm site)is that the "map" part of the edit URL is honoured (e.g. <a href="http://www.openstreetmap.org/edit?gpx=2160201#map=19/53.14600/-1.35612">http://www.openstreetmap.org/edit?gpx=2160201#map=19/53.14600/-1.35612</a> ) but not the "gpx" part - I don't see the GPS trace at all (no waypoints, no track - nothing).</p>
</div>
<div id="comment-51131-info" class="comment-info">
<span class="comment-age">(27 Jul '16, 11:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51125" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51125-form-container" class="comment-form-container">
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

<span id="51140"></span>

<div id="answer-container-51140" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51140-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wiltomap has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>how do you "download the file in JOSM from OSM server"?</p>
<p>If you use the "GPS raw data" option in <a href="https://josm.openstreetmap.de/wiki/Help/Action/Download">"Download from OSM" dialogue</a>, then it only downloads a GPS tracks at some area (from <a href="https://api.openstreetmap.org/api/0.6/trackpoints">https://api.openstreetmap.org/api/0.6/trackpoints</a> – see <a href="https://wiki.openstreetmap.org/wiki/API_v0.6#GPS_traces">its description</a>). You will notice that you will not get a GPS waypoint layer but only a GPS track layer.</p>
<p>If you use "<a href="https://josm.openstreetmap.de/wiki/Help/Action/OpenLocation">Open Location</a>" and provide your <a href="https://www.openstreetmap.org/trace/2210235/data">https://www.openstreetmap.org/trace/2210235/data</a> as source, then you will get GPS waypoints and tracks.</p>
<p><span class="small">[note: I am talking of "tracks" in the meaning which gpx files use, not the OSM highway type "track"]</span></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '16, 06:35</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jul '16, 06:40</strong> </span></p>
</div>
</div>
<div id="comments-container-51140" class="comments-container">
<span id="51141"></span>
<div id="comment-51141" class="comment">
<div id="post-51141-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="http://help.openstreetmap.org/users/5179/aseerel4c26"></a><a href="http://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a>, this is the good way. I indeed used the "GPS raw data" option. I tested the "Open location" and it goes fine! I just had to modify the URL I gave in my post to follow your syntax: <a href="https://www.openstreetmap.org/user/wiltomap/traces"><code>https://www.openstreetmap.org/user/wiltomap/traces</code></a> becomes <a href="https://www.openstreetmap.org/trace/2210235/data"><code>https://www.openstreetmap.org/trace/2210235/data</code></a>.</p>
</div>
<div id="comment-51141-info" class="comment-info">
<span class="comment-age">(28 Jul '16, 07:02)</span> <span class="comment-user userinfo">wiltomap</span>
</div>
</div>
<span id="51142"></span>
<div id="comment-51142" class="comment">
<div id="post-51142-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10989/wiltomap"></a><a href="http://help.openstreetmap.org/users/10989/wiltomap">@wiltomap</a>: Yes, the URL you need to provide is just the "Download" link on the uploaded gpx file's detail page (right click, copy link address).</p>
</div>
<div id="comment-51142-info" class="comment-info">
<span class="comment-age">(28 Jul '16, 07:07)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="51143"></span>
<div id="comment-51143" class="comment">
<div id="post-51143-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10989/wiltomap">@wiltomap</a>: maybe this evening I will <em>think</em> about changing the description of the checkbox in JOSM from "GPS raw data" to "raw GPS traces (no waypoints)" (no, that's much too long), or something.</p>
</div>
<div id="comment-51143-info" class="comment-info">
<span class="comment-age">(28 Jul '16, 07:18)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="51144"></span>
<div id="comment-51144" class="comment">
<div id="post-51144-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@aseerecl4c26: that would be great! Thanks again for help.</p>
</div>
<div id="comment-51144-info" class="comment-info">
<span class="comment-age">(28 Jul '16, 09:31)</span> <span class="comment-user userinfo">wiltomap</span>
</div>
</div>
</div>
<div id="comment-tools-51140" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51140-form-container" class="comment-form-container">
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

