+++
type = "question"
title = "IP Total Length include Ethernet Header"
description = '''I am working with software that includes the Ethernet Header size (14 bytes) in the IPv4 Total Length value. I have read the IP RFC 791 and it should not be part of the IP Total Length, but I noticed that Wireshark is not upset with the message. Does anyone know why?'''
date = "2015-03-10T09:12:00Z"
lastmod = "2015-03-11T03:31:00Z"
weight = 40430
keywords = [ "ip", "length", "ethernet" ]
aliases = [ "/questions/40430" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IP Total Length include Ethernet Header](/questions/40430/ip-total-length-include-ethernet-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40430-score" class="post-score" title="current number of votes">0</div><span id="post-40430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working with software that includes the Ethernet Header size (14 bytes) in the IPv4 Total Length value. I have read the IP RFC 791 and it should not be part of the IP Total Length, but I noticed that Wireshark is not upset with the message.</p><p>Does anyone know why?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '15, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/830b04216abf0473f8ecf5fd6e4371ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blogzit&#39;s gravatar image" /><p><span>blogzit</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blogzit has no accepted answers">0%</span></p></div></div><div id="comments-container-40430" class="comments-container"><span id="40441"></span><div id="comment-40441" class="comment"><div id="post-40441-score" class="comment-score"></div><div class="comment-text"><p>Not only should the Ethernet header not be included in the IP Total Length, but the entire frame should be 18 bytes larger than the IP packet, not 14. Many systems strip off the Frame Check Sequence before Wireshark sees the packet, so we only see 14 bytes of Ethernet overhead, but the entire frame as transmitted on the wire is 18 bytes larger than the IP portion if both the Ethernet header and trailer are included.</p><p>Can you possibly upload some packets illustrating this, if they don't include confidential information? You can upload to <a href="https://appliance.cloudshark.org/">https://appliance.cloudshark.org/</a> and then post the link here.</p><p>And the obvious conclusion about why Wireshark is not upset would be that Wireshark is simply displaying the Total Length field, but not doing error checking on that field.</p></div><div id="comment-40441-info" class="comment-info"><span class="comment-age">(10 Mar '15, 09:58)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="40446"></span><div id="comment-40446" class="comment"><div id="post-40446-score" class="comment-score"></div><div class="comment-text"><p>Thank you for answering my question. Unfortunately the packet are proprietary.</p></div><div id="comment-40446-info" class="comment-info"><span class="comment-age">(10 Mar '15, 11:50)</span> <span class="comment-user userinfo">blogzit</span></div></div><span id="40464"></span><div id="comment-40464" class="comment"><div id="post-40464-score" class="comment-score"></div><div class="comment-text"><p>then it's obviously hard to help you.</p><blockquote><p>but I noticed that Wireshark is not upset with the message.</p></blockquote><p>what does that mean?</p></div><div id="comment-40464-info" class="comment-info"><span class="comment-age">(11 Mar '15, 03:31)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-40430" class="comment-tools"></div><div class="clear"></div><div id="comment-40430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

