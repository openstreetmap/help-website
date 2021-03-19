+++
type = "question"
title = "Understanding SIP/SDP file in context of Opus codec. Cannot decode opus ."
description = '''This pcap file in cloudshark was captured during a voip mobile app (audio) conversation. https://www.cloudshark.org/captures/8fef0eaa85f4 As we can see, Opus is used as codec. In wireshark, I analyzed the RTP stream, saved as raw file. Then I downloaded opus encode/decoder tool from : http://www.opu...'''
date = "2015-05-13T07:47:00Z"
lastmod = "2015-05-15T02:16:00Z"
weight = 42367
keywords = [ "codec", "rtp", "decode_rtp", "decoder" ]
aliases = [ "/questions/42367" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Understanding SIP/SDP file in context of Opus codec. Cannot decode opus .](/questions/42367/understanding-sipsdp-file-in-context-of-opus-codec-cannot-decode-opus)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42367-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This pcap file in cloudshark was captured during a voip mobile app (audio) conversation. <a href="https://www.cloudshark.org/captures/8fef0eaa85f4">https://www.cloudshark.org/captures/8fef0eaa85f4</a></p><p>As we can see, Opus is used as codec. In wireshark, I analyzed the RTP stream, saved as raw file.</p><p>Then I downloaded opus encode/decoder tool from : <a href="http://www.opus-codec.org/downloads/">http://www.opus-codec.org/downloads/</a></p><p>I encoded the raw file as : "encode.exe --bitrate 16 --raw myrawfile.raw output.opus"</p><p>Then Tried to play opus file in audacity. What I can get is only the noise. I tried by decoding the opus file into wav and play again. Still no luck.</p><p>Could you please suggest me where have I gone wrong ?</p></div><div id="question-tags" class="tags-container tags">codec rtp decode_rtp decoder</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '15, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/4ec917e3556fb6d9c03cc0e39ec7732a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shas&#39;s gravatar image" /><p>Shas<br />
<span class="score" title="1 reputation points">1</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shas has no accepted answers">0%</span></p></div></div><div id="comments-container-42367" class="comments-container"></div><div id="comment-tools-42367" class="comment-tools"></div><div class="clear"></div><div id="comment-42367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42410"></span>

<div id="answer-container-42410" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42410-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You want to go the other way, decode from opus to wav.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '15, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-42410" class="comments-container"><span id="42474"></span><div id="comment-42474" class="comment"><div id="post-42474-score" class="comment-score"></div><div class="comment-text"><p>@Jaap, wireshark doesnt allow saving .opus, does it ? To decode it we need to have .opus file at first. That is the problem, we dont have ,opus file, we have only raw file. Thanks</p></div><div id="comment-42474-info" class="comment-info"><span class="comment-age">(17 May '15, 19:32)</span> Shas</div></div><span id="42487"></span><div id="comment-42487" class="comment"><div id="post-42487-score" class="comment-score"></div><div class="comment-text"><p>Raw != WAV. Raw is the binary data in the RTP packets.</p><p>The binary data in the RTP packets is Opus encoded sound. Therefore you need to decode the opus encoded data in WAV encoded data.</p></div><div id="comment-42487-info" class="comment-info"><span class="comment-age">(17 May '15, 23:04)</span> Jaap ♦</div></div><span id="42853"></span><div id="comment-42853" class="comment"><div id="post-42853-score" class="comment-score"></div><div class="comment-text"><p>@Jaap, Thanks for the comment. I couldnt be quiet clear. Yes, I have raw file (already opus encoded), need to make it wav file. but opus decoder takes only .opus file as input to decode and create wav file. Here is the problem, how do we feed raw (opus encoded) but not recognized by opus decoder as opus file in the decoder. Appreciated</p></div><div id="comment-42853-info" class="comment-info"><span class="comment-age">(03 Jun '15, 09:06)</span> Shas</div></div><span id="48036"></span><div id="comment-48036" class="comment"><div id="post-48036-score" class="comment-score"></div><div class="comment-text"><p>The problem with extracting the raw Opus stream is that it is a variable bit rate (VBR) codec. The extracted data needs to be written with some sort of framing such as Ogg or Matroska so the player knows where one frame ends and the next begins.</p></div><div id="comment-48036-info" class="comment-info"><span class="comment-age">(27 Nov '15, 16:36)</span> kjotte</div></div><span id="48038"></span><div id="comment-48038" class="comment"><div id="post-48038-score" class="comment-score"></div><div class="comment-text"><p>Indeed. And so opening a whole new can-o-worms.</p></div><div id="comment-48038-info" class="comment-info"><span class="comment-age">(27 Nov '15, 20:41)</span> Jaap ♦</div></div><span id="48046"></span><div id="comment-48046" class="comment not_top_scorer"><div id="post-48046-score" class="comment-score"></div><div class="comment-text"><p>@Shas,</p><p>look <a href="https://tools.ietf.org/html/rfc6716#section-3">here</a>. In short, by extracting the RTP payload from the RTP packets into a continuous stream of bytes, you strip information which the opus decoder needs. As @kjotte wrote, the decoder needs to know where the individual Opus packets (which are not the same as IP packets) begin and end, as they do not contain such information inside themselves and as their size is variable.</p><p>The opusdec from the Opus tools can only extract the Opus packets from an ogg file structure which provides, if we limit ourselves to aspects important for Opus, the same service like RTP: encapsulation of the Opus packets into a transport layer which indicates where they begin and end and also includes means to obtain this information also if part of the data gets lost in transport.</p><p>So you have three possibilities:</p><ul><li><p>to file an "enhancement" category bug (= wish) at <a href="https://bugs.wireshark.org/bugzilla/">Wireshark Bugzilla</a>, asking for integration of Opus decoder into Wireshark</p></li><li><p>to ask people at Opus to add support for pcap (pcapng) input files (i.e. Opus packets encapsulated into RTP packets stored in pcap or pcapng formatted file, which you could easily create by using File -&gt; Export Specified Packets in Wireshark after applying a corresponding display filter or by using the same display filter for tshark with -w option)</p></li><li><p>to write "something" yourself, where the "something" may be an application (script) written using your favourite programming language which would read the pcap(ng) file as above, extract the opus packets from it and save them using the <a href="https://tools.ietf.org/html/rfc3533">ogg encapsulation</a>, or (if you speak C), the pcap(ng) parser as an extension for the opusdec tool as mentioned above. As also other software than the opusdec can decode ogg-encapsulated Opus streams, the converter application may make sense even if you speak C.</p></li></ul></div><div id="comment-48046-info" class="comment-info"><span class="comment-age">(28 Nov '15, 11:18)</span> sindy</div></div><span id="48062"></span><div id="comment-48062" class="comment not_top_scorer"><div id="post-48062-score" class="comment-score"></div><div class="comment-text"><p>Hm, as there are many possible "link type" encapsulations, you'd need half of Wireshark code to properly parse a pcap(ng) file to reach the packet fields you need. So better to use<br />
<code>tshark.exe -r opus_reverse.pcap -T fields -e rtp.timestamp -e rtp.payload -d udp.port==10758,rtp -E separator=;</code> and use the output line by line to create an .opus (actually, ogg) file. The result of such processing then looks like this: <a href="https://drive.google.com/file/d/0B1ygoNuxMOQqVkVoVW84WURPZ1U/view?usp=sharing">forward direction</a> and <a href="https://drive.google.com/file/d/0B1ygoNuxMOQqVG5rUU5KWVRUbW8/view?usp=sharing">reverse direction</a>.</p></div><div id="comment-48062-info" class="comment-info"><span class="comment-age">(29 Nov '15, 13:02)</span> sindy</div></div></div><div id="comment-tools-42410" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-42410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

