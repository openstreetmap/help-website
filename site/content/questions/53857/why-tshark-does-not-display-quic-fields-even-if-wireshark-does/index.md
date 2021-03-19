+++
type = "question"
title = "why tshark does not display QUIC fields even if wireshark does?"
description = '''Hello, I&#x27;m trying to analyze QUIC traffic and tried Wireshark 2.1.0 with QUIC dissector on MAC El Capitan - it works great. The issue I&#x27;m having is with using tshark. When setting it to display QUIC fields it does not print information related to QUIC to stdio and when I tried &quot;-w file&quot; it writes th...'''
date = "2016-07-06T07:36:00Z"
lastmod = "2016-07-06T07:36:00Z"
weight = 53857
keywords = [ "macosx", "tshark", "quic" ]
aliases = [ "/questions/53857" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why tshark does not display QUIC fields even if wireshark does?](/questions/53857/why-tshark-does-not-display-quic-fields-even-if-wireshark-does)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53857-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,<br />
I'm trying to analyze QUIC traffic and tried Wireshark 2.1.0 with QUIC dissector on MAC El Capitan - it works great. The issue I'm having is with using tshark. When setting it to display QUIC fields it does not print information related to QUIC to stdio and when I tried <strong>"-w file"</strong> it writes this only line and exits:<br />
</p><p><strong>\M&lt;+????????8TShark (Wireshark) 2.1.0 (v2.1.0-0-g46f9217 from master)\,q???????? ,[email protected]:~/PXPRS/tests$</strong></p><p>The tshark command i'm using is this:<br />
<strong>sudo tshark -r test.pcap -w test.out -d "udp.port==12346,quic" -T fields -e udp.srcport -e quic.tags</strong></p><p>It does print everything related to the legacy protocols - udp, tcp, http etc. tshark also complains on some missing libraries when trying <strong>sudo tshark -D</strong>:<br />
</p><p><strong>dyld: Library not loaded: @rpath/libssh.4.dylib Referenced from: /Applications/Wireshark.app/Contents/MacOS/extcap/ciscodump Reason: image not found<br />
dyld: Library not loaded: @rpath/libssh.4.dylib Referenced from: /Applications/Wireshark.app/Contents/MacOS/extcap/sshdump Reason: image not found</strong></p><p>How do i fix it?<br />
Any help is greatly appreciated.</p><p>iez</p></div><div id="question-tags" class="tags-container tags">macosx tshark quic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '16, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/607514c7c1cfed6f0de7979450b85e86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iez&#39;s gravatar image" /><p>iez<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iez has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Jul '16, 07:41</p></div></div><div id="comments-container-53857" class="comments-container"><span id="53881"></span><div id="comment-53881" class="comment"><div id="post-53881-score" class="comment-score"></div><div class="comment-text"><p>Could you please file a bug on <a href="http://bugs.wireshark.org">the Wireshark bugzilla</a> and attach the <code>test.pcap</code> file, so we can try to reproduce the problem? It <em>might</em> be an issue of one-pass vs. two-pass processing.</p><blockquote><p>when I tried "-w file" it writes this only line</p></blockquote><p><code>-w</code> doesn't write lines to the file, it writes a binary <a href="http://xml2rfc.tools.ietf.org/cgi-bin/xml2rfc.cgi?url=https://raw.githubusercontent.com/pcapng/pcapng/master/draft-tuexen-opsawg-pcapng.xml&amp;modeAsFormat=html/ascii&amp;type=ascii">pcapng</a> file by default. That file can be read by TShark and Wireshark and programs that use a sufficiently recent version of libpcap - your Mac probably has a sufficiently recent version of libpcap, so the tcpdump that ships with your Mac can probably read it. It is <strong><em>NOT</em></strong>, however, a text file, so you <strong><em>CAN'T</em></strong> read it with <code>cat</code> or <code>more</code> or <code>less</code> or TextEdit or....</p><blockquote><p>dyld: Library not loaded: @rpath/libssh.4.dylib Referenced from: /Applications/Wireshark.app/Contents/MacOS/extcap/ciscodump Reason: image not found</p></blockquote><p>That might be an issue with the process of building the installation dmg for Wireshark. Try one of the 2.2.1 builds from <a href="https://www.wireshark.org/download/automated/osx/">the automated builds directory</a>.</p></div><div id="comment-53881-info" class="comment-info"><span class="comment-age">(07 Jul '16, 00:47)</span> Guy Harris ♦♦</div></div><span id="53902"></span><div id="comment-53902" class="comment"><div id="post-53902-score" class="comment-score"></div><div class="comment-text"><p>Guy, thanks for the reply. I did try 2-path processing - same result. The file produced with "-w file" is empty being opened by wireshark (size 136B). Sorry fro not being more specific. Filed a bug. Will try 2.2.1</p></div><div id="comment-53902-info" class="comment-info"><span class="comment-age">(07 Jul '16, 06:26)</span> iez</div></div></div><div id="comment-tools-53857" class="comment-tools"></div><div class="clear"></div><div id="comment-53857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

