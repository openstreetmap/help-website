+++
type = "question"
title = "SMB performance and extra SMB commands appearing"
description = '''Hi folks, We have a performance problem with one of our servers that reads thousands of small XML files from a SMB share and then stitches them together in to a collection of slightly bigger files on the local drive. The problem server can only manage to process about 1 XML file every 2 secs when it...'''
date = "2013-10-03T08:01:00Z"
lastmod = "2015-07-08T04:38:00Z"
weight = 25592
keywords = [ "performance", "trans", "nt", "smb" ]
aliases = [ "/questions/25592" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [SMB performance and extra SMB commands appearing](/questions/25592/smb-performance-and-extra-smb-commands-appearing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25592-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks,</p><p>We have a performance problem with one of our servers that reads thousands of small XML files from a SMB share and then stitches them together in to a collection of slightly bigger files on the local drive. The problem server can only manage to process about 1 XML file every 2 secs when it used to be doing 10s of files every second.</p><p>Running a fixed test and wiresharking the SMB conversation going on the server that is performing very slowly I can see according to SMB service response times the following:</p><ul><li>Trans2 = 12486 packets @ avg 0.007687</li><li>NT Trans = 8936 @ avg 0.007187</li><li>Close = 5585 @ avg 0.006872</li><li>NT Create AndX = 5585 @ avg 0.006897</li><li>Read AndX = 1834 @ avg 0.007608</li></ul><p>On another server that performs many times faster:</p><ul><li>Trans2 = 3376 @ avg 0.001545</li><li>Read AndX = 1833 @ avg 0.000811</li><li>Close = 187 @ avg 0.000225</li><li>NT Create AndX = 187 @ avg 0.000228</li></ul><p>Given that the same test (using the exact same XML files) has been run on both machines, I'd have expected roughly similar number of SMB commands/packets being sent but you can see on my poorly performing server there are several times more of every command and there are two extra commands which are appearing: NT Trans and also under the Trans2 sub-commands I'm seeing "QUERY FILE INFO" which I don't see on the server that performs well.</p><p>Is there an obvious reason why I should see so much more traffic going on for the same test and why am I seeing lots of "NT QUERY SECURITY DESC" commands? I should add that my Wireshark cap filter is limited to just the server I'm pulling the files from and I get the same results over and over.</p><p>Access to the share from both machines is the same too. I have tried the same test on a variety of servers and all of the others I have tested show the same results as the server that performs well.</p><p>These particular servers are both Windows 2003. I have checked SMB signing is off for both and other lanmanworkstation settings are the same from what I can see in the registry. I don't believe network performance is the issue because I've carried out a test using FTP instead.</p><p>Any help would be greatly appreciated.</p><p>Cheers</p><p>Sam</p></div><div id="question-tags" class="tags-container tags">performance trans nt smb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '13, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/a011be3874d7902d8904b8e239bdd201?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="billbofagends&#39;s gravatar image" /><p>billbofagends<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="billbofagends has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Oct '13, 08:03</p></div></div><div id="comments-container-25592" class="comments-container"></div><div id="comment-tools-25592" class="comment-tools"></div><div class="clear"></div><div id="comment-25592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="43959"></span>

<div id="answer-container-43959" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43959-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Long time since I asked this question I know but we have finally resolved the issue. The server in question is VMWare virtual machine on ESXi 5.0 and has VMWare tools installed. Part of VMware tools includes shared folders. After removing VMWare tools and then reinstalling without shared folders included, the issue was fixed and performance was restored. Pretty obscure but have proved this on quite a few other servers now. Hope this helps someone else out!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '15, 04:38</strong></p><img src="https://secure.gravatar.com/avatar/a011be3874d7902d8904b8e239bdd201?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="billbofagends&#39;s gravatar image" /><p>billbofagends<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="billbofagends has no accepted answers">0%</span></p></div></div><div id="comments-container-43959" class="comments-container"></div><div id="comment-tools-43959" class="comment-tools"></div><div class="clear"></div><div id="comment-43959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25605"></span>

<div id="answer-container-25605" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25605-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Does the bad-performing system use a (different) virus scanner or the same virus scanner with a different configuration? I have seen virus scanners introduce a lot of extra SMB calls.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '13, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-25605" class="comments-container"><span id="25634"></span><div id="comment-25634" class="comment"><div id="post-25634-score" class="comment-score"></div><div class="comment-text"><p>Good shout. We have Symantec installed on all our machines now and I have tried disabling it but it didn't help. After further poking around with it, however, you can config it to ignore certain folders etc which would be worth trying. I don't have privileges to do this by the look of it but I shall get it checked out. Cheers :-)</p></div><div id="comment-25634-info" class="comment-info"><span class="comment-age">(04 Oct '13, 03:22)</span> billbofagends</div></div></div><div id="comment-tools-25605" class="comment-tools"></div><div class="clear"></div><div id="comment-25605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25613"></span>

<div id="answer-container-25613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25613-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On the poorly performing server check if it is doing additional lookups to other servers in your environment, while your main transactions occurring. For instance it might be checking credentials with your domain controller or doing DNS lookups (that the other servers aren't). This might point to a configuration issues, inadequate authentication credentials or somee such that is putting additional overhead and latency on your transaction.</p><p>The best may to measure network-oriented performance is looking at the SYN to SYN-ACK response time from the client. Normal this is done at the kernel level in the server and hence isn't very load dependent. And again measure close to the server to eliminate link latency.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '13, 16:30</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-25613" class="comments-container"></div><div id="comment-tools-25613" class="comment-tools"></div><div class="clear"></div><div id="comment-25613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

