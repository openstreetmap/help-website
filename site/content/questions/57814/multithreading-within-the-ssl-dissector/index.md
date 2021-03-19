+++
type = "question"
title = "Multithreading within the SSL dissector"
description = '''A basic understanding in how the SSL dissector in wireshark works is like this  1. Determine packet content type ( App data, Key exchange, Alert, Handshake) 2. Append packet info to gui column. 3. Decode packet based on content type.  Specifically If content type is  A. Key exchange:  1. Read keylog...'''
date = "2016-12-03T03:09:00Z"
lastmod = "2016-12-03T08:41:00Z"
weight = 57814
keywords = [ "ssl", "multicore", "multithreaded", "decryption", "ssl_connection" ]
aliases = [ "/questions/57814" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Multithreading within the SSL dissector](/questions/57814/multithreading-within-the-ssl-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57814-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57814-score" class="post-score" title="current number of votes">0</div><span id="post-57814-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A basic understanding in how the SSL dissector in wireshark works is like this</p><pre><code>1. Determine packet content type ( App data, Key exchange, Alert, Handshake)
2. Append packet info to gui column.
3. Decode packet based on content type.

Specifically If content type is 
A. Key exchange:

1. Read keylog file if available
2. Generate TLS secrets and add to a “decoder” structure. Change “SSL state” to a global constant if successful generation of keys.
3. Load decoder structure for the ssl_session.

B. App data:
1. If decoder is available for the session, decrypt the data.</code></pre><p>I currently have a modified version of the SSL dissector such that it would enable remote decryption i.e. TLS session keys (not the keylog file) generated from another computer are sent to the gateway where my modified ssl dissector can use those keys to decrypt the data.</p><p>To do this, at some point I need to add a delay for every key exchange message to make sure that the appropriate TLS secrets have arrived inorder to create a decoder variable for that ssl session.</p><p>Because of the sequential nature of dissection in wireshark, the delay would eventually add up causing an undesirable performance.</p><p>Can someone please guide me on how I could avoid this problem or improve my code such that the delay does not accumulate. So far, I have looked at multithreading which is advised to be a big "No-No" for wireshark.</p><p>If multithreading is possible, could someone please tell me how do I proceed ? I am aware of this <a href="https://www.wireshark.org/lists/wireshark-dev/201205/msg00120.html">thread in the dev.</a></p><p>Sketch for remote decryption in wireshark <a href="https://ask.wireshark.org/questions/56910/remote-decryption-tls-in-wireshark">can also be seen here</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-multicore" rel="tag" title="see questions tagged &#39;multicore&#39;">multicore</span> <span class="post-tag tag-link-multithreaded" rel="tag" title="see questions tagged &#39;multithreaded&#39;">multithreaded</span> <span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-ssl_connection" rel="tag" title="see questions tagged &#39;ssl_connection&#39;">ssl_connection</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '16, 03:09</strong></p><img src="https://secure.gravatar.com/avatar/c28011fe6d6c690149158e45cf811175?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mac9393&#39;s gravatar image" /><p><span>mac9393</span><br />
<span class="score" title="36 reputation points">36</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mac9393 has no accepted answers">0%</span></p></div></div><div id="comments-container-57814" class="comments-container"></div><div id="comment-tools-57814" class="comment-tools"></div><div class="clear"></div><div id="comment-57814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57817"></span>

<div id="answer-container-57817" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57817-score" class="post-score" title="current number of votes">1</div><span id="post-57817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mac9393 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Multi-threading won't help you here, there is still a dependency between packets, and sometimes even between the ordering of TCP sessions (in the case of session resumption, though having the master secret for the resumed sessions helps a bit).</p><p>Your problem is the dependency on external data (the TLS master secrets). I see at least two options:</p><ul><li>Modify the server to delay handshake completion until your tool acknowledged the receipt of the secrets.</li><li>Put a proxy tool between the endpoint and Wireshark that buffers packets until the master secrets become available. Specfically:</li><li>A packet capture is not sent directly to Wireshark, but via a proxy.</li><li>This proxy (which could be using <code>tshark</code>) provides: TCP Stream number (<code>tcp.stream</code>), Client Hello and handshake types. No decryption is needed yet, you only have to recognize (the contents of) a TCP packet.</li><li>Now the decision to forward packets to Wireshark or to buffer it. If it is a TLS session, then you forward it only if you know the secrets. Otherwise, you buffer packets for which the keys are needed (e.g. ChangeCipherSpec, Finished, Application Data). Optionally you can flush a buffer (and forward the packets) after reaching a certain time deadline to avoid filling up buffers that never get emptied.</li></ul><p>The receiving side could use the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=doc/README.extcap">Extcap API</a> or just a simple pipe to stdin (<code>your_proxy_tool | wireshark -i - -k</code>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '16, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-57817" class="comments-container"></div><div id="comment-tools-57817" class="comment-tools"></div><div class="clear"></div><div id="comment-57817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

