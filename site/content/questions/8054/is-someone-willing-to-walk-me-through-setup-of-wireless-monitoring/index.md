+++
type = "question"
title = "Is someone willing to walk me through setup of wireless monitoring?"
description = '''I bought a switch capable of port mirroring. Use a mac and need to monitor another mac on my wireless network. I need to know how to set up the system and use Wireshark. I don&#x27;t have a PC or Mac close to the router/switch. I have multiple wireless routers if that matters, but don&#x27;t have to use them....'''
date = "2011-12-19T20:30:00Z"
lastmod = "2011-12-29T00:37:00Z"
weight = 8054
keywords = [ "wireless", "monitoring" ]
aliases = [ "/questions/8054" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is someone willing to walk me through setup of wireless monitoring?](/questions/8054/is-someone-willing-to-walk-me-through-setup-of-wireless-monitoring)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8054-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I bought a switch capable of port mirroring. Use a mac and need to monitor another mac on my wireless network. I need to know how to set up the system and use Wireshark. I don't have a PC or Mac close to the router/switch. I have multiple wireless routers if that matters, but don't have to use them. Thanks</p></div><div id="question-tags" class="tags-container tags">wireless monitoring</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '11, 20:30</strong></p><img src="https://secure.gravatar.com/avatar/d84b39734ade3f5393ad7fe72c045f95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="becomer&#39;s gravatar image" /><p>becomer<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="becomer has no accepted answers">0%</span></p></div></div><div id="comments-container-8054" class="comments-container"><span id="8056"></span><div id="comment-8056" class="comment"><div id="post-8056-score" class="comment-score"></div><div class="comment-text"><p>Yes we were willing to walk everybody through this. Thats why if you use the SEARCH function on this site, there are multiple topics regarding wireless captures and everything related to it.</p><p>Plus there is the very nice wireshark wiki explaining everything you need to know!</p></div><div id="comment-8056-info" class="comment-info"><span class="comment-age">(20 Dec '11, 01:37)</span> Landi</div></div><span id="8057"></span><div id="comment-8057" class="comment"><div id="post-8057-score" class="comment-score"></div><div class="comment-text"><p>The Wireshark Wiki is <a href="http://wiki.wireshark.org/FrontPage">here</a>. You might be interested in the article on <a href="http://wiki.wireshark.org/CaptureSetup">CaptureSetup</a>. Additionally, the <a href="http://www.wireshark.org/docs/wsug_html_chunked/">Wireshark User's Guide</a> may help you as well.</p><p>If you have a more specific question, perhaps about a particular step in the process, that is more likely to get a usable answer.</p></div><div id="comment-8057-info" class="comment-info"><span class="comment-age">(20 Dec '11, 06:48)</span> multipleinte...</div></div><span id="8073"></span><div id="comment-8073" class="comment"><div id="post-8073-score" class="comment-score"></div><div class="comment-text"><p>Do you want to monitor the wireless traffic sent to or by the other Mac - in which case the switch won't help, as the port mirroring would catch <em>wired</em> traffic - or do you want to monitor the traffic to or from that Mac that goes through the switch?</p></div><div id="comment-8073-info" class="comment-info"><span class="comment-age">(21 Dec '11, 14:49)</span> Guy Harris ♦♦</div></div><span id="8122"></span><div id="comment-8122" class="comment"><div id="post-8122-score" class="comment-score"></div><div class="comment-text"><p>I would like to monitor all traffic. Both Macs are wireless. Can I place the switch between the router and cable modem? I would like traffic both ways. Is it possible and if so how? I need setup and instructions for Wireshark. I am particularly concerned with email traffic, but all email from other Mac goes through webmail and not a program such as outlook. Any help would be greatly appreciated.</p></div><div id="comment-8122-info" class="comment-info"><span class="comment-age">(23 Dec '11, 20:08)</span> becomer</div></div><span id="8125"></span><div id="comment-8125" class="comment"><div id="post-8125-score" class="comment-score"></div><div class="comment-text"><p>If you truly want to monitor <em>all</em> traffic, i.e. monitor every single network segment on your network, you'll need to tell us how your network is set up, in its entirety. You have at least two Macs on your wireless network, and the fact that you have a wireless network probably means you have a wireless access point - do you have a Wi-Fi router directly connected by Ethernet to your cable modem, or is your network more complicated than that?</p></div><div id="comment-8125-info" class="comment-info"><span class="comment-age">(24 Dec '11, 01:12)</span> Guy Harris ♦♦</div></div><span id="8159"></span><div id="comment-8159" class="comment not_top_scorer"><div id="post-8159-score" class="comment-score"></div><div class="comment-text"><p>Guy Harris, I have comcast cable modem, ethernet to wireless router and all traffic goes through the router. I bought a switch with port monitoring thinking I could capture all traffic between router and modem. I would like all traffic as in emails sent and received through outlook, OSx mail and utilizing webmail (yahoo and google). Also if messaging as in facebook, etc is possible.<br />
Thanks</p></div><div id="comment-8159-info" class="comment-info"><span class="comment-age">(28 Dec '11, 20:04)</span> becomer</div></div></div><div id="comment-tools-8054" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-8054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8161"></span>

<div id="answer-container-8161" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8161-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, so that network isn't <em>too</em> complicated. Most of your traffic is probably between the machines with Wi-Fi access and the wireless router, so if you plug the wireless router's Ethernet connection and the cable modem's Ethernet connection into the switch, and set up a monitoring port on the cable modem and plug one of your Mac's <em>Ethernet</em> ports into the monitoring port, and have Wireshark capture traffic on the <em>Ethernet</em> port (<code>en0</code>) and do so in promiscuous mode, you should see all traffic running through the switch - i.e., all Ethernet traffic from the other Wi-Fi machines to and from the Internet.</p><p>I.e., with this setup, you don't need to use the monitoring machine's wireless interface to capture all the traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Dec '11, 00:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div></div><div id="comments-container-8161" class="comments-container"></div><div id="comment-tools-8161" class="comment-tools"></div><div class="clear"></div><div id="comment-8161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

