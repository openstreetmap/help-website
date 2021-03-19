+++
type = "question"
title = "text2pcap &quot;Inconsistent offset. Expecting 0, got 10&quot;"
description = '''I have the following data I&#x27;d like to convert to a pcap with text2pcap: # cat ~/temp.argus 12:00:01.3214  0000 2665 7547 4a0b c0f2 0fed 1a9b 9c1d b9f3 &amp;amp;euGJ...........  0010 7096 d098 7a1f 6255 f92e d9b0 b202 6c03 p...z.bU......l.  I attempt to do this by executing the following: # text2pcap -i ...'''
date = "2013-07-02T13:10:00Z"
lastmod = "2013-07-02T18:08:00Z"
weight = 22570
keywords = [ "text2pcap", "processing", "pcap" ]
aliases = [ "/questions/22570" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [text2pcap "Inconsistent offset. Expecting 0, got 10"](/questions/22570/text2pcap-inconsistent-offset-expecting-0-got-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22570-score" class="post-score" title="current number of votes">0</div><span id="post-22570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the following data I'd like to convert to a pcap with <code>text2pcap</code>:</p><pre><code># cat ~/temp.argus
12:00:01.3214
  0000       2665 7547 4a0b c0f2 0fed 1a9b 9c1d b9f3        &amp;euGJ...........
  0010       7096 d098 7a1f 6255 f92e d9b0 b202 6c03        p...z.bU......l.</code></pre><p>I attempt to do this by executing the following:</p><pre><code># text2pcap -i 4 -T 65000,80 -d ~/temp.argus ~/test.pcap</code></pre><p>But I receive the following error and conversion fails:</p><pre><code>Input from: /root/temp.argus
Output to: /root/test.pcap
Generate dummy Ethernet header: Protocol: 0x800
Generate dummy IP header: Protocol: 6
Generate dummy TCP header: Source port: 65000. Dest port: 80
Start new packet
Inconsistent offset. Expecting 0, got 10. Ignoring rest of packet
-------------------------
Read 1 potential packet, wrote 0 packets</code></pre><p>What is wrong with the syntax of the previous file? It's indicated that <code>text2pcap</code> recognizes the packet, as a packet, but doesn't like the <code>0010</code> offset? How do I resolve this issue?</p><p>Thanks,</p><p>Matt</p><p>[update]</p><p>Thanks guys. I think I also tried <code>"%T.%f"</code> originally (without the trailing <code>.</code>), but was not successful. I will test all three tomorrow and let you know. Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-text2pcap" rel="tag" title="see questions tagged &#39;text2pcap&#39;">text2pcap</span> <span class="post-tag tag-link-processing" rel="tag" title="see questions tagged &#39;processing&#39;">processing</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '13, 13:10</strong></p><img src="https://secure.gravatar.com/avatar/e6fa2b684fd063838a85a0aedef46c34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mbrownnyc&#39;s gravatar image" /><p><span>mbrownnyc</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mbrownnyc has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jul '13, 19:19</strong> </span></p></div></div><div id="comments-container-22570" class="comments-container"></div><div id="comment-tools-22570" class="comment-tools"></div><div class="clear"></div><div id="comment-22570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22572"></span>

<div id="answer-container-22572" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22572-score" class="post-score" title="current number of votes">1</div><span id="post-22572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>text2pcap needs a defined format as input, which is described here:</p><blockquote><p><a href="http://www.wireshark.org/docs/man-pages/text2pcap.html">http://www.wireshark.org/docs/man-pages/text2pcap.html</a></p></blockquote><p>In your input, text2pcap does not understand the date stamp. If you reformat the input like shown below, it will accept it.</p><pre><code>0000 26 65 75 47 4a 0b c0 f2 0f ed 1a 9b 9c 1d b9 f3        &amp;euGJ...........
0010 70 96 d0 98 7a 1f 62 55 f9 2e d9 b0 b2 02 6c 03        p...z.bU......l.</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '13, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jul '13, 14:05</strong> </span></p></div></div><div id="comments-container-22572" class="comments-container"><span id="22580"></span><div id="comment-22580" class="comment"><div id="post-22580-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. I'll give this a shot tomorrow. It's stated in the docs that if no timestamp is provided, then each packet is stamped a second apart. How do I properly supply the timstamp? Thanks.</p></div><div id="comment-22580-info" class="comment-info"><span class="comment-age">(02 Jul '13, 15:25)</span> <span class="comment-user userinfo">mbrownnyc</span></div></div><span id="22582"></span><div id="comment-22582" class="comment"><div id="post-22582-score" class="comment-score"></div><div class="comment-text"><p>Ah, it was your intention to have the time stamp in the packets. So, then please use the following command:</p><blockquote><p>text2pcap -i 4 -T 65000,80 -t "%H:%M:%S." -d input.txt output.pcap</p></blockquote><p>with this input.txt</p><pre><code>12:00:01.3214
  0000  26 65 75 47 4a 0b c0 f2 0f ed 1a 9b 9c 1d b9 f3        &amp;euGJ...........
  0010  70 96 d0 98 7a 1f 62 55 f9 2e d9 b0 b2 02 6c 03        p...z.bU......l.</code></pre></div><div id="comment-22582-info" class="comment-info"><span class="comment-age">(02 Jul '13, 16:00)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22583"></span><div id="comment-22583" class="comment"><div id="post-22583-score" class="comment-score">1</div><div class="comment-text"><p>Or you can use the shorter form:</p><pre><code>text2pcap -i 4 -T 65000,80 -t &quot;%T.&quot; -d input.txt output.pcap</code></pre><p>Refer to <a href="http://linux.die.net/man/3/strptime">strptime</a> for more details on the various time field descriptors.</p><p>Incidentally, Wireshark also supports importing a text file in this format to a pcap file. Use "<code>File -&gt; Import from Hex Dump</code>" (or "<code>File -&gt; Import</code>" for Wireshark 1.8).</p></div><div id="comment-22583-info" class="comment-info"><span class="comment-age">(02 Jul '13, 18:08)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-22572" class="comment-tools"></div><div class="clear"></div><div id="comment-22572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

