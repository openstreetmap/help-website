+++
type = "question"
title = "Non optimal OSRM route - yet all attributes appear correct."
description = '''When routing from Northallerton (UK) to Bedale (UK) using OSRM routing the route takes a non optimal route. The problem appears to be at a roundabout on an island on the A684 at here Routing from just east of the roundabout to the roundabout takes the correct direct route: correct route whereas rout...'''
date = "2020-01-24T13:46:00Z"
lastmod = "2020-01-27T10:58:00Z"
weight = 72664
keywords = [ "attributes", "routingerror" ]
aliases = [ "/questions/72664" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Non optimal OSRM route - yet all attributes appear correct.](/questions/72664/non-optimal-osrm-route-yet-all-attributes-appear-correct)

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
<span id="post-72664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72664-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When routing from Northallerton (UK) to Bedale (UK) using OSRM routing the route takes a non optimal route. The problem appears to be at a roundabout on an island on the A684 at <a href="https://www.openstreetmap.org/edit?editor=id#map=19/54.31166/-1.54163">here</a></p>
<p>Routing from just east of the roundabout to the roundabout takes the correct direct route: <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=54.31192%2C-1.54049%3B54.31157%2C-1.54170">correct route</a></p>
<p>whereas routing to slightly further round the roundabout routes a completely different and very non optimal way: <a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=54.31192%2C-1.54049%3B54.31151%2C-1.54179">incorrect route</a></p>
<p>I have checked the features and all the features seem to have correct attributes in terms of direction, allowed access, and turn restrictions -<br />
Please could someone tell me what attribute(s) needs changing to get the journey to route correctly</p>
<p>Thanks for any help,</p>
<p>Steve.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-attributes" rel="tag" title="see questions tagged &#39;attributes&#39;">attributes</span> <span class="post-tag tag-link-routingerror" rel="tag" title="see questions tagged &#39;routingerror&#39;">routingerror</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jan '20, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/aa604be467d765143ba6dc671e30714d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steve%20P&#39;s gravatar image" />
<p><span>Steve P</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steve P has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-72664" class="comments-container">
&#10;</div>
<div id="comment-tools-72664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72664-form-container" class="comment-form-container">
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

<span id="72665"></span>

<div id="answer-container-72665" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72665-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you switch to Car (Graphhopper) rather than Car (OSRM) the routing seems to work OK, so either the Fossgis routing service hasn't picked up any changes yet that you made which fixed the problem, or it is an OSRM rather than data problem.</p>
<p>Edit: I just realised you might not be the K<a href="https://www.openstreetmap.org/changeset/79988324">eirC who edited the junction about 22 hours ago</a> - but those changes might not have been picked up yet</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jan '20, 14:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jan '20, 14:21</strong> </span></p>
</div>
</div>
<div id="comments-container-72665" class="comments-container">
<span id="72666"></span>
<div id="comment-72666" class="comment">
<div id="post-72666-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer - the change(s) you mention were made by a colleague of mine - we're both new to OSM ... in case that these changes do need to take effect, roughly how long should it take for Fossgis to pickup the change (is it days or weeks or ...).</p>
<p>As the routing has been incorrect for many months (and I dont actually think the changes made by KeirC were particularly vital) I suspect it is probably an OSRM routing rather than data problem - if this is the case how should this be reported to OSM?</p>
<p>Thanks, Steve</p>
</div>
<div id="comment-72666-info" class="comment-info">
<span class="comment-age">(24 Jan '20, 14:48)</span> <span class="comment-user userinfo">Steve P</span>
</div>
</div>
<span id="72667"></span>
<div id="comment-72667" class="comment">
<div id="post-72667-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I don't know how often the Fossgis data updates. I've just tested on my phone using OsmAnd which updates monthly (although I've not downloaded the January update yet) and routing across the roundabout works fine on there again, so that would be data from 1st December.</p>
<p>I did wonder whether all the weird proposed tags on the roundabout might be causing the issue, or that this way <a href="https://www.openstreetmap.org/way/766035733">https://www.openstreetmap.org/way/766035733</a> seems to end at a strange point rather than where the road splits, but I don't know the technical details of how OSRM works.</p>
</div>
<div id="comment-72667-info" class="comment-info">
<span class="comment-age">(24 Jan '20, 15:07)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="72669"></span>
<div id="comment-72669" class="comment">
<div id="post-72669-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I wouldn't be surprised if it is due to the strange combination of proposed tags as you say. It is not obvious from the tags whether there is currently a road there or not. In particular the wiki page for "proposed" seems to suggest that highway:proposed=no means that the road is due to be removed. It may be that different routers make different guesses about which tags take priority.</p>
<p>I also note that the proposed tags were added nearly 4 years ago. If they refer to a project that has either been completed or abandoned they should probably be deleted.</p>
</div>
<div id="comment-72669-info" class="comment-info">
<span class="comment-age">(24 Jan '20, 18:31)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-72665" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72665-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72713"></span>

<div id="answer-container-72713" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72713-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for the suggestions. The roundabout is complete (no longer proposed) so I'll remove those tags and see if that makes a difference to the routing.</p>
<p>Steve</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '20, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/aa604be467d765143ba6dc671e30714d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steve%20P&#39;s gravatar image" />
<p><span>Steve P</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steve P has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72713" class="comments-container">
&#10;</div>
<div id="comment-tools-72713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72713-form-container" class="comment-form-container">
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

