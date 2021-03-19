+++
type = "question"
title = "how to dissect bytearray of tcp payload"
description = '''i have ByteArray of TCP payload (diameter message),(using getByteArray API on Diameter request message) now i want to dissect and print the diameter data. i have looked into the code of wireshark, could not find any way to do it. please suggest some way to do it. thanks'''
date = "2014-03-25T04:44:00Z"
lastmod = "2014-04-04T09:23:00Z"
weight = 31149
keywords = [ "bytearray", "diameter", "dissector", "libwireshark" ]
aliases = [ "/questions/31149" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to dissect bytearray of tcp payload](/questions/31149/how-to-dissect-bytearray-of-tcp-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31149-score" class="post-score" title="current number of votes">0</div><span id="post-31149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>i have ByteArray of TCP payload (diameter message),(using getByteArray API on Diameter request message)</p><p>now i want to dissect and print the diameter data.</p><p>i have looked into the code of wireshark, could not find any way to do it.</p><p>please suggest some way to do it.</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bytearray" rel="tag" title="see questions tagged &#39;bytearray&#39;">bytearray</span> <span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-libwireshark" rel="tag" title="see questions tagged &#39;libwireshark&#39;">libwireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '14, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p><span>Sanny_D</span><br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-31149" class="comments-container"><span id="31150"></span><div id="comment-31150" class="comment"><div id="post-31150-score" class="comment-score"></div><div class="comment-text"><p>What's wrong with the built in dissector? You can add your own .xml files to dissect vendor AVPs.</p></div><div id="comment-31150-info" class="comment-info"><span class="comment-age">(25 Mar '14, 05:50)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="31161"></span><div id="comment-31161" class="comment"><div id="post-31161-score" class="comment-score"></div><div class="comment-text"><p>my question did not sound clear, sorry for that.</p><p>i am not using wireshark directly,actually, i have written a C code to dissect network packet,</p><p>on the C++ Diameter request object i called getByteArray API and stored it in a memory area, clearly it doesnt contain ether,ip,tcp/udp header information.</p><p>now i want to dissect this ByteArray using wireshark API.</p><p>how to do it.</p></div><div id="comment-31161-info" class="comment-info"><span class="comment-age">(25 Mar '14, 22:44)</span> <span class="comment-user userinfo">Sanny_D</span></div></div><span id="31163"></span><div id="comment-31163" class="comment"><div id="post-31163-score" class="comment-score"></div><div class="comment-text"><p>See if I got this right, you have extracted the bytes of a Diameter PDU into a buffer in your program and now you want to use Wiresharks code as a library to "dissect" these bytes by calling some API in libwireshark? I'm not sure that would be trivial.</p></div><div id="comment-31163-info" class="comment-info"><span class="comment-age">(26 Mar '14, 01:57)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="31214"></span><div id="comment-31214" class="comment"><div id="post-31214-score" class="comment-score"></div><div class="comment-text"><p>this is exactly what i want to do. using libwireshark i have done dissection of pcap packets (whole) before, but coudnt find a way to directly dissect ByteArray. is this possible</p></div><div id="comment-31214-info" class="comment-info"><span class="comment-age">(27 Mar '14, 04:54)</span> <span class="comment-user userinfo">Sanny_D</span></div></div></div><div id="comment-tools-31149" class="comment-tools"></div><div class="clear"></div><div id="comment-31149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31511"></span>

<div id="answer-container-31511" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31511-score" class="post-score" title="current number of votes">0</div><span id="post-31511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Sanny_D has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>have done it using wireshark dissector code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '14, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p><span>Sanny_D</span><br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-31511" class="comments-container"><span id="31516"></span><div id="comment-31516" class="comment"><div id="post-31516-score" class="comment-score"></div><div class="comment-text"><p>hm.. answering your own question with a status update and accepting that, isn't exactly how this site works. Please read the FAQ:</p><blockquote><p><a href="http://ask.wireshark.org/faq/">http://ask.wireshark.org/faq/</a></p></blockquote></div><div id="comment-31516-info" class="comment-info"><span class="comment-age">(04 Apr '14, 08:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31519"></span><div id="comment-31519" class="comment"><div id="post-31519-score" class="comment-score"></div><div class="comment-text"><p>dint find this in faq, well,i it did on purpose, so that it can help others,</p></div><div id="comment-31519-info" class="comment-info"><span class="comment-age">(04 Apr '14, 09:23)</span> <span class="comment-user userinfo">Sanny_D</span></div></div></div><div id="comment-tools-31511" class="comment-tools"></div><div class="clear"></div><div id="comment-31511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31233"></span>

<div id="answer-container-31233" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31233-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31233-score" class="post-score" title="current number of votes">1</div><span id="post-31233-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but coudnt find a way to directly dissect ByteArray. is this possible</p></blockquote><p>as I see it, you have the following options:</p><ul><li>write your own dissector code, without the help of Wireshark code</li><li>use a pcap library (either C++ or another language with interface code) that provides Diameter support, like jnetpcap. Maybe you can borrow from <a href="http://code.google.com/p/libcrafter/">libcrafter</a>.</li><li>use the code of the Wireshark Diameter dissector as an example to write your own code. I guess that's rather hard, as the Diameter dissector code is not exactly the easiest dissector of all.</li><li>'dump' your byte array into a dummy frame (eth/ip/udp), similar to <a href="http://www.wireshark.org/docs/man-pages/text2pcap.html">text2pcap</a>, then call tshark on the generated pcap file, parse the output of tshark and use the results in your code</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '14, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31233" class="comments-container"><span id="31306"></span><div id="comment-31306" class="comment"><div id="post-31306-score" class="comment-score"></div><div class="comment-text"><p>thanks kurt!</p><p>what i am trying to do is , calling</p><p>dissect_diameter_tcp (tvb,pinfo, tree))</p><p>API with each argument initialized with required values, is this correct approach, i am not sure if i can populate these structures with correct values.</p></div><div id="comment-31306-info" class="comment-info"><span class="comment-age">(30 Mar '14, 22:16)</span> <span class="comment-user userinfo">Sanny_D</span></div></div></div><div id="comment-tools-31233" class="comment-tools"></div><div class="clear"></div><div id="comment-31233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

