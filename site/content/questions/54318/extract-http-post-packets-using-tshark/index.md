+++
type = "question"
title = "Extract HTTP POST packets using tshark"
description = '''Hello. I have a capture file named original.pcap from a wifi capture I did. When I open it in Wireshark and properly configure decryption, I can see two HTTP POST packets. When I double-click any of those packets, I got a window that shows me the packet in three different view modes (Frame, Decrypte...'''
date = "2016-07-25T16:19:00Z"
lastmod = "2016-07-26T10:41:00Z"
weight = 54318
keywords = [ "decryption", "post", "wifi", "http", "tshark" ]
aliases = [ "/questions/54318" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Extract HTTP POST packets using tshark](/questions/54318/extract-http-post-packets-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54318-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello.</p><p>I have a capture file named <strong>original.pcap</strong> from a <strong>wifi</strong> capture I did. When I open it in Wireshark and properly configure decryption, I can see two HTTP POST packets. When I double-click any of those packets, I got a window that shows me the packet in three different view modes (Frame, Decrypted CCMP data and Reassembled TCP). So far, so good.</p><p>Now, I'm trying to create a new file named <strong>post.pcap</strong> using tshark with those HTTP POST packets only. I tried the following command (no copy/paste here, please ignore any typos):</p><pre><code>tshark -r original.pcap -o wlan.enable_decryption:TRUE -o &quot;uat:80211_keys:\&quot;wpa-pwd\&quot;,\&quot; MyPassword:MySSID\&quot;&quot; -Y &quot;http.request.method == &quot;POST&quot; or eapol&quot; -w post.pcap</code></pre><p>I used UAT to config decryption in tshark. Also, I extracted eapol packets so tshark can do the decryption.</p><p>But when I open <strong>post.pcap</strong> in Wireshark, I can see the EAPOL packets and just two TCP packets, not the HTTP packets I was expecting. If I double-click one of those TCP packets, I can see it is related to the original HTTP POST, but it shows me only two view modes (Frame and Decrypted CCMP data). It seems that I need more packets in the original file in order to properly show the HTTP packets.</p><p>How can I make tshark extract the right combination of packets?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">decryption post wifi http tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '16, 16:19</strong></p><img src="https://secure.gravatar.com/avatar/54559ac204942f500ad5382cdc8dcc46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="santonline&#39;s gravatar image" /><p>santonline<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="santonline has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jul '16, 16:20</p></div></div><div id="comments-container-54318" class="comments-container"></div><div id="comment-tools-54318" class="comment-tools"></div><div class="clear"></div><div id="comment-54318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54347"></span>

<div id="answer-container-54347" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54347-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There may be a way to accomplish this in a single step (possibly using <a href="https://wiki.wireshark.org/Mate">MATE</a> or some other method?), but you should be able to at least use a 2-step approach to have <code>tshark</code> extract the packets you need.</p><p>First, find the relevant TCP stream(s) (options omitted for brevity and clarity):</p><pre><code>tshark -r original.pcap -Y &quot;http.request.method == &quot;POST&quot;&quot; -T fields -e tcp.stream</code></pre><p>(For illustrative purposes, let's suppose there are 2 matching streams, numbers 1 and 3.)</p><p>Second, modify the filter to include the entire stream and save those packets to your file:</p><pre><code>tshark -r original.pcap -Y &quot;tcp.stream eq 1 or tcp.stream eq 3 or eapol&quot; -w post.pcap</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '16, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jul '16, 10:50</p></div></div><div id="comments-container-54347" class="comments-container"><span id="54378"></span><div id="comment-54378" class="comment"><div id="post-54378-score" class="comment-score"></div><div class="comment-text"><p>Thank you, but I forgot to mention that I want to make a script out of it. Is there a way pass the stream IDs to the filter in the second command automatically?</p></div><div id="comment-54378-info" class="comment-info"><span class="comment-age">(27 Jul '16, 12:02)</span> santonline</div></div><span id="54379"></span><div id="comment-54379" class="comment"><div id="post-54379-score" class="comment-score"></div><div class="comment-text"><p>Below is my attempt at a script that should get you more or less what you want. It can produce either a single <code>.pcapng</code> file with all streams in one file, or it can produce a separate <code>.pcapng</code> file, one for each stream.</p><pre><code>#!/bin/sh
# Usage: post.sh &lt;infile&gt; &lt;outfileprefix&gt; [unified]

if [ ${#} -lt 2 ] ; then
        echo &quot;Usage: $0 &lt;infile&gt; &lt;outfileprefix&gt; [unified]&quot;
        exit 0
fi

infile=${1}
outfile_pfx=${2}

unified=0
if [ ${#} -gt 2 ] ; then
        if [ &quot;${3}&quot; == &quot;unified&quot; ] ; then
                unified=1
        fi
fi

if [ ${unified} -eq 0 ] ; then
        for stream in $(tshark -r ${infile} -o wlan.enable_decryption:TRUE -Y &quot;http.request.method==\&quot;POST\&quot;&quot; -T fields -e tcp.stream | sort -u | tr -d &#39;\r&#39;)
        do
                tshark -r ${infile} -o wlan.enable_decryption:TRUE -Y &quot;tcp.stream eq ${stream} or eapol&quot; -w ${outfile_pfx}-${stream}.pcapng
                echo &quot;Wrote ${outfile_pfx}-${stream}.pcapng&quot;
        done
else
        filter=
        for stream in $(tshark -r ${infile} -o wlan.enable_decryption:TRUE -Y &quot;http.request.method == \&quot;POST\&quot;&quot; -T fields -e tcp.stream | sort -u | tr -d &#39;\r&#39;)
        do
                if [[ -z ${filter}  ]] ; then
                        filter=&quot;tcp.stream eq ${stream}&quot;
                else
                        filter+=&quot; or tcp.stream eq ${stream}&quot;
                fi
        done

        tshark -r ${infile} -o wlan.enable_decryption:TRUE -Y &quot;${filter} or eapol&quot; -w ${outfile_pfx}.pcapng
        echo &quot;Wrote ${outfile_pfx}.pcapng&quot;
fi</code></pre></div><div id="comment-54379-info" class="comment-info"><span class="comment-age">(27 Jul '16, 13:55)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-54347" class="comment-tools"></div><div class="clear"></div><div id="comment-54347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

