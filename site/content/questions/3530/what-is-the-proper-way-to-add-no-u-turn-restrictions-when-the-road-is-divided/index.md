+++
type = "question"
title = "What is the proper way to add &quot;No U Turn&quot; restrictions when the road is divided?"
description = '''Summary: In Potlatch 2, how to create a no-u-turn restriction with a &quot;via&quot; member that is a way (as opposed to a node)? This is necessary when the intersecting roads are divided and an intersection is represented by four nodes rather than one. UPDATE I have deleted most of my original post. I realiz...'''
date = "2011-03-04T20:06:00Z"
lastmod = "2020-12-22T08:27:00Z"
weight = 3530
keywords = [ "uturn", "turn_restrictions", "routing", "restrictions" ]
aliases = [ "/questions/3530" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What is the proper way to add "No U Turn" restrictions when the road is divided?](/questions/3530/what-is-the-proper-way-to-add-no-u-turn-restrictions-when-the-road-is-divided)

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
<span id="post-3530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3530-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-3530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Summary</strong>: In Potlatch 2, how to create a no-u-turn restriction with a "via" member that is a way (as opposed to a node)? This is necessary when the intersecting roads are divided and an intersection is represented by four nodes rather than one.</p>
<p><strong>UPDATE</strong></p>
<p>I have deleted most of my original post. I realize that my problem was not with the schema for turn restrictions, but with the way it is implemented in Potlatch 2. Due to the way Potlatch 2 "simple" mode allows one to easily create no-u-turn restrictions with a via node, it did not even occur to me that via could be a way.</p>
<p>So really my question now becomes: is there a "simple" way to create a no-u-turn restriction in Potlatch 2 where via member is a way?</p>
<p>Here is what I do now:<br />
1. Split ways inside the intersection as needed.<br />
2. Ctrl-click (Command-click on Mac) one side of the road, the short section of the cross road to the left of it and the reverse side of the road.<br />
3. Add all three to a new relationship.<br />
4. Set relationship to Advanced-&gt;Turn restriction.<br />
5. Set type to No U turns.<br />
6. Click Members and set roles: to, via and from (have to type).</p>
<p>Can this be simplified at all? Is this a wishlist for Potlatch?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-uturn" rel="tag" title="see questions tagged &#39;uturn&#39;">uturn</span> <span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-restrictions" rel="tag" title="see questions tagged &#39;restrictions&#39;">restrictions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Mar '11, 20:06</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Mar '11, 05:18</strong> </span></p>
</div>
</div>
<div id="comments-container-3530" class="comments-container">
<span id="78054"></span>
<div id="comment-78054" class="comment">
<div id="post-78054-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For anyone finding this years later and using the iD editor:</p>
<p><a href="https://web.archive.org/web/20201222082028if_/https://wsend.net/e8cfc9d4ccab9d5e3637889509d1e63b/add%20no%20uturn%20split%20ways%20id.mp4">Here</a> is a quick video I recorded showing how to do it</p>
</div>
<div id="comment-78054-info" class="comment-info">
<span class="comment-age">(22 Dec '20, 08:27)</span> <span class="comment-user userinfo">ray331</span>
</div>
</div>
</div>
<div id="comment-tools-3530" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3530-form-container" class="comment-form-container">
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

<span id="3568"></span>

<div id="answer-container-3568" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3568-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-3568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ponzu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><em>&gt; is there a "simple" way to create a no-u-turn restriction in Potlatch 2 where via member is a way?</em></p>
<p>Not as yet, no. The dedicated turn restriction editor currently only works where the via member is a node.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '11, 12:19</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span> </br></br></p>
</div>
</div>
<div id="comments-container-3568" class="comments-container">
<span id="3574"></span>
<div id="comment-3574" class="comment">
<div id="post-3574-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. Is there a Potlatch wishlist?</p>
</div>
<div id="comment-3574-info" class="comment-info">
<span class="comment-age">(05 Mar '11, 14:58)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3579"></span>
<div id="comment-3579" class="comment">
<div id="post-3579-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm getting the feeling you're mapping in greater detail than Potlatch was intended. You can use Potlatch to map a large area with rich detail, but it makes about as much sense as driving to Chicago from Tulsa on a bicycle. Likewise, you can use JOSM for a quick, single edit, but it makes about as much sense as driving a car to the corner store...</p>
</div>
<div id="comment-3579-info" class="comment-info">
<span class="comment-age">(05 Mar '11, 18:46)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="3580"></span>
<div id="comment-3580" class="comment">
<div id="post-3580-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting analogy. I have a feeling I have to get into JOSM, but I just wanted to point out that if Potlatch authors went to the trouble of implementing the wizard for creating no_U_turns with a "via" node, they might as well create one for when the "via" is a way. It could actually be even easier (to use) than the existing UI. Click three ways in order, click Transport-&gt;No U Turn. It could save a lot of clicks to the users.</p>
</div>
<div id="comment-3580-info" class="comment-info">
<span class="comment-age">(05 Mar '11, 21:34)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3581"></span>
<div id="comment-3581" class="comment">
<div id="post-3581-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Plus it was Richard who said "not yet" thus implying that it may be coming. I just wanted to know if needs my vote.</p>
</div>
<div id="comment-3581-info" class="comment-info">
<span class="comment-age">(05 Mar '11, 21:35)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3587"></span>
<div id="comment-3587" class="comment">
<div id="post-3587-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>ponzu - it will be coming, yes; you can add a trac ticket to request it as an enhancement if you like (that'll remind us to do it :) ).</p>
<p>Paul - disagree absolutely. There is nothing intrinsic to Potlatch that makes it unsuitable for large edits; similarly, there's nothing intrinsic to JOSM that makes it unsuitable for drive-by edits. I've done, and continue to do, lots of large edits in Potlatch. It's simply a matter of personal preference.</p>
</div>
<div id="comment-3587-info" class="comment-info">
<span class="comment-age">(06 Mar '11, 12:03)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="3594"></span>
<div id="comment-3594" class="comment not_top_scorer">
<div id="post-3594-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Except for the whole "potlatch is unbelievably slow with large datasets" and "potlatch tends to lose it's lunch before saving on large datasets"...</p>
</div>
<div id="comment-3594-info" class="comment-info">
<span class="comment-age">(06 Mar '11, 19:14)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-3568" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-3568-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3537"></span>

<div id="answer-container-3537" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3537-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3537-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3537-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have used a way as the "via" member in the relation successfully using mkgmap, so at least one renderer understands a three-way, no node U-turn. As far as splitting ways, only ways that are separated by a median (open or closed) should be seperated into two ways on the map (note that two-way left turn lanes and a single set of centerlines is not a median for purposes of mapping). For u-turns on a single way, using the same member entered into the relation twice for both the from and the to members, with a via node should work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Mar '11, 21:47</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '11, 21:48</strong> </span></p>
</div>
</div>
<div id="comments-container-3537" class="comments-container">
<span id="3542"></span>
<div id="comment-3542" class="comment">
<div id="post-3542-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I understand and I only split ways that are physically split with a median. Also, I am not doing it for my health, but to eliminate massive problems with phantom left turns across the divider. I also have no problem mapping "no u-turns" on a single way and would be extremely surprised and disappointed if a routing algorithm misinterpreted those. For your first point, I need to understand better what you mean. Can you share a link to wiki and/or map that has those?</p>
</div>
<div id="comment-3542-info" class="comment-info">
<span class="comment-age">(04 Mar '11, 22:10)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3543"></span>
<div id="comment-3543" class="comment">
<div id="post-3543-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Paul, is it your opinion that it is impossible to properly map a u-turn restriction using any of the configurations described in my question (for the reasons stated)?</p>
</div>
<div id="comment-3543-info" class="comment-info">
<span class="comment-age">(04 Mar '11, 22:13)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3544"></span>
<div id="comment-3544" class="comment">
<div id="post-3544-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Honestly, I didn't understand your description, so I answered as best I could with the information I did understand; if you have mapped any in the way you describe, relation ID numbers would be great. And you're right to split divided roadways with a median into two different ways. Two relations in the vicinity of Shadow Mountain in Tulsa are demonstrations of restrictions involving a way for a "via" member: <a href="http://ra.osmsurround.org/analyze.jsp?relationId=1341305">http://ra.osmsurround.org/analyze.jsp?relationId=1341305</a> and <a href="http://ra.osmsurround.org/analyze.jsp?relationId=1341304">http://ra.osmsurround.org/analyze.jsp?relationId=1341304</a></p>
</div>
<div id="comment-3544-info" class="comment-info">
<span class="comment-age">(04 Mar '11, 22:28)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="3545"></span>
<div id="comment-3545" class="comment">
<div id="post-3545-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Memorial Drive and 61st, immediately east of both relations and running for several miles both north and south is a good example on how to map a divided roadway. Memorial Drive has driveway stubs added, and this touch really helps when trying to navigate along it with a GPS device.</p>
</div>
<div id="comment-3545-info" class="comment-info">
<span class="comment-age">(04 Mar '11, 22:31)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="3557"></span>
<div id="comment-3557" class="comment">
<div id="post-3557-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I did not know I could use a way as the "via" member. I restated my original question.</p>
</div>
<div id="comment-3557-info" class="comment-info">
<span class="comment-age">(05 Mar '11, 09:37)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="3575"></span>
<div id="comment-3575" class="comment not_top_scorer">
<div id="post-3575-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A lot of tools seem to disagree with me on this (the turn restriction plugin in JOSM, for example, complains loudly about editing one of these), but in practice, it seems to work.</p>
</div>
<div id="comment-3575-info" class="comment-info">
<span class="comment-age">(05 Mar '11, 16:03)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-3537" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-3537-form-container" class="comment-form-container">
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

