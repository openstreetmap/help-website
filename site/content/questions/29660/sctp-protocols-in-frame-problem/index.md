+++
type = "question"
title = "SCTP: &quot;Protocols in frame&quot; problem"
description = '''I am analyzing diameter over sctp packets.  There are also vendor specific AVPs included which I have added to the diameter dictionary. My problem is that I get a different analysis result on two different computers. One is running Windows 8 and the other is running Windows 7, but this might not be ...'''
date = "2014-02-10T22:18:00Z"
lastmod = "2014-02-13T13:06:00Z"
weight = 29660
keywords = [ "sctp", "protocols_in_frame" ]
aliases = [ "/questions/29660" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [SCTP: "Protocols in frame" problem](/questions/29660/sctp-protocols-in-frame-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29660-score" class="post-score" title="current number of votes">0</div><span id="post-29660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am analyzing diameter over sctp packets. There are also vendor specific AVPs included which I have added to the diameter dictionary.<br />
My problem is that I get a different analysis result on two different computers. One is running Windows 8 and the other is running Windows 7, but this might not be relevant. On both computers I have installed "Version 1.10.5 (SVN Rev 54262 from /trunk-1.10)". And to avoid any further differences I have copied the diameter subdirectory contaning the dictionaries from one computer to the other.</p><p>But then I still get a different result on both computers. The reason are the detected protocols in frame.</p><p>On one computer (Windows 8) I get the expected result:<br />
[Protocols in frame: eth:vlan:vlan:ip:sctp]<br />
The packet (2) is identified as "SCTP SACK DATA (Message Fragment)"<br />
The next packet (3) then shows the Diameter packet fully eassembled with all vendor specific AVPs.<br />
</p><p>On the other computer (Windows 7) I get the result:<br />
[Protocols in frame: eth:vlan:vlan:ip:sctp:diameter:diameter:diameter:diameter.3gpp:diameter:diameter.3gpp:xml]<br />
The packet (2) is identified as "Diameter SACK cmd=..."<br />
The next packet (3) cannot be reassembled [Unreassembled packet: Diameter]</p><p>What might be wrong here? If necessary I can add the 4 packets around the problem in pcap-fomat.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sctp" rel="tag" title="see questions tagged &#39;sctp&#39;">sctp</span> <span class="post-tag tag-link-protocols_in_frame" rel="tag" title="see questions tagged &#39;protocols_in_frame&#39;">protocols_in_frame</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '14, 22:18</strong></p><img src="https://secure.gravatar.com/avatar/f76e1057a16ab7d81c0981c956f34ae1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="efranz&#39;s gravatar image" /><p><span>efranz</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="efranz has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-29660" class="comments-container"><span id="29665"></span><div id="comment-29665" class="comment"><div id="post-29665-score" class="comment-score">1</div><div class="comment-text"><p>So if you read the <em>same</em> capture file with the <em>same</em> version of Wireshark on a Windows 7 machine and a Windows 8 machine, you get different results?</p><p>What happens if you make sure that the preference settings for the IP, SCTP and Diameter protocols on the Windows 8 machine are the same as they are on the Windows 7 machine (i.e., look at the settings on the Windows 7 machine, and change the settings on the Windows 8 machine to match them)?</p></div><div id="comment-29665-info" class="comment-info"><span class="comment-age">(11 Feb '14, 00:53)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="29666"></span><div id="comment-29666" class="comment"><div id="post-29666-score" class="comment-score"></div><div class="comment-text"><p>Yes, that is the same capture file and the same version of Wireshark (in both cases the 64-bit version).<br />
</p><p>Regarding the preference settings for IP, SCTP and Diameter protocol I assume these are the same on both machines, because I did not modify anything afaik. But I will check it in the evening and answer.<br />
(The Windows 8 machine is my private notebook and the Windows 7 machine is the office PC).</p></div><div id="comment-29666-info" class="comment-info"><span class="comment-age">(11 Feb '14, 01:04)</span> <span class="comment-user userinfo">efranz</span></div></div><span id="29726"></span><div id="comment-29726" class="comment"><div id="post-29726-score" class="comment-score"></div><div class="comment-text"><p>Just as an update:<br />
</p><p>The SCTP preference to reassemble fragmented messages is generally not enabled (independent of Windows 7 or 8).<br />
I enabled reassembling of fragmented messages on my Windows 8 machine and forgot it. Then I recognized the discrepancy.<br />
</p><p>Maybe it would be a good idea to enable reassembling of fragmented SCTP messages generally (per default). I don't know any reason wher this may harm.</p></div><div id="comment-29726-info" class="comment-info"><span class="comment-age">(11 Feb '14, 21:09)</span> <span class="comment-user userinfo">efranz</span></div></div><span id="29839"></span><div id="comment-29839" class="comment"><div id="post-29839-score" class="comment-score">1</div><div class="comment-text"><p>Well, it's probably off because enabling it means using more CPU and lots more memory. But TCP has desegmentation enabled by default so I guess it probably makes sense for SCTP to as well.</p><p>I submitted a <a href="https://code.wireshark.org/review/#/c/200/">change</a> to change the default.</p><p>BTW, if the Answer on this question, well, answered your question, please Accept it (by clicking the checkmark) so the question won't show up in the list of unanswered questions.</p></div><div id="comment-29839-info" class="comment-info"><span class="comment-age">(13 Feb '14, 13:06)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-29660" class="comment-tools"></div><div class="clear"></div><div id="comment-29660-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29713"></span>

<div id="answer-container-29713" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29713-score" class="post-score" title="current number of votes">1</div><span id="post-29713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="efranz has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>(As implied by Guy), it sounds a lot like the SCTP preference to reassemble fragmented messages is not enabled on the Windows 7 machine. (It's off by default.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '14, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span> </br></br></p></div></div><div id="comments-container-29713" class="comments-container"></div><div id="comment-tools-29713" class="comment-tools"></div><div class="clear"></div><div id="comment-29713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

