+++
type = "question"
title = "need part of data only"
description = '''greetings  when i display data as text it shows &#92;x011119 032914 121638 10 49.2768 49.2781 056.4940 0.3094 i want to make column shows only 121638 10 ??? i tried in column reference but it didnt work '''
date = "2014-03-30T12:45:00Z"
lastmod = "2014-04-02T14:25:00Z"
weight = 31295
keywords = [ "column", "custom" ]
aliases = [ "/questions/31295" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [need part of data only](/questions/31295/need-part-of-data-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31295-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>greetings when i display data as text it shows \x011119 032914 121638 10 49.2768 49.2781 056.4940 0.3094</p><p>i want to make column shows only 121638 10 ???</p><p>i tried in column reference but it didnt work</p></div><div id="question-tags" class="tags-container tags">column custom</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '14, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/583f60448e616e6c6f8408eb6620006a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shady&#39;s gravatar image" /><p>shady<br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shady has no accepted answers">0%</span></p></div></div><div id="comments-container-31295" class="comments-container"><span id="31297"></span><div id="comment-31297" class="comment"><div id="post-31297-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, but your description is not really helpful to understand your problem. So, if you are interested in a meaningful answer, please add much more details.</p><ul><li>what is the protocol</li><li>is it your own dissector or a standard one</li><li>can you post a sample capture file on cloudshark.org</li></ul></div><div id="comment-31297-info" class="comment-info"><span class="comment-age">(30 Mar '14, 14:11)</span> Kurt Knochner ♦</div></div><span id="31299"></span><div id="comment-31299" class="comment"><div id="post-31299-score" class="comment-score"></div><div class="comment-text"><p>first of all thank you for response i sorry i cannot upload the file its too large but while iam uploading the file this snapshot can show what i mean <img src="https://osqa-ask.wireshark.org/upfiles/111.jpg" alt="alt text" /></p></div><div id="comment-31299-info" class="comment-info"><span class="comment-age">(30 Mar '14, 17:01)</span> shady</div></div><span id="31309"></span><div id="comment-31309" class="comment"><div id="post-31309-score" class="comment-score"></div><div class="comment-text"><p>O.K some more questions:</p><ul><li>what kind of protocol is that?</li><li>do you really need the <strong>ASCII</strong> representation of some payload bytes, in your case (121638 10)?</li><li>are those bytes always at the same location?</li><li>do you need that as a <strong>column</strong> in Wireshark, or would it be sufficient to get text output with tshark?</li></ul></div><div id="comment-31309-info" class="comment-info"><span class="comment-age">(31 Mar '14, 01:53)</span> Kurt Knochner ♦</div></div><span id="31311"></span><div id="comment-31311" class="comment"><div id="post-31311-score" class="comment-score"></div><div class="comment-text"><p>sorry again if my questions are not clear i will try harder to be clear</p><p>its data protocol and here its page in wireshark site <a href="http://wiki.wireshark.org/Protocols/data">http://wiki.wireshark.org/Protocols/data</a></p><p>yes the are at same location every time</p><p>yes i need that as a column and if its possible to get text output it will be great</p><p>thank you very much</p></div><div id="comment-31311-info" class="comment-info"><span class="comment-age">(31 Mar '14, 03:31)</span> shady</div></div><span id="31358"></span><div id="comment-31358" class="comment"><div id="post-31358-score" class="comment-score"></div><div class="comment-text"><p>any information yet??</p></div><div id="comment-31358-info" class="comment-info"><span class="comment-age">(01 Apr '14, 13:43)</span> shady</div></div></div><div id="comment-tools-31295" class="comment-tools"></div><div class="clear"></div><div id="comment-31295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31443"></span>

<div id="answer-container-31443" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31443-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>its data protocol and here its page in wireshark site <a href="http://wiki.wireshark.org/Protocols/data">http://wiki.wireshark.org/Protocols/data</a></p></blockquote><p>'data' isn't a 'protocol'. It's just a way for Wireshark to show payload data, if there is no dissector available for that specific protocol.</p><blockquote><p>yes the are at same location every time</p></blockquote><p>good.</p><blockquote><p>yes i need that as a column and if its possible to get text output it will be great</p></blockquote><p>O.K. now comes the 'bad' news: You'll have to write a dissector for that to happen in Wireshark. Within a dissector you can defined protocol fields and you can expose them in a way to be able to use those fields as a source for column data in Wireshark.</p><p>Please read the developer docs how to write a dissector.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div></div><div id="comments-container-31443" class="comments-container"><span id="31466"></span><div id="comment-31466" class="comment"><div id="post-31466-score" class="comment-score"></div><div class="comment-text"><p>Usual plug: Or see my presentation from sharkFest'13 (to be reprised at SF'14) on 3 ways to write a dissector: <a href="http://sharkfest.wireshark.org/sharkfest.13/presentations/PA-10_Writing-a-Wireshark-Dissector_Graham-Bloice.zip">http://sharkfest.wireshark.org/sharkfest.13/presentations/PA-10_Writing-a-Wireshark-Dissector_Graham-Bloice.zip</a></p></div><div id="comment-31466-info" class="comment-info"><span class="comment-age">(03 Apr '14, 02:45)</span> grahamb ♦</div></div><span id="31468"></span><div id="comment-31468" class="comment"><div id="post-31468-score" class="comment-score"></div><div class="comment-text"><p>thank you very much for your help</p><p>i will try to write it</p><p>i will be back</p></div><div id="comment-31468-info" class="comment-info"><span class="comment-age">(03 Apr '14, 02:53)</span> shady</div></div></div><div id="comment-tools-31443" class="comment-tools"></div><div class="clear"></div><div id="comment-31443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

