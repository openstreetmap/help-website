+++
type = "question"
title = "Mapping an unmarked bus stop, i.e. no post, sign or other physical indicator"
description = '''How do I map a bus stop that is not marked in any way? I am mapping a bus stop that does not have a post, a sign or any other physical indicator - however, in all other ways it is a regular bus stop: buses do stop there regularly, the bus stop appears on official timetables, and the bus stop on the ...'''
date = "2019-08-21T11:39:00Z"
lastmod = "2019-10-17T12:53:00Z"
weight = 70448
keywords = [ "bus", "public-transport", "tagging" ]
aliases = [ "/questions/70448" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping an unmarked bus stop, i.e. no post, sign or other physical indicator](/questions/70448/mapping-an-unmarked-bus-stop-ie-no-post-sign-or-other-physical-indicator)

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
<span id="post-70448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70448-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How do I map a bus stop that is not marked in any way?</p>
<p>I am mapping a bus stop that does not have a post, a sign or any other physical indicator - however, in all other ways it is a regular bus stop: buses do stop there regularly, the bus stop appears on official timetables, and the bus stop on the opposite side of the road (which is marked) has a note indicating that some buses stop on the opposite side.</p>
<p>The <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dbus_stop">wiki page for highway=bus_stop</a> just says:</p>
<blockquote>
<p>Some bus stops are unmarked and known only by word-of-mouth or from information provided on a timetables.</p>
</blockquote>
<p>However there is no information on how to tag this. I would think this information is important, because otherwise people who see the bus stop on a map and want to use it will be looking out for a sign that is not there.</p>
<p>Is there a tag like <code>unmarked=yes</code> or similar? Is there any proposal?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Aug '19, 11:39</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-70448" class="comments-container">
&#10;</div>
<div id="comment-tools-70448" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70448-form-container" class="comment-form-container">
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

<span id="70456"></span>

<div id="answer-container-70456" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70456-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70456-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70456-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi sleske, I don't see any formal documentation on it, but it seems that adding <code>unsigned=yes</code> is a common way to tag this. I tried to check <em>how</em> common this is but Overpass is giving me guff today. My rough guess is somewhere between 500 and 1000 uses, so a semi-established tagging practice.</p>
<p>I'd probably also add something like <code>description=bus stop is unsigned in this direction, wait opposite the sign across the road</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '19, 15:55</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-70456" class="comments-container">
<span id="71219"></span>
<div id="comment-71219" class="comment">
<div id="post-71219-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hm, <code>unsigned=yes</code> seems reasonable. However, at least during my quick check with Overpass, I did not find any usage for bus stops (it is used, but apparently only for streets without a sign post). So right now I'm wary of starting a new tagging scheme...</p>
</div>
<div id="comment-71219-info" class="comment-info">
<span class="comment-age">(17 Oct '19, 12:53)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-70456" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70456-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70482"></span>

<div id="answer-container-70482" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70482-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It happens quite often in rural areas. When I face this situation, I just tag the public_transport=paltform with shelter=no, pole=no, source=*. Anyway, current rendering won't make any difference. But it's good to put the information in the database for future use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Aug '19, 20:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a588fbc312ece948db9faa4cc02b40de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zorglubu&#39;s gravatar image" />
<p><span>zorglubu</span><br />
<span class="score" title="324 reputation points">324</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zorglubu has 3 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-70482" class="comments-container">
<span id="70486"></span>
<div id="comment-70486" class="comment">
<div id="post-70486-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Even in urban area of developing countries. Where I live, a city of 200 000 inhabitants, most of the bus stops are such: there's absolutely nothing (no sign, no platform, no shelter, no bench), all that might help you know there's a bus stop is just that you will see several people waiting, then you ask them: "Does the bus stop here?". I've been mapping them as normal bus stops (without putting platform, bench and shelter of course)</p>
</div>
<div id="comment-70486-info" class="comment-info">
<span class="comment-age">(23 Aug '19, 05:10)</span> <span class="comment-user userinfo">Privatemajory</span>
</div>
</div>
</div>
<div id="comment-tools-70482" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70482-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70451"></span>

<div id="answer-container-70451" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70451-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70451-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-70451-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Sleske, It is a strange phenomenal, what still only can be found in rural area's, for instance in Scandinavia. If you walk along a main road and put your hand up the bus driver will make a local stop and if you ask him to stop elsewhere, he would do so as well. Just like at any other time and place, but nowadays a bus driver has to get and keep his schedule at all times stealth stops are no part of it. IMHO you could tag the route of a bus line with that option or possibillity and not a specific place, like my uncle's farm. With the tag informal stop=yes</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Aug '19, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-70451" class="comments-container">
<span id="70455"></span>
<div id="comment-70455" class="comment">
<div id="post-70455-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This type of bus behavior is called "hail and ride" -- the rider can choose where to board and where to disembark the bus, anywhere along a given section. There's a special way to tag this: <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/hail_and_ride">https://wiki.openstreetmap.org/wiki/Proposed_features/hail_and_ride</a> In short, instead of adding stops, you add the section of road to a bus route relation and use <code>hail_and_ride</code> as the role of that section in that relation.</p>
<p>I don't think this is applicable to sleske's question, though. It sounds like this situation is a normal bus stop in a fixed location, just without a sign. (Of course there could also be "hail and ride" along this same section; having fixed bus stop locations doesn't preclude that.)</p>
</div>
<div id="comment-70455-info" class="comment-info">
<span class="comment-age">(21 Aug '19, 15:41)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
<span id="70481"></span>
<div id="comment-70481" class="comment">
<div id="post-70481-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There are also plenty of unmarked bus stops where you need to know where they are in order to catch the bus (usually in out-of-the-way places in the country, but sometimes when a route has changed but the signage hasn't caught up, or when there is a bus stop (flag) on one side of the road but not the other). In the UK Naptan dataset these are called Customary stops; they have been imported in many areas into OSM, but not tagged with highway=bus_stop. Hail-and-ride sections have in the past been marked this way but this is inaccurate and really a legacy of inadequate data systems being owned by PT providers.</p>
</div>
<div id="comment-70481-info" class="comment-info">
<span class="comment-age">(22 Aug '19, 18:46)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-70451" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70451-form-container" class="comment-form-container">
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

