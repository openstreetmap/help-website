+++
type = "question"
title = "Unique Road Type - How to Include it on the map"
description = '''Our region is building a 50-mile paved road called CV Link that is restricted to pedestrians, bicycles, and low-speed electric vehicles e.g. golf carts. It&#x27;s the first roadway of its kind in the US and is considered high-profile with government officials from across the US, the media, and tourists v...'''
date = "2018-08-03T00:20:00Z"
lastmod = "2018-08-03T15:55:00Z"
weight = 65088
keywords = [ "electric_vehicle", "restrictions", "road" ]
aliases = [ "/questions/65088" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Unique Road Type - How to Include it on the map](/questions/65088/unique-road-type-how-to-include-it-on-the-map)

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
<span id="post-65088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65088-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Our region is building a 50-mile paved road called CV Link that is restricted to pedestrians, bicycles, and low-speed electric vehicles e.g. golf carts. It's the first roadway of its kind in the US and is considered high-profile with government officials from across the US, the media, and tourists visiting the area wanting to know the route. Three miles of it has already been opened and gets a lot of use.</p>
<p>What kind of road type would I use for this and how could I say that it can be used by low-speed electric vehicles? Including this is important because allowing this type of vehicle allowed it to be designated as a highway under California State Law. This makes it eligible to receive funds collected through a special tax for building and repairing highways. Anything that prevents the roadway from being seen as including low-speed electric vehicles makes people suspicious of taxpayer funds being misused and can jeopardize the completion of the roadway.</p>
<p>Here's a promotional video from the agency in charge of building CV Link: <a href="https://vimeo.com/97478887.">https://vimeo.com/97478887.</a> It may give you a clearer picture than my explanation does.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-electric_vehicle" rel="tag" title="see questions tagged &#39;electric_vehicle&#39;">electric_vehicle</span> <span class="post-tag tag-link-restrictions" rel="tag" title="see questions tagged &#39;restrictions&#39;">restrictions</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '18, 00:20</strong></p>
<img src="https://secure.gravatar.com/avatar/a4fa74f949029b84fd8768938cd5231d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PSTekbear&#39;s gravatar image" />
<p><span>PSTekbear</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PSTekbear has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65088" class="comments-container">
&#10;</div>
<div id="comment-tools-65088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65088-form-container" class="comment-form-container">
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

<span id="65091"></span>

<div id="answer-container-65091" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65091-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-65091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I agree that this should be tagged as a highway=path, and surface=paved. This is the standard designation for paved MUPs (multi-use paths) which exclude internal combustion motor vehicles. Often electric bicycles and mobility devices are allowed, and in this case it sounds like golf carts and similar low-speed electric vehicles are allowed. The paths within golf courses are similarly designated.</p>
<p>To show that low-speed electric vehicles are allowed, add golf_cart=yes or golf_cart=designated if there are signs that specifically state that this is route designed for golf carts / low-speed EV's. You can also add bicycle=yes, foot=yes, and horses=yes or no depending on the signs.</p>
<p>[The official website calls this a "path" as well: "CV Link is an award-winning plan to combine pedestrians, bicyclists, and low-speed electric vehicles (including golf carts) on a dual pathway. CV Link will connect Coachella Valley cities and the lands of three federally recognized tribes with an primarily road separated path that largely parallels Highway 111, the busiest corridor in the valley." (<a href="http://www.coachellavalleylink.com/">http://www.coachellavalleylink.com/</a> main page)]</p>
<p>In theory, you could also make up a new tag such as "low_speed_ev=yes", but I believe most everyone calls these vehicles "golf carts" and they golf_cart tag is well established. Often the names of the tags are different than what we would like in America, due to their origin in British English usage.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '18, 05:19</strong></p>
<img src="https://secure.gravatar.com/avatar/984eadc21cb77cb316db4ff21c94b869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joseph%20E&#39;s gravatar image" />
<p><span>Joseph E</span><br />
<span class="score" title="390 reputation points">390</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joseph E has 2 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-65091" class="comments-container">
<span id="65106"></span>
<div id="comment-65106" class="comment">
<div id="post-65106-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just one comment: from the video, it looked like the surface was paved in some areas, but unpaved in others.</p>
</div>
<div id="comment-65106-info" class="comment-info">
<span class="comment-age">(03 Aug '18, 14:42)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="65109"></span>
<div id="comment-65109" class="comment">
<div id="post-65109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/595/neuhausr">@neuhausr</a>, I thought they tried to express that they will make a paved paved and the the unpaved area track will disappear.</p>
</div>
<div id="comment-65109-info" class="comment-info">
<span class="comment-age">(03 Aug '18, 15:22)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="65112"></span>
<div id="comment-65112" class="comment">
<div id="post-65112-score" class="comment-score">
3
</div>
<div class="comment-text">
<blockquote>
<p>You can also add bicycle=yes, foot=yes, and horses=yes</p>
</blockquote>
<p>I'd change that "can" to "must" - highway=path with no access tags is pretty much useless as no routers will know whether or not it's usable.</p>
</div>
<div id="comment-65112-info" class="comment-info">
<span class="comment-age">(03 Aug '18, 15:32)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="65114"></span>
<div id="comment-65114" class="comment">
<div id="post-65114-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15477/joseph-e">@Joseph E</a> : unfortunately highway=path does NOT always mean a MUP. In various places it may mean: an unpaved rural footpath (common in UK), some kind of path with unknown properties; a MUP; a footway/bridleway/cycleway which allows uses distinct from the local default (e.g., in DE cycleway is bike only; in UK it always allows foot); and probably some meanings I've forgotten. As <a href="https://help.openstreetmap.org/users/5/richard">@Richard</a> says, this means that access tags for all allowed transport modes are pretty much mandatory with highway=path.</p>
</div>
<div id="comment-65114-info" class="comment-info">
<span class="comment-age">(03 Aug '18, 15:55)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65091" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65091-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65089"></span>

<div id="answer-container-65089" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65089-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I see a surfaced path with foot=yes;bicycle-yes and and "some other vehicle group"=yes. AFAIK, we do not have an tag for the low speed electric vehicles.</p>
<p>I leave it to native British English speakers to come up with the correct word for that group of vehicles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Aug '18, 04:10</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-65089" class="comments-container">
&#10;</div>
<div id="comment-tools-65089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65089-form-container" class="comment-form-container">
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

