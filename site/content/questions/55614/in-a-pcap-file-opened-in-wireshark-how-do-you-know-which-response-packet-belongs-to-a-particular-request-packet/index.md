+++
type = "question"
title = "In a .pcap file opened in Wireshark, how do you know which response (packet) belongs to a particular request (packet)?"
description = '''OK so I had seen a .pcap file which showed a few GSM MAP packets (there were 4 or 5 packets I guess) on the internet, but I can&#x27;t find it anymore. So for this question I am using another one which shows only packet, but please imagine that there are a few packets showing MAP requests (which have som...'''
date = "2016-09-17T04:45:00Z"
lastmod = "2016-09-20T18:06:00Z"
weight = 55614
keywords = [ "pcap", "gsm_sms", "wireshark", "gsm", "gsm_map" ]
aliases = [ "/questions/55614" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [In a .pcap file opened in Wireshark, how do you know which response (packet) belongs to a particular request (packet)?](/questions/55614/in-a-pcap-file-opened-in-wireshark-how-do-you-know-which-response-packet-belongs-to-a-particular-request-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55614-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>OK so I had seen a .pcap file which showed a few GSM MAP packets (there were 4 or 5 packets I guess) on the internet, but I can't find it anymore. So for this question I am using another one which shows only packet, but please imagine that there are a few packets showing <em>MAP requests</em> (which have something like <code>invoke processUnstructuredSS</code> in the <code>Info</code> column) and <em>MAP responses</em> (<code>showResultLast processUnstructuredSS</code>).</p><p>So imagine that we have the following sequence of MAP messages in Wireshark .pcap file:</p><pre><code>GSM MAP REQUEST processUnstructuredSS
GSM MAP REQUEST someOtherMAPMessage_B
GSM MAP REQUEST someOtherMAPMessage_C
GSM MAP REQUEST processUnstructuredSS
GSM MAP REQUEST processUnstructuredSS
GSM MAP RESPONSE someOtherMAPMessage_B
GSM MAP RESPONSE processUnstructuredSS
GSM MAP RESPONSE processUnstructuredSS
GSM MAP RESPONSE someOtherMAPMessage_C</code></pre><p><strong>My question is that how do I find out which particular response packet belongs to which request?</strong></p><p><strong>For example, how do I know which <code>processUnstructuresSS</code> response packet belongs to the FIRST request packet?</strong></p><p><img src="https://osqa-ask.wireshark.org/upfiles/teen.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">pcap gsm_sms wireshark gsm gsm_map</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '16, 04:45</strong></p><img src="https://secure.gravatar.com/avatar/d2c205566b4047d6494161edbd1223c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesss&#39;s gravatar image" /><p>Jesss<br />
<span class="score" title="51 reputation points">51</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesss has no accepted answers">0%</span></p></img></div></div><div id="comments-container-55614" class="comments-container"></div><div id="comment-tools-55614" class="comment-tools"></div><div class="clear"></div><div id="comment-55614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55688"></span>

<div id="answer-container-55688" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55688-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>With GSM MAP the answer actually lies in the TCAP layer. If you:</p><ol><li>Enable both TCAP Service Response Time/SRT preferences</li><li>Look at the <code>[Stat]</code> section of the TCAP dissection in a response</li></ol><p>... then you'll get a link back to the original request. For example, using one of the sample captures I found I got this:</p><pre><code>Frame 95: 131 bytes on wire (1048 bits), 131 bytes captured (1048 bits)
Ethernet II, Src: 01:01:01:01:01:01, Dst: 02:02:02:02:02:02
Internet Protocol Version 4, Src: 1.1.1.1, Dst: 2.2.2.2
Stream Control Transmission Protocol, Src Port: 2904 (2904), Dst Port: 2904 (2904)
MTP 2 User Adaptation Layer
Message Transfer Part Level 3
[CHINESE_ITU_STANDARD]
Signalling Connection Control Part
Transaction Capabilities Application Part
    end
    [Stat]
        [Session Id: 4]
        [Begin of session in frame 89]
        [Session duration: 1.099000000 seconds]
GSM Mobile Application</code></pre><p>The TCAP dissector figures out the relationship based on the SCCP Called and Calling addresses as well as the (TCAP) dialog ID(s).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '16, 18:06</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-55688" class="comments-container"><span id="55693"></span><div id="comment-55693" class="comment"><div id="post-55693-score" class="comment-score"></div><div class="comment-text"><p>..which is an excellent point (thank you, @JeffMorriss), but it still requires that you are lucky enough that the SCCP called address of the response can be identified as referring to the same endpoint as the SCCP calling address of the request.</p></div><div id="comment-55693-info" class="comment-info"><span class="comment-age">(21 Sep '16, 01:06)</span> sindy</div></div><span id="55713"></span><div id="comment-55713" class="comment"><div id="post-55713-score" class="comment-score"></div><div class="comment-text"><p>True. There is an SCCP preference ("Set source and destination GT addresses") which can sometimes (depending on the situation) help with that. The commit message that added the preference explains it thus:</p><pre><code>Add a preference that allows the user to decide if they want the calling and called GTs (if RI=GT) put in the (pinfo) source and destination (and thus into the source and destination columns).

This may help (if the PCs change but the GT does not) or hurt (if the GT or RI change but the PCs do not) TCAP&#39;s ability to identify which messages belong to which TCAP &quot;session.&quot;</code></pre></div><div id="comment-55713-info" class="comment-info"><span class="comment-age">(21 Sep '16, 07:33)</span> JeffMorriss ♦</div></div><span id="55718"></span><div id="comment-55718" class="comment"><div id="post-55718-score" class="comment-score"></div><div class="comment-text"><p>Assuming that the SCCP calling party of the request, and thus the SCCP called party of the response, is usually a "big piece of equipment" (as compared to the SCCP called party of the request which is usually a subscriber), would it make sense to extend the SCCP configuration with a user-configurable list of "locally" (i.e. at the point of capture) valid translations of the few E.164 (or eventually also E.212) numbers assigned to the locally interesting "big pieces of equipment" to their point codes and SSNs, making it possible to pair the requests with responses also where the address types of the request's calling and response's called cannot be compared directly?</p><p>Indexing that table by interface id and bundling it somewhere into the pcapng data, like IP to hostname translations can be, would be an extra luxury :-)</p></div><div id="comment-55718-info" class="comment-info"><span class="comment-age">(21 Sep '16, 09:30)</span> sindy</div></div><span id="55722"></span><div id="comment-55722" class="comment"><div id="post-55722-score" class="comment-score"></div><div class="comment-text"><p>Funny, I would have initially made the opposite assumption: that the request's Called address was the big piece of equipment (e.g., an HLR). :-)</p><p>As for the idea: honestly I never had much problem with Wireshark as it was--but I was further down the food^Wequipment chain than a majority of people using that stuff (i.e., my exposure was more limited than a person debugging a live SS7 network every day).</p><p>(And now I'm out of the Telco environment entirely...)</p></div><div id="comment-55722-info" class="comment-info"><span class="comment-age">(21 Sep '16, 10:42)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-55688" class="comment-tools"></div><div class="clear"></div><div id="comment-55688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55618"></span>

<div id="answer-container-55618" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55618-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>For popular protocols which intrinsically provide fields allowing to unambiguously map the relationship between messages, Wireshark dissectors do that for you as these protocols are interesting for many people so a lot of development effort has been spent on them.</p><p>For less popular protocols which intrinsically provide fields allowing to unambiguously map the relationship between messages, this may not be the case but it is relatively easy to use <a href="https://wiki.wireshark.org/Mate">MATE</a> to use the fields provided by existing dissectors and add metafields, allowing you to track the relationships, to protocol dissections.</p><p>For protocols using SCCP as transport, like in your example, no fields unambiguously mapping relationship of packets are available in general, so you have to look at your particular capturing environment and see whether you are lucky enough or not.</p><p>For these protocols, the sender of a request sends it with calling and called SCCP addresses which may both get translated as the messages are forwarded through the network, so a request's SCCP calling address may look quite different from the resulting response's SCCP called address although in the local context both identify the same equipment. Plus, in particular for MAP, you don't always get a response from the same equipment to which you have sent the request.</p><p>What could help a bit here would be to make dissectors of all the SS7 layers provide E.164 numbers in a uniform format (which they currently don't so numbers extracted from different layers cannot be matched against each other without format conversion, which <a href="https://wiki.wireshark.org/Mate">MATE</a> does not support) and differentiate these fields' names from one another (which some of these dissectors don't do as well, they give you several fields named just <code>e164</code> without a chance to tell a calling from called or any other one).</p><p>After such enhancement, it would be possible to use <a href="https://wiki.wireshark.org/Mate">MATE</a> to match numbers from the application layer (e.g. MAP) with numbers from the SCCP layer, so at least in cases where the SCCP address contains the E.164 number as its Global Title portion, you would be able to find relationships between messages automatically.</p><p>If you feel like that, you can <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi">file a bug</a> with severity "enhancement" for that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '16, 07:01</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Sep '16, 11:44</p></div></div><div id="comments-container-55618" class="comments-container"></div><div id="comment-tools-55618" class="comment-tools"></div><div class="clear"></div><div id="comment-55618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

