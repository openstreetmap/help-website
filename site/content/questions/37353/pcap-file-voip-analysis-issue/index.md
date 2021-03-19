+++
type = "question"
title = "pcap file VoIP analysis issue"
description = '''All, I did a packet capture on our gateway on the VoIP interface (we&#x27;re having issues). I was able to play the voip calls successfully using telephony -&amp;gt; voip calls -&amp;gt; player -&amp;gt; decode etc. I left my computer for a little while and went back to play the calls again from the same pcap file. ...'''
date = "2014-10-26T14:16:00Z"
lastmod = "2014-10-26T15:34:00Z"
weight = 37353
keywords = [ "playback", "pcap", "rtp", "voip" ]
aliases = [ "/questions/37353" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [pcap file VoIP analysis issue](/questions/37353/pcap-file-voip-analysis-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37353-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>All,</p><p>I did a packet capture on our gateway on the VoIP interface (we're having issues).</p><p>I was able to play the voip calls successfully using telephony -&gt; voip calls -&gt; player -&gt; decode etc. I left my computer for a little while and went back to play the calls again from the same pcap file. Now it's showing that the files are 100% out of sequence and the timestamps are all incorrect. These are the same calls I was successfully able to playback not 20 mins prior. The pcap has not been changed in any way. Has anyone experienced this?</p></div><div id="question-tags" class="tags-container tags">playback pcap rtp voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '14, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/c97cc932072aebf9b9aed5142f90d1d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bitskrieg&#39;s gravatar image" /><p>bitskrieg<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bitskrieg has no accepted answers">0%</span></p></div></div><div id="comments-container-37353" class="comments-container"><span id="37357"></span><div id="comment-37357" class="comment"><div id="post-37357-score" class="comment-score"></div><div class="comment-text"><p>what is your</p><ul><li>OS and OS version</li><li>Wireshark version</li></ul></div><div id="comment-37357-info" class="comment-info"><span class="comment-age">(26 Oct '14, 15:29)</span> Kurt Knochner ♦</div></div><span id="37358"></span><div id="comment-37358" class="comment"><div id="post-37358-score" class="comment-score"></div><div class="comment-text"><p>Win 7 x64 WS 1.8.2 x64 WinPCap 4.1.3</p></div><div id="comment-37358-info" class="comment-info"><span class="comment-age">(26 Oct '14, 15:31)</span> bitskrieg</div></div></div><div id="comment-tools-37353" class="comment-tools"></div><div class="clear"></div><div id="comment-37353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37360"></span>

<div id="answer-container-37360" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37360-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There have been issues with the RTP player. Please upgrade <a href="https://www.wireshark.org/download.html">Wireshark to the latest version (currently 1.12.1)</a> and then check if the problem is still there.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '14, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37360" class="comments-container"><span id="37362"></span><div id="comment-37362" class="comment"><div id="post-37362-score" class="comment-score"></div><div class="comment-text"><p>Tried that, when I update to 1.12.1 it doesn't even detect my ULAW streams correctly, only the g.729 ones. Anything higher than 1.8.2 doesn't find g.711 conversations (for me anyway).</p></div><div id="comment-37362-info" class="comment-info"><span class="comment-age">(26 Oct '14, 15:40)</span> bitskrieg</div></div></div><div id="comment-tools-37360" class="comment-tools"></div><div class="clear"></div><div id="comment-37360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

