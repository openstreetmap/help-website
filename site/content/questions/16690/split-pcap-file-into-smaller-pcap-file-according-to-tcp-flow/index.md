+++
type = "question"
title = "Split pcap file into smaller pcap file (according to tcp flow)"
description = '''I need to find a way to split a large pcap file into separated pcap files. What I want to find is a application like Splitcap but I need a application which runs on Linux. Tcpflow or Tcptrace don&#x27;t generate pcap file as their output. The output pcap file should contains a tcp flow. If there&#x27;s an app...'''
date = "2012-12-07T08:21:00Z"
lastmod = "2016-07-23T12:45:00Z"
weight = 16690
keywords = [ "flow", "pcap", "split", "tcp" ]
aliases = [ "/questions/16690" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Split pcap file into smaller pcap file (according to tcp flow)](/questions/16690/split-pcap-file-into-smaller-pcap-file-according-to-tcp-flow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16690-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to find a way to split a large pcap file into separated pcap files. What I want to find is a application like Splitcap but I need a application which runs on Linux. Tcpflow or Tcptrace don't generate pcap file as their output. The output pcap file should contains a tcp flow.</p><p>If there's an application, please let me know. Split pcap file using tshark will be very helpful for me.</p></div><div id="question-tags" class="tags-container tags">flow pcap split tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '12, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/2c33bce451fd8dc3844b351b798cbee1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fates&#39;s gravatar image" /><p>fates<br />
<span class="score" title="35 reputation points">35</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fates has no accepted answers">0%</span></p></div></div><div id="comments-container-16690" class="comments-container"></div><div id="comment-tools-16690" class="comment-tools"></div><div class="clear"></div><div id="comment-16690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="16691"></span>

<div id="answer-container-16691" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16691-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>tshark can do that.</p><blockquote><p><code>tshark -nr input.cap -R "tcp.stream eq 1" -w stream_1.cap</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '12, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16691" class="comments-container"><span id="16692"></span><div id="comment-16692" class="comment"><div id="post-16692-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the comment, Kurt. But my input file contains more than one millinon flows. Is there any other options to do this?</p></div><div id="comment-16692-info" class="comment-info"><span class="comment-age">(07 Dec '12, 08:33)</span> fates</div></div><span id="16695"></span><div id="comment-16695" class="comment"><div id="post-16695-score" class="comment-score">1</div><div class="comment-text"><p>And you are asking for what? Having 1 million files, one for each stream?</p><p>If so, you can run tshark in a loop and use the loop counter in the stream filter and the output file name.</p><p>See the following question:</p><blockquote><p><code>http://ask.wireshark.org/questions/4677/easy-way-to-save-tcp-streams</code></p></blockquote></div><div id="comment-16695-info" class="comment-info"><span class="comment-age">(07 Dec '12, 08:41)</span> Kurt Knochner ♦</div></div><span id="16696"></span><div id="comment-16696" class="comment"><div id="post-16696-score" class="comment-score"></div><div class="comment-text"><p>A easier/faster method would be this python script:</p><blockquote><p><code>http://corelabs.coresecurity.com/index.php?module=Wiki&amp;action=attachment&amp;type=tool&amp;page=Impacket&amp;file=split.py</code><br />
</p><p><code>http://corelabs.coresecurity.com/index.php?module=Wiki&amp;action=view&amp;type=tool&amp;name=Impacket</code></p></blockquote><p>The script needs pcapy. You can install pcapy on Ubuntu like this:</p><blockquote><p><code>apt-get install python-pcapy</code></p></blockquote></div><div id="comment-16696-info" class="comment-info"><span class="comment-age">(07 Dec '12, 08:57)</span> Kurt Knochner ♦</div></div><span id="16698"></span><div id="comment-16698" class="comment"><div id="post-16698-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Kurt! By the way, I've already tried the python script. :) But this script uses "Impacket" package and this package cannot handle corrupted packets. This is why I'm trying to find other solutions.</p></div><div id="comment-16698-info" class="comment-info"><span class="comment-age">(07 Dec '12, 09:51)</span> fates</div></div><span id="16700"></span><div id="comment-16700" class="comment"><div id="post-16700-score" class="comment-score"></div><div class="comment-text"><p>well, then use tshark.</p></div><div id="comment-16700-info" class="comment-info"><span class="comment-age">(07 Dec '12, 09:59)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16691" class="comment-tools"></div><div class="clear"></div><div id="comment-16691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17239"></span>

<div id="answer-container-17239" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17239-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Separate the packets into flows considering only 4 tuples: source address, source port, dest address, dest port for further analysis.</p><p>The packets are saved in the time order without any processing like TCP resembling.</p><p>The flow timeout is considered as 64 seconds suggested by CAIDA.</p><p><a href="https://github.com/caesar0301/pkt2flow">https://github.com/caesar0301/pkt2flow</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Dec '12, 04:01</strong></p><img src="https://secure.gravatar.com/avatar/81988a1f30e4bd1169a9352b6991ae9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jamin&#39;s gravatar image" /><p>Jamin<br />
<span class="score" title="17 reputation points">17</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jamin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-17239" class="comments-container"></div><div id="comment-tools-17239" class="comment-tools"></div><div class="clear"></div><div id="comment-17239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18641"></span>

<div id="answer-container-18641" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18641-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The tshark scripts didn't finish in 30 minutes on my 4G pcap with about 40 flows. The following finished in about 90 seconds. tshark versus tcpdump?</p><pre><code>#!/usr/bin/perl -w

use strict;

use Data::Dumper;

sub mysystem {
  my ($s, $donothing) = @_;
  chomp $s;
  print &quot;$s\n&quot;;
  if ( defined $donothing ) {
    return;
  }
  my $rv = system &quot;$s &gt; cmd.out&quot;;
  if ($? == -1) {
    die &quot;failed to execute: $!\n&quot;;
  } elsif ($? &amp; 127) {
    die sprintf &quot;child died with signal %d, %s coredump\n&quot;,
      ($? &amp; 127),  ($? &amp; 128) ? &#39;with&#39; : &#39;without&#39;;
  } elsif( $rv ) {
      $rv = $rv/256;
      die &quot;$s exited with status $rv\n&quot;;
  }
  `cat cmd.out`;
}

# return 4-tuples. the protocol is always tcp.
sub identify_tcp_flows {
  my $pcapfn = shift;

  my %flows;

  open F, &quot;tcpdump -n -r ${pcapfn} tcp |&quot; or die &quot;fozzle&quot;;
  while (&lt;F&gt;) {
    if ( m{
          \A
          (?&lt;timestamp&gt;
            \d{2} :
            \d{2} :
            \d{2} [\.] \d+
          ) \s+
          IP \s+
          (?&lt;src_ip&gt;
            \S+
          )
          [\.]
          (?&lt;src_port&gt;
            \d+
          ) \s+
          &gt; \s+
          (?&lt;dst_ip&gt;
            \S+
          )
          [\.]
          (?&lt;dst_port&gt;
            \d+ | http
          ) : \s+
          Flags \s+
          [\[]
          (?&lt;flags&gt;
            [^\]]+
          )
          [\]] , \s+
          (
            seq \s+ \d+ , \s+
          )?
          (?&lt;ack&gt;
            ack \s+
            (?&lt;ackbytes&gt;
              \d+
            ) , \s+
          ) ?
        }xms
       ) {
      if ( ! exists $flows{&quot;$+{dst_ip}:$+{dst_port}-$+{src_ip}:$+{src_port}&quot;} ) {
        $flows{&quot;$+{src_ip}:$+{src_port}-$+{dst_ip}:$+{dst_port}&quot;} = {
                                                                        src_ip =&gt; $+{src_ip},
                                                                        src_port =&gt; $+{src_port},
                                                                        dst_ip =&gt; $+{dst_ip},
                                                                        dst_port =&gt; $+{dst_port},
                                                                       };
}
    } else {
#      warn &quot;couldn&#39;t parse $_&quot;;
    }
  }
  \%flows
}

my $pcapfn = $ARGV[0];
my $r_h_flows = identify_tcp_flows $pcapfn;
for my $f ( keys $r_h_flows ) {
  mysystem &quot;tcpdump -n -r ${pcapfn} -w $f.pcap \&quot;tcp and host $$r_h_flows{$f}{src_ip} and host $$r_h_flows{$f}{dst_ip} and port $$r_h_flows{$f}{src_port} and port $$r_h_flows{$f}{dst_port} \&quot;&quot;;
}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '13, 13:51</strong></p><img src="https://secure.gravatar.com/avatar/05293fbabda5ac919b290dae5a01ef58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brucer42&#39;s gravatar image" /><p>brucer42<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brucer42 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Feb '13, 14:14</p></div></div><div id="comments-container-18641" class="comments-container"></div><div id="comment-tools-18641" class="comment-tools"></div><div class="clear"></div><div id="comment-18641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54257"></span>

<div id="answer-container-54257" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54257-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use <a href="https://github.com/seladb/PcapPlusPlus/tree/master/Examples/PcapSplitter">PcapSplitter</a> which is part of the <a href="https://github.com/seladb/PcapPlusPlus">PcapPlusPlus</a> suite. It's cross-platform so it can run on both Windows, Linux and Mac OS X. There's also a binary version for several OS's <a href="https://www.dropbox.com/sh/5go4ca778nu4zrm/AABbpDieIPBWQ0sGFNCWU7mza?dl=0">here</a>. It can process large pcap files containing large amount of streams (both TCP and UDP). You should use it as follows:</p><pre><code>./PcapSplitter -f /path/to/your/file.pcap -o /output/dir -m connection</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '16, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/0b6fc0687623a56d9f42c88153062754?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seladb&#39;s gravatar image" /><p>seladb<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seladb has no accepted answers">0%</span></p></div></div><div id="comments-container-54257" class="comments-container"></div><div id="comment-tools-54257" class="comment-tools"></div><div class="clear"></div><div id="comment-54257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

