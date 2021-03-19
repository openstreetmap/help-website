+++
type = "question"
title = "Large number of TCP RST"
description = '''I&#x27;m seeing a large number of tcp rst and am not quite sure what is causing it. I would appreciate any help. Below is that capture.  No. Time Source Destination Protocol Length Info 2939 2013-03-15 15:40:40.304765 10.1.4.2 208.89.168.x TCP 60 50090 &amp;gt; Frame 2939: 60 bytes on wire (480 bits), 60 byt...'''
date = "2013-03-19T10:03:00Z"
lastmod = "2013-03-19T13:55:00Z"
weight = 19653
keywords = [ "capture", "tcp" ]
aliases = [ "/questions/19653" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Large number of TCP RST](/questions/19653/large-number-of-tcp-rst)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19653-score" class="post-score" title="current number of votes">0</div><span id="post-19653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm seeing a large number of tcp rst and am not quite sure what is causing it. I would appreciate any help. Below is that capture.</p><pre><code>No. Time Source Destination Protocol Length Info
2939 2013-03-15 15:40:40.304765 10.1.4.2 208.89.168.x TCP 60 50090 &gt; Frame 2939: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
WTAP_ENCAP: 1
Arrival Time: Mar 15, 2013 15:40:40.304765000 Mountain Daylight Time
[Time shift for this packet: 0.000000000 seconds]
Epoch Time: 1363383640.304765000 seconds
[Time delta from previous captured frame: 0.000012000 seconds]
[Time delta from previous displayed frame: 0.000012000 seconds]
[Time since reference or first frame: 0.282367000 seconds]
Frame Number: 2939
Frame Length: 60 bytes (480 bits)
Capture Length: 60 bytes (480 bits)
[Frame is marked: False]
[Frame is ignored: False]
[Protocols in frame: eth:ip:tcp]
[Coloring Rule Name: TCP RST]
[Coloring Rule String: tcp.flags.reset eq 1]
Ethernet II, Src: Dell_0b:b3:6c (f0:4d:a2:0b:b3:6c), Dst: Dell_fd:78:06 (00:13:72:fd:78:06)
Destination: Dell_fd:78:06 (00:13:72:fd:78:06)
Address: Dell_fd:78:06 (00:13:72:fd:78:06)
.... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
.... ...0 .... .... .... .... = IG bit: Individual address (unicast)
Source: Dell_0b:b3:6c (f0:4d:a2:0b:b3:6c)
Address: Dell_0b:b3:6c (f0:4d:a2:0b:b3:6c)
.... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)
.... ...0 .... .... .... .... = IG bit: Individual address (unicast)
Type: IP (0x0800)
Padding: 000000000000
Internet Protocol Version 4, Src: 10.1.4.2 (10.1.4.2), Dst: 208.89.168.x (208.89.168.x)
Version: 4
Header length: 20 bytes
Differentiated Services Field: 0x00 (DSCP 0x00: Default; ECN: 0x00: Not-ECT (Not ECN-Capable Transport))
0000 00.. = Differentiated Services Codepoint: Default (0x00)
.... ..00 = Explicit Congestion Notification: Not-ECT (Not ECN-Capable Transport) (0x00)
Total Length: 40
Identification: 0x0000 (0)
Flags: 0x02 (Don&#39;t Fragment)
0... .... = Reserved bit: Not set
.1.. .... = Don&#39;t fragment: Set
..0. .... = More fragments: Not set
Fragment offset: 0
Time to live: 64
Protocol: TCP (6)
Header checksum: 0x3a76 [correct]
[Good: True]
[Bad: False]
Source: 10.1.4.2 (10.1.4.2)
Destination: 208.89.168.x (208.89.168.x)
[Source GeoIP: Unknown]
[Destination GeoIP: Unknown]
Transmission Control Protocol, Src Port: 50090 (50090), Dst Port: https (443), Seq: 608, Len: 0
Source port: 50090 (50090)
Destination port: https (443)
[Stream index: 49]
Sequence number: 608 (relative sequence number)
Header length: 20 bytes
Flags: 0x004 (RST)
000. .... .... = Reserved: Not set
...0 .... .... = Nonce: Not set
.... 0... .... = Congestion Window Reduced (CWR): Not set
.... .0.. .... = ECN-Echo: Not set
.... ..0. .... = Urgent: Not set
.... ...0 .... = Acknowledgment:</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '13, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/3145e241ad278a3681f33febe8608149?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mp84057&#39;s gravatar image" /><p><span>mp84057</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mp84057 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Mar '13, 10:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-19653" class="comments-container"><span id="19661"></span><div id="comment-19661" class="comment"><div id="post-19661-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'm seeing a large number of tcp rst and am not quite sure what is causing it.</p></blockquote><p>with only a single packet, it's hard to give any meaningful answer. You say a "large numver" of tcp reset. Here are some questions:</p><ul><li>what exactly is a "large number"?</li><li>are those packets all from the same IP?</li><li>who sends the first reset? client or server?</li></ul></div><div id="comment-19661-info" class="comment-info"><span class="comment-age">(19 Mar '13, 13:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-19653" class="comment-tools"></div><div class="clear"></div><div id="comment-19653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19656"></span>

<div id="answer-container-19656" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19656-score" class="post-score" title="current number of votes">1</div><span id="post-19656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With my little experience with load balancers i can think of these reasons for cause of RSTs</p><p>1)Max-connection limit reached on load balancer.</p><p>2)Real Server/Application is down.</p><p>3)May be 80 is handled by one load balancer and 443 by other load balancer breaking the session persistence which will trigger resets.</p><p>If My answer sounds vague so is the question.</p><p>Point is , please be informative with your question.The packet capture you provided won't help much in analyzing the situation(atleast for me).Please try to get the information from client side-Network Side and Server side traces for other experts to analyze.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '13, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Mar '13, 11:47</strong> </span></p></div></div><div id="comments-container-19656" class="comments-container"><span id="19658"></span><div id="comment-19658" class="comment"><div id="post-19658-score" class="comment-score"></div><div class="comment-text"><p>I also believe that it has something to do with our load balancer configuration. The following is the current setup of our load balancer:</p><p>Prod_Insecure 10.1.1.3 81 (Layer 4)<br />
Prod_Redirect_To_Secure 10.1.1.3 80 (HTTP)(Layer 4)<br />
Prod_Secure 10.1.1.3 443 Standard<br />
Public_Insecure 10.1.1.4 81 (Layer 4)<br />
Public_Redirect_To_Secure 10.1.1.4 80 (Layer 4)<br />
Public_Secure 10.1.1.4 443 Standard</p></div><div id="comment-19658-info" class="comment-info"><span class="comment-age">(19 Mar '13, 12:06)</span> <span class="comment-user userinfo">mp84057</span></div></div></div><div id="comment-tools-19656" class="comment-tools"></div><div class="clear"></div><div id="comment-19656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

