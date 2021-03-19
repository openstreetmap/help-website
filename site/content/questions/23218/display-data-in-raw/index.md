+++
type = "question"
title = "Display data in raw"
description = '''good morning, everyone i need to display a message in à field , but it is too long , so when it is displayed , it is truncked , so i want to display this message like a raw data like in SIP protocol. can someone tell me if a special type fot that existe ?? Thank you. '''
date = "2013-07-22T00:16:00Z"
lastmod = "2013-07-23T06:21:00Z"
weight = 23218
keywords = [ "raw" ]
aliases = [ "/questions/23218" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Display data in raw](/questions/23218/display-data-in-raw)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23218-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>good morning, everyone</p><p>i need to display a message in à field , but it is too long , so when it is displayed , it is truncked , so i want to display this message like a raw data like in SIP protocol.</p><p>can someone tell me if a special type fot that existe ??</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">raw</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '13, 00:16</strong></p><img src="https://secure.gravatar.com/avatar/9fbe9f669a6d14e31178d8193125c39a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cruz&#39;s gravatar image" /><p>cruz<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cruz has no accepted answers">0%</span></p></div></div><div id="comments-container-23218" class="comments-container"><span id="23232"></span><div id="comment-23232" class="comment"><div id="post-23232-score" class="comment-score"></div><div class="comment-text"><p>can you please post a screenshot with the truncated message and add more details about your protocol and where exactly the message was truncated (GUI, tshark, your own dissector)?</p></div><div id="comment-23232-info" class="comment-info"><span class="comment-age">(22 Jul '13, 06:49)</span> Kurt Knochner ♦</div></div><span id="23240"></span><div id="comment-23240" class="comment"><div id="post-23240-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/Nouvelle_image_(2).bmp" alt="alt text" /></p><p>This is a screenshot, the msg is too long so it is tunked when it is displayed , i want to display this msg in raw data exactly like in SIP protocol , because i need to display all the information, but i don't know if " raw data" is a special type or not !!!</p><p>thank you</p></div><div id="comment-23240-info" class="comment-info"><span class="comment-age">(22 Jul '13, 09:53)</span> cruz</div></div><span id="23255"></span><div id="comment-23255" class="comment"><div id="post-23255-score" class="comment-score"></div><div class="comment-text"><p>I cannot find a dissector with a field name "Filename:" !?! If this your own dissector code?</p></div><div id="comment-23255-info" class="comment-info"><span class="comment-age">(22 Jul '13, 14:38)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-23218" class="comment-tools"></div><div class="clear"></div><div id="comment-23218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23283"></span>

<div id="answer-container-23283" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23283-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>@cruz, I deleted your duplicate "answer" and your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>Have a look at the function <code>tvb_raw_text_add</code> in <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-sip.c?revision=50366&amp;view=markup">packet-sip.c</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '13, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div></div><div id="comments-container-23283" class="comments-container"><span id="23285"></span><div id="comment-23285" class="comment"><div id="post-23285-score" class="comment-score"></div><div class="comment-text"><p>thank you for your answer</p></div><div id="comment-23285-info" class="comment-info"><span class="comment-age">(23 Jul '13, 07:15)</span> cruz</div></div><span id="23327"></span><div id="comment-23327" class="comment"><div id="post-23327-score" class="comment-score"></div><div class="comment-text"><p>@grahamb ♦ thank you very match it is the right function.</p><p>Thank you,</p></div><div id="comment-23327-info" class="comment-info"><span class="comment-age">(24 Jul '13, 07:32)</span> cruz</div></div><span id="23328"></span><div id="comment-23328" class="comment"><div id="post-23328-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-23328-info" class="comment-info"><span class="comment-age">(24 Jul '13, 08:11)</span> grahamb ♦</div></div></div><div id="comment-tools-23283" class="comment-tools"></div><div class="clear"></div><div id="comment-23283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23270"></span>

<div id="answer-container-23270" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23270-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>After checking the code, I found that the item max length is defined as follows.</p><p><strong>proto.h</strong></p><pre><code>/** the maximum length of a protocol field string representation */
#define ITEM_LABEL_LENGTH   240</code></pre><p>If you try to add text that is larger than 240 chars, it will be truncated and the item/field will be marked with [truncated]. At least that's how I understand the code ;-)</p><blockquote><p>i want to display this msg in <strong>raw data</strong> exactly like <strong>in SIP</strong> protocol</p></blockquote><p>I'm not sure what you mean by <strong>raw data</strong> in SIP? Can you please add more details or a screenshot that shows it.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '13, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23270" class="comments-container"><span id="23281"></span><div id="comment-23281" class="comment"><div id="post-23281-score" class="comment-score"></div><div class="comment-text"><p>thank's for your answer, this is a <img src="https://osqa-ask.wireshark.org/upfiles/Nouvelle_image.jpg" alt="alt text" />screenshot foa a SIP trace , i want to display my msg like that, i mean that the message should be displayed line by line and not on one line.</p><p>tahnk you.</p></div><div id="comment-23281-info" class="comment-info"><span class="comment-age">(23 Jul '13, 05:37)</span> cruz</div></div></div><div id="comment-tools-23270" class="comment-tools"></div><div class="clear"></div><div id="comment-23270-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

