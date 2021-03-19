+++
type = "question"
title = "how to extract email files."
description = '''Hi there, some files are sent to mail server (using SMTP port 25).if i captured them and save as test.pcapng,then how can i extract these files using wireshark? best regards, Kanan'''
date = "2014-04-05T14:45:00Z"
lastmod = "2014-06-02T03:59:00Z"
weight = 31557
keywords = [ "extracing" ]
aliases = [ "/questions/31557" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how to extract email files.](/questions/31557/how-to-extract-email-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31557-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there, some files are sent to mail server (using SMTP port 25).if i captured them and save as test.pcapng,then how can i extract these files using wireshark? best regards, Kanan</p></div><div id="question-tags" class="tags-container tags">extracing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '14, 14:45</strong></p><img src="https://secure.gravatar.com/avatar/530d52e3f448b515ad792be8d7e88021?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="warrior289&#39;s gravatar image" /><p>warrior289<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="warrior289 has no accepted answers">0%</span></p></div></div><div id="comments-container-31557" class="comments-container"></div><div id="comment-tools-31557" class="comment-tools"></div><div class="clear"></div><div id="comment-31557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="33265"></span>

<div id="answer-container-33265" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33265-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>NetworkMiner automatically extracts all email and attachments from a PCAP file. <a href="https://www.netresec.com/?page=Networkminer">https://www.netresec.com/?page=Networkminer</a></p><p><img src="http://www.netresec.com/images/NetworkMiner_Professional_1-0_Messages_hotmail_message.png" alt="NetworkMiner with extracted emails in &quot;Messages&quot; tab, extracted files are in the &quot;Files&quot; tab" /></p><p><em>NetworkMiner with extracted emails in "Messages" tab, extracted files are in the "Files" tab</em></p><p>You'll need to save the PCAP-NG file in the old PCAP format first though. You can do that from wireshark (use File &gt; Save As and select libpcap format in the File format drop down list).</p><p>You can also convert the PCAP-NG file to plain old PCAP over at <a href="http://pcapng.com">http://pcapng.com</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '14, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/f3f4e29f86f75cd52ba86565a658dcd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Netresec_LJ&#39;s gravatar image" /><p>Netresec_LJ<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Netresec_LJ has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jan '17, 23:00</p></div></div><div id="comments-container-33265" class="comments-container"><span id="59033"></span><div id="comment-59033" class="comment"><div id="post-59033-score" class="comment-score"></div><div class="comment-text"><p>I've captured the packets. NetworkMiner opens the file. I click on MESSAGES but nothing is there. If I go to cleartext I see one massive block of text with Emails. I have NetworkMiner 1.6.1. So if anyone else sees this same problem, you are not alone. Not sure what I'm missing. (PCAP is from a firewall and not Wireshark.)</p></div><div id="comment-59033-info" class="comment-info"><span class="comment-age">(24 Jan '17, 14:04)</span> Tim Naami</div></div><span id="59039"></span><div id="comment-59039" class="comment"><div id="post-59039-score" class="comment-score"></div><div class="comment-text"><p>@tim-naami Please use the latest version of NetworkMiner (currently 2.1.1), which has support for SMTP, POP3 and IMAP. Here's a blog that covers how to extract emails in more detail: <a href="http://netres.ec/?b=17124C4">http://netres.ec/?b=17124C4</a></p></div><div id="comment-59039-info" class="comment-info"><span class="comment-age">(24 Jan '17, 23:02)</span> Netresec_LJ</div></div></div><div id="comment-tools-33265" class="comment-tools"></div><div class="clear"></div><div id="comment-33265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31559"></span>

<div id="answer-container-31559" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31559-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the email was not encrypted, follow the TCP stream, copy the attachment - it will be in ASCII - and convert it with a Base64 decoder. Or use another software that can do it automatically.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '14, 15:54</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-31559" class="comments-container"></div><div id="comment-tools-31559" class="comment-tools"></div><div class="clear"></div><div id="comment-31559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31565"></span>

<div id="answer-container-31565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31565-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no <strong>simple</strong> way to extract files (attachments) sent through SMTP with Wireshark. If you want/need (semi) automatic way, you should probably check other tools, like those mentioned here</p><blockquote><p><a href="http://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961">http://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961</a></p></blockquote><p>or this one</p><blockquote><p><a href="https://code.google.com/p/nfex/">https://code.google.com/p/nfex/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '14, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Apr '14, 05:28</p></div></div><div id="comments-container-31565" class="comments-container"></div><div id="comment-tools-31565" class="comment-tools"></div><div class="clear"></div><div id="comment-31565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

