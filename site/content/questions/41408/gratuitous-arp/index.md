+++
type = "question"
title = "Gratuitous ARP"
description = '''Hi, A few questions on Gratuitous ARP (GARP) (I am a network printer):   Lets say I power up on the network:  (a) Do I send out a GARP?  (b) At what point do I do this in the power-up sequence?  (c) Do I do this un-asked-for? Or should I wait for someone (a router, for example) to ask first?    Your...'''
date = "2015-04-13T08:05:00Z"
lastmod = "2015-04-13T12:55:00Z"
weight = 41408
keywords = [ "arp", "homework", "gratuitous" ]
aliases = [ "/questions/41408" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Gratuitous ARP](/questions/41408/gratuitous-arp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41408-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, A few questions on Gratuitous ARP (GARP) (I am a network printer):</p><ol><li><p>Lets say I power up on the network:<br />
(a) Do I send out a GARP?<br />
(b) At what point do I do this in the power-up sequence?<br />
(c) Do I do this un-asked-for? Or should I wait for someone (a router, for example) to ask first?<br />
</p></li><li><p>Your website says "the source and destination IP are both set to the IP of the machine issuing the packet and the destination MAC is the broadcast address ff:ff:ff:ff:ff:ff." However, all the example screen-shots on-line don't seem to do this... Any help in structuring a GARP?</p></li><li><p>I am told that I should send out a GARP when I establish a link...<br />
(a) True?<br />
(b) if so, do I do this un-asked-for?<br />
Or should I wait for someone (a router, for example) to ask first?<br />
</p></li></ol></div><div id="question-tags" class="tags-container tags">arp homework gratuitous</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '15, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/e9e05fc7c9eeb7212b6f17c6a7bdf356?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JayPrab1&#39;s gravatar image" /><p>JayPrab1<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JayPrab1 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Apr '15, 12:25</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></br></p></div></div><div id="comments-container-41408" class="comments-container"><span id="41409"></span><div id="comment-41409" class="comment"><div id="post-41409-score" class="comment-score"></div><div class="comment-text"><p>sounds like homework for me!</p><p>Please post your answers first and then we will help you to get it straight ....</p><p>BTW: Teachers of networking classes are known to monitor this Q&amp;A site!</p></div><div id="comment-41409-info" class="comment-info"><span class="comment-age">(13 Apr '15, 09:41)</span> Kurt Knochner ♦</div></div><span id="41410"></span><div id="comment-41410" class="comment"><div id="post-41410-score" class="comment-score"></div><div class="comment-text"><p>"Please post your answers first and then we will help you to get it straight ...." Not sure I understand this comment... New to this forum, so not familiar with the regs...</p></div><div id="comment-41410-info" class="comment-info"><span class="comment-age">(13 Apr '15, 10:26)</span> JayPrab1</div></div><span id="41411"></span><div id="comment-41411" class="comment"><div id="post-41411-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Not sure I understand this comment... New to this forum, so not familiar with the regs...</p></blockquote><p>It means: I (and probably others here) am <strong>willing to help</strong> you with your questions/homework, but I (and probably others here) am <strong>NOT willing to do the whole homework for you</strong>, by simply answering the questions you should have answered yourself</p><p>;-))</p><p>So, please show what you have done so far to find an answer and post your findings. I (and probably others here) will then comment these findings and your ideas.</p></div><div id="comment-41411-info" class="comment-info"><span class="comment-age">(13 Apr '15, 11:54)</span> Kurt Knochner ♦</div></div><span id="41413"></span><div id="comment-41413" class="comment"><div id="post-41413-score" class="comment-score"></div><div class="comment-text"><p>Fair enough. There is precious little about GARP on-line. I know that something like a Router can broadcast an ARP request to which my NIC (printer) will respond. But, if a device BEYOND the router (not part of the printer's subnet) wants to access the printer, then the router needs to know the printer's MAC address. The question is this: Does the printer send out an unsolicited GARP braodcast? If so, at what point in time does it do so? If not, is it in response to a GARP request ONLY? This is a TIMING issue I am asking about after looking quite exhaustively... Not just laziness... Thanks for your help!</p></div><div id="comment-41413-info" class="comment-info"><span class="comment-age">(13 Apr '15, 12:40)</span> JayPrab1</div></div><span id="41414"></span><div id="comment-41414" class="comment"><div id="post-41414-score" class="comment-score"></div><div class="comment-text"><p>Or, please give me a link to some source of this information, if you can. Thanks!</p></div><div id="comment-41414-info" class="comment-info"><span class="comment-age">(13 Apr '15, 12:48)</span> JayPrab1</div></div></div><div id="comment-tools-41408" class="comment-tools"></div><div class="clear"></div><div id="comment-41408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41415"></span>

<div id="answer-container-41415" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41415-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Or, please give me a link to some source of this information, if you can. Thanks!</p></blockquote><p>I suggest the following videos:</p><p>First ARP:</p><blockquote><p><a href="https://www.youtube.com/watch?v=OZi3tVrpI6U">https://www.youtube.com/watch?v=OZi3tVrpI6U</a><br />
<a href="https://www.youtube.com/watch?v=xTOyZ6TWQdM">https://www.youtube.com/watch?v=xTOyZ6TWQdM</a><br />
</p></blockquote><p>and then Gratuitous ARP:</p><blockquote><p><a href="https://www.youtube.com/watch?v=JPLn6wfAmZY">https://www.youtube.com/watch?v=JPLn6wfAmZY</a><br />
</p></blockquote><p>After the last video ask yourself: When does a <strong>printer</strong> need to send a gratuitous ARP and does it really need it (if so: for what)?</p><p>Further information:</p><blockquote><p><a href="http://networkengineering.stackexchange.com/questions/7713/how-does-gratuitous-arp-work">http://networkengineering.stackexchange.com/questions/7713/how-does-gratuitous-arp-work</a><br />
<a href="https://devcentral.f5.com/questions/gratuitous-arp-how-its-working">https://devcentral.f5.com/questions/gratuitous-arp-how-its-working</a><br />
<a href="http://www.rhyshaden.com/arp.htm">http://www.rhyshaden.com/arp.htm</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '15, 12:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Apr '15, 03:27</p></div></div><div id="comments-container-41415" class="comments-container"><span id="41417"></span><div id="comment-41417" class="comment"><div id="post-41417-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the links, Kurt! Will go thru them.</p></div><div id="comment-41417-info" class="comment-info"><span class="comment-age">(13 Apr '15, 13:14)</span> JayPrab1</div></div></div><div id="comment-tools-41415" class="comment-tools"></div><div class="clear"></div><div id="comment-41415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

