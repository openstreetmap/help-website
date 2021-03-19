+++
type = "question"
title = "The US$ 100 challenge: WPA2 decryption"
description = '''The US$ 100 challenge: WPA2 decryption The first person who solve successfully and post here the solution of my problem becomes US$ 100. What you have to solve: I have many encrypted WPA2 WiFi sniffed in a pcap file with the 4-way handshake, and I know the SSID and WPA2 Key. I like to convert the WP...'''
date = "2013-03-19T17:49:00Z"
lastmod = "2013-03-20T14:19:00Z"
weight = 19664
keywords = [ "decryption", "wpa2" ]
aliases = [ "/questions/19664" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [The US$ 100 challenge: WPA2 decryption](/questions/19664/the-us-100-challenge-wpa2-decryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19664-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The US$ 100 challenge: WPA2 decryption</p><p>The first person who solve successfully and post here the solution of my problem becomes US$ 100. What you have to solve: I have many encrypted WPA2 WiFi sniffed in a pcap file with the 4-way handshake, and I know the SSID and WPA2 Key. I like to convert the WPA2 pcap file to a decrypted pcap file with all protocols decrypted. What's not work: airdecap-ng from aircrack-ng does not decrypt all protocols like for example SMB. I need the decrypted file in the pcap format, so I can use it to analyze it with different software. Preferred is a solution with tshark, like</p><p>tshark -r myFile.pcap -o "wlan.enable_decryption:TRUE" -o wlan.wep_key1:wpa-pwd:MyPassword:MySSID -w outputFile.pcap</p><p>but this sample result in an error:</p><p>tshark: -o flag "wlan.wep_key1:wpa-pwd:MyPassword:MySSID" specifies unknown preference</p><p>With Wireshark I can view the decrypted data, if I enter the key under: -&gt;Edit-&gt;Preferences-&gt;Protocols-&gt;IEEE 802.11-&gt; "enable decryption" and "set the Key" (wpa-pwd myPassword:SSID) But I can't save it to a decrypted pcap file. Here is a sample file for tests: <a href="http://www.dler.ch/usd100challenge/h2_2.pcap.zip">http://www.dler.ch/usd100challenge/h2_2.pcap.zip</a> SSID: H2, Password: myAPretos2</p><p>To view the decrypted traffic in wireshark: <a href="http://www.dler.ch/usd100challenge/wireshark.jpg">http://www.dler.ch/usd100challenge/wireshark.jpg</a></p><p>Some decrypted SMB protocol traffic: <a href="http://www.dler.ch/usd100challenge/Screenshot.png">http://www.dler.ch/usd100challenge/Screenshot.png</a></p><p>If you have a solution: Please tell me the command you are using, the OS, the software and the version of it.</p></div><div id="question-tags" class="tags-container tags">decryption wpa2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '13, 17:49</strong></p><img src="https://secure.gravatar.com/avatar/7d1ef5d02d35ae25b6fb5a5683bd190d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RS2000&#39;s gravatar image" /><p>RS2000<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RS2000 has no accepted answers">0%</span></p></div></div><div id="comments-container-19664" class="comments-container"><span id="19699"></span><div id="comment-19699" class="comment"><div id="post-19699-score" class="comment-score"></div><div class="comment-text"><blockquote><p>airdecap-ng from aircrack-ng does not decrypt all protocols like for example SMB</p></blockquote><p>airdecap-ng has no idea what SMB <em>is</em>. Do you mean that it, for some reason, does not decrypt all IEEE 802.11 data frames (and that one type of IEEE 802.11 data frame that it does not decrypt is a data frame containing IP, atop which is carried TCP, atop which is captured either raw SMB or the NetBIOS-over-TCP session service with SMB atop it)?</p></div><div id="comment-19699-info" class="comment-info"><span class="comment-age">(20 Mar '13, 17:34)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-19664" class="comment-tools"></div><div class="clear"></div><div id="comment-19664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19697"></span>

<div id="answer-container-19697" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19697-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Download an old version: <a href="ftp://ftp.uni-kl.de/pub/wireshark/win32/all-versions/">ftp://ftp.uni-kl.de/pub/wireshark/win32/all-versions/</a><br />
I have downloaded: wireshark 1.2.1 (SVN Rev 29141)<br />
Generate the PSK: <a href="http://www.wireshark.org/tools/wpa-psk.html">http://www.wireshark.org/tools/wpa-psk.html</a><br />
Go to:<br />
Edit<br />
Preferences<br />
Protocols<br />
IEEE 802.11<br />
Key #1:<br />
add:<br />
wpa-psk:b8c787bf968d8503671b4345db9397c4355ba45a9f90a8f79420c3cbf87cb154<br />
</p><pre><code>Run:
tshark -r q19664_h2_2.pcap -o &quot;wlan.enable_decryption:TRUE&quot; -o wlan.wep_key1:wpa-psk:b8c787bf968d8503671b4345db9397c4355ba45a9f90a8f79420c3cbf87cb154 -R &quot;eapol || smb&quot; -w q19664_eapol_smb_h2_2.pcap</code></pre>Hope this helps.<br />
BTW: Running on Windows XP</div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '13, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-19697" class="comments-container"><span id="19698"></span><div id="comment-19698" class="comment"><div id="post-19698-score" class="comment-score"></div><div class="comment-text"><p>After this procedure, you see in Wireshark on the file "q19664_eapol_smb_h2_2.pcap" the decrypted SMB stuff, but as soon as you remove in Wireshark the Key under -&gt;Edit-&gt;Preferences-&gt;Protocols-&gt;IEEE 802.11-&gt;Key #1, you can see that the file is still encrypted! If I use the file "q19664_eapol_smb_h2_2.pcap" with other tools, it did not work because it is still encrypted. Please send the decrypted file to my email address [email protected] if you have a working solution. Thank you!</p></div><div id="comment-19698-info" class="comment-info"><span class="comment-age">(20 Mar '13, 15:52)</span> RS2000</div></div><span id="19700"></span><div id="comment-19700" class="comment"><div id="post-19700-score" class="comment-score"></div><div class="comment-text"><p>Neither TShark nor Wireshark have any support whatsoever for writing out packets that are different from the packets that they read, other than Wireshark 1.8.0 and later's ability to add comments to, remove comments from, and edit comments in a pcap-ng file.</p></div><div id="comment-19700-info" class="comment-info"><span class="comment-age">(20 Mar '13, 17:35)</span> Guy Harris ♦♦</div></div><span id="19787"></span><div id="comment-19787" class="comment"><div id="post-19787-score" class="comment-score"></div><div class="comment-text"><pre><code>TShark can export decrypted data to a text file:
tshark -r q19664_h2_2.pcap -o &quot;wlan.enable_decryption:TRUE&quot; -o wlan.wep_key1:wpa-psk:b8c787bf968d8503671b4345db9397c4355ba45a9f90a8f79420c3cbf87cb154 -R &quot;eapol || smb&quot; -q -xV -O smb &gt; q19664_smb_2_h2_2.txt
but it cannot save decrypted data into pcap file, which is still decrypted after removing the key.</code></pre><p>See this thread on <a href="http://www.wireshark.org/lists/">Wireshark Mailing Lists</a>:<br />
<a href="https://www.wireshark.org/lists/wireshark-users/200906/msg00175.html">Save Decrypted traffic</a></p></div><div id="comment-19787-info" class="comment-info"><span class="comment-age">(24 Mar '13, 07:26)</span> joke</div></div></div><div id="comment-tools-19697" class="comment-tools"></div><div class="clear"></div><div id="comment-19697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

