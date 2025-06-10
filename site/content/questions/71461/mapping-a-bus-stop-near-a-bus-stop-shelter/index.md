+++
type = "question"
title = "Mapping a bus stop near a bus-stop shelter"
description = '''How should I map a bus stop where the stop sign and the shelter are separate? See here. I&#x27;ve tagged the shelter as a shelter, and the bus stop as a bus stop, but as they&#x27;re only metres from each other the result on OSM Carto is unsatisfactory: the shelter appears in the middle of the road and the bu...'''
date = "2019-11-04T21:50:00Z"
lastmod = "2019-11-05T13:37:00Z"
weight = 71461
keywords = [ "shelter", "busstops" ]
aliases = [ "/questions/71461" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping a bus stop near a bus-stop shelter](/questions/71461/mapping-a-bus-stop-near-a-bus-stop-shelter)

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
<span id="post-71461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71461-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How should I map a bus stop where the stop sign and the shelter are separate? See <a href="https://drive.google.com/open?id=1gwsvbBXIegYfHlIoBHunf0b8zY4aSBup">here</a>.</p>
<p>I've tagged the shelter as a shelter, and the bus stop as a bus stop, but as they're only metres from each other <a href="https://www.openstreetmap.org/?mlat=52.57160&amp;mlon=-0.34158#map=16/52.57160/-0.34158">the result</a> on OSM Carto is unsatisfactory: the shelter appears in the middle of the road and the bus-stop (normally blue) disappears.</p>
<p>I know we don't tag for the renderer, but assuming the renderer makes good sense of good tagging, should I instead tag amenity=shelter on the bus stop node itself, and not on the physical shelter nearby?</p>
<hr />
<p>Related, presumably the <strong>name</strong> of the bus stop is all the white text on navy blue <a href="https://drive.google.com/open?id=1Ua86xaabdYD9MW756rPJeJyvIkVmw2mR">here</a>, even though it's quite long?</p>
<p>And (UK people especially) the <strong>txt</strong>-<strong>info</strong> code, now obsolete, is presumably no use for anything at all, even identifying the stop?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shelter" rel="tag" title="see questions tagged &#39;shelter&#39;">shelter</span> <span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '19, 21:50</strong></p>
<img src="https://secure.gravatar.com/avatar/4f273f48fd8756729fc15f4fcf4aae2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eteb3&#39;s gravatar image" />
<p><span>eteb3</span><br />
<span class="score" title="295 reputation points">295</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eteb3 has one accepted answer">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Nov '19, 21:57</strong> </span></p>
</div>
</div>
<div id="comments-container-71461" class="comments-container">
&#10;</div>
<div id="comment-tools-71461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71461-form-container" class="comment-form-container">
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

<span id="71465"></span>

<div id="answer-container-71465" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71465-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looks fine to me <a href="https://osm.org/go/eu7wEuXuO">at z19</a> so I wouldn't worry about your mapping.</p>
<p>(Aside: Eleb3 is the txt-info code obsolete? I've just checked a current timetable and the last page lists all the text codes and stop names relevant for the route underneath this text:</p>
<blockquote>
<p>For times of the next departures from a particular stop you can use traveline-txt - by sending the SMS code to 84268. Add the service number after the code if you just want a specific service - eg: buctdgtd 60. The return message from traveline-txt will show the next three departures, and it currently costs 25p plus any message sending charge. Departure times will be real-time predictions where available, or scheduled departure times if not. You can also get the same information by using the SMS code at www.nextbuses.mobi (only normal browsing charges apply) or through several iPhone or Android apps that offer access to NextBuses. NOTE: SMS codes are different in each direction. Make sure you choose the right direction from these lists.</p>
</blockquote>
<p>Having said that, searching the naptan data as it was in January shows the name of this stop (as used in timetables) as Splash Lane and the NaptanCode as PETGTPM rather than PEDGTPM for stop with AtcoCode 0590PGC726)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '19, 13:24</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-71465" class="comments-container">
<span id="71466"></span>
<div id="comment-71466" class="comment">
<div id="post-71466-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, I didn't realise that was a Naptan code. Maybe it's just my mobile/provider, but having tried in several districts to get info by text, my handset always tells me the text couldn't be sent. I've always presumed that's because the shortcode 84268 is no longer in service - and that in these days of smartphones the service is completely disbanded.</p>
</div>
<div id="comment-71466-info" class="comment-info">
<span class="comment-age">(05 Nov '19, 13:37)</span> <span class="comment-user userinfo">eteb3</span>
</div>
</div>
</div>
<div id="comment-tools-71465" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71465-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

