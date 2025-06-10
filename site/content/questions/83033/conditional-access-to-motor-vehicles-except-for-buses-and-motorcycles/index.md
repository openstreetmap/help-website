+++
type = "question"
title = "Conditional access to motor vehicles except for buses and motorcycles"
description = '''Hello,  I have a question regarding correct tags on a road with conditional access to motor vehicles with an exception for buses, motorcycles, mopeds, mofas. Specifically, I am not sure Grafton Bridge, Auckland, New Zealand (36°51&#x27;33.4&quot;S 174°45&#x27;54.1&quot;E) has correct tagging.  Grafton Bridge:   1 lane ...'''
date = "2022-01-10T10:38:00Z"
lastmod = "2022-01-11T05:11:00Z"
weight = 83033
keywords = [ "buslane", "conditional", "motorcycle", "designation", "motor_vehicle" ]
aliases = [ "/questions/83033" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Conditional access to motor vehicles except for buses and motorcycles](/questions/83033/conditional-access-to-motor-vehicles-except-for-buses-and-motorcycles)

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
<span id="post-83033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83033-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have a question regarding correct tags on a road with conditional access to motor vehicles with an exception for buses, motorcycles, mopeds, mofas. Specifically, I am not sure Grafton Bridge, Auckland, New Zealand (36°51'33.4"S 174°45'54.1"E) has correct tagging.</p>
<p><strong>Grafton Bridge:</strong></p>
<ul>
<li><p>1 lane in each direction</p></li>
<li><p>condition - 7am-7pm, Mo-Fr - Bus Lane (access to buses, motorcycles, mopeds, mofas, psv) (<a href="https://www.nzta.govt.nz/walking-cycling-and-public-transport/cycling/cycling-standards-and-guidance/cycling-network-guidance/designing-a-cycle-facility/between-intersections/bus-lanes/">Bus lane access description</a>)</p></li>
</ul>
<p><strong>Current tags are following:</strong></p>
<pre><code>bicycle=yes 
bridge=yes
bus:lanes:backward=designated
bus:lanes:forward=designated 
foot=yes
highway=secondary 
lanes=2 
layer=1
maxspeed=30 
maxweight=44
motor_vehicle:conditional=no @ (Mo-Fr 07:00-19:00) 
motorcycle=yes
name=Grafton Bridge 
name:ja=グラフトン橋
psv=yes 
surface=asphalt</code></pre>
<p><strong>Question:</strong> Now, doesn't the bus:lanes occupy all the lanes and prevent all other vehicles from access? I would see the tags rather as following:</p>
<pre><code>bicycle=yes 
bridge=yes
bus:lanes:backward=designated @ (Mo-Fr 07:00-19:00)
bus:lanes:forward=designated @ (Mo-Fr 07:00-19:00)
cycleway=share_busway
? Exception for motorcycles ?
foot=yes
highway=secondary 
lanes=2 
layer=1
maxspeed=30 
maxweight=44
name=Grafton Bridge 
name:ja=グラフトン橋
surface=asphalt</code></pre>
<p>Or</p>
<pre><code>bicycle=yes 
bridge=yes
foot=yes
highway=secondary 
lanes=2 
layer=1
maxspeed=30 
maxweight=44
motor_vehicle:conditional=no @ (Mo-Fr 07:00-19:00) 
motorcycle=yes
bus=yes
moped=yes
mofa=yes
name=Grafton Bridge 
name:ja=グラフトン橋
psv=yes 
surface=asphalt</code></pre>
<p>Do I understand right that when there is a tag with a sub-group (motorcycle) of motor_vehicle, and without conditions, it excludes these from the motor_vehicle conditions?</p>
<p>Thanks a lot!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buslane" rel="tag" title="see questions tagged &#39;buslane&#39;">buslane</span> <span class="post-tag tag-link-conditional" rel="tag" title="see questions tagged &#39;conditional&#39;">conditional</span> <span class="post-tag tag-link-motorcycle" rel="tag" title="see questions tagged &#39;motorcycle&#39;">motorcycle</span> <span class="post-tag tag-link-designation" rel="tag" title="see questions tagged &#39;designation&#39;">designation</span> <span class="post-tag tag-link-motor_vehicle" rel="tag" title="see questions tagged &#39;motor_vehicle&#39;">motor_vehicle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jan '22, 10:38</strong></p>
<img src="https://secure.gravatar.com/avatar/4660eafc9d705be1c65dd6f06577b999?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KingCZE&#39;s gravatar image" />
<p><span>KingCZE</span><br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KingCZE has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83033" class="comments-container">
&#10;</div>
<div id="comment-tools-83033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83033-form-container" class="comment-form-container">
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

<span id="83046"></span>

<div id="answer-container-83046" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83046-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is only one lane per direction and the same restrictions apply to both directions. So there is no need for any <code>:lanes</code> tagging. <code>bicycle=yes</code>, <code>foot=yes</code> etc. don't need to be tagged as they are default for a <code>highway=secondary</code>.</p>
<p>Your last question is a bit tricky and interpretation of conditions might be implemented differently by data consumers. To be on the safe side I would explicitly tag what might be confusing.</p>
<p>I'd propose:</p>
<pre><code>highway=secondary  
name=Grafton Bridge  
name:ja=グラフトン橋  
bridge=yes  
lanes=2  
layer=1  
maxspeed=30  
maxweight=44  
surface=asphalt  
sidewalk=both  
motor_vehicle:conditional=no @ (Mo-Fr 07:00-19:00)  
motorcycle:conditional=yes@ (Mo-Fr 07:00-19:00)  
bus:conditional=yes @ (Mo-Fr 07:00-19:00) (or psv?)  
moped:conditional=yes @ (Mo-Fr 07:00-19:00)  
mofa:conditional=yes @ (Mo-Fr 07:00-19:00)</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jan '22, 21:21</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-83046" class="comments-container">
<span id="83051"></span>
<div id="comment-83051" class="comment">
<div id="post-83051-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That is what I thought, thank you. I do not really understand why there was originally "bus:lanes:backward=designated..." as for one lane in each direction, it would occupy all lanes. These Bus Lanes in New Zealand are not the best for OSM tagging :D</p>
<p>Thank you, I agree...</p>
</div>
<div id="comment-83051-info" class="comment-info">
<span class="comment-age">(11 Jan '22, 05:11)</span> <span class="comment-user userinfo">KingCZE</span>
</div>
</div>
</div>
<div id="comment-tools-83046" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83046-form-container" class="comment-form-container">
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

