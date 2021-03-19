+++
type = "question"
title = "Tshark - How to extrakt certificate from radius eap packet"
description = '''I am looking for a way using programming in Python to extract from a Radius sniffertrace the EAP packetflow, which includes e.g the Server Hello and therfore Server certificate. So far I am using tschark to extract the Radius packet containing EAP Server hello with the fragments already reassembled....'''
date = "2014-03-14T18:32:00Z"
lastmod = "2014-04-03T04:56:00Z"
weight = 30807
keywords = [ "eap-peap", "radius", "certificate" ]
aliases = [ "/questions/30807" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark - How to extrakt certificate from radius eap packet](/questions/30807/tshark-how-to-extrakt-certificate-from-radius-eap-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30807-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking for a way using programming in Python to extract from a Radius sniffertrace the EAP packetflow, which includes e.g the Server Hello and therfore Server certificate. So far I am using tschark to extract the Radius packet containing EAP Server hello with the fragments already reassembled. I can store this packet in PDML format. There I can see all the Bytes of the certificate. Lets say, I woulde be able to build the String/List of Bytes from the certificate. Question: How could I build now from all those Bytes e.g a DER or PEM formated certificate file?</p><p>In wireshark GUI the certificate can be saved as Extraktes Bytes in DER format manually, but I need the certificate automattically extracted using some Python programming. <a href="http://www.wireshark.org/lists/wireshark-users/201003/msg00080.html">http://www.wireshark.org/lists/wireshark-users/201003/msg00080.html</a></p><p>Thx for your valid input!</p></div><div id="question-tags" class="tags-container tags">eap-peap radius certificate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '14, 18:32</strong></p><img src="https://secure.gravatar.com/avatar/367e7a458dfc9d97df9d1520cf741468?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RogNob&#39;s gravatar image" /><p>RogNob<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RogNob has no accepted answers">0%</span></p></div></div><div id="comments-container-30807" class="comments-container"></div><div id="comment-tools-30807" class="comment-tools"></div><div class="clear"></div><div id="comment-30807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30838"></span>

<div id="answer-container-30838" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30838-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I can store this packet in PDML format. There <strong>I can see all the Bytes of the certificate.</strong><br />
but I <strong>need the certificate automattically extracted</strong> using some <strong>Python programming</strong></p></blockquote><p>Hm.. that sounds more like a <strong>Python programming specific problem</strong>, right? You did everything right (with tshark) to get the 'extract' payload of the frames. Reading the tshark output and creating a certificate from that data <strong>with Python</strong> is a programming exercise and I'm sure will get (much better) answers in a Python programming forum or at <a href="http://stackoverflow.com">http://stackoverflow.com</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '14, 13:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-30838" class="comments-container"><span id="30860"></span><div id="comment-30860" class="comment"><div id="post-30860-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, indeed I ask the question there as well. However since Wireshark can save the certificate directly as per link above, I hopped this maybe also possible using tschark. Maybe you know if I have all the bytes from PDLM. How to progress to get the Certificate as DER or PEM Format? I did Save the Bytes as certificate.der or certificate.pem but can not open the certificate. Best regeres Roger</p></div><div id="comment-30860-info" class="comment-info"><span class="comment-age">(16 Mar '14, 11:47)</span> RogNob</div></div><span id="30862"></span><div id="comment-30862" class="comment"><div id="post-30862-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I hopped this maybe also possible using tshark.</p></blockquote><p>no, that's not possible, as it is not implemented. So, all you can do is to parse the payload bytes and try to create a cert based on that data. As I mentioned, that's a programming exercise.</p><blockquote><p>Maybe you know if I have all the bytes from PDLM.</p></blockquote><p>I can't tell you, as you did not post the PDML output, but in general PDML will print the full payload, afiak.</p><blockquote><p>How to progress to get the Certificate as DER or PEM Format?</p></blockquote><p>Here are the necessary steps.</p><ol><li>understand the PEM or DER cert format (see google for that), as that's your output format</li><li>understand the format in which the cert is transmitted. Here, wireshark and some basic protocol knowledge would help.</li><li>read the output of tshark, extract the relevant bytes and write them in PEM or DER format.</li></ol><p>At least that's how I would do it.</p><blockquote><p>I did Save the Bytes as certificate.der or certificate.pem but can not open the certificate.</p></blockquote><p>did you check the content of the exported file? Does it look like a PEM formatted cert in an editor?</p></div><div id="comment-30862-info" class="comment-info"><span class="comment-age">(16 Mar '14, 12:59)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-30838" class="comment-tools"></div><div class="clear"></div><div id="comment-30838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31473"></span>

<div id="answer-container-31473" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31473-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just to update. I am using now tshark to create PDML and extract with python code using ElementTree the certificate bytes which I convert to ASCII allow to save the certificate as DER file. •extract the certificate bytes in a string : cert_string_bin •change the bytes into ASCII</p><p>cert_string_der = cert_string_bin.decode("hex") •write the certificate file in DER format</p><p>cert = open("server_cert_of_stream_" + str(stream_counter )+".der", 'w')</p><p>cert.write(cert_string_der)</p><p>cert.close()</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '14, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/367e7a458dfc9d97df9d1520cf741468?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RogNob&#39;s gravatar image" /><p>RogNob<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RogNob has no accepted answers">0%</span></p></div></div><div id="comments-container-31473" class="comments-container"></div><div id="comment-tools-31473" class="comment-tools"></div><div class="clear"></div><div id="comment-31473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

