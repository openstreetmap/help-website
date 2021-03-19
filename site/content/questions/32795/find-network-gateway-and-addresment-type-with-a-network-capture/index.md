+++
type = "question"
title = "Find network gateway and addresment type with a network capture."
description = '''Hi! First of all I&#x27;m newbie using wireshark, I also got common network knownledge. I&#x27;ve got a network captured file, with 50k packets, it&#x27;s from a big institution, and I need to know two things about it:  Type of network addressment (classful A/B/C or Classless and it&#x27;s mask) Network gateway  In my ...'''
date = "2014-05-14T06:33:00Z"
lastmod = "2014-05-15T00:36:00Z"
weight = 32795
keywords = [ "mask", "gateway" ]
aliases = [ "/questions/32795" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Find network gateway and addresment type with a network capture.](/questions/32795/find-network-gateway-and-addresment-type-with-a-network-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32795-score" class="post-score" title="current number of votes">0</div><span id="post-32795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! First of all I'm newbie using wireshark, I also got common network knownledge.</p><p>I've got a network captured file, with 50k packets, it's from a big institution, and I need to know two things about it:</p><ul><li>Type of network addressment (classful A/B/C or Classless and it's mask)</li><li>Network gateway</li></ul><p>In my capture I see that 99% of ip's are 172.16.X.X, so I asume that's ClasFul B, and most ppackets go to 172.16.20.1, so I supose that's the default gateway, but how can I be more sure? Some type of filter?</p><p>Thanks a lot!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mask" rel="tag" title="see questions tagged &#39;mask&#39;">mask</span> <span class="post-tag tag-link-gateway" rel="tag" title="see questions tagged &#39;gateway&#39;">gateway</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '14, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/861dec3aae8fb99f794886cd0dd68a90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rul3s&#39;s gravatar image" /><p><span>rul3s</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rul3s has no accepted answers">0%</span></p></div></div><div id="comments-container-32795" class="comments-container"></div><div id="comment-tools-32795" class="comment-tools"></div><div class="clear"></div><div id="comment-32795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32804"></span>

<div id="answer-container-32804" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32804-score" class="post-score" title="current number of votes">2</div><span id="post-32804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rul3s has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are several options to conclude the netmask based on the traffic in the capture file.</p><ul><li>check the IP addresses in the capture file and try to figure out the mask as you did it, by looking at the distribution of the addresses in a certain range.</li><li>try to find packets to the local network broadcast address (like 172.16.<strong>255.255</strong> or 172.16.20.<strong>255</strong>)</li><li>take a look at ARP requests. If they are also spread across 172.16.x.x, chances are good, that your netmask is /16.</li></ul><p>Regarding the default gateway.</p><ul><li>take a look at ARP requests. If several systems ask for the MAC address of the same IP address, that 'could' be the default gateway. However, it could be a local busy server as well, unless the IP address is one of the 'typical' gateway addresses x.x.x.1, x.x.x.254, x.x.x.253, etc.</li><li>take a look at the destination MAC address of connections to an external network (e.g. internet). If there is the same MAC address for several different destination IP addresses, that's most certainly the router/gateway.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '14, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32804" class="comments-container"><span id="32808"></span><div id="comment-32808" class="comment"><div id="post-32808-score" class="comment-score"></div><div class="comment-text"><p>Also, if there is IPv6 traffic, look for Router Advertisements. You will then know the MAC of the Router and can filter on that MAC to learn the IPv4 address.</p></div><div id="comment-32808-info" class="comment-info"><span class="comment-age">(14 May '14, 21:12)</span> <span class="comment-user userinfo">Rooster_50</span></div></div><span id="32809"></span><div id="comment-32809" class="comment"><div id="post-32809-score" class="comment-score"></div><div class="comment-text"><p>Mate!! Thanks you so much, perfect answer!!! :)</p></div><div id="comment-32809-info" class="comment-info"><span class="comment-age">(15 May '14, 00:36)</span> <span class="comment-user userinfo">rul3s</span></div></div></div><div id="comment-tools-32804" class="comment-tools"></div><div class="clear"></div><div id="comment-32804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

