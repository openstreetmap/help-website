+++
type = "question"
title = "US roads and suitability for pedestrians"
description = '''Hi,  I&#x27;m using GraphHopper in an application which helps suggest running routes for people. I&#x27;m seeing cases where routes are being suggested that use unsuitable/unsafe roads. For example: West Powell Road, Ohio This road and bridge has no sidewalk and always has heavy traffic on it.  OSM [Street Vi...'''
date = "2019-11-30T12:52:00Z"
lastmod = "2019-12-01T16:04:00Z"
weight = 71904
keywords = [ "pedestrian" ]
aliases = [ "/questions/71904" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [US roads and suitability for pedestrians](/questions/71904/us-roads-and-suitability-for-pedestrians)

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
<span id="post-71904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71904-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm using GraphHopper in an application which helps suggest running routes for people.</p>
<p>I'm seeing cases where routes are being suggested that use unsuitable/unsafe roads. For example:</p>
<p><strong>West Powell Road, Ohio</strong></p>
<p>This road and bridge has no sidewalk and always has heavy traffic on it.</p>
<ul>
<li><a href="https://www.openstreetmap.org/way/37058434#map=17/40.15508/-83.04160">OSM</a></li>
<li><del>[Street View][2]</del></li>
<li><a href="https://graphhopper.com/maps/?point=40.156975%2C-83.0469&amp;point=40.156847%2C-83.04383&amp;locale=en-GB&amp;vehicle=foot&amp;weighting=fastest&amp;elevation=true&amp;use_miles=false&amp;layer=Omniscale">GraphHopper</a> - shows pedestrians being routed over this bridge</li>
</ul>
<p><strong>12th Street Bridge, Ohio River</strong></p>
<p>You definitely don't want to be walking over this!</p>
<ul>
<li><a href="https://www.openstreetmap.org/way/16101779">OSM</a></li>
<li><del>[Street View][5]</del></li>
<li><a href="https://graphhopper.com/maps/?point=38.480657%2C-82.642604&amp;point=38.486317%2C-82.63855&amp;locale=en-GB&amp;vehicle=foot&amp;weighting=fastest&amp;elevation=true&amp;use_miles=false&amp;layer=Omniscale">GraphHopper</a></li>
</ul>
<p>I strongly suspect that this is just going to be down to poor OSM tag data for these roads. It seems quite common on many US roads.</p>
<p>My questions are:</p>
<ol>
<li>Is my assumption correct that this is just down to tagging?</li>
<li>What would be the correct tag to apply to these roads? foot=no? sidewalk=none?</li>
<li>Is there a reasonable heuristic I can use as a workaround? e.g. Avoid any primary/trunk/motorways for foot unless explicitly tagged with foot=&lt;acceptable values=""&gt; or sidewalk=&lt;acceptablevalues&gt;</li>
</ol>
<p>Thanks,</p>
<p>Sam</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Nov '19, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/3599a5b9b3013b0230d176a7d98657c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samcrawford&#39;s gravatar image" />
<p><span>samcrawford</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samcrawford has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Nov '19, 13:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-71904" class="comments-container">
<span id="71906"></span>
<div id="comment-71906" class="comment">
<div id="post-71906-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In general can you avoid providing references to Google StreetView: such information is inadmissible in using OSM. I have replaced these with equivalent images from Bing Streetside which we do have permission to use when mapping.</p>
</div>
<div id="comment-71906-info" class="comment-info">
<span class="comment-age">(30 Nov '19, 13:56)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="71907"></span>
<div id="comment-71907" class="comment">
<div id="post-71907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately no Bing Streetside available: StreetView links removed.</p>
</div>
<div id="comment-71907-info" class="comment-info">
<span class="comment-age">(30 Nov '19, 14:04)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71904-form-container" class="comment-form-container">
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

<span id="71908"></span>

<div id="answer-container-71908" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71908-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-71908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="samcrawford has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes sidewalk=none is the appropriate tag.</p>
<p>You may need to tune the routing rules to severely penalise such ways. Some routing applications for cyclists may make use of other open data on likely traffic volumes to provide additional penalties. Motorways should automatically be non-routable for pedestrians, horses &amp; cyclists (there are exceptions which require explicit tagging to over-ride). Penalising other road categories will produce odd decisions where a main road runs through an urban area: in particular where such a road is the main street in a small town.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Nov '19, 14:08</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-71908" class="comments-container">
<span id="71913"></span>
<div id="comment-71913" class="comment">
<div id="post-71913-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You might also want to consider shoulder=yes|no.</p>
</div>
<div id="comment-71913-info" class="comment-info">
<span class="comment-age">(01 Dec '19, 08:01)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="71922"></span>
<div id="comment-71922" class="comment">
<div id="post-71922-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For completeness, in the UK verge=none|left|right|both can help identify busier roads where there is some kind of safer space for walking. In rural Ireland shoulder=yes is common and can be heavily used by pedestrians.</p>
</div>
<div id="comment-71922-info" class="comment-info">
<span class="comment-age">(01 Dec '19, 14:12)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="71926"></span>
<div id="comment-71926" class="comment">
<div id="post-71926-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>foot=no is also a correct tag when there's signage prohibiting foot traffic. (Can't tell if that's the case in your examples.)</p>
</div>
<div id="comment-71926-info" class="comment-info">
<span class="comment-age">(01 Dec '19, 16:04)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-71908" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71908-form-container" class="comment-form-container">
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

