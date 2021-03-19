+++
type = "question"
title = "60870-104 message guide"
description = '''Hi, I am a novice to wireshark and I just had a question about the types of messages which involve 60870-104. I understand that two main types are boadcasted: 104asdu, 104apci. One is from the RTUs to the control center and the other the other way around. What is the difference between the two and w...'''
date = "2015-11-17T01:49:00Z"
lastmod = "2015-11-17T04:10:00Z"
weight = 47655
keywords = [ "60870-5-104", "104apci" ]
aliases = [ "/questions/47655" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [60870-104 message guide](/questions/47655/60870-104-message-guide)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47655-score" class="post-score" title="current number of votes">0</div><span id="post-47655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am a novice to wireshark and I just had a question about the types of messages which involve 60870-104. I understand that two main types are boadcasted: 104asdu, 104apci. One is from the RTUs to the control center and the other the other way around. What is the difference between the two and what significance either has? I am sorry if the question is quite ordinary. Like I said, I am a novice.</p><p>Thanks, Mehrdad</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-60870-5-104" rel="tag" title="see questions tagged &#39;60870-5-104&#39;">60870-5-104</span> <span class="post-tag tag-link-104apci" rel="tag" title="see questions tagged &#39;104apci&#39;">104apci</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '15, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/076c0e4b9ce0017f7a17dafc74981a49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mehrdad%20Kazemtabrizi&#39;s gravatar image" /><p><span>Mehrdad Kaze...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mehrdad Kazemtabrizi has no accepted answers">0%</span></p></div></div><div id="comments-container-47655" class="comments-container"></div><div id="comment-tools-47655" class="comment-tools"></div><div class="clear"></div><div id="comment-47655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47662"></span>

<div id="answer-container-47662" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47662-score" class="post-score" title="current number of votes">0</div><span id="post-47662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is <a href="http://infosys.beckhoff.com/english.php?content=../content/1033/tcplclibiec870_5_104/html/tcplclibiec870_5_104_telegrammstructure.htm&amp;id=">this explanation</a> what you are looking for? The APCI part of the APDU is used for control of the communication, the ASDU part carries the payload.</p><p>NB: "broadcast" has a specific meaning, "to send something to all reachable recipients simultaneously", which is probably not the case here. When talking about sending something to a single recipient, "unicast" is used when you need distinction from broadcast (and multicast), and plain "send" or "transmit" otherwise.</p><p>If your actual question was why some of the packets are described as "104apci" and some as "104asdu" in the packet list pane, it is because Wireshark always shows the highest level of protocol hierarchy which can be found in the frame. So APDUs which only contain APCI but no ASDU are described as 104apci, and APDUs where also ASDU is present are described as 104asdu.</p><p>(well, to be precise: "Wireshark always shows the highest level of protocol hierarchy which can be found in the frame <em>and whose dissection is permitted in Wireshark configuration</em>").</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '15, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Nov '15, 12:38</strong> </span></p></div></div><div id="comments-container-47662" class="comments-container"></div><div id="comment-tools-47662" class="comment-tools"></div><div class="clear"></div><div id="comment-47662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

