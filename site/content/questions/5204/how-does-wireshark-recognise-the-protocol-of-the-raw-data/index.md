+++
type = "question"
title = "How does Wireshark recognise the protocol of the raw data?"
description = '''Are the functions located in the capture.c file? I have gone through the Developer&#x27;s Guide but I can&#x27;t really find the explanation on how wireshark automatically detects which protocol the raw data belongs to. Thanks for your attention. Regards, Eddie Choo'''
date = "2011-07-25T01:14:00Z"
lastmod = "2011-07-25T20:16:00Z"
weight = 5204
keywords = [ "wireshark" ]
aliases = [ "/questions/5204" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How does Wireshark recognise the protocol of the raw data?](/questions/5204/how-does-wireshark-recognise-the-protocol-of-the-raw-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5204-score" class="post-score" title="current number of votes">1</div><span id="post-5204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Are the functions located in the capture.c file? I have gone through the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/">Developer's Guide</a> but I can't really find the explanation on how wireshark automatically detects which protocol the raw data belongs to.</p><p>Thanks for your attention.</p><p>Regards, Eddie Choo</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '11, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/c1dac05d0e75992546b5da006c6b718e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eddie%20choo&#39;s gravatar image" /><p><span>eddie choo</span><br />
<span class="score" title="66 reputation points">66</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eddie choo has 2 accepted answers">66%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jul '11, 01:52</strong> </span></p></div></div><div id="comments-container-5204" class="comments-container"><span id="5205"></span><div id="comment-5205" class="comment"><div id="post-5205-score" class="comment-score"></div><div class="comment-text"><p>i have been reading <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChapterCapture.html#ChCaptureAddLibpcap">this</a> whole day and still feeling blurred</p></div><div id="comment-5205-info" class="comment-info"><span class="comment-age">(25 Jul '11, 02:08)</span> <span class="comment-user userinfo">eddie choo</span></div></div></div><div id="comment-tools-5204" class="comment-tools"></div><div class="clear"></div><div id="comment-5204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5210"></span>

<div id="answer-container-5210" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5210-score" class="post-score" title="current number of votes">1</div><span id="post-5210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="eddie choo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'll refer you to <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChWorksOverview.html">the overview</a> in the Developer Guide. There you'll see the frame data comes in from the Wiretap library. It is generalized input from various sources. Epan <a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/packet.c">gives</a> data and <a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/packet_info.h">metadata</a> to the <a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-frame.c">frame dissector</a>. Based on this metadata it decides which further dissector gets the data passed to it. Therefore these dissectors have to register themselves, for the Wiretap encapsulation type they handle, with the table ("wtap_encap") which is used by the frame dissector. Then it's just a matter of Rinse and Repeat(sm).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '11, 05:15</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5210" class="comments-container"></div><div id="comment-tools-5210" class="comment-tools"></div><div class="clear"></div><div id="comment-5210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5239"></span>

<div id="answer-container-5239" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5239-score" class="post-score" title="current number of votes">0</div><span id="post-5239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have found a quite complete explanation from an <a href="http://comes.umy.ac.id/file.php/1/Pengumuman_FT/E-Book_TI/Wireshark_and_Ethereal.pdf">e-book</a> for my own question (again) Chapter 8, pg 440 "The Dissection Process"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '11, 20:16</strong></p><img src="https://secure.gravatar.com/avatar/c1dac05d0e75992546b5da006c6b718e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eddie%20choo&#39;s gravatar image" /><p><span>eddie choo</span><br />
<span class="score" title="66 reputation points">66</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eddie choo has 2 accepted answers">66%</span></p></div></div><div id="comments-container-5239" class="comments-container"></div><div id="comment-tools-5239" class="comment-tools"></div><div class="clear"></div><div id="comment-5239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

