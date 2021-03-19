+++
type = "question"
title = "decoding GSM_SMS to get plain text SMS Text"
description = '''Hi, I just try to capture GSMTAP packets from my OpenBTS. unfortunately I could not get SMS content as plain text. only looks symbol etc (seems still encoded). anybody know how to figure out this problem? some sources said with standart wireshark they could get content sms in plain text. I had tried...'''
date = "2015-03-06T01:48:00Z"
lastmod = "2015-03-07T06:15:00Z"
weight = 40316
keywords = [ "gsmtap", "openbts", "gsm_sms" ]
aliases = [ "/questions/40316" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [decoding GSM\_SMS to get plain text SMS Text](/questions/40316/decoding-gsm_sms-to-get-plain-text-sms-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40316-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I just try to capture GSMTAP packets from my OpenBTS. unfortunately I could not get SMS content as plain text. only looks symbol etc (seems still encoded). anybody know how to figure out this problem?</p><p>some sources said with standart wireshark they could get content sms in plain text. I had tried to copy its hex stream and decode with 7bit encoder which was provided online, but the result was same, I got nothing.</p><p>hex stream: 0000001b0405a10017f100 TP-User-Data: SMS TExt : @@@x@ @pa.Di</p><p>Many Thanks, Bass</p></div><div id="question-tags" class="tags-container tags">gsmtap openbts gsm_sms</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '15, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/bd24f32fb23479c997d1c603e5b6bff0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bass&#39;s gravatar image" /><p>bass<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bass has no accepted answers">0%</span></p></div></div><div id="comments-container-40316" class="comments-container"><span id="40325"></span><div id="comment-40325" class="comment"><div id="post-40325-score" class="comment-score"></div><div class="comment-text"><p>Could you share your pcap file? At first glance the decoding seems to make sense as the 0000000b character is @. Are you sure this hex stream corresponds to the TP-User-Data?</p></div><div id="comment-40325-info" class="comment-info"><span class="comment-age">(06 Mar '15, 06:11)</span> Pascal Quantin</div></div><span id="40343"></span><div id="comment-40343" class="comment"><div id="post-40343-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_from_2015-03-07_03:03:14.png" alt="alt text" /></p><p>I dont know how to upload my pcap file here, sorry. But, this is the print screen..</p></div><div id="comment-40343-info" class="comment-info"><span class="comment-age">(07 Mar '15, 00:05)</span> bass</div></div><span id="40344"></span><div id="comment-40344" class="comment"><div id="post-40344-score" class="comment-score"></div><div class="comment-text"><p>You cannot attach captures to ask, but should either upload it on a file sharing site like dropbox &amp; co, or upload it to <a href="http://www.cloudshark.org">http://www.cloudshark.org</a> and share the link here. Given the dissection you get, this does not seem to be a valid GSM SMS TPDU (invlaid TP-Service-Center-Time-Stamp, invalid TP-User-Dala-Length, ...). This could be a bug in the old Wiresahrk version you use, or a wrong logging done by your OpenBTS software.</p></div><div id="comment-40344-info" class="comment-info"><span class="comment-age">(07 Mar '15, 00:48)</span> Pascal Quantin</div></div><span id="40346"></span><div id="comment-40346" class="comment"><div id="post-40346-score" class="comment-score"></div><div class="comment-text"><p>sorry for inconvinience, hre the link:</p><p><a href="https://drive.google.com/open?id=0B2PfFt7P5kAgcjJaQUNBeVFuMGM&amp;authuser=0">https://drive.google.com/open?id=0B2PfFt7P5kAgcjJaQUNBeVFuMGM&amp;authuser=0</a></p><p>many thnks,</p></div><div id="comment-40346-info" class="comment-info"><span class="comment-age">(07 Mar '15, 02:33)</span> bass</div></div></div><div id="comment-tools-40316" class="comment-tools"></div><div class="clear"></div><div id="comment-40316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40347"></span>

<div id="answer-container-40347" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40347-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The TPDU generated by your SMS gateway seems invalid: the CP-User Data is 35 bytes long, the RP-User Data is 27 bytes long (so everything seems coherent so far) but the TP-User-Data-Length indicates a SMS of 161 characters. This is wrong for 2 reasons: a SMS cannot be more than 160 characters otherwise it needs to be segmented, and there is only 11 bytes left in the message (so 12 characters in 7-bits encoding). Moreover the SMSC timestamp field is completely buggy: the value for the month field is 94!</p><p>I do not see any Wireshark bug here, but a buggy TPDU payload.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '15, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></img></div></div><div id="comments-container-40347" class="comments-container"><span id="40348"></span><div id="comment-40348" class="comment"><div id="post-40348-score" class="comment-score"></div><div class="comment-text"><p>hmm. so it means that error comes from openbts sms? what possibility of caused? anyway thnks for your information.. I'll try to send sms and capture again.</p></div><div id="comment-40348-info" class="comment-info"><span class="comment-age">(07 Mar '15, 06:53)</span> bass</div></div><span id="40349"></span><div id="comment-40349" class="comment"><div id="post-40349-score" class="comment-score"></div><div class="comment-text"><p>I do not know anything about openbts, but I can tell you that the SMS DELIVER TPDU is definitely malformed.</p></div><div id="comment-40349-info" class="comment-info"><span class="comment-age">(07 Mar '15, 07:06)</span> Pascal Quantin</div></div><span id="40826"></span><div id="comment-40826" class="comment"><div id="post-40826-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal,</p><p>I have re-install my openBTS, with the latest version 5.0. sending SMS again then captute its packet. no "symbol" shown more. But in TP-User-DaTA just showed "Short Messages body". please take look..</p><p>here is my pcap file..</p><p><a href="https://drive.google.com/file/d/0B2PfFt7P5kAgWjg0bW5VX19jWXc/view?usp=sharing">https://drive.google.com/file/d/0B2PfFt7P5kAgWjg0bW5VX19jWXc/view?usp=sharing</a></p><p>Manythanks, bass</p></div><div id="comment-40826-info" class="comment-info"><span class="comment-age">(24 Mar '15, 22:40)</span> bass</div></div><span id="40828"></span><div id="comment-40828" class="comment"><div id="post-40828-score" class="comment-score"></div><div class="comment-text"><p>It shows only "short message body" because the character set used is 8 bits, which can be used both for a text (even if usually SMS are more using 7 bits GSM or UCS 2 encoding). A newer release of Wireshark would display the corresponding hex stream: 91:26:18:48:54:00:f9:27:11:aa:07:81:00:19:11:f1:00:00:ff:1e:d4:f2:1c:a4:ae:9f:c3 Which does not correspond to an ASCII text. Wireshark would display the text for 7bits GSM or UCS2 encoding.</p></div><div id="comment-40828-info" class="comment-info"><span class="comment-age">(25 Mar '15, 00:15)</span> Pascal Quantin</div></div><span id="40829"></span><div id="comment-40829" class="comment"><div id="post-40829-score" class="comment-score"></div><div class="comment-text"><p>The second SMS (frame 5082) uses 7 bits GSM encoding, the the length of the SMS is 0: TP-User-Data-Length: (0) no User-Data</p></div><div id="comment-40829-info" class="comment-info"><span class="comment-age">(25 Mar '15, 00:17)</span> Pascal Quantin</div></div></div><div id="comment-tools-40347" class="comment-tools"></div><div class="clear"></div><div id="comment-40347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

