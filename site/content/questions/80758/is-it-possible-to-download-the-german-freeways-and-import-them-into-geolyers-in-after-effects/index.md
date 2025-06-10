+++
type = "question"
title = "Is it possible to download the German freeways and import them into Geolyers in After effects?"
description = '''I am completly new to OSM, please excuse my dumb questions. I am supposed to animate the freeways in the German state of Hessen in After Effects with the plugin Geolyers. With animate I mean drawing the freeways on the map one after the other. So I need the information as shapes or even better as pa...'''
date = "2021-06-28T10:54:00Z"
lastmod = "2021-06-28T17:06:00Z"
weight = 80758
keywords = [ "freeway", "download", "geolyers", "germany" ]
aliases = [ "/questions/80758" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to download the German freeways and import them into Geolyers in After effects?](/questions/80758/is-it-possible-to-download-the-german-freeways-and-import-them-into-geolyers-in-after-effects)

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
<span id="post-80758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80758-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am completly new to OSM, please excuse my dumb questions. I am supposed to animate the freeways in the German state of Hessen in After Effects with the plugin Geolyers. With animate I mean drawing the freeways on the map one after the other. So I need the information as shapes or even better as paths. Ideally in seperate files for each freeway and not one single file.</p>
<p>In geolayers it is very simple to connect two points with a path that follows the actual roads, so the geospatial information seems to be there. So far I haven`t found a way to download the freeways by their names (A49, A7 and so on).</p>
<p>I know that some people use QGIS to download OSM information and export them as KML oder Geojson. The tutorials I found on youtube did not cover how to solve my problem.</p>
<p>Thanks for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-freeway" rel="tag" title="see questions tagged &#39;freeway&#39;">freeway</span> <span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-geolyers" rel="tag" title="see questions tagged &#39;geolyers&#39;">geolyers</span> <span class="post-tag tag-link-germany" rel="tag" title="see questions tagged &#39;germany&#39;">germany</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '21, 10:54</strong></p>
<img src="https://secure.gravatar.com/avatar/b8090a8c3265804a9850bc091790f270?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zupppp&#39;s gravatar image" />
<p><span>Zupppp</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zupppp has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80758" class="comments-container">
&#10;</div>
<div id="comment-tools-80758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80758-form-container" class="comment-form-container">
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

<span id="80764"></span>

<div id="answer-container-80764" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80764-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use Overpass Turbo to query for the motorways. Either one by one like this:</p>
<pre><code>[out:json][timeout:25];
// fetch area “hassia” to search in
{{geocodeArea:hassia}}-&gt;.searchArea;
// gather results
(
  // query part for: “motorway”
  way[&quot;highway&quot;=&quot;motorway&quot;][ref=&quot;A 5&quot;](area.searchArea);
);
// print results
out geom;</code></pre>
<p>or all Hassian ones at once by removing the <code>[ref="A 5"]</code> piece.</p>
<p>I have no idea what format you can use to process the data so you might need to play a bit with the different output formats available from Overpass Turbo.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jun '21, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jun '21, 17:07</strong> </span></p>
</div>
</div>
<div id="comments-container-80764" class="comments-container">
&#10;</div>
<div id="comment-tools-80764" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80764-form-container" class="comment-form-container">
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

