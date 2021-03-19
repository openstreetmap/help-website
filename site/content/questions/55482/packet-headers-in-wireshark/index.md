+++
type = "question"
title = "Packet headers in wireshark"
description = '''I am dealing with ROHC(RObust Header Compression) ,in voip . Can anyone tell me that how to check that header of packets in communication are well formed through wireshark ? also want to know whether Kernel or OS is going to attached any own headers in packet passing through network ?'''
date = "2016-09-12T03:46:00Z"
lastmod = "2016-09-12T09:11:00Z"
weight = 55482
keywords = [ "kernel", "headers", "packets", "wireshark" ]
aliases = [ "/questions/55482" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packet headers in wireshark](/questions/55482/packet-headers-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55482-score" class="post-score" title="current number of votes">0</div><span id="post-55482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am dealing with ROHC(RObust Header Compression) ,in voip . Can anyone tell me that how to check that header of packets in communication are well formed through wireshark ? also want to know whether Kernel or OS is going to attached any own headers in packet passing through network ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-kernel" rel="tag" title="see questions tagged &#39;kernel&#39;">kernel</span> <span class="post-tag tag-link-headers" rel="tag" title="see questions tagged &#39;headers&#39;">headers</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '16, 03:46</strong></p><img src="https://secure.gravatar.com/avatar/fe46f9a9147da796d172745b5d4fe71d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="avani%20badheka&#39;s gravatar image" /><p><span>avani badheka</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="avani badheka has no accepted answers">0%</span></p></div></div><div id="comments-container-55482" class="comments-container"><span id="55491"></span><div id="comment-55491" class="comment"><div id="post-55491-score" class="comment-score"></div><div class="comment-text"><p>On what type of link do you capture?</p><p>Is it in a LTE context? If yes, have you seen the Answer to <a href="https://ask.wireshark.org/questions/50505/how-to-see-rohc-decoded-data-in-wireshark">this Question</a>?</p><p>Which kernel or OS you suspect to be adding headers while "a packet is passing through the network"? ROHC is used on a point-to-point link (physical or virtual) and the recipient has to decompress the header to be able to route the packet, but if it does not need to change the header contents, it may theoretically forward the compressed packet without modification if the forward link is also configured as a ROHC one.</p></div><div id="comment-55491-info" class="comment-info"><span class="comment-age">(12 Sep '16, 09:11)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-55482" class="comment-tools"></div><div class="clear"></div><div id="comment-55482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

