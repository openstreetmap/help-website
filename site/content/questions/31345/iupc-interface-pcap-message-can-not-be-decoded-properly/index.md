+++
type = "question"
title = "Iupc interface PCAP message can not be decoded properly."
description = '''Hi, I am trying to decode Iupc interface, PCAP messages (Position Calculation Request), but its not showing some field. Was wondering, if any special filter has to be added for the same. Regards, Saurabh'''
date = "2014-04-01T06:29:00Z"
lastmod = "2014-04-02T07:35:00Z"
weight = 31345
keywords = [ "iupc", "pcap", "decoding" ]
aliases = [ "/questions/31345" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Iupc interface PCAP message can not be decoded properly.](/questions/31345/iupc-interface-pcap-message-can-not-be-decoded-properly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31345-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to decode Iupc interface, PCAP messages (Position Calculation Request), but its not showing some field. Was wondering, if any special filter has to be added for the same.</p><p>Regards, Saurabh</p></div><div id="question-tags" class="tags-container tags">iupc pcap decoding</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '14, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/313258c6096222395df57b12e1a1b37c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="saurabhkalra&#39;s gravatar image" /><p>saurabhkalra<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="saurabhkalra has no accepted answers">0%</span></p></div></div><div id="comments-container-31345" class="comments-container"><span id="31350"></span><div id="comment-31350" class="comment"><div id="post-31350-score" class="comment-score"></div><div class="comment-text"><p>Might be a bug or new fields Wireshark can't handle - impossible to say whithout having the .pcap file.</p></div><div id="comment-31350-info" class="comment-info"><span class="comment-age">(01 Apr '14, 09:09)</span> Anders ♦</div></div><span id="31368"></span><div id="comment-31368" class="comment"><div id="post-31368-score" class="comment-score"></div><div class="comment-text"><p>How can i send traces? anywhere i can upload?</p><p>Regards, Saurabh</p></div><div id="comment-31368-info" class="comment-info"><span class="comment-age">(02 Apr '14, 00:32)</span> saurabhkalra</div></div><span id="31369"></span><div id="comment-31369" class="comment"><div id="post-31369-score" class="comment-score"></div><div class="comment-text"><p>The best would be to open a bug at <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a></p></div><div id="comment-31369-info" class="comment-info"><span class="comment-age">(02 Apr '14, 01:28)</span> Anders ♦</div></div><span id="31370"></span><div id="comment-31370" class="comment"><div id="post-31370-score" class="comment-score"></div><div class="comment-text"><p>But it seems a configuration issue as one of my colleague with same version of wireshark is able to open and decode the message properly. I can not see some of the parameters.</p></div><div id="comment-31370-info" class="comment-info"><span class="comment-age">(02 Apr '14, 01:32)</span> saurabhkalra</div></div><span id="31372"></span><div id="comment-31372" class="comment"><div id="post-31372-score" class="comment-score"></div><div class="comment-text"><p>dropbox, cloudshark? Have you compared your preferences with your colleagues. Diff the profiles maybe? Do you use the same version? What "paramters" can't you see? Paste a picture?</p></div><div id="comment-31372-info" class="comment-info"><span class="comment-age">(02 Apr '14, 01:59)</span> Anders ♦</div></div><span id="31373"></span><div id="comment-31373" class="comment not_top_scorer"><div id="post-31373-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/saurabh.jpg" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/WireSharkSnapShot.JPG" alt="alt text" /></p><p>Here I am postiong the pictures. saurabh.jpg is the pic from my computer and WireSharkSnapShot.jpg is pic of my colleague's PC.</p><p>Regards, Saurabh</p></div><div id="comment-31373-info" class="comment-info"><span class="comment-age">(02 Apr '14, 02:09)</span> saurabhkalra</div></div></div><div id="comment-tools-31345" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-31345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31392"></span>

<div id="answer-container-31392" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31392-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a "bug" in Wireshark none of you are seeing the extensionValue if you go to preferences-&gt;protocols-&gt;per and untick show internal PER fields. I think your output will look the same. If you can attach a small trace to a bug report I could verify a fix.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></img></div></div><div id="comments-container-31392" class="comments-container"><span id="31393"></span><div id="comment-31393" class="comment"><div id="post-31393-score" class="comment-score"></div><div class="comment-text"><p>Thank you, it really solved the issue I am facing... Thanks a lot!!!</p></div><div id="comment-31393-info" class="comment-info"><span class="comment-age">(02 Apr '14, 07:39)</span> saurabhkalra</div></div><span id="31397"></span><div id="comment-31397" class="comment"><div id="post-31397-score" class="comment-score"></div><div class="comment-text"><p>From FAQ What if I get a good answer?</p><p>Please accept it by clicking on the check mark next to the answer. :-)</p></div><div id="comment-31397-info" class="comment-info"><span class="comment-age">(02 Apr '14, 08:55)</span> Anders ♦</div></div><span id="31399"></span><div id="comment-31399" class="comment"><div id="post-31399-score" class="comment-score"></div><div class="comment-text"><p>An even better response would be: "Here's the capture that shows the problem".</p></div><div id="comment-31399-info" class="comment-info"><span class="comment-age">(02 Apr '14, 08:58)</span> grahamb ♦</div></div><span id="31400"></span><div id="comment-31400" class="comment"><div id="post-31400-score" class="comment-score"></div><div class="comment-text"><p>I checked in a potential fix in v1.11.3-rc1-2201-g9410882 you could try a development build once it finishes.</p></div><div id="comment-31400-info" class="comment-info"><span class="comment-age">(02 Apr '14, 09:00)</span> Anders ♦</div></div></div><div id="comment-tools-31392" class="comment-tools"></div><div class="clear"></div><div id="comment-31392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

