+++
type = "question"
title = "DTLS decipher &quot;Application Data&quot; becomes &quot;Continuation Data&quot;"
description = '''Hello. I am using Wireshark 2.0.0 to debug an embedded system that uses DTLS to offload sensitive data with a custom protocol to a PC over WiFi/UDP. Openssl 1.0.2 is in use on both ends and the cipher suite is RSA-AES128-SHA. It took me several hours today to figure out that having the client send i...'''
date = "2015-12-16T22:38:00Z"
lastmod = "2015-12-16T22:38:00Z"
weight = 48595
keywords = [ "decipher", "decryption", "dtls", "dissector" ]
aliases = [ "/questions/48595" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DTLS decipher "Application Data" becomes "Continuation Data"](/questions/48595/dtls-decipher-application-data-becomes-continuation-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48595-score" class="post-score" title="current number of votes">0</div><span id="post-48595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello.</p><p>I am using Wireshark 2.0.0 to debug an embedded system that uses DTLS to offload sensitive data with a custom protocol to a PC over WiFi/UDP. Openssl 1.0.2 is in use on both ends and the cipher suite is RSA-AES128-SHA. It took me several hours today to figure out that having the client send its certificate to the server (as well as the usual server-to-client exchange) was confusing the decrypting dissector, which seems only capable of sniffing out the master key if the server behaves like a regular TLS-enabled web server or something. Oookay...no problem...I turned the client certificate presentation off and now I can see my packets beautifully decompressed and deciphered IN THE DTLS DISSECTOR'S DEBUG LOG.</p><p>BUT, of course, I'd like to see cleartext of each packet with each packet in the GUI. I notice that before I started trying to decrypt DTLS, my post-handshake packets were all labeled "Application Data" -- now, with the decryption in place, they are all labeled "Continuation Data." Looking at the dissector source, it appears that's what it does when it can't classify a DTLS packet (?). This makes sense as the DTLS section for a packet in the GUI now only shows the topmost level DTLS information (packet type number, length, sequence number). Whereas before it would show the "encrypted data" as well.</p><p>So my question is, how do I get the packet cleartext and stats into the GUI, or, failing that, at least correlate the info now in the debug log with the packet trace? Is there some magic I can do with "Decode as..." to force this? Is my setup borked? Or is the dissector currently incapable of handling app data payloads that are custom and weird to it?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decipher" rel="tag" title="see questions tagged &#39;decipher&#39;">decipher</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-dtls" rel="tag" title="see questions tagged &#39;dtls&#39;">dtls</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '15, 22:38</strong></p><img src="https://secure.gravatar.com/avatar/eb081795da62cb45ca6f82b37fbd5ddc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PatchyFog&#39;s gravatar image" /><p><span>PatchyFog</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PatchyFog has no accepted answers">0%</span></p></div></div><div id="comments-container-48595" class="comments-container"></div><div id="comment-tools-48595" class="comment-tools"></div><div class="clear"></div><div id="comment-48595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

