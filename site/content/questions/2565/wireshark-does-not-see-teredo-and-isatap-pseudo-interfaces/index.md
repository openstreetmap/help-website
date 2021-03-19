+++
type = "question"
title = "Wireshark does not see Teredo and ISATAP Pseudo-Interfaces"
description = '''Hello, I have installed on my PC several versions of wireshark. All of them show in the &quot;Capture Interfaces&quot; window three interfaces: the wired LAN interface, the wireless LAN interface, and a logical wireless interface. The last two are shown as &quot;Microsoft Intefaces&quot;. Wireshark deos not see the log...'''
date = "2011-02-25T08:54:00Z"
lastmod = "2011-02-28T09:45:00Z"
weight = 2565
keywords = [ "tunnel", "interfaces", "teredo", "ipv6" ]
aliases = [ "/questions/2565" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark does not see Teredo and ISATAP Pseudo-Interfaces](/questions/2565/wireshark-does-not-see-teredo-and-isatap-pseudo-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2565-score" class="post-score" title="current number of votes">0</div><span id="post-2565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have installed on my PC several versions of wireshark. All of them show in the "Capture Interfaces" window three interfaces: the wired LAN interface, the wireless LAN interface, and a logical wireless interface. The last two are shown as "Microsoft Intefaces".</p><p>Wireshark deos not see the logical IPv6 interfaces (Teredo and ISATAP tunnels). The Teredo interface is working and it is correctly shown by Microsoft Network Monitor 3.4!</p><p>Is there any way to make Wireshark see the Teredo interface?</p><p>Thanks to all, giorgio</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tunnel" rel="tag" title="see questions tagged &#39;tunnel&#39;">tunnel</span> <span class="post-tag tag-link-interfaces" rel="tag" title="see questions tagged &#39;interfaces&#39;">interfaces</span> <span class="post-tag tag-link-teredo" rel="tag" title="see questions tagged &#39;teredo&#39;">teredo</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '11, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/eab2e462ed33d377e30b4a9d75a1f543?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="giorgio&#39;s gravatar image" /><p><span>giorgio</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="giorgio has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Feb '11, 23:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-2565" class="comments-container"><span id="2569"></span><div id="comment-2569" class="comment"><div id="post-2569-score" class="comment-score">1</div><div class="comment-text"><p>I don't know the answer to your question. It does bring up a question I have though. Is it necessary or beneficial to be able to see the logical teredo and ISATAP interfces? Since they aren't encrypted, I'd imagine the protocols stack properly. In that case, it might be possible to simply do a capture filter down to the protocol (for ISATAP) and for the port (Teredo).</p></div><div id="comment-2569-info" class="comment-info"><span class="comment-age">(25 Feb '11, 16:22)</span> <span class="comment-user userinfo">Paul Stewart</span></div></div><span id="2573"></span><div id="comment-2573" class="comment"><div id="post-2573-score" class="comment-score"></div><div class="comment-text"><p>If filtering on the Teredo port number (3544) we will be able to capture only packets during the initial packet exchange between the Teredo client and the Teredo Server. Once two Teredo clients have obtained their IPv6 addresses, they will use in the IPv4 packet exchange the UDP port numbers embedded in their IPv6 addresses. So we cannot filter on the Teredo port number. We can filter seeking for the Teredo prefix (2001:0000/32) inside the UDP packets. But in this way Wireshark will capture and show the packets, but will not decode them as IPv6 packets.</p></div><div id="comment-2573-info" class="comment-info"><span class="comment-age">(26 Feb '11, 04:54)</span> <span class="comment-user userinfo">giorgio</span></div></div><span id="2574"></span><div id="comment-2574" class="comment"><div id="post-2574-score" class="comment-score">1</div><div class="comment-text"><p>In the last Teredo packet if you filter on "Teredo", you will expand and find "Destination Teredo Port". Then you need to decode everything to and from that port as Teredo. At that point, filtering on Teredo will show the maintenance communication and the transit communication. In the future maybe it will automagically do this like h323 and sip does.</p></div><div id="comment-2574-info" class="comment-info"><span class="comment-age">(26 Feb '11, 09:44)</span> <span class="comment-user userinfo">Paul Stewart</span></div></div><span id="2575"></span><div id="comment-2575" class="comment"><div id="post-2575-score" class="comment-score"></div><div class="comment-text"><p>Thanks Paul. I had never used the "decode" feature. It does work.</p></div><div id="comment-2575-info" class="comment-info"><span class="comment-age">(27 Feb '11, 01:40)</span> <span class="comment-user userinfo">giorgio</span></div></div><span id="2576"></span><div id="comment-2576" class="comment"><div id="post-2576-score" class="comment-score"></div><div class="comment-text"><p>I thought a lot about the original question. I personally think that Teredo and ISATAP tunnels should not show up as separate interfaces. However, it could make it much easier in certain instances. An example of this is the Cisco VPN adapter shows up as a separate interface. I guess in the case of Teredo and ISATAP, I feel like it is less of an interface and more of a "shim" protocol. I guess I can see it either way (show up as an interface or not). It would be nice if it would automatically decode the subsequent packets based on the setup though.</p></div><div id="comment-2576-info" class="comment-info"><span class="comment-age">(27 Feb '11, 07:04)</span> <span class="comment-user userinfo">Paul Stewart</span></div></div><span id="2590"></span><div id="comment-2590" class="comment not_top_scorer"><div id="post-2590-score" class="comment-score"></div><div class="comment-text"><p>I totally agree with your last statement: " It would be nice if it would automatically decode the subsequent packets based on the (interface) setup". Thanks</p></div><div id="comment-2590-info" class="comment-info"><span class="comment-age">(28 Feb '11, 09:45)</span> <span class="comment-user userinfo">giorgio</span></div></div></div><div id="comment-tools-2565" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-2565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2579"></span>

<div id="answer-container-2579" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2579-score" class="post-score" title="current number of votes">0</div><span id="post-2579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is probably a result of the way WinPcap, which is what Wireshark uses to capture network traffic on Windows, works. I don't know whether the WinPcap developers follow this site, but, if not, try <a href="http://www.winpcap.org/contact.htm">contacting the WinPcap developers</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '11, 23:22</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2579" class="comments-container"></div><div id="comment-tools-2579" class="comment-tools"></div><div class="clear"></div><div id="comment-2579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

