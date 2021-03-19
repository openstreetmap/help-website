+++
type = "question"
title = "Capture F5 Vpn on Windows7"
description = '''Hi. I experienced problem when I tried to launch applications in company network after I had established full vpn network access from home =&amp;gt; I have obtained IP address(eg. 10.1.1.1) in company network. This 10.1.1.1 was assigned to my PPP Adaptor (shown in ipconfig) and not wireless nic interfac...'''
date = "2014-03-28T20:29:00Z"
lastmod = "2014-04-03T00:37:00Z"
weight = 31276
keywords = [ "winpcap", "windows7", "vpn", "f5" ]
aliases = [ "/questions/31276" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture F5 Vpn on Windows7](/questions/31276/capture-f5-vpn-on-windows7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31276-score" class="post-score" title="current number of votes">0</div><span id="post-31276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I experienced problem when I tried to launch applications in company network after I had established full vpn network access from home =&gt; I have obtained IP address(eg. 10.1.1.1) in company network. This 10.1.1.1 was assigned to my PPP Adaptor (shown in ipconfig) and not wireless nic interface.</p><p>I am using f5 VPN and windows7.</p><p>I turned on wireshark and realised the Capture Interface does not include the PPP Interface assigned with 10.1.1.1.</p><p>I googled and saw suggestions that the latest Winpcap 4.1.3 may not support capture over VPN,and I should downgrade to Winpcap 3.1. So I tried to install Winpcap 3.1 on Windows7 but I got error "installation not supported on this OS"</p><p>Btw, if this capture over vpn from 10.1.1.1 can work, am I right to assume that wireshark can capture the ip and tcp info for corresponding access over the VPN for analysis and only data is encrypted?</p><p>I seek advice from experts like u : )</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-f5" rel="tag" title="see questions tagged &#39;f5&#39;">f5</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '14, 20:29</strong></p><img src="https://secure.gravatar.com/avatar/66ff60caa109e46ba0cc25637cbbddaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="walnut23&#39;s gravatar image" /><p><span>walnut23</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="walnut23 has no accepted answers">0%</span></p></div></div><div id="comments-container-31276" class="comments-container"></div><div id="comment-tools-31276" class="comment-tools"></div><div class="clear"></div><div id="comment-31276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31288"></span>

<div id="answer-container-31288" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31288-score" class="post-score" title="current number of votes">0</div><span id="post-31288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The F5 VPN client should install a virtual network adapter, but I assume you are using the clientless version which does not. The WinPcap FAQ says that it's not possible to capture PPP/VPN connections on Win 7 and some third party VPN implementation are not detected because of their unclean NDIS intermediate driver structure. See <a href="http://www.winpcap.org/misc/faq.htm#Q-5">http://www.winpcap.org/misc/faq.htm#Q-5</a></p><p>If you can, install the F5 VPN client or use MS Network Monitor instead of Wireshark to capture the traffic.</p><p>In general the traffic will be in clear text (if it was not encrypted by an application) on the VPN interface and encrypted on your physical interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '14, 17:19</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-31288" class="comments-container"><span id="31371"></span><div id="comment-31371" class="comment"><div id="post-31371-score" class="comment-score"></div><div class="comment-text"><p>Thanks for responding.</p><p>I have installed the F5 VPN client prior to Wireshark capture with no success(cannot detect PPP adaptor assigned with assigned ip address from VPN gateway)</p><p>I have also tried installing MS Network Monitor to capture the traffic with no success(cannot detect PPP adaptor assigned with assigned ip address from VPN gateway)</p><p>:(</p></div><div id="comment-31371-info" class="comment-info"><span class="comment-age">(02 Apr '14, 01:38)</span> <span class="comment-user userinfo">walnut23</span></div></div><span id="31455"></span><div id="comment-31455" class="comment"><div id="post-31455-score" class="comment-score"></div><div class="comment-text"><p>Are you using Firepass or APM?</p></div><div id="comment-31455-info" class="comment-info"><span class="comment-age">(03 Apr '14, 00:37)</span> <span class="comment-user userinfo">Roland</span></div></div></div><div id="comment-tools-31288" class="comment-tools"></div><div class="clear"></div><div id="comment-31288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

