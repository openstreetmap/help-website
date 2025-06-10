+++
type = "question"
title = "Gamin Nüvi 660 cannot navigate on OSM data"
description = '''I have stored an OSM file on my Gamin Nüvi 660FM. The file is an IMG file of New Zealand, downloaded from OSMAustralia. I stored the file on the SD card in my Gamin unit. The map displays nicely in my Gamin device, and I can manually (with the GPS receiver disabled) place my position on the new map,...'''
date = "2011-04-24T16:46:00Z"
lastmod = "2011-04-24T19:10:00Z"
weight = 4775
keywords = [ "navigation", "gamin" ]
aliases = [ "/questions/4775" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Gamin Nüvi 660 cannot navigate on OSM data](/questions/4775/gamin-nuvi-660-cannot-navigate-on-osm-data)

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
<span id="post-4775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4775-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have stored an OSM file on my Gamin Nüvi 660FM. The file is an IMG file of New Zealand, downloaded from <a href="http://www.osmaustralia.org/NZ-garmin.php">OSMAustralia</a>. I stored the file on the SD card in my Gamin unit.</p>
<p>The map displays nicely in my Gamin device, and I can manually (with the GPS receiver disabled) place my position on the new map, but any attempts to navigate fail. Even though my starting position is on a street, the device says "No street found near starting position", and searching for a particular location also fails - the device doesn't even know a country named New Zealand.</p>
<p>So, am I expecting too much, or must I store the map in the unit's internal memory rather than on an SD card? Or is there another problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-navigation" rel="tag" title="see questions tagged &#39;navigation&#39;">navigation</span> <span class="post-tag tag-link-gamin" rel="tag" title="see questions tagged &#39;gamin&#39;">gamin</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '11, 16:46</strong></p>
<img src="https://secure.gravatar.com/avatar/6df66df302ab0ecde669021a140ccd3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oz1cz&#39;s gravatar image" />
<p><span>oz1cz</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oz1cz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4775" class="comments-container">
&#10;</div>
<div id="comment-tools-4775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4775-form-container" class="comment-form-container">
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

<span id="4777"></span>

<div id="answer-container-4777" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4777-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-4777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="oz1cz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not familiar with the maps you link to, but it sounds like they are not routable. Whether to support routing is an option in Mkgmap (the software used to generate most OSM based Garmin maps), and not all maps have it enabled.</p>
<p>I see that OSM Australia also has routable maps to download: <a href="http://www.osmaustralia.org/NZ-garminroute.php">Garmin Routable IMG Files (New Zealand)</a>. So try downloading that, and using it on your Garmin instead, then routing should work.</p>
<p>For "searching for a particular location", note that address searching is not properly supported by Mkgmap (yet). So searching for an address may not work (it may depend on what Garmin device you are using). Though searching for a point of interest or city etc, then navigating to it should be possible (depending on your device). I believe there has recently been work on getting address searching working in Mkgmap, so recent versions may have some support for this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '11, 17:43</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-4777" class="comments-container">
<span id="4779"></span>
<div id="comment-4779" class="comment">
<div id="post-4779-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, Vclaw, that helped a lot!</p>
<p>The routable IMG files can indeed be used for navigating to other cities, but address searches do not work.</p>
</div>
<div id="comment-4779-info" class="comment-info">
<span class="comment-age">(24 Apr '11, 19:10)</span> <span class="comment-user userinfo">oz1cz</span>
</div>
</div>
</div>
<div id="comment-tools-4777" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4777-form-container" class="comment-form-container">
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

