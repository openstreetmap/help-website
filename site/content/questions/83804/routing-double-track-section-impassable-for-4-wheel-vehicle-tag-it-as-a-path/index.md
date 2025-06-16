+++
type = "question"
title = "routing: double track section impassable for 4-wheel vehicle: tag it as a path?"
description = '''Is it better for routing to tag a section of double track impassable for 4WD (smoothness=very_horrible/impassable) as highway=path?'''
date = "2022-03-11T09:56:00Z"
lastmod = "2022-03-21T06:48:00Z"
weight = 83804
keywords = [ "track", "routing", "path", "smoothness", "impassable" ]
aliases = [ "/questions/83804" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [routing: double track section impassable for 4-wheel vehicle: tag it as a path?](/questions/83804/routing-double-track-section-impassable-for-4-wheel-vehicle-tag-it-as-a-path)

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
<span id="post-83804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83804-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it better for routing to tag a section of double track impassable for 4WD (smoothness=very_horrible/impassable) as highway=path?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-smoothness" rel="tag" title="see questions tagged &#39;smoothness&#39;">smoothness</span> <span class="post-tag tag-link-impassable" rel="tag" title="see questions tagged &#39;impassable&#39;">impassable</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Mar '22, 09:56</strong></p>
<img src="https://secure.gravatar.com/avatar/e3f994b2488e2182c63a7c44a5028ff6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmoffroad&#39;s gravatar image" />
<p><span>cmoffroad</span><br />
<span class="score" title="205 reputation points">205</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmoffroad has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83804" class="comments-container">
<span id="83836"></span>
<div id="comment-83836" class="comment">
<div id="post-83836-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just for the record, this seems closely related to your <a href="/questions/83777/can-smoothness-be-used-for-highwaypath">previous question</a>.</p>
</div>
<div id="comment-83836-info" class="comment-info">
<span class="comment-age">(13 Mar '22, 16:35)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-83804" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83804-form-container" class="comment-form-container">
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

<span id="83837"></span>

<div id="answer-container-83837" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83837-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi.</p>
<p>I'd say no. If the track is wide enough, then it's a <code>highway=track</code>. You could imagine some heavy-duty machinery, and farmer tractors, going through it, which should not be possible on a <code>highway=path</code> IMHO.</p>
<p>It would also be confusing for people on the ground, trying to understand why something mapped as a little path is a double track on the ground.</p>
<p>Eventually some mappers following conventions might retag it.</p>
<p>To answer your concern about routing, following your previous questions, I'm thinking that maybe a not too bad compromise, would be to tag the way as <code>motor_vehicle=no</code> with a <code>note=</code> saying that while it's legally allowed to drive, it's technically impossible to do so.</p>
<p>The <code>note=</code> tag is meant for other mappers who might not understand the tagging. If it's the same wording each time, it might also be used to mechanically remove all the "wrong" tags once smoothness support in routers is ok.</p>
<p>I know some people will cringe at this "tagging for the router", but I think it's better to bend the <code>access</code> tags, than the physical or structural ones.</p>
<p>FYI, I think that most of your recent questions here might be more relevant on the <a href="https://wiki.openstreetmap.org/wiki/Tagging_mailing_list">Tagging mailing-list</a>. I'm not following it for years, some you might already have tried, but it's supposed to be the place to discuss new tagging conventions.</p>
<p>Hope this helps.</p>
<p>Best regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '22, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-83837" class="comments-container">
<span id="83856"></span>
<div id="comment-83856" class="comment">
<div id="post-83856-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Doesn't motor_vehicle=no also imply no specialized vehicles (ATV, motorcycles)? If that's the case, such a tag would work for smoothness=impassable but not for smoothness=very_horrible</p>
</div>
<div id="comment-83856-info" class="comment-info">
<span class="comment-age">(15 Mar '22, 04:38)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
<span id="83858"></span>
<div id="comment-83858" class="comment">
<div id="post-83858-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm one of those cringing. :-)</p>
<p>I don't recommend using <code>access</code> and its variations here. In my opinion <code>access</code> tags should be reserved for legal access restrictions and where barriers physically block the access.</p>
<p>What are the practical implications? From my experience routers for cars regularly abstain from routing over tracks anyway unless they are positively mapped as driving friendly. Routers for bicycles evaluate also smoothness and surface tags (at least those specifically designed for bicycle routing).</p>
<p>I'd expect a router targeted at off-road drivers to also take into account surface and smoothness. If not it's their fault and we should not encourage them to not adopt good routing practices.</p>
<p>What I want to say is that the routing technology to make a good choice based on non-access tags is already out there. We don't need to wait until "smoothness support in routers is ok".</p>
</div>
<div id="comment-83858-info" class="comment-info">
<span class="comment-age">(15 Mar '22, 07:23)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="83859"></span>
<div id="comment-83859" class="comment">
<div id="post-83859-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"I'd expect a router targeted at off-road drivers to also take into account surface and smoothness" &gt; my thought too.</p>
<p>I also want to avoid using these access tags, and focus on smoothness/surface tags but rendering support for these is inexistent.</p>
</div>
<div id="comment-83859-info" class="comment-info">
<span class="comment-age">(15 Mar '22, 09:43)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
<span id="83868"></span>
<div id="comment-83868" class="comment not_top_scorer">
<div id="post-83868-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10133/tzorn">@TZorn</a> I totally understand your concern, I'm myself quite uneasy about my own proposal. But I'm pretty sure the major routers don't take smoothness into account. OsmAnd and OrganicMaps do propose an option to use unpaved roads, which seems to be useful in Thailand. I'll test soon if <code>smoothness=impassable</code> blocks the routing, but I guess not at this point. I was only proposing this as a temporary measure, and a way to tell the developers how much it would be useful to support <code>smoothness</code>...</p>
</div>
<div id="comment-83868-info" class="comment-info">
<span class="comment-age">(15 Mar '22, 18:53)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="83869"></span>
<div id="comment-83869" class="comment">
<div id="post-83869-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/20238/cmoffroad">@cmoffroad</a> OsmAnd does render it (if you enable the right options, or if you dig in the details of the planned route). That's a start, but I'm aware it is not enough.</p>
</div>
<div id="comment-83869-info" class="comment-info">
<span class="comment-age">(15 Mar '22, 18:56)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="83870"></span>
<div id="comment-83870" class="comment not_top_scorer">
<div id="post-83870-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Most bike router will avoid tracks anyway.</p>
<p>As an example, the brouter trekking profile says this about smoothness :</p>
<pre><code># include `smoothness=` tags in the response&#39;s WayTags for track analysis
assign dummyUsage = smoothness=</code></pre>
<p>On the other hand, it does use <code>tracktype</code>, but only to put a higher cost, there is no value that will block the road. Funnily there are a <a href="https://taginfo.openstreetmap.org/keys/tracktype#values">few instances of grade7</a> in the world, mostly in Australia. But it's not documented, so kind of useless.</p>
</div>
<div id="comment-83870-info" class="comment-info">
<span class="comment-age">(15 Mar '22, 19:20)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="83905"></span>
<div id="comment-83905" class="comment">
<div id="post-83905-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/13231/h_mlet"></a><a href="https://help.openstreetmap.org/users/13231/h_mlet">@H_mlet</a> said "motor_vehicle=no with a note= saying that while it's legally allowed to drive, it's technically impossible to do so.". "motor_vehicle=no is /the/ tag to define legality. There are various tags, such as surface &amp; smoothness, to quantify <em>ability</em> to use a highway. I'm cringing - You're conflating two different tags with two separate purposes.</p>
</div>
<div id="comment-83905-info" class="comment-info">
<span class="comment-age">(17 Mar '22, 18:20)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="83906"></span>
<div id="comment-83906" class="comment not_top_scorer">
<div id="post-83906-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/20238/cmoffroad">@cmoffroad</a> Similar to H_met you're conflating tags with two different purposes &amp; in doing so you're tagging incorrectly for the renderer. 'Access' defines legal permissions to use a highway. The separate 'surface' &amp; 'smoothness' etc help aid a highway user's decision whether they're physically able to use the highway. Based on the users ability, this is so subjective - You may not want to push a pram along it, but be happy in an ATV.</p>
</div>
<div id="comment-83906-info" class="comment-info">
<span class="comment-age">(17 Mar '22, 18:32)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="83908"></span>
<div id="comment-83908" class="comment not_top_scorer">
<div id="post-83908-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/1532/davef">@DaveF</a> Well I did say it was bending the meaning of the ̀<code>access</code> tag. The point here was that <code>smoothness</code> has literally no support for now. From the previous conversations, it seems that cmoffroad is concerned about mapping tracks correctly and have people following their router blindingly into trouble. I have no knowledge of Thailand, but I thought I could propose a temporary compromise...</p>
<p>The alternative is to say to people in Thailand (and other places I'm sure) don't use OSM with the current tools.</p>
</div>
<div id="comment-83908-info" class="comment-info">
<span class="comment-age">(17 Mar '22, 20:02)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-83837" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-83837-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83904"></span>

<div id="answer-container-83904" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83904-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If "double tracked" that's evidence it is passable. Also depends on the size of the multi drive axle vehicle.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '22, 18:14</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83904" class="comments-container">
<span id="83939"></span>
<div id="comment-83939" class="comment">
<div id="post-83939-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not all tracks are double tracks and those or even graded ones can become impassable to 4-wheel vehicles. Recommended supported tags in the wiki include smoothness=very_horrible or impassable.</p>
</div>
<div id="comment-83939-info" class="comment-info">
<span class="comment-age">(21 Mar '22, 06:48)</span> <span class="comment-user userinfo">cmoffroad</span>
</div>
</div>
</div>
<div id="comment-tools-83904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83904-form-container" class="comment-form-container">
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

