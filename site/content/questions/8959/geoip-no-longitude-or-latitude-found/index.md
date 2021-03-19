+++
type = "question"
title = "GeoIP no longitude or latitude found"
description = '''Hi, I&#x27;m having trouble getting GeoIP resolution to work. I&#x27;ve downloaded the databases from Maxmind, set the correct path ( double checked ), checked permissions and file names and they&#x27;re accurate. I&#x27;ve also selected &quot;Enable GeoIP resolution&quot; under Protocols | IPV4.   When I view Endpoints, no Lati...'''
date = "2012-02-10T16:31:00Z"
lastmod = "2012-02-10T19:08:00Z"
weight = 8959
keywords = [ "geoip" ]
aliases = [ "/questions/8959" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [GeoIP no longitude or latitude found](/questions/8959/geoip-no-longitude-or-latitude-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8959-score" class="post-score" title="current number of votes">0</div><span id="post-8959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm having trouble getting GeoIP resolution to work. I've downloaded the databases from Maxmind, set the correct path ( double checked ), checked permissions and file names and they're accurate.</p><p>I've also selected "Enable GeoIP resolution" under Protocols | IPV4.<br />
</p><p>When I view Endpoints, no Latitude or Longitude information is displayed in any of the tabs, and if I try to use the map, I get the error "no latitude/longitude data found"</p><p>Any ideas?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-geoip" rel="tag" title="see questions tagged &#39;geoip&#39;">geoip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '12, 16:31</strong></p><img src="https://secure.gravatar.com/avatar/70ec78f9909cb916b49e538a0489216a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="glennX&#39;s gravatar image" /><p><span>glennX</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="glennX has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '12, 18:40</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-8959" class="comments-container"></div><div id="comment-tools-8959" class="comment-tools"></div><div class="clear"></div><div id="comment-8959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8960"></span>

<div id="answer-container-8960" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8960-score" class="post-score" title="current number of votes">0</div><span id="post-8960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe the IP addresses you are trying to map are <a href="http://en.wikipedia.org/wiki/IP_address#IPv4_private_addresses">private addresses</a> or <a href="http://en.wikipedia.org/wiki/Multicast_address">multicast</a> addresses? If that's the case, then you won't get any latitude/longitude information, hopefully for obvious reasons. If that's not the case, then what IP addresses are they?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '12, 19:08</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-8960" class="comments-container"></div><div id="comment-tools-8960" class="comment-tools"></div><div class="clear"></div><div id="comment-8960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

