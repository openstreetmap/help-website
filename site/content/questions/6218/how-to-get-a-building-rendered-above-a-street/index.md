+++
type = "question"
title = "How to get a building rendered above a street?"
description = '''Why does a building that is no bridge and goes over a street renders as if it was underneath the street? Street:  layer=0 Building (Multipolygon):  layer=1 I refuse bridge=yes, as from my understanding this is no real bridge. Also I don&#x27;t think tunnel=yes is what I want as this is obviously no tunne...'''
date = "2011-07-08T10:00:00Z"
lastmod = "2018-12-19T10:50:00Z"
weight = 6218
keywords = [ "rendering", "bridge" ]
aliases = [ "/questions/6218" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [How to get a building rendered above a street?](/questions/6218/how-to-get-a-building-rendered-above-a-street)

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
<span id="post-6218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6218-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-6218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Why does a building that is no bridge and goes over a street renders as if it was underneath the street?</p>
<p>Street: layer=0</p>
<p>Building (Multipolygon): layer=1</p>
<p>I refuse bridge=yes, as from my understanding this is no real bridge. Also I don't think tunnel=yes is what I want as this is obviously no tunnel.</p>
<p>See it here: <a href="http://maps.google.de/?ll=51.258081,7.144289&amp;spn=0.00558,0.011362&amp;z=17&amp;layer=c&amp;cbll=51.258081,7.144289&amp;panoid=j5CE8HLds5NCzW-_1_yulQ&amp;cbp=12,176.91,,0,-34.59">Street View</a> <a href="http://www.openstreetmap.org/?lat=51.2580536305904&amp;lon=7.1443185210228&amp;zoom=18">OSM</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '11, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/aa89e8e008c7920f96a759f481dd04a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bot47&#39;s gravatar image" />
<p><span>bot47</span><br />
<span class="score" title="236 reputation points">236</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bot47 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6218" class="comments-container">
&#10;</div>
<div id="comment-tools-6218" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6218-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="6224"></span>

<div id="answer-container-6224" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6224-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-6224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bot47 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The mapping you did it entirely right, but the mapnik renderer chooses to render highway on top of buildings because more people are interested in way than in buildings. This is a design decision done by the stylesheet maintainers of the mapnik view on the OpenStreetMap website and nothing that you have to - or should for that matter - try to change by changing the mapped data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '11, 12:10</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Aug '11, 16:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span></p>
</div>
</div>
<div id="comments-container-6224" class="comments-container">
&#10;</div>
<div id="comment-tools-6224" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6224-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6226"></span>

<div id="answer-container-6226" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6226-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-6226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like a bridge to me from your street view link. I would have tagged it bridge=yes on the section which is suspended in mid-air above the road... or looked further into the bridge relation.</p>
<p>Edit:</p>
<p>To further clarify in light of looking more closely at street view and satellite, it looks to me like the whole of the ring-shaped "building" is actually a road whose physical form is a helix.</p>
<p>My own preference if I was mapping that would be to show it as a service road, and the mid-aid section as a bridge (so that if you are in the car park and ask a navigation system using OSM data for directions, it will direct you to the bridge, down the helical service road, and onto the main road).</p>
<p>However, per petschge's comment, I'd agree that if you are considering it to be a "building" rather than a "road", then you can't call the elevated section a "bridge".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '11, 13:43</strong></p>
<img src="https://secure.gravatar.com/avatar/b95e1b5cb818be577b5561688a50368c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="banoffee&#39;s gravatar image" />
<p><span>banoffee</span><br />
<span class="score" title="884 reputation points">884</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="banoffee has 3 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jul '11, 14:53</strong> </span></p>
</div>
</div>
<div id="comments-container-6226" class="comments-container">
<span id="6227"></span>
<div id="comment-6227" class="comment">
<div id="post-6227-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not a bridge to don't do that. If you really want to tag the precise form of the building have a look at <a href="http://wiki.openstreetmap.org/wiki/Proposed_features/Building_attributes">http://wiki.openstreetmap.org/wiki/Proposed_features/Building_attributes</a></p>
</div>
<div id="comment-6227-info" class="comment-info">
<span class="comment-age">(08 Jul '11, 13:47)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="6229"></span>
<div id="comment-6229" class="comment">
<div id="post-6229-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When I zoom out of the google street view, to the satellite view, it looks even more like a bridge - a structure that cars drive over to get onto or off a rooftop parking space. Why shouldn't it be tagged as one?</p>
<p>Edit: thanks to link to Building attributes page for the general case of non-bridge parts of buildings though - I've got one I did earlier to fix up!</p>
</div>
<div id="comment-6229-info" class="comment-info">
<span class="comment-age">(08 Jul '11, 14:01)</span> <span class="comment-user userinfo">banoffee</span>
</div>
</div>
<span id="6232"></span>
<div id="comment-6232" class="comment">
<div id="post-6232-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>On the picture, it is a bridge.</p>
</div>
<div id="comment-6232-info" class="comment-info">
<span class="comment-age">(08 Jul '11, 15:35)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-6226" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6226-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67221"></span>

<div id="answer-container-67221" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67221-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to use tunnel=building_passage <a href="https://wiki.openstreetmap.org/wiki/Key:tunnel#tunnel.3Dbuilding_passage">https://wiki.openstreetmap.org/wiki/Key:tunnel#tunnel.3Dbuilding_passage</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '18, 23:24</strong></p>
<img src="https://secure.gravatar.com/avatar/d5eaa49c5a53ff02de59c85de7959871?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="poselab&#39;s gravatar image" />
<p><span>poselab</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="poselab has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67221" class="comments-container">
&#10;</div>
<div id="comment-tools-67221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67221-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67276"></span>

<div id="answer-container-67276" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67276-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not a tunnel indeed, only a building above a street.</p>
<p>You can use the tag "covered=yes" on the part of the road below the building (connect the road to the building outline and split it to only tag the part exactly below it). It will show with a better visualization (nearly as a tunnel).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Dec '18, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/96cd30b0fbe956d9518d2c4593f67215?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anakil&#39;s gravatar image" />
<p><span>Anakil</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anakil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67276" class="comments-container">
&#10;</div>
<div id="comment-tools-67276" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67276-form-container" class="comment-form-container">
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

