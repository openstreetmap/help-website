+++
type = "question"
title = "Decode SMS Bearer Data Hex String"
description = '''I have the hex string for the SMS bearer data, GSM MAP, etc part of a network capture. Rather than providing an entire capture file to the Wireshark application, I just want to provide the hex stream of the SMS bearer data for decoding. Does Wireshark provide tools or an API for such a task? For exa...'''
date = "2014-01-09T08:53:00Z"
lastmod = "2014-01-10T13:24:00Z"
weight = 28735
keywords = [ "decode", "ansi", "tool", "sms", "gsm" ]
aliases = [ "/questions/28735" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Decode SMS Bearer Data Hex String](/questions/28735/decode-sms-bearer-data-hex-string)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28735-score" class="post-score" title="current number of votes">0</div><span id="post-28735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the hex string for the SMS bearer data, GSM MAP, etc part of a network capture. Rather than providing an entire capture file to the Wireshark application, I just want to provide the hex stream of the SMS bearer data for decoding. Does Wireshark provide tools or an API for such a task?</p><p>For example, below I have provided the hex string for the GSM Mobile Application and GSM SMS TPDU parts of a packet capture. It is an SMS-SUBMIT request which I have manually decoded.</p><p>0x3045840891150009880132008208917535f150f239f2042f3d000a9132695403000011411090513032002074747a0e4acf416110bd3ca783ccf2771b44479741d120885e0eb743</p><pre><code>    GTT: 1951009088102300
    MSISDN: 1957531052932
    Message Reference (TP-MR): 00
    TP-DA: 2396453000
    Timestamp: 01-09-2014 15:03:23 GMT+0
    Text Message: this is a test from the QA team!</code></pre><p>I am hoping that I don't have to go spelunking through ANSI/GSM specification documents, since Wireshark has probably already done that...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-ansi" rel="tag" title="see questions tagged &#39;ansi&#39;">ansi</span> <span class="post-tag tag-link-tool" rel="tag" title="see questions tagged &#39;tool&#39;">tool</span> <span class="post-tag tag-link-sms" rel="tag" title="see questions tagged &#39;sms&#39;">sms</span> <span class="post-tag tag-link-gsm" rel="tag" title="see questions tagged &#39;gsm&#39;">gsm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '14, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/ca7da0e6dc4124d3372c856e052fef24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tongerny&#39;s gravatar image" /><p><span>tongerny</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tongerny has no accepted answers">0%</span></p></div></div><div id="comments-container-28735" class="comments-container"></div><div id="comment-tools-28735" class="comment-tools"></div><div class="clear"></div><div id="comment-28735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28774"></span>

<div id="answer-container-28774" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28774-score" class="post-score" title="current number of votes">3</div><span id="post-28774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tongerny has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, you can do this with some manual steps:</p><ul><li>put your hex string in a file following the text2pcap format (<a href="http://www.wireshark.org/docs/man-pages/text2pcap.html)">http://www.wireshark.org/docs/man-pages/text2pcap.html)</a></li><li>in case of GSM SMS, as direction matters (to differentiate a SMS-DELIVER from a SMS-DELIVER REPORT for example) it's better to put it in the text file (see text2pcap -D option description)</li><li>in Wireshark GUI, click on File -&gt; Import from Hex Dump</li><li>In the new window, select your file, click on "Direction indication" checkbox in case you put a I or O to indicate the direction, and select a USER 0 to 15 encapsulation type</li><li>Then go to Edit -&gt; Preferences -&gt; DLT USER and configure the protocol used to decode the user layer type you selected (see wiki.wireshark.org/HowToDissectAnything). For GSM SMS, the protocol name is <code>gsm_sms</code> and for GSM MAP, it is <code>gsm_map</code></li></ul><p>Note that to call directly the GSM SMS dissector, you need to use a Wireshark 1.11.2 or later development version.</p><p>Good luck,</p><p>Pascal.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '14, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-28774" class="comments-container"><span id="28779"></span><div id="comment-28779" class="comment"><div id="post-28779-score" class="comment-score"></div><div class="comment-text"><p>Nice! It worked. Thanks.</p><p>I do have another related question though. Can this be done using a command line tool?</p><p>For example, I would like to be able to display GSM MAP in human readable format via a Perl script. As a debugging tool.</p></div><div id="comment-28779-info" class="comment-info"><span class="comment-age">(10 Jan '14, 12:24)</span> <span class="comment-user userinfo">tongerny</span></div></div><span id="28784"></span><div id="comment-28784" class="comment"><div id="post-28784-score" class="comment-score"></div><div class="comment-text"><p>Yes it can be done using a small script / program. You need to:</p><ul><li><p>generate the text file</p></li><li><p>call text2pcap to generate a pcap file from the text file: <code>text2pcap -D -l 147 input.txt output.pcap</code> (if you want to use User 0 link type)</p></li><li><p>call tshark and specifying how to decode the user DLT value as show here: <a href="https://ask.wireshark.org/questions/24474/user_dlt-option-in-tshark">https://ask.wireshark.org/questions/24474/user_dlt-option-in-tshark</a></p></li></ul></div><div id="comment-28784-info" class="comment-info"><span class="comment-age">(10 Jan '14, 13:24)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-28774" class="comment-tools"></div><div class="clear"></div><div id="comment-28774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

