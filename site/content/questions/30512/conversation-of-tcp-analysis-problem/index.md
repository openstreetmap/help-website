+++
type = "question"
title = "Conversation of tcp analysis problem"
description = '''When I choose local connection or wireless, it is confused that the wireshark can not capture a whole conversion that including packages of two direction. My implements are as follows: 1.double click to start wireshark  2.select local connection and click start 3.select &#x27;Statistics-&amp;gt;Conversations...'''
date = "2014-03-06T17:41:00Z"
lastmod = "2014-03-10T23:25:00Z"
weight = 30512
keywords = [ "conversation", "statistics", "tcp" ]
aliases = [ "/questions/30512" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Conversation of tcp analysis problem](/questions/30512/conversation-of-tcp-analysis-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30512-score" class="post-score" title="current number of votes">0</div><span id="post-30512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I choose local connection or wireless, it is confused that the wireshark can not capture a whole conversion that including packages of two direction. My implements are as follows:</p><pre><code>1.double click to start wireshark 
2.select local connection and click start
3.select &#39;Statistics-&gt;Conversations&#39; to display conversion window
4.select TCP, then I start analsis</code></pre><p>The problem are that I want to watch the conversations displayed in step 4 that including both dirtctions(say both "package A-&gt;B" and "package B-&gt;A" is not zero), but the reality is that there is no such conversitions in my machine, and in other machines it displays well.</p><p>Please tell me how to slove this problem,thanks.</p><p>other info:</p><pre><code>My Pc is win7 32bit,Thinkpad E520, Realtek PCIe GBE Family Controller,
the wireshark version is 1.10.5 .</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '14, 17:41</strong></p><img src="https://secure.gravatar.com/avatar/0e0959fd006f49be421608b75fe22f6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevselect&#39;s gravatar image" /><p><span>nevselect</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevselect has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Mar '14, 03:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-30512" class="comments-container"></div><div id="comment-tools-30512" class="comment-tools"></div><div class="clear"></div><div id="comment-30512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30614"></span>

<div id="answer-container-30614" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30614-score" class="post-score" title="current number of votes">1</div><span id="post-30614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><strong>I want to watch the conversations</strong> displayed in step 4 that <strong>including both dirtctions</strong>(say both "package A-&gt;B" and "package B-&gt;A" is not zero), but the reality is that <strong>there is no such conversations in my machine</strong>, and in other machines it displays well.</p></blockquote><p>O.K. As I understand your problem:</p><ul><li>you have two capturing systems</li><li>on one system, you see traffic in both directions</li><li>on the other system, you see only traffic in one direction (no packets show in the Conversations for either A-&gt;B or B-&gt;A)</li></ul><p>If that assumption is correct, here are some possible problems</p><ul><li>You are trying to capture wifi traffic on Windows. That has some limitations on its own, but I don't think that's your main problem</li><li>You are try to capture on the 'local connection' and I guess you mean the Ethernet interface (Realtek). In that case you might have hit the same problem that others have also reported, namely you either don't see incoming or outgoing traffic.</li></ul><p>As we have had some (a lot of) reports about problems with outgoing packets, here are some common problems, starting with the most plausible ones:</p><ul><li>There is some Endpoint Security Software installed on the system, that prevents Wireshark from seeing <strong>outgoing</strong> packets. The software that was mentioned most was <strong>Symantec Endpoint Security</strong>. If that is installed on your system, try to disable to uninstall it. If that is not an option, you cannot use that specific system to capture traffic of the local machine.</li><li>Another problem could be a VPN client with a special network driver called <strong>DNE LightWeight Filter</strong>. If that is the case, <strong>uncheck</strong> DNE LightWeight Filter in the adapter settings.</li><li>There could be other <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">interfering software</a> on the system like AV, IDS, Firewall, Networking software, etc. If that's the case, try to disable or uninstall that software.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '14, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30614" class="comments-container"><span id="30675"></span><div id="comment-30675" class="comment"><div id="post-30675-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot. I try to slove the problems in the ways you give, and it works!</p></div><div id="comment-30675-info" class="comment-info"><span class="comment-age">(10 Mar '14, 23:25)</span> <span class="comment-user userinfo">nevselect</span></div></div></div><div id="comment-tools-30614" class="comment-tools"></div><div class="clear"></div><div id="comment-30614-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

