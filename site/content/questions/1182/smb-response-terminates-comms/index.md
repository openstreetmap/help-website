+++
type = "question"
title = "SMB response terminates comms"
description = '''I&#x27;m having an issue with failed SMB communications and cannot determine the source of the response behavior from a Windows 7 PC. Was hoping that anyone might be able to help. Here&#x27;s the response packet: No. Time Source Destination Protocol Info  1425 34.647499 192.168.1.74 192.168.1.68 SMB Negotiate...'''
date = "2010-11-30T10:15:00Z"
lastmod = "2010-12-07T17:22:00Z"
weight = 1182
keywords = [ "negotiation", "failed", "smb" ]
aliases = [ "/questions/1182" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SMB response terminates comms](/questions/1182/smb-response-terminates-comms)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1182-score" class="post-score" title="current number of votes">0</div><span id="post-1182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm having an issue with failed SMB communications and cannot determine the source of the response behavior from a Windows 7 PC. Was hoping that anyone might be able to help.</p><p>Here's the response packet:</p><p>No. Time Source Destination Protocol Info 1425 34.647499 192.168.1.74 192.168.1.68 SMB Negotiate Protocol Response</p><p>Frame 1425: 475 bytes on wire (3800 bits), 475 bytes captured (3800 bits) Ethernet II, Src: Dell_24:7e:41 (00:21:9b:24:7e:41), Dst: Xerox_c3:73:c7 (00:00:aa:c3:73:c7) Internet Protocol, Src: 192.168.1.74 (192.168.1.74), Dst: 192.168.1.68 (192.168.1.68) Transmission Control Protocol, Src Port: microsoft-ds (445), Dst Port: 60933 (60933), Seq: 1, Ack: 195, Len: 409 NetBIOS Session Service SMB (Server Message Block Protocol)</p><p>0000 00 00 aa c3 73 c7 00 21 9b 24 7e 41 08 00 45 00 ....s..!.$~A..E. 0010 01 cd 41 9e 40 00 80 06 00 00 c0 a8 01 4a c0 a8 <span class="__cf_email__" data-cfemail="06282847284628282828282828284c2828">[email protected]</span> 0020 01 44 01 bd ee 05 31 a6 d8 8b 95 e2 ce 1c 80 18 .D....1......... 0030 01 04 85 9e 00 00 01 01 08 0a 00 0d 45 17 00 03 ............E... 0040 f3 e9 00 00 01 95 ff 53 4d 42 72 00 00 00 00 88 .......SMBr..... 0050 01 c8 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................ 0060 4e 03 00 00 01 00 11 09 00 03 32 00 01 00 04 11 N.........2..... 0070 00 00 00 00 01 00 00 00 00 00 fc e3 01 80 f1 99 ................ 0080 ad 07 98 4f cb 01 2c 01 00 50 01 40 de 4e df 0e ...O..,<span class="__cf_email__" data-cfemail="5f71710f711f71117171">[email protected]</span> 0090 59 3b 48 bd 5f 89 c6 ca bd 06 05 60 82 01 3c 06 Y;H._......<code>..&lt;. 00a0  06 2b 06 01 05 05 02 a0 82 01 30 30 82 01 2c a0   .+........00..,. 00b0  1a 30 18 06 0a 2b 06 01 04 01 82 37 02 02 1e 06   .0...+.....7.... 00c0  0a 2b 06 01 04 01 82 37 02 02 0a a2 82 01 0c 04   .+.....7........ 00d0  82 01 08 4e 45 47 4f 45 58 54 53 01 00 00 00 00   ...NEGOEXTS..... 00e0  00 00 00 60 00 00 00 70 00 00 00 ec b9 81 d6 13   ...</code>...p........ 00f0 c2 3c a6 38 35 7f e7 b4 f1 c5 93 6f 2d b0 e5 45 .&lt;.85......o-..E 0100 88 52 cc b7 a0 eb 9a ea fa 9b 68 93 11 6c 1a fd .R........h..l.. 0110 8a ca 2b b7 d1 7a c6 14 df 0c 6e 00 00 00 00 00 ..+..z....n..... 0120 00 00 00 60 00 00 00 01 00 00 00 00 00 00 00 00 ...`............ 0130 00 00 00 5c 33 53 0d ea f9 0d 4d b2 ec 4a e3 78 ...3S....M..J.x 0140 6e c3 08 4e 45 47 4f 45 58 54 53 03 00 00 00 01 n..NEGOEXTS..... 0150 00 00 00 40 00 00 00 98 00 00 00 ec b9 81 d6 13 <span class="__cf_email__" data-cfemail="f6d8d8d8b6d8d8d8d8d8d8d8d8d8d8d8d8">[email protected]</span> 0160 c2 3c a6 38 35 7f e7 b4 f1 c5 93 5c 33 53 0d ea .&lt;.85......3S.. 0170 f9 0d 4d b2 ec 4a e3 78 6e c3 08 40 00 00 00 58 <span class="__cf_email__" data-cfemail="6846462546462246100646462846464630">[email protected]</span> 0180 00 00 00 30 56 a0 54 30 52 30 27 80 25 30 23 31 ...0V.T0R0'.%0#1 0190 21 30 1f 06 03 55 04 03 13 18 54 6f 6b 65 6e 20 !0...U....Token 01a0 53 69 67 6e 69 6e 67 20 50 75 62 6c 69 63 20 4b Signing Public K 01b0 65 79 30 27 80 25 30 23 31 21 30 1f 06 03 55 04 ey0'.%0#1!0...U. 01c0 03 13 18 54 6f 6b 65 6e 20 53 69 67 6e 69 6e 67 ...Token Signing 01d0 20 50 75 62 6c 69 63 20 4b 65 79 Public Key</p><p>The Win 7 machine appears to be asking the client to begin signing but I've tried everything I can think of to simulate this behavior - Security Policies, Lanman registry edits, etc. to no avail. Successful communication does not include the mechToken in the security blob. When we see this, all comms stop.</p><p>Does anyone know what can cause this behavior? Any assistance will be greatly appreciated. Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-negotiation" rel="tag" title="see questions tagged &#39;negotiation&#39;">negotiation</span> <span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span> <span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Nov '10, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/0750da61d6029bad9eca9140f3d86e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MarkMcD&#39;s gravatar image" /><p><span>MarkMcD</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MarkMcD has no accepted answers">0%</span></p></div></div><div id="comments-container-1182" class="comments-container"></div><div id="comment-tools-1182" class="comment-tools"></div><div class="clear"></div><div id="comment-1182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1276"></span>

<div id="answer-container-1276" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1276-score" class="post-score" title="current number of votes">3</div><span id="post-1276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I converted your hex dump to a trace file to get this SMB decode of your packet:</p><p><img src="http://www.synerity.com/images/SMB-response.png" alt="alt text" /></p><p>The interesting part is the server offering two authentication mechanisms to the client: The well understood NTLMSSP or a less known mechType 1.3.6.1.4.1.311.2.2.30.</p><p>This mechtype can be found in a patent filed by Microsoft. The text can be found <a href="http://www.freepatentsonline.com/y2009/0328140.html" title="MS Patent on authentication">here</a></p><p>It looks like the the "Microsoft live sign-on assistant" tampers with the SMB authentication. One report is found in a <a href="http://social.technet.microsoft.com/Forums/en/w7itpronetworking/thread/9c6f1d74-f7f0-4503-94fa-0d79a5597527" title="MS live sign-on assistant and SMB authentication">technet forum</a></p><p>A topic in the discussion shows reads</p><p>For reference, please see the following samba bug report: https://bugzilla.samba.org/show_bug.cgi?id=7577</p><p>Alas, your post does not state the client OS. Given the postings I would not be surprised to hear that it's a samba client.</p><p>The obvious solution would be a) to uninstall the Live sign-on assistant or b) apply the fix to the samba client</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '10, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Dec '10, 14:52</strong> </span></p></div></div><div id="comments-container-1276" class="comments-container"><span id="1279"></span><div id="comment-1279" class="comment"><div id="post-1279-score" class="comment-score"></div><div class="comment-text"><p>Wow..packethunter, talk about going the mile! (converting it to pcap, I mean)</p></div><div id="comment-1279-info" class="comment-info"><span class="comment-age">(07 Dec '10, 17:22)</span> <span class="comment-user userinfo">hansangb</span></div></div></div><div id="comment-tools-1276" class="comment-tools"></div><div class="clear"></div><div id="comment-1276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

