+++
type = "question"
title = "Schannel errors EventID 36888"
description = '''Hi, A Windows 2012 R2 server running Exchange 2013 started logging Schannel errors, which according to this post (http://blog.ittoby.com/2014/07/why-schannel-eventid-36888-36874-occurs.html) is a result of the cipher mismatch.  I am seeing RST packets in the LDAP communication between the exchange s...'''
date = "2016-06-23T14:02:00Z"
lastmod = "2016-06-24T02:14:00Z"
weight = 53634
keywords = [ "schannel", "ldap" ]
aliases = [ "/questions/53634" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Schannel errors EventID 36888](/questions/53634/schannel-errors-eventid-36888)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53634-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>A Windows 2012 R2 server running Exchange 2013 started logging Schannel errors, which according to this post (<a href="http://blog.ittoby.com/2014/07/why-schannel-eventid-36888-36874-occurs.html)">http://blog.ittoby.com/2014/07/why-schannel-eventid-36888-36874-occurs.html)</a> is a result of the cipher mismatch.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wsh.jpg" alt="alt text" /></p><p>I am seeing RST packets in the LDAP communication between the exchange server and the domain controller, where RST is sent by the DC to Exchange. Not sure if I grabbed the correct stream, but the time of the Windows Event with the schannel error matches the time stamp of the RST packet.</p><p>Should LDAP communication end with an RST packet?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">schannel ldap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '16, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jun '16, 14:56</p></div></div><div id="comments-container-53634" class="comments-container"></div><div id="comment-tools-53634" class="comment-tools"></div><div class="clear"></div><div id="comment-53634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53639"></span>

<div id="answer-container-53639" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53639-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Any application using TCP as transport may terminate the TCP session using RST to distinguish a "peaceful" termination from an emergency one.</p><p>But your screenshot doesn't indicate any cipher issue, as a cipher negotiation has to be successfully completed before the ciphered communication may start. In your case, LDAP exchange was already in progress and the RST came in response to LDAP <code>unbindRequest</code>, so the cipher negotiation phase has either completed successfully or no ciphering is used.</p><p>So I'd suspect something else to be broken, either at the DC side or with the contents of the <code>unbindRequest</code> sent by the Exchange. As you have provided a screenshot rather than a capture file (which has to be uploaded to Cloudshark or any file sharing service and a link for login-free access to it has to be placed here if you want to share it), there is little more anyone here could tell until you post the capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '16, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53639" class="comments-container"><span id="53640"></span><div id="comment-53640" class="comment"><div id="post-53640-score" class="comment-score"></div><div class="comment-text"><p>Thanks sindy.</p><p>I am wondering now if there is an issue at all? unbindRequest is a signlal to the directory server from exchange server that it is about to close its connection. DC sends an RST and the connection is peacefully closed.</p></div><div id="comment-53640-info" class="comment-info"><span class="comment-age">(24 Jun '16, 06:12)</span> net_tech</div></div><span id="53647"></span><div id="comment-53647" class="comment"><div id="post-53647-score" class="comment-score"></div><div class="comment-text"><p>I don't know whether there is an issue from user point of view. From protocol point of view, there definitely is: if the contents of the LDAP <code>unbindRequest</code> was OK, the DC should have responded it with a proper LDAP response, and then maybe terminate the TCP session using FIN, but surely not using RST. As said, RST is reserved for emergency termination of a session.</p></div><div id="comment-53647-info" class="comment-info"><span class="comment-age">(24 Jun '16, 14:16)</span> sindy</div></div><span id="53648"></span><div id="comment-53648" class="comment"><div id="post-53648-score" class="comment-score"></div><div class="comment-text"><p>There may also be an issue at client side at TCP level, but as also already said, this can be found from capture file but not from a screenshot.</p></div><div id="comment-53648-info" class="comment-info"><span class="comment-age">(24 Jun '16, 14:34)</span> sindy</div></div><span id="53699"></span><div id="comment-53699" class="comment"><div id="post-53699-score" class="comment-score"></div><div class="comment-text"><p>Users are not reporting any issues that are related to Schannel errors. What packet would be of interest to you? Not sure I could post the entire stream without revealing too much of corporate information.</p><p>here is the last 4 packets</p><p><a href="https://www.cloudshark.org/captures/2ffe4ec37b5a">https://www.cloudshark.org/captures/2ffe4ec37b5a</a></p></div><div id="comment-53699-info" class="comment-info"><span class="comment-age">(28 Jun '16, 10:56)</span> net_tech</div></div><span id="53716"></span><div id="comment-53716" class="comment"><div id="post-53716-score" class="comment-score"></div><div class="comment-text"><p>I was suspecting that the reason for RST could have been that the TCP window size announced in the packet carrying the <code>unbindRequest</code> was zero so the answer would not fit, but your capture shows it is not the case.</p><p>As the LDAP payload cannot be decrypted from this 4-packet capture, can you add to the Question (as pictures in comments destroy page layout) a screenshot of the fully expanded dissection of the LDAP part of the <code>unbindRequest</code> packet (the one right before the RST)?</p></div><div id="comment-53716-info" class="comment-info"><span class="comment-age">(29 Jun '16, 03:35)</span> sindy</div></div><span id="53734"></span><div id="comment-53734" class="comment not_top_scorer"><div id="post-53734-score" class="comment-score"></div><div class="comment-text"><p>Sure</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ldapp.jpg" alt="alt text" /></p></div><div id="comment-53734-info" class="comment-info"><span class="comment-age">(29 Jun '16, 12:48)</span> net_tech</div></div><span id="53736"></span><div id="comment-53736" class="comment not_top_scorer"><div id="post-53736-score" class="comment-score"></div><div class="comment-text"><p>OK, I give up. There are no parameters to <code>unbindRequest</code> and Wireshark doesn't claim any error of SASL. So nothing at TCP or LAPD level suggests why the server should send a TCP RST rather than a regular response to the <code>unbindRequest</code>.</p></div><div id="comment-53736-info" class="comment-info"><span class="comment-age">(29 Jun '16, 13:57)</span> sindy</div></div></div><div id="comment-tools-53639" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-53639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

