+++
type = "question"
title = "Receiver limits TCP window size to 64,512"
description = '''Facts (please identify any false statements):   I have a 100 Mbps connection between two sites that are 80 ms apart   This is a long fat connection that could benefit from a large TCP window size perhaps up to 100 Mbps * 0.08 sec = 1,000,000 bytes   Both machines are running Windows Server 2012. &quot;Re...'''
date = "2015-06-12T12:58:00Z"
lastmod = "2015-06-19T06:27:00Z"
weight = 43102
keywords = [ "tcpwindowsize" ]
aliases = [ "/questions/43102" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Receiver limits TCP window size to 64,512](/questions/43102/receiver-limits-tcp-window-size-to-64512)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43102-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43102-score" class="post-score" title="current number of votes">0</div><span id="post-43102-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong>Facts</strong> (please identify any false statements):</p><ol><li><p>I have a 100 Mbps connection between two sites that are 80 ms apart</p></li><li><p>This is a long fat connection that could benefit from a large TCP window size perhaps up to 100 Mbps * 0.08 sec = 1,000,000 bytes</p></li><li><p>Both machines are running Windows Server 2012. "Receive window auto tuning level" is normal on both. "Window scaling heuristics" are disabled on both.</p></li><li><p>I ran "iperf -s" on one side and "iperf -c" on the other. The transfer happened at 5 Mbps. I get the same result going the other direction.</p></li><li><p>Both sides advertised support for TCP sliding windows in their SYNs.</p></li><li><p>The receiver requested a TCP window size of 64,512 bytes (0xFC00) during the entire run with a TCP window scale value of "no shift" (0x000).</p></li><li><p>The network was able to handle a larger window size (see sequence diagrams below)</p></li><li><p>The receiver kept the window smaller than the network supports</p></li><li><p>This connection is happening within an IPSEC VPN. MTU of the tunnel interface is reduced to 1400 bytes in both directions.</p></li></ol><p><strong>Question</strong></p><p>Why is the receiver keeping the window small?</p><hr /><p><strong>Sender TCP Settings</strong></p><pre><code>PS C:\Users\acs&gt; netsh interface tcp show global
Querying active state...

TCP Global Parameters
----------------------------------------------
Receive-Side Scaling State          : enabled
Chimney Offload State               : disabled
NetDMA State                        : disabled
Direct Cache Access (DCA)           : disabled
Receive Window Auto-Tuning Level    : normal
Add-On Congestion Control Provider  : none
ECN Capability                      : enabled
RFC 1323 Timestamps                 : disabled
Initial RTO                         : 3000
Receive Segment Coalescing State    : enabled

PS C:\Users\acs&gt; netsh interface tcp show heuristics
TCP Window Scaling heuristics Parameters
----------------------------------------------
Window Scaling heuristics         : disabled
Qualifying Destination Threshold  : 3
Profile type unknown              : normal
Profile type public               : normal
Profile type private              : normal
Profile type domain               : normal

PS C:\Users\acs&gt; Get-NetTCPSetting

SettingName                   : Automatic
MinRto(ms)                    : 
InitialCongestionWindow(MSS)  : 
CongestionProvider            : 
CwndRestart                   : 
DelayedAckTimeout(ms)         : 
MemoryPressureProtection      : 
AutoTuningLevelLocal          : 
AutoTuningLevelGroupPolicy    : 
AutoTuningLevelEffective      : 
EcnCapability                 : 
Timestamps                    : 
InitialRto(ms)                : 
ScalingHeuristics             : 
DynamicPortRangeStartPort     : 
DynamicPortRangeNumberOfPorts :

SettingName                   : Custom
MinRto(ms)                    : 20
InitialCongestionWindow(MSS)  : 4
CongestionProvider            : DCTCP
CwndRestart                   : True
DelayedAckTimeout(ms)         : 10
MemoryPressureProtection      : Enabled
AutoTuningLevelLocal          : Normal
AutoTuningLevelGroupPolicy    : NotConfigured
AutoTuningLevelEffective      : Local
EcnCapability                 : Enabled
Timestamps                    : Disabled
InitialRto(ms)                : 3000
ScalingHeuristics             : Disabled
DynamicPortRangeStartPort     : 49152
DynamicPortRangeNumberOfPorts : 16384

SettingName                   : Compat
MinRto(ms)                    : 300
InitialCongestionWindow(MSS)  : 2
CongestionProvider            : Default
CwndRestart                   : False
DelayedAckTimeout(ms)         : 200
MemoryPressureProtection      : Enabled
AutoTuningLevelLocal          : Normal
AutoTuningLevelGroupPolicy    : NotConfigured
AutoTuningLevelEffective      : Local
EcnCapability                 : Enabled
Timestamps                    : Disabled
InitialRto(ms)                : 3000
ScalingHeuristics             : Disabled
DynamicPortRangeStartPort     : 49152
DynamicPortRangeNumberOfPorts : 16384

SettingName                   : Datacenter
MinRto(ms)                    : 20
InitialCongestionWindow(MSS)  : 4
CongestionProvider            : DCTCP
CwndRestart                   : True
DelayedAckTimeout(ms)         : 10
MemoryPressureProtection      : Enabled
AutoTuningLevelLocal          : Normal
AutoTuningLevelGroupPolicy    : NotConfigured
AutoTuningLevelEffective      : Local
EcnCapability                 : Enabled
Timestamps                    : Disabled
InitialRto(ms)                : 3000
ScalingHeuristics             : Disabled
DynamicPortRangeStartPort     : 49152
DynamicPortRangeNumberOfPorts : 16384

SettingName                   : Internet
MinRto(ms)                    : 300
InitialCongestionWindow(MSS)  : 4
CongestionProvider            : CTCP
CwndRestart                   : False
DelayedAckTimeout(ms)         : 50
MemoryPressureProtection      : Enabled
AutoTuningLevelLocal          : Normal
AutoTuningLevelGroupPolicy    : NotConfigured
AutoTuningLevelEffective      : Local
EcnCapability                 : Enabled
Timestamps                    : Disabled
InitialRto(ms)                : 3000
ScalingHeuristics             : Disabled
DynamicPortRangeStartPort     : 49152
DynamicPortRangeNumberOfPorts : 16384</code></pre><p><strong>Sender SYN</strong></p><pre><code>No.     Time           Source                Destination           Protocol Length Delta      Sequence number Acknowledgment number Bytes in flight Calculated window size Info
    814 5.036577000    10.10.0.21            10.11.0.1             TCP      66     0.000000000 0               0                                     64512                  49758→5001 [SYN, ECN, CWR] Seq=0 Win=64512 Len=0 MSS=1460 WS=1 SACK_PERM=1

Frame 814: 66 bytes on wire (528 bits), 66 bytes captured (528 bits) on interface 0
Ethernet II, Src: 00:11:22:33:44:55, Dst: aa:bb:cc:dd:ee:ff
Internet Protocol Version 4, Src: 10.10.0.21 (10.10.0.21), Dst: 10.11.0.1 (10.11.0.1)
Transmission Control Protocol, Src Port: 49758 (49758), Dst Port: 5001 (5001), Seq: 0, Len: 0
    Source Port: 49758 (49758)
    Destination Port: 5001 (5001)
    [Stream index: 73]
    [TCP Segment Len: 0]
    Sequence number: 0    (relative sequence number)
    Acknowledgment number: 0
    Header Length: 32 bytes
    .... 0000 1100 0010 = Flags: 0x0c2 (SYN, ECN, CWR)
    Window size value: 64512
    [Calculated window size: 64512]
    Checksum: 0x1451 [validation disabled]
    Urgent pointer: 0
    Options: (12 bytes), Maximum segment size, No-Operation (NOP), Window scale, No-Operation (NOP), No-Operation (NOP), SACK permitted
        Maximum segment size: 1460 bytes
        No-Operation (NOP)
        Window scale: 0 (multiply by 1)
            Kind: Window Scale (3)
            Length: 3
            Shift count: 0
            [Multiplier: 1]
        No-Operation (NOP)
        No-Operation (NOP)
        TCP SACK Permitted Option: True</code></pre><p><strong>Sender perspective of sequence graph</strong></p><p><a href="https://www.stankevitz.com/images/sender-seq.png">Sequence graph</a></p><hr /><p><strong>Receiver TCP Settings</strong></p><pre><code>PS C:\Users\acs&gt; netsh interface tcp show global
Querying active state...

TCP Global Parameters
----------------------------------------------
Receive-Side Scaling State          : enabled
Chimney Offload State               : disabled
NetDMA State                        : disabled
Direct Cache Access (DCA)           : disabled
Receive Window Auto-Tuning Level    : normal
Add-On Congestion Control Provider  : none
ECN Capability                      : enabled
RFC 1323 Timestamps                 : disabled
Initial RTO                         : 3000
Receive Segment Coalescing State    : enabled

PS C:\Users\acs&gt; netsh interface tcp show heuristics
TCP Window Scaling heuristics Parameters
----------------------------------------------
Window Scaling heuristics         : disabled
Qualifying Destination Threshold  : 3
Profile type unknown              : normal
Profile type public               : normal
Profile type private              : normal
Profile type domain               : normal

PS C:\Users\acs&gt; Get-NetTCPSetting

SettingName                   : Automatic
MinRto(ms)                    : 
InitialCongestionWindow(MSS)  : 
CongestionProvider            : 
CwndRestart                   : 
DelayedAckTimeout(ms)         : 
MemoryPressureProtection      : 
AutoTuningLevelLocal          : 
AutoTuningLevelGroupPolicy    : 
AutoTuningLevelEffective      : 
EcnCapability                 : 
Timestamps                    : 
InitialRto(ms)                : 
ScalingHeuristics             : 
DynamicPortRangeStartPort     : 
DynamicPortRangeNumberOfPorts :

SettingName                   : Custom
MinRto(ms)                    : 20
InitialCongestionWindow(MSS)  : 4
CongestionProvider            : DCTCP
CwndRestart                   : True
DelayedAckTimeout(ms)         : 10
MemoryPressureProtection      : Enabled
AutoTuningLevelLocal          : Normal
AutoTuningLevelGroupPolicy    : NotConfigured
AutoTuningLevelEffective      : Local
EcnCapability                 : Enabled
Timestamps                    : Disabled
InitialRto(ms)                : 3000
ScalingHeuristics             : Disabled
DynamicPortRangeStartPort     : 49152
DynamicPortRangeNumberOfPorts : 16384

SettingName                   : Compat
MinRto(ms)                    : 300
InitialCongestionWindow(MSS)  : 2
CongestionProvider            : Default
CwndRestart                   : False
DelayedAckTimeout(ms)         : 200
MemoryPressureProtection      : Enabled
AutoTuningLevelLocal          : Normal
AutoTuningLevelGroupPolicy    : NotConfigured
AutoTuningLevelEffective      : Local
EcnCapability                 : Enabled
Timestamps                    : Disabled
InitialRto(ms)                : 3000
ScalingHeuristics             : Disabled
DynamicPortRangeStartPort     : 49152
DynamicPortRangeNumberOfPorts : 16384

SettingName                   : Datacenter
MinRto(ms)                    : 20
InitialCongestionWindow(MSS)  : 4
CongestionProvider            : DCTCP
CwndRestart                   : True
DelayedAckTimeout(ms)         : 10
MemoryPressureProtection      : Enabled
AutoTuningLevelLocal          : Normal
AutoTuningLevelGroupPolicy    : NotConfigured
AutoTuningLevelEffective      : Local
EcnCapability                 : Enabled
Timestamps                    : Disabled
InitialRto(ms)                : 3000
ScalingHeuristics             : Disabled
DynamicPortRangeStartPort     : 49152
DynamicPortRangeNumberOfPorts : 16384

SettingName                   : Internet
MinRto(ms)                    : 300
InitialCongestionWindow(MSS)  : 4
CongestionProvider            : CTCP
CwndRestart                   : False
DelayedAckTimeout(ms)         : 50
MemoryPressureProtection      : Enabled
AutoTuningLevelLocal          : Normal
AutoTuningLevelGroupPolicy    : NotConfigured
AutoTuningLevelEffective      : Local
EcnCapability                 : Enabled
Timestamps                    : Disabled
InitialRto(ms)                : 3000
ScalingHeuristics             : Disabled
DynamicPortRangeStartPort     : 49152
DynamicPortRangeNumberOfPorts : 16384</code></pre><p><strong>Receiver SYN</strong></p><pre><code>No.     Time           Source                Destination           Protocol Length Delta      Sequence number Acknowledgment number Bytes in flight Calculated window size Info
    817 5.110501000    10.11.0.1             10.10.0.21            TCP      70     0.073924000 0               1                                     64512                  5001→49758 [SYN, ACK, ECN] Seq=0 Ack=1 Win=64512 Len=0 MSS=1460 WS=1 SACK_PERM=1 [ETHERNET FRAME CHECK SEQUENCE INCORRECT]

Frame 817: 70 bytes on wire (560 bits), 70 bytes captured (560 bits) on interface 0
Ethernet II, Src: aa:bb:cc:dd:ee:ff, Dst: 00:11:22:33:44:55
Internet Protocol Version 4, Src: 10.11.0.1 (10.11.0.1), Dst: 10.10.0.21 (10.10.0.21)
Transmission Control Protocol, Src Port: 5001 (5001), Dst Port: 49758 (49758), Seq: 0, Ack: 1, Len: 0
    Source Port: 5001 (5001)
    Destination Port: 49758 (49758)
    [Stream index: 73]
    [TCP Segment Len: 0]
    Sequence number: 0    (relative sequence number)
    Acknowledgment number: 1    (relative ack number)
    Header Length: 32 bytes
    .... 0000 0101 0010 = Flags: 0x052 (SYN, ACK, ECN)
    Window size value: 64512
    [Calculated window size: 64512]
    Checksum: 0xb5bb [validation disabled]
    Urgent pointer: 0
    Options: (12 bytes), Maximum segment size, No-Operation (NOP), Window scale, No-Operation (NOP), No-Operation (NOP), SACK permitted
        Maximum segment size: 1460 bytes
        No-Operation (NOP)
        Window scale: 0 (multiply by 1)
            Kind: Window Scale (3)
            Length: 3
            Shift count: 0
            [Multiplier: 1]
        No-Operation (NOP)
        No-Operation (NOP)
        TCP SACK Permitted Option: True
    [SEQ/ACK analysis]</code></pre><p><strong>Receiver perspective of sequence graph</strong></p><p><a href="https://www.stankevitz.com/images/receiver-seq.png">Sequence graph</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpwindowsize" rel="tag" title="see questions tagged &#39;tcpwindowsize&#39;">tcpwindowsize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '15, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/9d84a3bc6c2a9a6dfd97b3a17252e0be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chrisstankevitz&#39;s gravatar image" /><p><span>chrisstankevitz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chrisstankevitz has no accepted answers">0%</span></p></div></div><div id="comments-container-43102" class="comments-container"><span id="43106"></span><div id="comment-43106" class="comment"><div id="post-43106-score" class="comment-score"></div><div class="comment-text"><p>Have you ever tried to disable the autotuning level?</p></div><div id="comment-43106-info" class="comment-info"><span class="comment-age">(12 Jun '15, 14:14)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="43110"></span><div id="comment-43110" class="comment"><div id="post-43110-score" class="comment-score"></div><div class="comment-text"><p>My question would be: did you ever see the window size being a problem? Meaning: did the trace show symptoms at any point in time that the sender had to actually wait for an ACK before it continue to send? You should see things like "Window Full" etc. if that happens, plus long delta times before continuing to send.</p></div><div id="comment-43110-info" class="comment-info"><span class="comment-age">(12 Jun '15, 15:16)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="43189"></span><div id="comment-43189" class="comment"><div id="post-43189-score" class="comment-score"></div><div class="comment-text"><p><span>@Christian_R</span>: No, my autotuning is enabled. Are you suggesting that disabling autotuning will "solve" my problem? Or are you concerned that I inadvertently disabled autotuning and that is why I am having a problem? I believe "disable autotuning" causes the receive window to be stuck at some fixed value, which is not what I'm after.</p></div><div id="comment-43189-info" class="comment-info"><span class="comment-age">(15 Jun '15, 09:08)</span> <span class="comment-user userinfo">chrisstankevitz</span></div></div><span id="43190"></span><div id="comment-43190" class="comment"><div id="post-43190-score" class="comment-score"></div><div class="comment-text"><p><span>@Jasper</span>: Thank you. You are correct, no "window full". I now believe the question is "When one is not specified, why isn't Windows Server 2012 dynamically increasing SO_SNDBUF/SO_RCVBUF to accommodate long fat pipes as described at <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/bb736549(v=vs.85).aspx">MSDN</a>?"</p></div><div id="comment-43190-info" class="comment-info"><span class="comment-age">(15 Jun '15, 09:12)</span> <span class="comment-user userinfo">chrisstankevitz</span></div></div><span id="43191"></span><div id="comment-43191" class="comment"><div id="post-43191-score" class="comment-score"></div><div class="comment-text"><p>Wouldn't setting the buffer sizes be an application issue?</p></div><div id="comment-43191-info" class="comment-info"><span class="comment-age">(15 Jun '15, 09:44)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43197"></span><div id="comment-43197" class="comment not_top_scorer"><div id="post-43197-score" class="comment-score"></div><div class="comment-text"><p>@christiankevitz: Easily said I just were interested if you tried it. I never tried, because of the same reason as you.</p><p>I have a side question out of topic, just for interest the questions really have nothing to do with the window size: Do you use nlb? Do you have a lot of multicasts/broadcast at the servers? Are the systems physical or virtualized?</p></div><div id="comment-43197-info" class="comment-info"><span class="comment-age">(15 Jun '15, 15:19)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="43199"></span><div id="comment-43199" class="comment not_top_scorer"><div id="post-43199-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span>: indeed setting buffer sizes is an application issue. In this particular case, the application is not setting a buffer size... in which case I'm expecting Windows to dynamically increase the buffer sizes as needed per the MSDN link posted above. But apparently that is not happening and I'm trying to figure out why.</p></div><div id="comment-43199-info" class="comment-info"><span class="comment-age">(16 Jun '15, 01:14)</span> <span class="comment-user userinfo">chrisstankevitz</span></div></div><span id="43367"></span><div id="comment-43367" class="comment not_top_scorer"><div id="post-43367-score" class="comment-score"></div><div class="comment-text"><p>Did you have any more joy with this? I also have a window size limited to this value despite setting larger buffer sizes. While its not a problem, as <span>@Jasper</span> pointed out, with the window getting full, I do believe it can limit the maximum congestion window size, which may be more of an issue. (And we do often have to wait for ACKs before it continues to send)</p></div><div id="comment-43367-info" class="comment-info"><span class="comment-age">(19 Jun '15, 06:27)</span> <span class="comment-user userinfo">glyn_walters</span></div></div></div><div id="comment-tools-43102" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-43102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

