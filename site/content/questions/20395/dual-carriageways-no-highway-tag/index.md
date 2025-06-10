+++
type = "question"
title = "Dual carriageways - no highway tag?"
description = '''I am currently doing some processing of OSM highway data, and attempting to identify speed limits for highways. Of course, some highways are tagged with maxspeed=*, but where this is absent or clearly incorrect, I would like to assume a default speed limit for the road based on its type. In the UK, ...'''
date = "2013-02-28T16:47:00Z"
lastmod = "2013-03-03T09:11:00Z"
weight = 20395
keywords = [ "carriageway", "highway", "dual" ]
aliases = [ "/questions/20395" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dual carriageways - no highway tag?](/questions/20395/dual-carriageways-no-highway-tag)

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
<span id="post-20395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20395-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am currently doing some processing of OSM highway data, and attempting to identify speed limits for highways. Of course, some highways are tagged with maxspeed=*, but where this is absent or clearly incorrect, I would like to assume a default speed limit for the road based on its type.</p>
<p>In the UK, the default national speed limit is 70mph on motorways and dual carriageways, 60mph on other roads. So, for example, a "highway=primary" road could be either 70mph or 60mph[1].</p>
<p>I understand that dual carriageways are normally mapped as separate ways, but as far as I can from the wiki, there is no way to determine from highway tags that the way is part of a dual carriageway.</p>
<p>Is the only/correct way to determine this, to check whether there is a relation that includes the way, and is tagged as a dual carriageway?</p>
<p>[1] There is an additional complication - the speed limit for a highway may vary according to the vehicle type, weight etc., which may not be representable using the maxspeed tag. I guess that's a separate question, though!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-carriageway" rel="tag" title="see questions tagged &#39;carriageway&#39;">carriageway</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span> <span class="post-tag tag-link-dual" rel="tag" title="see questions tagged &#39;dual&#39;">dual</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '13, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/9b6b142985091a1566e3f91e1902284d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dave&#39;s gravatar image" />
<p><span>Dave</span><br />
<span class="score" title="86 reputation points">86</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dave has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Feb '13, 16:56</strong> </span></p>
</div>
</div>
<div id="comments-container-20395" class="comments-container">
<span id="20396"></span>
<div id="comment-20396" class="comment">
<div id="post-20396-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>In some areas (Derbyshire's an example), many / most "highway=primary" roads aren't national limit (either 60 or 70 depending on carriageway separation) but are actively signed at 50mph or lower. Where maxspeed's missing, you probably need to get out and survey.</p>
</div>
<div id="comment-20396-info" class="comment-info">
<span class="comment-age">(28 Feb '13, 16:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="20457"></span>
<div id="comment-20457" class="comment">
<div id="post-20457-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Additional complications: There's many dual carriageways that aren't part of a route relation (because they're not part of a route), and extreme cases have different speed limits for day and night and by type of vehicle (such as Montana's very common "reasonable and prudent" daytime speed, 65 daytime HGV/PSV speed, 55 night speed, and 45 night HGV/PSV speed. Or Oregon's "no speed limit but basic speed rule still applies and it may really be 55 even when outside speed zones" speed limit, with a mandatory 55 for HGV even when there is no speed zone.</p>
</div>
<div id="comment-20457-info" class="comment-info">
<span class="comment-age">(03 Mar '13, 09:11)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-20395" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20395-form-container" class="comment-form-container">
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

<span id="20399"></span>

<div id="answer-container-20399" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20399-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-20399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In OSM, most dual-carriageways are not specifically tagged as such. But the separate ways will be tagged as <code>oneway=yes</code>. So in the UK, you can probably assume that a way tagged as <code>highway=trunk</code> or <code>highway=primary</code> plus <code>oneway=yes</code> will be part of a dual-carriageway. Though there may be some exceptions to this.</p>
<p>Many major roads are mapped with route relations, but these usually don't specify if it is dual-carriageway or not. Some route relations include both single and dual-carriageway sections of a route.</p>
<p>You could do some sort of query in GIS software, ie if there are 2 ways running in opposite directions approximately parallel to each other, and both tagged with <code>highway=primary</code>/<code>trunk</code>, and <code>oneway=yes</code>, and both have the same <code>ref</code>/<code>name</code> tag, then they are part of a dual carriageway. But this is rather complicated, and may require a lot of processing.</p>
<p>Of course, even if a road is dual-carriageway, it may not have a speed limit of 70 mph. eg there may be a lower speed if it passes through an urban area, or some other restriction. So best to survey the roads and tag the actual speed where possible.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '13, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Feb '13, 18:51</strong> </span></p>
</div>
</div>
<div id="comments-container-20399" class="comments-container">
<span id="20421"></span>
<div id="comment-20421" class="comment">
<div id="post-20421-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, that's useful information. Looking for parallel ways is an option, though I would do that in my own codespace as I'm importing and processing the OSM data myself. Of course the maxspeed tag (where present and sensible-looking) would always take precedence.</p>
<p>Unfortunately, as I'm trying to build a database of all roads within the EU (and eventually beyond), getting out and surveying them isn't really an option!</p>
</div>
<div id="comment-20421-info" class="comment-info">
<span class="comment-age">(01 Mar '13, 13:11)</span> <span class="comment-user userinfo">Dave</span>
</div>
</div>
</div>
<div id="comment-tools-20399" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20399-form-container" class="comment-form-container">
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

