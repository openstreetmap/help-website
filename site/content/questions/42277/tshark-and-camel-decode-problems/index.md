+++
type = "question"
title = "Tshark and Camel decode problems"
description = '''Hello. Please help. I use Tshark (1.8.10) to capture TCAP-&amp;gt;CAMEL messages on Centos 6.3. And what I found is that Tshark can&#x27;t decode EstablishTemporaryConnection operation and others (applyCharging, furnishChargingInformation, etc.) and InitialDP (where tcap.application_context_name == 0.4.0.0.1...'''
date = "2015-05-10T04:41:00Z"
lastmod = "2015-05-10T04:41:00Z"
weight = 42277
keywords = [ "sctp", "decodeproblems", "tshark", "camel" ]
aliases = [ "/questions/42277" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark and Camel decode problems](/questions/42277/tshark-and-camel-decode-problems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42277-score" class="post-score" title="current number of votes">0</div><span id="post-42277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello.</p><p>Please help. I use Tshark (1.8.10) to capture TCAP-&gt;CAMEL messages on Centos 6.3. And what I found is that Tshark can't decode EstablishTemporaryConnection operation and others (applyCharging, furnishChargingInformation, etc.) and InitialDP (where tcap.application_context_name == 0.4.0.0.1.21.3.4). If I open .pcap file in Wireshark (Version 1.12.4 (v1.12.4-0-gb4861da from master-1.12)) on Windows 7, all messages decoded correctly.</p><p>i use next command:</p><p>tshark -i any -f sctp -d sccp.ssn==146,tcap -O sccp,tcap,camel -V -c 500 -x</p><p>Here is the output, where Camel message is decoded (InitialDP):</p><pre><code>Frame 8: 284 bytes on wire (2272 bits), 284 bytes captured (2272 bits) on interface 0
Linux cooked capture
Internet Protocol Version 4, Src: 10.20.13.6 (10.20.13.6), Dst: 10.20.17.1 (10.20.17.1)
Stream Control Transmission Protocol, Src Port: 3724 (3724), Dst Port: 3724 (3724)
MTP 3 User Adaptation Layer
Signalling Connection Control Part
    Message Type: Unitdata (0x09)
    .... 0001 = Class: 0x01
    1000 .... = Message handling: Return message on error (0x08)
    Pointer to first Mandatory Variable parameter: 3
    Pointer to second Mandatory Variable parameter: 14
    Pointer to third Mandatory Variable parameter: 25
    Called Party address (11 bytes)
        Address Indicator
            0... .... = Reserved for national use: 0x00
            .1.. .... = Routing Indicator: Route on SSN (0x01)
            ..01 00.. = Global Title Indicator: Translation Type, Numbering Plan, Encoding Scheme, and Nature of Address Indicator included (0x04)
            .... ..1. = SubSystem Number Indicator: SSN present (0x01)
            .... ...0 = Point Code Indicator: Point Code not present (0x00)
        SubSystem Number: CAP (146)
        [Linked to TCAP]
        Global Title 0x4 (9 bytes)
            Translation Type: 0x00
            0001 .... = Numbering Plan: ISDN/telephony (0x01)
            .... 0010 = Encoding Scheme: BCD, even number of digits (0x02)
            .000 0100 = Nature of Address Indicator: International number (0x04)
            Called Party Digits: 856209000332
                Called or Calling GT Digits: 856209000332
                Number of Called Party Digits: 12
                Country Code: 856 Laos (length 3)
    Calling Party address (11 bytes)
        Address Indicator
            0... .... = Reserved for national use: 0x00
            .0.. .... = Routing Indicator: Route on GT (0x00)
            ..01 00.. = Global Title Indicator: Translation Type, Numbering Plan, Encoding Scheme, and Nature of Address Indicator included (0x04)
            .... ..1. = SubSystem Number Indicator: SSN present (0x01)
            .... ...0 = Point Code Indicator: Point Code not present (0x00)
        SubSystem Number: CAP (146)
        [Linked to TCAP]
        Global Title 0x4 (9 bytes)
            Translation Type: 0x00
            0001 .... = Numbering Plan: ISDN/telephony (0x01)
            .... 0010 = Encoding Scheme: BCD, even number of digits (0x02)
            .000 0100 = Nature of Address Indicator: International number (0x04)
            Calling Party Digits: 856209000004
                Called or Calling GT Digits: 856209000004
                Number of Calling Party Digits: 12
                Country Code: 856 Laos (length 3)
Transaction Capabilities Application Part
    begin
        Source Transaction ID
            Transaction Id: 03ff6472
        oid: 0.0.17.773.1.1.1 (id-as-dialogue)
        dialogueRequest
            application-context-name: 0.4.0.0.1.0.50.1 (CAP-v2-gsmSSF-to-gsmSCF-AC)
        components: 1 item
            Component: invoke (1)
                invoke
                    invokeID: 1
                    opCode: localValue (0)
                        localValue: 0
                    CONSTRUCTOR
                        CONSTRUCTOR Tag
                        Tag: 0x00
                        Length: 117
                        Parameter (0x00)
                            Tag: 0x00
                            Length: 1
                        Data: 01
                        Parameter (0x03)
                            Tag: 0x03
                            Length: 9
                        Data: 84
                        Parameter (0x05)
                            Tag: 0x05
                            Length: 1
                        Data: 0a
                        Parameter (0x0a)
                            Tag: 0x0a
                            Length: 5
                        Data: 84
                        CONSTRUCTOR
                            CONSTRUCTOR Tag
                            Tag: 0x02
                            Length: 5
                            Parameter (0x00)
                                Tag: 0x00
                                Length: 3
                            Data: 80
                        Parameter (0x1c)
                            Tag: 0x1c
                            Length: 1
                        Data: 02
                        Parameter (0x32)
                            Tag: 0x32
                            Length: 8
                        Data: 54
                        CONSTRUCTOR
                            CONSTRUCTOR Tag
                            Tag: 0x02
                            Length: 23
                            Parameter (0x02)
                                Tag: 0x02
                                Length: 1
                            Data: 00
                            Parameter (0x01)
                                Tag: 0x01
                                Length: 7
                            Data: 91
                            CONSTRUCTOR
                                CONSTRUCTOR Tag
                                Tag: 0x02
                                Length: 9
                                Parameter (0x00)
                                    Tag: 0x00
                                    Length: 7
                                Data: 54
                        CONSTRUCTOR
                            CONSTRUCTOR Tag
                            Tag: 0x02
                            Length: 3
                            Parameter (0x03)
                                Tag: 0x03
                                Length: 1
                            Data: 11
                        Parameter (0x36)
                            Tag: 0x36
                            Length: 5
                        Data: 17
                        Parameter (0x37)
                            Tag: 0x37
                            Length: 7
                        Data: 91
                        Parameter (0x38)
                            Tag: 0x38
                            Length: 8
                        Data: 91
                        Parameter (0x39)
                            Tag: 0x39
                            Length: 8
                        Data: 02
Camel
    invoke
        invokeId: present (0)
            present: 1
        opcode: local (0)
            local: initialDP (0)
        InitialDPArg
            serviceKey: 1
            callingPartyNumber: 841358269066817706
                1... .... = Odd/even indicator: odd number of address signals
                .000 0100 = Nature of address indicator: international number (4)
                0... .... = NI indicator: complete
                .001 .... = Numbering plan indicator: ISDN (Telephony) numbering plan (1)
                .... 00.. = Address presentation restricted indicator: presentation allowed (0)
                .... ..11 = Screening indicator: network provided (3)
                Calling Party Number: 8562096618776
                    .... 1000 = Address signal digit: 8 (8)
                    0101 .... = Address signal digit: 5 (5)
                    .... 0110 = Address signal digit: 6 (6)
                    0010 .... = Address signal digit: 2 (2)
                    .... 0000 = Address signal digit: 0 (0)
                    1001 .... = Address signal digit: 9 (9)
                    .... 0110 = Address signal digit: 6 (6)
                    0110 .... = Address signal digit: 6 (6)
                    .... 0001 = Address signal digit: 1 (1)
                    1000 .... = Address signal digit: 8 (8)
                    .... 0111 = Address signal digit: 7 (7)
                    0111 .... = Address signal digit: 7 (7)
                    .... 0110 = Address signal digit: 6 (6)
                    E.164 Calling party number digits: 8562096618776
            callingPartysCategory: ordinary calling subscriber (10)
            locationNumber: 8413584601
                1... .... = Odd/even indicator: odd number of address signals
                .000 0100 = Nature of address indicator: international number (4)
                0... .... = INN indicator: routing to internal network number allowed 
                .001 .... = Numbering plan indicator: ISDN (Telephony) numbering plan (1)
                .... 00.. = Address presentation restricted indicator: presentation allowed (0)
                .... ..11 = Screening indicator: network provided (3)
                Location number: 85641
                    .... 1000 = Address signal digit: 8 (8)
                    0101 .... = Address signal digit: 5 (5)
                    .... 0110 = Address signal digit: 6 (6)
                    0100 .... = Address signal digit: 4 (4)
                    .... 0001 = Address signal digit: 1 (1)
            bearerCapability: bearerCap (0)
                bearerCap: 8090a3
                1... .... = Extension indicator: last octet
                .00. .... = Coding standard: ITU-T standardized coding (0x00)
                ...0 0000 = Information transfer capability: Speech (0x00)
                1... .... = Extension indicator: last octet
                .00. .... = Transfer mode: Circuit mode (0x00)
                ...1 0000 = Information transfer rate: 64 kbit/s (0x10)
                1... .... = Extension indicator: last octet
                .01. .... = Layer identification: Layer 1 identifier (0x01)
                ...0 0011 = User information layer 1 protocol: Recommendation G.711 A-law (0x03)
            eventTypeBCSM: collectedInfo (2)
            iMSI: 54072301244986f5
            TBCD digits: 457032104294685
            locationInformation
                ageOfLocationInformation: 0
                vlr-number: 91582690000040
                    1... .... = Extension: No Extension
                    .001 .... = Nature of number: International Number (0x01)
                    .... 0001 = Number plan: ISDN/Telephony Numbering (Rec ITU-T E.164) (0x01)
                    Address digits: 856209000004
                    Country Code: 856 Laos (length 3)
                cellGlobalIdOrServiceAreaIdOrLAI: cellGlobalIdOrServiceAreaIdFixedLength (0)
                    cellGlobalIdOrServiceAreaIdFixedLength: 54f7301fce6863
            ext-basicServiceCode: ext-Teleservice (3)
                ext-Teleservice: telephony (17)
            callReferenceNumber: 17818f8c13
            mscAddress: 91582690000040
                1... .... = Extension: No Extension
                .001 .... = Nature of number: International Number (0x01)
                .... 0001 = Number plan: ISDN/Telephony Numbering (Rec ITU-T E.164) (0x01)
                Address digits: 856209000004
                Country Code: 856 Laos (length 3)
            calledPartyBCDNumber: 91582690871949f0
                1... .... = Extension: No Extension
                .001 .... = Type of number: International Number (0x01)
                .... 0001 = Numbering plan identification: ISDN/Telephony Numbering (Rec ITU-T E.164) (0x01)
                BCD Digits: 8562097891940
            timeAndTimezone: 0251500161353223

0000  00 03 00 01 00 06 08 19 a6 25 f6 b3 00 00 08 00   .........%......
0010  45 02 01 0c e1 6f 00 00 fe 84 a7 cd 0a 14 0d 06   E....o..........
0020  0a 14 11 01 0e 8c 0e 8c 49 82 72 5c 31 41 9a 1e   ........I.r\1A..
0030  00 03 00 ec 5d f1 9b 28 00 0d 47 22 00 00 00 03   ....]..(..G&quot;....
0040  01 00 01 01 00 00 00 dc 02 10 00 d4 00 00 03 ed   ................
0050  00 00 05 02 03 03 00 0e 09 81 03 0e 19 0b 52 92   ..............R.
0060  00 12 04 58 26 90 00 30 23 0b 12 92 00 12 04 58   ...X&amp;..0#......X
0070  26 90 00 00 40 a6 62 81 a3 48 04 03 ff 64 72 6b   &amp;[email protected]
0080  1a 28 18 06 07 00 11 86 05 01 01 01 a0 0d 60 0b   .(............`.
0090  a1 09 06 07 04 00 00 01 00 32 01 6c 7f a1 7d 02   .........2.l..}.
00a0  01 01 02 01 00 30 75 80 01 01 83 09 84 13 58 26   .....0u.......X&amp;
00b0  90 66 81 77 06 85 01 0a 8a 05 84 13 58 46 01 bb   .f.w........XF..
00c0  05 80 03 80 90 a3 9c 01 02 9f 32 08 54 07 23 01   ..........2.T.#.
00d0  24 49 86 f5 bf 34 17 02 01 00 81 07 91 58 26 90   $I...4.......X&amp;.
00e0  00 00 40 a3 09 80 07 54 f7 30 1f ce 68 63 bf 35   [email protected]
00f0  03 83 01 11 9f 36 05 17 81 8f 8c 13 9f 37 07 91   .....6.......7..
0100  58 26 90 00 00 40 9f 38 08 91 58 26 90 87 19 49   X&amp;[email protected]&amp;...I
0110  f0 9f 39 08 02 51 50 01 61 35 32 23               ..9..QP.a52#</code></pre><p><strong>this is not decoded message (InitialDP):</strong></p><pre><code>Frame 188: 304 bytes on wire (2432 bits), 304 bytes captured (2432 bits) on interface 0
Linux cooked capture
Internet Protocol Version 4, Src: 10.20.13.6 (10.20.13.6), Dst: 10.20.17.1 (10.20.17.1)
Stream Control Transmission Protocol, Src Port: 3722 (3722), Dst Port: 3722 (3722)
MTP 3 User Adaptation Layer
Signalling Connection Control Part
    Message Type: Unitdata (0x09)
    .... 0001 = Class: 0x01
    1000 .... = Message handling: Return message on error (0x08)
    Pointer to first Mandatory Variable parameter: 3
    Pointer to second Mandatory Variable parameter: 14
    Pointer to third Mandatory Variable parameter: 25
    Called Party address (11 bytes)
        Address Indicator
            0... .... = Reserved for national use: 0x00
            .1.. .... = Routing Indicator: Route on SSN (0x01)
            ..01 00.. = Global Title Indicator: Translation Type, Numbering Plan, Encoding Scheme, and Nature of Address Indicator included (0x04)
            .... ..1. = SubSystem Number Indicator: SSN present (0x01)
            .... ...0 = Point Code Indicator: Point Code not present (0x00)
        SubSystem Number: CAP (146)
        [Linked to TCAP]
        Global Title 0x4 (9 bytes)
            Translation Type: 0x00
            0001 .... = Numbering Plan: ISDN/telephony (0x01)
            .... 0010 = Encoding Scheme: BCD, even number of digits (0x02)
            .000 0100 = Nature of Address Indicator: International number (0x04)
            Called Party Digits: 856209000332
                Called or Calling GT Digits: 856209000332
                Number of Called Party Digits: 12
                Country Code: 856 Laos (length 3)
    Calling Party address (11 bytes)
        Address Indicator
            0... .... = Reserved for national use: 0x00
            .0.. .... = Routing Indicator: Route on GT (0x00)
            ..01 00.. = Global Title Indicator: Translation Type, Numbering Plan, Encoding Scheme, and Nature of Address Indicator included (0x04)
            .... ..1. = SubSystem Number Indicator: SSN present (0x01)
            .... ...0 = Point Code Indicator: Point Code not present (0x00)
        SubSystem Number: CAP (146)
        [Linked to TCAP]
        Global Title 0x4 (9 bytes)
            Translation Type: 0x00
            0001 .... = Numbering Plan: ISDN/telephony (0x01)
            .... 0010 = Encoding Scheme: BCD, even number of digits (0x02)
            .000 0100 = Nature of Address Indicator: International number (0x04)
            Calling Party Digits: 856209000004
                Called or Calling GT Digits: 856209000004
                Number of Calling Party Digits: 12
                Country Code: 856 Laos (length 3)
Transaction Capabilities Application Part
    begin
        Source Transaction ID
            Transaction Id: 03f35abe
        oid: 0.0.17.773.1.1.1 (id-as-dialogue)
        dialogueRequest
            application-context-name: 0.4.0.0.1.21.3.4 (itu-t.4.0.0.1.21.3.4)
        components: 1 item
            Component: invoke (1)
                invoke
                    invokeID: 1
                    opCode: localValue (0)
                        localValue: 0
                    CONSTRUCTOR
                        CONSTRUCTOR Tag
                        Tag: 0x00
                        Length: 132
                        Parameter (0x00)
                            Tag: 0x00
                            Length: 1
                        Data: 01
                        Parameter (0x02)
                            Tag: 0x02
                            Length: 9
                        Data: 84
                        Parameter (0x03)
                            Tag: 0x03
                            Length: 9
                        Data: 84
                        Parameter (0x05)
                            Tag: 0x05
                            Length: 1
                        Data: 0a
                        Parameter (0x0a)
                            Tag: 0x0a
                            Length: 5
                        Data: 84
                        CONSTRUCTOR
                            CONSTRUCTOR Tag
                            Tag: 0x02
                            Length: 5
                            Parameter (0x00)
                                Tag: 0x00
                                Length: 3
                            Data: 80
                        Parameter (0x1c)
                            Tag: 0x1c
                            Length: 1
                        Data: 0e
                        Parameter (0x32)
                            Tag: 0x32
                            Length: 8
                        Data: 54
                        CONSTRUCTOR
                            CONSTRUCTOR Tag
                            Tag: 0x02
                            Length: 2
                            Parameter (0x00)
                                Tag: 0x00
                                Length: 0
                        CONSTRUCTOR
                            CONSTRUCTOR Tag
                            Tag: 0x02
                            Length: 33
                            Parameter (0x02)
                                Tag: 0x02
                                Length: 1
                            Data: 02
                            Parameter (0x00)
                                Tag: 0x00
                                Length: 8
                            Data: 10
                            Parameter (0x01)
                                Tag: 0x01
                                Length: 7
                            Data: 91
                            CONSTRUCTOR
                                CONSTRUCTOR Tag
                                Tag: 0x02
                                Length: 9
                                Parameter (0x00)
                                    Tag: 0x00
                                    Length: 7
                                Data: 54
                        CONSTRUCTOR
                            CONSTRUCTOR Tag
                            Tag: 0x02
                            Length: 3
                            Parameter (0x03)
                                Tag: 0x03
                                Length: 1
                            Data: 11
                        Parameter (0x36)
                            Tag: 0x36
                            Length: 5
                        Data: 0b
                        Parameter (0x37)
                            Tag: 0x37
                            Length: 7
                        Data: 91
                        Parameter (0x39)
                            Tag: 0x39
                            Length: 8
                        Data: 02
Data (144 bytes)

0000  00 03 00 01 00 06 08 19 a6 25 f6 b3 00 00 08 00   .........%......
0010  45 02 01 20 e1 71 00 00 fe 84 a7 b7 0a 14 0d 06   E.. .q..........
0020  0a 14 11 01 0e 8a 0e 8a 9f 0a e7 f1 28 9e 9b 36   ............(..6
0030  00 03 01 00 6a f5 5f 65 00 03 0b c8 00 00 00 03   ....j._e........
0040  01 00 01 01 00 00 00 f0 02 10 00 e6 00 00 03 ed   ................
0050  00 00 05 02 03 03 00 04 09 81 03 0e 19 0b 52 92   ..............R.
0060  00 12 04 58 26 90 00 30 23 0b 12 92 00 12 04 58   ...X&amp;..0#......X
0070  26 90 00 00 40 b8 62 81 b5 48 04 03 f3 5a be 6b   &amp;[email protected]
0080  1a 28 18 06 07 00 11 86 05 01 01 01 a0 0d 60 0b   .(............`.
0090  a1 09 06 07 04 00 00 01 15 03 04 6c 81 90 a1 81   ...........l....
00a0  8d 02 01 01 02 01 00 30 81 84 80 01 01 82 09 84   .......0........
00b0  10 58 26 90 55 36 87 04 83 09 84 13 58 26 90 97   .X&amp;.U6......X&amp;..
00c0  84 24 01 85 01 0a 8a 05 84 13 58 46 01 bb 05 80   .$........XF....
00d0  03 80 90 a3 9c 01 0e 9f 32 08 54 07 23 01 09 50   ........2.T.#..P
00e0  41 f5 bf 33 02 80 00 bf 34 21 02 01 02 80 08 10   A..3....4!......
00f0  00 00 00 00 00 00 00 81 07 91 58 26 90 00 00 40   ..........X&amp;[email protected]
0100  a3 09 80 07 54 f7 30 1f ce 6e 84 bf 35 03 83 01   ....T.0..n..5...
0110  11 9f 36 05 0b 11 40 8c 13 9f 37 07 91 58 26 90   [email protected]&amp;.
0120  00 00 40 9f 39 08 02 51 50 01 61 35 32 23 00 00   [email protected]#..</code></pre><p><strong>and another not decoded message (applyChargingReport and eventReportBCSM):</strong></p><pre><code>Frame 10: 280 bytes on wire (2240 bits), 280 bytes captured (2240 bits) on interface 0
Linux cooked capture
Internet Protocol Version 4, Src: 10.20.13.5 (10.20.13.5), Dst: 10.20.17.1 (10.20.17.1)
Stream Control Transmission Protocol, Src Port: 3721 (3721), Dst Port: 3721 (3721)
MTP 3 User Adaptation Layer
Signalling Connection Control Part
    Message Type: Unitdata (0x09)
    .... 0001 = Class: 0x01
    1000 .... = Message handling: Return message on error (0x08)
    Pointer to first Mandatory Variable parameter: 3
    Pointer to second Mandatory Variable parameter: 14
    Pointer to third Mandatory Variable parameter: 25
    Called Party address (11 bytes)
        Address Indicator
            0... .... = Reserved for national use: 0x00
            .1.. .... = Routing Indicator: Route on SSN (0x01)
            ..01 00.. = Global Title Indicator: Translation Type, Numbering Plan, Encoding Scheme, and Nature of Address Indicator included (0x04)
            .... ..1. = SubSystem Number Indicator: SSN present (0x01)
            .... ...0 = Point Code Indicator: Point Code not present (0x00)
        SubSystem Number: CAP (146)
        [Linked to TCAP]
        Global Title 0x4 (9 bytes)
            Translation Type: 0x00
            0001 .... = Numbering Plan: ISDN/telephony (0x01)
            .... 0010 = Encoding Scheme: BCD, even number of digits (0x02)
            .000 0100 = Nature of Address Indicator: International number (0x04)
            Called Party Digits: 856209000332
                Called or Calling GT Digits: 856209000332
                Number of Called Party Digits: 12
                Country Code: 856 Laos (length 3)
    Calling Party address (11 bytes)
        Address Indicator
            0... .... = Reserved for national use: 0x00
            .0.. .... = Routing Indicator: Route on GT (0x00)
            ..01 00.. = Global Title Indicator: Translation Type, Numbering Plan, Encoding Scheme, and Nature of Address Indicator included (0x04)
            .... ..1. = SubSystem Number Indicator: SSN present (0x01)
            .... ...0 = Point Code Indicator: Point Code not present (0x00)
        SubSystem Number: CAP (146)
        [Linked to TCAP]
        Global Title 0x4 (9 bytes)
            Translation Type: 0x00
            0001 .... = Numbering Plan: ISDN/telephony (0x01)
            .... 0010 = Encoding Scheme: BCD, even number of digits (0x02)
            .000 0100 = Nature of Address Indicator: International number (0x04)
            Calling Party Digits: 856209000004
                Called or Calling GT Digits: 856209000004
                Number of Calling Party Digits: 12
                Country Code: 856 Laos (length 3)
Transaction Capabilities Application Part
    continue
        Source Transaction ID
            Transaction Id: 03f078a6
        Destination Transaction ID
            Transaction Id: 06fe1341
        components: 1 item
            Component: invoke (1)
                invoke
                    invokeID: 3
                    opCode: localValue (0)
                        localValue: 36
                    Parameter (0x04)
                        Tag: 0x04
                        Length: 16
                    Data: a0
Data (26 bytes)
Stream Control Transmission Protocol
MTP 3 User Adaptation Layer
Signalling Connection Control Part
    Message Type: Unitdata (0x09)
    .... 0001 = Class: 0x01
    1000 .... = Message handling: Return message on error (0x08)
    Pointer to first Mandatory Variable parameter: 3
    Pointer to second Mandatory Variable parameter: 14
    Pointer to third Mandatory Variable parameter: 25
    Called Party address (11 bytes)
        Address Indicator
            0... .... = Reserved for national use: 0x00
            .1.. .... = Routing Indicator: Route on SSN (0x01)
            ..01 00.. = Global Title Indicator: Translation Type, Numbering Plan, Encoding Scheme, and Nature of Address Indicator included (0x04)
            .... ..1. = SubSystem Number Indicator: SSN present (0x01)
            .... ...0 = Point Code Indicator: Point Code not present (0x00)
        SubSystem Number: CAP (146)
        [Linked to TCAP]
        Global Title 0x4 (9 bytes)
            Translation Type: 0x00
            0001 .... = Numbering Plan: ISDN/telephony (0x01)
            .... 0010 = Encoding Scheme: BCD, even number of digits (0x02)
            .000 0100 = Nature of Address Indicator: International number (0x04)
            Called Party Digits: 856209000332
                Called or Calling GT Digits: 856209000332
                Number of Called Party Digits: 12
                Country Code: 856 Laos (length 3)
    Calling Party address (11 bytes)
        Address Indicator
            0... .... = Reserved for national use: 0x00
            .0.. .... = Routing Indicator: Route on GT (0x00)
            ..01 00.. = Global Title Indicator: Translation Type, Numbering Plan, Encoding Scheme, and Nature of Address Indicator included (0x04)
            .... ..1. = SubSystem Number Indicator: SSN present (0x01)
            .... ...0 = Point Code Indicator: Point Code not present (0x00)
        SubSystem Number: CAP (146)
        [Linked to TCAP]
        Global Title 0x4 (9 bytes)
            Translation Type: 0x00
            0001 .... = Numbering Plan: ISDN/telephony (0x01)
            .... 0010 = Encoding Scheme: BCD, even number of digits (0x02)
            .000 0100 = Nature of Address Indicator: International number (0x04)
            Calling Party Digits: 856209000004
                Called or Calling GT Digits: 856209000004
                Number of Calling Party Digits: 12
                Country Code: 856 Laos (length 3)
Transaction Capabilities Application Part
    continue
        Source Transaction ID
            Transaction Id: 03f078a6
        Destination Transaction ID
            Transaction Id: 06fe1341
        components: 1 item
            Component: invoke (1)
                invoke
                    invokeID: 4
                    opCode: localValue (0)
                        localValue: 24
                    CONSTRUCTOR
                        CONSTRUCTOR Tag
                        Tag: 0x00
                        Length: 21
                        Parameter (0x00)
                            Tag: 0x00
                            Length: 1
                        Data: 09
                        CONSTRUCTOR
                            CONSTRUCTOR Tag
                            Tag: 0x02
                            Length: 6
                            CONSTRUCTOR
                                CONSTRUCTOR Tag
                                Tag: 0x02
                                Length: 4
                                Parameter (0x00)
                                    Tag: 0x00
                                    Length: 2
                                Data: 80
                        CONSTRUCTOR
                            CONSTRUCTOR Tag
                            Tag: 0x02
                            Length: 3
                            Parameter (0x01)
                                Tag: 0x01
                                Length: 1
                            Data: 01
                        CONSTRUCTOR
                            CONSTRUCTOR Tag
                            Tag: 0x02
                            Length: 3
                            Parameter (0x00)
                                Tag: 0x00
                                Length: 1
                            Data: 00
Data (31 bytes)
0000  00 03 00 01 00 06 08 19 a6 25 f6 b3 00 00 08 00   .........%......
0010  45 02 01 08 75 85 00 00 fe 84 13 bd 0a 14 0d 05   E...u...........
0020  0a 14 11 01 0e 89 0e 89 77 8e d1 1a cb fe 35 ce   ........w.....5.
0030  00 03 00 70 14 a9 f5 de 00 02 54 7f 00 00 00 03   ...p......T.....
0040  01 00 01 01 00 00 00 60 02 10 00 58 00 00 03 ed   .......`...X....
0050  00 00 05 02 03 03 00 03 09 81 03 0e 19 0b 52 92   ..............R.
0060  00 12 04 58 26 90 00 30 23 0b 12 92 00 12 04 58   ...X&amp;..0#......X
0070  26 90 00 00 40 2a 65 28 48 04 03 f0 78 a6 49 04   &amp;[email protected]*e(H...x.I.
0080  06 fe 13 41 6c 1a a1 18 02 01 03 02 01 24 04 10   ...Al........$..
0090  a0 0e a0 03 81 01 01 a1 04 80 02 01 ea 82 01 00   ................
00a0  00 03 00 78 14 a9 f5 df 00 02 54 80 00 00 00 03   ...x......T.....
00b0  01 00 01 01 00 00 00 68 02 10 00 5d 00 00 03 ed   .......h...]....
00c0  00 00 05 02 03 03 00 03 09 81 03 0e 19 0b 52 92   ..............R.
00d0  00 12 04 58 26 90 00 30 23 0b 12 92 00 12 04 58   ...X&amp;..0#......X
00e0  26 90 00 00 40 2f 65 2d 48 04 03 f0 78 a6 49 04   &amp;[email protected]/e-H...x.I.
00f0  06 fe 13 41 6c 1f a1 1d 02 01 04 02 01 18 30 15   ...Al.........0.
0100  80 01 09 a2 06 a7 04 80 02 80 90 a3 03 81 01 01   ................
0110  a4 03 80 01 00 00 00 00                           ........</code></pre><p>Which parameter do i need to add to tshark command line for correct decode of all CAMEL messages?</p><p>Regards, Stanislav</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sctp" rel="tag" title="see questions tagged &#39;sctp&#39;">sctp</span> <span class="post-tag tag-link-decodeproblems" rel="tag" title="see questions tagged &#39;decodeproblems&#39;">decodeproblems</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-camel" rel="tag" title="see questions tagged &#39;camel&#39;">camel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 May '15, 04:41</strong></p><img src="https://secure.gravatar.com/avatar/48804bdf81a3d7958fff2e722728f827?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stanislav&#39;s gravatar image" /><p><span>Stanislav</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stanislav has no accepted answers">0%</span></p></div></div><div id="comments-container-42277" class="comments-container"></div><div id="comment-tools-42277" class="comment-tools"></div><div class="clear"></div><div id="comment-42277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

