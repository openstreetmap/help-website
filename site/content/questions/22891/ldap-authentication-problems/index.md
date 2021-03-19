+++
type = "question"
title = "LDAP authentication problems"
description = '''hi guys, I have pretty much the same issue. I have a SERVER (.129) authenticating to an LDAP SERVER (.53) Sometimes works, sometimes it does not. I am checking it, and: SOURCE DESTINATION PROTOCOL INFO  .129 .53 TCP ldaps [FIN, ACK]  .53 .129 TLSv1 Encrypted alert .129 .53 TCP ldaps [RST]  .53 .129 ...'''
date = "2013-07-12T01:49:00Z"
lastmod = "2013-07-12T02:51:00Z"
weight = 22891
keywords = [ "authentication", "ldap" ]
aliases = [ "/questions/22891" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LDAP authentication problems](/questions/22891/ldap-authentication-problems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22891-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi guys,</p><p>I have pretty much the same issue. I have a SERVER (.129) authenticating to an LDAP SERVER (.53)</p><p>Sometimes works, sometimes it does not.</p><p>I am checking it, and:</p><pre><code>SOURCE    DESTINATION         PROTOCOL         INFO

.129      .53                 TCP              ldaps [FIN, ACK]    
.53       .129                TLSv1            Encrypted alert
.129      .53                 TCP              ldaps [RST]    
.53       .129                TCP              ldaps [FIN, ACK]    
.129      .53                 TCP              ldaps [RST]
</code></pre><p>Any comment is very welcome :)</p><p>HINT: I converted your comment/answer to a <a href="http://ask.wireshark.org/questions/14212/router-replies-with-rst-after-fin-ack">question</a>, as it's better to handle your request in a new question, instead of the original question: <a href="http://ask.wireshark.org/questions/14212/router-replies-with-rst-after-fin-ack">http://ask.wireshark.org/questions/14212/router-replies-with-rst-after-fin-ack</a> (Kurt)</p></div><div id="question-tags" class="tags-container tags">authentication ldap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '13, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/e4d961b4bdd510b1020fd8c3c4d9b236?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dora&#39;s gravatar image" /><p>dora<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dora has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jul '13, 03:11</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-22891" class="comments-container"></div><div id="comment-tools-22891" class="comment-tools"></div><div class="clear"></div><div id="comment-22891-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22899"></span>

<div id="answer-container-22899" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22899-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>.129 .53 TCP ldaps [FIN, ACK]<br />
</p></blockquote><p>This is not necessarily a network (or IP stack) problem, as the LDAP client (server .129) actively closes the connection. So, to figure out what's going on, you need insight into the (clear text) communication.</p><p>So, here are some questions:</p><ol><li>Do you have access to the private key of the LDAP server, to decrypt the comminication?</li><li>In the 'good' case, how many packets are being exchanged between the systems?</li><li>In the 'bad' case, how many packets are being exchanged between the systems?</li><li>What type of LDAP server is this (OpenLDAP, Active Directory, ...)?</li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '13, 02:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-22899" class="comments-container"><span id="23070"></span><div id="comment-23070" class="comment"><div id="post-23070-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for creating another post. I was waiting for an email from Wireshark.org advising of the new comment in the old thread (your comment, Kurt), but never came up (possibly because a new thread was created). I am new to here, but this forum looks pretty cool. I am getting really hooked to Whireshark :)</p><p>Anyhow:</p><ol><li>Waiting...</li><li>Working on it...</li><li>Working on it...</li><li>Open LDAP</li></ol><p>The thing is, that this was working ok when the servers were phisycal servers, but now they a Virtual machines (Vmware), since then, they face this issue.</p></div><div id="comment-23070-info" class="comment-info"><span class="comment-age">(17 Jul '13, 05:23)</span> dora</div></div><span id="23072"></span><div id="comment-23072" class="comment"><div id="post-23072-score" class="comment-score"></div><div class="comment-text"><p>Here we have an example when LDAP authentification does not work. This is TCPDUMP running on 10.X.X.129, listening to port 636</p><p><img src="https://osqa-ask.wireshark.org/upfiles/failure_1.jpg" alt="alt text" /></p></div><div id="comment-23072-info" class="comment-info"><span class="comment-age">(17 Jul '13, 06:48)</span> dora</div></div><span id="23075"></span><div id="comment-23075" class="comment"><div id="post-23075-score" class="comment-score">1</div><div class="comment-text"><p>BTW: if you want to skip the encryption (because you can't get the keys easy) and want to capture the traffic visible to you without the keys you can use DavMail:</p><p><a href="http://davmail.sourceforge.net/index.html">http://davmail.sourceforge.net/index.html</a></p><p>It's an open source gateway for services like POP/IMAP/SMTP/Caldav/Carddav/<strong><em>LDAP</em></strong>.</p><p>The client/server communication will still be encrypted but you will capture the unencrypted traffic locally:</p><p>10.X.X.129 ---unencrypted traffic ---&gt; 10.X.X.129:1636 ---encrypted traffic---&gt; 10.X.X.53:636</p><p>tcpdump on port 1636 will give you some hints.</p></div><div id="comment-23075-info" class="comment-info"><span class="comment-age">(17 Jul '13, 11:09)</span> Edmond</div></div><span id="23085"></span><div id="comment-23085" class="comment"><div id="post-23085-score" class="comment-score"></div><div class="comment-text"><p>what is the sort order of the packets in your screenshot?</p></div><div id="comment-23085-info" class="comment-info"><span class="comment-age">(17 Jul '13, 15:41)</span> Kurt Knochner ♦</div></div><span id="23093"></span><div id="comment-23093" class="comment"><div id="post-23093-score" class="comment-score"></div><div class="comment-text"><p>Edmond, Thank you. Will check out ASAP.</p><p>Kurt, Thank you. I just ran TCPDUMP on port 636 in the Server (client), no in the LDAP Server. Then I tried to authenticate, and it failed (it failed at the first attempt, therefore I stopped TCPDUMP)). This is all I got. Just few packets.</p></div><div id="comment-23093-info" class="comment-info"><span class="comment-age">(17 Jul '13, 23:37)</span> dora</div></div><span id="23094"></span><div id="comment-23094" class="comment not_top_scorer"><div id="post-23094-score" class="comment-score"></div><div class="comment-text"><p>BTW, I believe, that the failing Servers (clients), since they are Vmware machines, are adding some wrong info to the TCP handshake. It is pretty weird, cause after not using the server for some time (hours), sometimes it works at the first attempt, and sometimes it does not. Like TCP FIN timeout is not steady.</p></div><div id="comment-23094-info" class="comment-info"><span class="comment-age">(17 Jul '13, 23:41)</span> dora</div></div><span id="23097"></span><div id="comment-23097" class="comment not_top_scorer"><div id="post-23097-score" class="comment-score"></div><div class="comment-text"><p>@dora Your "answers" have been converted to comments as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-23097-info" class="comment-info"><span class="comment-age">(18 Jul '13, 01:06)</span> grahamb ♦</div></div><span id="23102"></span><div id="comment-23102" class="comment not_top_scorer"><div id="post-23102-score" class="comment-score"></div><div class="comment-text"><p>@dora: some suggestions:</p><ul><li><p>How do you authenticate against the LDAP server? Is that something built into an application? Until you get the server key, can you check the logs of the application for any errors?</p></li><li><p>How did you virtualize the systems?</p></li><li>How is the networking for the virtual systems configured (e.g. <strong>bridged</strong> interfaces, NAT, etc.)?</li><li>Is it possible to post the whole communication as a pcap file somewhere (Google Drive, dropbox, etc.)? We would need a capture file for the "good" case and for the "bad" case.</li></ul></div><div id="comment-23102-info" class="comment-info"><span class="comment-age">(18 Jul '13, 04:57)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-22899" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-22899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

