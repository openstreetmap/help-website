+++
type = "question"
title = "Call wireshark 3gpp decoder in a python script"
description = '''Hi , As we already have a 3gpp decoder by wireshark to decode 3gpp messages, I need to call this decoder in my python script to decode a hex dump provided to the program as an input and write the decoded result in a text file. Is there any API for this decoder to use or any other way to do this?'''
date = "2016-04-20T05:43:00Z"
lastmod = "2016-04-20T21:29:00Z"
weight = 51818
keywords = [ "python", "text2pcap", "3gpp", "lte", "wireshark" ]
aliases = [ "/questions/51818" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Call wireshark 3gpp decoder in a python script](/questions/51818/call-wireshark-3gpp-decoder-in-a-python-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51818-score" class="post-score" title="current number of votes">0</div><span id="post-51818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>As we already have a 3gpp decoder by wireshark to decode 3gpp messages, I need to call this decoder in my python script to decode a hex dump provided to the program as an input and write the decoded result in a text file. Is there any API for this decoder to use or any other way to do this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-text2pcap" rel="tag" title="see questions tagged &#39;text2pcap&#39;">text2pcap</span> <span class="post-tag tag-link-3gpp" rel="tag" title="see questions tagged &#39;3gpp&#39;">3gpp</span> <span class="post-tag tag-link-lte" rel="tag" title="see questions tagged &#39;lte&#39;">lte</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '16, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/551d513fdbe07b90802975e8848073e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shayaan_xd&#39;s gravatar image" /><p><span>shayaan_xd</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shayaan_xd has no accepted answers">0%</span></p></div></div><div id="comments-container-51818" class="comments-container"></div><div id="comment-tools-51818" class="comment-tools"></div><div class="clear"></div><div id="comment-51818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51822"></span>

<div id="answer-container-51822" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51822-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51822-score" class="post-score" title="current number of votes">1</div><span id="post-51822-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would say your best bet is to create a pcap file from the hex data and then use tshark to convert the pcap file into a text file containing dissections of the packets. If you have the hex records offline, there is text2pcap which does the first step (hex -&gt; pcap) for you on the command line, or you can do the same using Wireshark (the GUI version).</p><p>If you need to receive and process the hex records live as they come in (which does not seem likely as the required final product is a text file), you'd need to feed text2pcap from a pipe and send its output to tshark using another pipe, and I'm not sure whether this is actually possible. So you might have to replace text2pcap by your Python script doing the same. When capturing from a named pipe, tshark needs the data in pcap format, so you'd have to generate the pcap file header once and then convert the received hex dumps into binary packet data with timestamps. It is not a big deal as the pcap file structure is not complex and it is well documented.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '16, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-51822" class="comments-container"><span id="51826"></span><div id="comment-51826" class="comment"><div id="post-51826-score" class="comment-score"></div><div class="comment-text"><p>Thanks sindy, Can you simplify it more ? I have 100's of hex and i need information of 2 Information elements out of them from each hex.</p></div><div id="comment-51826-info" class="comment-info"><span class="comment-age">(20 Apr '16, 21:14)</span> <span class="comment-user userinfo">shayaan_xd</span></div></div><span id="51827"></span><div id="comment-51827" class="comment"><div id="post-51827-score" class="comment-score">1</div><div class="comment-text"><p>In concept:</p><ul><li>Have the python script 'print' the hex lines to a file</li><li>assuming they're in a format text2pcap understands, you then do a system call to the 'text2pcap' (Wireshark executable) to receive the hex dump and generate an output pcap file</li><li>do a system call to the "tshark" executable (another Wireshark executable, installed typically with Wireshark itself). In that system call, you can make use of tshark's access to Wireshark's dissector intelligence (see the man page, it supports many useful output options, in this case possibly the -T fields and -e flags may be all you need).</li><li>Have the python script use that output as desired.</li><li>Have python unlink/delete the temporary files generated by the script above.</li></ul><p>Aside from that answer you might also consider 'pyshark' instead of the tshark system calls (a python plugin for use of these tools within python).</p></div><div id="comment-51827-info" class="comment-info"><span class="comment-age">(20 Apr '16, 21:29)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-51822" class="comment-tools"></div><div class="clear"></div><div id="comment-51822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

