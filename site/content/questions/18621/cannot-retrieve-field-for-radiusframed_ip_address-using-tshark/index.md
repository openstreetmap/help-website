+++
type = "question"
title = "Cannot retrieve field for radius.Framed_IP_Address using Tshark."
description = '''Hi, I am having an issue with retrieving the value for the field radius.Framed_IP_Address but all other fields seem to be returned fine. Here is the command I&#x27;m running and sample output. $tshark -i eth1 -T fields -e radius.Event_Timestamp -e radius.User_Name -e radius.Acct_Status_Type -e radius.Acc...'''
date = "2013-02-13T19:01:00Z"
lastmod = "2013-02-13T19:28:00Z"
weight = 18621
keywords = [ "accounting", "radius", "tshark", "framed-ip-address" ]
aliases = [ "/questions/18621" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot retrieve field for radius.Framed\_IP\_Address using Tshark.](/questions/18621/cannot-retrieve-field-for-radiusframed_ip_address-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18621-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am having an issue with retrieving the value for the field radius.Framed_IP_Address but all other fields seem to be returned fine.</p><p>Here is the command I'm running and sample output.</p><pre><code>$tshark -i eth1 -T fields -e radius.Event_Timestamp  -e radius.User_Name  -e radius.Acct_Status_Type -e radius.Acct_Session_Id -e radius.Calling_Station_Id -e radius.Framed_IP_Address -E separator=&quot;|&quot;</code></pre><p>I have confirmed that there is a value for the AVP for Framed-IP-Address by viewing the output. All other fields seem to work and I have tried using both radius.Framed_IP_Address and radius.Framed-IP-Address with no success.</p><p>is there any reason why only this field doesn't seem to work?</p></div><div id="question-tags" class="tags-container tags">accounting radius tshark framed-ip-address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '13, 19:01</strong></p><img src="https://secure.gravatar.com/avatar/fad6f04e98254b85ab7301ab7c4425ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TsharkNewb&#39;s gravatar image" /><p>TsharkNewb<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TsharkNewb has no accepted answers">0%</span></p></div></div><div id="comments-container-18621" class="comments-container"></div><div id="comment-tools-18621" class="comment-tools"></div><div class="clear"></div><div id="comment-18621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18623"></span>

<div id="answer-container-18623" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18623-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong><code>-e radius.Framed-IP-Address</code></strong> works with tshark 1.8.4 on Windows XP, while reading these capture files:</p><ul><li><a href="https://bugs.wireshark.org/bugzilla/attachment.cgi?id=8975">https://bugs.wireshark.org/bugzilla/attachment.cgi?id=8975</a></li><li><a href="http://www.wand.net.nz/trac/libtrace/browser/trunk/test/traces/radius.pcap">http://www.wand.net.nz/trac/libtrace/browser/trunk/test/traces/radius.pcap</a></li></ul><blockquote><p>is there any reason why only this field doesn't seem to work?</p></blockquote><p>it could be a bug in your tshark version. What is the output of <strong><code>tshark -v</code></strong> on your system?<br />
it could be a typo in your command. Did you <strong>really</strong> try <strong><code>-e radius.Framed-IP-Address</code></strong>?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '13, 19:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-18623" class="comments-container"><span id="18624"></span><div id="comment-18624" class="comment"><div id="post-18624-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt,</p><p>I have tried both commands. No output for that field for either one.</p><p>tshark -v shows: TShark 1.8.5 (SVN Rev Unknown from unknown)</p><p>...</p><p>Compiled (64-bit) with GLib 2.22.5, with libpcap, with libz 1.2.3, with POSIX capabilities (Linux), without SMI, without c-ares, without ADNS, without Lua, without Python, with GnuTLS 2.8.5, with Gcrypt 1.4.5, with MIT Kerberos, without GeoIP.</p><p>Running on Linux 2.6.32-220.el6.x86_64, with locale en_US.UTF-8, with libpcap version 1.3.0, with libz 1.2.3.</p><p>Built using gcc 4.4.6 20110731 (Red Hat 4.4.6-3).</p></div><div id="comment-18624-info" class="comment-info"><span class="comment-age">(13 Feb '13, 19:39)</span> TsharkNewb</div></div><span id="18625"></span><div id="comment-18625" class="comment"><div id="post-18625-score" class="comment-score"></div><div class="comment-text"><p>I just ran it using one of the input file you supplied with the command:</p><p>tshark -r radius-acct-no-dups-sample.pcap -T fields -e radius.Framed-IP-Address</p><p>This works and returns the IP addresses. It only seems to not be working when I am trying to capture from the interface.</p></div><div id="comment-18625-info" class="comment-info"><span class="comment-age">(13 Feb '13, 19:49)</span> TsharkNewb</div></div><span id="18629"></span><div id="comment-18629" class="comment"><div id="post-18629-score" class="comment-score"></div><div class="comment-text"><blockquote><p>It only seems to not be working when I am trying to capture from the interface.</p></blockquote><p>does it work, if you capture from the interface and write to a file. Then, afterwards read from that file with tshark?</p><p>I just want to check if it's the live capturing or a 'problem' with the radius protocol in your environment.</p><p>If does work that way, it might be a bug in tshark. Then, please file a bug report at bugs.wireshark.org. Please add a detailed problem description and a link to this question.</p></div><div id="comment-18629-info" class="comment-info"><span class="comment-age">(13 Feb '13, 20:17)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-18623" class="comment-tools"></div><div class="clear"></div><div id="comment-18623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

