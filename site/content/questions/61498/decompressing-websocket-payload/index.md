+++
type = "question"
title = "Decompressing websocket payload"
description = '''I have a pcap of websocket traffic .  how can i see clear payload meaning after deflat masking .... actually i have a couple of question but first a bit of info  i can see that both client and server agree on the flag premessage-deflate in addition the client sent client_max_window_bits without numb...'''
date = "2017-05-18T13:57:00Z"
lastmod = "2017-09-19T11:49:00Z"
weight = 61498
keywords = [ "websocket", "deflate", "decompress" ]
aliases = [ "/questions/61498" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Decompressing websocket payload](/questions/61498/decompressing-websocket-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61498-score" class="post-score" title="current number of votes">0</div><span id="post-61498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap of websocket traffic . how can i see clear payload meaning after deflat masking .... actually i have a couple of question but first a bit of info i can see that both client and server agree on the flag premessage-deflate in addition the client sent client_max_window_bits without number (i assume by default its 32k window right???) another info : some of the packets are masked</p><p>additional question : do you do the decompression after unmasking the payload or after ? what octets do you decompress (i assume everything after the websocket header)? before decompressing do i need to add decompressing headers like 0x78 0x01 ? do you know any python library that can do it for me ?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-websocket" rel="tag" title="see questions tagged &#39;websocket&#39;">websocket</span> <span class="post-tag tag-link-deflate" rel="tag" title="see questions tagged &#39;deflate&#39;">deflate</span> <span class="post-tag tag-link-decompress" rel="tag" title="see questions tagged &#39;decompress&#39;">decompress</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '17, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/cce50cb41e08f84235b3bffa81b24e94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saeedh&#39;s gravatar image" /><p><span>saeedh</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saeedh has no accepted answers">0%</span></p></div></div><div id="comments-container-61498" class="comments-container"></div><div id="comment-tools-61498" class="comment-tools"></div><div class="clear"></div><div id="comment-61498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61574"></span>

<div id="answer-container-61574" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61574-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61574-score" class="post-score" title="current number of votes">1</div><span id="post-61574-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="saeedh has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Support for this is currently missing in the Websocket dissector. Until it gets implemented, you could try to manually decompress it. Here is an example for Python 3, the <code>websocket_payload_packet_X</code> variables contain the unmasked binary <code>websocket.payload</code> data (replace it accordingly):</p><pre><code>#!/usr/bin/env python3
import zlib

websocket_payload_packet_1 = bytes.fromhex(&quot;&quot;&quot;
aabbccddeeff...
&quot;&quot;&quot;.replace(&quot;\n&quot;, &quot;&quot;))

websocket_payload_packet_2 = bytes.fromhex(&quot;&quot;&quot;
aabbccddeeff...
&quot;&quot;&quot;.replace(&quot;\n&quot;, &quot;&quot;))

websocket_payload_packet_3 = bytes.fromhex(&quot;&quot;&quot;
aabbccddeeff...
&quot;&quot;&quot;.replace(&quot;\n&quot;, &quot;&quot;))

# Data from frame 1
data = websocket_payload_packet_1
# Needed per spec (https://tools.ietf.org/html/rfc7692#section-7.2.2)
data += b&#39;\0\0\xff\xff&#39;
data += websocket_payload_packet_2
data += b&#39;\0\0\xff\xff&#39;
data += websocket_payload_packet_3
data += b&#39;\0\0\xff\xff&#39;

z = zlib.decompressobj(wbits=-15)
out = z.decompress(data)
print(out)</code></pre><p>A variant of this (with actual valid data) was successfully tested (I just stripped it here because it could be sensitive data).</p><p>If you want to help, you could open an enhancement request and provide a small capture sample in the issue tracker at: <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '17, 09:45</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 May '17, 09:46</strong> </span></p></div></div><div id="comments-container-61574" class="comments-container"><span id="61578"></span><div id="comment-61578" class="comment"><div id="post-61578-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot this worked</p></div><div id="comment-61578-info" class="comment-info"><span class="comment-age">(23 May '17, 11:21)</span> <span class="comment-user userinfo">saeedh</span></div></div><span id="63502"></span><div id="comment-63502" class="comment"><div id="post-63502-score" class="comment-score"></div><div class="comment-text"><p>FYi and all other people who have the same issue. I created a LUA Plugin that does more or less what you described in here and has all the necessary glue code around it. You can find it incl. documentation here: <a href="https://github.com/stefanLeo/wireshark_websocket_deflate">https://github.com/stefanLeo/wireshark_websocket_deflate</a></p></div><div id="comment-63502-info" class="comment-info"><span class="comment-age">(23 Aug '17, 00:06)</span> <span class="comment-user userinfo">stefanLeo</span></div></div><span id="63590"></span><div id="comment-63590" class="comment"><div id="post-63590-score" class="comment-score"></div><div class="comment-text"><p>Native support for deflate (without LZ77 sliding window) is under review here: <a href="https://code.wireshark.org/review/23515">https://code.wireshark.org/review/23515</a> Any capture for LZ77 testing would be appreciated.</p></div><div id="comment-63590-info" class="comment-info"><span class="comment-age">(12 Sep '17, 12:52)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="63613"></span><div id="comment-63613" class="comment"><div id="post-63613-score" class="comment-score"></div><div class="comment-text"><p>Full support is now part of Wireshark 2.5 development tree.</p></div><div id="comment-63613-info" class="comment-info"><span class="comment-age">(19 Sep '17, 11:49)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-61574" class="comment-tools"></div><div class="clear"></div><div id="comment-61574-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

