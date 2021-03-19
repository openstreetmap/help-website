+++
type = "question"
title = "Help Analyzing for LDAP/Active Directory Errors"
description = '''Hello - I am a very new user to Wireshark and definitely have no experience in reading or interpreting the capture files. I am working with a client to find out why an application fails to return/authenticate a user accouunt when installing this application. The server the application is being insta...'''
date = "2011-05-03T05:49:00Z"
lastmod = "2011-05-05T05:44:00Z"
weight = 3898
keywords = [ "capture", "analyze", "ldap" ]
aliases = [ "/questions/3898" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Help Analyzing for LDAP/Active Directory Errors](/questions/3898/help-analyzing-for-ldapactive-directory-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3898-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello - I am a very new user to Wireshark and definitely have no experience in reading or interpreting the capture files.</p><p>I am working with a client to find out why an application fails to return/authenticate a user accouunt when installing this application.</p><p>The server the application is being installed on is a member server and I am sure there are errors when calling to the Domain Controller. I have done NSLOOKUPS, NETDOM Verify etc tests and have had some failures.</p><p>The network department for the client will not offer help until I PROVE thier network is the issue.</p><p>The system is a VM system, Windows 2003 server. The network lan is said to be open, no ACL's no port blocks, all routing supposedly correct. All DNS servers supposedly have all SRV records.</p><p>So I installed Wireshark and performed the installation of the application with the capture running. I am not sure how to identify the exact information I am looking for.</p><p>I have looked through the file and can see some things that look to be some kind of issues with ldap/api calls, but I am not sure.</p><p>I would appreciate some help in interpreting this file for my own education and to also give the client's network team specific details of the issues/errors in preventing the system from properly reaching or returning information from the Active Directory.</p><p>With Sincere Gratitude. Alina</p></div><div id="question-tags" class="tags-container tags">capture analyze ldap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '11, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/1f0da09274caca9f27e5c0e9d5a26271?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bluewiskie&#39;s gravatar image" /><p>Bluewiskie<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bluewiskie has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 May '11, 05:50</p></div></div><div id="comments-container-3898" class="comments-container"></div><div id="comment-tools-3898" class="comment-tools"></div><div class="clear"></div><div id="comment-3898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="3910"></span>

<div id="answer-container-3910" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3910-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your posting sounds like a several consulting jobs that we did: "It's the network." Now, in most case it was <em>not</em> the network.</p><p>If a Windows domain member (workstation or server) authenticates a user against the AD you would look for Kerberos problems. Now, Kerberos can (and will) show error codes like "Response too big". This is an error that can be ignored, as it tells the Kerberos how to talk to the Kerberos server. The more interesting messages would be "Client Principal unknown" or "Server Principal unknown". Kerberos error messages are easy to find with the display filter <strong>kerberos.msg.type == 30</strong></p><p>If you suspect a problem with LDAP you want to apply the display filter <strong>ldap</strong> Analyzing LDAP is not that easy: Depending on your application you will see a bunch of queries. For example when a system boots it searches for information at a specific point and gets less specific with more queries, say first look for policies for a site, then for the domain.</p><p>When analyzing your application's LDAP traffic you should understand the LDAP calls made by your application. Alas, we often talk to programmers who don't know what their application is doing to the network (or servers).</p><p>Here are a few ideas if you suspect that something is going wrong with LDAP:</p><ul><li>Do you get LDAP error messages?</li><li>Do you get no results (Wireshark would show "[0 results]") from your query?</li><li>If yes: Do you know, why you did not get any results (Just because no information was there, or was it because the query was not properly written)</li><li>Do you make the same queries over and over again?</li><li>If yes: Can you cache the results?</li><li>How fast are your LDAP servers (Statistics -&gt; Service Response Time -&gt; LDAP)</li></ul><p>It is probably a good idea to compare your trace with a "known good" sample. If you suspect that something is misconfigured take another trace in your lab and find out where your client installation goes a different path - and find out why (is it a policy thing, a network thing or somehting else).</p><p>Good hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '11, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-3910" class="comments-container"></div><div id="comment-tools-3910" class="comment-tools"></div><div class="clear"></div><div id="comment-3910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3935"></span>

<div id="answer-container-3935" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3935-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Kerberos snippets from your posting already hint at a few problems:</p><ul><li>The Kerberos errors "bad option" are usually related to the flag "Constrained delegation" in the request. Constrained delegation has to be configured on the client and/or server principal (i. e. the user or application account)</li><li>The Kerberos error "S_PRINCIPAL_UNKNOWN" (Server principal unknown) shows that the Kerberos server does not know about the service for which it should issue a ticket.</li><li>The "Response too big" is just to force the protocol from UDP to TCP and no problem at all, as long as a proper TCP session follows.</li></ul><p>The big thing here is the Server principal. Most common reasons are:</p><ol><li>A host name is misspelled</li><li>The target host is addressed by IP address, not by host name</li><li>The target server is not a domain member</li><li>The target application is not "kerberized" (i. e. not properly configured in the domain so the KRB server can not issue a ticket)</li></ol><p>The trace might contain sensitive information like passwords, password hashes, e-Mails or other confidential information. Before posting or otherwise publishing the trace file I recommend to get a written permission (at least per e-mail).</p><p>Also, please bear in mind that a thorough analysis of a 200 MB trace is a small project in itself and is hardly done as a freebee.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '11, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-3935" class="comments-container"></div><div id="comment-tools-3935" class="comment-tools"></div><div class="clear"></div><div id="comment-3935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3914"></span>

<div id="answer-container-3914" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3914-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello and Thank you for your response.</p><p>I actually did perform the trace on a good environment where we are a member server and I did good returns on my NETDOM verify calls and GETUSER Info tests, etc.</p><p>And I don't see any of the same information I see on the site that is giving me issues, so I know something is not allowing our API/LDAP calls to perform correctly.</p><p>I was able to do some more digging and found another analyzer that helped group the issues found in a better format for reviewing.</p><p>There were a number of SMB issues and I did spot the Kerberos issues that I am not familiar with.</p><p>false 132 172.16.3.75 165.6.3.109 190 KRB5 KRB Error: KRB5KDC_ERR_BADOPTION NT Status: STATUS_NOT_SUPPORTED 1.556517000 0.000619000 2011-05-03 09:18:07.850668000</p><p>false 558 172.16.3.75 165.6.3.109 147 KRB5 KRB Error: KRB5KDC_ERR_S_PRINCIPAL_UNKNOWN 33.172496000 0.000009000 2011-05-03 09:18:39.466647000</p><p>false 4322 172.16.3.75 165.6.3.109 124 KRB5 KRB Error: KRB5KRB_ERR_RESPONSE_TOO_BIG 63.545952000 0.001478000 2011-05-03 09:19:09.840103000</p><p>Considering it's a 200mb capture file I am not sure I can upload it on to this thread for full review.</p><p>I am still searching to check what these specific entries mean, but any help would be greatly appreciated!!</p><p>Thank you again. Alina.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '11, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/1f0da09274caca9f27e5c0e9d5a26271?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bluewiskie&#39;s gravatar image" /><p>Bluewiskie<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bluewiskie has no accepted answers">0%</span></p></div></div><div id="comments-container-3914" class="comments-container"></div><div id="comment-tools-3914" class="comment-tools"></div><div class="clear"></div><div id="comment-3914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

