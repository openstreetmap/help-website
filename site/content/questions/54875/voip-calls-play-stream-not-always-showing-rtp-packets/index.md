+++
type = "question"
title = "VoIP Calls Play Stream not always showing RTP packets..."
description = '''All traffic is being captured between my VRU system and PBX using dumpcap: &quot;c:&#92;program files&#92;wireshark&#92;dumpcap&quot; -b filesize:100000 -b files:100 -i 1 -w ivr_dmp_p1.pcapng -f &quot;net &amp;lt;PBX IP Addr&amp;gt;&quot; The files are being captured just fine and all the data for the calls appears to be in the files, how...'''
date = "2016-08-16T08:44:00Z"
lastmod = "2016-08-16T08:44:00Z"
weight = 54875
keywords = [ "rtp", "voip", "calls", "stream", "rtp_stream" ]
aliases = [ "/questions/54875" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [VoIP Calls Play Stream not always showing RTP packets...](/questions/54875/voip-calls-play-stream-not-always-showing-rtp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54875-score" class="post-score" title="current number of votes">0</div><span id="post-54875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>All traffic is being captured between my VRU system and PBX using dumpcap:</p><p><code>"c:\program files\wireshark\dumpcap" -b filesize:100000 -b files:100 -i 1 -w ivr_dmp_p1.pcapng -f "net &lt;PBX IP Addr&gt;"</code></p><p>The files are being captured just fine and all the data for the calls appears to be in the files, however when the files are analyzed using Telephony-&gt;VoIP Calls-&gt;Play Stream, the first few calls in the file have, and play the RTP audio, but after the third or fourth call, the RTP audio does not appear in the play stream window. The RTP audio packets can be listened to using Telephony-&gt;RTP-&gt;RTP Streams. The draw back to this is that it takes a while to manually correlate the RTP audio with the VoIP call.</p><p>I am using WireShark 2.0.5, 64 bit. Is this a configuration problem? Should I capture smaller files? any suggestions would be greatly appreciated.</p><p>Thank you,</p><p>SBrock</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span> <span class="post-tag tag-link-calls" rel="tag" title="see questions tagged &#39;calls&#39;">calls</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-rtp_stream" rel="tag" title="see questions tagged &#39;rtp_stream&#39;">rtp_stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '16, 08:44</strong></p><img src="https://secure.gravatar.com/avatar/5d3a105bdd5493421fbbb1cb78adac1c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sbrock&#39;s gravatar image" /><p><span>sbrock</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sbrock has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Aug '16, 08:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54875" class="comments-container"></div><div id="comment-tools-54875" class="comment-tools"></div><div class="clear"></div><div id="comment-54875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

