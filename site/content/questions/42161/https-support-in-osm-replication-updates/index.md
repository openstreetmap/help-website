+++
type = "question"
title = "[closed] HTTPS support in osm replication updates"
description = '''Hi, Since the OSM updates diff support only http, I cannot update the OSM database in my production environment due to security issue. It is vulnerable to MITM(Man-In-The-Middle) attack. When I tried https url, it redirects to http url.  https://planet.openstreetmap.org/replication/day/000/000/ Is t...'''
date = "2015-04-07T08:03:00Z"
lastmod = "2015-04-08T04:18:00Z"
weight = 42161
keywords = [ "planet", "diff", "https" ]
aliases = [ "/questions/42161" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] HTTPS support in osm replication updates](/questions/42161/https-support-in-osm-replication-updates)

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
<span id="post-42161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42161-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Since the OSM updates diff support only http, I cannot update the OSM database in my production environment due to security issue. It is vulnerable to MITM(Man-In-The-Middle) attack. When I tried https url, it redirects to http url.</p>
<p><a href="https://planet.openstreetmap.org/replication/day/000/000/">https://planet.openstreetmap.org/replication/day/000/000/</a></p>
<p>Is there any specific reason for not having https support ?</p>
<p>It would be great, if OSM gives support https. And also OSM may add md5check sum details in the xx_state.txt files.</p>
<p>Thanks,</p>
<p>Ramesh</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-diff" rel="tag" title="see questions tagged &#39;diff&#39;">diff</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Apr '15, 08:03</strong></p>
<img src="https://secure.gravatar.com/avatar/1730eca5ec5677fb1f6d4d7f25797cf2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rameshj&#39;s gravatar image" />
<p><span>rameshj</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rameshj has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>08 Apr '15, 04:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42161" class="comments-container">
&#10;</div>
<div id="comment-tools-42161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42161-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Problem is outdated – problem has been fixed by server admins (HTTPS works now as expected)" by aseerel4c26 08 Apr '15, 04:23

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42180"></span>

<div id="answer-container-42180" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42180-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>your URL works for me (current Firefox 37.0.1) – no redirect to HTTP. I could download the arbitrarily chosen <a href="https://planet.openstreetmap.org/replication/day/000/000/012.osc.gz">https://planet.openstreetmap.org/replication/day/000/000/012.osc.gz</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '15, 03:56</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-42180" class="comments-container">
<span id="42181"></span>
<div id="comment-42181" class="comment">
<div id="post-42181-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I raised a ticket yesterday and OSM fixed it very quickly. Thanks to OSM team. Special Thanks to Tom Hughes !</p>
</div>
<div id="comment-42181-info" class="comment-info">
<span class="comment-age">(08 Apr '15, 04:13)</span> <span class="comment-user userinfo">rameshj</span>
</div>
</div>
<span id="42182"></span>
<div id="comment-42182" class="comment">
<div id="post-42182-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Okay, fine, thanks! There it is: <a href="https://trac.openstreetmap.org/ticket/5302">https://trac.openstreetmap.org/ticket/5302</a></p>
<p>Next time, please provide cross links to such new (and old) locations.</p>
</div>
<div id="comment-42182-info" class="comment-info">
<span class="comment-age">(08 Apr '15, 04:18)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42180-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="42165"></span>

<div id="answer-container-42165" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42165-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>https has a slightly higher resource consumption and is not as easily cachable as HTTP. Also you need to purchase a SSL certificate. All factors that add cost. You might have to use a workaround on your environment. Maybe you can setup and additional server that passes through the data from openstreetmap.org through a SSL channcel.</p>
<p>Adding a md5 checksum to the files seams reasonable. You might want to ask operations@osmfoundation.org</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Apr '15, 10:24</strong></p>
<img src="https://secure.gravatar.com/avatar/9ac1de0d402dfdf47bd4c4d664156c64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap_Alexander&#39;s gravatar image" />
<p><span>AddisMap_Ale...</span><br />
<span class="score" title="1120 reputation points"><span>1.1k</span></span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap_Alexander has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42165" class="comments-container">
<span id="42179"></span>
<div id="comment-42179" class="comment">
<div id="post-42179-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>not really … OSM already has a wildcard certificate *.openstreetmap.org which is used for e.g. <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> and for this help site.</p>
</div>
<div id="comment-42179-info" class="comment-info">
<span class="comment-age">(08 Apr '15, 03:53)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42165" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42165-form-container" class="comment-form-container">
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

