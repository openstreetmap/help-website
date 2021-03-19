+++
type = "question"
title = "SSDP traffic"
description = '''Hi all thank you for the reply on the IGMP and NBNS question.  Indeed it is an amazing experience to look through real time network traffic.  the reason i am looking through the traffic is that my computers are suffering from sever trojan attacks…:( recently i realised that the setting of my router ...'''
date = "2011-02-16T12:52:00Z"
lastmod = "2014-02-11T13:21:00Z"
weight = 2387
keywords = [ "-", "ssdp", "protocol", "upnp" ]
aliases = [ "/questions/2387" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SSDP traffic](/questions/2387/ssdp-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2387-score" class="post-score" title="current number of votes">0</div><span id="post-2387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>thank you for the reply on the IGMP and NBNS question.</p><p>Indeed it is an amazing experience to look through real time network traffic. the reason i am looking through the traffic is that my computers are suffering from sever trojan attacks…:(</p><p>recently i realised that the setting of my router have been changed … for example the UPnP setting form the default (disabled) was enabled. then..., at the wireshark traffic analysis:</p><p>source: 192.168.2.1 destination: 239.255.255.250 protocol: SSDP Info: NOTIFY* HTTP/1.1 Host: 239.255.255.250rn NT:urn:schemas-wifialliance-org:service:WFAWLANConfig:1rn NTS:ssdp:alivern Location:http://192.168.2.1:80/igd.xmlrn USN:uuid:00000000-0000-0001-1000-9444529c85c4::urn:schemas-wifialliance-org:service:WFWAWLANConfigg:1rn Server:F7D1401-v1/1.0 UPnP/1.0rn Cache-control:max-age=60rn rn</p><p>I disabled the UPnP at the router interface, and the next traffic capture from the wireshark was only with http packets. During both of the SSDP and http - TCP captures I only opened the internet explorer...nothing else</p><p>Does that mean that someone is attacking my router somehow? any advice?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link--" rel="tag" title="see questions tagged &#39;-&#39;">-</span> <span class="post-tag tag-link-ssdp" rel="tag" title="see questions tagged &#39;ssdp&#39;">ssdp</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-upnp" rel="tag" title="see questions tagged &#39;upnp&#39;">upnp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '11, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/e15247a28980167b64a8419f60a71e7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stefi&#39;s gravatar image" /><p><span>Stefi</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stefi has no accepted answers">0%</span></p></div></div><div id="comments-container-2387" class="comments-container"></div><div id="comment-tools-2387" class="comment-tools"></div><div class="clear"></div><div id="comment-2387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29716"></span>

<div id="answer-container-29716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29716-score" class="post-score" title="current number of votes">0</div><span id="post-29716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>SSDP (Simple Service Discovery protocol) is a part of UPnP (Universal Plug and Play).</p><p>It is normal traffic for all UPnP enabled devices in your LAN.</p><p>Each device will send out a group of NOTIFY packets every 15 minutes or so while UPnP is enabled.</p><p>Many devices will also periodically send out M-SEARCH packets, which are usually followed by response HTTP packets.</p><p>If you want to see them in WireShark, the best filter I have found to see just SSDP is this:</p><pre><code>(udp contains &quot;HTTP/1.1&quot;) and ((udp contains 0a:53:54:3a) or (udp contains 0a:59:54:3a))</code></pre><p>The hex is looking for the strings "ST:" and "NT:" at the beginning of a line.</p><p>-jesse</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '14, 13:21</strong></p><img src="https://secure.gravatar.com/avatar/7f01743e24e94a4bfe007c57079b21e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JesseChisholm&#39;s gravatar image" /><p><span>JesseChisholm</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JesseChisholm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '14, 13:22</strong> </span></p></div></div><div id="comments-container-29716" class="comments-container"></div><div id="comment-tools-29716" class="comment-tools"></div><div class="clear"></div><div id="comment-29716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

