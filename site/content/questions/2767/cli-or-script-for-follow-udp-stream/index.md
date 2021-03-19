+++
type = "question"
title = "CLI or script for &quot;Follow udp stream&quot;?"
description = '''I have many .pcap files of video multicast. To strip off the network info and keep just the video data, I have been manually doing the &quot;Follow UDP stream&quot; command, then saving those results as &quot;raw&quot; transport stream (.ts) files. The problem is that this is a very long process (&amp;gt;15 min per 250Meg ...'''
date = "2011-03-10T11:37:00Z"
lastmod = "2012-07-05T14:29:00Z"
weight = 2767
keywords = [ "follow", "udp", "cli", "script" ]
aliases = [ "/questions/2767" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [CLI or script for "Follow udp stream"?](/questions/2767/cli-or-script-for-follow-udp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2767-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2767-score" class="post-score" title="current number of votes">0</div><span id="post-2767-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have many .pcap files of video multicast. To strip off the network info and keep just the video data, I have been manually doing the "Follow UDP stream" command, then saving those results as "raw" transport stream (.ts) files. The problem is that this is a very long process (&gt;15 min per 250Meg file).</p><p>I have the proper filter needed to get just the frames I want from the .pcap files and can launch them from the CLI. My question is whether or not there is a method to do the "Follow UDP stream" part via CLI or script. If so, pointers or suggestions are GREATLY appreciated.</p><p>Thanks, Dave T.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow" rel="tag" title="see questions tagged &#39;follow&#39;">follow</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-cli" rel="tag" title="see questions tagged &#39;cli&#39;">cli</span> <span class="post-tag tag-link-script" rel="tag" title="see questions tagged &#39;script&#39;">script</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '11, 11:37</strong></p><img src="https://secure.gravatar.com/avatar/54667c36306632b68c0d90b76d23301b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveT&#39;s gravatar image" /><p><span>DaveT</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveT has no accepted answers">0%</span></p></div></div><div id="comments-container-2767" class="comments-container"><span id="12471"></span><div id="comment-12471" class="comment"><div id="post-12471-score" class="comment-score"></div><div class="comment-text"><p>Is there a layer of protocol of some kind in between the UDP and the mpeg stream?</p></div><div id="comment-12471-info" class="comment-info"><span class="comment-age">(05 Jul '12, 14:29)</span> <span class="comment-user userinfo">rakslice</span></div></div></div><div id="comment-tools-2767" class="comment-tools"></div><div class="clear"></div><div id="comment-2767-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2784"></span>

<div id="answer-container-2784" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2784-score" class="post-score" title="current number of votes">0</div><span id="post-2784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at the discussion at <a href="http://www.wireshark.org/lists/wireshark-users/200611/msg00133.html">http://www.wireshark.org/lists/wireshark-users/200611/msg00133.html</a>, it contains a little script I wrote that might help you out:</p><pre><code>#!/usr/bin/perl -w

# Just a little script written by Sake Blok ([email protected])
# to extract udp-payload data from an udp-stream.

use strict;
use English;

use Net::PcapUtils;
use NetPacket::Ethernet qw(:strip);
use NetPacket::IP;
use NetPacket::UDP;

my $packet_nr=0;

sub process_pkt {
   my($arg, $hdr, $pkt) = @_;

   my $ip_obj = NetPacket::IP-&gt;decode(eth_strip($pkt));
   my $udp_obj = NetPacket::UDP-&gt;decode($ip_obj-&gt;{data});

   $packet_nr++;

   printf OUT &quot;%s&quot;,$udp_obj-&gt;{data};
}

my $infile = shift || die &quot;Usage: $0 &lt;infile&gt; &lt;outfile&gt;\n&quot;;
my $outfile = shift || die &quot;Usage: $0 &lt;infile&gt; &lt;outfile&gt;\n&quot;;

open(OUT,&quot;&gt;$outfile&quot;);
Net::PcapUtils::loop(\&amp;process_pkt, (SAVEFILE =&gt; $infile, FILTER =&gt; &#39;udp&#39;));
close(OUT);</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '11, 04:02</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2784" class="comments-container"><span id="2786"></span><div id="comment-2786" class="comment"><div id="post-2786-score" class="comment-score"></div><div class="comment-text"><p>I'll give it a try.</p><p>Thanks!</p><p>Dave</p></div><div id="comment-2786-info" class="comment-info"><span class="comment-age">(11 Mar '11, 07:34)</span> <span class="comment-user userinfo">DaveT</span></div></div><span id="2787"></span><div id="comment-2787" class="comment"><div id="post-2787-score" class="comment-score"></div><div class="comment-text"><p>Converted to a comment in keeping with the philosophy of this site.</p><p>See the FAQ for further info....</p></div><div id="comment-2787-info" class="comment-info"><span class="comment-age">(11 Mar '11, 07:41)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="10188"></span><div id="comment-10188" class="comment"><div id="post-10188-score" class="comment-score"></div><div class="comment-text"><p>With a minor modification to the perl script, one can recapture the udpflow as an rtptools dump file.</p><p>Here are the changes:</p><p>1) add "OUT-&gt;autoflush(1);" after the open statement</p><p>2) add "use IO::Handle;" to the end of the package include list</p><p>Now you can do something like this:</p><p>In one window...</p><p>$ rtpdump -Fhex localhost/60004</p><p>In another window...</p><p>$ tshark -r aaa.pcap -w- rtp | ./udpflow - - | nc -u localhost 60004</p><p>"udpflow" is our little wrapped up/chmod +x perl script. (Note: the udpflow pipeline must be run as root. I haven't figured out how to turn off perl's "taint mode")</p><p>"nc" is the linux netcat command (a handy dandy general purpose tcp/udp socket utility)</p><p>The change I've suggested causes the udpflow script to flush its output to the nc cmd with each write thus resulting in a single udp datagram w/ rtp payload for each upd packet in the flow (rtp has no length field. an rtp packet is framed by its udp transport packet.) The rtpdump utility dumps the rec'd rtp flow as an ascii representation w/ hex payload.</p><p>From there one can pump the resulting dump file into other tools to play the media stream. (See eg. <a href="http://wiki.wireshark.org/RTP_statistics)">http://wiki.wireshark.org/RTP_statistics)</a></p></div><div id="comment-10188-info" class="comment-info"><span class="comment-age">(16 Apr '12, 07:30)</span> <span class="comment-user userinfo">rroy</span></div></div></div><div id="comment-tools-2784" class="comment-tools"></div><div class="clear"></div><div id="comment-2784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

