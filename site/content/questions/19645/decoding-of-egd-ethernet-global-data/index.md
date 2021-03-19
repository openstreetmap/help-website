+++
type = "question"
title = "Decoding of EGD (Ethernet Global Data)"
description = '''I have a couple of addresses in a PLC that I am writing to and reading from over Modbus TCP. However, the data itself is being sent on EGD. When I apply the filter for showing EGD, I can see the data packet (usually 88 bytes long) but I cannot make out anything of the content. Is there a way to diss...'''
date = "2013-03-19T07:44:00Z"
lastmod = "2013-03-19T10:07:00Z"
weight = 19645
keywords = [ "modbus", "udp", "tcp", "egd" ]
aliases = [ "/questions/19645" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding of EGD (Ethernet Global Data)](/questions/19645/decoding-of-egd-ethernet-global-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19645-score" class="post-score" title="current number of votes">0</div><span id="post-19645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a couple of addresses in a PLC that I am writing to and reading from over Modbus TCP. However, the data itself is being sent on EGD. When I apply the filter for showing EGD, I can see the data packet (usually 88 bytes long) but I cannot make out anything of the content. Is there a way to dissect the contents of the data packet and verify that data I send from my system is actually being sent correctly by reading the contents of the data packet? In that case, how do I do that (which filter and preferences do I use)?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-modbus" rel="tag" title="see questions tagged &#39;modbus&#39;">modbus</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-egd" rel="tag" title="see questions tagged &#39;egd&#39;">egd</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '13, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/706b38f9a5baee633ef9bbf8b5b49438?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dvu86&#39;s gravatar image" /><p><span>dvu86</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dvu86 has no accepted answers">0%</span></p></div></div><div id="comments-container-19645" class="comments-container"></div><div id="comment-tools-19645" class="comment-tools"></div><div class="clear"></div><div id="comment-19645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19648"></span>

<div id="answer-container-19648" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19648-score" class="post-score" title="current number of votes">0</div><span id="post-19648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You have Modbus/TCP being transported over EGD? If that is the case, the EGD dissector only shows the data content, it doesn't do any further dissection or make it available for other dissectors to use, e.g. Modbus/TCP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '13, 08:27</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-19648" class="comments-container"><span id="19649"></span><div id="comment-19649" class="comment"><div id="post-19649-score" class="comment-score"></div><div class="comment-text"><p>It is the other way around. Modbus/TCP shows only the transmission log (requests, acks etc.) while the EGD dissector contains the data in a HEX form. This HEX "dump" contains data from all the addresses I am sending to, and I asked if there is a way to decode this message to something that makes sense to me. For example being able to make out which addresses in the PLC are referred to, and what value I sent to them. Is this possible?</p><p>To simplify it, the data type I am looking for is a float (32 bit). How can I filter this from the HEX message in WireShark?</p></div><div id="comment-19649-info" class="comment-info"><span class="comment-age">(19 Mar '13, 08:33)</span> <span class="comment-user userinfo">dvu86</span></div></div><span id="19654"></span><div id="comment-19654" class="comment"><div id="post-19654-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>Modbus/TCP traffic is dissected to show all the data values as the protocol defines all the data types and the commands used to send them. EGD is a transport layer for the memory of a device and as such it's impossible to dissect unless you know the specific memory layout of the device transmitting the data.</p></div><div id="comment-19654-info" class="comment-info"><span class="comment-age">(19 Mar '13, 10:07)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-19648" class="comment-tools"></div><div class="clear"></div><div id="comment-19648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

