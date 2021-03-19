+++
type = "question"
title = "RTP packet play"
description = '''Hi everyone, I need to analyze a sequence of RTP packets, in order to try to listen the payload and &#92;or to convert it to wav. I understand that under Telephony -&amp;gt; RTP Wireshark permits to analyze inbound &#92;  outbound streams but, here is the problem, i&#x27;ve no stream, i only have a file with all RTP...'''
date = "2017-07-11T00:32:00Z"
lastmod = "2017-07-11T02:02:00Z"
weight = 62655
keywords = [ "rtp" ]
aliases = [ "/questions/62655" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [RTP packet play](/questions/62655/rtp-packet-play)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62655-score" class="post-score" title="current number of votes">0</div><span id="post-62655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone, I need to analyze a sequence of RTP packets, in order to try to listen the payload and \or to convert it to wav. I understand that under Telephony -&gt; RTP Wireshark permits to analyze inbound \ outbound streams but, here is the problem, i've no stream, i only have a file with all RTP packets one after another (this is not a Wireshark dump).</p><p>Is there any way to try to analize that file.</p><p>Thanks in advance to everyone.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '17, 00:32</strong></p><img src="https://secure.gravatar.com/avatar/46c3cf954f98256f5dc11f2b9b5be054?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iplaga&#39;s gravatar image" /><p><span>iplaga</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iplaga has no accepted answers">0%</span></p></div></div><div id="comments-container-62655" class="comments-container"><span id="62656"></span><div id="comment-62656" class="comment"><div id="post-62656-score" class="comment-score"></div><div class="comment-text"><p>Is it a pcap file or at least something that Wireshark can open?</p></div><div id="comment-62656-info" class="comment-info"><span class="comment-age">(11 Jul '17, 00:55)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-62655" class="comment-tools"></div><div class="clear"></div><div id="comment-62655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62658"></span>

<div id="answer-container-62658" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62658-score" class="post-score" title="current number of votes">0</div><span id="post-62658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to convert raw file with RTP packets into .pcap format, or other formats compatible with wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '17, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/5f52a68bc7c3007b89b6d13df27d4184?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nomad&#39;s gravatar image" /><p><span>Nomad</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nomad has no accepted answers">0%</span></p></div></div><div id="comments-container-62658" class="comments-container"></div><div id="comment-tools-62658" class="comment-tools"></div><div class="clear"></div><div id="comment-62658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="62659"></span>

<div id="answer-container-62659" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62659-score" class="post-score" title="current number of votes">0</div><span id="post-62659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A "stream" is just a logical view of a group of packets. So what you need is to sort out the packets up to some properties into "streams". For normal RTP recorded in wild, grouping them by the SSRC field is the easiest way to go, but in some laboratory environments you may have to look at source&amp;destination IP addresses and UDP ports as well because the SSRC values are not generated properly.</p><p>So once you have the file open in Wireshark, the first question is whether Wireshark dissects them as RTP or only as plain UDP. If as RTP, you can obtain a list of all RTP streams using <code>Telephony -&gt; RTP -&gt; RTP Streams</code>, then choose one of them for "Analyse stream" and from there either directly play it or save its contents into an .au file. Depending on the codec, this may be enough or not.</p><p>If Wireshark could not auto-detect that the UDP packets were RTP ones, you have to apply a display filter <code>udp and !rtp</code> and then randomly choose packets in the packet list, right-click them, choose <code>Decode as...</code> and mark them as RTP ones (both directions) until you have no packets left. Then you can remove the display filter and proceed as written above.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '17, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62659" class="comments-container"></div><div id="comment-tools-62659" class="comment-tools"></div><div class="clear"></div><div id="comment-62659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

