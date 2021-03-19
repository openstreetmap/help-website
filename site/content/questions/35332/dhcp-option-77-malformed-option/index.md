+++
type = "question"
title = "DHCP Option 77 - malformed option"
description = '''In Windows 7 I am setting a custom DHCP client class id (DHCP Option 77) ipconfig /setclassid &quot;Local Area Connection&quot; &quot;SOME_CUSTOM_CLASS_ID&quot;  and in Wireshark I am capturing the DHCP handshake. The custom class id is present in the DHCP request, but wireshark has the Option 77 info highlighed with t...'''
date = "2014-08-08T12:35:00Z"
lastmod = "2016-08-20T15:38:00Z"
weight = 35332
keywords = [ "dhcp", "option77" ]
aliases = [ "/questions/35332" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [DHCP Option 77 - malformed option](/questions/35332/dhcp-option-77-malformed-option)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35332-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In Windows 7 I am setting a custom DHCP client class id (DHCP Option 77)</p><pre><code>ipconfig /setclassid &quot;Local Area Connection&quot; &quot;SOME_CUSTOM_CLASS_ID&quot;</code></pre><p>and in Wireshark I am capturing the DHCP handshake. The custom class id is present in the DHCP request, but wireshark has the Option 77 info highlighed with the error "malformed option".</p><p>Any ideas on this? Is it a bug, either in Wireshark or Windows?</p><p><strong>Edit:</strong> using Version 1.12.0 (v1.12.0-0-g4fab41a from master-1.12)</p><p>I've discovered that the first byte of the option string is being read as the value length. In my case, "1" is interpreted as length 49, whereas it is actually the first char of my user class. Cloudshark: <a href="https://www.cloudshark.org/captures/ecc7ed937a6a">https://www.cloudshark.org/captures/ecc7ed937a6a</a></p><p>Here's a hacky edit where I'm tacking on a placeholder byte at the beginning of the class to be read as the length. E.g., my class should start "101-...", so I made it "1101-..." and padded it to 49 chars, which wireshark parses happily. Cloudshark: <a href="https://www.cloudshark.org/captures/cf0b15f11b83">https://www.cloudshark.org/captures/cf0b15f11b83</a></p></div><div id="question-tags" class="tags-container tags">dhcp option77</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Aug '14, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/9285d0800418f5faa5aba025830fc846?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Orrin&#39;s gravatar image" /><p>Orrin<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Orrin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Aug '14, 14:28</p></div></div><div id="comments-container-35332" class="comments-container"><span id="35333"></span><div id="comment-35333" class="comment"><div id="post-35333-score" class="comment-score"></div><div class="comment-text"><p>Wireshark version?</p><p>Can you post a capture contain the packet in question somewhere publicly accessible, e.g. <a href="http://cloudshark.org">Cloudshark</a>, Google Drive, Dropbox etc.</p></div><div id="comment-35333-info" class="comment-info"><span class="comment-age">(08 Aug '14, 14:06)</span> grahamb ♦</div></div><span id="35334"></span><div id="comment-35334" class="comment"><div id="post-35334-score" class="comment-score"></div><div class="comment-text"><p>@grahamb - I've edited my question to supply some extra info.</p></div><div id="comment-35334-info" class="comment-info"><span class="comment-age">(08 Aug '14, 14:28)</span> Orrin</div></div></div><div id="comment-tools-35332" class="comment-tools"></div><div class="clear"></div><div id="comment-35332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="35335"></span>

<div id="answer-container-35335" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35335-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like a bug in the DHCP client to me. <a href="http://tools.ietf.org/html/rfc3004">RFC 3004</a> states that each instance of user class data should have a 1 octet prefix of the length.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '14, 16:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35335" class="comments-container"><span id="35336"></span><div id="comment-35336" class="comment"><div id="post-35336-score" class="comment-score"></div><div class="comment-text"><p>Thanks for confirming. The Funny thing is, 3 of the RFC's authors work for Microsoft!</p></div><div id="comment-35336-info" class="comment-info"><span class="comment-age">(08 Aug '14, 16:28)</span> Orrin</div></div></div><div id="comment-tools-35335" class="comment-tools"></div><div class="clear"></div><div id="comment-35335-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55006"></span>

<div id="answer-container-55006" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55006-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This does not seem to be a bug in the DHCP client, but rather a conflicting specification. Microsoft defines DHCPv4 option code 77 as follows (see <a href="https://msdn.microsoft.com/en-us/library/dd358019.aspx">2.2.6.1 User Class Option Sent by DHCPv4 Client to DHCPv4 Server</a>):</p><pre><code>octet 0: Option Code (77, 0x4D)
octet 1: Option Length
octet 2...: User_Class_Data (variable)</code></pre><p>They recognize that it is deviating, see <a href="https://msdn.microsoft.com/en-us/library/cc227281.aspx">2.2.6 DHCPv4 Option Code 77 (0x4D) - User Class Option</a>:</p><blockquote><p>This section describes the message format of the User Class Option sent by DHCPv4 clients and DHCPv4 servers, and the values for this option that are predefined on DHCPv4 servers that implement this specification. The format of this option varies from the implementation described in [RFC3004] in that the User Class Data field format is changed. The use of this alternate format is indicated by the presence of a Vendor Class Identifier Option (section 2.2.3), which can occur anywhere in the same message.</p></blockquote><p>Upon further inspection, it appears that implementations vary in the implementation:</p><ul><li>iPXE implements the MS spec (it sends <code>77 04 "iPXE"</code>). <a href="http://forum.ipxe.org/showthread.php?tid=7530">Related forum topic</a>. See also <a href="http://ipxe.org/cfg/user-class">documentation</a>: "RFC 3004 defines the DHCP user class as a set of length-value tuples, but iPXE treats it as a string."</li><li>ISC DHCP: "RFC3004 [RFC3004] defines the User-Class option. Note carefully that ISC DHCP currently does not implement to this reference, but has (inexplicably) selected an incompatible format: a plain text string." (<a href="https://www.isc.org/wp-content/uploads/2013/06/References.html">source</a>)</li><li>dnsmasq <a href="http://thekelleys.org.uk/gitweb/?p=dnsmasq.git;a=blob;f=src/rfc2131.c;h=8b99d4bfca8662923b059ceb138a2887ef13a767;hb=HEAD#l412">implements</a> uses heuristics to figure out whether to follow RFC 3004 or non-compliant behavior.</li><li>dhcpcd also uses the format <code>77 &lt;N&gt; &lt;N octets&gt;</code>, <a href="https://sources.debian.net/src/dhcpcd/1:3.2.3-11%2Bdeb7u1/dhcp.c/#L199">source</a>.</li></ul><p>Wireshark should probably be modified to recognize this not apparently not so uncommon case. (I encountered while monitoring DHCP traffic from the iPXE implementation shipped with QEMU 2.6.0).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '16, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-55006" class="comments-container"></div><div id="comment-tools-55006" class="comment-tools"></div><div class="clear"></div><div id="comment-55006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38129"></span>

<div id="answer-container-38129" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38129-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>isc dhcp client also do the same thing...(it will not add the total length ) before adding all the instances.</p><p>servers may not send the response because of this bug....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '14, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/0e3d17e153e9a187352b0142aa693058?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="venki&#39;s gravatar image" /><p>venki<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="venki has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '14, 08:39</p></div></div><div id="comments-container-38129" class="comments-container"></div><div id="comment-tools-38129" class="comment-tools"></div><div class="clear"></div><div id="comment-38129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

