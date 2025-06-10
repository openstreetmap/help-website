+++
type = "question"
title = "Connecting a separated cycle track"
description = '''I&#x27;m trying to draw a separated two-way cycle track that is attached to a main road (separated by bollards, very clearly marked). The wiki suggests two ways of doing this: Either I use cycleway=track on the road, or I draw a separate cycle path parallel to the road. I&#x27;d like to use the latter; it&#x27;s m...'''
date = "2019-11-25T04:50:00Z"
lastmod = "2019-11-26T21:26:00Z"
weight = 71808
keywords = [ "cycle" ]
aliases = [ "/questions/71808" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Connecting a separated cycle track](/questions/71808/connecting-a-separated-cycle-track)

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
<span id="post-71808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71808-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to draw a separated two-way cycle track that is attached to a main road (separated by bollards, very clearly marked).</p>
<p>The wiki <a href="https://wiki.openstreetmap.org/wiki/Key:cycleway#Cycle_tracks">suggests two ways of doing this</a>: Either I use <code>cycleway=track</code> on the road, or I draw a separate cycle path parallel to the road. I'd like to use the latter; it's much easier to understand when reading maps.</p>
<p>The wiki mentions:</p>
<blockquote>
<p>It is of paramount importance, to properly connect separately drawn cycle tracks to general roads and to other paths. This is both to reflect ground truth and to aid routing algorithms, which cannot 'understand' or take a chance on this by themselves, even though the distance might be less than a metre, or even if lines cross but the ways do not have merged nodes.</p>
</blockquote>
<p>This makes sense, but I'm not 100% sure what the exact way to do this is: should we be adding extra cycle tracks to connect with features, or should we extend features to hit the cycle tracks?</p>
<p>If I have the following situation, I have two ways of connecting the cycle track (top left) to the parking aisle (bottom right). I can either extend the parking aisle route further across the road (yellow diagonal) to connect with the track, or I can draw a tiny branch off the cycle track that meets at the junction. It seems like the former is the better option, but I'm not sure.</p>
<p>(Note: the satellite imagery here hasn't been updated to show the cycle track, but it's where the old cycle lane used to be)</p>
<p><img src="https://help.openstreetmap.org/upfiles/Capture_ZsfChq1.PNG" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cycle" rel="tag" title="see questions tagged &#39;cycle&#39;">cycle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Nov '19, 04:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0a3069491bfded90cdf623341cadc1d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manishearth&#39;s gravatar image" />
<p><span>Manishearth</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manishearth has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-71808" class="comments-container">
&#10;</div>
<div id="comment-tools-71808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71808-form-container" class="comment-form-container">
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

<span id="71809"></span>

<div id="answer-container-71809" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71809-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Manishearth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Personally I would usually extend the parking aisle to the cycle track if there were a suitable dropped curb etc. for the bikes to drive over. There has been a recent proposal for <code>footway=link</code> for the pedestrian version of your first suggestion, but this has not been approved yet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '19, 07:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-71809" class="comments-container">
<span id="71810"></span>
<div id="comment-71810" class="comment">
<div id="post-71810-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! We should probably mention this in the wiki somehow if it's the most common way to do things.</p>
</div>
<div id="comment-71810-info" class="comment-info">
<span class="comment-age">(25 Nov '19, 08:03)</span> <span class="comment-user userinfo">Manishearth</span>
</div>
</div>
<span id="71811"></span>
<div id="comment-71811" class="comment">
<div id="post-71811-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't know whether it's truly the most common. I tend to think of it as the simplest way that isn't 'wrong', similar to extending the service road through a dual carriageway rather than stopping at the first lane and transitioning into <code>primary_link</code>.</p>
</div>
<div id="comment-71811-info" class="comment-info">
<span class="comment-age">(25 Nov '19, 08:20)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="71831"></span>
<div id="comment-71831" class="comment">
<div id="post-71831-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>AFAIK, In the country where I map, this would be changed to the way SK53 describes</p>
</div>
<div id="comment-71831-info" class="comment-info">
<span class="comment-age">(26 Nov '19, 04:12)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-71809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71809-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71821"></span>

<div id="answer-container-71821" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71821-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-71821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I disagree with InsertUser here, albeit in details rather than in principle.</p>
<p>I would connect the service road to the main road, <strong>BUT NOT</strong> to the cycleway. Instead I would create a short cycleway from the main cycleway to join the service road where it intersects the service road. These would be rather equivalent to the footway=link suggestion as InsertUser remarks. The reason for doing it this way are: you cant drive from the service road onto the cycleway; it doesn't require lots of additional access tags; and (co-incidentally) it happens to render more cleanly.</p>
<p>Equivalent constructions are quite common with footpaths in estates with many short service roads.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '19, 16:58</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-71821" class="comments-container">
<span id="71822"></span>
<div id="comment-71822" class="comment">
<div id="post-71822-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Won't it render the cycleway as having a lot of little "hairs" on maps?</p>
</div>
<div id="comment-71822-info" class="comment-info">
<span class="comment-age">(25 Nov '19, 17:18)</span> <span class="comment-user userinfo">Manishearth</span>
</div>
</div>
<span id="71830"></span>
<div id="comment-71830" class="comment">
<div id="post-71830-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/17488/manishearth"></a><a href="https://help.openstreetmap.org/users/17488/manishearth">@Manishearth</a>: you shouldn't care about the rendering, but about the correctness of the data, for the reason SK53 gives: "you cannot dive from the service road onto the cycleway"</p>
</div>
<div id="comment-71830-info" class="comment-info">
<span class="comment-age">(26 Nov '19, 04:05)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="71834"></span>
<div id="comment-71834" class="comment">
<div id="post-71834-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/17488/manishearth">@Manishearth</a>: in practice the road will be rendered over the cycleway so that at most zoom levels it will be either totally obscured or barely visible. If the footway=link suggestion is adopted then renders could, in the future, choose not to render such ways.</p>
</div>
<div id="comment-71834-info" class="comment-info">
<span class="comment-age">(26 Nov '19, 10:58)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="71854"></span>
<div id="comment-71854" class="comment">
<div id="post-71854-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the bollards mentioned in the question were mapped on the side road then they wouldn't be passable by cars either. <code>cycleway=link</code> would be the nicest if that style ever gets approved.</p>
</div>
<div id="comment-71854-info" class="comment-info">
<span class="comment-age">(26 Nov '19, 21:26)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-71821" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71821-form-container" class="comment-form-container">
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

