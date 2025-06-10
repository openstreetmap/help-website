+++
type = "question"
title = "OpenSeaMap into OpenStreetMap"
description = '''Hi I have a question about OpenSeaMap integration into a OpenStreetMap application. What I want to achieve is to visual sector for mobile cells as bearing , open angle for cell sector-carriers and range of cells range (distance). I see that the OpenSeaMap have similar functionality for ex lighthouse...'''
date = "2023-02-09T10:41:00Z"
lastmod = "2023-02-11T12:01:00Z"
weight = 86652
keywords = [ "open-angle", "bearing", "distance-range", "openseamap" ]
aliases = [ "/questions/86652" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OpenSeaMap into OpenStreetMap](/questions/86652/openseamap-into-openstreetmap)

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
<span id="post-86652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86652-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I have a question about OpenSeaMap integration into a OpenStreetMap application.</p>
<p>What I want to achieve is to visual sector for mobile cells as bearing , open angle for cell sector-carriers and range of cells range (distance). I see that the OpenSeaMap have similar functionality for ex lighthouses for sea traffic so I wonder if it possibly to use this type of icons for mobile cell purpose? If so , I need some guide how to put them together.</p>
<p>Best Regards Jörgen Sjögren</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-open-angle" rel="tag" title="see questions tagged &#39;open-angle&#39;">open-angle</span> <span class="post-tag tag-link-bearing" rel="tag" title="see questions tagged &#39;bearing&#39;">bearing</span> <span class="post-tag tag-link-distance-range" rel="tag" title="see questions tagged &#39;distance-range&#39;">distance-range</span> <span class="post-tag tag-link-openseamap" rel="tag" title="see questions tagged &#39;openseamap&#39;">openseamap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '23, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/52fb6b98482e7ffb57a5d02163633d1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emwjosj&#39;s gravatar image" />
<p><span>emwjosj</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emwjosj has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86652" class="comments-container">
<span id="86653"></span>
<div id="comment-86653" class="comment">
<div id="post-86653-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is absolutely possible to achieve what you want, but without a bit more information about what you want to achieve people won't be able to help much.</p>
<p>OpenStreetMap is just a big pile of data. Subject to the licence, you can do pretty much what you want with that. OpenSeaMap is just some sea-specific data stored in among the OSM data.</p>
<p>You probably have some idea what platform you are writing your application for, and that platform probably has some documentation about reading data from json, web servers or local files. I'd start there.</p>
</div>
<div id="comment-86653-info" class="comment-info">
<span class="comment-age">(09 Feb '23, 11:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-86652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86652-form-container" class="comment-form-container">
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

<span id="86678"></span>

<div id="answer-container-86678" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86678-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>OpenSeaMap is an open source project, that generate a raster overlay, based on OSM data, selected for nautical interest.</p>
<p>You could dive into the OpenSeaMap code, and either use their stack to generate an overlay dedicated to mobile cells, or use the part of their code that generate sectors, and use it in another rendering stack, like the default openstreeetmap-carto for example.</p>
<p>Both approach are big project, and quite technical.</p>
<p>On the other hand, you might take inspiration from surveillance cameras maps. <a href="https://osmcamera.dihe.de/">These</a> <a href="https://mapcomplete.osm.be/surveillance?">few</a> <a href="https://sunders.uber.space/">examples</a> display the cameras on a map, with their coverage (based on the tagging available, of course).</p>
<p>Which takes me to the most important question, did you check if the needed data is actually in OSM ?</p>
<p>The only technical tag associated with <a href="https://wiki.openstreetmap.org/wiki/Tag:man_made%3Dantenna"><code>man_made=antenna</code></a> is <code>frequency</code>.</p>
<p>On the <a href="https://wiki.openstreetmap.org/wiki/Key:communication:mobile_phone"><code>communication:mobile_phone</code></a> page, some reference to the generation (LTE, umts)...</p>
<p>I've seen some discussion to import such data, but as it's more or less unverifiable from the ground, it seems the general consensus is not to map that kind of information (cell id, bearing, theoretical range, etc).</p>
<p>Best regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '23, 12:01</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-86678" class="comments-container">
&#10;</div>
<div id="comment-tools-86678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86678-form-container" class="comment-form-container">
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

