+++
type = "question"
title = "Help with 3D building."
description = '''Hi, I&#x27;m currently trying to add a simple 3D building called &#x27;De La Warr Pavilion&#x27; here - https://www.openstreetmap.org/#map=19/50.83745/0.47171 But it appears, at least on F4Map the ground floor is missing under the other building parts - http://demo.f4map.com/#lat=50.8374459&amp;amp;lon=0.4714628&amp;amp;zo...'''
date = "2016-02-11T20:08:00Z"
lastmod = "2016-02-13T12:09:00Z"
weight = 48063
keywords = [ "building", "3d" ]
aliases = [ "/questions/48063" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Help with 3D building.](/questions/48063/help-with-3d-building)

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
<span id="post-48063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48063-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm currently trying to add a simple 3D building called 'De La Warr Pavilion' here - <a href="https://www.openstreetmap.org/#map=19/50.83745/0.47171">https://www.openstreetmap.org/#map=19/50.83745/0.47171</a></p>
<p>But it appears, at least on F4Map the ground floor is missing under the other building parts - <a href="http://demo.f4map.com/#lat=50.8374459&amp;lon=0.4714628&amp;zoom=20&amp;camera.theta=39.893&amp;camera.phi=-5.73">http://demo.f4map.com/#lat=50.8374459&amp;lon=0.4714628&amp;zoom=20&amp;camera.theta=39.893&amp;camera.phi=-5.73</a></p>
<p>Am I doing something wrong, or is this a known bug? Thanks in advance.</p>
<p>Alex</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-3d" rel="tag" title="see questions tagged &#39;3d&#39;">3d</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Feb '16, 20:08</strong></p>
<img src="https://secure.gravatar.com/avatar/b60dfdd58818dd0080134dcecdf7756b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dr-Mx&#39;s gravatar image" />
<p><span>Dr-Mx</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dr-Mx has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48063" class="comments-container">
&#10;</div>
<div id="comment-tools-48063" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48063-form-container" class="comment-form-container">
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

<span id="48080"></span>

<div id="answer-container-48080" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48080-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Dr-Mx has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://osm2world.org/">OSM2World</a> also doesn't draw the ground floor (tried with a local copy of the latest build). So I guess it's a tagging problem although I'm not sure why. It seems to be caused somehow by the other outlines having a "building:min_level" set.</p>
<p>The <a href="https://wiki.openstreetmap.org/wiki/Simple_3D_buildings">simple 3D buildings</a> wiki page contains an interesting sentence that could be relevant here:</p>
<blockquote>
<p>Note that if a building=* contains at least one area tagged as building:part=*, the building outline is no longer considered for volume rendering.</p>
</blockquote>
<p>So it might be necessary to draw another outline with building:part=yes and building:levels=1 which overlaps with the parts having a "building:min_level" set. This seems to render correctly with at least OSM2World. The new way looks in JOSM like this:</p>
<p><img src="/upfiles/foo_osF0OM6.png" alt="alt text" /></p>
<p>However since I'm neither convinced that this is the correct solution (isn't there an easier one?) nor do I know whether the building really does look the way I "fixed" it I won't upload it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '16, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '16, 16:51</strong> </span></p>
</div>
</div>
<div id="comments-container-48080" class="comments-container">
<span id="48084"></span>
<div id="comment-48084" class="comment">
<div id="post-48084-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm, interesting. With that thinking I'll remove all the "building:min_level" tags and reset the "building:levels". This seems to render it correctly, albeit the buildings parts are all inside one another. Thanks you for your help.</p>
</div>
<div id="comment-48084-info" class="comment-info">
<span class="comment-age">(12 Feb '16, 20:39)</span> <span class="comment-user userinfo">Dr-Mx</span>
</div>
</div>
<span id="48085"></span>
<div id="comment-48085" class="comment">
<div id="post-48085-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not sure if that's the correct approach either. Making the building parts stuck in each other although they don't in reality sounds wrong. But I'm not very experienced in 3D tagging.</p>
</div>
<div id="comment-48085-info" class="comment-info">
<span class="comment-age">(12 Feb '16, 20:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="48087"></span>
<div id="comment-48087" class="comment">
<div id="post-48087-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, it's not the cleanest approach. I haven't made any permanent changes yet, so I'll try a bit more experimentation given your advice.</p>
</div>
<div id="comment-48087-info" class="comment-info">
<span class="comment-age">(12 Feb '16, 23:42)</span> <span class="comment-user userinfo">Dr-Mx</span>
</div>
</div>
<span id="48098"></span>
<div id="comment-48098" class="comment">
<div id="post-48098-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As you say the building=yes isn't rendered if there is a building:part=yes above it, so I just lowered level 2 to ground level. That was all I needed to do. Cheers.</p>
</div>
<div id="comment-48098-info" class="comment-info">
<span class="comment-age">(13 Feb '16, 12:09)</span> <span class="comment-user userinfo">Dr-Mx</span>
</div>
</div>
</div>
<div id="comment-tools-48080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48080-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48067"></span>

<div id="answer-container-48067" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48067-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Alex, not a direct an answer but did you studied these pages ? <a href="https://wiki.openstreetmap.org/wiki/3D_tagging">https://wiki.openstreetmap.org/wiki/3D_tagging</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Feb '16, 23:35</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-48067" class="comments-container">
<span id="48076"></span>
<div id="comment-48076" class="comment">
<div id="post-48076-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... or ask in the OSM 3D subforum.</p>
<p><a href="http://forum.openstreetmap.org/viewforum.php?id=42">http://forum.openstreetmap.org/viewforum.php?id=42</a></p>
<p>Normaly the developers of f4map are active there, too.</p>
</div>
<div id="comment-48076-info" class="comment-info">
<span class="comment-age">(12 Feb '16, 15:04)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="48077"></span>
<div id="comment-48077" class="comment">
<div id="post-48077-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It appears "This forum is not accepting new registrations." But I'll keep checking back, thanks.</p>
</div>
<div id="comment-48077-info" class="comment-info">
<span class="comment-age">(12 Feb '16, 15:43)</span> <span class="comment-user userinfo">Dr-Mx</span>
</div>
</div>
<span id="48079"></span>
<div id="comment-48079" class="comment">
<div id="post-48079-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Just login to the forum with your regular OSM account.</p>
</div>
<div id="comment-48079-info" class="comment-info">
<span class="comment-age">(12 Feb '16, 16:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48067" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48067-form-container" class="comment-form-container">
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

