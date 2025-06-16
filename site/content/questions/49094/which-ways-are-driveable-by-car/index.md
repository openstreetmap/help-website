+++
type = "question"
title = "Which ways are driveable by car"
description = '''I see a few highway types here: https://wiki.openstreetmap.org/wiki/Key:highway  Is there a table with the types that can be driven by car (or by foot, by bike, etc.), as well as the recommended speed for them ?'''
date = "2016-04-07T22:20:00Z"
lastmod = "2016-04-12T14:49:00Z"
weight = 49094
keywords = [ "export", "highway" ]
aliases = [ "/questions/49094" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Which ways are driveable by car](/questions/49094/which-ways-are-driveable-by-car)

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
<span id="post-49094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49094-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I see a few highway types here: <a href="https://wiki.openstreetmap.org/wiki/Key:highway">https://wiki.openstreetmap.org/wiki/Key:highway</a></p>
<p>Is there a table with the types that can be driven by car (or by foot, by bike, etc.), as well as the recommended speed for them ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Apr '16, 22:20</strong></p>
<img src="https://secure.gravatar.com/avatar/029b463e5af8b5dc5d6094a7a4686c6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shiro900&#39;s gravatar image" />
<p><span>shiro900</span><br />
<span class="score" title="54 reputation points">54</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shiro900 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Apr '16, 22:28</strong> </span></p>
</div>
</div>
<div id="comments-container-49094" class="comments-container">
&#10;</div>
<div id="comment-tools-49094" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49094-form-container" class="comment-form-container">
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

<span id="49100"></span>

<div id="answer-container-49100" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49100-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-49100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="shiro900 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The page you link makes a distinction between roads and paths. Roads are for vehicles, paths are not. Roads are largely open to pedestrians (but this varies by country and some classes of roads are usually closed to pedestrians). Special circumstances may be indicated by access tags:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Key:access">https://wiki.openstreetmap.org/wiki/Key:access</a></p>
<p>So there could be a path that is open to motor vehicles (maybe someone is allowed to use part of a bike trail as a driveway or whatever), and some roads may be closed to some classes of vehicles, or restricted as to who is allowed to use them. But these are exceptions that should be explicitly noted with the access tags, it is reasonable to make some assumptions that apply when specific access tags are not present.</p>
<p>One strategy for making sense of it is to look at the choices that others have made. Here are the various default profiles for OSRM (a routing engine):</p>
<p><a href="https://github.com/Project-OSRM/osrm-backend/tree/develop/profiles">https://github.com/Project-OSRM/osrm-backend/tree/develop/profiles</a></p>
<p>Each of <code>car.lua</code>, <code>foot.lua</code> and <code>bicycle.lua</code> has rules for how tags are interpreted by the routing engine for that use. I think the lua files are easier reading, but here are the rules used by OSMAND:</p>
<p><a href="https://github.com/osmandapp/OsmAnd-resources/blob/master/routing/routing.xml">https://github.com/osmandapp/OsmAnd-resources/blob/master/routing/routing.xml</a></p>
<p>There's surely more, those are quick to find.</p>
<p>The choices end up being fairly consistent, but can vary from country to country and different users of the data are free to make whatever choices they feel provide the best results, so there is some degree of subjectivity.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '16, 01:54</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Apr '16, 02:27</strong> </span></p>
</div>
</div>
<div id="comments-container-49100" class="comments-container">
&#10;</div>
<div id="comment-tools-49100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49100-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49102"></span>

<div id="answer-container-49102" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49102-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-49102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Additionally to the <a href="https://wiki.openstreetmap.org/wiki/Key:access">access key</a> already mentioned by maxerickson you will get a good idea by looking at the <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions">implicit default access values</a>. Remember that this is just a suggestion by OSM and some routers might decide to use slightly different default values.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '16, 07:58</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-49102" class="comments-container">
&#10;</div>
<div id="comment-tools-49102" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49102-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="49103"></span>

<div id="answer-container-49103" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49103-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49103-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49103-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What is your goals with getting the "roads which can be driven by a car"? Because you might also want to look at the <a href="https://wiki.openstreetmap.org/wiki/Key:surface"><code>surface</code> tag</a> which tells you the road surface. Sure, someone might be legally able to drive on a certain road, but if you're making a satnav device for tourists you might not want to send someone down an unpaved, gravel road.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '16, 09:06</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-49103" class="comments-container">
<span id="49104"></span>
<div id="comment-49104" class="comment">
<div id="post-49104-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What if there are only unpaved gravel roads available? :)</p>
</div>
<div id="comment-49104-info" class="comment-info">
<span class="comment-age">(08 Apr '16, 09:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="49105"></span>
<div id="comment-49105" class="comment">
<div id="post-49105-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It depends on the use case. :)</p>
</div>
<div id="comment-49105-info" class="comment-info">
<span class="comment-age">(08 Apr '16, 09:18)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="49196"></span>
<div id="comment-49196" class="comment">
<div id="post-49196-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yup, "a car" can be one of many vehicle types - for which gravel roads might be an expected mode of travel (4WD offroad), impassable (a Smart), or passable as a last resort, but not preferred (most cars in-between).</p>
</div>
<div id="comment-49196-info" class="comment-info">
<span class="comment-age">(12 Apr '16, 14:49)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
</div>
<div id="comment-tools-49103" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49103-form-container" class="comment-form-container">
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

