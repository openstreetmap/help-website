+++
type = "question"
title = "DHCPv6 packets not seen"
description = '''Hi All, Let me describe my situation: I am trying to check for the DHCPv6 packets (mainly solicit messages) sent to the Router from the CMTS. I have a PC which is connected behind a CMTS in my environment , basically connected to the Switch belonging to the CMTS. And I am able to get any data coming...'''
date = "2014-08-19T14:12:00Z"
lastmod = "2014-08-25T18:21:00Z"
weight = 35597
keywords = [ "dhcpv6" ]
aliases = [ "/questions/35597" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DHCPv6 packets not seen](/questions/35597/dhcpv6-packets-not-seen)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35597-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35597-score" class="post-score" title="current number of votes">0</div><span id="post-35597-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>Let me describe my situation:</p><p>I am trying to check for the DHCPv6 packets (mainly solicit messages) sent to the Router from the CMTS.</p><p>I have a PC which is connected behind a CMTS in my environment , basically connected to the Switch belonging to the CMTS. And I am able to get any data coming from the CMTS to the Router. I am running wireshark on this particular windows 7 PC and sniffing on the mentioned WAN side But I am unable to sniff "DHCPv6 packets" . My sniffed interface has both Ipv6 and Ipv4 address.</p><p>whereas If i sniff on the DHCPv6 server machine itself using wireshark I can see the packets . The server machine is a Fedora linux one.</p><p>I am using wireshar 1.12 and i can see "DHCPv6" protocol enabled under the "enabled protcols" and I can even sniff icmpv6 and other packets , but not DHCPv6 ones</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dhcpv6" rel="tag" title="see questions tagged &#39;dhcpv6&#39;">dhcpv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '14, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/35103890f2be63f3116eee2c058265a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gourab%20Majumdar&#39;s gravatar image" /><p><span>Gourab Majumdar</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gourab Majumdar has no accepted answers">0%</span></p></div></div><div id="comments-container-35597" class="comments-container"><span id="35735"></span><div id="comment-35735" class="comment"><div id="post-35735-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, but for me it's unclear how your environment looks like and where exactly you were sniffing. You are talking about a Cable modem (CMTS??) a router and a Linux DHCP server. Can you please add a drawing of your environment and where exactly you were capturing the traffic.</p><ul><li>Where is the Linux DHCP server located in relation to the router and the CMTS</li><li>Where exactly did you try to capture DHCPv6 traffic</li></ul></div><div id="comment-35735-info" class="comment-info"><span class="comment-age">(25 Aug '14, 16:11)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="35739"></span><div id="comment-35739" class="comment"><div id="post-35739-score" class="comment-score"></div><div class="comment-text"><p>The setup is as follows :</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark_forum_1.jpg" alt="alt text" /></p><p>DHCP linux server is beyond the CMTS . I am trying to capture packets on my win7 PC which is connected to the WAN side interface and is on the same network subnet as the CMTS or DHCPv6 server.</p></div><div id="comment-35739-info" class="comment-info"><span class="comment-age">(25 Aug '14, 18:21)</span> <span class="comment-user userinfo">Gourab Majumdar</span></div></div></div><div id="comment-tools-35597" class="comment-tools"></div><div class="clear"></div><div id="comment-35597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

