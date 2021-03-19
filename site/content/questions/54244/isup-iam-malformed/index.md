+++
type = "question"
title = "ISUP IAM Malformed?"
description = '''Can someone please take a look at this IAM decode and give me your opinion if it is correct or malformed please? What I am suspecting to be incorrect is the optional fields, specifically the Generic Name. When this call leaves the originating MSS it is leaving with calling, called and jip but it arr...'''
date = "2016-07-22T13:08:00Z"
lastmod = "2016-07-27T05:43:00Z"
weight = 54244
keywords = [ "decode", "ansi", "isup", "malformed" ]
aliases = [ "/questions/54244" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ISUP IAM Malformed?](/questions/54244/isup-iam-malformed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54244-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can someone please take a look at this IAM decode and give me your opinion if it is correct or malformed please?</p><p>What I am suspecting to be incorrect is the optional fields, specifically the Generic Name. When this call leaves the originating MSS it is leaving with calling, called and jip but it arrives with calling, called, AN II, Carrier ID and Generic Name... This is failing and any help I can get is greatly appreciated.</p><pre><code>ISDN User Part
    CIC: 430
    Message type: Initial address (1)
    Nature of Connection Indicators: 0x0
        Mandatory Parameter: Nature of connection indicators (6)
        .... ..00 = Satellite Indicator: No Satellite circuit in connection (0x00)
        .... 00.. = Continuity Check Indicator: Continuity check not required (0x00)
        ...0 .... = Echo Control Device Indicator: Echo control device not included
    Forward Call Indicators: 0x6010
        Mandatory Parameter: Forward call indicators (7)
        .... ...0 .... .... = National/international call indicator: Call to be treated as national call
        .... .00. .... .... = End-to-end method indicator: No End-to-end method available (only link-by-link method available) (0x0000)
        .... 0... .... .... = Interworking indicator: no interworking encountered (No.7 signalling all the way)
        ...0 .... .... .... = End-to-end information indicator: no end-to-end information available
        ..1. .... .... .... = ISDN user part indicator: ISDN user part used all the way
        01.. .... .... .... = ISDN user part preference indicator: ISDN user part not required all the way (0x0001)
        .... .... .... ...0 = ISDN access indicator: originating access non-ISDN
        .... .... .... .00. = SCCP method indicator: No indication (0x0000)
        .... .... ...1 .... = Ported number translation indicator: number translated
        .... .... ..0. .... = Query on Release attempt indicator: no QoR routing attempt in progress
    Calling Party&#39;s category: 0xa (ordinary calling subscriber)
        Mandatory Parameter: Calling party&#39;s category (9)
        Calling Party&#39;s category: ordinary calling subscriber (0x0a)
    User service information, (3 bytes length)
        Mandatory Parameter: User service information (29)
        Pointer to Parameter: 3
        Parameter Length: 3
        User service information (-&gt; Q.931 Bearer_capability): 9090a2
        1... .... = Extension indicator: last octet
        .00. .... = Coding standard: ITU-T standardized coding (0x00)
        ...1 0000 = Information transfer capability: 3.1 kHz audio (0x10)
        1... .... = Extension indicator: last octet
        .00. .... = Transfer mode: Circuit mode (0x00)
        ...1 0000 = Information transfer rate: 64 kbit/s (0x10)
        1... .... = Extension indicator: last octet
        .01. .... = Layer identification: Layer 1 identifier (0x01)
        ...0 0010 = User information layer 1 protocol: Recommendation G.711 u-law (0x02)
    Called Party Number: 2175041116
        Mandatory Parameter: Called party number (4)
        Pointer to Parameter: 6
        Parameter Length: 7
        0... .... = Odd/even indicator: even number of address signals
        .000 0011 = Nature of address indicator: national (significant) number (3)
        0... .... = INN indicator: routing to internal network number allowed 
        .001 .... = Numbering plan indicator: ISDN (Telephony) numbering plan (1)
        Called Party Number: 2175041116
            .... 0010 = Address signal digit: 2 (2)
            0001 .... = Address signal digit: 1 (1)
            .... 0111 = Address signal digit: 7 (7)
            0101 .... = Address signal digit: 5 (5)
            .... 0000 = Address signal digit: 0 (0)
            0100 .... = Address signal digit: 4 (4)
            .... 0001 = Address signal digit: 1 (1)
            0001 .... = Address signal digit: 1 (1)
            .... 0001 = Address signal digit: 1 (1)
            0110 .... = Address signal digit: 6 (6)
            E.164 Called party number digits: 2175041116
    Pointer to start of optional part: 13
    Calling Party Number: 2174972872
        Optional Parameter: Calling party number (10)
        Parameter Length: 7
        0... .... = Odd/even indicator: even number of address signals
        .000 0011 = Nature of address indicator: national (significant) number (3)
        0... .... = NI indicator: complete
        .001 .... = Numbering plan indicator: ISDN (Telephony) numbering plan (1)
        .... 00.. = Address presentation restricted indicator: presentation allowed (0)
        .... ..11 = Screening indicator: network provided (3)
        Calling Party Number: 2174972872
            .... 0010 = Address signal digit: 2 (2)
            0001 .... = Address signal digit: 1 (1)
            .... 0111 = Address signal digit: 7 (7)
            0100 .... = Address signal digit: 4 (4)
            .... 1001 = Address signal digit: 9 (9)
            0111 .... = Address signal digit: 7 (7)
            .... 0010 = Address signal digit: 2 (2)
            1000 .... = Address signal digit: 8 (8)
            .... 0111 = Address signal digit: 7 (7)
            0010 .... = Address signal digit: 2 (2)
            E.164 Calling party number digits: 2174972872
    Originating line info: 0 (ANI II if &lt; 51, reserved otherwise)
        Optional Parameter: Originating line information (234)
        Parameter Length: 1
        Originating line info: 0
    Parameter Type unknown/reserved (3 Bytes)
        Optional Parameter: Carrier identification (197)
        Parameter Length: 3
    Generic name: 
        Optional Parameter: Generic name (199)
        Parameter Length: 1
        .... ..00 = Presentation indicator: presentation allowed (0)
        ...0 .... = Availability indicator: name available/unknown
        001. .... = Type indicator: calling name (1)
        Generic Name: 
    End of optional parameters (0)</code></pre></div><div id="question-tags" class="tags-container tags">decode ansi isup malformed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '16, 13:08</strong></p><img src="https://secure.gravatar.com/avatar/4bc0fe37a8150f1e564b5943078ed660?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Pierotti&#39;s gravatar image" /><p>Michael Pier...<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Pierotti has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '16, 14:29</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-54244" class="comments-container"><span id="54247"></span><div id="comment-54247" class="comment"><div id="post-54247-score" class="comment-score"></div><div class="comment-text"><p>Without seeing the original message bytes it is hard to tell whether the message has actually been malformed in transit or whether the Wireshark dissector has just chosen to interpret the i.e. "name" value as Originating Line Info Parameter instead of Jurisdiction Identification Parameter (causing the other bytes of the JIP to be misinterpreted). So can you please post the hex dump of the complete message? To do so, you have to choose the message in the packet list, right-click the first line (<code>Frame n: ...</code>), choose <code>Copy -&gt; ...as Hex Dump</code> from the drop-down menu, and paste the result into the text of your Question after clicking "edit" below the Question? Then, click open the Frame subtree and state the <code>Encapsulation type:</code> value (such as <code>Ethernet (1)</code>).</p><p>For a single message this may be less annoying than exporting a single message into a new capture file, uploading that file to a login-free file sharing service, and editing the Question with a link to it. But you may think otherwise, so feel free to do it this way. Cloudshark would be the best place for the file in such case.</p><p>As I'm not based in the North American region, I'd also like to have the i.e. "names" (codes identifying the information element) specified for JIP and OLIP in the Telcordia GR-317-CORE.</p><p>If you cannot find these codes either, please state at least the expected JIP contents (which should be a 6-character ASCII string or 6 digits encoded into three bytes according to different sources).</p><p>Another question is where you have taken the capture. Is there any ISUP-aware equipment (like another voice exchange or an STP) between the originating MSS and the capturing point, or is it just transport equipment which is not supposed to tamper with the message contents?</p></div><div id="comment-54247-info" class="comment-info"><span class="comment-age">(23 Jul '16, 04:00)</span> sindy</div></div><span id="54248"></span><div id="comment-54248" class="comment"><div id="post-54248-score" class="comment-score"></div><div class="comment-text"><p>Just an afterthought, the ISUP dissector, like some others, does not show in the dissection pane the contents of parameters it does not know. So the lines</p><pre><code>Parameter Type unknown/reserved (3 Bytes)
    Optional Parameter: Carrier identification (197)
    Parameter Length: 3</code></pre><p>in your dissection may actually represent a non-dissected JIP. The variant setting in Wireshark's ISUP preferences does not offer ANSI ISUP (at least in 2.0.4), so the 197 which represents Carrier identification in the ITU variant may represent the ANSI-specific JIP, and that would explain the whole mystery.</p><p>If you left-click at the first line (<code>Parameter Type unknown/reserved (3 Bytes)</code>), you should see five bytes highlighted in the lower, "packet bytes" pane. The first two should be <code>c5 03</code>, the remaining three would be the JIP value in 6 BCD format (4 bits/digit), probably with swapped order of digits - in ISUP and SS7 in general, the lower nibble has to be read first. So bytes <code>32 54 76</code> would represent a JIP value of <code>234-567</code>.</p></div><div id="comment-54248-info" class="comment-info"><span class="comment-age">(23 Jul '16, 05:25)</span> sindy</div></div><span id="54249"></span><div id="comment-54249" class="comment"><div id="post-54249-score" class="comment-score"></div><div class="comment-text"><p>And an afterthought No. 2: thanks to <a href="https://www.dialogic.com/webhelp/MSP1010/10.2.3/WebHelp/MSP_DG/ISUP/Message_Parameters.htm">Dialogic's WebHelp</a>, I've discovered that the JIP parameter code is 196, not 197, and that Wireshark's ISUP dissector can recognize it properly. So it decodes a <code>c4 03 32 54 76</code> byte sequence like this:</p><pre><code>Jurisdiction: 234567
    Optional Parameter: Jurisdiction (196)
    Parameter Length: 3
    Jurisdiction: 234567
        .... 0010 = Address signal digit: 2 (2)
        0011 .... = Address signal digit: 3 (3)
        .... 0100 = Address signal digit: 4 (4)
        0101 .... = Address signal digit: 5 (5)
        .... 0110 = Address signal digit: 6 (6)
        0111 .... = Address signal digit: 7 (7)</code></pre><p>Now it is up to you to check whether the mistake is at the sending MSS side or somewhere else (I assume that guys at Dialogic would not publish rubbish).</p></div><div id="comment-54249-info" class="comment-info"><span class="comment-age">(23 Jul '16, 06:05)</span> sindy</div></div><span id="54293"></span><div id="comment-54293" class="comment"><div id="post-54293-score" class="comment-score"></div><div class="comment-text"><p><code>000000  00 0c 00 04 6d 33 75 61 00 14 00 04 c0 a8 7d 44 000010  00 15 00 04 c0 a8 7b 24 00 18 00 04 00 00 00 01 000020  00 19 00 04 00 00 6e 29 00 1a 00 04 00 00 0b 5a 000030  00 1e 00 04 00 00 4d 81 00 00 00 00 01 00 01 01 000040  00 00 00 4c 02 00 00 08 00 00 00 08 02 10 00 3b 000050  00 fa 84 01 00 05 5c 2e 05 02 00 0b 92 01 01 00 000060  60 10 0a 03 06 0d 03 90 90 a2 07 03 10 12 57 40 000070  01 86 0a 07 03 13 12 47 79 82 27 ea 01 00 c5 03 000080  22 40 23 c7 01 20 00 00</code></p><p>Encapsulation type: <code>Wireshark upper PDU export</code></p></div><div id="comment-54293-info" class="comment-info"><span class="comment-age">(25 Jul '16, 06:23)</span> Michael Pier...</div></div><span id="54297"></span><div id="comment-54297" class="comment"><div id="post-54297-score" class="comment-score"></div><div class="comment-text"><p><a href="https://drive.google.com/open?id=0BxQ87I-IfPX3TVRfT2dRQmVBTHc">https://drive.google.com/open?id=0BxQ87I-IfPX3TVRfT2dRQmVBTHc</a></p><p>This work ?</p></div><div id="comment-54297-info" class="comment-info"><span class="comment-age">(25 Jul '16, 06:43)</span> Michael Pier...</div></div><span id="54298"></span><div id="comment-54298" class="comment not_top_scorer"><div id="post-54298-score" class="comment-score"></div><div class="comment-text"><p>Yes, this worked, asking nothing at all :-)</p></div><div id="comment-54298-info" class="comment-info"><span class="comment-age">(25 Jul '16, 06:46)</span> sindy</div></div><span id="54299"></span><div id="comment-54299" class="comment not_top_scorer"><div id="post-54299-score" class="comment-score"></div><div class="comment-text"><p>Ohhh forgot about this. This is a snip from the outgoing MSS. They sent me a word doc text decode and not the hex, but you can see if is going out C4 (196)</p><pre><code>139       | 1100 0100 | Jurisdiction Information Identifier: c4                                 
140       | 0000 0011 |   Length: 3 octet(s)                                                    
141       | 0001 0010 |   Address Signal: 217497                                                
142       | 0100 0111 |   Address Signal:                                                       
143       | 0111 1001 |   Address Signal:                                                       
144       | 0000 0000 | End of Optional Parameters: 0                                           
          |           | IETF.M3UA                                                               
145       | 0000 0000 |   Padding: 0000(hex)                                                    
146       | 0000 0000 |   Padding:</code></pre></div><div id="comment-54299-info" class="comment-info"><span class="comment-age">(25 Jul '16, 06:47)</span> Michael Pier...</div></div><span id="54300"></span><div id="comment-54300" class="comment not_top_scorer"><div id="post-54300-score" class="comment-score"></div><div class="comment-text"><p>OK, so if the Jurisdiction ID is actually <code>220432</code>, then some equipment along the path malforms the parameter name from <code>c4</code> to <code>c5</code> and that's it.</p><p>As <code>c5</code> is not a standardized name of any ISUP parameter (well, at least according to the friend at Dialogic, maybe something in GR-317-CORE has changed since they've published that list?), I would suspect the last exchange in the chain to be guilty, as a non-standard parameter should normally be accompanied by a PCI parameter so if it has been malformed by some machine mid-stream, the sender of the <code>IAM</code> should have got at least an upstream <code>CFN</code> by the first recipient of the malformed version.</p></div><div id="comment-54300-info" class="comment-info"><span class="comment-age">(25 Jul '16, 06:55)</span> sindy</div></div><span id="54301"></span><div id="comment-54301" class="comment not_top_scorer"><div id="post-54301-score" class="comment-score"></div><div class="comment-text"><p>Actually I think we may already know who the culprit is, as this wouldn't be the first time they have screwed up something for us. Last time it was they were not sending the GAP for a LNP</p></div><div id="comment-54301-info" class="comment-info"><span class="comment-age">(25 Jul '16, 06:57)</span> Michael Pier...</div></div><span id="54302"></span><div id="comment-54302" class="comment not_top_scorer"><div id="post-54302-score" class="comment-score"></div><div class="comment-text"><p>We were writing against each other (simultaneously) :-)</p><p>I assume the text from the originator is from another call? Because your IAM at CIC 402 says <code>220432</code> (as <code>c5</code>), while their text says <code>217497</code>... If it is the same call, the evil ghost does much more damage.</p></div><div id="comment-54302-info" class="comment-info"><span class="comment-age">(25 Jul '16, 07:00)</span> sindy</div></div><span id="54303"></span><div id="comment-54303" class="comment not_top_scorer"><div id="post-54303-score" class="comment-score"></div><div class="comment-text"><p>I will know better here shortly as I have some end to end testing scheduled.</p></div><div id="comment-54303-info" class="comment-info"><span class="comment-age">(25 Jul '16, 07:01)</span> Michael Pier...</div></div><span id="54307"></span><div id="comment-54307" class="comment not_top_scorer"><div id="post-54307-score" class="comment-score"></div><div class="comment-text"><p>Just added a new file. Outgoing_IAM.txt where you can see the outgoing JIP is 217304, and a wireshark cap where there is no JIP that I can find.</p></div><div id="comment-54307-info" class="comment-info"><span class="comment-age">(25 Jul '16, 10:02)</span> Michael Pier...</div></div><span id="54308"></span><div id="comment-54308" class="comment not_top_scorer"><div id="post-54308-score" class="comment-score"></div><div class="comment-text"><p><a href="https://www.dialogic.com/~/media/manuals/ss7/cd/GenericInfo/ProtocolDocumentation/U04SSS-ISUP-PM.pdf">https://www.dialogic.com/~/media/manuals/ss7/cd/GenericInfo/ProtocolDocumentation/U04SSS-ISUP-PM.pdf</a></p><p>Found the 199 in this</p></div><div id="comment-54308-info" class="comment-info"><span class="comment-age">(25 Jul '16, 10:13)</span> Michael Pier...</div></div><span id="54309"></span><div id="comment-54309" class="comment not_top_scorer"><div id="post-54309-score" class="comment-score"></div><div class="comment-text"><p>Weird enough, I can see only iam_issue.pcapng (plus the original isup_cap.pcapng) in the Google drive directory, but no text file.</p><p>But that's not important, I guess you are sure enough that the four IAMs which have arrived are reincarnations of the one the calling MSS has sent.</p><p>And as there is a JIP in the source IAM, with a value of 217304, and what arrives through the jungle is an IAM with a <code>c5</code> parameter of same length but different contents (220432 in all 4 IAMs in your capture), you may be sure that "something" in the chain affects the IAM contents.</p><p>As you get this <code>c5 03 22 40 23</code> in all 4 IAMs, one more question - was there just a single call attempt at the calling side? If yes, I'd expect that</p><ul><li><p>either the <code>c5 03 22 40 23</code> has been put to the IAM before the exchanges which attempted to deliver the IAM to you using several distinct routes,</p></li><li><p>or it has been put there between the point where these routes join again and the place where you capture.</p></li></ul><p>As nothing has survived from the original value, we cannot exclude that one exchange has erased the JIP and another one has inserted the <code>c5 03 22 40 23</code>.</p><p>As for the 199 (0xc7), I could imagine some exchanges to insert an empty Generic Name parameter to an egress IAM if none was available at ingress. Same case for the empty Originating Line Information.</p><p>Are you sure that the whole call path passes through North American operators?</p></div><div id="comment-54309-info" class="comment-info"><span class="comment-age">(25 Jul '16, 10:26)</span> sindy</div></div><span id="54310"></span><div id="comment-54310" class="comment not_top_scorer"><div id="post-54310-score" class="comment-score"></div><div class="comment-text"><p>Yes this is a single call. Because our MSS doesn't like this IAM it is not sending an ACM so the Tandem tries it on a different CIC. And yes it is a call originating in US and terminating in US. I filtered on a few other calls for the Generic Name parameter and I do see calls which are successful IF the Generic Name actually has something included.</p></div><div id="comment-54310-info" class="comment-info"><span class="comment-age">(25 Jul '16, 10:36)</span> Michael Pier...</div></div><span id="54311"></span><div id="comment-54311" class="comment not_top_scorer"><div id="post-54311-score" class="comment-score"></div><div class="comment-text"><p>I uploaded generic_name.pcapng where there is actually information in there.</p></div><div id="comment-54311-info" class="comment-info"><span class="comment-age">(25 Jul '16, 10:39)</span> Michael Pier...</div></div><span id="54312"></span><div id="comment-54312" class="comment not_top_scorer"><div id="post-54312-score" class="comment-score"></div><div class="comment-text"><p>Wow... in the Dialogic document in which you've found the 199, there is also 197 = 0xc5, called "Carrier Identification". So maybe it has been added to the specification since the Dialogic document I was referring to was published? In any case, the Wireshark dissector does not like something about its contents (because it states the proper name and because the size of the parameter value is correct, 3 octets), or there is a bug in the dissector. Can you check T1.113 Section 3.8A to find out whether the <code>22 40 23</code> is a legal contents of this parameter? If it is, it would be best to file a bug at Wireshark bugzilla, attaching the full relevant description from T1.113.</p><p>But in any case, as the Carrier Identification legally exists, I would dare to conclude that its addition to the IAM and the disappearance of the JIP from it are not related to each other.</p><p>As for the call path, I understand that the origin and destination are in the US, I was asking whether you can be sure it doesn't run via e.g. LatAm which uses the ETSI ISUP flavors, so the JIP may not be supported there.</p><p>Does your receiving switch complain about something about the IAM to its logs, if any?</p></div><div id="comment-54312-info" class="comment-info"><span class="comment-age">(25 Jul '16, 10:53)</span> sindy</div></div><span id="54314"></span><div id="comment-54314" class="comment not_top_scorer"><div id="post-54314-score" class="comment-score"></div><div class="comment-text"><p>3.20C Generic Name Parameter<br />
The format of the generic name parameter field shall be as shown in Figure 18C/T1.113.3.<br />
The following codes are used in the subfields of the generic name parameter field:<br />
</p><pre><code>(1) Presentation (Pres.)
0 0 presentation allowed
0 1 presentation restricted
1 0 blocking toggle
1 1 no indication
(2) Availability (Avail.)
0 name available/unknown
1 name not available
(3) Type of name
0 0 0 spare
0 0 1 calling name
0 1 0 original called name
0 1 1 redirecting name
1 0 0 connected name
1 0 1 }
   to } spare
1 1 1 }</code></pre><p>Up to 15 characters of name information are coded in IA5 format.</p></div><div id="comment-54314-info" class="comment-info"><span class="comment-age">(25 Jul '16, 12:30)</span> Michael Pier...</div></div><span id="54315"></span><div id="comment-54315" class="comment not_top_scorer"><div id="post-54315-score" class="comment-score"></div><div class="comment-text"><p>That didn't paste right so I added some new text files to that shared folder.</p></div><div id="comment-54315-info" class="comment-info"><span class="comment-age">(25 Jul '16, 12:38)</span> Michael Pier...</div></div><span id="54316"></span><div id="comment-54316" class="comment not_top_scorer"><div id="post-54316-score" class="comment-score"></div><div class="comment-text"><p>Seems we are slightly mistuned :-)</p><ul><li><p>I wanted a description of the Carrier Identfication parameter (197 = 0xc5), but in the meantime I've discovered that T1.113 can be downloaded from the 3GPP archive. Using the description from there, I conclude that the Carrier Identifier data in your IAMs have a proper contents, so there is a bug in Wireshark dissector which can be filed.</p></li><li><p>you have instead provided a description of Generic Name (199 = 0xc7) which Wireshark dissects properly; as the whole parameter wasn't available in the original IAM, it seems fine to me that one of the exchanges along the path has added that parameter with zero size and "presentation alowed, name available or unknown, calling name" properties.</p></li></ul><p>Off topic: once you are through with this issue, please have a look at the formatting possibilities of this site. They can be used not only for Questions and Answers but also for Comments. Hint: use the form field intended for writing an Answer so that you would see the result in the preview, then cut the text from there and paste it to the form field which opens after you press the Comment button.</p></div><div id="comment-54316-info" class="comment-info"><span class="comment-age">(25 Jul '16, 12:55)</span> sindy</div></div></div><div id="comment-tools-54244" class="comment-tools"><span class="comments-showing"> showing 5 of 20 </span> <a href="#" class="show-all-comments-link">show 15 more comments</a></div><div class="clear"></div><div id="comment-54244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54367"></span>

<div id="answer-container-54367" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54367-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>So to wrap the chain of comments up into a proper Answer to the original Question:</p><p>(1) from the <strong>protocol</strong> point of view, the IAM in the example is <strong>not</strong> malformed - all parameters it contains are properly formatted, although their values may be unusual.</p><p>(2) from the <strong>service</strong> point of view, the contents of the IAM has changed in transit to an extent which may cause interworking or even legal issues, although from the protocol point of view alone, all the affected parameters are optional:</p><ul><li><p>some parameters from the original IAM have been lost in transit (in particular, the Jurisdiction Information),<br />
</p></li><li><p>others have been added (the Generic Name, the Carrier Identification),<br />
</p></li><li><p>the contents of some others has changed in transit (the Originating Line Info which was 63 at the source but 00 at the point of capture).</p></li></ul><p>(3) from <strong>Wireshark</strong> point of view, the ISUP dissector doesn't handle the Carrier Identification parameter properly. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12674">An enhancement bug</a> has been filed on that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '16, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jul '16, 05:45</p></div></div><div id="comments-container-54367" class="comments-container"><span id="54402"></span><div id="comment-54402" class="comment"><div id="post-54402-score" class="comment-score"></div><div class="comment-text"><p>Sorry it took me so long to get back on this. Yes I would say that you are accurate and I appreciate the assistance. On a side note the issue was resolved by a LEC routing change</p></div><div id="comment-54402-info" class="comment-info"><span class="comment-age">(28 Jul '16, 08:12)</span> Michael Pier...</div></div></div><div id="comment-tools-54367" class="comment-tools"></div><div class="clear"></div><div id="comment-54367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

