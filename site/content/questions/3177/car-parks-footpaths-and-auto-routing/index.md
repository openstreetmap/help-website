+++
type = "question"
title = "Car parks footpaths and auto-routing"
description = '''When using auto-routing on my GPS whenever the track meets a car park the GPS will try and find a way around it or changes my &#x27;preferences&#x27; to direct to&#x27;. On one particular route the automatically generated route will add about 5 km of road and bike track to &#x27;get around&#x27; about 50m of car park! Is th...'''
date = "2011-02-19T06:46:00Z"
lastmod = "2011-02-20T17:02:00Z"
weight = 3177
keywords = [ "car", "tracks", "bike", "auto-routing", "parks" ]
aliases = [ "/questions/3177" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Car parks footpaths and auto-routing](/questions/3177/car-parks-footpaths-and-auto-routing)

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
<span id="post-3177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3177-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When using auto-routing on my GPS whenever the track meets a car park the GPS will try and find a way around it or changes my 'preferences' to direct to'. On one particular route the automatically generated route will add about 5 km of road and bike track to 'get around' about 50m of car park! Is there a way to treat car parks as both a physical thing and traversable objects like cycle paths or roads such that auto-routing will still work?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-car" rel="tag" title="see questions tagged &#39;car&#39;">car</span> <span class="post-tag tag-link-tracks" rel="tag" title="see questions tagged &#39;tracks&#39;">tracks</span> <span class="post-tag tag-link-bike" rel="tag" title="see questions tagged &#39;bike&#39;">bike</span> <span class="post-tag tag-link-auto-routing" rel="tag" title="see questions tagged &#39;auto-routing&#39;">auto-routing</span> <span class="post-tag tag-link-parks" rel="tag" title="see questions tagged &#39;parks&#39;">parks</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '11, 06:46</strong></p>
<img src="https://secure.gravatar.com/avatar/e74cecd2af836e176edeb119236d97c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PSD&#39;s gravatar image" />
<p><span>PSD</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PSD has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3177" class="comments-container">
<span id="3178"></span>
<div id="comment-3178" class="comment">
<div id="post-3178-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In my ears that sounds a litte bit like a router specific problem. But anyway, do you have a map link or lat/long to a car park where that problem occurs, so people can look further into it?</p>
<p>What GPS model do you use?</p>
<p>From where do you get the GPS map files?</p>
</div>
<div id="comment-3178-info" class="comment-info">
<span class="comment-age">(19 Feb '11, 06:51)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
</div>
<div id="comment-tools-3177" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3177-form-container" class="comment-form-container">
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

<span id="3182"></span>

<div id="answer-container-3182" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3182-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One can map the "roads" in car parks as ways with <code>highway=service</code> and <code>service=parking_aisle</code>. But I'd consider every router that uses parking aisle as shortcuts to be quite broken.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '11, 11:32</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-3182" class="comments-container">
<span id="3188"></span>
<div id="comment-3188" class="comment">
<div id="post-3188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>when map was made the car park must have joined some roads for instance two controlled entry's ,not a problem on a bike or foot but if you have to pay to enter or exit a car it is.this could be hard to tag</p>
</div>
<div id="comment-3188-info" class="comment-info">
<span class="comment-age">(19 Feb '11, 14:13)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="3189"></span>
<div id="comment-3189" class="comment">
<div id="post-3189-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>perhaps splitting car park into two would solve the edit problem and the auto routing</p>
</div>
<div id="comment-3189-info" class="comment-info">
<span class="comment-age">(19 Feb '11, 14:15)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="3190"></span>
<div id="comment-3190" class="comment">
<div id="post-3190-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>where is it? some body will edit the map if you tell then where. but you will have to wait for the update on the GPS map and then update the gps with it</p>
</div>
<div id="comment-3190-info" class="comment-info">
<span class="comment-age">(19 Feb '11, 14:20)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="3204"></span>
<div id="comment-3204" class="comment">
<div id="post-3204-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In some jurisdictions/countries/cities it's legal to use parking aisles as shortcuts provided you observe the speed limit. It is therefore good practice to tag as much information as possible. Fortunately you have a number of access tags to choose from, incl "no", "yes" and "destination".</p>
</div>
<div id="comment-3204-info" class="comment-info">
<span class="comment-age">(19 Feb '11, 19:26)</span> <span class="comment-user userinfo">Nic Roets</span>
</div>
</div>
</div>
<div id="comment-tools-3182" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3182-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3202"></span>

<div id="answer-container-3202" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3202-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm assuming you are routing in bicycle mode.</p>
<p>Firstly, make sure that there is no trivial problem with the data. If there is a service way that runs through the parking lot, it will have to be tagged with bicycle=yes. If there is a gate or other barrier along the this way, make sure it is also tagged with bicycle=yes, as the default is access=no. If the service road is closed to the public, and you have special permission to use it, tag it with access=no and use multi point routing tool that allows you skip over the service way.</p>
<p>Now let's assume the parking lot is complete unorganized space and it would be wrong to add a routable way through it. Then the bad news is that I have never hear of any production quality street map routing software or firmware that can route through a polygon. One of the reasons is that it's more computationally expensive. The other reason if that it's quite rare and the detours are typically not very long.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '11, 18:17</strong></p>
<img src="https://secure.gravatar.com/avatar/d25927545eb18b4d577280081df5ce6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nic%20Roets&#39;s gravatar image" />
<p><span>Nic Roets</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nic Roets has one accepted answer">6%</span></p>
</div>
</div>
<div id="comments-container-3202" class="comments-container">
&#10;</div>
<div id="comment-tools-3202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3202-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3221"></span>

<div id="answer-container-3221" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3221-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the car park is in the UK ( I have that map on my garmin) please tell us where,I'll feed it into my Garmin and see if it duplicates the problem, that will tell us if its a device or device software problem. Somebody could also edit the car park with a dividing line so hopefully the routing prog in your device sees a dead end. If OSM is edited it wouldn't solve the problem until you had the new OSM (the just edited) map in your device and if you use a download that in created by someone else it could be a week or two before you could install it</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '11, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-3221" class="comments-container">
&#10;</div>
<div id="comment-tools-3221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3221-form-container" class="comment-form-container">
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

