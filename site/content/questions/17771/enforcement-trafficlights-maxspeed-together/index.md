+++
type = "question"
title = "Enforcement, trafficlights &amp; maxspeed together"
description = '''I’m struggling with the tag enforcement with 2 utilities, maxspeed and traffic lights. As soon as I added one and safe it, the otherone disappears. The red light camera reacts at &amp;gt; speed levels too. The taglist shows some but I misted this specific one.'''
date = "2012-11-18T22:48:00Z"
lastmod = "2012-11-20T20:08:00Z"
weight = 17771
keywords = [ "enforcement", "maxspeed", "traffic_lights", "taglist" ]
aliases = [ "/questions/17771" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Enforcement, trafficlights & maxspeed together](/questions/17771/enforcement-trafficlights-maxspeed-together)

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
<span id="post-17771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17771-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I’m struggling with the tag enforcement with 2 utilities, maxspeed and traffic lights. As soon as I added one and safe it, the otherone disappears. The red light camera reacts at &gt; speed levels too. The taglist shows some but I misted this specific one.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-enforcement" rel="tag" title="see questions tagged &#39;enforcement&#39;">enforcement</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-traffic_lights" rel="tag" title="see questions tagged &#39;traffic_lights&#39;">traffic_lights</span> <span class="post-tag tag-link-taglist" rel="tag" title="see questions tagged &#39;taglist&#39;">taglist</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Nov '12, 22:48</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-17771" class="comments-container">
&#10;</div>
<div id="comment-tools-17771" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17771-form-container" class="comment-form-container">
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

<span id="17779"></span>

<div id="answer-container-17779" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17779-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hendrikklaas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You cannot have a <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dspeed_camera">highway=speed_camera</a> and <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dtraffic_signals">highway=traffic_signals</a> on the same <a href="https://wiki.openstreetmap.org/wiki/Elements">element</a> because they obviously share the same <em>key</em>. Create a separate element for each.</p>
<p>Another common approach is to use a <a href="https://wiki.openstreetmap.org/wiki/Semi-colon_value_separator">semicolon</a> to separate multiple values for the same key. But don't expect all tools to handle this correctly.</p>
<p>I don't understand your maxspeed problem though.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '12, 06:17</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Nov '12, 18:13</strong> </span></p>
</div>
</div>
<div id="comments-container-17779" class="comments-container">
<span id="17798"></span>
<div id="comment-17798" class="comment">
<div id="post-17798-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks, but its only one pole with surprisingly a double function. Just add a extra node on top of the other one ? Greetz</p>
</div>
<div id="comment-17798-info" class="comment-info">
<span class="comment-age">(19 Nov '12, 11:11)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="17807"></span>
<div id="comment-17807" class="comment">
<div id="post-17807-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Although having two nodes on the exact same location is usually discouraged it seems to be a valid solution here.</p>
</div>
<div id="comment-17807-info" class="comment-info">
<span class="comment-age">(19 Nov '12, 14:15)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="17809"></span>
<div id="comment-17809" class="comment">
<div id="post-17809-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, would this format do without any complaints ? Enforcement - traffic_signals / maxspeed, I'd already added it here ; <a href="https://www.openstreetmap.org/edit?lat=52.3295&amp;lon=6.6467&amp;zoom=17">https://www.openstreetmap.org/edit?lat=52.3295&amp;lon=6.6467&amp;zoom=17</a> Greetz</p>
</div>
<div id="comment-17809-info" class="comment-info">
<span class="comment-age">(19 Nov '12, 17:45)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="17810"></span>
<div id="comment-17810" class="comment">
<div id="post-17810-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No <a href="https://www.openstreetmap.org/browse/node/2020443461">it</a> won't. Why are you asking if you are ignoring the answer anyway?</p>
</div>
<div id="comment-17810-info" class="comment-info">
<span class="comment-age">(19 Nov '12, 18:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="17813"></span>
<div id="comment-17813" class="comment">
<div id="post-17813-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Scai, Im just asked because this is one of the platforms I know, to talk together to make OSM better and usable. Isnt that whats all about ? Making a Worldwide and usable map together and trying to improve the system daily to be used by everyone ? If its a mistake please tell me. Greetz</p>
</div>
<div id="comment-17813-info" class="comment-info">
<span class="comment-age">(19 Nov '12, 21:16)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="17819"></span>
<div id="comment-17819" class="comment not_top_scorer">
<div id="post-17819-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Of course Hendrik, that's why I told you how this specific problem is usually solved by the majority of the community.</p>
</div>
<div id="comment-17819-info" class="comment-info">
<span class="comment-age">(20 Nov '12, 06:16)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17779" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-17779-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17824"></span>

<div id="answer-container-17824" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17824-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17824-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17824-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The maxspeed tag applies to a way rather than a node, so it does not conflict with the other two tags mentioned. Traffic signals and enforcement cameras each exist at a point, and so must belong to a node. The OSM community has decided that both should use the 'highway' key, and scai has explained that an element may not have two tags with the same key, so the traffic signals and the camera must be tagged on different nodes. If they happen to be at exactly the same place, at least when recorded in only two dimensions (e.g. if they are mounted on the same pole), that must be a justification for having two nodes in exactly the same place. Two nodes at the same position on the map give the most accurate representation of what exists on the ground.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Nov '12, 18:09</strong></p>
<img src="https://secure.gravatar.com/avatar/c81fd17cde8b2747629b78bdef81a202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madryn&#39;s gravatar image" />
<p><span>Madryn</span><br />
<span class="score" title="2241 reputation points"><span>2.2k</span></span><span title="36 badges"><span class="badge1">●</span><span class="badgecount">36</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madryn has 5 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-17824" class="comments-container">
<span id="17825"></span>
<div id="comment-17825" class="comment">
<div id="post-17825-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, done <a href="https://www.openstreetmap.org/edit?lat=52.36018&amp;lon=6.54994&amp;zoom=16,">https://www.openstreetmap.org/edit?lat=52.36018&amp;lon=6.54994&amp;zoom=16,</a> even the shadow is recognisable !</p>
</div>
<div id="comment-17825-info" class="comment-info">
<span class="comment-age">(20 Nov '12, 20:08)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-17824" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17824-form-container" class="comment-form-container">
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

