+++
type = "question"
title = "radius packet processing issue - not enough room in packet for AVP"
description = '''Hi Experts, While analysing radius packet traces in wireshark - I noticed error i.e. &quot;Not enough room in packet for AVP&quot; Besides -  1. this packet is visible only in wireshark. If I search such packets in application logs I don&#x27;t find them at all. 2. there are certain other packets also which look g...'''
date = "2017-02-25T11:19:00Z"
lastmod = "2017-03-19T22:01:00Z"
weight = 59683
keywords = [ "performance", "radius" ]
aliases = [ "/questions/59683" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [radius packet processing issue - not enough room in packet for AVP](/questions/59683/radius-packet-processing-issue-not-enough-room-in-packet-for-avp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59683-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59683-score" class="post-score" title="current number of votes">0</div><span id="post-59683-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts,</p><p>While analysing radius packet traces in wireshark - I noticed error i.e. "Not enough room in packet for AVP"</p><p>Besides - 1. this packet is visible only in wireshark. If I search such packets in application logs I don't find them at all. 2. there are certain other packets also which look genuine in wireshark - but they too are not visible in application logs at all.</p><p>We are using RHEL 7 with kernel 3.10.0-229.1.2.el7.x86_64. It is VM instance &amp; not physical server.</p><p>I tried searching Internet but didnt find much hints (other than dictionary defination which is not the case here). Has anyone observed such issue pertaining to radius/UDP message not visible in application debug logs ? Is it something to do with linux kernel ?</p><p>Any guidance would be really appreciated.</p><p>Thanks in advance !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '17, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p><span>Vijay Gharge</span><br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Feb '17, 11:25</strong> </span></p></div></div><div id="comments-container-59683" class="comments-container"></div><div id="comment-tools-59683" class="comment-tools"></div><div class="clear"></div><div id="comment-59683-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59689"></span>

<div id="answer-container-59689" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59689-score" class="post-score" title="current number of votes">0</div><span id="post-59689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Not enough room in packet for AVP</p></blockquote><p>This means that an AVP in the packet has a length that implies that the AVP goes past the end of the packet.</p><p>This presumably means either that 1) the packet required multiple TCP segments but was not reassembled for some reason or 2) the packet really <em>is</em> malformed. We'd have to see the packet (preferably in the form of a capture file, <em>NOT</em> a screenshot!) in order to figure out which of those is the case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '17, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-59689" class="comments-container"><span id="59690"></span><div id="comment-59690" class="comment"><div id="post-59690-score" class="comment-score"></div><div class="comment-text"><p>It is also possible that the traffic isn't radius at all if some other protocol is using the ports on which radius is expected.</p></div><div id="comment-59690-info" class="comment-info"><span class="comment-age">(26 Feb '17, 02:48)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="59694"></span><div id="comment-59694" class="comment"><div id="post-59694-score" class="comment-score"></div><div class="comment-text"><p>Thanks for response. Actually there was error in the analysis process itself. Instead of looking at /proc/net/udp6 we were concentrating on /proc/net/udp only. Radius clients and server communicate over IPv6. We noticed dropped packets in udp6 file. Thanks once again...</p></div><div id="comment-59694-info" class="comment-info"><span class="comment-age">(26 Feb '17, 12:31)</span> <span class="comment-user userinfo">Vijay Gharge</span></div></div><span id="59695"></span><div id="comment-59695" class="comment"><div id="post-59695-score" class="comment-score"></div><div class="comment-text"><p>Thanks for response. Actually there was error in the analysis process itself. Instead of looking at /proc/net/udp6 we were concentrating on /proc/net/udp only. Radius clients and server communicate over IPv6. We noticed dropped packets in udp6 file. Thanks once again...</p></div><div id="comment-59695-info" class="comment-info"><span class="comment-age">(26 Feb '17, 12:32)</span> <span class="comment-user userinfo">Vijay Gharge</span></div></div><span id="60165"></span><div id="comment-60165" class="comment"><div id="post-60165-score" class="comment-score">1</div><div class="comment-text"><p>The problem comes from the Radius header that indicates a length shorter than what it is in reality.</p><p>For example if you look at packet 2 you will see that the length indicated in Radius header is 58 bytes while UDP payload length is 186 bytes.</p></div><div id="comment-60165-info" class="comment-info"><span class="comment-age">(18 Mar '17, 12:44)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="60166"></span><div id="comment-60166" class="comment"><div id="post-60166-score" class="comment-score">1</div><div class="comment-text"><p>In other words, whatever software is sending those RADIUS packets is buggy, according to <a href="https://tools.ietf.org/html/rfc2865#section-3">RFC 2865, the RADIUS protocol specification</a>; it's not correctly filling in the Length field in the header.</p><p>Perhaps the application that received the packet silently dropped the packet, without logging it.</p></div><div id="comment-60166-info" class="comment-info"><span class="comment-age">(18 Mar '17, 18:27)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="60182"></span><div id="comment-60182" class="comment not_top_scorer"><div id="post-60182-score" class="comment-score"></div><div class="comment-text"><p>thanks for response. My source node (radius proxy) can decode it correctly. Do you suspect that it may be turning malformed as soon as it enters radius server ? How exactly I could troubleshoot this issue ? Do I need to provide any more information ? Besides, I want to know which exact element calculates radius length ? Is it source node i.e. radius proxy or destination server ?</p></div><div id="comment-60182-info" class="comment-info"><span class="comment-age">(19 Mar '17, 19:06)</span> <span class="comment-user userinfo">Vijay Gharge</span></div></div><span id="60184"></span><div id="comment-60184" class="comment not_top_scorer"><div id="post-60184-score" class="comment-score"></div><div class="comment-text"><blockquote><p>My source node (radius proxy) can decode it correctly.</p></blockquote><p>So do you mean that 1) Wireshark, when running on the source node and capturing traffic to and from the source node, can decode it correctly, or 2) the packet was sent to the RADIUS proxy running on the source node and it decodes the packet correctly, or 3) both?</p></div><div id="comment-60184-info" class="comment-info"><span class="comment-age">(19 Mar '17, 22:01)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-59689" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-59689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

