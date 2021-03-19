+++
type = "question"
title = "Is it possible to use a blacklist.txt file as an input list for a wireshark | tshark displayfilter?"
description = '''Is it possible to use a blacklist.txt file as an input address list for a wireshark or tshark display filter? My current blacklist of 4000 entries errors out in the display filter box ( syntax is ok , i wonder what max number of entries is ;-) ).  I&#x27;d be very happy if something exists along the line...'''
date = "2015-08-25T07:40:00Z"
lastmod = "2015-09-01T23:54:00Z"
weight = 45344
keywords = [ "blacklist", "address-list", "input-list", "display-filter" ]
aliases = [ "/questions/45344" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Is it possible to use a blacklist.txt file as an input list for a wireshark | tshark displayfilter?](/questions/45344/is-it-possible-to-use-a-blacklisttxt-file-as-an-input-list-for-a-wireshark-tshark-displayfilter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45344-score" class="post-score" title="current number of votes">0</div><span id="post-45344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to use a blacklist.txt file as an input address list for a wireshark or tshark display filter? My current blacklist of 4000 entries errors out in the display filter box ( syntax is ok , i wonder what max number of entries is ;-) ). I'd be very happy if something exists along the lines of:</p><pre><code>for file in *.pkt
tshark.exe -r $file -Y &quot;ip.addr == blacklist.txt&quot; -w $file-toblacklist.pcap
done</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-blacklist" rel="tag" title="see questions tagged &#39;blacklist&#39;">blacklist</span> <span class="post-tag tag-link-address-list" rel="tag" title="see questions tagged &#39;address-list&#39;">address-list</span> <span class="post-tag tag-link-input-list" rel="tag" title="see questions tagged &#39;input-list&#39;">input-list</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '15, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p><span>Marc</span><br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></div></div><div id="comments-container-45344" class="comments-container"><span id="45356"></span><div id="comment-45356" class="comment"><div id="post-45356-score" class="comment-score"></div><div class="comment-text"><p>Right, the limit of the Wireshark display filter field seems to be 64K <img src="https://osqa-ask.wireshark.org/upfiles/endofipfilterrange_3q1eO7E.jpg" alt="alt text" /></p><p>which leaves room for about 2290 ip addresses in one filter pass ... so for now i guess i'll filter all files twice .. :-(</p></div><div id="comment-45356-info" class="comment-info"><span class="comment-age">(26 Aug '15, 00:04)</span> <span class="comment-user userinfo">Marc</span></div></div><span id="45357"></span><div id="comment-45357" class="comment"><div id="post-45357-score" class="comment-score"></div><div class="comment-text"><p>So much for trying that in cygwin, argument list is too long ..</p><p><img src="https://osqa-ask.wireshark.org/upfiles/arglisttoolong.jpg" alt="alt text" /></p></div><div id="comment-45357-info" class="comment-info"><span class="comment-age">(26 Aug '15, 01:15)</span> <span class="comment-user userinfo">Marc</span></div></div><span id="45502"></span><div id="comment-45502" class="comment"><div id="post-45502-score" class="comment-score"></div><div class="comment-text"><p>Do you need only a list of non-blacklisted IP addresses in the capture files, or do you want to remove frames from/to the blacklisted IPs in all capture files?</p></div><div id="comment-45502-info" class="comment-info"><span class="comment-age">(29 Aug '15, 03:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="45523"></span><div id="comment-45523" class="comment"><div id="post-45523-score" class="comment-score"></div><div class="comment-text"><p>The correlation i need is in which files do what blacklisted ip adresses occur?</p></div><div id="comment-45523-info" class="comment-info"><span class="comment-age">(30 Aug '15, 01:54)</span> <span class="comment-user userinfo">Marc</span></div></div><span id="45527"></span><div id="comment-45527" class="comment"><div id="post-45527-score" class="comment-score"></div><div class="comment-text"><p>my perl script does that. It does not output a simple list of files, it writes all frames from/to blacklisted IPs to a new file called *_blacklist.pcap. So, actually you get what you want (a list of files that contain blacklisted IPs), but it also gives you the whole communication from/to blacklisted IPs.</p></div><div id="comment-45527-info" class="comment-info"><span class="comment-age">(30 Aug '15, 02:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-45344" class="comment-tools"></div><div class="clear"></div><div id="comment-45344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="45377"></span>

<div id="answer-container-45377" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45377-score" class="post-score" title="current number of votes">1</div><span id="post-45377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Marc has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One option would be:</p><p><code>for ip in $(cat blacklist.txt); do tshark -r file.pcapng -Y ip.addr==$ip; done</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '15, 17:24</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></img></div></div><div id="comments-container-45377" class="comments-container"><span id="45491"></span><div id="comment-45491" class="comment"><div id="post-45491-score" class="comment-score"></div><div class="comment-text"><p>Thanks , that will do for the tshark part of my Q ..although i guess this will take 1 ip address at a time, filter the pcap file and then hop to the next , for 4000 ip adresses X 2183 tracefiles of 262 MB it'll be a long process...</p></div><div id="comment-45491-info" class="comment-info"><span class="comment-age">(28 Aug '15, 23:56)</span> <span class="comment-user userinfo">Marc</span></div></div><span id="45524"></span><div id="comment-45524" class="comment"><div id="post-45524-score" class="comment-score"></div><div class="comment-text"><p>In your question there was no mention of 2k trace files. The command in your last comment should be:</p><p><code>for IP in $(cat blacklist.txt); do grep "$IP" *.txt &gt;&gt; BADIPS.csv; done</code></code></p></div><div id="comment-45524-info" class="comment-info"><span class="comment-age">(30 Aug '15, 02:51)</span> <span class="comment-user userinfo">Roland</span></div></div></div><div id="comment-tools-45377" class="comment-tools"></div><div class="clear"></div><div id="comment-45377-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45380"></span>

<div id="answer-container-45380" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45380-score" class="post-score" title="current number of votes">1</div><span id="post-45380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could write a Lua plugin script to do it, running inside tshark or Wireshark. You can pass the filename(s) of your blacklist to the Lua plugin using the command line, and have the Lua plugin open the blacklist file(s) and build a match table, and have the plugin create either a post-dissector or Listener tap, which will get invoked for every packet letting you check the source and dest IP addresses against the match table; and if it matches then have the plugin either (1) add a field called "blacklisted" which you can then use as your actual display filter for tshark/wireshark, or (2) have the plugin save the blacklisted packet to a new pcap file directly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '15, 19:02</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></img></div></div><div id="comments-container-45380" class="comments-container"><span id="45492"></span><div id="comment-45492" class="comment"><div id="post-45492-score" class="comment-score"></div><div class="comment-text"><p>Ok, sweet , have to learn how to do that then ;-) But the extra possibilities do appeal to me! , Thanks!</p></div><div id="comment-45492-info" class="comment-info"><span class="comment-age">(28 Aug '15, 23:58)</span> <span class="comment-user userinfo">Marc</span></div></div></div><div id="comment-tools-45380" class="comment-tools"></div><div class="clear"></div><div id="comment-45380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45506"></span>

<div id="answer-container-45506" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45506-score" class="post-score" title="current number of votes">1</div><span id="post-45506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Based on the information provided so far, I conclude, that you want to write the packets to/from blacklisted IP addresses to a new pcap file.</p><p>If so, here is my simple Perl example. Save the code to a file and run it like this:</p><blockquote><p>perl extract_blacklist_frames.pl blacklist.txt capturefile1.pcap</p></blockquote><p>This will create a new pcap file called: <strong>capturefile1.pcap_blacklist.pcap</strong> (I did not invest any time to create a 'pretty' new name. I leave that up to you).</p><p>If you want to process several files, run it in a loop on Unix/BSD like systems with a bash</p><pre><code>for name in *.pcap
do 
echo processing file: $name
perl extract_blacklist_frames.pl blacklist.txt $name
done </code></pre><p><strong>Blacklist file:</strong> one IP per line!</p><pre><code>1.2.3.4
10.10.10.10
2.3.4.5</code></pre><p><strong>Perl code</strong>:</p><pre><code>use Net::Pcap qw(:functions);
use NetPacket::Ethernet qw(:types);
use NetPacket::IP qw(:protos);

use warnings;
use strict;

my %blacklist;

my $blacklist_file = $ARGV[0] || die (&quot;ERROR: please specifiy the name of the blacklist file\n&quot;);
my $pcap_file = $ARGV[1] || die (&quot;ERROR: please specifiy the pcap file name\n&quot;);
my $pcap_file_blacklist = $pcap_file . &quot;_blacklist.pcap&quot;;

my $pcap_read;
my $pcap_write;

read_blacklist();
process_pcap_file();

sub read_blacklist {

    open(BLACKLIST, $blacklist_file) || die (&quot;FATAL: cannot open blacklist file: $blacklist_file\n&quot;);
    while (&lt;BLACKLIST&gt;) {
        chomp;
        $blacklist{$_} = 1;
    }
    close (BLACKLIST);
}

sub process_pcap_file {

    my $err;
    my $maxpkts;

    $pcap_read = Net::Pcap::open_offline($pcap_file, \$err) || die(&quot;FATAL: cannot read pcap file $pcap_file: $err\n&quot;);
    $pcap_write = Net::Pcap::dump_open($pcap_read, $pcap_file_blacklist) || die(&quot;FATAL: cannot write pcap file $pcap_file_blacklist: $err\n&quot;);

    Net::Pcap::loop($pcap_read, $maxpkts, \&amp;process_packet, &#39;&#39;);

    Net::Pcap::close($pcap_read);
    Net::Pcap::dump_close($pcap_write);
}

sub process_packet {
    my ($user_data, $header, $packet) = @_;

    my $ip = NetPacket::IP-&gt;decode(NetPacket::Ethernet::strip($packet));
    my $src_ip = $ip-&gt;{src_ip};
    my $dst_ip = $ip-&gt;{dest_ip};

    if (exists $blacklist{$src_ip} or exists $blacklist{$dst_ip}) {
        print &quot;Blacklist IP found, writing packet\n&quot;;
        Net::Pcap::dump($pcap_write, $header, $packet);
    }
}</code></pre><p><strong>HINT:</strong> The Perl script will be able to read pcap-ng files only if the libpcap version on your system is able to read pcap-ng, otherwise the script will throw an error! If that happens, either install the latest libpcap or convert the capture files to pcap style with <strong>editcap</strong>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '15, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Aug '15, 08:08</strong> </span></p></div></div><div id="comments-container-45506" class="comments-container"><span id="45521"></span><div id="comment-45521" class="comment"><div id="post-45521-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, cool , i'll give your Perl script a try too! Sofar i've come up with:</p><pre><code>for file in *.pkt do tshark.exe -r $file -q -z conv,ip &gt;&gt; $file-IPsummary.txt;done

for IP in cat blacklist.txt; do grep &quot;$IP&quot; *.txt &gt;&gt; BADIPS.csv;done</code></pre><p>although only the first part works at the moment .. :-)</p></div><div id="comment-45521-info" class="comment-info"><span class="comment-age">(30 Aug '15, 01:51)</span> <span class="comment-user userinfo">Marc</span></div></div><span id="45522"></span><div id="comment-45522" class="comment"><div id="post-45522-score" class="comment-score"></div><div class="comment-text"><p>btw i know this should be a comment but have no clue on how to post code in a comment ..</p></div><div id="comment-45522-info" class="comment-info"><span class="comment-age">(30 Aug '15, 01:52)</span> <span class="comment-user userinfo">Marc</span></div></div><span id="45525"></span><div id="comment-45525" class="comment"><div id="post-45525-score" class="comment-score"></div><div class="comment-text"><p>I converted your answer to a comment. What I do, if I need formatting in a comment: I write the comment as an answer and if it looks O.K. in the preview I copy the text in the edit window and paste it into a commment.</p></div><div id="comment-45525-info" class="comment-info"><span class="comment-age">(30 Aug '15, 02:54)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="45587"></span><div id="comment-45587" class="comment"><div id="post-45587-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, yep, that works! Thanks for the script. I will try it out in due time , for now i stuck with the path of getting the info from the t-shark summary command and then processing it afterwards, like so ( thanks to Roland for cleaning up the second line too)<br />
</p><pre><code>for file in *.pkt do tshark.exe -r $file -q -z conv,ip &gt;&gt; $file-IPsummary.txt;done
for IP in $(cat blacklist.txt); do grep &quot;$IP&quot; *.txt &gt;&gt; BADIPS.csv; done</code></pre><p>only reason being speed at the moment ;-)</p></div><div id="comment-45587-info" class="comment-info"><span class="comment-age">(01 Sep '15, 23:54)</span> <span class="comment-user userinfo">Marc</span></div></div></div><div id="comment-tools-45506" class="comment-tools"></div><div class="clear"></div><div id="comment-45506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45421"></span>

<div id="answer-container-45421" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45421-score" class="post-score" title="current number of votes">0</div><span id="post-45421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here's a quick Python script for you. It outputs any IP addresses in the .pcap which match those in the blacklist file.</p><p>Requires Python 3. Save this as a python file (.py) and run it (./filename.py).</p><p>Change these in the code to the files you're analysing: [.pcap file = packets.pcap] [blacklist file = blklstfile]</p><pre><code>#!/usr/bin/python
import os
os.system(&quot;tshark -r packet.pcap -T fields -e ip.src | sort | uniq &gt; temp&quot;)
blklst = [line.rstrip(&quot;\n&quot;) for line in open(&quot;blklstfile&quot;)]
temp = open(&quot;temp&quot;, &quot;r&quot;)
for blkip in temp.readlines():
 blkip = blkip.rstrip(&quot;\n&quot;)
 if blkip == &quot;#&quot;:
  continue
 check = blkip
 if check!=&quot;&quot; and check in blklst:
  print(&quot;Blacklisted IP found:&quot; + check)</code></pre><p>Not quite what you're asking for but it will flag any blacklisted IP addresses if they appear in the PCAP file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Aug '15, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/6706dcd3c17a4d870b3a0d633c541c92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbm&#39;s gravatar image" /><p><span>tbm</span><br />
<span class="score" title="29 reputation points">29</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbm has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '15, 14:43</strong> </span></p></div></div><div id="comments-container-45421" class="comments-container"><span id="45493"></span><div id="comment-45493" class="comment"><div id="post-45493-score" class="comment-score"></div><div class="comment-text"><p>Right! Same here , looking like exactly what i want and all of these are different paths to get to the same answers: do i have any blacklisted ip's in a load of pcap files? It will be a bit of a learning curve do it either with Lua or Python but i will give it a whirl! However i do like the idea of letting the shark create a 'ip summary' first then automate some unix search power on those lists .. .. Something along the lines of "tshark -r &lt;pcapfile&gt; -q -z conv,ip &gt; pcapfile_ip_summary.csv" then search those "for ip in $(cat blacklist.txt); do ... .</p></div><div id="comment-45493-info" class="comment-info"><span class="comment-age">(29 Aug '15, 00:03)</span> <span class="comment-user userinfo">Marc</span></div></div></div><div id="comment-tools-45421" class="comment-tools"></div><div class="clear"></div><div id="comment-45421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

