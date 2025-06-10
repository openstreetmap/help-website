+++
type = "question"
title = "Paths not visible in other gps applications"
description = '''I added a few paths in OSM. They are visible in other gps applications that use OSM (such as afstandmeten.nl), but routing does not go via these paths, even though it is the shortest route. How do I add paths that can actually be used in other GPS applications?'''
date = "2020-03-22T18:58:00Z"
lastmod = "2020-03-24T13:26:00Z"
weight = 73681
keywords = [ "paths" ]
aliases = [ "/questions/73681" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Paths not visible in other gps applications](/questions/73681/paths-not-visible-in-other-gps-applications)

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
<span id="post-73681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73681-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I added a few paths in OSM. They are visible in other gps applications that use OSM (such as afstandmeten.nl), but routing does not go via these paths, even though it is the shortest route. How do I add paths that can actually be used in other GPS applications?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-paths" rel="tag" title="see questions tagged &#39;paths&#39;">paths</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '20, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/68174b4fb2022d2b95dd6fb10b9fa587?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JustNicci48&#39;s gravatar image" />
<p><span>JustNicci48</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JustNicci48 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73681" class="comments-container">
<span id="73683"></span>
<div id="comment-73683" class="comment">
<div id="post-73683-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Can you tell us explicitly which application does not road over which way? I see two ways you created that can be routed via (<a href="https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=51.33668%2C4.96862%3B51.33668%2C4.96908#map=19/51.33674/4.96886">1</a>, <a href="https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=51.34145%2C4.97507%3B51.34094%2C4.97622#map=19/51.34120/4.97572">2</a>). A third way you have just deleted so it is hard to say what might have been wrong.</p>
</div>
<div id="comment-73683-info" class="comment-info">
<span class="comment-age">(22 Mar '20, 19:50)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="73687"></span>
<div id="comment-73687" class="comment">
<div id="post-73687-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the paths are unset it could explain why they are not routable. Unless the paths were tagged as foot=allowed or foot=designated i have noticed they won't route with Garmins i have used.</p>
</div>
<div id="comment-73687-info" class="comment-info">
<span class="comment-age">(23 Mar '20, 00:12)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="73688"></span>
<div id="comment-73688" class="comment">
<div id="post-73688-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looking at those two examples one is tagged as cycle and one is not. If you try cycle routing via them one works and one does not, but if depends if you use OSRM or Graphopper for some reason.</p>
</div>
<div id="comment-73688-info" class="comment-info">
<span class="comment-age">(23 Mar '20, 00:23)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="73708"></span>
<div id="comment-73708" class="comment">
<div id="post-73708-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Your path works for both OSRM and Graphhopper, for both foot and bicycle routing in each case. So you probably need to ask afstandmeten.nl to be sure why their routing gives a different result. It may be related to access tags as andy mackey suggested above. However that seems odd to me, I would expect a path to be open to non motorized traffic unless the access tags specify otherwise.</p>
</div>
<div id="comment-73708-info" class="comment-info">
<span class="comment-age">(23 Mar '20, 15:16)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-73681" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73681-form-container" class="comment-form-container">
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

<span id="73682"></span>

<div id="answer-container-73682" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73682-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-73682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How long ago did you add the paths? Changes can take a while to feed through to routing engines, sometimes longer than changes to map tiles - the fact that a change is visible on the map does not guarantee that it is being used for routing.</p>
<p>If you don't think that is the issue, maybe post a link to a specific path so we can look at whether something might be blocking the routing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '20, 19:48</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-73682" class="comments-container">
&#10;</div>
<div id="comment-tools-73682" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73682-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73704"></span>

<div id="answer-container-73704" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73704-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I added path <a href="https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=51.33680%2C4.96873%3B51.33673%2C4.96899">Polderstraat</a> weeks or months ago. To me, it looks the same as path <a href="https://www.openstreetmap.org/directions?engine=graphhopper_foot&amp;route=51.33937%2C4.97110%3B51.33939%2C4.97029">Rabauwakkers</a>, which was created by someone else. On the website <a href="http://www.afstandmeten.nl">www.afstandmeten.nl</a> (used for creating routes and calculating distances), the second one will be used in routes, whereas my path will not...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '20, 13:45</strong></p>
<img src="https://secure.gravatar.com/avatar/68174b4fb2022d2b95dd6fb10b9fa587?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JustNicci48&#39;s gravatar image" />
<p><span>JustNicci48</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JustNicci48 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '20, 13:47</strong> </span></p>
</div>
</div>
<div id="comments-container-73704" class="comments-container">
<span id="73718"></span>
<div id="comment-73718" class="comment">
<div id="post-73718-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>as mentioned elsewhere, it all depends on the frequency of the data updates. While your change is in OSM's database, it might take takes or even months before afstandmeten.nl updates their data.</p>
</div>
<div id="comment-73718-info" class="comment-info">
<span class="comment-age">(24 Mar '20, 04:34)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-73704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73704-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73711"></span>

<div id="answer-container-73711" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73711-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This side by side view of the two paths and their Tagging (in Potlatch2 edit mode and advanced mode) you will see that the tagging is slightly different. One has foot=yes tag the other does not. This, i think will explain what you have discovered.</p>
<p><img src="https://help.openstreetmap.org/upfiles/Both_paths_side_by_side.JPG" alt="alt text" /></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '20, 17:37</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Mar '20, 17:38</strong> </span></p>
</div>
</div>
<div id="comments-container-73711" class="comments-container">
<span id="73715"></span>
<div id="comment-73715" class="comment">
<div id="post-73715-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>We should note that both ways should yield the same results. A path should be accessible/routable by foot and by bicycle by default. As alan_gr observed above, JustNicci should contact the site/app that does not route correctly here to fix their rules. There is no need to alter the data.</p>
</div>
<div id="comment-73715-info" class="comment-info">
<span class="comment-age">(23 Mar '20, 20:27)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="73720"></span>
<div id="comment-73720" class="comment">
<div id="post-73720-score" class="comment-score">
2
</div>
<div class="comment-text">
<blockquote>
<p>A path should be accessible/routable by foot and by bicycle by default</p>
</blockquote>
<p>If you route with that assumption in all countries, then your routing will be terrible. Whatever it says in the wiki, this is not an observation that is consistently borne out in the field.</p>
</div>
<div id="comment-73720-info" class="comment-info">
<span class="comment-age">(24 Mar '20, 08:44)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="73727"></span>
<div id="comment-73727" class="comment">
<div id="post-73727-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You might be right that a universal rule comes with some problems. But that's why communities have tried to define some country specific rules (<a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access_restrictions">Wiki: Access_restrictions</a>) The general definition in Belgium (and in the Netherlands where the website seems to originate) is that a footway is good for foot traffic, a cycle way is good for bicycles and a path is good for both. If you want to have that differently you should tag it.</p>
<p>I would consider a router that does not route pedestrians via a footway in Belgium to be broken.</p>
<p>But I rather suspect that afstandmeten.nl has just not updated their data in a couple of months.</p>
</div>
<div id="comment-73727-info" class="comment-info">
<span class="comment-age">(24 Mar '20, 13:26)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-73711" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73711-form-container" class="comment-form-container">
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

