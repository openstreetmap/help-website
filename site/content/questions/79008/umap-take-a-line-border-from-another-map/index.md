+++
type = "question"
title = "umap take a line (border) from another map"
description = '''hello i like to take a border (district line) from another map in my own map. https://www.openstreetmap.org/relation/1990598#map=13/48.2261/16.2529 this orange borders i need in my map - how to do that? thank you , best regards, winionline'''
date = "2021-02-24T21:48:00Z"
lastmod = "2021-02-25T15:50:00Z"
weight = 79008
keywords = [ "umap" ]
aliases = [ "/questions/79008" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [umap take a line (border) from another map](/questions/79008/umap-take-a-line-border-from-another-map)

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
<span id="post-79008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79008-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-79008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello i like to take a border (district line) from another map in my own map.</p>
<p><a href="https://www.openstreetmap.org/relation/1990598#map=13/48.2261/16.2529">https://www.openstreetmap.org/relation/1990598#map=13/48.2261/16.2529</a></p>
<p>this orange borders i need in my map - how to do that?</p>
<p>thank you , best regards, winionline</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Feb '21, 21:48</strong></p>
<img src="https://secure.gravatar.com/avatar/da2926f04654618b497e34cbc9d20256?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="winfried&#39;s gravatar image" />
<p><span>winfried</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="winfried has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Feb '21, 10:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-79008" class="comments-container">
&#10;</div>
<div id="comment-tools-79008" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79008-form-container" class="comment-form-container">
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

<span id="79017"></span>

<div id="answer-container-79017" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-79017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79017-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-79017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>not sure this is the fastest way but you can go to <a href="http://overpass-turbo.eu/">Overpass Turbo</a> and write a query:</p>
<pre><code>[out:json][timeout:25];
rel(1990598);out geom;</code></pre>
<p>Then run it and when you see the results click on "data" on the top right and copy the whole data to a text file with ending .osm. In umap go to the import function and import that file into the desired layer.</p>
<p>This would be a one-time load. If you want to have the data always reflect the current version in OSM you need to create a linked layer. You can read on that on the <a href="https://forum.openstreetmap.org/viewtopic.php?pid=642046#p642046">OSM forum thread</a> where I got this solution from. I assume you can read German.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '21, 09:34</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-79017" class="comments-container">
<span id="79031"></span>
<div id="comment-79031" class="comment">
<div id="post-79031-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>workes very well!</p>
<p>you put me on the track. finaly i took this tutorial:</p>
<p><a href="https://olea.org/diario/2020/03/31/create_border_maps.html">https://olea.org/diario/2020/03/31/create_border_maps.html</a></p>
<p>and as i found the upload button</p>
<p><a href="https://wiki.openstreetmap.org/wiki/UMap/Guide/Import_data_files">https://wiki.openstreetmap.org/wiki/UMap/Guide/Import_data_files</a></p>
<p>all worked well.</p>
<p>thank you, winionline</p>
</div>
<div id="comment-79031-info" class="comment-info">
<span class="comment-age">(25 Feb '21, 15:50)</span> <span class="comment-user userinfo">winfried</span>
</div>
</div>
</div>
<div id="comment-tools-79017" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79017-form-container" class="comment-form-container">
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

