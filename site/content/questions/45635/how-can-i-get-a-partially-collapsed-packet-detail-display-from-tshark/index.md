+++
type = "question"
title = "How can I get a partially-collapsed packet detail display from TShark?"
description = '''I&#x27;m using tshark protocol filter as I need to parse the contents of the SIP Packets. tshark -r df32c2248fe646a6793ce9a63b124b34@0.0.0.0.pcap -O sip  I get this: Frame 14: 553 bytes on wire (4424 bits), 553 bytes captured (4424 bits) Linux cooked capture Internet Protocol Version 4, Src: 4.4.4.4 (4.4...'''
date = "2015-09-04T08:58:00Z"
lastmod = "2015-09-06T09:28:00Z"
weight = 45635
keywords = [ "details", "collapse", "tshark" ]
aliases = [ "/questions/45635" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get a partially-collapsed packet detail display from TShark?](/questions/45635/how-can-i-get-a-partially-collapsed-packet-detail-display-from-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45635-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using tshark protocol filter as I need to parse the contents of the SIP Packets.</p><pre><code>tshark -r [email protected] -O sip</code></pre><p>I get this:</p><pre><code>Frame 14: 553 bytes on wire (4424 bits), 553 bytes captured (4424 bits)
Linux cooked capture
Internet Protocol Version 4, Src: 4.4.4.4 (4.4.4.4), Dst: 3.3.3.3 (3.3.3.3)
User Datagram Protocol, Src Port: 5060 (5060), Dst Port: 5060 (5060)
Session Initiation Protocol (200)
    Status-Line: SIP/2.0 200 OK
        Status-Code: 200
        [Resent Packet: False]
        [Request Frame: 11]
        [Response Time (ms): 115]
        [Release Time (ms): 115]
    Message Header
        Via: SIP/2.0/UDP 2.2.2.2:5060;received=3.3.3.3;branch=z9hG4bK18f6609d-1c76-4a8b-a96b-2cf7d8036d36_6772d868_3067109296759172
            Transport: UDP
            Sent-by Address: 2.2.2.2
            Sent-by port: 5060
            Received: 3.3.3.3
            Branch: z9hG4bK18f6609d-1c76-4a8b-a96b-2cf7d8036d36_6772d868_3067109296759172
        Contact: &lt;sip:[email protected]:17060&gt;
            Contact URI: sip:[email protected]:17060
                Contact URI User Part: 14082186500
                Contact URI Host Part: 1.1.1.1
                Contact URI Host Port: 17060
        To: &lt;sip:[email protected];user=phone&gt;;tag=83174026
            SIP to address: sip:[email protected];user=phone
                SIP to address User Part: 14082186500
                SIP to address Host Part: spicyramen.ippbx.com
                SIP To URI parameter: user=phone
            SIP to tag: 83174026
        From: &lt;sip:[email protected]&gt;;tag=87638703_6772d868_18f6609d-1c76-4a8b-a96b-2cf7d8036d36
            SIP from address: sip:[email protected]
                SIP from address User Part: anonymous
                SIP from address Host Part: sip.ie1.sipprovider.com
            SIP from tag: 87638703_6772d868_18f6609d-1c76-4a8b-a96b-2cf7d8036d36
        Call-ID: [email protected]
        CSeq: 44365 BYE
            Sequence Number: 44365
            Method: BYE
        User-Agent: 3CXPhoneSystem 14.0.44198.522 (44097)
        Content-Length: 0</code></pre><p>As you can see output is not collapsed. I want to see something like this:</p><pre><code>Frame 14: 553 bytes on wire (4424 bits), 553 bytes captured (4424 bits)
Linux cooked capture
Internet Protocol Version 4, Src: 4.4.4.4 (4.4.4.4), Dst: 3.3.3.3 (3.3.3.3)
User Datagram Protocol, Src Port: 5060 (5060), Dst Port: 5060 (5060)
Session Initiation Protocol (200)
    Status-Line: SIP/2.0 200 OK
    Message Header
        Via: SIP/2.0/UDP 2.2.2.2:5060;received=3.3.3.3;branch=z9hG4bK18f6609d-1c76-4a8b-a96b-2cf7d8036d36_6772d868_3067109296759172
        Contact: &lt;sip:[email protected]:17060&gt;
        To: &lt;sip:[email protected];user=phone&gt;;tag=83174026
        From: &lt;sip:[email protected]&gt;;tag=87638703_6772d868_18f6609d-1c76-4a8b-a96b-2cf7d8036d36
        Call-ID: [email protected]
        CSeq: 44365 BYE
        User-Agent: 3CXPhoneSystem 14.0.44198.522 (44097)
        Content-Length: 0</code></pre></div><div id="question-tags" class="tags-container tags">details collapse tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '15, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/5a2d6a17424a997970d7a1caebdc5aa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spicyramen&#39;s gravatar image" /><p>spicyramen<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spicyramen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Sep '15, 19:58</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-45635" class="comments-container"></div><div id="comment-tools-45635" class="comment-tools"></div><div class="clear"></div><div id="comment-45635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="45644"></span>

<div id="answer-container-45644" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45644-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Nothing that you can do from tshark, but you could remove the lines that you don't want with grep e.g.</p><p><code>tshark -r file.pcap -O sip | grep -v -e "Contact URI" -e "SIP from" -e "SIP to" </code></code></p><code></code><p>or use a file if there are too many patterns.</p></code></code></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '15, 04:19</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p>Roland<br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Sep '15, 06:30</p></div></div><div id="comments-container-45644" class="comments-container"></div><div id="comment-tools-45644" class="comment-tools"></div><div class="clear"></div><div id="comment-45644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45646"></span>

<div id="answer-container-45646" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45646-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark<br />
You can use Wireshark to do the job.<br />
Apply a <a href="https://wiki.wireshark.org/DisplayFilters">display filter</a>:<br />
sip</p><p>Go to the the <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChUsePacketDetailsPaneSection.html">Packet Details</a> pane.<br />
Expand "Session Initiation Protocol"<br />
Expand Request-Line, Message Header and Message Body* (do not Expand Subtrees)<br />
Go to File - Export - Export Packet Dissections... - As "Plain Text" File...<br />
Packet Format section: select "Packet Summery Line" and "Packet Details: As Displayed"<br />
Add a file name and save the file<br />
</p><p>*Note<br />
I have used <a href="https://wiki.wireshark.org/SampleCaptures#SIP_and_RTP">sample file</a>: aaa.pcap<br />
Message Body: see packet 223</p><p><a href="https://www.wireshark.org/docs/man-pages/tshark.html">TShark</a><br />
You can use -T Fields and add all the <a href="https://www.wireshark.org/docs/dfref/s/sip.html">fields</a> you need.<br />
For example:<br />
tshark -r aaa.pcap -Y sip -E header=y -E separator="?" -T fields -e frame.number -e sip.Request-Line -e sip.r-uri -e sip.Via -e sip.From -e sip.To -e sip.Call-ID -e sip.Contact -e sip.Expires -e sip.CSeq -e sip.User-Agent -e sip.Content-Length &gt; aaa.csv</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '15, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-45646" class="comments-container"></div><div id="comment-tools-45646" class="comment-tools"></div><div class="clear"></div><div id="comment-45646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

