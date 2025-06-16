+++
type = "question"
title = "Notating wheelchair ramps in pedestrian overpasses"
description = '''To notate pedestrian overpasses, I&#x27;ve been copying an example I found somewhere in the map for Mexico City: Steps on each side of the bridge, and a Footpath of type Bridge for the overpass itself. In my town they have been installing ramps for wheelchairs/bikes in addition to steps in overpasses, an...'''
date = "2013-05-17T00:57:00Z"
lastmod = "2013-05-28T12:08:00Z"
weight = 22487
keywords = [ "pedestrian", "wheelchair", "overpass" ]
aliases = [ "/questions/22487" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Notating wheelchair ramps in pedestrian overpasses](/questions/22487/notating-wheelchair-ramps-in-pedestrian-overpasses)

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
<span id="post-22487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22487-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>To notate pedestrian overpasses, I've been copying an example I found somewhere in the map for Mexico City: Steps on each side of the bridge, and a Footpath of type Bridge for the overpass itself.</p>
<p>In my town they have been installing ramps for wheelchairs/bikes in addition to steps in overpasses, and I'm wondering how to notate those. Should I use another footpath with the wheelchair tag on it?</p>
<p>Finally, I guess I actually need to connect the Steps and the ramps to the actual sidewalk. But if the sidewalk is just a flag on the road itself - should I just connect the steps/ramps to the road line?</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-wheelchair" rel="tag" title="see questions tagged &#39;wheelchair&#39;">wheelchair</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 May '13, 00:57</strong></p>
<img src="https://secure.gravatar.com/avatar/e81394b007264247f2acb0e57e596301?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Federico%20Mena%20Quintero&#39;s gravatar image" />
<p><span>Federico Men...</span><br />
<span class="score" title="471 reputation points">471</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Federico Mena Quintero has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22487" class="comments-container">
&#10;</div>
<div id="comment-tools-22487" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22487-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="22490"></span>

<div id="answer-container-22490" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22490-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-22490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Federico Mena Quintero has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These are two questions (at least):).</p>
<ol>
<li>Yes map the ramp path and give it highway=footway, wheelchair=yes or if it is ONLY for wheelchairs highway=path, wheelchair=designated, foot=no, horse=no, bicycle=no</li>
<li>Yes in the case described you just connect to the road line (or you can add footways along the road if you know where is it).</li>
</ol>
<p>It is also useful to tag the incline, to specify which way the ramp goes. At least incline=up or incline=down (relative to the direction of the way). Or if you are able to measure the steepness, you can tag that as a percentage or angle. See <a href="https://wiki.openstreetmap.org/wiki/Key:incline">https://wiki.openstreetmap.org/wiki/Key:incline</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '13, 01:15</strong></p>
<img src="https://secure.gravatar.com/avatar/e6dd88ec54643689069f97f0d52398ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gorn&#39;s gravatar image" />
<p><span>gorn</span><br />
<span class="score" title="542 reputation points">542</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gorn has one accepted answer">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 May '13, 12:09</strong> </span></p>
</div>
</div>
<div id="comments-container-22490" class="comments-container">
<span id="22491"></span>
<div id="comment-22491" class="comment">
<div id="post-22491-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you so much! Makes perfect sense.</p>
</div>
<div id="comment-22491-info" class="comment-info">
<span class="comment-age">(17 May '13, 02:04)</span> <span class="comment-user userinfo">Federico Men...</span>
</div>
</div>
<span id="22500"></span>
<div id="comment-22500" class="comment">
<div id="post-22500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why highway=path if it is ONLY for wheelchairs? path allows foot, bicycles and horses according to the <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">default access restrictions</a>.</p>
</div>
<div id="comment-22500-info" class="comment-info">
<span class="comment-age">(17 May '13, 10:41)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22530"></span>
<div id="comment-22530" class="comment">
<div id="post-22530-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It is also useful to tag the incline, to specify which way the ramp goes. At least incline=up or incline=down (relative to the direction of the way). Or if you are able to measure the steepness, you can tag that as a percentage or angle. See <a href="https://wiki.openstreetmap.org/wiki/Key:incline">https://wiki.openstreetmap.org/wiki/Key:incline</a></p>
</div>
<div id="comment-22530-info" class="comment-info">
<span class="comment-age">(17 May '13, 19:37)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
<span id="22809"></span>
<div id="comment-22809" class="comment">
<div id="post-22809-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@scai</span> - for me the hightway=path is the most neutral nonvehicle type of way, where individual access tags can be added. I do not see an alternative if it is only for wheelchairs - for example higway=footway, foot=no does not make much sense :) ... I have edited my answer to say foot=no to be more precise, this is true.</p>
</div>
<div id="comment-22809-info" class="comment-info">
<span class="comment-age">(28 May '13, 12:08)</span> <span class="comment-user userinfo">gorn</span>
</div>
</div>
</div>
<div id="comment-tools-22490" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22490-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22499"></span>

<div id="answer-container-22499" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22499-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22499-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22499-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Federico, here’s another example, <a href="https://www.openstreetmap.org/?lat=52.04074&amp;lon=5.079667&amp;zoom=18&amp;layers=M">https://www.openstreetmap.org/?lat=52.04074&amp;lon=5.079667&amp;zoom=18&amp;layers=M</a> an access ramp wich looks like a large corkscrew with separated stairways. A pedestrian is allowed to 'take' a wheelchair, buggy or even a bicycle along to cross the Railway line.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '13, 10:31</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-22499" class="comments-container">
<span id="22524"></span>
<div id="comment-22524" class="comment">
<div id="post-22524-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The surface of that bridge is really loose gravel? I highly doubt it. If there is split rolled into the top of asphalt, then you should use surface=asphalt</p>
</div>
<div id="comment-22524-info" class="comment-info">
<span class="comment-age">(17 May '13, 16:33)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="22533"></span>
<div id="comment-22533" class="comment">
<div id="post-22533-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Since there's no tag for acrylaatrasin with siliconcarbide or simply rasin with korund, I choose gravel. It should be possible to add a new tag for these kind a surfaces, isnt it ? But until that gravel comes awsome close enough.</p>
</div>
<div id="comment-22533-info" class="comment-info">
<span class="comment-age">(17 May '13, 21:52)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="22535"></span>
<div id="comment-22535" class="comment">
<div id="post-22535-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Actually gravel is considered among the "unpaved" category by most users, because it describes loose gravel. If you don't have a completely accurate tag, but something is definitely paved, you are far better of to just tag it surface=paved.</p>
<p>What you should NEVER do, is using a tag that means something else entirely.</p>
</div>
<div id="comment-22535-info" class="comment-info">
<span class="comment-age">(18 May '13, 00:40)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="22538"></span>
<div id="comment-22538" class="comment">
<div id="post-22538-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span></span><span>@Hendrikklaas</span> If your surface is not among your editor's presets you can either choose between the categories paved/unpaved or specify the surface as close as possible by <a href="https://wiki.openstreetmap.org/wiki/Any_tags_you_like">using a custom value</a>. There is no option between those two.</p>
</div>
<div id="comment-22538-info" class="comment-info">
<span class="comment-age">(18 May '13, 09:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22499" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22499-form-container" class="comment-form-container">
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

