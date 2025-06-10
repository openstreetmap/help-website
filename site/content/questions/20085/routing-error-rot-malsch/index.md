+++
type = "question"
title = "Routing error Rot-Malsch"
description = '''In http://openrouteservice.org/ I entered Pos@: 8.643856 49.239940 as start and Pos@: 8.638670 49.237443 as end. If I choose pedestrian the route goes over the bridge; if I choose bicylce it goes a long way around; the bridge is marked as cyclists dismount because it has a few steps. Please can you ...'''
date = "2013-02-21T07:41:00Z"
lastmod = "2013-02-21T13:47:00Z"
weight = 20085
keywords = [ "bridge", "wrong", "dismount", "route", "cyclists" ]
aliases = [ "/questions/20085" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Routing error Rot-Malsch](/questions/20085/routing-error-rot-malsch)

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
<span id="post-20085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20085-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In <a href="http://openrouteservice.org/">http://openrouteservice.org/</a> I entered Pos@: 8.643856 49.239940 as start and Pos@: 8.638670 49.237443 as end. If I choose pedestrian the route goes over the bridge; if I choose bicylce it goes a long way around; the bridge is marked as cyclists dismount because it has a few steps.</p>
<p>Please can you explain why it does not find the shortes path?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span> <span class="post-tag tag-link-wrong" rel="tag" title="see questions tagged &#39;wrong&#39;">wrong</span> <span class="post-tag tag-link-dismount" rel="tag" title="see questions tagged &#39;dismount&#39;">dismount</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-cyclists" rel="tag" title="see questions tagged &#39;cyclists&#39;">cyclists</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Feb '13, 07:41</strong></p>
<img src="https://secure.gravatar.com/avatar/5d46a41f532a7b3677b28b51f6634609?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ESSnavik&#39;s gravatar image" />
<p><span>ESSnavik</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ESSnavik has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20085" class="comments-container">
<span id="20090"></span>
<div id="comment-20090" class="comment">
<div id="post-20090-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I now tried <a href="http://maps.cloudmade.de/">http://maps.cloudmade.de/</a> and <a href="http://open.mapquest.de/">http://open.mapquest.de/</a> but they also don't work. Maybe they are not updated? Or is it an error in the data?</p>
</div>
<div id="comment-20090-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 08:50)</span> <span class="comment-user userinfo">ESSnavik</span>
</div>
</div>
<span id="20091"></span>
<div id="comment-20091" class="comment">
<div id="post-20091-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your end point isn't anywhere near a way, did you copy the wrong coordinates?</p>
</div>
<div id="comment-20091-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 08:53)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="20093"></span>
<div id="comment-20093" class="comment">
<div id="post-20093-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The endpoints should be directly near both sides of the bridge on the street and on the forest path (red dotted line).</p>
</div>
<div id="comment-20093-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 09:24)</span> <span class="comment-user userinfo">ESSnavik</span>
</div>
</div>
<span id="20095"></span>
<div id="comment-20095" class="comment">
<div id="post-20095-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I guess your endpoint should be somewhere around <em>Pos@: 8.643672 49.231793</em> and <a href="http://openrouteservice.org/index.php?start=8.643856,49.23994&amp;end=8.6436723,49.231793&amp;pref=Bicycle&amp;lang=en&amp;noMotorways=false&amp;noTollways=false">this</a> is the route you are trying. If not please specify a link (use the <em>Route Link</em> behind <em>Extras/Download</em>).</p>
<p>My guess is that either those routing services try to avoid steps at all for bicycles or don't understand bicycle=dismount and handle it as bicycle=no. Note that especially bicycle routing seems to be still very experimental for most routing services.</p>
</div>
<div id="comment-20095-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 09:30)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="20101"></span>
<div id="comment-20101" class="comment">
<div id="post-20101-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Right. The pedestrian path is right and I would expect the cycle path to be the same. <a href="http://openrouteservice.org/index.php?start=8.643856,49.23994&amp;end=8.6438384,49.2395029&amp;pref=Bicycle&amp;lang=en&amp;noMotorways=false&amp;noTollways=false">http://openrouteservice.org/index.php?start=8.643856,49.23994&amp;end=8.6438384,49.2395029&amp;pref=Bicycle&amp;lang=en&amp;noMotorways=false&amp;noTollways=false</a></p>
</div>
<div id="comment-20101-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 10:03)</span> <span class="comment-user userinfo">ESSnavik</span>
</div>
</div>
<span id="20102"></span>
<div id="comment-20102" class="comment not_top_scorer">
<div id="post-20102-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also tried naviki and it does not find the right path: (put 'Route von hier' at the A of 'Am Bahnhof' and the 'Route hierher' (right mouse) down on the dotted line; mark shortes route.)</p>
<p><a href="http://www.naviki.org/de/naviki/karten/?tx_naviki_pi_routing_request%5Baction%5D=show&amp;tx_naviki_pi_routing_request%5Bcontroller%5D=RoutingRequest&amp;tx_naviki_pi_routing_request%5Bdst%5D%5B0%5D=rot-malsch&amp;tx_naviki_pi_routing_request%5Bdst%5D%5B1%5D=rot-malsch&amp;tx_naviki_pi_routing_request%5Boption%5D=SHORTEST&amp;tx_naviki_pi_routing_request%5BavoidGradients%5D=0#lat=49.238569999999996&amp;lon=8.641479&amp;zoom=17">http://www.naviki.org/de/naviki/karten/?tx_naviki_pi_routing_request%5Baction%5D=show&amp;tx_naviki_pi_routing_request%5Bcontroller%5D=RoutingRequest&amp;tx_naviki_pi_routing_request[dst][0]=rot-malsch&amp;tx_naviki_pi_routing_request[dst][1]=rot-malsch&amp;tx_naviki_pi_routing_request[option]=SHORTEST&amp;tx_naviki_pi_routing_request[avoidGradients]=0#lat=49.238569999999996&amp;lon=8.641479&amp;zoom=17</a></p>
</div>
<div id="comment-20102-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 10:03)</span> <span class="comment-user userinfo">ESSnavik</span>
</div>
</div>
</div>
<div id="comment-tools-20085" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-20085-form-container" class="comment-form-container">
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

<span id="20107"></span>

<div id="answer-container-20107" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20107-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ESSnavik has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Then I guess all those routing engines handle bicycle=dismount the same way as bicycle=no and try to avoid the bridge. This is a problem if those routers, you shouldn't change the tag because it is correct.</p>
<p>By the way I saw you added a name tag to the <a href="http://www.openstreetmap.org/browse/way/24581166">bridge</a>. This tag is only for the <a href="https://wiki.openstreetmap.org/wiki/Names#Name_is_the_name_only"><em>official</em> name</a> of the object and not for a description. Use the <a href="https://wiki.openstreetmap.org/wiki/Key:description">description</a> or <a href="https://wiki.openstreetmap.org/wiki/Key:note">note</a> tag instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '13, 11:57</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Feb '13, 12:47</strong> </span></p>
</div>
</div>
<div id="comments-container-20107" class="comments-container">
<span id="20109"></span>
<div id="comment-20109" class="comment">
<div id="post-20109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the great answer. I removed the name and created it as description (under advanced settings, since I didn't find a field).</p>
<p>Maybe I write to the router engines, if they want to check their settings.</p>
<p>I think you have to put your comment as answer, that I can close it?</p>
</div>
<div id="comment-20109-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 12:16)</span> <span class="comment-user userinfo">ESSnavik</span>
</div>
</div>
<span id="20110"></span>
<div id="comment-20110" class="comment">
<div id="post-20110-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I requested a change at naviki, cloudemade and open route service.</p>
</div>
<div id="comment-20110-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 13:21)</span> <span class="comment-user userinfo">ESSnavik</span>
</div>
</div>
<span id="20111"></span>
<div id="comment-20111" class="comment">
<div id="post-20111-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Great! Let's hope they get improved.</p>
</div>
<div id="comment-20111-info" class="comment-info">
<span class="comment-age">(21 Feb '13, 13:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-20107" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20107-form-container" class="comment-form-container">
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

