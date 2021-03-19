+++
type = "question"
title = "Can I save RTP packets without the media data?"
description = '''I have a trace where I don&#x27;t need the media inside the RTP Packets. I need the RTP headers, but not the real payload. Is it possible to discard/drop the media/payload while saving a trace?'''
date = "2012-05-16T09:12:00Z"
lastmod = "2012-05-19T22:26:00Z"
weight = 11052
keywords = [ "rtp", "payload" ]
aliases = [ "/questions/11052" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can I save RTP packets without the media data?](/questions/11052/can-i-save-rtp-packets-without-the-media-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11052-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a trace where I don't need the media inside the RTP Packets. I need the RTP headers, but not the real payload.</p><p>Is it possible to discard/drop the media/payload while saving a trace?</p></div><div id="question-tags" class="tags-container tags">rtp payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '12, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/bf08f20c55d55fc2202a904b34d89af3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramsundar%20Kandasamy&#39;s gravatar image" /><p>Ramsundar Ka...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramsundar Kandasamy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '12, 09:54</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-11052" class="comments-container"></div><div id="comment-tools-11052" class="comment-tools"></div><div class="clear"></div><div id="comment-11052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11055"></span>

<div id="answer-container-11055" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11055-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is possible. You want to set the <em>snaplen</em> of the capture.<br />
For captures taken using the Wireshark GUI by checking the "Limit each packet to" box and setting a sensible limit, then starting the capture (this option is accessed by using the "Capture Options" window to start the capture).<br />
When using <code>tshark</code>, use the <code>-s</code> option (<code>tshark -s &lt;snaplen&gt; ...</code>).<br />
For captures already taken, you can truncate each packet using <code>editcap</code> and the <code>-s</code> option (<code>editcap -s &lt;snaplen&gt; ...</code>).<br />
I do not know offhand what the <code>snaplen</code> value should be for RTP, but you should be able to determine this from one of the captures you have already taken.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '12, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span> </br></br></p></div></div><div id="comments-container-11055" class="comments-container"><span id="11142"></span><div id="comment-11142" class="comment"><div id="post-11142-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot.</p><p>It might have been better if we have an option to set snaplen for particular payload type. Eg. If RTP then set snaplen to xx bytes.</p><p>The problem is that, if we set snaplen to zz bytes and if a non rtp (say sip signalling) packet is stripped to that size it could be a problem while analyzing a trace.</p><p>Thanks, Ram</p></div><div id="comment-11142-info" class="comment-info"><span class="comment-age">(19 May '12, 08:16)</span> Ramsundar Ka...</div></div></div><div id="comment-tools-11055" class="comment-tools"></div><div class="clear"></div><div id="comment-11055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11150"></span>

<div id="answer-container-11150" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11150-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Setting the <em>snaplen</em> as @multipleinterfaces suggested is a good idea. If you want to truncate only specific packets (specified by a display filter), you can use the following <code>bash</code> script, which uses <code>tshark</code> and <a href="http://www.wireshark.org/docs/man-pages/editcap.html"><code>editcap</code></a>.</p><h4 id="snap.sh">snap.sh:</h4><pre><code>#!/bin/bash

if [ -z &quot;$1&quot; -o -z &quot;$2&quot; -o -z &quot;$3&quot; ]; then
    echo Usage: `basename $0` {infile} {snaplen} {displayfilter}
    exit 1
fi

# binaries
TSHARK=/opt/local/bin/tshark
EDITCAP=/opt/local/bin/editcap

# parameters
TMPFILE=$(mktemp pcap.XXXXXXXXXX)
INFILE=$1
OUTFILE=$1.out
SNAPLEN=$2
DFILTER=$3

cp &quot;${INFILE}&quot; &quot;${TMPFILE}&quot;

echo &quot;Filtering packets...&quot;
INPUT=$(${TSHARK} -R &quot;${DFILTER}&quot; -r &quot;${INFILE}&quot; -T fields -e frame.number)
__max=`echo ${INPUT} | wc -w`
__i=0

echo &quot;Writing pcap...&quot;
for x in ${INPUT[*]}
do
    # show progress
    ((__i++))
    printf &quot;${__i}/${__max} ($((${__i}*100/${__max}))%%)\r&quot;

    # truncate the specified packet, copy the resulting pcap
    # back to the temporary working file for the next iteration
    ${EDITCAP} -s &quot;${SNAPLEN}&quot; &quot;${TMPFILE}&quot; &quot;${OUTFILE}&quot; &quot;${x}&quot; &gt; /dev/null
    cp &quot;${OUTFILE}&quot; &quot;${TMPFILE}&quot;
done

echo
rm &quot;${TMPFILE}&quot;
echo &quot;Wrote ${OUTFILE}&quot;</code></pre><p>I tested the script on a <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=SIP_CALL_RTP_G711">sample pcap, containing SIP and RTP packets</a>. For example, to truncate all RTP packets to 12 UDP bytes (which is the RTP header length in the sample pcap), enter this:</p><pre><code>$ snap.sh SIP_CALL_RTP_G711.pcap 54 rtp.payload
Filtering packets...
Writing pcap...
1445/    1445 (100%)
Wrote SIP_CALL_RTP_G711.pcap.out</code></pre><p><sub>Note the 54 snaplen comes from the frame headers (Ethernet, IP, etc) leading up to UDP plus the length of the desired UDP payload</sub></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '12, 22:26</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></br></p></div></div><div id="comments-container-11150" class="comments-container"></div><div id="comment-tools-11150" class="comment-tools"></div><div class="clear"></div><div id="comment-11150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

