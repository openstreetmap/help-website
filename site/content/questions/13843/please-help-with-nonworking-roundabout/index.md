+++
type = "question"
title = "Please help with nonworking roundabout"
description = '''Recently I&#x27;ve added 2 roundabouts to the location near my home, as they were not in the maps yet. The first seems to be ok, but the second is somehow wrong, because the navigation, that uses openstreetmaps as a source for generating map files for itself, refuses to route a way through it. It&#x27;s most ...'''
date = "2012-06-27T13:08:00Z"
lastmod = "2012-07-12T18:58:00Z"
weight = 13843
keywords = [ "problem", "roundabout" ]
aliases = [ "/questions/13843" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Please help with nonworking roundabout](/questions/13843/please-help-with-nonworking-roundabout)

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
<span id="post-13843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13843-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Recently I've added 2 roundabouts to the location near my home, as they were not in the maps yet. The first seems to be ok, but the second is somehow wrong, because the navigation, that uses openstreetmaps as a source for generating map files for itself, refuses to route a way through it.</p>
<p>It's most probably my mistake as I am quite new to this editation, though I have experience with vector editors etc.</p>
<p>Is it possible to test the changes made using some kind of website map?</p>
<p>This is the roundabout <a href="http://www.openstreetmap.org/edit?lat=49.640189&amp;lon=17.319912&amp;zoom=18">http://www.openstreetmap.org/edit?lat=49.640189&amp;lon=17.319912&amp;zoom=18</a></p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-roundabout" rel="tag" title="see questions tagged &#39;roundabout&#39;">roundabout</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jun '12, 13:08</strong></p>
<img src="https://secure.gravatar.com/avatar/ea4deb947ff8163bfdd584589253542c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harvester&#39;s gravatar image" />
<p><span>harvester</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harvester has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13843" class="comments-container">
&#10;</div>
<div id="comment-tools-13843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13843-form-container" class="comment-form-container">
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

<span id="13847"></span>

<div id="answer-container-13847" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13847-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It may be that it doesn't like oneway=-1. Roundabouts don't need a oneway tag, but you then have to draw them in the correct orientation. There is a button in Potlatch 2 to reverse the direction if you need to.</p>
<p>Of course, the above depends what routing implementation you are using and how often they update their routing data. OSRM is pretty up to date usually, and the roundabout looks OK to me <a href="http://map.project-osrm.org/LP">testing there</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jun '12, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-13847" class="comments-container">
<span id="13851"></span>
<div id="comment-13851" class="comment">
<div id="post-13851-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks to the link for map testing! However it really seems to be ok, I'll try to contact the GPS autors.</p>
</div>
<div id="comment-13851-info" class="comment-info">
<span class="comment-age">(27 Jun '12, 14:36)</span> <span class="comment-user userinfo">harvester</span>
</div>
</div>
<span id="13853"></span>
<div id="comment-13853" class="comment">
<div id="post-13853-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting, I've found out that the neighbour roudabout has one-way off and roundabout on, while the problematic one had both on, and the other I made, that works, has on the other hand roundabout off and one-way on. So I assume that the two restrictions together cause the problem. Now I set it all to one-way off, roundabout on and I'll see till the next maps update for the navigation. BTW it's the free MapFactor Navigator Free.</p>
</div>
<div id="comment-13853-info" class="comment-info">
<span class="comment-age">(27 Jun '12, 14:50)</span> <span class="comment-user userinfo">harvester</span>
</div>
</div>
<span id="14233"></span>
<div id="comment-14233" class="comment">
<div id="post-14233-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ive had a look at your your roundabout in the link to testing in EdLoach's answer above. It appears to work Ok now but the direction of traffic flow is still set to clockwise ,as in UK. I sugggest this needs to be anti clockwise in your part of the world. In Potlatch2 the direction of flow can be changed by firstly highlighting the roundabout and then use the icon to the right of the Delete button in the bottom righthand corner of the screen, the one with arrows on, to change the direction .The arrows on the roundabout will change direction as you edit.</p>
</div>
<div id="comment-14233-info" class="comment-info">
<span class="comment-age">(12 Jul '12, 18:58)</span> <span class="comment-user userinfo">BillyWizz</span>
</div>
</div>
</div>
<div id="comment-tools-13847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13847-form-container" class="comment-form-container">
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

