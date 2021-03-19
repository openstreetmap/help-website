+++
type = "question"
title = "how to decode GSM Um Interface Message?"
description = '''Now i have a GSM Um Interface Message: 06 21 00 01 F0 CB 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B  In GSM Um Interface ,IT is a &quot;Paging Request Type 1&quot; message, How to Use Wireshark to Decoded it? thanks!'''
date = "2014-03-22T09:13:00Z"
lastmod = "2014-03-24T02:16:00Z"
weight = 31078
keywords = [ "decoded", "gsm" ]
aliases = [ "/questions/31078" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to decode GSM Um Interface Message?](/questions/31078/how-to-decode-gsm-um-interface-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31078-score" class="post-score" title="current number of votes">0</div><span id="post-31078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Now i have a GSM Um Interface Message: 06 21 00 01 F0 CB 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B 2B In GSM Um Interface ,IT is a "Paging Request Type 1" message, How to Use Wireshark to Decoded it?</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decoded" rel="tag" title="see questions tagged &#39;decoded&#39;">decoded</span> <span class="post-tag tag-link-gsm" rel="tag" title="see questions tagged &#39;gsm&#39;">gsm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '14, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/ca63beaa30363d3b98d78cce231f71a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="whywhyyu&#39;s gravatar image" /><p><span>whywhyyu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="whywhyyu has no accepted answers">0%</span></p></div></div><div id="comments-container-31078" class="comments-container"></div><div id="comment-tools-31078" class="comment-tools"></div><div class="clear"></div><div id="comment-31078-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31084"></span>

<div id="answer-container-31084" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31084-score" class="post-score" title="current number of votes">0</div><span id="post-31084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Some air interface sniffers can encapsulate those messages into a GSMTAP message, and append "dummy" IP and UDP headers to them, saving them in a .pcap file format for Wireshark to decode.</p><p>The message you posted there is definitely not an IP packet. You won't be able to just directly decode air interface messages in Wireshark but as I said most tools I've seen that do this kind of air interface tracing should support that kind of export into .pcap files.</p><p>What kind of analyzer are you using at the UE to trace the Um interface?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '14, 14:23</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Mar '14, 14:24</strong> </span></p></div></div><div id="comments-container-31084" class="comments-container"><span id="31085"></span><div id="comment-31085" class="comment"><div id="post-31085-score" class="comment-score">1</div><div class="comment-text"><p>I could not resist to award you one extra point ;-)) Total now: 666</p></div><div id="comment-31085-info" class="comment-info"><span class="comment-age">(22 Mar '14, 14:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31086"></span><div id="comment-31086" class="comment"><div id="post-31086-score" class="comment-score"></div><div class="comment-text"><p>Ha. Not sure if I should thank you for that or not. :)</p></div><div id="comment-31086-info" class="comment-info"><span class="comment-age">(22 Mar '14, 14:28)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="31087"></span><div id="comment-31087" class="comment"><div id="post-31087-score" class="comment-score"></div><div class="comment-text"><p>depends on your godliness :-)) If you feel uncomfortable, you can return the point to me or donate it to someone else ;-))</p></div><div id="comment-31087-info" class="comment-info"><span class="comment-age">(22 Mar '14, 14:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31094"></span><div id="comment-31094" class="comment"><div id="post-31094-score" class="comment-score"></div><div class="comment-text"><p>Thank you ! We have No "analyzer"! I got that message from the Phone(BaseBand GSM stack) internal log system ,these logs show what message they got from the BTS,and always i need to analyser message manual .</p><p>can you give me an idea? what "tools" can convert these message to a ".pcap" file? Thank you again!</p></div><div id="comment-31094-info" class="comment-info"><span class="comment-age">(23 Mar '14, 08:13)</span> <span class="comment-user userinfo">whywhyyu</span></div></div><span id="31099"></span><div id="comment-31099" class="comment"><div id="post-31099-score" class="comment-score"></div><div class="comment-text"><p>Well, for free stuff, take a look at "airprobe" which used to be called gsm-sniffer. Among its binaries is "gsm-receiver" which stores in a .pcap file format for Wireshark using GSMTAP.</p><p>Another is OpenBTS, but for that you're effectively emulating the base station.</p><p>If you're an operator, you can probably get your hands on more sophisticated UE testers from the chipset vendors, like Qualcom's QXDM. Also, if you're an operator, usually the IuB interface onwards nowadays <em>is</em> over IP and Wireshark supports those kinds of stacks (eg: IP/SCTP/NBAP from the base stations). Depending on what you want to see from the UE, if it's something like a NAS exchange (eg: that location update you're looking at), there's usually no reason to need to trace the air interface unless you're isolating RRC-level troubleshooting or unless you're not an operator but just testing the performance or behaviour of the operator.</p><p>You've got me thinking though, if there's a program to take the messages as text from your log file and encapsulate them into GSMTAP...... In concept it should be doable, though I'm not sure of any tool that does quite what you're looking for.</p></div><div id="comment-31099-info" class="comment-info"><span class="comment-age">(23 Mar '14, 12:42)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-31084" class="comment-tools"></div><div class="clear"></div><div id="comment-31084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31106"></span>

<div id="answer-container-31106" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31106-score" class="post-score" title="current number of votes">0</div><span id="post-31106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can follow the procedure described here: <a href="http://ask.wireshark.org/questions/28735/decode-sms-bearer-data-hex-string">http://ask.wireshark.org/questions/28735/decode-sms-bearer-data-hex-string</a> and use the <code>gsm_a_dtap</code> dissector name instead of <code>gsm_sms</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '14, 02:16</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Mar '14, 02:16</strong> </span></p></div></div><div id="comments-container-31106" class="comments-container"></div><div id="comment-tools-31106" class="comment-tools"></div><div class="clear"></div><div id="comment-31106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

