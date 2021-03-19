+++
type = "question"
title = "Reassembling TCP fragments doesn&#x27;t reassemble some packets"
description = '''I wrote a dissector named PROTOC. for some reasons this dissector doesn&#x27;t reassemble all of the protocol&#x27;s packets which can be found as [TCP segment of a reassembled PDU], But there is no trace to the reassembled PDU. Example can be seen at the attached link below of the .pcap, where TYPE D is show...'''
date = "2013-04-02T00:15:00Z"
lastmod = "2013-04-02T00:15:00Z"
weight = 20001
keywords = [ "reassembly", "tcppackets", "dissector", "wireshark" ]
aliases = [ "/questions/20001" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reassembling TCP fragments doesn't reassemble some packets](/questions/20001/reassembling-tcp-fragments-doesnt-reassemble-some-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20001-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wrote a dissector named <code>PROTOC</code>.</p><p>for some reasons this dissector doesn't reassemble all of the protocol's packets which can be found as <code>[TCP segment of a reassembled PDU]</code>, But there is no trace to the reassembled PDU. Example can be seen at the attached link below of the .pcap, where <code>TYPE D</code> is shown at the beginning of the file (type 4)(line 1 or 3), and <code>TYPE E</code> cannot be shown at the end of the file (type 5)(line 6312)</p><p>I uploaded the .pcap I'm using in order to debug my protocol <a href="http://www.cloudshark.org/captures/fdbbf1feedda">here</a> (I made this .pcap shorter, but it shows the same results on the original .pcap version, and on other .pcaps also) and the source of my protocol <a href="http://www.2shared.com/file/OGIFvV40/PROTOC.html">here</a> <strong>(DOWNLOADING PASSWORD:</strong> "wireshark"<strong>)</strong></p><p>My protocol format is:</p><ul><li>4 bytes of type</li><li>4 bytes of length</li><li>256 bytes of something called "context id"</li><li><code>length</code> bytes of data</li></ul><p>I compiled it on wireshark version 1.8.4, using x64 compiler. "Setting environment for using Microsoft Visual Studio 2010 x64 cross tools"</p><p>Compiling the dissector:</p><ol><li>get into "cmd" and writes call "C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\vcvarsall.bat"</li></ol><p>or for 64bit</p><p>call "C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\vcvarsall.bat" x86_amd64</p><ol><li>compile the dissector (in the dissector directory) nmake -f Makefile.nmake</li></ol><p>Any help will be very appreciated Thanks</p></div><div id="question-tags" class="tags-container tags">reassembly tcppackets dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '13, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/b7ccaef1113111fc5cb2bb2a0d866a4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hudac&#39;s gravatar image" /><p>hudac<br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hudac has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Apr '13, 02:24</p></div></div><div id="comments-container-20001" class="comments-container"></div><div id="comment-tools-20001" class="comment-tools"></div><div class="clear"></div><div id="comment-20001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

