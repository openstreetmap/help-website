+++
type = "question"
title = "Priority road crossing, how to correctly map these?"
description = '''Just ran into a dangerous navigation comment due to this. See the situation outside Alhaurín el Grande or graphically:  ++++++++++ -----------------  +  +  +++++++++++++++++  I&#x27;m traveling from left to right, the ++ refer to the main (priority) road A-404, the -- to an old route. I needed to go onto...'''
date = "2012-08-03T17:09:00Z"
lastmod = "2020-06-04T16:45:00Z"
weight = 14815
keywords = [ "priority", "give-way", "crossing", "unequal", "road" ]
aliases = [ "/questions/14815" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Priority road crossing, how to correctly map these?](/questions/14815/priority-road-crossing-how-to-correctly-map-these)

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
<span id="post-14815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14815-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-14815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Just ran into a dangerous navigation comment due to this. <a href="http://www.openstreetmap.org/edit?lat=36.65467&amp;lon=-4.65104&amp;zoom=16">See the situation outside Alhaurín el Grande</a> or graphically:</p>
<pre><code>           ++++++++++ -----------------
                      +
                        +
                          +++++++++++++++++</code></pre>
<p>I'm traveling from left to right, the ++ refer to the main (priority) road A-404, the -- to an old route. I needed to go onto the old road, which means leaving the main road and giving way to any traffic on it coming my way. The comment however was: GO STRAIGHT ON, while IMO it should have been 'Take a left turn' or similar.</p>
<p>I have just now, added 'priority_road=yes_unposted' to the A-404, after finding this possibility, I however do not know if this will solve the potentially dangerous situation, by giving correct comments on the route to follow.</p>
<p>If it does, it would be a lot easier (and thus used a lot more then the, supposedly, only 2000 uses in all OSM) if this option were available in one of the drop-down menus.</p>
<p>If it does not, how should it be mapped correctly?</p>
<p>Additional, but related question, how do I map correctly the way back at the same crossing, where I have to GIVE WAY to the priority road? Can I add a 'Give way' sign to the intersection? If so, how?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-priority" rel="tag" title="see questions tagged &#39;priority&#39;">priority</span> <span class="post-tag tag-link-give-way" rel="tag" title="see questions tagged &#39;give-way&#39;">give-way</span> <span class="post-tag tag-link-crossing" rel="tag" title="see questions tagged &#39;crossing&#39;">crossing</span> <span class="post-tag tag-link-unequal" rel="tag" title="see questions tagged &#39;unequal&#39;">unequal</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '12, 17:09</strong></p>
<img src="https://secure.gravatar.com/avatar/b6930628f98860273e67f69dcae2de87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LimburgCowboy&#39;s gravatar image" />
<p><span>LimburgCowboy</span><br />
<span class="score" title="277 reputation points">277</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LimburgCowboy has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Aug '12, 17:36</strong> </span></p>
</div>
</div>
<div id="comments-container-14815" class="comments-container">
&#10;</div>
<div id="comment-tools-14815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14815-form-container" class="comment-form-container">
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

<span id="14817"></span>

<div id="answer-container-14817" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14817-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are many different routing engines/satnavs using OSM data.</p>
<p>All of them differ in how they interpret OSM data.</p>
<p>Some might understand your tag <code>priority_road=yes_unposted</code> however I doubt that any will. (Note that you mistakenly used a minus sign instead of an underscore in your question).</p>
<p>There is most likely not one true way to map this in OSM to make sure that all routing engines/satnavs do the right thing. If you are interested in one specific routing engine/satnav, you have to (a) tell us which and (b) likely talk to its authors to find out.</p>
<p>Your idea that the situation you describe should be called "making a left turn" seems a bit outlandish to me. It is not a left turn. The instruction "straight on" will typically even be given if you have to stop at a traffic light, or if you have to cross a road that has priority - "straight on" does not usually mean that you have priority.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '12, 17:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-14817" class="comments-container">
<span id="14818"></span>
<div id="comment-14818" class="comment">
<div id="post-14818-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Corrected the underscore.</p>
<p>In this situation 'Making a left turn' is not outlandish, as you will be leaving the designated main-road to the left. If I remember correctly my driving lessons (from long, long ago), this would also referenced as a left turn by my driving instructor.</p>
<p>I am not interested in a specific satnav as I'm using NavFree and OsmAnd as both have their qualities in different situations.</p>
<p>If, at the moment, there is no 'true way' to do this, would it not be time to find it?</p>
</div>
<div id="comment-14818-info" class="comment-info">
<span class="comment-age">(03 Aug '12, 17:41)</span> <span class="comment-user userinfo">LimburgCowboy</span>
</div>
</div>
</div>
<div id="comment-tools-14817" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14817-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14819"></span>

<div id="answer-container-14819" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14819-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, wich traffic sings are there to show the travellers who gets the right of way ? That should give the solutions for this problem. And tag the roads accordingly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '12, 17:41</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-14819" class="comments-container">
<span id="14820"></span>
<div id="comment-14820" class="comment">
<div id="post-14820-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As in Spain generally the 'priority'road-sign (45º tilted square) is not used on priority roads, it can only be guesstimated that you are on one.</p>
<p>However the users of the road entering the priority road, ALWAYS have the give-way (upside-down triangle) or STOP sign. So if I could add the give-way or STOP sign to an intersection-node that could solve part of the problem.</p>
<p>However being able to correctly tag a priority-road as one (and being correctly interpreted by most satnav's) would be the easiest way.</p>
</div>
<div id="comment-14820-info" class="comment-info">
<span class="comment-age">(03 Aug '12, 17:57)</span> <span class="comment-user userinfo">LimburgCowboy</span>
</div>
</div>
</div>
<div id="comment-tools-14819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14819-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="75147"></span>

<div id="answer-container-75147" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75147-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't know how it is in your country, but in most European countries, the situation as drawn in the OP's post is really that by going "straight" (from left) you leave the main road, no signaling necessary. To stay on main road, you have to turn right and signal. Making turns and giving way are 2 different independent actions in a crossroad.</p>
<p>Unless the main road is really marked as being just a large curve (that you are basically following it). In this case it is better to adjust the main road to be in a nice arc, and make the side road join it under a sharper angle so for the navigation it really looks like turning. I did adjust few crossing like this after navigation (Osmand) told me to sharply turn left, where it actually was more like 90 degree turn.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '20, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ce04e9c1d898db2b9bf6cc4a48193239?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vmicho&#39;s gravatar image" />
<p><span>vmicho</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vmicho has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75147" class="comments-container">
&#10;</div>
<div id="comment-tools-75147" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75147-form-container" class="comment-form-container">
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

