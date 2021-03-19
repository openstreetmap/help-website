+++
type = "question"
title = "How to exactly analyze a packet?"
description = '''Hi guys, so the real purpose of this program is to analyze a packet right? to determine network problems, test network security, and many other more, and i think this is really intended for those who want or is a network analyst. I just want to ask HOW DO YOU EXACTLY ANALYZE A PACKET? Like, i see a ...'''
date = "2014-02-11T04:20:00Z"
lastmod = "2014-02-11T06:56:00Z"
weight = 29685
keywords = [ "howtoanalyze", "newbie", "analysis" ]
aliases = [ "/questions/29685" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to exactly analyze a packet?](/questions/29685/how-to-exactly-analyze-a-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29685-score" class="post-score" title="current number of votes">0</div><span id="post-29685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, so the real purpose of this program is to analyze a packet right? to determine network problems, test network security, and many other more, and i think this is really intended for those who want or is a network analyst. I just want to ask HOW DO YOU EXACTLY ANALYZE A PACKET? Like, i see a UDP or TCP protocol packet, if i open it, what would i read, or what is my aim to understand each of the line? Im really a noob here.. i passed through the "user guide" but it seems it only teaches on how to navigate the wireshark specially the user interface, i can't really find the "ways" or "aims" or i dont really know what to call it, but i cant really find the thing to look for in packet to analyze it. Sorry, for example, i want to know why my network is in very slow download, what would i do to analyze it in wireshark? Sorry to ask guys, but im really eager to learn this, i love networks too, im still a student and i only learned the basics. Hopefully you could help thank you so much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-howtoanalyze" rel="tag" title="see questions tagged &#39;howtoanalyze&#39;">howtoanalyze</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/c97c18dbcf85a8509b636dc12c024a3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="newb&#39;s gravatar image" /><p><span>newb</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="newb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '14, 05:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-29685" class="comments-container"></div><div id="comment-tools-29685" class="comment-tools"></div><div class="clear"></div><div id="comment-29685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29690"></span>

<div id="answer-container-29690" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29690-score" class="post-score" title="current number of votes">2</div><span id="post-29690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Like, i see a UDP or TCP protocol packet, if i open it, <strong>what would i read, or what is my aim to understand each of the line</strong>?</p></blockquote><p>Wireshark is just a tool to view the content of the packets in a certain form (dissected into records/fields). However, without a solid understanding of the typical protocols, it won't help you very much, as you can't interpret the output of Wireshark.</p><p>So, if you want to understand the content of the packets, the first step would be to get a solid understanding of the typical protocols (ethernet, ip, tcp, udp, http and many more). Here are some resources to start with:</p><p><strong>Books:</strong><br />
</p><ul><li><strong><a href="http://www.amazon.com/TCP-Illustrated-Vol-Addison-Wesley-Professional/dp/0201633469/ref=sr_1_1?ie=UTF8&amp;qid=1296828460&amp;sr=8-1">TCP/IP Illustrated (Volume 1)</a></strong> still the best resource to start with<br />
</li><li><strong><a href="http://www.wiresharkbook.com/">The Wireshark book</a></strong></li></ul><p>There obviously other books about networking. google will help: 'books networking'.</p><p><strong>Online resources:</strong><br />
</p><ul><li><strong><a href="http://en.wikipedia.org/wiki/Transmission_Control_Protocol">TCP on Wikipedia</a></strong><br />
</li><li><strong><a href="http://www.tcpipguide.com/index.htm">The TCP/IP guide</a></strong><br />
</li></ul><p>There are also some video tutorials about Wireshark on Youtube (<strong><a href="http://www.youtube.com/results?search_query=wireshark%20tutorial">http://www.youtube.com/results?search_query=wireshark%20tutorial</a></strong> - Hint: Please open the link in a separate browser window/tab manually, if clicking the link in your browser does not work).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '14, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '14, 06:53</strong> </span></p></div></div><div id="comments-container-29690" class="comments-container"><span id="29698"></span><div id="comment-29698" class="comment"><div id="post-29698-score" class="comment-score">2</div><div class="comment-text"><p>When's the KK "Answers to all networking questions" book coming out?</p></div><div id="comment-29698-info" class="comment-info"><span class="comment-age">(11 Feb '14, 06:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="29700"></span><div id="comment-29700" class="comment"><div id="post-29700-score" class="comment-score">1</div><div class="comment-text"><p>Never. You neither get rich nor famous with those kind of books these days, unless you manage somehow to include vampires or other 'interesting aspects of life' into the 'protocol story' ;-)</p><p>Maybe something like this, would attract the nerd hordes...</p><ul><li>Twilight, and the shades of green in the dark corners of the switch panel</li><li>Twilight #2, and the raise of the ping</li><li>From egress til drop - the story of a packets short life</li></ul><p>Maybe a networking book with some nice ladies, covered only by a whiff of bits and bytes on every second page, would work as well....</p></div><div id="comment-29700-info" class="comment-info"><span class="comment-age">(11 Feb '14, 06:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29690" class="comment-tools"></div><div class="clear"></div><div id="comment-29690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

