+++
type = "question"
title = "Handling TCP Retransmission in a Wireshark Dissector"
description = '''I&#x27;m working with a Wireshark dissector that interprets an application layer protocol built on top of TCP. I&#x27;m trying to fix a bug in the dissector in which it is trying to reassemble a packet with a TCP retransmitted packet. The retransmitted packet should be ignored because the original has already...'''
date = "2013-09-14T20:20:00Z"
lastmod = "2013-09-15T12:55:00Z"
weight = 24701
keywords = [ "dissector", "retransmission", "tcp" ]
aliases = [ "/questions/24701" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Handling TCP Retransmission in a Wireshark Dissector](/questions/24701/handling-tcp-retransmission-in-a-wireshark-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24701-score" class="post-score" title="current number of votes">0</div><span id="post-24701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working with a Wireshark dissector that interprets an application layer protocol built on top of TCP.</p><p>I'm trying to fix a bug in the dissector in which it is trying to reassemble a packet with a TCP retransmitted packet. The retransmitted packet should be ignored because the original has already been dissected.</p><p>I've stepped through with gdb and looked at the contents of pinfo and pinfo-&gt;fd related to the retransmitted packet, but I couldn't find anything indicating that it is a retransmission.</p><p>I'm sure I'm missing something simple since this must be a common problem. My desperate web searching isn't proving fruitful, but I notice this:</p><p><a href="http://www.wireshark.org/lists/ethereal-dev/200308/msg00466.html">http://www.wireshark.org/lists/ethereal-dev/200308/msg00466.html</a></p><p>Quoting from there:</p><pre><code>Is it to detect retransmissions? If so the TCP itself already have code to do so.</code></pre><p>That makes me hopeful, but what does that mean? What is "the TCP"? Is there some Wireshark TCP library I can call into to see if the bytes from the packet I'm dissecting comes from a TCP retransmission?</p><p>Thanks!</p><hr /><p>Update</p><p>I'm noticing that tcp_dissect_pdus is generally used for such things. If I'm understanding things right, it takes care of retransmission for you automatically, right? Here's my concern, though: my dissector may or may not be called by another dissector between it and tcp which itself would have used tcp_dissect_pdus. Does that preclude me from using it? That is, from the perspective of my dissector, I'm not sure whether I'm on top of this other layer or not and therefore won't know how to indicate to tcp_dissect_pdus how to interpret the application layer data. Perhaps I can indicate the existence of this other layer somehow from the other dissector that may call this one?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '13, 20:20</strong></p><img src="https://secure.gravatar.com/avatar/2e4763f0cc8124d677d249a99800950a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="firebush&#39;s gravatar image" /><p><span>firebush</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="firebush has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Sep '13, 21:00</strong> </span></p></div></div><div id="comments-container-24701" class="comments-container"></div><div id="comment-tools-24701" class="comment-tools"></div><div class="clear"></div><div id="comment-24701-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24722"></span>

<div id="answer-container-24722" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24722-score" class="post-score" title="current number of votes">0</div><span id="post-24722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Up until relatively recently TCP would always call subdissectors even when the packets are retransmitted. But since revision 42774 there has been a preference that controls that: <code>tcp.no_subdissector_on_error</code>.</p><p>The <a href="https://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=42774">commit message</a> for that revision explains at length why it's done this way and why the preference was put in. There does not appear to be a way to set this behavior programatically (i.e., from your dissector) however.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '13, 12:55</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-24722" class="comments-container"></div><div id="comment-tools-24722" class="comment-tools"></div><div class="clear"></div><div id="comment-24722-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

