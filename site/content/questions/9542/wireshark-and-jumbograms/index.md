+++
type = "question"
title = "WireShark and Jumbograms"
description = '''Dear *, I&#x27;m currently investigating the effects of IPv6 Jumbograms on a network (IP packets of up to 4GiB). However, Wireshark does not seem to support packet sizes over IPv4&#x27;s maximum, 64k. I&#x27;ve already edited and recompiled libpcap and wireshark from source to allow a higher snaplen, but it seems ...'''
date = "2012-03-14T10:56:00Z"
lastmod = "2012-03-14T10:56:00Z"
weight = 9542
keywords = [ "jumbo", "jumbograms", "payload", "ipv6" ]
aliases = [ "/questions/9542" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WireShark and Jumbograms](/questions/9542/wireshark-and-jumbograms)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9542-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9542-score" class="post-score" title="current number of votes">1</div><span id="post-9542-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear *,</p><p>I'm currently investigating the effects of IPv6 Jumbograms on a network (IP packets of up to 4GiB). However, Wireshark does not seem to support packet sizes over IPv4's maximum, 64k.</p><p>I've already edited and recompiled libpcap and wireshark from source to allow a higher snaplen, but it seems that whenever I send a packet being &gt; 64k, the received data loops and restarts at 0. The length of the packet shows fine, but the received data somehow gets looped back. The maximum I can make it understand is around 65435, everything in the margin of 200 bytes around that value returns a Malformed Packet and if I send data in the regions of 70000, the received data on WireShark will be around 4000+ bytes.</p><p>I'm just wondering how WireShark is supporting Jumbograms and if there are any modifications I could make to the source to help me in making WireShark understand them :)</p><p>Greetz,</p><p>Jack</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-jumbo" rel="tag" title="see questions tagged &#39;jumbo&#39;">jumbo</span> <span class="post-tag tag-link-jumbograms" rel="tag" title="see questions tagged &#39;jumbograms&#39;">jumbograms</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span> <span class="post-tag tag-link-ipv6" rel="tag" title="see questions tagged &#39;ipv6&#39;">ipv6</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '12, 10:56</strong></p><img src="https://secure.gravatar.com/avatar/451b49e4c45290219260ec33c2dd7895?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jack&#39;s gravatar image" /><p><span>Jack</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jack has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Mar '12, 11:36</strong> </span></p></div></div><div id="comments-container-9542" class="comments-container"></div><div id="comment-tools-9542" class="comment-tools"></div><div class="clear"></div><div id="comment-9542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

