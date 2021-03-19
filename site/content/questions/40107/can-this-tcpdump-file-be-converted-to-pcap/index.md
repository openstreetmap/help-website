+++
type = "question"
title = "Can this tcpdump file be converted to pcap?"
description = '''This command: tcpdump -vv -x -X -s 1500 -i eth0 &#x27;port 8080&#x27; &amp;gt; /var/tmp/tcpdump_port_8080  produces 17:49:45.461651 IP (tos 0x0, ttl 61, id 39983, offset 0, flags [DF], proto: TCP (6), length: 986) ack.com.57004 &amp;gt; ack.com.webcache: P, cksum 0xde66 (correct), 300:1234(934) ack 1 win 46 nop,nop,t...'''
date = "2015-02-26T13:44:00Z"
lastmod = "2015-02-26T15:16:00Z"
weight = 40107
keywords = [ "tcpdump" ]
aliases = [ "/questions/40107" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can this tcpdump file be converted to pcap?](/questions/40107/can-this-tcpdump-file-be-converted-to-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40107-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This command:</p><pre><code>tcpdump -vv -x -X -s 1500 -i eth0 &#39;port 8080&#39; &gt; /var/tmp/tcpdump_port_8080</code></pre><p>produces</p><pre><code>17:49:45.461651 IP (tos 0x0, ttl  61, id 39983, offset 0, flags [DF], proto: TCP (6), length: 986) ack.com.57004 &gt; ack.com.webcache: P, cksum 0xde66 (correct), 300:1234(934) ack 1 win 46  nop,nop,timestamp 2475621520 2475152160

0x0000:  4500 03da 9c2f 4000 3d06 39b7 c129 1156  E..../@.=.9..).V
0x0350:  7261 6e73 6163 7469 6f6e 4964 3e30 6231  ransactionId&gt;0b1
0x0360:  6163 3666 372d 3638 3432 2d34 3436 382d  ac6f7-6842-4468-
0x0370:  6166 6631 2d63 3063 3530 3635 6362 3235  aff1-c0c5065cb25
0x0380:  313c 2f74 7261 6e73 6163 7469 6f6e 4964  1&lt;/transactionId</code></pre></div><div id="question-tags" class="tags-container tags">tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '15, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/ab41998b8ac31c6d93c3c2ecd8f49d3b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Urnst66&#39;s gravatar image" /><p>Urnst66<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Urnst66 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '15, 14:42</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-40107" class="comments-container"><span id="40111"></span><div id="comment-40111" class="comment"><div id="post-40111-score" class="comment-score"></div><div class="comment-text"><p>Note that if you had done</p><pre><code>tcpdump -vv -x -X -s 1500 -i eth0 -w /var/tmp/tcpdump_port_8080.pcap  &#39;port 8080&#39;</code></pre><p>you would have had a pcap file, and wouldn't have to do the conversion.</p><p>Note also that <code>-s 1500</code> is wrong for Ethernet; the "snapshot length" specified by the <code>-s</code> flag is the <em>total</em> length of the packet, <em>including</em> the Ethernet header, <em>not</em> the MTU! The latest versions of tcpdump default to a large snapshot length; versions before that allow you to say <code>-s 0</code> to get a large snapshot length, and, for versions older than that, you'd have to do something such as <code>-s 262144</code>.</p></div><div id="comment-40111-info" class="comment-info"><span class="comment-age">(26 Feb '15, 19:39)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-40107" class="comment-tools"></div><div class="clear"></div><div id="comment-40107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40108"></span>

<div id="answer-container-40108" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40108-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can use <a href="https://www.wireshark.org/docs/man-pages/text2pcap.html"><code>text2pcap</code></a> to convert it to a pcap file, but you will first need to massage the data into a format that <code>text2pcap</code> accepts, because the depicted format is currently not supported by <code>text2pcap</code>.</p><p>So first, you can convert the data into a suitable format by using <a href="https://ask.wireshark.org/users/2593/kurt-knochner">Kurt Knochner's</a> perl script, given as an answer to <a href="https://ask.wireshark.org/questions/22758/changing-the-link-layer-type-of-input-frames">this</a> question and copied here for convenience:</p><pre><code>#!/usr/bin/perl

$| = 1;

my $regexp_time = &#39;(\d\d:\d\d:\d\d\.\d+ )&#39;;
my $regexp_hex = &#39;(0x\d+:\s+)([0-9a-f ]+)+  &#39;;

while (&lt;STDIN&gt;) {

   my $input = $_;

   if ($input =~ /^$regexp_time/) {
      print &quot;$1\n&quot;;
   }

   if ($input =~ /$regexp_hex/) {
      my $counter = $1;
      my $line = $2;

      $line =~ s/ //g;
      $counter =~ s/(0x|:)//g;

      print $counter . join(&#39; &#39;, ( $line =~ m/../g )) . &quot;\n&quot;;
   }
}</code></pre><p>Assuming the output of <code>tcpdump</code> is saved in a file called, <code>tcpdump.txt</code>, and Kurt's perl script is saved as <code>convert.pl</code>, run:</p><pre><code>cat tcpdump.txt | convert.pl &gt; tcpdump_converted.txt</code></pre><p>Once that's done, run <code>text2pcap</code> on the converted file:</p><pre><code> text2pcap -l 101 tcpdump_converted.txt tcpdump_converted.pcap</code></pre><p>Note that here I'm specifying "Raw IP" encapsulation. See <a href="http://www.tcpdump.org/linktypes.html">http://www.tcpdump.org/linktypes.html</a> for link types.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '15, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Feb '15, 00:53</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-40108" class="comments-container"><span id="40109"></span><div id="comment-40109" class="comment"><div id="post-40109-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Note that here I'm specifying "Raw IP" encapsulation.</p></blockquote><p>...because the packet data, in the tcpdump output, starts with the IP header, not with an Ethernet header.</p></div><div id="comment-40109-info" class="comment-info"><span class="comment-age">(26 Feb '15, 19:35)</span> Guy Harris ♦♦</div></div><span id="40129"></span><div id="comment-40129" class="comment"><div id="post-40129-score" class="comment-score"></div><div class="comment-text"><p>Thank you! That worked great.</p></div><div id="comment-40129-info" class="comment-info"><span class="comment-age">(27 Feb '15, 06:37)</span> Urnst66</div></div><span id="40131"></span><div id="comment-40131" class="comment"><div id="post-40131-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-40131-info" class="comment-info"><span class="comment-age">(27 Feb '15, 06:47)</span> grahamb ♦</div></div></div><div id="comment-tools-40108" class="comment-tools"></div><div class="clear"></div><div id="comment-40108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

