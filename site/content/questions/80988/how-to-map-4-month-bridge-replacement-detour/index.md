+++
type = "question"
title = "How to map 4-month bridge replacement detour?"
description = '''I am wondering how I should temporarily (approximately a four-month period) map a designated/signed detour route due to an old bridge over a freeway being demolished and replaced with a new bridge. Here is a link to the MnDOT detour map (there are actually two detours): http://www.dot.state.mn.us/d6...'''
date = "2021-07-16T02:26:00Z"
lastmod = "2021-07-30T02:20:00Z"
weight = 80988
keywords = [ "construction", "detour" ]
aliases = [ "/questions/80988" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to map 4-month bridge replacement detour?](/questions/80988/how-to-map-4-month-bridge-replacement-detour)

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
<span id="post-80988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80988-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-80988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am wondering how I should temporarily (approximately a four-month period) map a designated/signed detour route due to an old bridge over a freeway being demolished and replaced with a new bridge.</p>
<p>Here is a link to the MnDOT detour map (there are actually two detours):</p>
<p><a href="http://www.dot.state.mn.us/d6/projects/hwy52-hader-southbound-improvements/pdfs/detour1.pdf?utm_content=&amp;utm_medium=email&amp;utm_name=&amp;utm_source=govdelivery&amp;utm_term=">http://www.dot.state.mn.us/d6/projects/hwy52-hader-southbound-improvements/pdfs/detour1.pdf?utm_content=&amp;utm_medium=email&amp;utm_name=&amp;utm_source=govdelivery&amp;utm_term=</a></p>
<p>According to the OSM wiki, a route relation with route=detour is for PERMANENT alternate routes during traffic jams. This is not the same thing; it is temporary but 4 months long.</p>
<p>Thru-traffic on US 52 will simply be temporarily re-routed using the on- and off-ramps (motorway links already existing).</p>
<p>David</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-construction" rel="tag" title="see questions tagged &#39;construction&#39;">construction</span> <span class="post-tag tag-link-detour" rel="tag" title="see questions tagged &#39;detour&#39;">detour</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '21, 02:26</strong></p>
<img src="https://secure.gravatar.com/avatar/d52dc9111ac1bab71d8dadb2506610d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yourvillagemaps&#39;s gravatar image" />
<p><span>yourvillagemaps</span><br />
<span class="score" title="95 reputation points">95</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yourvillagemaps has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80988" class="comments-container">
<span id="81113"></span>
<div id="comment-81113" class="comment">
<div id="post-81113-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Don't forget to mark which answer you went with as accepted.</p>
</div>
<div id="comment-81113-info" class="comment-info">
<span class="comment-age">(30 Jul '21, 02:20)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-80988" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80988-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="80991"></span>

<div id="answer-container-80991" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80991-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80991-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80991-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a perfect use-case for <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">conditional restrictions</a>.</p>
<p>If the bridge is closed for all types of traffic (motor vehicles, bicycles and pedestrians) and you (roughly) know the time-span for which this road is closed, then simply add the following tag to this road:</p>
<p><code>access:conditional=no @ (2021 Jul 15-2021 Nov 15)</code></p>
<p>If the bridge is just closed for motor vehicles but open for cyclists and pedestrians then add the following instead:</p>
<p><code>motor_vehicle:conditional=no @ (2021 Jul 15-2021 Nov 15)</code></p>
<p>You might have to adapt the date to your needs. Note that not all end-user software support conditional restrictions yet. In fact, the only application known to me is OsmAnd.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '21, 08:00</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '21, 08:02</strong> </span></p>
</div>
</div>
<div id="comments-container-80991" class="comments-container">
&#10;</div>
<div id="comment-tools-80991" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80991-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81000"></span>

<div id="answer-container-81000" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81000-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If it's closed for construction, then set the access to what it will be once it reopens, and then change <code>highway=*</code> to <code>construction=*</code>, and add tags like</p>
<pre><code>highway=construction
opening_date=2021-11-30</code></pre>
<p>(or whatever y-m-d it's expected to be open by). This method makes it easy to reopen, then all you have to do in JOSM is change <code>construction=*</code> back to <code>highway=*</code> and remove the <code>opening_date=*</code> tag. Programs like StreetComplete and Osmose will ask people if something is still under construction or flag it as being possibly completed respectively after the opening date.</p>
<p><code>highway=construction</code> is not routable but is renderable on most consuming software, and it's not intended to be routable except by traffic destined for the worksite.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '21, 15:02</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '21, 15:04</strong> </span></p>
</div>
</div>
<div id="comments-container-81000" class="comments-container">
<span id="81110"></span>
<div id="comment-81110" class="comment">
<div id="post-81110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have decided to go with the suggestion by Baloo Uriza.</p>
<p>Thanks!</p>
<p>David</p>
</div>
<div id="comment-81110-info" class="comment-info">
<span class="comment-age">(29 Jul '21, 21:45)</span> <span class="comment-user userinfo">yourvillagemaps</span>
</div>
</div>
</div>
<div id="comment-tools-81000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81000-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80990"></span>

<div id="answer-container-80990" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80990-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-80990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For only four moths i wound just add some map notes, they are instant and can be removed just as quickly. <img src="https://help.openstreetmap.org/upfiles/map_note_Great_Ouse_way_NqL0kTG.jpg" alt="alt text" /></p>
<p>I would not recommend changing the map data for such a short time. The change would be ok for the main OSM map but many derived maps use that data, and they will time lag so long that by the time they have reacted to the closed bridge it will be repaired and then there will be another time lag for them to show the restored route. I am looking at this from the point of view for a OSM on Garmin user. I don't know what commercial map providers like TomTom and Garmins do. They, i think, only do once a year updates and I guess they ignore short time closures and use dab or phone traffic alerts to cover this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '21, 07:40</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '21, 07:56</strong> </span></p>
</div>
</div>
<div id="comments-container-80990" class="comments-container">
<span id="80993"></span>
<div id="comment-80993" class="comment">
<div id="post-80993-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I agree to not change the map substantially for this time frame. Scai has given a good solution how to do it with little unwanted impact.</p>
<p>I don't agree on placing a map note, though. In my understanding they are there to leave hints for mappers what to change in the map. That's why they can be "resolved", too. They shouldn't be used to give general notes to the public. The fact that they cannot systematically evaluated by any consumer alone makes them unsuitable for such case.</p>
</div>
<div id="comment-80993-info" class="comment-info">
<span class="comment-age">(16 Jul '21, 08:12)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-80990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80990-form-container" class="comment-form-container">
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

