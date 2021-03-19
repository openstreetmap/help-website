+++
type = "question"
title = "No H.225 in packet &quot;decode as&quot;"
description = '''Hi, When trying to decode a packet, H.225 is not on the list. (H.223 appears twice). How can I decode a packet as H.225? Thanks, Chicco'''
date = "2013-12-29T07:55:00Z"
lastmod = "2013-12-30T12:44:00Z"
weight = 28472
keywords = [ "h.225" ]
aliases = [ "/questions/28472" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No H.225 in packet "decode as"](/questions/28472/no-h225-in-packet-decode-as)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28472-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>When trying to decode a packet, H.225 is not on the list. (H.223 appears twice). How can I decode a packet as H.225?</p><p>Thanks, Chicco</p></div><div id="question-tags" class="tags-container tags">h.225</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '13, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/f9e27c00c34c5a4f011f494a94f3f4c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chicco&#39;s gravatar image" /><p>chicco<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chicco has no accepted answers">0%</span></p></div></div><div id="comments-container-28472" class="comments-container"></div><div id="comment-tools-28472" class="comment-tools"></div><div class="clear"></div><div id="comment-28472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28480"></span>

<div id="answer-container-28480" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28480-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>AFIAK the 'decode as' feature for the transport layer (TCP/UDP) only works if a dissector adds itself to the UDP/TCP port dissector table. Now, the H.225 dissector registers itself for <strong>UDP ports</strong> 1718 and 1719 , so you won't see H.225 in the list of 'decode as' protocols if you try it with TCP ('H.223 is shown twice' indicates that you've tried TCP).</p><p>BTW: Why do you need to decode a TCP frame directly as H.225? Wireshark should be able to detect H.225 if it is used in the right context.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '13, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28480" class="comments-container"><span id="28493"></span><div id="comment-28493" class="comment"><div id="post-28493-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your prompt answer Kurt.</p><p>UDP 1719 is relevant only for RAS messages while H.225 also uses TCP over other ports. One example why need it: There are systems that tunnels all H.323 messages over one port (Security purposes) so WireShark can't decode them and it needs the users input (Decode as) in order to recognize what type is each packet.</p><p>Thanks, Chicco</p></div><div id="comment-28493-info" class="comment-info"><span class="comment-age">(30 Dec '13, 22:06)</span> chicco</div></div></div><div id="comment-tools-28480" class="comment-tools"></div><div class="clear"></div><div id="comment-28480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

