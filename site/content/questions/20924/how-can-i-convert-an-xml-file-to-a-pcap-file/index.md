+++
type = "question"
title = "How can I convert an .xml file to a .pcap file"
description = '''How can I convert an .xml file to a .pcap file,so that I can analyze the protocols I get.'''
date = "2013-05-03T02:42:00Z"
lastmod = "2017-08-17T02:45:00Z"
weight = 20924
keywords = [ "xml", "pcap" ]
aliases = [ "/questions/20924" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I convert an .xml file to a .pcap file](/questions/20924/how-can-i-convert-an-xml-file-to-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20924-score" class="post-score" title="current number of votes">0</div><span id="post-20924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I convert an .xml file to a .pcap file,so that I can analyze the protocols I get.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '13, 02:42</strong></p><img src="https://secure.gravatar.com/avatar/04963e74d6d21997800389c24adb8cc6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kiyomi&#39;s gravatar image" /><p><span>kiyomi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kiyomi has no accepted answers">0%</span></p></div></div><div id="comments-container-20924" class="comments-container"></div><div id="comment-tools-20924" class="comment-tools"></div><div class="clear"></div><div id="comment-20924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20928"></span>

<div id="answer-container-20928" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20928-score" class="post-score" title="current number of votes">0</div><span id="post-20928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That depends on the structure and the content of the XML file. If the XML file contains the raw packet bytes, you could extract those bytes from the XML file and write those bytes in a format that <a href="http://www.wireshark.org/docs/man-pages/text2pcap.html">text2pacp</a> understands. If the XML file contains just application data, there is a lot more to do and then it's probably better not to analyze that data with Wireshark.</p><p>Can you please add some information about the nature and structure of your XML file and who/what generated that file?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '13, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-20928" class="comments-container"><span id="20950"></span><div id="comment-20950" class="comment"><div id="post-20950-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your prompt reply! My project contains a part for tracing the protocols that we use to send some message, I get the stream and then I parse it to List&lt;packet(already defined)=""&gt;. Then I use jSON to post the packets to front page. But now, another requirement appears, I want to get the jSONArray or something else back, and turn it to .xml file, eventually, I wang to convert the xml file to pcap(or some else file formats that the Wireshark can read). Thank you again for your help.Thanks for your prompt reply!The jSONArrays is generated as follows: I use "tshark -T pdml" in linux terminal, and then I parse the inputstream to get the packet I want, then I use dom4j to generate List&lt;packet&gt;, then turn that to jSON. Thank you again for your help.</p></div><div id="comment-20950-info" class="comment-info"><span class="comment-age">(03 May '13, 19:50)</span> <span class="comment-user userinfo">kiyomi</span></div></div><span id="63481"></span><div id="comment-63481" class="comment"><div id="post-63481-score" class="comment-score"></div><div class="comment-text"><p>I have also the same problem can you help me?</p></div><div id="comment-63481-info" class="comment-info"><span class="comment-age">(17 Aug '17, 02:14)</span> <span class="comment-user userinfo">Wegang</span></div></div><span id="63482"></span><div id="comment-63482" class="comment"><div id="post-63482-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/41933/wegang">@Wegang</a>, please open your own question with your xml file rather than trying to piggy-back on to a long dormant older question.</p></div><div id="comment-63482-info" class="comment-info"><span class="comment-age">(17 Aug '17, 02:45)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-20928" class="comment-tools"></div><div class="clear"></div><div id="comment-20928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

