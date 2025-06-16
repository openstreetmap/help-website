+++
type = "question"
title = "Bus route passes twice through a way. Is it correct to add it twice to the relation?"
description = '''I am mapping several bus routes in São Paulo, Brazil, and while adding one specific route, I found that the bus passes twice in the same direction through a way, when going from one end point to the other. So, the question is: Is it correct to add this way twice to the same relation as I did? Is the...'''
date = "2013-09-09T01:11:00Z"
lastmod = "2015-02-08T10:09:00Z"
weight = 26213
keywords = [ "bus", "route", "relation", "josm" ]
aliases = [ "/questions/26213" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Bus route passes twice through a way. Is it correct to add it twice to the relation?](/questions/26213/bus-route-passes-twice-through-a-way-is-it-correct-to-add-it-twice-to-the-relation)

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
<span id="post-26213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26213-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-26213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am mapping several bus routes in São Paulo, Brazil, and while adding one specific route, I found that the bus passes <strong>twice in the same direction</strong> through a way, when going from one end point to the other.</p>
<p>So, the question is: Is it correct to add this way twice to the same relation as I did?</p>
<p>Is there some alternative form of doing this without adding the way twice to the relation in the same direction? JOSM allows it, but warns me and shows the way in a red background (and that usually means something wrong...)</p>
<p>The way in question is # 237169404 (<a href="https://www.openstreetmap.org/browse/way/237169404">OSM</a>), and the relation is # 3191062 (<a href="https://www.openstreetmap.org/browse/relation/3191062">OSM</a>)</p>
<p>Thanks.</p>
<p>Edit: Added the return route # 3193918 (<a href="https://www.openstreetmap.org/browse/relation/3193918">OSM</a>) and the route_master relation # 3193919 (<a href="https://www.openstreetmap.org/browse/relation/3193919">OSM</a>)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Sep '13, 01:11</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Sep '13, 17:59</strong> </span></p>
</div>
</div>
<div id="comments-container-26213" class="comments-container">
&#10;</div>
<div id="comment-tools-26213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26213-form-container" class="comment-form-container">
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

<span id="26223"></span>

<div id="answer-container-26223" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26223-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-26223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MCPicoli has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, as far as I know, adding the way twice in the relation is the correct thing to do. Otherwise, you'll end up with a gap in the bus route, which is semantically incorrect. Remember to order the ways correctly; JOSM displays wether ways are connected to each other or not.</p>
<p>The annoying thing is that JOSM's validator will warn you about the duplicated way, but this particular warning can be ignored. JOSM's validator is great, but not free of false positives. If you can, consider helping the JOSM devs to fix this particular false-positive.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '13, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-26223" class="comments-container">
&#10;</div>
<div id="comment-tools-26223" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26223-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26228"></span>

<div id="answer-container-26228" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26228-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It isn't wrong to add the way/role twice to the relation, but at one time in the past the relation wouldn't be preserved by other editors (it might be OK now). One solution is to create another relation for that loop, and have an overall route_master relation to identify all relations making up that route.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Sep '13, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-26228" class="comments-container">
<span id="26233"></span>
<div id="comment-26233" class="comment">
<div id="post-26233-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How would you tag the route_master relation regarding the loop and the main "course" of the bus route? I already added the route_master for this bus line (# 3193919 <a href="https://www.openstreetmap.org/browse/relation/3193919">OSM</a>). Thankfully no loops on the return route...</p>
</div>
<div id="comment-26233-info" class="comment-info">
<span class="comment-age">(09 Sep '13, 17:57)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
<span id="26253"></span>
<div id="comment-26253" class="comment">
<div id="post-26253-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Right now, there is no special convention to add the relation members to the master route. Ideally, software should be able to determine the actual vehicle travel path by connecting the end of one route to the beginning of another route.</p>
<p>For this example, I would also add Rua Robério Dias to both routes, indicating that the bus turns around on that street, or add the driveways to the relation to complete the turnaround path.</p>
</div>
<div id="comment-26253-info" class="comment-info">
<span class="comment-age">(10 Sep '13, 14:20)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
</div>
<div id="comment-tools-26228" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26228-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27207"></span>

<div id="answer-container-27207" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27207-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So, just so I'm sure, I'm going to use Metrobus route 400 (UK), which runs between Caterham-on-the-Hill, and East Grinstead, as an example...</p>
<p>From Caterham-on-the-Hill, it basically, makes its way from Caterham-on-the-Hill, down towards the Caterham town centre, towards Godstone, Bletchingley, Nutfield and then Redhill. For this part of the route, it's straight forward. There are no parts where it goes through twice along the same route. However, my first question is at Redhill. When it enters "The Stations Roundabout" from the east, it travels around the roundabout and exits at the north (Princess Way), and then enters the Bus Station. It then exits the bus station, and enters the roundabout again, from the north, and travels to the south exit. At this point, the part of the roundabout between the east and south would have been traveled on twice. Therefore, would this particular section of the roundabout be split to add a second relation for this route, to avoid a gap?</p>
<p>After it leaves Redhill, it travels south on the A23 towards East Surrey Hospital. At this point, it travels long Three Arch Road, to the roundabout, entering East Surrey Hospital, where it exits again, travelling the other direction on Three Arch Road, back to the A23. Should this be done like this? Assuming Three Arch Road is eastward: A relation on Three Arch Road facing forwards (&gt;&gt;), followed by a relation for the part of East Surrey Hospital where the bus route is, and where it enters Three Arch Road, have a second relation but 'backwards'? (&lt;&lt;)?</p>
<p>For example, let's say it's relation 400... would it be something like this?</p>
<p>Three Arch Road has relation 400, ID 1 facing forwards Part of East Surrey Hospital has relation 400, ID 2 Three Arch Road has relation 400, ID 3 facing backwards?</p>
<p>Trying to explain is more complicated than how it actually is.</p>
<p>And to make things more confusing, after eventually reaching East Grinstead, and then making its way back towards Caterham-on-the-Hill, it enters the hospital again, therefore, on its full route, it'll travel along Three Arch Road east, enter the hospital, exit the hospital, travel west along Three Arch Road, travel south, then continue its route, then eventually, return from the south (travelling north), enter Three Arch Road, travel east, enter the hospital again, exit the hospital, travel west, along Three Arch Road, and then travel north. Essentially, travelling along Three Arch Road twice, in both directions, a total of four times...</p>
<p>And a more general question about routes... for routes where the bus travels from one place to another, before turning around (usually by making a small loop around an area), and then travel along the same route, in the opposite direction, should we have two relations for each way that it travels along in both directions, one being forwards and one being backwards?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '13, 21:03</strong></p>
<img src="https://secure.gravatar.com/avatar/6035647123b433de9d9aaa4259d07e8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheUltimateKoopa&#39;s gravatar image" />
<p><span>TheUltimateK...</span><br />
<span class="score" title="161 reputation points">161</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheUltimateKoopa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27207" class="comments-container">
<span id="27273"></span>
<div id="comment-27273" class="comment">
<div id="post-27273-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Use two relations, one for each direction, and one for each possible variant. Do not forget to group them all under a route_master relation!</p>
</div>
<div id="comment-27273-info" class="comment-info">
<span class="comment-age">(17 Oct '13, 19:57)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
<span id="27274"></span>
<div id="comment-27274" class="comment">
<div id="post-27274-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I usually split the roudabout in parts following the bus route, but the routers may be able to use them without splitting. Note that at least in JOSM, when a roundabout is added to a route, it appears with a special symbol.</p>
</div>
<div id="comment-27274-info" class="comment-info">
<span class="comment-age">(17 Oct '13, 19:59)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
<span id="27292"></span>
<div id="comment-27292" class="comment">
<div id="post-27292-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, so two further questions. Can you 'split' relations? For example, say a route was created with a single relation in both directions. Is there a way of splitting it at a certain point, so that all members of the relation after that point are in a new relation? I.e. can you split it at say the 115th member of a relation, so that the 116th member and so on, are then the 1st member (etc) of a new relation?</p>
<p>Secondly, as in the other question, how exactly do you use the route_master relation? When you've created the route_master relation, what do you actually add to the relation?</p>
</div>
<div id="comment-27292-info" class="comment-info">
<span class="comment-age">(18 Oct '13, 02:32)</span> <span class="comment-user userinfo">TheUltimateK...</span>
</div>
</div>
<span id="27295"></span>
<div id="comment-27295" class="comment">
<div id="post-27295-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please don't post your questions here but instead start new separate questions. This Q&amp;A system is not suited for such discussions.</p>
</div>
<div id="comment-27295-info" class="comment-info">
<span class="comment-age">(18 Oct '13, 07:45)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="40853"></span>
<div id="comment-40853" class="comment">
<div id="post-40853-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can mark the ways in the relation editor in blue, then press a button in the middle of the relation editor to have them selected in JOSM's editor window. Now go to the relation editor window of the relation you want to add it to and use one of the middle buttons to add all those ways to this route relation.</p>
</div>
<div id="comment-40853-info" class="comment-info">
<span class="comment-age">(08 Feb '15, 10:09)</span> <span class="comment-user userinfo">Polyglot</span>
</div>
</div>
</div>
<div id="comment-tools-27207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27207-form-container" class="comment-form-container">
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

