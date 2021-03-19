+++
type = "question"
title = "802.11 FCS computation and Annex G"
description = '''Hi, I tried to check the CRC32 computation of WLAN MAC frames by the CRC32 function in the Wireshark code. For this test, I am using the test packets in Annex G of the 802.11 2007 spec, and the vector in H.6.4 CCMP of the same spec. However, I don&#x27;t get the result as written there, and I don&#x27;t under...'''
date = "2011-08-02T18:50:00Z"
lastmod = "2011-08-04T18:53:00Z"
weight = 5413
keywords = [ "crc32", "annex-g", "fcs", "802.11" ]
aliases = [ "/questions/5413" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [802.11 FCS computation and Annex G](/questions/5413/80211-fcs-computation-and-annex-g)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5413-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I tried to check the CRC32 computation of WLAN MAC frames by the CRC32 function in the Wireshark code. For this test, I am using the test packets in Annex G of the 802.11 2007 spec, and the vector in H.6.4 CCMP of the same spec.</p><p>However, I don't get the result as written there, and I don't understand what I am doing wrong. I used Matlab to generate the FCS as follows:</p><pre><code>% WLAN MAC FCS % x32 + x26 + x23 + x22 + x16 + x12 + x11 + x10 + x8 + x7 + x5 + x4 + x2 + x + 1

G = [1 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 1 0 0 0 1 1 1 0 1 1 0 1 1 0 1 1 1]; %G = 0x104C11DB7

%
%CRC generator object
gen = crc.generator(&#39;Polynomial&#39;, G, ... 
&#39;ReflectInput&#39;, false, ... 
&#39;InitialSate&#39;, ones(1, 32), ... %all ones initial state 
&#39;FinalXOR&#39;, ones(1, 32), ... %one-complement CRC 
&#39;ReflectRemainder&#39;, false);

%
% ADD CRC 
encoded = generate(gen, binmpdu); %binmpdu is shown partly below and is based on
                                  %the Annex G test vector

%
% CHECK CRC
crc = encoded(end-31:end);</code></pre><p>The test data I am using is the following (except for the last 4 bytes, which are the CRC)</p><pre><code>% Hex table in Annex G is as follows (read out per row) 
% mpdu = [&#39;04&#39; &#39;02&#39; &#39;00&#39; &#39;2e&#39; &#39;00&#39; 
% &#39;60&#39; &#39;08&#39; &#39;cd&#39; &#39;37&#39; &#39;a6&#39; 
% &#39;00&#39; &#39;20&#39; &#39;d6&#39; &#39;01&#39; &#39;3c&#39; 
% &#39;f1&#39; &#39;00&#39; &#39;60&#39; &#39;08&#39; &#39;ad&#39; 
% &#39;3b&#39; &#39;af&#39; &#39;00&#39; &#39;00&#39; &#39;4a&#39; 
% &#39;6f&#39; &#39;79&#39; &#39;2c&#39; &#39;20&#39; &#39;62&#39; 
% &#39;72&#39; &#39;69&#39; &#39;67&#39; &#39;68&#39; &#39;74&#39; 
% &#39;20&#39; &#39;73&#39; &#39;70&#39; &#39;61&#39; &#39;72&#39;
% &#39;6b&#39; &#39;20&#39; &#39;6f&#39; &#39;66&#39; &#39;20&#39; 
% &#39;64&#39; &#39;69&#39; &#39;76&#39; &#39;69&#39; &#39;6e&#39; 
% &#39;69&#39; &#39;74&#39; &#39;79&#39; &#39;2c&#39; &#39;0a&#39; 
% &#39;44&#39; &#39;61&#39; &#39;75&#39; &#39;67&#39; &#39;68&#39;
% &#39;74&#39; &#39;65&#39; &#39;72&#39; &#39;20&#39; &#39;6f&#39;
% &#39;66&#39; &#39;20&#39; &#39;45&#39; &#39;6c&#39; &#39;79&#39;
% &#39;73&#39; &#39;69&#39; &#39;75&#39; &#39;6d&#39; &#39;2c&#39;
% &#39;0a&#39; &#39;46&#39; &#39;69&#39; &#39;72&#39; &#39;65&#39;
% &#39;2d&#39; &#39;69&#39; &#39;6e&#39; &#39;73&#39; &#39;69&#39;
% &#39;72&#39; &#39;65&#39; &#39;64&#39; &#39;20&#39; &#39;77&#39;
% &#39;65&#39; &#39;20&#39; &#39;74&#39; &#39;72&#39; &#39;65&#39;
% &#39;61&#39; &#39;da&#39; &#39;57&#39; &#39;99&#39; &#39;ed&#39;
% ];</code></pre><p>In binary, this gives:</p><pre><code>bit 0 (PHY encoded, e.g. enters scrambled first) | 00100000010000000000 ...</code></pre><p>(this is '04' '02'` '00' '2e', written as '4' first, the '0', then '2', then '0', etc...</p><p>I have checked this binary sequence by successfully generating the PHY baseband signal from it which is identical to the reference in Annex G.</p><p>But I can't get the CRC32 computation right (the last 4 bytes in the mpdu above, listed in the spec as 'da' '57' '99' 'ed'). I tried swapping the nibbles, reversing the nibbles, ... but nothing works, I just don't get the same CRC bytes as in the spec. Can anybody tell me what I am doing so wrong?</p><p>Many thanks for your help!!!</p><p>Karen</p></div><div id="question-tags" class="tags-container tags">crc32 annex-g fcs 802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '11, 18:50</strong></p><img src="https://secure.gravatar.com/avatar/3d73367ea6311fa5a1e7b781f2ad3fb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karen&#39;s gravatar image" /><p>Karen<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Aug '11, 22:08</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5413" class="comments-container"></div><div id="comment-tools-5413" class="comment-tools"></div><div class="clear"></div><div id="comment-5413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5512"></span>

<div id="answer-container-5512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5512-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I suggest reading <a href="http://standards.ieee.org/getieee802/download/802.11-2007.pdf">section 7.1.3.7</a> very carefully and then examining the Wireshark source code to see how it computes the CRC32.</p><p>In particular, have a look at the implementation of <code>crc32_802_tvb_padded()</code> located in <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-ieee80211.c?revision=38281&amp;view=markup"><code>packet-ieee80211.c</code></a> around lines 8719-8734, as well as the implementation of <code>crc32_802_tvb()</code> in <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/crc32.c?revision=35989&amp;view=markup"><code>crc32.c</code></a> around lines 252-275. Both of those functions are called in <code>packet-ieee80211.c</code> around lines 9412-9414.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '11, 18:53</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-5512" class="comments-container"></div><div id="comment-tools-5512" class="comment-tools"></div><div class="clear"></div><div id="comment-5512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

