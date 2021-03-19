+++
type = "question"
title = "Tool to identify unanswered SIP messages"
description = '''Hi,  I would like to know if any tool (a script or whatever) exists that identifies all the SIP messages, from a pcap file, which were send to a specific IP Address that where not replied.  For example, for SIP protocol, this script would check all the INVITE messages that were not replying back. Fo...'''
date = "2014-04-21T10:00:00Z"
lastmod = "2014-04-23T12:17:00Z"
weight = 32031
keywords = [ "sip" ]
aliases = [ "/questions/32031" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tool to identify unanswered SIP messages](/questions/32031/tool-to-identify-unanswered-sip-messages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32031-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to know if any tool (a script or whatever) exists that identifies all the SIP messages, from a pcap file, which were send to a specific IP Address that where not replied.</p><p>For example, for SIP protocol, this script would check all the INVITE messages that were not replying back. For this case, the tool will check if any '100 Trying' message was send back for each INVITE message.</p><p>This would help when analyzing huge wireshark traces with hundreds of thousands packets.</p><p>I could develop my own script but if a similar solution already exists I would use it.</p><p>Thank you in advance. BR, Catarina</p></div><div id="question-tags" class="tags-container tags">sip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '14, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/25554d4215a038f8afe1305315f61f4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Catarina&#39;s gravatar image" /><p>Catarina<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Catarina has no accepted answers">0%</span></p></div></div><div id="comments-container-32031" class="comments-container"></div><div id="comment-tools-32031" class="comment-tools"></div><div class="clear"></div><div id="comment-32031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32074"></span>

<div id="answer-container-32074" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32074-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds like (Yet Another) job for <a href="http://wiki.wireshark.org/Mate">MATE</a>. That's a pain to set up and use, but I'd guess you could do something like:</p><ol><li>Create PDUs for SIP messages</li><li>Create Gops (Groups of Packets) which contain requests + responses</li><li>Filter on "<code>mate.[your_gop_name].NumOfPdus == 1</code>"</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '14, 18:00</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-32074" class="comments-container"><span id="32140"></span><div id="comment-32140" class="comment"><div id="post-32140-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Thank you. I didn't know MATE. It's an incredible tool. It helped to solve my problem. Just followed the steps you mentioned above.</p><p>Regards.</p></div><div id="comment-32140-info" class="comment-info"><span class="comment-age">(24 Apr '14, 02:31)</span> Catarina</div></div><span id="32154"></span><div id="comment-32154" class="comment"><div id="post-32154-score" class="comment-score"></div><div class="comment-text"><p>Great, you're welcome!</p><p>As this is a Q&amp;A site it's useful if you can "accept" an answer by clicking on the checkbox next to it (assuming it answered your question). See the FAQ for details.</p></div><div id="comment-32154-info" class="comment-info"><span class="comment-age">(24 Apr '14, 11:41)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-32074" class="comment-tools"></div><div class="clear"></div><div id="comment-32074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32121"></span>

<div id="answer-container-32121" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32121-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I believe the following tool could be interesting for you.</p><blockquote><p><a href="https://code.google.com/p/sipana/">https://code.google.com/p/sipana/</a></p></blockquote><p><strong>However:</strong> This is not just a small scripted solution. So, it's probably only worth trying if you have to analyze a lot of SIP calls day by day.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32121" class="comments-container"></div><div id="comment-tools-32121" class="comment-tools"></div><div class="clear"></div><div id="comment-32121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

