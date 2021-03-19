+++
type = "question"
title = "Extracting a link from this output. I&#x27;m mystified....."
description = '''Hi guys, I am needing help extracting a playable URL/Stream from this: http://embed.wildearth.tv:8080/cam/dju-waterhole-02.stream?aspectratio=16:9&amp;amp;sourceid=101-101-122-125-11&amp;amp;autostart=true. I followed the most excellent tutorial here: https://ask.wireshark.org/questions/29730/wireshark-filt...'''
date = "2016-08-17T14:35:00Z"
lastmod = "2016-08-17T14:35:00Z"
weight = 54929
keywords = [ "url", "follow.tcp.stream", "video" ]
aliases = [ "/questions/54929" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting a link from this output. I'm mystified.....](/questions/54929/extracting-a-link-from-this-output-im-mystified)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54929-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, I am needing help extracting a playable URL/Stream from this: <a href="http://embed.wildearth.tv:8080/cam/dju-waterhole-02.stream?aspectratio=16:9&amp;sourceid=101-101-122-125-11&amp;autostart=true">http://embed.wildearth.tv:8080/cam/dju-waterhole-02.stream?aspectratio=16:9&amp;sourceid=101-101-122-125-11&amp;autostart=true</a>. I followed the most excellent tutorial here: <a href="https://ask.wireshark.org/questions/29730/wireshark-filter-for-finding-url-of-live-stream-video">https://ask.wireshark.org/questions/29730/wireshark-filter-for-finding-url-of-live-stream-video</a> and ran into a big dead end.</p><p>I see most ( vast majority )packets are coming from one IP after I sorted based on packets. When I look at Conversations -&gt; TCP, to try to see the header and extract a URL I see this ( it's snipped of course ).</p><pre><code>H.&amp;{../....play.............mp4:dju-waterhole-02.stream........................&quot;........onStatus.............level...status..code...NetStream.Play.Stop..description..ZStopped playing wowz://206.190.136.148:1935/rtsp-ingest/_definst_/dju-waterhole-02.stream...clientid.A..D......reason.....details..Iwowz://206.190.136.148:1935/rtsp-ingest/_definst_/dju-waterhole-02.stream..  .................................onStatus.............level...status..code...NetStream.Play.Reset..description..`Playing and resetting wowz://206.190.136.148:1935/rtsp-ingest/_definst_/dju-waterhole-02.stream...clientid.A..D......  ...............onStatus.............level...status..code...NetStream.Play.Start..description..ZStarted playing wowz://206.190.136.148:1935/rtsp-ingest/_definst_/dju-waterhole-02.stream...clientid.A..D.....
isFastPlay....timecodeOffset...3962530061L..    E..........|RtmpSampleAccess..........,........onStatus...code...NetStream.Data.Start.. ............. ....E.........
onMetaData...videocodecid...avc1.
[email protected]
[email protected]@[email protected]
audiodatarate.@P....... trackinfo
......  [email protected]
......
sampletype...H264.. ..type...video..    ..  [email protected]@.......language...eng..sampledescription
......
sampletype..
MPEG4-GENERIC.. ..type...audio..config...1410..description..W{AACFrame: codec:AAC, channels:2, frequency:16000, samplesPerFrame:1024, objectType:LC}..  ..rtpsessioninfo...information...rtsp-server..name...Session streamed with GStreamer..origin..+- 1188340656180883 1 IN IP4 192.168.123.252..timing...0 0..protocolversion...0.
attributes...range...npt=now-..tool..   GStreamer..type..   broadcast.. ..  ..  ......&amp; ..........M.)....gM.)..
..`[email protected]@xx.....h.&lt;.F......   W.......6   [email protected]</code></pre><p>After going back to the main Wireshark window and sorting by RTMP, I did discover this...</p><pre><code>24  3.617806    192.168.1.2 206.190.138.100 RTMP    121 play(&#39;mp4:dju-waterhole-02.stream&#39;)</code></pre><p>But I'm not sure if that's helpful either. Does anyone have any pointers to send me in the right direction?</p><p>Many thanks H.S.</p></div><div id="question-tags" class="tags-container tags">url follow.tcp.stream video</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '16, 14:35</strong></p><img src="https://secure.gravatar.com/avatar/0722deaee4f613f726a8a186c776b229?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hiromitsu_shinaka&#39;s gravatar image" /><p>hiromitsu_sh...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hiromitsu_shinaka has no accepted answers">0%</span></p></div></div><div id="comments-container-54929" class="comments-container"></div><div id="comment-tools-54929" class="comment-tools"></div><div class="clear"></div><div id="comment-54929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

