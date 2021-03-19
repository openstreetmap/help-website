+++
type = "question"
title = "how do I configure dumpcap from tshark while pipeing the tshark output to my program?"
description = '''I&#x27;m trying to configure tshark to instruct dumpcap to create a raw network data capture ring buffer in ram disk while pipeing the filtered packets output by tshark to my program. It worked fine UNTIL I tried to set up a ring buffer in ram. I now get this error message: tshark: Read filters aren&#x27;t su...'''
date = "2014-12-12T17:54:00Z"
lastmod = "2014-12-17T14:46:00Z"
weight = 38546
keywords = [ "tshark", "ringbuffer", "dumpcap" ]
aliases = [ "/questions/38546" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how do I configure dumpcap from tshark while pipeing the tshark output to my program?](/questions/38546/how-do-i-configure-dumpcap-from-tshark-while-pipeing-the-tshark-output-to-my-program)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38546-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to configure tshark to instruct dumpcap to create a raw network data capture ring buffer in ram disk while pipeing the filtered packets output by tshark to my program. It worked fine UNTIL I tried to set up a ring buffer in ram. I now get this error message:</p><p>tshark: Read filters aren't supported when capturing and saving the captured packets.</p><p>Here's my tshark command line:</p><p>/usr/bin/tshark -nn -t e -i wlan0 -R "wlan.fc.type==0 and wlan.fc.subtype==4" -e frame.time -e wlan.sa -e radiotap.dbm_antsignal -Tfields -E separator=, -l -b files:10 -b filesize:10000 -w /var/tmp/wlan0_capture | &lt;my_program&gt;.sh &amp;</p><p>I've set wlan0 into monitormode. I'm running all the latest code on Raspian.</p><p>How do I fix this ? Thank you in advance.</p></div><div id="question-tags" class="tags-container tags">tshark ringbuffer dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '14, 17:54</strong></p><img src="https://secure.gravatar.com/avatar/a07a2459f82b7e0994552a4088be7857?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NewtownGuy&#39;s gravatar image" /><p>NewtownGuy<br />
<span class="score" title="9 reputation points">9</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NewtownGuy has no accepted answers">0%</span></p></div></div><div id="comments-container-38546" class="comments-container"></div><div id="comment-tools-38546" class="comment-tools"></div><div class="clear"></div><div id="comment-38546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38568"></span>

<div id="answer-container-38568" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38568-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Read filters are only supported when reading a capture from file. For capture filtering, you need to use a capture filter which uses the limited pcap filter format rather than the more expressive wireshark display filter format.</p><p>Have a look at the <code>pcap-filter</code> manual page. You probably need to replace <code>-R "wlan.fc.type == 0 and wlan.fc.subtype == 4"</code> by:</p><pre><code>-f &#39;type 0 subtype 4`</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '14, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-38568" class="comments-container"><span id="38572"></span><div id="comment-38572" class="comment"><div id="post-38572-score" class="comment-score"></div><div class="comment-text"><p>Thank you, but the -R format works so long as I don't use the -b and -w options. Is there a performance difference between -R and -f ?</p><p>How do I tell dumpcap, through the tshark command line, to create a circular buffer at a particular location ? Maybe tshark is getting confused by -w, which I'm trying to use to create the capture buffer, rather than the output from tshark. The dumpcap spec says to use -w, and I'm assuming tshark passes commands through to dumpcap.</p></div><div id="comment-38572-info" class="comment-info"><span class="comment-age">(15 Dec '14, 07:08)</span> NewtownGuy</div></div><span id="38573"></span><div id="comment-38573" class="comment"><div id="post-38573-score" class="comment-score"></div><div class="comment-text"><p>@NewtownGuy</p><p>A display filter with the -R option is incompatible with -w, that's why you have to use the capture filter option -f and adapt the syntax accordingly.</p><p>For a circular buffer use the -b option, and as it is only usable with the -w option, again this is not compatible with a -R display filter, you have to use -f capture filter.</p></div><div id="comment-38573-info" class="comment-info"><span class="comment-age">(15 Dec '14, 07:18)</span> grahamb ♦</div></div><span id="38580"></span><div id="comment-38580" class="comment"><div id="post-38580-score" class="comment-score"></div><div class="comment-text"><p>Thank you. How does tshark know that -w /path/filename, when used with -b filesize:10000 -b file:10, applies to dumpcap and not its outfile ?</p></div><div id="comment-38580-info" class="comment-info"><span class="comment-age">(15 Dec '14, 08:15)</span> NewtownGuy</div></div><span id="38592"></span><div id="comment-38592" class="comment"><div id="post-38592-score" class="comment-score"></div><div class="comment-text"><p>Here's my revised command line using -f, -b and -w, but it does not work. It creates a 160-byte binary file at /var/tmp/capture_wlan0_xxx, but it's static. The manual for tshark says the -b and -w options control the (output?) file that tshark creates, but I want to control the file that dumpcap creates and feeds to tshark. I want to pipe the filtered output from tshark to myscript.sh, so if dumpcap -f does the filtering, why do I need tshark ?</p><p>/usr/bin/tshark -n -t e -i wlan0 -f "type 0 subtype 4" -e frame.time -e wlan.sa -e radiotap.dbm_antsignal -T fields -E separator=, -l -b files:10 -b filesize:10000 -w /var/tmp/capture_wlan0 | /path/myscript.sh &amp;</p><p>How should I fix this ?</p><p>Thank you.</p></div><div id="comment-38592-info" class="comment-info"><span class="comment-age">(15 Dec '14, 15:06)</span> NewtownGuy</div></div><span id="38596"></span><div id="comment-38596" class="comment"><div id="post-38596-score" class="comment-score"></div><div class="comment-text"><p>What version of tshark are you using? Using multiple files and -T fields output works for me with 1.99-2.</p><p>You need tshark to dissect the data and produce the fields you are piping to myscript.sh. Dumpcap handles the capturing and file writing, and it pipes the data to tshark which then dissects the data and outputs the text.</p><p>You seem to be confused by the filtering. You are using capture filtering (performed by dumpcap) using the -f option that filters what is fed to the dissection engine (libwireshark, which is part of tshark and Wireshark) and what is saved into the capture files, and then output field selection by tshark using the -T fields -e xxx options.</p><p>There are also display filters (tshark -R and -Y options) that restrict output, but do not affect what is captured.</p><p>See this <a href="https://ask.wireshark.org/questions/6660/what-is-the-difference-between-capture-filter-and-display-filter">question</a> on the differences between capture and display filters for more info.</p></div><div id="comment-38596-info" class="comment-info"><span class="comment-age">(16 Dec '14, 05:28)</span> grahamb ♦</div></div><span id="38609"></span><div id="comment-38609" class="comment not_top_scorer"><div id="post-38609-score" class="comment-score"></div><div class="comment-text"><p>I'm running tshark 1.8.2-5wheez. I looked for the dumpcap version, but it's not listed in dpkg --list, so it must be embedded in tshark.</p><p>I'm confused by the -w option because tshark uses it to write its output file, but dumpcap uses it to write its capture file. While I don't need tshark to write its output to a file (only a pipe), it's not clear to me if there's a way to write a tshark command line that pipes its output to a script, while using -w to control the capture file created by dumpcap. It seems to me that tshark needs one parameter to write its output file, and a different parameter to tell dumpcap where to write its capture file that is fed into tshark.</p><p>I'm also confused by dumpcap filtering. Unless the cpu is awfully fast, I don't see how it can process a high data rate without buffering to a file first, so it doesn't drop packets. I'm seeing occasional dropped packets now on my wireless interfaces, without any filtering.</p><p>If I were able to get dumpcap to write a filtered capture file to ram disk, and thus greatly reduce how much is written to disk, can tshark format it and pipe it to my script in real time ?</p></div><div id="comment-38609-info" class="comment-info"><span class="comment-age">(17 Dec '14, 09:14)</span> NewtownGuy</div></div><span id="38610"></span><div id="comment-38610" class="comment not_top_scorer"><div id="post-38610-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>You're running a somewhat old version, current stable is 1.12.2, there may be some issues there. Certainly what you are attempting to do works for me using 1.12.2.</p><p>When capturing, tshark (and Wireshark) start dumpcap to make the capture and write out the capture files. dumpcap also feeds the packets to tshark (and Wireshark) over a pipe. tshark (and Wireshark) then process the packets for output at their own rate, possibly leading to lag behind the actual capture.</p><p>A capture filter (or dumpcap filtering as you call it) is a high performance filter using bpf. The high performance requirements dictate the less extensive filtering capabilities. The packets are buffered by the kernel in the capturing mechanism and packets can be dropped, usually when using very high line rate, e.g. 10GBe. The fact that line rates exceed disk I/O rates is one reason for capture filtering so that the torrent of packets from a high line rate can be reduced to something that the disk I/O can handle.</p><p>Dumpcap does write the capture filtered file to disk, but there is no mechanism for tshark (or Wireshark) to read that capture file, instead, as I've described, they consume packets from dumpcap via a pipe.</p><p>Hopefully you are aware that running tshark continuously in this manner will cause tshark to eventually run out of memory due to maintain state about conversations?</p></div><div id="comment-38610-info" class="comment-info"><span class="comment-age">(17 Dec '14, 10:34)</span> grahamb ♦</div></div></div><div id="comment-tools-38568" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-38568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38612"></span>

<div id="answer-container-38612" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38612-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you don't mind a lag between when <code>dumpcap</code> finishes writing to a particular file of the ringbuffer and when <code>tshark</code> processes that file, then the following script <em>might</em> be of use to you. I don't claim to be a script expert, so improvements are certainly possible.</p><p>This script was tested using Wireshark 1.12.1 command-line tools, so it may not run with your version of Wiresshark. For example, you may need to replace the "<code>-Y</code>" option with "<code>-R</code>".</p><pre><code>#!/bin/sh
# This script starts dumpcap with ring buffer settings and then feeds a
# completed capture file to tshark for further processing.
#
# The tshark output will lag because it must wait for a capture file to be
# fully written first.
#
# When dumpcap terminates, the last capture file in progress will be processed
# by tshark.

# Check usage
if (( $# &lt; 1 ))
then
    &lt;tab&gt;echo &quot;Usage: $0 &lt; prefix &gt;&quot;
    &lt;tab&gt;exit 0
fi

# Cleanup any old lingering files or processes ...
killall dumpcap tshark &amp;&gt; /dev/null

###################################
# Initialize stuff, edit as needed.
prefix=$1_`date +%s`

# dumpcap-specific
interface=&quot;eth0&quot;
capfilter=&quot;icmp&quot;
ringbuffer=&quot;-b files:10 -b filesize:10&quot;

# tshark-specific
filter=&quot;icmp&quot;
fields=&quot;-T fields -E separator=, -e frame.number -e frame.time_epoch&quot;

########################################
# Start dumpcap and save its process ID
dumpcap -q -i $interface -f &quot;$capfilter&quot; $ringbuffer -w $prefix &amp;
sleep 1
dcpid=`pidof dumpcap`
pid=$dcpid

let count=1
let next=$(( (count + 1) % 100000))

curfile=$( ls -1 `printf ${prefix}_%05d_* $count` )

#################################################
# Process one complete ring buffer file at a time
while [[ $dcpid = $pid ]]
do
    sleep 1
    # See if dumpcap is done with the current file
    nextfile=$( ls -1 `printf ${prefix}_%05d_* $next` 2&gt; /dev/null )
    if [[ -f $nextfile ]]
    then
        tshark -r $curfile -Y &quot;$filter&quot; $fields | ./myscript.sh
        curfile=$nextfile
        let count=$next
        let next=$(( (count + 1) % 100000))
    fi
    pid=`pidof dumpcap`
done

tshark -r $curfile -Y &quot;$filter&quot; $fields | ./myscript.sh

# Final cleanup (useful during testing)
killall dumpcap tshark &amp;&gt; /dev/null</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '14, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-38612" class="comments-container"><span id="38614"></span><div id="comment-38614" class="comment"><div id="post-38614-score" class="comment-score"></div><div class="comment-text"><p>To: cmaynard</p><p>Wow. I appreciate the effort you put in to this. Thank you.</p><p>But there are three problems:</p><p>1) I need a real time output, so I can't wait for a file to fill.</p><p>2) I need to run multiple instances of tshark/dumpcap simultaneously, one for each of several wireless interfaces. I can't use killall because it would take all of them down. I can't use pidof because there are multiple instances of dumpcap.</p><p>3) Killing a top level process does not always kill its child processes. I get the pid from running the tshark command, and I've tried 'kill -1 pid' (that's minus one) and 'kill -9 pid', but they sometimes leave dumpcap running. Is there any guaranteed way to kill tshark and have it take down dumpcap, too ?</p></div><div id="comment-38614-info" class="comment-info"><span class="comment-age">(17 Dec '14, 17:07)</span> NewtownGuy</div></div><span id="38616"></span><div id="comment-38616" class="comment"><div id="post-38616-score" class="comment-score"></div><div class="comment-text"><p>Regarding points 2 and 3:</p><pre><code>2. You really don&#39;t need to `killall` at all.  I only added it during testing, but it&#39;s not needed.  You can  pass the interface to the script.
3. To test if the `dumpcap` is still running, you can always pass the process ID of the `dumpcap` instance to the script. [EDIT: Passing the pid to the script naturally means starting up `dumpcap` outside of the script.  If you still wanted to launch `dumpcap` from within the script, then in order to obtain the pid of specific `dumpcap` instance just started, you could parse `pidof dumpcap` output by grepping each `/proc/pid/cmdline` for the relevant interface.  There may be other ways to accomplish the same thing.]</code></pre><p>Unfortunately, I can't think of a way to address point #1. Perhaps someone else has an idea?</p></div><div id="comment-38616-info" class="comment-info"><span class="comment-age">(17 Dec '14, 19:33)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-38612" class="comment-tools"></div><div class="clear"></div><div id="comment-38612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

