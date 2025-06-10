+++
type = "question"
title = "Tag a road as unsuitable for walking"
description = '''I live near a road that is very narrow, winding, with reasonable gradient, and a 40 mph speed limit. There is no pavement alongside the road for a pedestrian to walk. This is the UK so by right any pedestrian can walk on this road. I would argue walking on this road is dangerous due to the above-men...'''
date = "2016-02-08T10:00:00Z"
lastmod = "2020-07-08T10:51:00Z"
weight = 47997
keywords = [ "dangerous", "routing", "pedestrian" ]
aliases = [ "/questions/47997" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Tag a road as unsuitable for walking](/questions/47997/tag-a-road-as-unsuitable-for-walking)

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
<span id="post-47997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47997-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-47997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I live near a road that is very narrow, winding, with reasonable gradient, and a 40 mph speed limit. There is no pavement alongside the road for a pedestrian to walk. This is the UK so by right any pedestrian can walk on this road.</p>
<p>I would argue walking on this road is dangerous due to the above-mentioned conditions, yet all OSM-sourced routing softwares direct me to walk this road. There are ample safer alternatives such as footpaths and roadside pavements that increase the distance to walk by ~300 m.</p>
<p>Is there a way to tag a road as open to pedestrians but dangerous? If there are, do any routing softwares take note of it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-dangerous" rel="tag" title="see questions tagged &#39;dangerous&#39;">dangerous</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '16, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/3f65346fceedcaa10489dd5e19e255b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iainrist&#39;s gravatar image" />
<p><span>iainrist</span><br />
<span class="score" title="86 reputation points">86</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iainrist has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47997" class="comments-container">
&#10;</div>
<div id="comment-tools-47997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47997-form-container" class="comment-form-container">
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

<span id="47998"></span>

<div id="answer-container-47998" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47998-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-47998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I sympathise, here's my example: <a href="http://www.openstreetmap.org/way/24349310">http://www.openstreetmap.org/way/24349310</a>, Spring Lane in Cookham Dean.</p>
<p>Undoubtedly the first thing to add is <a href="http://wiki.openstreetmap.org/wiki/Sidewalks">sidewalk=none</a>. This is the single most useful tag which could be used by routers to optimise for safer routes. There is also the very little used verges tag which looks to take similar values to sidewalk. Also adding a note is a useful start in case we develop more elaborate ways of tagging this.</p>
<p>I don't know of any router which explicitly makes use of this, but it is eminently possible. I would not be surprised if SomeoneElse doesn't use sidewalk in his own Garmin mkgmap routine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '16, 11:33</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-47998" class="comments-container">
<span id="48001"></span>
<div id="comment-48001" class="comment">
<div id="post-48001-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>It should also be helpful to add width. If it is not much more than the average passenger car (which is IIRC 2.1m wide) this could also point out the discomfort pedestrians may experience on that road.</p>
<p>I am a little surprised (and disappointed, too), that you as one of the nearly ideal mappers describe the width in words but not as machine readable tag. :)</p>
</div>
<div id="comment-48001-info" class="comment-info">
<span class="comment-age">(08 Feb '16, 11:54)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
<span id="48002"></span>
<div id="comment-48002" class="comment">
<div id="post-48002-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/583/malenki">@malenki</a> I've never walked along that road since 2006, long before OSM days. Too scary. So I do have an excuse.</p>
</div>
<div id="comment-48002-info" class="comment-info">
<span class="comment-age">(08 Feb '16, 12:06)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="52445"></span>
<div id="comment-52445" class="comment">
<div id="post-52445-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Another suggestion (not much used yet) is the "verge" tag: <a href="https://wiki.openstreetmap.org/wiki/Key:verge">https://wiki.openstreetmap.org/wiki/Key:verge</a> . There may be others.</p>
</div>
<div id="comment-52445-info" class="comment-info">
<span class="comment-age">(10 Oct '16, 16:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47998" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47998-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75599"></span>

<div id="answer-container-75599" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75599-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a number of cycle routers which consider safety such as Cycle-UK or Open Trip Planner. They look at the common tagging and generate a "safety factor", the user then can choose a combination of flatness, safety and directness. A similar thing can and should be done for walk routing.</p>
<p>As per other comments make it bendy, sidewalk=none, verge=none, add a width or est_width tag and speed limit.</p>
<p>Then push for the routing tool you use to consider adding a safety factor from those tags for walking.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jul '20, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/e4a3b88a2d65ba17d20b29c06c10f0d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DevonshireBoy42&#39;s gravatar image" />
<p><span>DevonshireBoy42</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DevonshireBoy42 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75599" class="comments-container">
&#10;</div>
<div id="comment-tools-75599" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75599-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48255"></span>

<div id="answer-container-48255" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48255-score" class="post-score" title="current number of votes">
-5
</div>
<span id="post-48255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Consider also using foot=no to tag ways with no pedestrian access.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '16, 00:43</strong></p>
<img src="https://secure.gravatar.com/avatar/543cbbe52e9c50d608ea79186c912e08?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rhubarb&#39;s gravatar image" />
<p><span>Rhubarb</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rhubarb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48255" class="comments-container">
<span id="48256"></span>
<div id="comment-48256" class="comment">
<div id="post-48256-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>"This is the UK so by right any pedestrian can walk on this road." (from iainrist above) So, your suggested <a href="https://wiki.openstreetmap.org/wiki/Key:access">legal access restriction</a> should not be used here.</p>
</div>
<div id="comment-48256-info" class="comment-info">
<span class="comment-age">(21 Feb '16, 00:55)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="48445"></span>
<div id="comment-48445" class="comment">
<div id="post-48445-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>A lot of my local lanes are 60MPH and have pedestians cyclists and horses on them regularly.</p>
<p>They work withen an older part of the law that says that could drive as fast as you liked (pre-speedlimits) and if you could not safely handle the road or other traffic and obsticals then you could be prosercuted and even held in prison for murder if in a fatal accident.</p>
<p>Speed limits used to be a guide to triming the top speed of faster vehicals especially when improvements relying sightlines and speed-to-sign_size made roads work at up to design speeds before problems for avearge drivers, could occur.</p>
<p>If you can't stop for a drover with cattle or hikers around a blind bend then you can still be deemed as going too fast for the "Conditions". If that dosn't make sence think about the messages to slow with rain, snow and ice it's the same or similar part of the law.</p>
<p>Maps don't often try to handel this leveing it to driver/rider descrestion though some sharp bend and crests can be added sometimes though I'm not sure how OSM tags them at the moment.</p>
</div>
<div id="comment-48445-info" class="comment-info">
<span class="comment-age">(01 Mar '16, 19:40)</span> <span class="comment-user userinfo">Govanus</span>
</div>
</div>
</div>
<div id="comment-tools-48255" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48255-form-container" class="comment-form-container">
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

