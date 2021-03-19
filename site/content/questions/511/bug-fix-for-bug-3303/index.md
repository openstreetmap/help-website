+++
type = "question"
title = "Bug fix for Bug 3303"
description = '''I&#x27;m new to this list but I have a relatively simple question: I was wondering when a patch would be available for &quot;Bug 3303 - Problem with fragmentation at the SSL record layer&quot;? Is it targeted at a particular release? If not, is there any beta code that I can test? I am working on an application wh...'''
date = "2010-10-14T15:08:00Z"
lastmod = "2010-10-14T22:58:00Z"
weight = 511
keywords = [ "ssl" ]
aliases = [ "/questions/511" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Bug fix for Bug 3303](/questions/511/bug-fix-for-bug-3303)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-511-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm new to this list but I have a relatively simple question:</p><p>I was wondering when a patch would be available for "Bug 3303 - Problem with fragmentation at the SSL record layer"? Is it targeted at a particular release? If not, is there any beta code that I can test?</p><p>I am working on an application where I need to be able to decrypt the traffic from a browser to another server.</p><p>I have downloaded the source and have applied the patch for "Bug 3343" but need the fix for 3303 so that I can decrypt the pkts.</p><p>Any help would be greatly appreciated.</p><p>Thanks,</p><p>Tom</p></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Oct '10, 15:08</strong></p><img src="https://secure.gravatar.com/avatar/c17fd1ed7918552bc5db931bb13b3042?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tom%20S&#39;s gravatar image" /><p>Tom S<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tom S has no accepted answers">0%</span></p></div></div><div id="comments-container-511" class="comments-container"></div><div id="comment-tools-511" class="comment-tools"></div><div class="clear"></div><div id="comment-511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="512"></span>

<div id="answer-container-512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-512-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Tom,</p><p>The problem in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3303">bug 3303</a> occurs only under very rare circumstances. Most references to that bug were actually caused by other things. The most common problems with decryption of SSL traffic are:</p><ul><li>Wireshark not being able to load the key. Check the ssl-debug file to make sure it loads the key.</li><li>Wireshark not seeing all packets of the SSL session. If the tracefile only contains part of the SSL session or only a resumed session, then Wireshark does not have all the information needed to decrypt the traffic. Make sure you have the full handshake (a resumed session does not have a "certificate" message from the server).</li><li>A diffie-hellman(DH) cipher has been chosen. Since DH uses keys that are generated on the fly to transport the pre-master-secret, Wireshark is unable to decrypt this traffic. For successful decryption, a RSA key exchange must be used where the pre-master-secret must be encrypted with the public key of the server. Wireshark can then decrypt this with the provided private key of the server. To determine if a DH is used, look for the ServerHello message and check the cipher in it. If it contains DH or DHE, DH is used. You can restrict the list of acceptable ciphers to not use DH ciphers on either the client or the server as a workaround</li></ul><p>Please have a look at a presentation I gave at Sharkfest (<a href="https://www.cacetech.com/sharkfest.09/AU2_Blok_SSL_Troubleshooting_with_Wireshark_and_Tshark.pps">PPT</a> or <a href="http://www.lovemytool.com/blog/2009/06/sake_blok_11.html">Video</a>) about troubleshooting SSL for more information. If you still feel you are running into bug 3303, please attach a tracefile to the bugreport and if possible, attach the key there as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '10, 22:58</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-512" class="comments-container"><span id="518"></span><div id="comment-518" class="comment"><div id="post-518-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the response.</p><p>From looking at the Server Hello, it appears that the cipher being used is TLS_RSA_WITH_RC4_128_MD5.</p><p>From talking to one of the other engineers here, we had already disabled the DH ciphers for the reasons you mentioned above.</p><p>I have not had a chance to watch the video but I will do so when I have time.</p><p>Not sure if I am running into 3303 or something else. I will post the trace and the keys later today.</p><p>Thanks,</p><p>Tom</p></div><div id="comment-518-info" class="comment-info"><span class="comment-age">(15 Oct '10, 08:44)</span> Tom S</div></div></div><div id="comment-tools-512" class="comment-tools"></div><div class="clear"></div><div id="comment-512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

