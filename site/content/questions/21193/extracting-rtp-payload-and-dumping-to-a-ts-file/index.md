+++
type = "question"
title = "Extracting RTP payload and dumping to a ts file"
description = '''Hi guys, I&#x27;ve looked around but haven&#x27;t been able to find anything that works. How would I extract the RTP payload and dump it to a ts file via the command line interface? Through the GUI, I can simply Decode as RTP and then &#x27;Save payload&#x27; for the filtered packets, but haven&#x27;t been able to succeed w...'''
date = "2013-05-16T12:17:00Z"
lastmod = "2013-05-16T13:19:00Z"
weight = 21193
keywords = [ "decapsulation", "udp", "extract", "rtp", "payload" ]
aliases = [ "/questions/21193" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Extracting RTP payload and dumping to a ts file](/questions/21193/extracting-rtp-payload-and-dumping-to-a-ts-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21193-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I've looked around but haven't been able to find anything that works.</p><p>How would I extract the RTP payload and dump it to a ts file via the command line interface? Through the GUI, I can simply Decode as RTP and then 'Save payload' for the filtered packets, but haven't been able to succeed with doing this through tshark.</p><p>Thanks very much! Jero</p></div><div id="question-tags" class="tags-container tags">decapsulation udp extract rtp payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '13, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/4ec4ab693b8f9dcd0d91625695f09b1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sheh&#39;s gravatar image" /><p>Sheh<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sheh has no accepted answers">0%</span></p></div></div><div id="comments-container-21193" class="comments-container"></div><div id="comment-tools-21193" class="comment-tools"></div><div class="clear"></div><div id="comment-21193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21194"></span>

<div id="answer-container-21194" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21194-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could possibly do it with some scripting, by parsing the PDML output of tshark or by using the output of this command:</p><blockquote><p>tshark -nr rtp.pcap -R rtp -T fields -e rtp.payload<br />
</p></blockquote><p>but there are other tools that can do it for you automatically.</p><blockquote><p><a href="http://wiki.wireshark.org/RtpDumpScript">http://wiki.wireshark.org/RtpDumpScript</a><br />
<a href="http://cpansearch.perl.org/src/SULLR/Net-Inspect-0.29/tools/rtpxtract.pl">http://cpansearch.perl.org/src/SULLR/Net-Inspect-0.29/tools/rtpxtract.pl</a><br />
</p></blockquote><p>See also my answer to a similar question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/10493/can-tshark-extract-voice-data-from-an-rtp-stream">http://ask.wireshark.org/questions/10493/can-tshark-extract-voice-data-from-an-rtp-stream</a></p></blockquote><p>Something different, but also nice (using tshark)</p><blockquote><p><a href="http://www.e-c-group.com/software/ecg_extract_call/">http://www.e-c-group.com/software/ecg_extract_call/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '13, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '13, 13:38</p></div></div><div id="comments-container-21194" class="comments-container"><span id="21427"></span><div id="comment-21427" class="comment"><div id="post-21427-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Kurt. I was able to get the stream to decode as RTP using the -d option as follows:</p><p>tshark -r "my.pcap" -R udp.port==&lt;src port=""&gt; -d udp.port==&lt;src port=""&gt;,rtp -T fields -e rtp.payload -w "my_ts.ts"</p><p>However, at this point the dumped file is 12.9mb and does not play in VLC. If i use the RTP stream analysis "Save payload" option from the GUI, the file size is 12.1mb. I guess I need to figure out what additional content is being dumped...</p></div><div id="comment-21427-info" class="comment-info"><span class="comment-age">(23 May '13, 16:29)</span> Sheh</div></div><span id="21432"></span><div id="comment-21432" class="comment"><div id="post-21432-score" class="comment-score"></div><div class="comment-text"><p>With <code>-w "my_ts.ts"</code> tshark writes the whole packet to disk, not the output from <code>-T fields -e rtp.payload</code>. So the resulting file is a pcap file, not a media file.</p></div><div id="comment-21432-info" class="comment-info"><span class="comment-age">(24 May '13, 00:27)</span> SYN-bit ♦♦</div></div><span id="21467"></span><div id="comment-21467" class="comment"><div id="post-21467-score" class="comment-score"></div><div class="comment-text"><p>Oops my bad, thanks for catching that.</p><p>I was able to get the payload only to dump and convert to binary (very dirty though), but turns out the mp2t headers weren't being dumped. If I include that as a field as well, I first get a dump of all mp2t headers in a packet, followed up all the respective payloads.</p><p>At this point, it looks like I'll have to do what Kurt suggested earlier and get my scripts to parse the output and join (luckily the payloads are separated with commas so should be easily doable).</p></div><div id="comment-21467-info" class="comment-info"><span class="comment-age">(24 May '13, 14:22)</span> Sheh</div></div><span id="21741"></span><div id="comment-21741" class="comment"><div id="post-21741-score" class="comment-score"></div><div class="comment-text"><p>Finally got a chance to look into this again. Ended up using a dump of the 'data' field. I then stripped the RTP headers for each packet data (first 12 bytes) using a simple python script and then converted to binary (python binascii module) after concatenating.</p><p>Thanks very much for your help guys.</p></div><div id="comment-21741-info" class="comment-info"><span class="comment-age">(04 Jun '13, 07:36)</span> Sheh</div></div></div><div id="comment-tools-21194" class="comment-tools"></div><div class="clear"></div><div id="comment-21194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

