+++
type = "question"
title = "Automated TCP Reassembler?"
description = '''Hello fellow Wireshark Ninjas, I have been thinking about making a plugin for Wireshark (LUA) that automatically parses through a PCAP file, reassembles any known file types by file header details, and then saves them in a directory. Any ideas on how to get started? I have successfully created a few...'''
date = "2013-04-01T15:34:00Z"
lastmod = "2013-07-06T15:21:00Z"
weight = 19995
keywords = [ "reassembly", "script", "lua", "automation" ]
aliases = [ "/questions/19995" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Automated TCP Reassembler?](/questions/19995/automated-tcp-reassembler)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19995-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello fellow Wireshark Ninjas,</p><p>I have been thinking about making a plugin for Wireshark (LUA) that automatically parses through a PCAP file, reassembles any known file types by file header details, and then saves them in a directory. Any ideas on how to get started? I have successfully created a few LUA scripts, one even sets up the proper directories for the files I wish to reassemble. My problem is the API and if it is/isn't possible to call a dissector already? Or if something already exists that does this? Or maybe even some example code of someone automating TCP reassembler?</p><p>Ideally, I would like to run this script over a pcap file capture from a gateway that allows me to reconstruct websites entirely offline. Or something can capture and rebuild an FTP stream to check for sensitive data leaving my network. I think it would be a wickedly sweet plugin. Sadly, it is shaping up to be a beast with my lack of wireshark LUA API knowhow.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">reassembly script lua automation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '13, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/6f40a438bd6cf5fc655e25a757ed867b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="T3CHKOMMIE&#39;s gravatar image" /><p>T3CHKOMMIE<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="T3CHKOMMIE has no accepted answers">0%</span></p></div></div><div id="comments-container-19995" class="comments-container"></div><div id="comment-tools-19995" class="comment-tools"></div><div class="clear"></div><div id="comment-19995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="19996"></span>

<div id="answer-container-19996" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19996-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Save yourself the trouble, unless you have something very specific in mind. Wireshark can already export files for HTTP and SMB (See the export functionality in the file menu), and with the "Follow TCP Stream" functionality you can also pull files from FTP transfers if done correctly.</p><p>If you're trying to code a payload extraction plugin you need to consider that you'll have to do that for the protocol above TCP. For example: if you want to extract a file that is an attachment sent via SMTP you need to code it exactly so that it does SMTP payload extraction. TCP payload extraction won't help at all since you'd also get the SMTP protocol layer in your extracted payload, and that will not work.</p><p>And, by the way, there are lots of tools out there who dig content out of tracefiles already, e.g here: <a href="https://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961">https://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '13, 15:42</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Apr '13, 15:48</p></div></div><div id="comments-container-19996" class="comments-container"><span id="19998"></span><div id="comment-19998" class="comment"><div id="post-19998-score" class="comment-score"></div><div class="comment-text"><p>Ah, export object http functionality. That's Brilliant!</p><p>Sounds like trouble indeed. I think I will forgo this project. The export HTTP object looks like it does what I am looking for. Is there a way to script that functionality so that its a bit more automated?</p><p>I am looking at analyzing several day long packet captures. :) Its more of a "web cache".</p><p>thanks again, your comment has been quite helpful.</p></div><div id="comment-19998-info" class="comment-info"><span class="comment-age">(01 Apr '13, 16:00)</span> T3CHKOMMIE</div></div><span id="19999"></span><div id="comment-19999" class="comment"><div id="post-19999-score" class="comment-score"></div><div class="comment-text"><p>There is a "Save All" button, but I think that's all "automation" you can get from Wireshark. Maybe one of the other tools helps when dealing with large amount of trace files. Most tools that do large scale Web forensics on trace files cost money afaik.</p></div><div id="comment-19999-info" class="comment-info"><span class="comment-age">(01 Apr '13, 16:16)</span> Jasper ♦♦</div></div></div><div id="comment-tools-19996" class="comment-tools"></div><div class="clear"></div><div id="comment-19996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="20003"></span>

<div id="answer-container-20003" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20003-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If all you need is to extract files from pcaps, then Wireshark (as an packet analysis tool) is not the best fitted tool to use. Although it does have some options to export files (as @Jasper indicated), the main purpose of Wireshark lies elsewhere.</p><p>A quick google on the subject gives the following link. It lists a couple of other tools you might use that are a closer fit.</p><p>See: <a href="https://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961">https://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '13, 00:19</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-20003" class="comments-container"></div><div id="comment-tools-20003" class="comment-tools"></div><div class="clear"></div><div id="comment-20003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22696"></span>

<div id="answer-container-22696" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22696-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I capture in pcap format many SMTP packets, and I can assemble the packets from each SMTP connection through "Analyse --&gt; Follow TCP Stream". With that, I can get all the e-mails from each SMTP connection. However, I think the only way wireshark let me save the e-mails in separated files is doing one-by-one (and they are thousands of e-mails) through the reassembled tab in the "Packet Bytes" pane. Is there any way to do these savings automatically?</p><p>I saw that the attributes of the command line (using tshark) does not let me do that, and LUA scripts does not either ...</p><p>thank you for any help, Otavio</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '13, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/48e7519748fb722099c36d68bf681da7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="otavioc&#39;s gravatar image" /><p>otavioc<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="otavioc has no accepted answers">0%</span></p></div></div><div id="comments-container-22696" class="comments-container"></div><div id="comment-tools-22696" class="comment-tools"></div><div class="clear"></div><div id="comment-22696-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22697"></span>

<div id="answer-container-22697" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22697-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Any ideas on how to get started?</p></blockquote><p>I'd start by looking at <a href="https://github.com/simsong/tcpflow">tcpflow</a> and see whether it already does what I want.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '13, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22697" class="comments-container"></div><div id="comment-tools-22697" class="comment-tools"></div><div class="clear"></div><div id="comment-22697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

