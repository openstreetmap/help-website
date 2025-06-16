+++
type = "question"
title = "Aligning Roads to proper location"
description = '''There doesn&#x27;t seem to be a good answer to this anywhere. The closest is Satellite Image Accuracy which relates to having a inacurate background. It is definitely hard to not want to trace these. However, what about when you have GPX data that backs the satellite image? What is the correct way to adj...'''
date = "2012-11-12T18:51:00Z"
lastmod = "2012-11-28T17:22:00Z"
weight = 17661
keywords = [ "satellite", "gpx", "alignment" ]
aliases = [ "/questions/17661" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Aligning Roads to proper location](/questions/17661/aligning-roads-to-proper-location)

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
<span id="post-17661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17661-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There doesn't seem to be a good answer to this anywhere. The closest is <a href="/questions/13320/satellite-image-accuracy">Satellite Image Accuracy</a> which relates to having a inacurate background. It is definitely hard to not want to trace these.</p>
<p>However, what about when you have GPX data that backs the satellite image? What is the correct way to adjust this. Do the same rules apply for when the GPS image is innacurate? Or should the roads all be manually moved (I know you can multi select).</p>
<p>What is the right way and is there anything to make this eaiser?</p>
<p>Update: I don't know if "aligning" the image actually fixes the accuracy or just causes both roads and satellite to be inaccurate. Sounds like that is the common approach though.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-satellite" rel="tag" title="see questions tagged &#39;satellite&#39;">satellite</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-alignment" rel="tag" title="see questions tagged &#39;alignment&#39;">alignment</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Nov '12, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/7e77c05737bf455a5bf99c0f17ac19d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="he_the_great&#39;s gravatar image" />
<p><span>he_the_great</span><br />
<span class="score" title="1175 reputation points"><span>1.2k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="he_the_great has 3 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Nov '12, 21:07</strong> </span></p>
</div>
</div>
<div id="comments-container-17661" class="comments-container">
&#10;</div>
<div id="comment-tools-17661" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17661-form-container" class="comment-form-container">
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

<span id="17664"></span>

<div id="answer-container-17664" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17664-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-17664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="he_the_great has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We should preferably not map directly from the aerial imagery, because it can be a bit approximate. Accurate georeferencing of photographic images requires an equally accurate knowledge of the height of the camera above the ground, which requires knowledge of the height of the camera and the height of the ground, and both can be hard to determine with the required accuracy. My preference is to slide the background image until it agrees with something that I believe is accurate, which normally means the average of several GPS traces taken where the GPS receiver would have had a good view of the sky. Other accurately positioned objects can be used, but be careful not to infringe the copyright of the people who determined their position. Having aligned the background image, it can be used at least as a check on the accuracy of the map, and mapping directly from the aligned image is usually OK unless the ground slopes sharply, in which case the image could be accurate at one place and less accurate some distance away. To align the image in Potlatch 2, drag it with the mouse while holding down the space bar.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '12, 19:56</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-17664" class="comments-container">
<span id="17668"></span>
<div id="comment-17668" class="comment">
<div id="post-17668-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I realize the inacuracies that can come from these different sources, but I'm trying to figure out what is correct to update roadways when their position is found to most likely be the inaccuracy. Does aligning the satellite image do that, or does it just make them both wrong?</p>
</div>
<div id="comment-17668-info" class="comment-info">
<span class="comment-age">(12 Nov '12, 21:08)</span> <span class="comment-user userinfo">he_the_great</span>
</div>
</div>
<span id="17671"></span>
<div id="comment-17671" class="comment">
<div id="post-17671-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think our current 'gold standard' is the average of several good GPS traces. I would not normally use any imagery without first aligning it, except perhaps to correct an obvious gross error or omission where GPS data is not available and would be hard to obtain. Aligning the imagery to the existing mapping is a good method if you know that the existing mapping of that area is good, but otherwise it does not guarantee accuracy. You might want to consider the answers to <a href="/questions/5137/satellite-images-versus-gps-tracks.">https://help.openstreetmap.org/questions/5137/satellite-images-versus-gps-tracks.</a></p>
</div>
<div id="comment-17671-info" class="comment-info">
<span class="comment-age">(12 Nov '12, 22:16)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
<span id="17677"></span>
<div id="comment-17677" class="comment">
<div id="post-17677-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I understand verifying where the road should be is a first step, but this question is specifically about what is a good/proper way to make these changes over an area. And since moving the satellite image is so easy, does that work or does it just make both the road and satellite wrong.</p>
</div>
<div id="comment-17677-info" class="comment-info">
<span class="comment-age">(13 Nov '12, 00:18)</span> <span class="comment-user userinfo">he_the_great</span>
</div>
</div>
<span id="17684"></span>
<div id="comment-17684" class="comment">
<div id="post-17684-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If an area as been mapped but then you come to the conclusion that the image is misaligned you have to decide if you wish to move all the nodes one by one to your new alignment. "does it just make the road and satellite wrong" Yes but they ARE wrong, assuming you believe several GPX traces taken over a period of time not all on one day so you get a good average.</p>
</div>
<div id="comment-17684-info" class="comment-info">
<span class="comment-age">(13 Nov '12, 10:11)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="17688"></span>
<div id="comment-17688" class="comment">
<div id="post-17688-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The background image is provided only to help us to edit the map. If you slide the background image so that it aligns with some other feature (e.g. GPS traces, or an existing mapped feature), it affects the way that the image is shown on your computer for the rest of your editing session, but it does not affect anyone else, it does not change the map, and it is forgotten when you close the editor.</p>
</div>
<div id="comment-17688-info" class="comment-info">
<span class="comment-age">(13 Nov '12, 12:42)</span> <span class="comment-user userinfo">Madryn</span>
</div>
</div>
</div>
<div id="comment-tools-17664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17664-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17663"></span>

<div id="answer-container-17663" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17663-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Great, Just correct the layout conform the arial picture. Since the arial maps upgrade continuously all the time and the old data has been changed. But ask some oldies in your region if the maps are older or newer. By changing the view you’ll be one of a few, most of us see it and leave it as it is. Keep up the good work and have fun. Greetz Hendrik</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '12, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-17663" class="comments-container">
&#10;</div>
<div id="comment-tools-17663" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17663-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="18047"></span>

<div id="answer-container-18047" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18047-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I thought I would summarize the information I've come across in a way that most directly answers the question.</p>
<p>If the roadway is not aligned, either align it or ignore it.</p>
<p>Things to consider</p>
<ul>
<li>It is most important to have a consistency in flow. If updating a road position generally this will mean other roads are also incorrectly aligned. It would not be good for two roads to cross where they don't physically do so, or having a road which turns sharply when mostly straight.</li>
<li>Accuracy can be difficult to identify.</li>
<li>Bing imagery tries hard to be geographically aligned but is not always achieved as hills may cause improper dimensions (rumor is Bing uses planes).</li>
<li>Consumer GPS is highly inaccurate and is affected by clouds, trees, mountains, buildings, and most anything else. It is best to have multiple tracks from different or the best conditions. A straight drive may not appear so just from GPS tracks.</li>
<li>Moving the Bing imagery does nothing permanent, do so only to help tracing shapes after verifying a proper location or ignoring incorrect location.</li>
</ul>
<p>There is no efficient way of aligning. The Potlatch editor provides multiple selection with CTRL, but can be challenging to verify the boundary connections, my findings have shown that roads tend to be incorrectly shaped along with incorrect position so hand alignment tends to be of more value.</p>
<p>Moving a road tends to require all roads in the grid to move. This is fine in smaller cities, but would be challenging on the larger scale. As you move outside the grid there is usually good opportunity to transition into the non-hand-tuned portions without making things worse than before.</p>
<p><strong>Degree of Accuracy</strong>:</p>
<p>My thoughts on accuracy is that GPS/Bing is generally acceptable for new roads. For existing roads I find it good to verify Bing with some tracks.</p>
<p>My considerations for this</p>
<ul>
<li>Bing does try to be geographically correct.</li>
<li>No matter how dated Bing is, Tiger is even more so.</li>
<li>Those using the maps will likely also have consumer GPS and when using overlays it is nice to see proper image/road alignment.</li>
<li>Don't really want to change work that has verified as correctly placed, hopefully that verification is still available.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '12, 03:02</strong></p>
<img src="https://secure.gravatar.com/avatar/7e77c05737bf455a5bf99c0f17ac19d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="he_the_great&#39;s gravatar image" />
<p><span>he_the_great</span><br />
<span class="score" title="1175 reputation points"><span>1.2k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="he_the_great has 3 accepted answers">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Nov '12, 18:57</strong> </span></p>
</div>
</div>
<div id="comments-container-18047" class="comments-container">
<span id="18077"></span>
<div id="comment-18077" class="comment">
<div id="post-18077-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I would like to know is the acceptable tolerance for OSM. Is it +/- 1 or 5 or 10 meters?</p>
<p>My Garmin 60CSx reports +/- 2 meters accuracy at the best of times but it is mostly poorer than that.</p>
<p>If I walk the same way many times I have deviating traces by many meters more than my Garmin reports.</p>
<p>However, when these tracks are overlaid on Bing they are still within a tolerance which I would consider acceptable and vice-versa: Outdated Bing looks to be very acceptable to me.</p>
<p>It gives me confidence that what I upload is "good enough" for OSM, i.e. not 100% accurate but of acceptable tolerances!</p>
</div>
<div id="comment-18077-info" class="comment-info">
<span class="comment-age">(28 Nov '12, 17:22)</span> <span class="comment-user userinfo">dcp</span>
</div>
</div>
</div>
<div id="comment-tools-18047" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18047-form-container" class="comment-form-container">
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

