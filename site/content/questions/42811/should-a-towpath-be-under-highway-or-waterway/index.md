+++
type = "question"
title = "Should a towpath be under highway or waterway?"
description = '''I&#x27;m looking to see how to define a towpath on a canal or river as a seperate way from the waterway it self; so I can show features along it and its course better. I&#x27;ve tried looking in tag info but the numbers are low and inconclusive as to use k=&quot;waterway&quot;,v=&quot;towpath&quot; or k=&quot;highway&quot;,v=&quot;towpath&quot; I&#x27;v...'''
date = "2015-05-02T17:12:00Z"
lastmod = "2015-05-05T21:43:00Z"
weight = 42811
keywords = [ "canal", "waterway", "river", "towpath", "highway" ]
aliases = [ "/questions/42811" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Should a towpath be under highway or waterway?](/questions/42811/should-a-towpath-be-under-highway-or-waterway)

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
<span id="post-42811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42811-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking to see how to define a towpath on a canal or river as a seperate way from the waterway it self; so I can show features along it and its course better.</p>
<p>I've tried looking in tag info but the numbers are low and inconclusive as to use k="waterway",v="towpath" or k="highway",v="towpath"</p>
<p>I've found how people have tagged towpaths like sidewalks as a tag to the main highway (such as towpath=left, right, both) but I wanted to make a better distinction as the route is appearing as cycleways and footpaths as opposed to being a drag route for horses, people, and sometimes landtugs pulling boats and barges.</p>
<p>There other tags and relations already on the route to allow for its other rolls (cycleway, footpath, bridleway etc) but none for the main reason that it is there in the first place!</p>
<p>If all the other users have tags can the path be marked as a towpath kind? like the distinction in the highway tag between cycleway, footway and tertiary.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-canal" rel="tag" title="see questions tagged &#39;canal&#39;">canal</span> <span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span> <span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-towpath" rel="tag" title="see questions tagged &#39;towpath&#39;">towpath</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '15, 17:12</strong></p>
<img src="https://secure.gravatar.com/avatar/30d90feb3a40fa6255767f95a8cd7943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Govanus&#39;s gravatar image" />
<p><span>Govanus</span><br />
<span class="score" title="154 reputation points">154</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Govanus has one accepted answer">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 May '15, 17:13</strong> </span></p>
</div>
</div>
<div id="comments-container-42811" class="comments-container">
&#10;</div>
<div id="comment-tools-42811" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42811-form-container" class="comment-form-container">
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

<span id="42814"></span>

<div id="answer-container-42814" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42814-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-42814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Govanus has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The towpath should be tagged as a <code>highway=footway</code> or <code>highway=cycleway</code>, depending on whether it's been upgraded for cycle use or not. Adding a <code>surface=</code> tag is always good.</p>
<p>To indicate that it's a towpath, many UK mappers also add <code>towpath=yes</code>. Where the towpath is on a CRT waterway and you know it is owned by CRT, you could add <code>operator=Canal &amp; River Trust</code> if you like.</p>
<p>Bear in mind that there are <a href="http://www.horseboating.org.uk/operators/">fewer than 10 horseboats still in operation in the UK</a>, so the towpath tail should not be wagging the footway <del>dog</del> horse.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '15, 17:53</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 May '15, 17:54</strong> </span></p>
</div>
</div>
<div id="comments-container-42814" class="comments-container">
<span id="42905"></span>
<div id="comment-42905" class="comment">
<div id="post-42905-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>see reply for tags I'll use based on this.</p>
</div>
<div id="comment-42905-info" class="comment-info">
<span class="comment-age">(05 May '15, 18:27)</span> <span class="comment-user userinfo">Govanus</span>
</div>
</div>
</div>
<div id="comment-tools-42814" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42814-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42904"></span>

<div id="answer-container-42904" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42904-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for your advice. I map in boating range of Hungerford which was on your list operators or horse boats join to that society, so I'll augment the routes accordingly. The waterways I'll be augmented are operated by the central goverment these days; though the Department of Transports's British Waterways and the other operated by the all encompasing Enviroment Agency under the jurisdiction of the Department for Environment, Food &amp; Rural Affairs. I'll also put a look out for these tags in my render and data solution.</p>
<p>So to summerise the waterway [routeing line - ie line in the middle of the water gets tagged with towpath = right / left / both and the paths used/madefor/useable for towing get a towpath=yes tag. The first helps routers find waterways served by towpaths eaily and the later help identify it for indication to someone trying to follow the towpath route.</p>
<p>Thank you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '15, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/30d90feb3a40fa6255767f95a8cd7943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Govanus&#39;s gravatar image" />
<p><span>Govanus</span><br />
<span class="score" title="154 reputation points">154</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Govanus has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-42904" class="comments-container">
<span id="42909"></span>
<div id="comment-42909" class="comment">
<div id="post-42909-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thnak you <a href="http://help.openstreetmap.org/users/3443/hendrikklaas">@Hendrikklaas</a> I did just manage to catchup with you entries stored in my inbox before they dissappeared from here. I think I was hopeing to make towpath the aquatic and highly focused version of sidewalk so we where thinking along similar lines but I did think later that for the big canals that towpath:type rail mght be needed ie the suez and panama ship cannals. These swap houses and people for pulling and replace them with special locomotives running on a dedicated parral railway. ;) so in a big picture context the boats do order who dose the wagging. I guess a a few centries of lcal decline can colour some peoples first impresions in the uk.</p>
<p>I think for now its missleading to some operators who used to be reluctant to let bike down them for the problems of erosion the bike make on simple worn out gravel and bare earth tracks that the paths had become some decades ago.</p>
</div>
<div id="comment-42909-info" class="comment-info">
<span class="comment-age">(05 May '15, 21:43)</span> <span class="comment-user userinfo">Govanus</span>
</div>
</div>
</div>
<div id="comment-tools-42904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42904-form-container" class="comment-form-container">
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

