+++
type = "question"
title = "Write Gzip Encoded HTTP as Inflated in PCAP File"
description = '''Is there any option or way to force tshark to write to the pcap output file the inflated http content body that was received encoded?'''
date = "2011-07-19T10:42:00Z"
lastmod = "2011-07-21T11:00:00Z"
weight = 5132
keywords = [ "gzip", "pcap", "inflate", "http", "tshark" ]
aliases = [ "/questions/5132" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Write Gzip Encoded HTTP as Inflated in PCAP File](/questions/5132/write-gzip-encoded-http-as-inflated-in-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5132-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any option or way to force tshark to write to the pcap output file the inflated http content body that was received encoded?</p></div><div id="question-tags" class="tags-container tags">gzip pcap inflate http tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '11, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/8eb26411ed8849ab46c314226c598644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sethlwilson&#39;s gravatar image" /><p>sethlwilson<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sethlwilson has one accepted answer">12%</span></p></div></div><div id="comments-container-5132" class="comments-container"></div><div id="comment-tools-5132" class="comment-tools"></div><div class="clear"></div><div id="comment-5132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5157"></span>

<div id="answer-container-5157" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5157-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found a way to extract what I needed which was SOAP XML traffic to/from a Web service. I wrote a simple Perl script that uses some very handy modules that I found.</p><pre><code>#!/usr/bin/perl

use strict;
use Net::Pcap;
use Net::PcapUtils;
use NetPacket;
use NetPacket::IP;
use NetPacket::Ethernet qw(:strip);
use Sniffer::HTTP;

my $VERBOSE = 0;

my $sniffer = Sniffer::HTTP-&gt;new( 
  callbacks =&gt; {
    request  =&gt; sub { my ($req, $conn) = @_; print $req-&gt;as_string,&quot;\n&quot; if $req },
    response =&gt; sub { my ($res, $req, $conn) = @_; print $res-&gt;decoded_content,&quot;\n&quot; },
    log      =&gt; sub { print $_[0] if $VERBOSE },
    tcp_log  =&gt; sub { print $_[0] if $VERBOSE &gt; 1 },
    }
);

sub process_pkt
{
  my ($usr, $hdr, $pkt) = @_;
  my $eth_obj = NetPacket::Ethernet-&gt;decode($pkt);
  $sniffer-&gt;handle_eth_packet($pkt);
}

my $err;
my $pcap = Net::Pcap::open_offline(&quot;$ARGV[0]&quot;, \$err)
  or die &quot;Unable to open pcap file: $err\n&quot;;
Net::Pcap::loop($pcap, -1, \&amp;process_pkt, &#39;&#39;);
Net::Pcap::close($pcap);</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jul '11, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/8eb26411ed8849ab46c314226c598644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sethlwilson&#39;s gravatar image" /><p>sethlwilson<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sethlwilson has one accepted answer">12%</span></p></div></div><div id="comments-container-5157" class="comments-container"></div><div id="comment-tools-5157" class="comment-tools"></div><div class="clear"></div><div id="comment-5157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5137"></span>

<div id="answer-container-5137" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5137-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think it is possible at the moment. And when I think about it there are some serious reasons why it won't work that easily. If you save the (originally compressed) payload uncompressed you'll heavily increase the packet size since the playload expands quite a bit. As a direct result most of the TCP sequence/ack numbers will get corrupted since they were calculated based on the original segment size. To correct them the saving process would need to go through the packets and recalculate all relevant values. Also, you'll quite often expand frames beyond the MTU (which is something you could live with, but still it will probably not be a valid trace anymore after saving it).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '11, 16:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-5137" class="comments-container"></div><div id="comment-tools-5137" class="comment-tools"></div><div class="clear"></div><div id="comment-5137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

