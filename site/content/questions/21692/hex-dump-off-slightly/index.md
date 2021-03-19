+++
type = "question"
title = "Hex Dump off slightly"
description = '''Hello, I am developing a program using libpcap to capture Beacon Frames, Probe Requests and Probe Responses from my wireless interface that I specify. When I try and hex dump the packet and look at the packet it is slightly off compared to what I am seeing in Wireshark, so I was wondering why this i...'''
date = "2013-06-02T09:45:00Z"
lastmod = "2013-06-02T12:44:00Z"
weight = 21692
keywords = [ "pcap-hex", "hexdump", "hex", "libpcap" ]
aliases = [ "/questions/21692" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Hex Dump off slightly](/questions/21692/hex-dump-off-slightly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21692-score" class="post-score" title="current number of votes">0</div><span id="post-21692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am developing a program using libpcap to capture Beacon Frames, Probe Requests and Probe Responses from my wireless interface that I specify. When I try and hex dump the packet and look at the packet it is slightly off compared to what I am seeing in Wireshark, so I was wondering why this is and if you guys do something special to the hex dump before you dump it?</p><p>If you need to see anymore information let me know.</p><p>This what I am doing for the hexdump (just incase you want to see)</p><pre><code>void hexdump(const void *ptr, int buflen) {
   unsigned char *buf = (unsigned char*)ptr;
   int i, j;
     for (i= 0; i&lt; buflen; i+=16) {
       printf(&quot;%06x: &quot;, i);
       for (j=0; j&lt;16; j++)
         if (i+j &lt; buflen)
           printf(&quot;%02x &quot;, buf[i+j]);
         else
           printf(&quot;   &quot;);
       printf(&quot; &quot;);
       for (j=0; j&lt;16; j++)
         if (i+j &lt; buflen)
           printf(&quot;%c&quot;, isprint(buf[i+j]) ? buf[i+j] : &#39;.&#39;);
       printf(&quot;\n&quot;);
     }
   }</code></pre><p>Thank you! DO</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap-hex" rel="tag" title="see questions tagged &#39;pcap-hex&#39;">pcap-hex</span> <span class="post-tag tag-link-hexdump" rel="tag" title="see questions tagged &#39;hexdump&#39;">hexdump</span> <span class="post-tag tag-link-hex" rel="tag" title="see questions tagged &#39;hex&#39;">hex</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '13, 09:45</strong></p><img src="https://secure.gravatar.com/avatar/def5fa9d8aae80ba742417f38842c462?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_Derko&#39;s gravatar image" /><p><span>_Derko</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_Derko has no accepted answers">0%</span></p></div></div><div id="comments-container-21692" class="comments-container"></div><div id="comment-tools-21692" class="comment-tools"></div><div class="clear"></div><div id="comment-21692-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21693"></span>

<div id="answer-container-21693" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21693-score" class="post-score" title="current number of votes">0</div><span id="post-21693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you say "slightly off", what exactly is the difference you are seeing between a wireshark hex dump of the packet and your own output?</p><p>A Wireshark "Packet bytes" hex dump output is in the format of [offset] [bytes] [ascii], where those three sections are delimited by two spaces and each byte is delimited by one space.</p><p>As an example, this is how I generate a hex dump file from an array of packets in perl (each entry is a hex string representing an entire packet), where I want to read the output of this into Wireshark's text2pcap utility (not bothering with the ASCII piece):</p><p><code>foreach (@packets) {         $packet = $_;         $packet_length = $_ =~ tr/[0-9a-zA-Z]//;         # The +0.999... is a cheap way to round up for the last line.         $line_count = int(($packet_length/32) + 0.9999999999);         for ($n=0; $n &lt; $line_count; $n++){             $offset = sprintf("%x",($n*16));             # Assumes no offset greater than 4 hex characters.             $lead_zeros = 4 - ($offset =~ tr/[0-9a-zA-Z]//);             $lead_zeros = '0' x $lead_zeros;             $bytes = substr($packet,$n*32,32);             # Adds a space character after every byte.             $bytes =~ s/([0-9a-zA-Z]{2})/$1 /g;             print "$lead_zeros$offset  $bytes\n";         }; };</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '13, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jun '13, 12:47</strong> </span></p></div></div><div id="comments-container-21693" class="comments-container"></div><div id="comment-tools-21693" class="comment-tools"></div><div class="clear"></div><div id="comment-21693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

