+++
type = "question"
title = "How to import KML files into OpenStreetMap?"
description = '''Anyone know how to import KML files into OpenStreetMap?'''
date = "2011-08-17T22:06:00Z"
lastmod = "2022-10-19T03:58:00Z"
weight = 7174
keywords = [ "kml" ]
aliases = [ "/questions/7174" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [How to import KML files into OpenStreetMap?](/questions/7174/how-to-import-kml-files-into-openstreetmap)

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
<span id="post-7174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7174-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-7174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Anyone know how to import KML files into OpenStreetMap?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '11, 22:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0a9804ccb2b14071dbc6363410c49563?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="br55&#39;s gravatar image" />
<p><span>br55</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="br55 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7174" class="comments-container">
&#10;</div>
<div id="comment-tools-7174" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7174-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="7176"></span>

<div id="answer-container-7176" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7176-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-7176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can't import KML files directly into OpenStreetMap, but you can probably trace over them in one of the editors available. <a href="http://merkaartor.be/">Merkaartor</a> can open KML files directly, and if you <a href="https://wiki.openstreetmap.org/wiki/Converting_GPS_track_data_between_formats">convert the file to GPX</a> <a href="http://josm.openstreetmap.de/">JOSM</a> can display it.</p>
<p>Even if you do convert your KML file to GPX, you won't be able to upload it to OpenStreetMap's traces, since it won't contain time stamps. This is done deliberately so that only traces gathered using a GPS receiver, rather than traced from an existing map, can be used as source material. Information traced from existing maps will be derived from those maps and carry their copyright, making them unsuitable to use as a source for OpenStreetMap.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '11, 22:46</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '11, 23:08</strong> </span></p>
</div>
</div>
<div id="comments-container-7176" class="comments-container">
<span id="85916"></span>
<div id="comment-85916" class="comment">
<div id="post-85916-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Merkaartor seems to only import points, not paths?</p>
</div>
<div id="comment-85916-info" class="comment-info">
<span class="comment-age">(19 Oct '22, 03:49)</span> <span class="comment-user userinfo">brightj</span>
</div>
</div>
</div>
<div id="comment-tools-7176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7176-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17166"></span>

<div id="answer-container-17166" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17166-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can also convert it with gpsbabel adding fake time:</p>
<pre><code>#!/bin/bash
for file in *.kml; do 
  gpsbabel -i kml -f &quot;$file&quot; -x track,faketime=20120901000001 -o gpx -F &quot;${file}.gpx&quot;
done</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '12, 19:01</strong></p>
<img src="https://secure.gravatar.com/avatar/1aaaf77e89ed1b496cefd433400ebf27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="int_ua&#39;s gravatar image" />
<p><span>int_ua</span><br />
<span class="score" title="275 reputation points">275</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="int_ua has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '12, 19:02</strong> </span></p>
</div>
</div>
<div id="comments-container-17166" class="comments-container">
&#10;</div>
<div id="comment-tools-17166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17166-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16617"></span>

<div id="answer-container-16617" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16617-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can load a KML file as a vector background layer in Potlatch and then choose which features from it to merge into the main layer. There is more information in the <a href="https://wiki.openstreetmap.org/wiki/Potlatch_2/vector_background_layers">wiki</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Oct '12, 21:29</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-16617" class="comments-container">
<span id="85917"></span>
<div id="comment-85917" class="comment">
<div id="post-85917-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This works with Potlatch 3. It works with both paths and points. It doesn't seem to import labels of the objects, though?</p>
</div>
<div id="comment-85917-info" class="comment-info">
<span class="comment-age">(19 Oct '22, 03:58)</span> <span class="comment-user userinfo">brightj</span>
</div>
</div>
</div>
<div id="comment-tools-16617" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16617-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18199"></span>

<div id="answer-container-18199" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18199-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How can one keep some attributes of the KML file when bringing them into openstreetmap? I want to bring in some bus stop data for example, and I'd like to keep the stop names with each stop without retyping them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '12, 20:26</strong></p>
<img src="https://secure.gravatar.com/avatar/910c7d9fe8793585a4177133a52c7ea1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nate_Wessel&#39;s gravatar image" />
<p><span>Nate_Wessel</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nate_Wessel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18199" class="comments-container">
&#10;</div>
<div id="comment-tools-18199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18199-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16622"></span>

<div id="answer-container-16622" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16622-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16622-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16622-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've had some luck with this site, which provides several conversion capabilities.</p>
<p><a href="http://www.gpsies.com/convert.do">http://www.gpsies.com/convert.do</a></p>
<p>If anybody has any warnings about this source, please speak up.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Oct '12, 02:37</strong></p>
<img src="https://secure.gravatar.com/avatar/5a51e6418375a0b544e3ec790dbb0a06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metricrider&#39;s gravatar image" />
<p><span>metricrider</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metricrider has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16622" class="comments-container">
&#10;</div>
<div id="comment-tools-16622" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16622-form-container" class="comment-form-container">
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

