+++
type = "question"
title = "OSM data for Road/Lane Edges ?"
description = '''I want to get Road/Lane edges data (Lat/Long/Alt) from the Open Street Map so, that I can overlay rendered edges on a video overlay. I have video overlay working fine but I just need coordinates of road/Lane edges from OSM.  How should I go about it ? Up until now, I have used OSMIUM (http://osmcode...'''
date = "2017-06-14T19:48:00Z"
lastmod = "2017-06-15T08:56:00Z"
weight = 56627
keywords = [ "openstreetmap", "osmium", "pbf", "lanes", "highway" ]
aliases = [ "/questions/56627" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM data for Road/Lane Edges ?](/questions/56627/osm-data-for-roadlane-edges)

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
<span id="post-56627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56627-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get Road/Lane edges data (Lat/Long/Alt) from the Open Street Map so, that I can overlay rendered edges on a video overlay. I have video overlay working fine but I just need coordinates of road/Lane edges from OSM.</p>
<p>How should I go about it ?</p>
<p>Up until now, I have used OSMIUM (<a href="http://osmcode.org/libosmium/manual.html)">http://osmcode.org/libosmium/manual.html)</a> to import PBF file into my C++ program, I can see tags like "Highway" but they contain Lat/Long of an arbitrary point on the road AND I need is coordinates of the edges.</p>
<p>Can anyone point me in the right direction ?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-pbf" rel="tag" title="see questions tagged &#39;pbf&#39;">pbf</span> <span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jun '17, 19:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0844b1c91a72fe56590d20599cc906bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NitinH&#39;s gravatar image" />
<p><span>NitinH</span><br />
<span class="score" title="4 reputation points">4</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NitinH has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56627" class="comments-container">
&#10;</div>
<div id="comment-tools-56627" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56627-form-container" class="comment-form-container">
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

<span id="56628"></span>

<div id="answer-container-56628" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56628-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-56628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM generally maps linear features such as roads by a single line ideally located on the centre line of the feature. OSM does not, in general, store altitude data. There is a method of mapping highways as areas but it is not yet widely used (partly because it makes mapping things more difficult, but mainly because areas are not necessary for many use-cases). Equally the width tag is not widely used with highways.</p>
<p>To achieve what you want you will need to:</p>
<ul>
<li>Define areas for highways. In practice simple rules of thumb and a standard buffering of linestrings gives perfectly reasonable results. (For instance a typical residential street will be 5-6 m across, so buffer values of 2.5 to 4 m should be sensible).</li>
<li>Use an external source for elevation data. Most people use SRTM data from NASA.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jun '17, 20:01</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-56628" class="comments-container">
<span id="56629"></span>
<div id="comment-56629" class="comment">
<div id="post-56629-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Where available, the road width might be also estimated from the <code>lanes</code> tag.</p>
</div>
<div id="comment-56629-info" class="comment-info">
<span class="comment-age">(15 Jun '17, 08:56)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
</div>
<div id="comment-tools-56628" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56628-form-container" class="comment-form-container">
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

