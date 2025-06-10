+++
type = "question"
title = "Filtering a region for street name extraction"
description = '''I&#x27;m trying to extract a list (in csv format) of street names from a city using OSMFilter and OSMConvert. Problem is, there&#x27;s no .osm file for said city, what I can find is just the .osm of the country and the province. How do you extract the name tag of the streets of just one city from an .osm file...'''
date = "2020-10-05T05:27:00Z"
lastmod = "2020-10-11T05:22:00Z"
weight = 76956
keywords = [ "streetnames", "osmconvert", "csv", "osmfilter", "extraction" ]
aliases = [ "/questions/76956" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering a region for street name extraction](/questions/76956/filtering-a-region-for-street-name-extraction)

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
<span id="post-76956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76956-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to extract a list (in csv format) of street names from a city using OSMFilter and OSMConvert. Problem is, there's no .osm file for said city, what I can find is just the .osm of the country and the province.</p>
<p>How do you extract the name tag of the streets of just one city from an .osm file of a bigger region? addr:city yields different results instead.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-extraction" rel="tag" title="see questions tagged &#39;extraction&#39;">extraction</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Oct '20, 05:27</strong></p>
<img src="https://secure.gravatar.com/avatar/71f61dbbe1a477635bed39e3a11cb8c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ceeslt&#39;s gravatar image" />
<p><span>ceeslt</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ceeslt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76956" class="comments-container">
&#10;</div>
<div id="comment-tools-76956" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76956-form-container" class="comment-form-container">
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

<span id="76965"></span>

<div id="answer-container-76965" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76965-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use a polygon specification with osmconvert (and also osmosis). The relevant .poly can be created using JOSM or QGIS (with a plugin). This is how the country files are produced in the first place (the Geofabrik Download site displays the polygons used).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Oct '20, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-76965" class="comments-container">
<span id="76997"></span>
<div id="comment-76997" class="comment">
<div id="post-76997-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the suggestion, I tried it but it turns out that my computer can't handle loading the file in JOSM. I finally managed to slice the area using BBBike. Is there any difference from extracting via JOSM result-wise?</p>
</div>
<div id="comment-76997-info" class="comment-info">
<span class="comment-age">(08 Oct '20, 01:37)</span> <span class="comment-user userinfo">ceeslt</span>
</div>
</div>
</div>
<div id="comment-tools-76965" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76965-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77038"></span>

<div id="answer-container-77038" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77038-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This can be done with the following Overpass Turbo script. You just need to change the city. You will have to do some cleaning after.</p>
<p><a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a></p>
<pre><code>[out:csv(&quot;name&quot;;false)];
area[name=&quot;Brownsville&quot;];
way(area)[highway][name];
out;</code></pre>
<p>met.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Oct '20, 05:22</strong></p>
<img src="https://secure.gravatar.com/avatar/6783b46d5425152bbb4fc48e90eb279a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdelatorre&#39;s gravatar image" />
<p><span>mdelatorre</span><br />
<span class="score" title="177 reputation points">177</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdelatorre has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77038" class="comments-container">
&#10;</div>
<div id="comment-tools-77038" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77038-form-container" class="comment-form-container">
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

