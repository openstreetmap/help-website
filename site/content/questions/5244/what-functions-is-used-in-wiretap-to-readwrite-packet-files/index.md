+++
type = "question"
title = "What function(s) is used in wiretap to read/write packet files?"
description = '''Hi all, I am currently researching on how Wiretap in Wireshark reads the files (eg. pcap). I have gone through the README and README.developer but both of them yields no result. The Wireshark and Ethereal Network Protocol Analyzer Toolkit ebook does not explicitly show which function is called. I ha...'''
date = "2011-07-26T01:58:00Z"
lastmod = "2011-07-26T19:20:00Z"
weight = 5244
keywords = [ "wiretap", "wireshark" ]
aliases = [ "/questions/5244" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What function(s) is used in wiretap to read/write packet files?](/questions/5244/what-functions-is-used-in-wiretap-to-readwrite-packet-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5244-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I am currently researching on how Wiretap in Wireshark reads the files (eg. pcap). I have gone through the <a href="http://anonsvn.wireshark.org/wireshark/trunk/wiretap/README">README</a> and <a href="http://anonsvn.wireshark.org/wireshark/trunk/wiretap/README.developer">README.developer</a> but both of them yields no result. The <a href="http://comes.umy.ac.id/file.php/1/Pengumuman_FT/E-Book_TI/Wireshark_and_Ethereal.pdf">Wireshark and Ethereal Network Protocol Analyzer Toolkit ebook</a> does not explicitly show which function is called.</p><p>I have also gone through <a href="http://anonsvn.wireshark.org/wireshark/trunk/wiretap/wtap.c">wtap.c</a>, <a href="http://anonsvn.wireshark.org/wireshark/trunk/wiretap/wtap.h">wtap.h</a> and <a href="http://anonsvn.wireshark.org/wireshark/trunk/wiretap/wtap.def">wtap.def</a> but i still can't find my answer.</p><p>Any help and guidance is appreciated</p><p>Thanks</p><p>Regards,</p><p>Eddie Choo</p></div><div id="question-tags" class="tags-container tags">wiretap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '11, 01:58</strong></p><img src="https://secure.gravatar.com/avatar/c1dac05d0e75992546b5da006c6b718e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eddie%20choo&#39;s gravatar image" /><p>eddie choo<br />
<span class="score" title="66 reputation points">66</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eddie choo has 2 accepted answers">66%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jul '11, 01:58</p></div></div><div id="comments-container-5244" class="comments-container"></div><div id="comment-tools-5244" class="comment-tools"></div><div class="clear"></div><div id="comment-5244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5289"></span>

<div id="answer-container-5289" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5289-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>wtap_open_offline</code> opens a file; <code>wtap_read</code> reads the next sequential packet from the file; <code>wtap_seek_read</code>, if you've opened the file for both sequential and random access, will seek to the packet at the specified offset (where the offset is a value supplied by <code>wtap_read</code> for the packet in question) and read its data. <code>wtap_sequential_close</code> closes the sequential side of a file opened for both sequential and random access; <code>wtap_close</code> closes the sequential side if it hasn't already been closed, and also closes the random-access side if the file was opened for both sequential and random access, and frees up the data structure returned by <code>wtap_open_offline</code>.</p><p>Do not assume that any of these routines will remain unchanged in future Wireshark releases; if you write code that depends on them, it might have to be rewritten for a future release.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '11, 19:20</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-5289" class="comments-container"><span id="5293"></span><div id="comment-5293" class="comment"><div id="post-5293-score" class="comment-score"></div><div class="comment-text"><p>Hi Mr Guy Harris, thanks for replying to my questions I have came across one of your <a href="http://seclists.org/wireshark/2010/Apr/515">mails</a>, you have stated that winpcap/libpcap could also be used to read pcap files. May i know can i pass a file read by winpcap/libpcap directly into wireshark? or it needs to go through wiretap ? Thanks for your time</p></div><div id="comment-5293-info" class="comment-info"><span class="comment-age">(26 Jul '11, 20:35)</span> eddie choo</div></div><span id="5297"></span><div id="comment-5297" class="comment"><div id="post-5297-score" class="comment-score">1</div><div class="comment-text"><p>If a file can be <em>read</em> by libpcap/WinPcap, it's a pcap file - or, in newer versions of libpcap/WinPcap, a pcap file or a pcap-ng file - and thus can also be read by Wiretap. Wiretap is the library that Wireshark uses to read capture files, so any file that is "read ... into Wireshark" goes through Wiretap.</p></div><div id="comment-5297-info" class="comment-info"><span class="comment-age">(27 Jul '11, 00:41)</span> Guy Harris ♦♦</div></div><span id="5305"></span><div id="comment-5305" class="comment"><div id="post-5305-score" class="comment-score"></div><div class="comment-text"><p>May i know what is your advice if i wanted to use functions to read pcap files? Would you recommend using the libpcap library or the wiretap library? The wiretap library might be more suitable since i will be working on telecommunication protocols but i couldn't find any tutorials out there. libpcap is relatively easier to find its tutorials but i remember you stated somewhere that libpcap is more suitable for TCP/IP. Thanks for your help</p></div><div id="comment-5305-info" class="comment-info"><span class="comment-age">(27 Jul '11, 03:11)</span> eddie choo</div></div><span id="5322"></span><div id="comment-5322" class="comment"><div id="post-5322-score" class="comment-score">1</div><div class="comment-text"><p>If you're only going to read pcap files - or, with newer versions of libpcap, pcap-ng files that have only one link-layer type - libpcap will work just fine. If you need to read other file types, you'll need wiretap.</p><p>That has nothing to do with telecommunication protocols vs. TCP/IP, except that some telecommunications protocols are not supported by pcap and pcap-ng - but some are, e.g. MTP2.</p></div><div id="comment-5322-info" class="comment-info"><span class="comment-age">(27 Jul '11, 10:17)</span> Guy Harris ♦♦</div></div><span id="42696"></span><div id="comment-42696" class="comment"><div id="post-42696-score" class="comment-score"></div><div class="comment-text"><p>Thanks eddie choo &amp; Guy Harris for your posts i got much information about wiretap and Actually i am trying to find the file that wiretap is using to read(which libpcap format packet finally dumped for wiretap) but didnt find it,can you guys help me to get me out.</p></div><div id="comment-42696-info" class="comment-info"><span class="comment-age">(27 May '15, 05:24)</span> karun256</div></div></div><div id="comment-tools-5289" class="comment-tools"></div><div class="clear"></div><div id="comment-5289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

