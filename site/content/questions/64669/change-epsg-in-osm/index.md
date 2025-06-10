+++
type = "question"
title = "Change EPSG in OSM"
description = '''Hi! I&#x27;m working on an android application where I want to plot my data in an OSM view. The data I want to plot is in EPSG 3857 but the OSM only wants it in EPSG 4326. Is it a way I can set the OSM in the android app (working with JAVA) to use EPSG 3857?'''
date = "2018-07-12T07:07:00Z"
lastmod = "2018-07-16T07:03:00Z"
weight = 64669
keywords = [ "development", "android", "java", "projection" ]
aliases = [ "/questions/64669" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Change EPSG in OSM](/questions/64669/change-epsg-in-osm)

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
<span id="post-64669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64669-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>I'm working on an android application where I want to plot my data in an OSM view. The data I want to plot is in EPSG 3857 but the OSM only wants it in EPSG 4326. Is it a way I can set the OSM in the android app (working with JAVA) to use EPSG 3857?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-projection" rel="tag" title="see questions tagged &#39;projection&#39;">projection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '18, 07:07</strong></p>
<img src="https://secure.gravatar.com/avatar/114a5cc1077cff2cdb66a542e8b25b54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LeeMap&#39;s gravatar image" />
<p><span>LeeMap</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LeeMap has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '18, 18:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-64669" class="comments-container">
<span id="64676"></span>
<div id="comment-64676" class="comment">
<div id="post-64676-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>What Android framework/library are you using to display the map?</p>
</div>
<div id="comment-64676-info" class="comment-info">
<span class="comment-age">(12 Jul '18, 12:53)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="64680"></span>
<div id="comment-64680" class="comment">
<div id="post-64680-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The gdal library is a great way to reproject data, and it looks like there are ways to use it with Java. I don't know Java, but maybe this might give you a starting point? <a href="https://www.programcreek.com/java-api-examples/?api=org.gdal.gdal.Driver">https://www.programcreek.com/java-api-examples/?api=org.gdal.gdal.Driver</a></p>
</div>
<div id="comment-64680-info" class="comment-info">
<span class="comment-age">(12 Jul '18, 15:18)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="64744"></span>
<div id="comment-64744" class="comment">
<div id="post-64744-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'm using osmbonuspack 5.8 and omsdroid 5.2.</p>
</div>
<div id="comment-64744-info" class="comment-info">
<span class="comment-age">(16 Jul '18, 07:03)</span> <span class="comment-user userinfo">LeeMap</span>
</div>
</div>
</div>
<div id="comment-tools-64669" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64669-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

