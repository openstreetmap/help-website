+++
type = "question"
title = "tshark and tcpreplay together?"
description = '''I&#x27;ve got a python script that launches tshark and then uses tcpreplay to inject packets onto a small network. After tshark stops capturing and writes a pcap to disk, I attempt to use another tshark call to translate that capture to text for parsing. This last bit doesn&#x27;t work. I see &#x27;tshark: Unrecog...'''
date = "2013-09-25T11:23:00Z"
lastmod = "2013-09-25T13:32:00Z"
weight = 25230
keywords = [ "python", "tcpreplay", "tshark" ]
aliases = [ "/questions/25230" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark and tcpreplay together?](/questions/25230/tshark-and-tcpreplay-together)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25230-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've got a python script that launches tshark and then uses tcpreplay to inject packets onto a small network. After tshark stops capturing and writes a pcap to disk, I attempt to use another tshark call to translate that capture to text for parsing. This last bit doesn't work. I see 'tshark: Unrecognized libpcap format' on screen. Code looks like this:</p><pre><code># Capture and Translate calls for tshark
tsharkCapture =  shlex.split(&quot;tshark -a duration:%s -i %s -F libpcap -w %s&quot; % (10, &quot;eth0&quot;, &quot;result.pcap&quot;))
tsharkTranslate = shlex.split(&quot;tshark -i - -V&quot;)

# Replay call for tcpreplay
tcpreplayCall = shlex.split(&quot;tcpreplay --intf1 %s --enable-file-cache --timer=gtod --quiet --loop=%s --pps=%s %s&quot; % (&quot;eth0&quot;, 1, 1, &quot;replay.pcap&quot;))

# start up tshark to generate a pcap file, which will (hopefully!) hold the relevant traffic
tsharkProc = subprocess.Popen(tsharkCapture, bufsize=0)

# snooze a bit, launch the replay file
time.sleep(1)
tcpreplayProc = subprocess.Popen(tcpreplayCall)

# wait for the tshark capture process to terminate
tsharkProc.poll()
while tsharkProc.returncode == None:
    time.sleep(0.1)
    tsharkProc.poll()

# translate the pcap capture to a txt file
tsharkProc = subprocess.Popen(tsharkTranslate,
                              stdin=open(&quot;result.pcap&quot;, &quot;rb&quot;),
                              stdout=open(&quot;result.txt&quot;, &quot;wb&quot;))

# wait for the translation process to terminate
tsharkProc.poll()
while tsharkProc.returncode == None:
    time.sleep(0.1)
    tsharkProc.poll()</code></pre><p>The calls themselves appear correct. Tshark captures, tcpreplay replays 'replay.pcap', tshark writes 'result.pcap' to file, and this file contains what it should. 'result.txt' is empty however.</p><p>If (just to see) I replace 'result.pcap' with 'replay.pcap' in the translate call, there is no error, and 'result.txt' has what I expect. If I comment out the replay launch (with 'result.pcap' in the translate call), there is again no error, and 'result.txt' has what I would expect.</p><p>It really looks like the issue is with running tshark, then tcpreplay, and finally tshark to translate to text--all those things together.</p><p>I would be happy to have the first tshark call write the 'result.txt' file directly rather than using a second call to write it out, but I haven't had luck with that either.</p><p>I can open 'result.pcap' with Wireshark and export the file to text without any issues.</p><p>FYI 'replay.pcap' is generated using text2pcap, from this:</p><pre><code>0000  00 40 ae 00 47 e3 00 02 b3 11 11 11 00 14 82 82  End
0010  03 01 04 02 73 21 0e 0c 02 00 21 98 1e 09 4c 19  End
0020  00 1f                                            End</code></pre><p>What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags">python tcpreplay tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '13, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/6b1667d5ede510b48d36f58da1c5282d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ozymandias&#39;s gravatar image" /><p>ozymandias<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ozymandias has no accepted answers">0%</span></p></div></div><div id="comments-container-25230" class="comments-container"><span id="25238"></span><div id="comment-25238" class="comment"><div id="post-25238-score" class="comment-score"></div><div class="comment-text"><blockquote><p>If (just to see) I <strong>replace 'result.pcap' with 'replay.pcap'</strong> in the translate call, <strong>there is no error</strong>,</p></blockquote><p>what is the output of the following commands:</p><blockquote><p>capinfos result.pcap<br />
file result.pcap<br />
od -x result.pcap | head 20</p></blockquote></div><div id="comment-25238-info" class="comment-info"><span class="comment-age">(25 Sep '13, 12:44)</span> Kurt Knochner ♦</div></div><span id="25239"></span><div id="comment-25239" class="comment"><div id="post-25239-score" class="comment-score"></div><div class="comment-text"><pre><code>File name:           result.pcap
File type:           Wireshark - pcapng
File encapsulation:  Ethernet
Packet size limit:   file hdr: (not set)
Number of packets:   11
File size:           2000 bytes
Data size:           1379 bytes
Capture duration:    1 seconds
Start time:          Wed Sep 25 10:09:44 2013
End time:            Wed Sep 25 10:09:46 2013
Data byte rate:      1029.07 bytes/sec
Data bit rate:       8232.57 bits/sec
Average packet size: 125.36 bytes
Average packet rate: 8.21 packets/sec
SHA1:                bf0ded3960a96ab06573dafdd6eb9f8a98ae5012
RIPEMD160:           6df5adfe55ef1f6b45341788bf8304e3b634b76f
MD5:                 7e6659c259afd6303683c265f5e5d316
Strict time order:   True</code></pre></div><div id="comment-25239-info" class="comment-info"><span class="comment-age">(25 Sep '13, 12:51)</span> ozymandias</div></div><span id="25240"></span><div id="comment-25240" class="comment"><div id="post-25240-score" class="comment-score"></div><div class="comment-text"><p>That was capinfos above.</p><p>file result.pcap gives: result.pcap pcap-ng capture file - version 1.0</p><p>od -x result.pcap | head 20 (20 had to be left off)</p><p>0000000 0d0a 0a0d 0050 0000 3c4d 1a2b 0001 0000<br />
0000020 ffff ffff ffff ffff 0003 0015 694c 756e<br />
0000040 2078 2e33 2e32 2d30 2d34 3836 2d36 6170<br />
0000060 0065 0000 0004 000d 7544 706d 6163 2070<br />
0000100 2e31 2e38 0032 0000 0000 0000 0050 0000<br />
0000120 0001 0000 0044 0000 0001 0000 ffff 0000<br />
0000140 0002 0004 7465 3068 0009 0001 0006 0000<br />
0000160 000c 0015 694c 756e 2078 2e33 2e32 2d30<br />
0000200 2d34 3836 2d36 6170 0065 0000 0000 0000<br />
0000220 0044 0000 0006 0000 005c 0000 0000 0000<br />
</p></div><div id="comment-25240-info" class="comment-info"><span class="comment-age">(25 Sep '13, 13:12)</span> ozymandias</div></div></div><div id="comment-tools-25230" class="comment-tools"></div><div class="clear"></div><div id="comment-25230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25241"></span>

<div id="answer-container-25241" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25241-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>File name:           result.pcap
File type:           Wireshark - pcapng</code></pre><p>O.K. capinfos shows it's a pcap-ng file.</p><blockquote><p>I see 'tshark: Unrecognized libpcap format' on screen.</p></blockquote><p>well, the error must be related to the way you run tshark.</p><p>Why do you call it this way</p><blockquote><p>tsharkTranslate = shlex.split("tshark -i - -V")</p></blockquote><p>and not this way:</p><pre><code>tsharkTranslate = shlex.split(&quot;tshark -nr result.pcap -V&quot;) 
tsharkProc = subprocess.Popen(tsharkTranslate,stdout=open(&quot;result.txt&quot;, &quot;wb&quot;))</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '13, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '13, 13:34</p></div></div><div id="comments-container-25241" class="comments-container"><span id="25244"></span><div id="comment-25244" class="comment"><div id="post-25244-score" class="comment-score"></div><div class="comment-text"><p>That works! I did it the way I did out of ignorance, which thanks to your answer, is a little less than it was before.</p><p>Thanks much.</p></div><div id="comment-25244-info" class="comment-info"><span class="comment-age">(25 Sep '13, 14:04)</span> ozymandias</div></div><span id="25245"></span><div id="comment-25245" class="comment"><div id="post-25245-score" class="comment-score"></div><div class="comment-text"><p>good.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-25245-info" class="comment-info"><span class="comment-age">(25 Sep '13, 14:06)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25241" class="comment-tools"></div><div class="clear"></div><div id="comment-25241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

