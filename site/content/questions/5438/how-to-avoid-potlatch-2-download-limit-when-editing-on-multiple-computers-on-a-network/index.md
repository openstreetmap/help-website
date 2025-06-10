+++
type = "question"
title = "how to avoid Potlatch 2 download limit when editing on multiple computers on a network?"
description = '''Hi, I work as an OSM-community manager for the Danish Cyclist Federation. We&#x27;re going all in with OSM for all our map needs and my job is to teach as many of our 17.000 members to edit. We&#x27;re teaching Potlatch 2, but have problems with hitting the download limit almost instantly during sessions. We&#x27;...'''
date = "2011-05-30T13:55:00Z"
lastmod = "2011-06-27T15:40:00Z"
weight = 5438
keywords = [ "potlatch2", "download", "lan", "limit", "proxy" ]
aliases = [ "/questions/5438" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [how to avoid Potlatch 2 download limit when editing on multiple computers on a network?](/questions/5438/how-to-avoid-potlatch-2-download-limit-when-editing-on-multiple-computers-on-a-network)

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
<span id="post-5438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5438-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-5438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I work as an OSM-community manager for the Danish Cyclist Federation. We're going all in with OSM for all our map needs and my job is to teach as many of our 17.000 members to edit. We're teaching Potlatch 2, but have problems with hitting the download limit almost instantly during sessions. We're guessing it's because our network uses a proxy with a single outgoing IP for all 10+ computers in use.</p>
<p>This is bad news, not least because I have to go on road trips around the country and use unfamiliar network setups.</p>
<p>1) What sort of network setup would be required to avoid hitting the download wall? I'm not much into this, but please feel free to shove tech-stuff at me. I'll pass it on to our resident buffs.</p>
<p>2) I've read earlier posts saying there is no possibility of having an IP-address put on a whitelist. Is this still the case?</p>
<p>Regards Andreas</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-potlatch2" rel="tag" title="see questions tagged &#39;potlatch2&#39;">potlatch2</span> <span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-lan" rel="tag" title="see questions tagged &#39;lan&#39;">lan</span> <span class="post-tag tag-link-limit" rel="tag" title="see questions tagged &#39;limit&#39;">limit</span> <span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 May '11, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/81e1bc8f59a4a03ed223ab5776f4a44f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hammershoej&#39;s gravatar image" />
<p><span>Hammershoej</span><br />
<span class="score" title="166 reputation points">166</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hammershoej has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5438" class="comments-container">
&#10;</div>
<div id="comment-tools-5438" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5438-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="5528"></span>

<div id="answer-container-5528" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5528-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-5528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The map data downloads are capped per-IP, so any kind of proxied network (e.g. NAT) is going to have this problem. If you are using a network where the different computers have different public IP addresses, then you will have much less of a issue.</p>
<p>There is currently no solution available for per-IP whitelisting, mainly because we don't have the manpower to deal with non-automated solutions like that. There have been discussions about taking into account signed-in users and even users-who-upload-changesets and raising the limits for these people, but again neither of those options are currently active.</p>
<p>The best solution is to encourage people to zoom in as far as possible before editing, so that they download the minimum possible data for the area that they are editing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '11, 11:20</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jun '11, 14:35</strong> </span></p>
</div>
</div>
<div id="comments-container-5528" class="comments-container">
<span id="5532"></span>
<div id="comment-5532" class="comment">
<div id="post-5532-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi, thanks for the answer.</p>
<p>We're always very careful about having people zoom in, but it just isn't enough. Also, we can't change our network setup or bet on finding suitable networks as we go on OSM road trips. I think our best chance is to buy a small heap of USB-modems. They'll hopefully be fast enough and have their own IP's.</p>
<p>It's an unfortunate problem, but I understand the reason for the limit. Hope you find a solution for networks, though.</p>
<p>Thanks a lot for the great work you are doing:)</p>
<p>/A</p>
</div>
<div id="comment-5532-info" class="comment-info">
<span class="comment-age">(03 Jun '11, 12:50)</span> <span class="comment-user userinfo">Hammershoej</span>
</div>
</div>
<span id="5545"></span>
<div id="comment-5545" class="comment">
<div id="post-5545-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the explanation Andy.</p>
<p>This situation impacted a mapping party in Uganda: <a href="https://twitter.com/#!/batje/status/76956988948496384">https://twitter.com/#!/batje/status/76956988948496384</a></p>
<p>Is there any stats on how often this happens? And any idea on what the manual workload would be?</p>
<p>What does it take to add in the tweaks to raise limits?</p>
</div>
<div id="comment-5545-info" class="comment-info">
<span class="comment-age">(04 Jun '11, 16:10)</span> <span class="comment-user userinfo">mikelmaron</span>
</div>
</div>
<span id="5952"></span>
<div id="comment-5952" class="comment">
<div id="post-5952-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Andy.</p>
<p>Thanks for the explanation.</p>
<p>I was attending the course that Andreas describes. We did not use any kind of proxy server. So in that sense the HTTP requests did not come from the same machine (IP address). We were however sitting behind a NAT, so in some sense we were sharing the same GLOBAL IP address. Can you please elaborate on your comment "If you are using a network where the different computers have different IP addresses, then you will have much less of a issue."? Apparently this was our situation and we still had issues regarding this.</p>
<p>Thanks in advance...</p>
<p>Jarl</p>
</div>
<div id="comment-5952-info" class="comment-info">
<span class="comment-age">(22 Jun '11, 13:38)</span> <span class="comment-user userinfo">jarl</span>
</div>
</div>
<span id="5953"></span>
<div id="comment-5953" class="comment">
<div id="post-5953-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>well, a NAT is a form of proxying in that the NAT machine intercepts the requests, alters the IP addresses and forwards them on. I've updated my answer to specifically state NAT and that it's the number of public IP addresses that is important.</p>
</div>
<div id="comment-5953-info" class="comment-info">
<span class="comment-age">(22 Jun '11, 14:38)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="5965"></span>
<div id="comment-5965" class="comment">
<div id="post-5965-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Would proxying some of your requests via a 3rd party proxy server help in this case? (Or multiple different proxy servers.) I'm not suggesting you try to circumvent the protections on people flooding the API, but it sounds like you simply have multiple people trying to use it normally.</p>
</div>
<div id="comment-5965-info" class="comment-info">
<span class="comment-age">(23 Jun '11, 00:35)</span> <span class="comment-user userinfo">Ebenezer</span>
</div>
</div>
<span id="6023"></span>
<div id="comment-6023" class="comment not_top_scorer">
<div id="post-6023-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Andy. Thank you for clearing out the heuristics for determine individual "users", I would like to suggest the heuristics to be improved to distinguish individual users even behind NAT, but I guess that must be somewhere else in a different forum, can you suggest any good starting points for such a discussion? I have plans to arrange some mapping parties but I hesitate as long as this problem exists.</p>
</div>
<div id="comment-6023-info" class="comment-info">
<span class="comment-age">(27 Jun '11, 14:35)</span> <span class="comment-user userinfo">jarl</span>
</div>
</div>
<span id="6024"></span>
<div id="comment-6024" class="comment not_top_scorer">
<div id="post-6024-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>dev@<a href="http://openstreetmap.org">openstreetmap.org</a> is the best place for development discussions.</p>
</div>
<div id="comment-6024-info" class="comment-info">
<span class="comment-age">(27 Jun '11, 15:40)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
</div>
<div id="comment-tools-5528" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-5528-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5538"></span>

<div id="answer-container-5538" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5538-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5538-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5538-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you were to use <a href="http://wiki.openstreetmap.org/wiki/JOSM">JOSM</a> instead you'd be less likely to hit the limit, since it gives more control over what data gets downloaded when.</p>
<p>That's probably not a very helpful suggestion because it's a whole new software to learn/teach but perhaps it's an option for you. JOSM is not as difficult for new users as people sometimes suggest.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '11, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-5538" class="comments-container">
<span id="5968"></span>
<div id="comment-5968" class="comment">
<div id="post-5968-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In a group situation it would be easier to get a demo or ask questions on josm but you are asking about P2</p>
</div>
<div id="comment-5968-info" class="comment-info">
<span class="comment-age">(23 Jun '11, 16:30)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-5538" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5538-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5960"></span>

<div id="answer-container-5960" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5960-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm currently working on an improvement to Potlatch 2 that will typically result in it pulling down less data from the server when you pan. (Well, to be strictly accurate, I'm converting some clever code by Matt Amos to ActionScript for Potlatch 2. :) ) It won't be live for a few weeks but it should hopefully make a difference.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jun '11, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-5960" class="comments-container">
&#10;</div>
<div id="comment-tools-5960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5960-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5975"></span>

<div id="answer-container-5975" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5975-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One of our members, a keen open-source man, has offered to administer a P2 white-list for situations like mapping parties. He works for Denmark's largest dedicated IT-security company, Dubex ( <a href="http://www.dubex.dk/dubex/profile/">http://www.dubex.dk/dubex/profile/</a> + <a href="http://www.linkedin.com/company/40332">http://www.linkedin.com/company/40332</a> ) and I'm sure he would be more than qualified to take on the task.</p>
<p>Would the P2 team be interested in this? If so I can set up contact.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '11, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/81e1bc8f59a4a03ed223ab5776f4a44f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hammershoej&#39;s gravatar image" />
<p><span>Hammershoej</span><br />
<span class="score" title="166 reputation points">166</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hammershoej has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5975" class="comments-container">
<span id="5976"></span>
<div id="comment-5976" class="comment">
<div id="post-5976-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's not a P2 issue - it's a server issue.</p>
</div>
<div id="comment-5976-info" class="comment-info">
<span class="comment-age">(24 Jun '11, 08:39)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="5977"></span>
<div id="comment-5977" class="comment">
<div id="post-5977-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, would the serverguys be interested then? And who are they?</p>
</div>
<div id="comment-5977-info" class="comment-info">
<span class="comment-age">(24 Jun '11, 08:57)</span> <span class="comment-user userinfo">Hammershoej</span>
</div>
</div>
<span id="5983"></span>
<div id="comment-5983" class="comment">
<div id="post-5983-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The server admin guys are listed at <a href="http://wiki.openstreetmap.org/wiki/Sysadmin">http://wiki.openstreetmap.org/wiki/Sysadmin</a></p>
</div>
<div id="comment-5983-info" class="comment-info">
<span class="comment-age">(24 Jun '11, 19:21)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-5975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5975-form-container" class="comment-form-container">
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

