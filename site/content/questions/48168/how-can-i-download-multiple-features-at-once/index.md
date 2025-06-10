+++
type = "question"
title = "How can I download multiple features at once?"
description = '''Hi everyone. I have a big csv containing about 9600 lines with the following structure: way1:way2:way3 | pointGeom 100234171:277425069:102706559 | POINT(-117.738886 33.581471) way1:way2:way3 = OSM way IDs pointGeom = a point with known coordinates Is there an automated/semi-automated method to downl...'''
date = "2016-02-16T09:46:00Z"
lastmod = "2016-02-16T11:03:00Z"
weight = 48168
keywords = [ "qgis", "josm", "download", ".osm" ]
aliases = [ "/questions/48168" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I download multiple features at once?](/questions/48168/how-can-i-download-multiple-features-at-once)

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
<span id="post-48168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48168-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone.</p>
<p>I have a big csv containing about 9600 lines with the following structure:</p>
<p><strong>way1:way2:way3 | pointGeom</strong></p>
<p><strong>100234171:277425069:102706559 | POINT(-117.738886 33.581471)</strong></p>
<p>way1:way2:way3 = OSM way IDs</p>
<p>pointGeom = a point with known coordinates</p>
<p>Is there an automated/semi-automated method to download in the form of an OSM file (or in any other format that I can vizulize in QGIS or JOSM) all the ways that I have listed in my way1:way2:way3 column?</p>
<p>Hopefully I made my question clear.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qgis" rel="tag" title="see questions tagged &#39;qgis&#39;">qgis</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '16, 09:46</strong></p>
<img src="https://secure.gravatar.com/avatar/5adf0c254e0ecccabcf2d8250d74518b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mihaii&#39;s gravatar image" />
<p><span>mihaii</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mihaii has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Feb '16, 18:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-48168" class="comments-container">
&#10;</div>
<div id="comment-tools-48168" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48168-form-container" class="comment-form-container">
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

<span id="48170"></span>

<div id="answer-container-48170" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48170-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You want to download 30,000 ways with their node members (another 150,000 objects on average). While there are API calls that let you download a couple of objects at the same time, they are certainly not meant for such a download volume. You should download a planet file (or a country extract if all your ways are within the same country), and extract the information you need from there.</p>
<p>If you were looking for a smaller number of objects, the easiest way to load them all would probably be creating dummy versions for every way, like</p>
<pre><code>&lt;way id=&quot;1234&quot; version=&quot;1&quot; user=&quot;...&quot; ... /&gt;</code></pre>
<p>then if you open that file in JOSM and request to "update from server", JOSM will download the correct data for all the ways (and the matching nodes).</p>
<p>But as I said, don't do that for 30k ways.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '16, 11:03</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-48170" class="comments-container">
&#10;</div>
<div id="comment-tools-48170" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48170-form-container" class="comment-form-container">
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

