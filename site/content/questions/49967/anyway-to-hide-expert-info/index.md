+++
type = "question"
title = "Anyway to hide expert info"
description = '''I am trying to parse XMPP messages. Looks like some attribute/elements are unknown. For each this attribute/element, there is &quot;expert info&quot; next to it. It is kind of annoying and make hard to read the packet info. Following is a screen capture.  Is there any way to remove expert info from the displa...'''
date = "2016-02-08T07:38:00Z"
lastmod = "2016-02-12T06:56:00Z"
weight = 49967
keywords = [ "expert" ]
aliases = [ "/questions/49967" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Anyway to hide expert info](/questions/49967/anyway-to-hide-expert-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49967-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to parse XMPP messages. Looks like some attribute/elements are unknown. For each this attribute/element, there is "expert info" next to it. It is kind of annoying and make hard to read the packet info. Following is a screen capture.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2016-02-08_at_2.17.47_PM.png" alt="alt text" /></p><p>Is there any way to remove expert info from the display window?</p></div><div id="question-tags" class="tags-container tags">expert</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '16, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/b7590de43adb375f2d9c6ba1f98b72cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yacare&#39;s gravatar image" /><p>yacare<br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yacare has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 08 Feb '16, 11:23</p></div></div><div id="comments-container-49967" class="comments-container"></div><div id="comment-tools-49967" class="comment-tools"></div><div class="clear"></div><div id="comment-49967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="49979"></span>

<div id="answer-container-49979" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49979-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, there's no way to do that (short of modifying Wireshark's source code).</p><p>Can I ask why you'd want to?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Feb '16, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-49979" class="comments-container"><span id="49981"></span><div id="comment-49981" class="comment"><div id="post-49981-score" class="comment-score"></div><div class="comment-text"><p>Just updated my question above.</p></div><div id="comment-49981-info" class="comment-info"><span class="comment-age">(08 Feb '16, 11:24)</span> yacare</div></div><span id="49982"></span><div id="comment-49982" class="comment"><div id="post-49982-score" class="comment-score"></div><div class="comment-text"><p>In that case, and assuming that the highlighted fields actually are valid XMPP, I'd suggest opening an <a href="https://bugs.wireshark.org">enhancement request</a> (with a sample capture) asking Wireshark to correctly decode those fields (that is, make Wireshark understand them/decode them so it stops noting that it didn't understand/decode them).</p></div><div id="comment-49982-info" class="comment-info"><span class="comment-age">(08 Feb '16, 11:29)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-49979" class="comment-tools"></div><div class="clear"></div><div id="comment-49979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50144"></span>

<div id="answer-container-50144" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50144-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To answer my question, expert info will not be shown when wireshark runs in command line with tshark.</p><pre><code>Frame 4045: 971 bytes on wire (7768 bits), 971 bytes captured (7768 bits)
Ethernet II, Src: f0:1c:2d:43:ee:27 (f0:1c:2d:43:ee:27), Dst: 5c:b9:01:8b:6f:3c (5c:b9:01:8b:6f:3c)
Internet Protocol Version 4, Src: 172.222.19.203 (172.222.19.203), Dst: 172.222.76.4 (172.222.76.4)
Transmission Control Protocol, Src Port: xmpp-server (5269), Dst Port: 40897 (40897), Seq: 34670, Ack: 18449, Len: 905
[2 Reassembled TCP Segments (2353 bytes): #4043(1448), #4045(905)]
XMPP Protocol
    XML HEADER VER. 1.0
    MESSAGE []
        from: [email protected]
        to: compute4/bgp-peer
        EVENT [xmlns=&quot;http://jabber.org/protocol/pubsub&quot;]
            xmlns: http://jabber.org/protocol/pubsub
            ITEMS [node=&quot;1/1/default-domain:admin:VRF_TEST:VRF_TEST&quot;]
                node: 1/1/default-domain:admin:VRF_TEST:VRF_TEST
                ITEM [id=&quot;1.2.3.6/32&quot;]
                    id: 1.2.3.6/32</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '16, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/b7590de43adb375f2d9c6ba1f98b72cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yacare&#39;s gravatar image" /><p>yacare<br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yacare has no accepted answers">0%</span></p></div></div><div id="comments-container-50144" class="comments-container"><span id="50150"></span><div id="comment-50150" class="comment"><div id="post-50150-score" class="comment-score"></div><div class="comment-text"><p>Odd... That actually sounds like a bug to me. Does it behave differently if you give the "-2" or "-Y"/"-R" options?</p></div><div id="comment-50150-info" class="comment-info"><span class="comment-age">(12 Feb '16, 07:25)</span> JeffMorriss ♦</div></div><span id="50152"></span><div id="comment-50152" class="comment"><div id="post-50152-score" class="comment-score"></div><div class="comment-text"><p>Please don't fix it if it is indeed a bug. :)</p><p>Here is what I used.</p><p>tshark -X lua_script:xmpp.lua -r vhost0.pcap -O xmpp -Y "tcp.port==5269"</p><p>I don't see any difference with -2 option.</p><p>tshark -X lua_script:xmpp.lua -r vhost0.pcap -O xmpp -Y "tcp.port==5269" -2</p></div><div id="comment-50152-info" class="comment-info"><span class="comment-age">(12 Feb '16, 07:31)</span> yacare</div></div></div><div id="comment-tools-50144" class="comment-tools"></div><div class="clear"></div><div id="comment-50144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

