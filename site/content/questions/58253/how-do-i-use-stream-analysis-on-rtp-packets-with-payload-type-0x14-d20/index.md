+++
type = "question"
title = "How do I use &quot;Stream Analysis&quot; on RTP packets with payload type 0x14 (d&#x27;20)"
description = '''The payload type is custom (using PT=20) and defined as: PayloadType payload_type_pcm8000 = TYPE( PAYLOAD_AUDIO_CONTINUOUS), CLOCK_RATE(8000), BITS_PER_SAMPLE(16), ZERO_PATTERN( offset0), PATTERN_LENGTH(1), NORMAL_BITRATE( 128000), MIME_TYPE (&quot;PCM&quot;), CHANNELS(1)  I cannot play the audio directly in ...'''
date = "2016-12-20T04:53:00Z"
lastmod = "2016-12-20T04:53:00Z"
weight = 58253
keywords = [ "traffic-analysis", "decode_rtp", "rtp.payload" ]
aliases = [ "/questions/58253" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I use "Stream Analysis" on RTP packets with payload type 0x14 (d'20)](/questions/58253/how-do-i-use-stream-analysis-on-rtp-packets-with-payload-type-0x14-d20)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58253-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The payload type is custom (using PT=20) and defined as:</p><pre><code>PayloadType payload_type_pcm8000 =
TYPE( PAYLOAD_AUDIO_CONTINUOUS),
CLOCK_RATE(8000),
BITS_PER_SAMPLE(16),
ZERO_PATTERN( offset0),
PATTERN_LENGTH(1),
NORMAL_BITRATE( 128000),
MIME_TYPE (&quot;PCM&quot;),
CHANNELS(1)</code></pre><p>I cannot play the audio directly in Wireshark and neither get any analysis of the data in regards of jitter for example. I can save the stream as .raw data from Wireshark and then import this file in AudaCity (for example) as signed 16 bit PCM at 8000 samples / second. And here I can listen to the audio file. However this does not reflect the delay on the network and results in a perfect sound listening on the receiver side I have a "fuzzy" sound.</p><p>To be able to analyze this behavior I was hopping to analyze the network traffic to tell if the sound is distorted on the transmitter or receiver side. Can I tell Wireshark what I'm expecting in the payload for this data type or is there any other good way on how I can analyze RTP data.</p><hr /><p>The test setup is:</p><pre><code>| Transmitter | ---&gt; | Mirroring switch | ---&gt; | Receiver |
                               ↓
                  | Computer with Wireshark |</code></pre><p>I have access to the source code on the receiver and can change this if I needed, but I cannot control the transmitter side (at least not directly). The return audio is clear and good (using the same protocol and network interface).</p><p>edit: Wireshark version: Version 2.2.3 (v2.2.3-0-g57531cd)</p></div><div id="question-tags" class="tags-container tags">traffic-analysis decode_rtp rtp.payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '16, 04:53</strong></p><img src="https://secure.gravatar.com/avatar/e6525a6a33d3c14b863f86d4986a8367?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JonasOlofsson&#39;s gravatar image" /><p>JonasOlofsson<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JonasOlofsson has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Dec '16, 05:52</p></div></div><div id="comments-container-58253" class="comments-container"></div><div id="comment-tools-58253" class="comment-tools"></div><div class="clear"></div><div id="comment-58253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

