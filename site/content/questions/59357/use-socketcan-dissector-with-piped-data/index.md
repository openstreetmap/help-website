+++
type = "question"
title = "Use socketcan dissector with piped data"
description = '''Hi I&#x27;m using a pipe to send CAN data to Wireshark and would like to use the socketCAN dissector to interpret the data. The question is how I should send the data for socketCAN to interpret it correctly? I am using the C# example from https://wiki.wireshark.org/CaptureSetup/Pipes to pipe the data. I ...'''
date = "2017-02-12T12:35:00Z"
lastmod = "2017-02-16T10:31:00Z"
weight = 59357
keywords = [ "pipe", "socketcan", "dissector" ]
aliases = [ "/questions/59357" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Use socketcan dissector with piped data](/questions/59357/use-socketcan-dissector-with-piped-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59357-score" class="post-score" title="current number of votes">0</div><span id="post-59357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I'm using a pipe to send CAN data to Wireshark and would like to use the socketCAN dissector to interpret the data. The question is how I should send the data for socketCAN to interpret it correctly?</p><p>I am using the C# example from <a href="https://wiki.wireshark.org/CaptureSetup/Pipes">https://wiki.wireshark.org/CaptureSetup/Pipes</a> to pipe the data. I have set the data link type in the global header to 125 which should be the socketCAN number ( <a href="https://github.com/wireshark/wireshark/blob/master/wiretap/wtap.h">https://github.com/wireshark/wireshark/blob/master/wiretap/wtap.h</a> ). When I send some dummy data to Wireshark the protocol is listed as UNKNOWN and not CAN. I guess this is because the structure or length of the data is not correct. Do You know if that's true?</p><p>I have looked at the socketCAN dissector file ( <a href="https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-socketcan.c">https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-socketcan.c</a> ) but still have not been able to format the data correctly.</p><p>Hope that someone is able to provide some guidance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pipe" rel="tag" title="see questions tagged &#39;pipe&#39;">pipe</span> <span class="post-tag tag-link-socketcan" rel="tag" title="see questions tagged &#39;socketcan&#39;">socketcan</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '17, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/cd91864a99534016834b708fd5a49fa9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Degnemose&#39;s gravatar image" /><p><span>Degnemose</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Degnemose has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Feb '17, 06:30</strong> </span></p></div></div><div id="comments-container-59357" class="comments-container"></div><div id="comment-tools-59357" class="comment-tools"></div><div class="clear"></div><div id="comment-59357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59470"></span>

<div id="answer-container-59470" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59470-score" class="post-score" title="current number of votes">1</div><span id="post-59470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Degnemose has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You're writing PCAP headers, so you'll need to use PCAP defined link layer types. For socketCAN this is <a href="https://github.com/wireshark/wireshark/blob/master/wiretap/pcap-common.c#L382">227</a>, which is translated into the Wiretap library's corresponding value of .... 125.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '17, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59470" class="comments-container"><span id="59471"></span><div id="comment-59471" class="comment"><div id="post-59471-score" class="comment-score"></div><div class="comment-text"><p>You might also want to look into <a href="https://wiki.wireshark.org/Development/Extcap">extcap</a>, this "formalises" the pipe style interface such that the extcap plugins show up in the interface list and can be passed configuration parameters.</p></div><div id="comment-59471-info" class="comment-info"><span class="comment-age">(16 Feb '17, 07:05)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="59480"></span><div id="comment-59480" class="comment"><div id="post-59480-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jaap, that seems to do it for me. Now the protocol shows as CAN and the data structure is clear from the frame interpretation. The first 4 bytes are 3 flag bits and 29 id bits. Then 4 bytes where the first byte is the data length (the remaining 3 bytes seems to be ignored). Finally the data bytes follows.</p><p>Also thank you for the tip grahamb, I will look into that.</p></div><div id="comment-59480-info" class="comment-info"><span class="comment-age">(16 Feb '17, 10:31)</span> <span class="comment-user userinfo">Degnemose</span></div></div></div><div id="comment-tools-59470" class="comment-tools"></div><div class="clear"></div><div id="comment-59470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

