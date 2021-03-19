+++
type = "question"
title = "Completely lost on this TCP FTP issue."
description = '''My system in Florida cannot ftp to ftp.childnet.us.  It can ftp to other sites, i.e. ftp.bnl.gov I can ftp to ftp.childnet.us from outside of our network. I&#x27;ve done about everything I can think of to troubleshoot this. Here&#x27;s what&#x27;s going on exactly. 1) launch the command:   C:&#92;Windows&#92;system32&amp;gt;f...'''
date = "2013-07-13T09:07:00Z"
lastmod = "2013-07-13T16:19:00Z"
weight = 22928
keywords = [ "rst", "ftp", "ack" ]
aliases = [ "/questions/22928" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Completely lost on this TCP FTP issue.](/questions/22928/completely-lost-on-this-tcp-ftp-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22928-score" class="post-score" title="current number of votes">0</div><span id="post-22928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My system in Florida cannot ftp to ftp.childnet.us.<br />
</p><p>It can ftp to other sites, i.e. ftp.bnl.gov</p><p>I can ftp to ftp.childnet.us from outside of our network.</p><p>I've done about everything I can think of to troubleshoot this. Here's what's going on exactly.</p><p>1) launch the command:<br />
</p><p>C:\Windows\system32&gt;ftp ftp.childnet.us</p><p>2) Our systems do a 3-way TCP handshake:</p><pre><code>96  4.871876000 192.168.180.12  65.240.236.154  TCP 66  51337 &gt; ftp [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=1 SACK_PERM=1
97  4.901984000 65.240.236.154  192.168.180.12  TCP 66  ftp &gt; 51337 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1420 WS=256
SACK_PERM=1
98  4.902033000 192.168.180.12  65.240.236.154  TCP 54  51337 &gt; ftp [ACK] Seq=1 Ack=1 Win=8192 Len=0</code></pre><p>That results in the following display in the ftp screen:</p><p>Connected to ftp.childnet.us.</p><p>3) But then something goes wrong. The next packet is this:</p><pre><code>99  4.930141000 65.240.236.154  192.168.180.12  TCP 60  ftp &gt; 51337 [RST, ACK] Seq=1 Ack=1 Win=0 Len=0</code></pre><p>That is Childnet resetting the connection. it results in the following message on screen:</p><p>Connection closed by remote host.</p><p>And that's that. Nothing is possible.</p><p>I've been banging my head to figure this one out for quite a while. I'm open to any ideas here.</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span> <span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '13, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/369b9297ce256a1171a6a0c742aeddf0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="meatstack&#39;s gravatar image" /><p><span>meatstack</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="meatstack has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-22928" class="comments-container"><span id="22929"></span><div id="comment-22929" class="comment"><div id="post-22929-score" class="comment-score">1</div><div class="comment-text"><p>what is the ip.ttl of the rst packet? is it the same as the syn_ack?</p></div><div id="comment-22929-info" class="comment-info"><span class="comment-age">(13 Jul '13, 09:49)</span> <span class="comment-user userinfo">mrEEde2</span></div></div></div><div id="comment-tools-22928" class="comment-tools"></div><div class="clear"></div><div id="comment-22928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22931"></span>

<div id="answer-container-22931" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22931-score" class="post-score" title="current number of votes">2</div><span id="post-22931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just a guess, but I have seen behavior like this on the FTP command channel when the client IP address (in this case your public NAT address) was listed on a blacklist, or, depending on how the server is set up, NOT part of the whitelist. The FTP server learns about the connection attempt right after the stack finished the three way handshake, compares your public IP to the list of allowed clients and closes the socket when it is not allowed. This results in a Reset packet coming from the server right after the handshake.</p><p>Update: looks like the PC from where you're not able to connect is on a blacklist (or the public IP range is, for whatever reason), since I can connect to their FTP service just fine.</p><p>Advice: contact the FTP server admin, give him your public IP and ask, why you're being refused.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '13, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jul '13, 14:32</strong> </span></p></div></div><div id="comments-container-22931" class="comments-container"><span id="22937"></span><div id="comment-22937" class="comment"><div id="post-22937-score" class="comment-score"></div><div class="comment-text"><p>I connected to the site and entered <strong>5 times a wrong user/password</strong>. My 6th connection (and all thereafter) received a RESET. I guess I'm now banned by their FTP server forever ;-))</p><p><span></span><span>@meatstack</span>: Please follow the advice of <span></span><span>@Jasper</span> and contact the admin of that system. Maybe one of your users (or you) did the same I did ;-))</p><p>UPDATE: And here is the online help for that nice feature :-)</p><blockquote><p><a href="http://help.globalscape.com/help/eft6-2/mergedprojects/eft/banning_an_ip_address_that_uses_an_invalid_account.htm">http://help.globalscape.com/help/eft6-2/mergedprojects/eft/banning_an_ip_address_that_uses_an_invalid_account.htm</a></p></blockquote><p>Regards<br />
Kurt</p></div><div id="comment-22937-info" class="comment-info"><span class="comment-age">(13 Jul '13, 16:19)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-22931" class="comment-tools"></div><div class="clear"></div><div id="comment-22931-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22930"></span>

<div id="answer-container-22930" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22930-score" class="post-score" title="current number of votes">0</div><span id="post-22930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Perhaps you need to use passive ftp mode?</p><p>See also <a href="http://ask.wireshark.org/questions/22585/question-about-passive-ftp">http://ask.wireshark.org/questions/22585/question-about-passive-ftp</a> and the various links in the answers to that question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '13, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></p></div></div><div id="comments-container-22930" class="comments-container"></div><div id="comment-tools-22930" class="comment-tools"></div><div class="clear"></div><div id="comment-22930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

