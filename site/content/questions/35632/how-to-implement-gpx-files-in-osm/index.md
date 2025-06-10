+++
type = "question"
title = "how to implement gpx-files in OSM"
description = '''If I implement a gpx track from a file of my harddisk to an OpenLayer it works great as long as the gpx file is in the same directory or in a directory down. I receive the map from the internet and the track from the harddisk can be seen. var GPXVariable_1 = new OpenLayers.Layer.Vector(&quot;Alpspitze&quot;, ...'''
date = "2014-08-07T17:56:00Z"
lastmod = "2014-08-08T12:46:00Z"
weight = 35632
keywords = [ "track", "openlayers", "gpx", "url" ]
aliases = [ "/questions/35632" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to implement gpx-files in OSM](/questions/35632/how-to-implement-gpx-files-in-osm)

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
<span id="post-35632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35632-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I implement a gpx track from a file of my harddisk to an OpenLayer it works great as long as the gpx file is in the same directory or in a directory down. I receive the map from the internet and the track from the harddisk can be seen.</p>
<p>var GPXVariable_1 = new OpenLayers.Layer.Vector("Alpspitze", {</p>
<pre><code>strategies: [new OpenLayers.Strategy.Fixed()], protocol: new OpenLayers.Protocol.HTTP({
url:&quot;Alpspitze.gpx&quot;, format: new OpenLayers.Format.GPX()
        }),  // works</code></pre>
<p>... url:"directory_x/Alpspitze.gpx" // works</p>
<p>If I try to implement a gpx file that is in a different directory structure, it doesn't work.</p>
<p>... url:"../../directory_y/directory_z/Alpspitze.gpx" // doesn't work</p>
<p>What am I doing wrong? What is the correct syntax for the address?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Aug '14, 17:56</strong></p>
<img src="https://secure.gravatar.com/avatar/b979098350df4e6b584bdabdf353382f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flegar&#39;s gravatar image" />
<p><span>flegar</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flegar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35632" class="comments-container">
&#10;</div>
<div id="comment-tools-35632" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35632-form-container" class="comment-form-container">
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

<span id="35641"></span>

<div id="answer-container-35641" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35641-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe it is a security mechanism of the browser to prevent JavaScript code to read your whole file system and independent on OpenLayers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '14, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/9c2804a11ecb10bbf42653cfe9189e90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarkusHD&#39;s gravatar image" />
<p><span>MarkusHD</span><br />
<span class="score" title="375 reputation points">375</span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarkusHD has one accepted answer">12%</span></p>
</div>
</div>
<div id="comments-container-35641" class="comments-container">
&#10;</div>
<div id="comment-tools-35641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35641-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35643"></span>

<div id="answer-container-35643" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35643-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the meantime, I've got an answer from a different forum.</p>
<p>Unfortunatelly there ist a restriction that allows local documents having access to other local documents in the <strong>same directory and in subdirectories</strong>, but not directory listings.</p>
<p>When I change the config:about (Firefox) <strong>security.fileuri.origin_policy</strong> to <strong>false</strong>, the track gets visible although it is implemented from a different file tree.</p>
<p>Conclusion: Due to the security police of browsers I have to rearrange my directory.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '14, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/b979098350df4e6b584bdabdf353382f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flegar&#39;s gravatar image" />
<p><span>flegar</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flegar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35643" class="comments-container">
&#10;</div>
<div id="comment-tools-35643" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35643-form-container" class="comment-form-container">
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

