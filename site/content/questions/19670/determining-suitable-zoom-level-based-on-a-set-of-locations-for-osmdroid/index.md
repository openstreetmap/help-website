+++
type = "question"
title = "Determining suitable zoom level based on a set of locations for OSMDroid"
description = '''From Google Maps Android API v2, I understand that this can be done through this method: LatLngBounds.Builder builder = new LatLngBounds.Builder(); for (Location loc : allLocations) {  LatLng position = new LatLng(loc.getLatitude(), loc.getLongitude());  builder.include(position); }  CameraUpdate cu...'''
date = "2013-02-07T11:00:00Z"
lastmod = "2013-02-07T22:39:00Z"
weight = 19670
keywords = [ "maptile", "downloading", "zoom" ]
aliases = [ "/questions/19670" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Determining suitable zoom level based on a set of locations for OSMDroid](/questions/19670/determining-suitable-zoom-level-based-on-a-set-of-locations-for-osmdroid)

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
<span id="post-19670-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19670-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19670-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>From Google Maps Android API v2, I understand that this can be done through this method:</p>
<pre><code>LatLngBounds.Builder builder = new LatLngBounds.Builder();
for (Location loc : allLocations) {
    LatLng position = new LatLng(loc.getLatitude(), loc.getLongitude());
    builder.include(position);
}
&#10;CameraUpdate cu = CameraUpdateFactory.newLatLngBounds(builder.build(), someMarginValue);
map.moveCamera(cu);</code></pre>
<p>However I can't seem to find a way to do this for OSMDroid. Is there a solution/ class to help determine the zoom level based on a set of locations?</p>
<p>I need the zoom level to be determined first as I am downloading a specific set of maptiles for offline display. However to do that I need to determine the right zoom level to download from the server first... Are there any algorithms out there that can determine this zoom level first?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-maptile" rel="tag" title="see questions tagged &#39;maptile&#39;">maptile</span> <span class="post-tag tag-link-downloading" rel="tag" title="see questions tagged &#39;downloading&#39;">downloading</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '13, 11:00</strong></p>
<img src="https://secure.gravatar.com/avatar/8e2f3652fadd1fc58cbd9780977ab5d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lyk&#39;s gravatar image" />
<p><span>lyk</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lyk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19670" class="comments-container">
&#10;</div>
<div id="comment-tools-19670" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19670-form-container" class="comment-form-container">
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

<span id="19716"></span>

<div id="answer-container-19716" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19716-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe the OSM wiki can help about <a href="http://wiki.openstreetmap.org/wiki/Zoom_levels">Zoomlevels</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '13, 22:39</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-19716" class="comments-container">
&#10;</div>
<div id="comment-tools-19716" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19716-form-container" class="comment-form-container">
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

