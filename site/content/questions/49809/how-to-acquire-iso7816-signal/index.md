+++
type = "question"
title = "how to acquire iso7816 signal"
description = '''I need to be able to analyse the iso7816 communication between a smart card and a smart card reader. I&#x27;ve seen that wireshark is able to analyse the iso7816 communication, but where can I find the hardware to record the communication that I will put between the smart card and the reader?'''
date = "2016-02-04T02:03:00Z"
lastmod = "2016-02-04T04:22:00Z"
weight = 49809
keywords = [ "iso7816" ]
aliases = [ "/questions/49809" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to acquire iso7816 signal](/questions/49809/how-to-acquire-iso7816-signal)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49809-score" class="post-score" title="current number of votes">0</div><span id="post-49809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to be able to analyse the iso7816 communication between a smart card and a smart card reader. I've seen that wireshark is able to analyse the iso7816 communication, but where can I find the hardware to record the communication that I will put between the smart card and the reader?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iso7816" rel="tag" title="see questions tagged &#39;iso7816&#39;">iso7816</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Feb '16, 02:03</strong></p><img src="https://secure.gravatar.com/avatar/ee4b2d8d93476b46fc91ca497f7a4409?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc%20A&#39;s gravatar image" /><p><span>Marc A</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc A has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Feb '16, 04:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-49809" class="comments-container"><span id="49810"></span><div id="comment-49810" class="comment"><div id="post-49810-score" class="comment-score"></div><div class="comment-text"><p>Just a blind shot - have you tried to capture the USB communication of the reader with your PC, using USBPcap? You may find iso7816 as the payload if lucky.</p></div><div id="comment-49810-info" class="comment-info"><span class="comment-age">(04 Feb '16, 03:43)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="49812"></span><div id="comment-49812" class="comment"><div id="post-49812-score" class="comment-score"></div><div class="comment-text"><p>I think I need to clarify the reader s not a USB reader linked to the PC but a standalone device. My aim is to check that this standalone device is correctly handling the ISO7816 protocol. So, what I need is to capture all the exchanges between this device and the card in real time, so that wireshark can analyse it. I can not capture the and analyse the USB communication of the reader, since the reader is not linked to the PC</p></div><div id="comment-49812-info" class="comment-info"><span class="comment-age">(04 Feb '16, 04:22)</span> <span class="comment-user userinfo">Marc A</span></div></div></div><div id="comment-tools-49809" class="comment-tools"></div><div class="clear"></div><div id="comment-49809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

