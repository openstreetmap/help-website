+++
type = "question"
title = "Failed to export HTTP objects from an export-PDU file"
description = '''After I decrypted the SSL session in a capture file and saved the decrypted data to a new pcap file by &quot;export PDUs to file&quot; function, I was failed to export the HTTP objects from the export-PDU file. Seems wireshark doesn&#x27;t reassemble the HTTP payload. Is there any way I can export the complete htt...'''
date = "2017-07-24T06:50:00Z"
lastmod = "2017-07-24T06:50:00Z"
weight = 63043
keywords = [ "export-http", "export" ]
aliases = [ "/questions/63043" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Failed to export HTTP objects from an export-PDU file](/questions/63043/failed-to-export-http-objects-from-an-export-pdu-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63043-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After I decrypted the SSL session in a capture file and saved the decrypted data to a new pcap file by "export PDUs to file" function, I was failed to export the HTTP objects from the export-PDU file. Seems wireshark doesn't reassemble the HTTP payload. Is there any way I can export the complete http objects from this export-PDU file?</p><p>The output of tshark when reading this export-PDU file:</p><p>tshark -r export_PDU.pcap</p><pre><code> 1 0.000000000 230  10.140.8.27 → 10.79.46.117 HTTP GET /wiresharkdoc.ico HTTP/1.1  exported_pdu:http
    2 0.002855000 348 10.79.46.117 → 10.140.8.27  HTTP HTTP/1.1 200 OK  exported_pdu:http
    3 0.002855000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
    4 0.002930000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
    5 0.002939000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
    6 0.002941000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
    7 0.002943000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
    8 0.002945000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
    9 0.005285000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   10 0.005285000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   11 0.005291000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   12 0.005292000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   13 0.005758000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   14 0.005758000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   15 0.005959000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   16 0.006866000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   17 0.006902000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   18 0.006909000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   19 0.006911000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   20 0.008352000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   21 0.008366000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   22 0.008426000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   23 0.010263000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   24 0.010309000 16456 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data
   25 0.010320000 12150 10.79.46.117 → 10.140.8.27  HTTP Continuation exported_pdu:http:data</code></pre></div><div id="question-tags" class="tags-container tags">export-http export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '17, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/2e1e083486948d2a22563b861609015d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frank%20Lin&#39;s gravatar image" /><p>Frank Lin<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frank Lin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jul '17, 06:57</p></div></div><div id="comments-container-63043" class="comments-container"><span id="63067"></span><div id="comment-63067" class="comment"><div id="post-63067-score" class="comment-score"></div><div class="comment-text"><p>What Wireshark version did you use? Can you reproduce it with 2.4 which was released some days ago?</p></div><div id="comment-63067-info" class="comment-info"><span class="comment-age">(24 Jul '17, 20:47)</span> Lekensteyn</div></div><span id="63079"></span><div id="comment-63079" class="comment"><div id="post-63079-score" class="comment-score"></div><div class="comment-text"><p>I used the latest Wireshark version 2.4.</p><p>tshark -v</p><p>TShark (Wireshark) 2.4.0 (v2.4.0)</p><p>Thank you for looking into this.</p></div><div id="comment-63079-info" class="comment-info"><span class="comment-age">(25 Jul '17, 02:43)</span> Frank Lin</div></div><span id="63081"></span><div id="comment-63081" class="comment"><div id="post-63081-score" class="comment-score"></div><div class="comment-text"><p>You can find the capture file that I use from the link below:</p><p><a href="https://1drv.ms/f/s!AnBHC0wl8DZ9eFVwAEuvDMjbFoM">https://1drv.ms/f/s!AnBHC0wl8DZ9eFVwAEuvDMjbFoM</a></p></div><div id="comment-63081-info" class="comment-info"><span class="comment-age">(25 Jul '17, 02:53)</span> Frank Lin</div></div><span id="63092"></span><div id="comment-63092" class="comment"><div id="post-63092-score" class="comment-score"></div><div class="comment-text"><p>Confirmed and I have an idea where it goes wrong. Can you file a bug about it and attach the pcap / steps to reproduce?</p></div><div id="comment-63092-info" class="comment-info"><span class="comment-age">(25 Jul '17, 08:25)</span> Lekensteyn</div></div><span id="63107"></span><div id="comment-63107" class="comment"><div id="post-63107-score" class="comment-score">1</div><div class="comment-text"><p>Sure. I have filed a bug as below.</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13918">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13918</a></p><p>Could you send me the Pull Request to fix this bug when it's done. I can merge the fix and rebuild wireshark locally.</p><p>Many thanks in advance.</p></div><div id="comment-63107-info" class="comment-info"><span class="comment-age">(25 Jul '17, 19:16)</span> Frank Lin</div></div></div><div id="comment-tools-63043" class="comment-tools"></div><div class="clear"></div><div id="comment-63043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

