+++
type = "question"
title = "What are the IGMP Messages doing in my network?"
description = '''Hey guys,  I´m trying to analyze my networktraffic and I´m not a networking pro, so I got some questions regarding the traffic. If there are stupid I apologize in front. The first thing I see are three IGMP Messages.  192.168.2.1 224.0.0.22 IGMP 62 V3 Membership Report /Join group 224.0.0.252 for an...'''
date = "2011-11-25T04:30:00Z"
lastmod = "2011-11-27T02:52:00Z"
weight = 7629
keywords = [ "igmp" ]
aliases = [ "/questions/7629" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What are the IGMP Messages doing in my network?](/questions/7629/what-are-the-igmp-messages-doing-in-my-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7629-score" class="post-score" title="current number of votes">0</div><span id="post-7629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys,</p><p>I´m trying to analyze my networktraffic and I´m not a networking pro, so I got some questions regarding the traffic. If there are stupid I apologize in front.</p><p>The first thing I see are three IGMP Messages. 192.168.2.1 224.0.0.22 IGMP 62 V3 Membership Report /Join group 224.0.0.252 for any sources / Join group 239.255.255.254 for any sources</p><p>10.0.0.0 224.0.0.1 IGMP 60 v3 Membership Query, general</p><p>192.168.2.1 224.0.0.22 IGMP 62 port /Join group 224.0.0.252 for any sources / Join group 239.255.255.254 for any sources</p><p>the first and third one are marked black, so there is an error, despite I don´t really know why.</p><p>So, I figured out IGMP has something to do with broadcasting and I figured out the IGMP messages are send at the start of the capture no matter when I start them. So I assume the have something to do with Wireshark.</p><p>The next thin I assume is, that every time I start wireshark it is looking for some broadcast groups. Since it´s marked false, I assume that nobody is answering. So wireshark tries but with no success.</p><p>So, could you please let me know what this have to do with wireshark, I know I don´t have a clue about the stuff, but I couldn´t find anythin on the internet.</p><p>Cheers</p><p>Michael</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-igmp" rel="tag" title="see questions tagged &#39;igmp&#39;">igmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '11, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/6dfd1e686d2457870aa6531245cf3d4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael86&#39;s gravatar image" /><p><span>Michael86</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael86 has no accepted answers">0%</span></p></div></div><div id="comments-container-7629" class="comments-container"></div><div id="comment-tools-7629" class="comment-tools"></div><div class="clear"></div><div id="comment-7629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7632"></span>

<div id="answer-container-7632" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7632-score" class="post-score" title="current number of votes">1</div><span id="post-7632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Google is your friend here. These are multicast addresses.</p><p>So, if you look them up they say:</p><ul><li>224.0.0.22 : Internet Group Management Protocol (IGMP) Version 3</li><li>224.0.0.252 : Link-local Multicast Name Resolution (LLMNR) address</li><li>239.255.255.254 : Multicast Address Dynamic Client Allocation Protocol (MADCAP)</li></ul><p>So these all have to do with name resolving. And indeed that's something Wireshark does use, so that makes sense.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '11, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7632" class="comments-container"><span id="7647"></span><div id="comment-7647" class="comment"><div id="post-7647-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick response. But I´m still not certain, why wireshark is doing this.</p><p>I learned that you need a software on your computer to be able to receive this multicast traffic. So i assume wireshark is trying to get in this multicast group to read the all traffic. Make sense for a network sniffer, but</p><p>first who is 224.0.0.22? I mean, is there are service on my network who is responding to wireshark? It says join group 224.0.0.252 for any sources, so does it mean, wireshark is trying to get in this group and furthermore does wireshark succed? Can I now read the multicast traffic?</p><p>Second, who is 10.0.0.0, he is sending a Membership Query general to 224.0.0.1. But I don´t have a clue what this is doing there.</p><p>The main question is, why is wireshark doing this?</p></div><div id="comment-7647-info" class="comment-info"><span class="comment-age">(26 Nov '11, 05:29)</span> <span class="comment-user userinfo">Michael86</span></div></div><span id="7660"></span><div id="comment-7660" class="comment"><div id="post-7660-score" class="comment-score"></div><div class="comment-text"><p>224.0.0.22 is the address all IGMPv3-capable multicast routers listen to. They have to learn of your host joining a multicast group, so they can forward you multicast messages send to this group. This has nothing to do with the capture itself, just the DNS functions used by Wireshark. A join is never acknowledged, the router just starts forwarding any relevant traffic. 10.0.0.0 is the address of an IGMP querier in the local network who tries to reaffirm multicast group memberships. If all hosts have dropped off the local net there's no need for multicast traffic to be forwarded there anymore.</p></div><div id="comment-7660-info" class="comment-info"><span class="comment-age">(27 Nov '11, 02:52)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-7632" class="comment-tools"></div><div class="clear"></div><div id="comment-7632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7654"></span>

<div id="answer-container-7654" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7654-score" class="post-score" title="current number of votes">0</div><span id="post-7654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When resolving names, what Wireshark is doing is attempting to translate IP addresses to names; it does so either by calling the host operating system's routines or by using the ADNS or C-ARES name resolution packages. Perhaps whichever one of those is being used sends out <a href="http://en.wikipedia.org/wiki/Link-local_Multicast_Name_Resolution">LLMNR</a> packets.</p><p>Wireshark itself does not explicitly try to join any multicast groups; it puts the network adapter into promiscuous mode so that it can see all traffic sent on the network port into which the network adapter is plugged. Perhaps, in some OSes, the networking stack will attempt to join multicast groups if the adapter is put into promiscuous mode, in the hopes of convincing a switch to send multicast traffic for those groups to the port in question.</p><p>224.0.0.22 is an IP address for <a href="http://www.ietf.org/rfc/rfc3376.txt">IGMP v3</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '11, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7654" class="comments-container"></div><div id="comment-tools-7654" class="comment-tools"></div><div class="clear"></div><div id="comment-7654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

