+++
type = "question"
title = "Integrating wireshark with Z-Lib"
description = '''Hi, Need to understand whether you can integrate wire shark with Z LIB library. If yes what are the commercials involved in the same.  Basically need to uncompress the wireshark data captures which is compresses using Z-LIB. thanks  '''
date = "2014-03-20T11:07:00Z"
lastmod = "2014-03-20T16:26:00Z"
weight = 31003
keywords = [ "and", "zlib", "wireshark" ]
aliases = [ "/questions/31003" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Integrating wireshark with Z-Lib](/questions/31003/integrating-wireshark-with-z-lib)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31003-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Need to understand whether you can integrate wire shark with Z LIB library. If yes what are the commercials involved in the same.</p><p>Basically need to uncompress the wireshark data captures which is compresses using Z-LIB.</p><p>thanks<br />
</p></div><div id="question-tags" class="tags-container tags">and zlib wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '14, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/aec279163a2f63914f707222210c7606?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alcatel&#39;s gravatar image" /><p>alcatel<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alcatel has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Mar '14, 11:38</p></div></div><div id="comments-container-31003" class="comments-container"></div><div id="comment-tools-31003" class="comment-tools"></div><div class="clear"></div><div id="comment-31003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31005"></span>

<div id="answer-container-31005" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31005-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark binaries are already built with zlib support (see wireshark -v ; in my case: libz 1.2.5).</p><blockquote><p>Basically need to uncompress the wireshark data captures which is compresses using Z-LIB.</p></blockquote><p>Wireshark capture files (pcap or pcapng) are not compressed (although pcapng does support compression), so there is no need to uncompress those files. If you have a special capture file format, you'll have to uncompress it first and then convert it to a format that Wireshark is able to read.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '14, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31005" class="comments-container"><span id="31023"></span><div id="comment-31023" class="comment"><div id="post-31023-score" class="comment-score"></div><div class="comment-text"><p>Wireshark supports gzip (zlib) compression of <em>all</em> capture file formats - the code that handles reading gzip-compressed files is in a layer below the layer that handles particular file formats, and the routines in the upper layer all use the routines in the lower layer.</p></div><div id="comment-31023-info" class="comment-info"><span class="comment-age">(20 Mar '14, 16:27)</span> Guy Harris ♦♦</div></div><span id="31042"></span><div id="comment-31042" class="comment"><div id="post-31042-score" class="comment-score"></div><div class="comment-text"><p>Interesting, I never noticed that.</p></div><div id="comment-31042-info" class="comment-info"><span class="comment-age">(20 Mar '14, 23:26)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-31005" class="comment-tools"></div><div class="clear"></div><div id="comment-31005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31022"></span>

<div id="answer-container-31022" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31022-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Basically need to uncompress the wireshark data captures which is compresses using Z-LIB.</p></blockquote><p>A <a href="http://tools.ietf.org/html/rfc1952">gzip compressed file</a> that is a compressed version of a capture file that Wireshark can read (in <em>any</em> format that it can read) can be read by Wireshark without uncompressing the file, as long as Wireshark has been built with libz.</p><p>If Wireshark <em>hasn't</em> been built with libz, you'll need to get a version that has been built with libz. The Windows and OS X binaries we build are built with libz; other binaries may or may not be built with libz - if they're not, complain to whoever built them (your Linux distribution, your *BSD, Oracle for their Solaris 11 packaging system, etc., etc.).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '14, 16:26</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-31022" class="comments-container"><span id="31104"></span><div id="comment-31104" class="comment"><div id="post-31104-score" class="comment-score"></div><div class="comment-text"><p>Hi Harris,</p><p>Thanks for your response. Currently we are using the below version of wireshark but unable to decompress the packet captures. All the data is encrypted or compressed by our application.</p><p>Could you please suggest where i could get the lbiz integrated wireshark. If needed we are ready to purchase the same.</p><p>Version 1.10.5 (SVN Rev 54262 from /trunk-1.10)</p><p>Copyright 1998-2013 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GTK+ 2.24.14, with Cairo 1.10.2, with Pango 1.30.1, with GLib 2.34.1, with WinPcap (4_1_3), with libz 1.2.5, without POSIX capabilities,without libnl, with SMI 0.4.8, with c-ares 1.9.1, with Lua 5.1, without Python, with GnuTLS 2.12.18, with Gcrypt 1.4.6, without Kerberos, with GeoIP, with PortAudio V19-devel (built Dec 19 2013), with AirPcap.</p></div><div id="comment-31104-info" class="comment-info"><span class="comment-age">(23 Mar '14, 22:59)</span> alcatel</div></div><span id="31105"></span><div id="comment-31105" class="comment"><div id="post-31105-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Currently we are using the below version of wireshark but unable to decompress the packet captures. All the data is encrypted or compressed by our application.</p></blockquote><p>What happens if you try to use gunzip on one of your compressed files? If that doesn't work, it's probably not compressed correctly; you need to compress the files into gzip format in order for Wireshark to be able to read them. See <a href="http://tools.ietf.org/html/rfc1952">RFC 1952</a> for a description of gzip format.</p><blockquote><p>Could you please suggest where i could get the lbiz integrated wireshark.</p></blockquote><pre><code>...</code></pre><blockquote><p>Compiled (64-bit) with GTK+ 2.24.14, with Cairo 1.10.2, with Pango 1.30.1, with GLib 2.34.1, with WinPcap (4_1_3), with libz 1.2.5</p></blockquote><p>That <strong><em>IS</em></strong> a version of Wireshark with libz integrated. Your files probably aren't in gzip format, so Wireshark can't read them, even if it's linked with libz.</p></div><div id="comment-31105-info" class="comment-info"><span class="comment-age">(24 Mar '14, 02:08)</span> Guy Harris ♦♦</div></div><span id="31407"></span><div id="comment-31407" class="comment"><div id="post-31407-score" class="comment-score"></div><div class="comment-text"><p>Hi Harris,</p><p>We are compressing using RFC 1950 ZLIB compressed data format. Is it possible to uncompress the files and read it in wireshark. This is our exchange market feed which we want to read it with wireshark.</p><p>If its not possible can the wireshark developers help us in creating a plugin or decoder to do the same. Incase a sample file is required we are ready to provide it. We are ready for any commercial involved for the same.</p><p>Regards, Khalid</p></div><div id="comment-31407-info" class="comment-info"><span class="comment-age">(02 Apr '14, 09:56)</span> alcatel</div></div><span id="31411"></span><div id="comment-31411" class="comment"><div id="post-31411-score" class="comment-score"></div><div class="comment-text"><blockquote><p>We are compressing using RFC 1950 ZLIB compressed data format. Is it possible to uncompress the files and read it in wireshark. This is our exchange market feed which we want to read it with wireshark.</p></blockquote><p>If you want to read your file in the same way that Wireshark reads, for example, pcap files, you will have to add code to libwiretap (source is in the <code>wiretap</code> subdirectory) to handle that file.</p><p>Once you have done that, then, if Wireshark is being built with libz (the configure script on UN*Xes will built with libz if it finds the libz header files and library), Wireshark will <em>automatically</em> be able to read gzip-compressed versions of those files. That's the RFC 1952 format.</p><p>Wireshark includes no support for the RFC 1950 format. You will have to figure out yourself how to support that and write your own code to handle it.</p></div><div id="comment-31411-info" class="comment-info"><span class="comment-age">(02 Apr '14, 10:03)</span> Guy Harris ♦♦</div></div><span id="31420"></span><div id="comment-31420" class="comment"><div id="post-31420-score" class="comment-score"></div><div class="comment-text"><blockquote><p>We are compressing using RFC 1950 ZLIB compressed data format.<br />
This is our <strong>exchange market feed</strong> which we want to read it with wireshark.</p></blockquote><p>well, <strong>what</strong> is your <strong>data format</strong> if you uncompress it yourself? Is it a pcap file, is it raw data, anything else?</p></div><div id="comment-31420-info" class="comment-info"><span class="comment-age">(02 Apr '14, 12:33)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-31022" class="comment-tools"></div><div class="clear"></div><div id="comment-31022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

