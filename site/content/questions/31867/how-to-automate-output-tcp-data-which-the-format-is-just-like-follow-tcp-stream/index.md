+++
type = "question"
title = "how to automate output tcp data which the format is just like Follow TCP Stream?"
description = '''when i click the Follow TCP Stream,wireshark can output entire conversation stream content,i want to how to make wireshark automate output every entire conversation stream content to a file. Is there anyone can give me some advice?'''
date = "2014-04-15T22:23:00Z"
lastmod = "2014-04-21T20:38:00Z"
weight = 31867
keywords = [ "content", "output", "every", "stream", "conversation" ]
aliases = [ "/questions/31867" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to automate output tcp data which the format is just like Follow TCP Stream?](/questions/31867/how-to-automate-output-tcp-data-which-the-format-is-just-like-follow-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31867-score" class="post-score" title="current number of votes">0</div><span id="post-31867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>when i click the Follow TCP Stream,wireshark can output entire conversation stream content,i want to how to make wireshark automate output every entire conversation stream content to a file. Is there anyone can give me some advice?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-content" rel="tag" title="see questions tagged &#39;content&#39;">content</span> <span class="post-tag tag-link-output" rel="tag" title="see questions tagged &#39;output&#39;">output</span> <span class="post-tag tag-link-every" rel="tag" title="see questions tagged &#39;every&#39;">every</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '14, 22:23</strong></p><img src="https://secure.gravatar.com/avatar/885666c057a323159826c414b83eae37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fred&#39;s gravatar image" /><p><span>fred</span><br />
<span class="score" title="26 reputation points">26</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fred has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Apr '14, 22:30</strong> </span></p></div></div><div id="comments-container-31867" class="comments-container"></div><div id="comment-tools-31867" class="comment-tools"></div><div class="clear"></div><div id="comment-31867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31874"></span>

<div id="answer-container-31874" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31874-score" class="post-score" title="current number of votes">1</div><span id="post-31874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fred has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use tshark</p><blockquote><p>tshark -nr input.pcap -z "follow,tcp,ascii,1"</p></blockquote><p>This will print the payload of TCP stream 1 in ASCII. See the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a> for details.</p><p>Or one of the tools listed here</p><blockquote><p><a href="https://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961">https://isc.sans.edu/diary/Tools+for+extracting+files+from+pcaps/6961</a><br />
<a href="http://wiki.wireshark.org/Tools">http://wiki.wireshark.org/Tools</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '14, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-31874" class="comments-container"><span id="31881"></span><div id="comment-31881" class="comment"><div id="post-31881-score" class="comment-score"></div><div class="comment-text"><p>good job. And I have another question that how to know how many TCP streams in a pcap file?</p></div><div id="comment-31881-info" class="comment-info"><span class="comment-age">(16 Apr '14, 05:42)</span> <span class="comment-user userinfo">fred</span></div></div><span id="31994"></span><div id="comment-31994" class="comment"><div id="post-31994-score" class="comment-score">1</div><div class="comment-text"><p>GUI:</p><blockquote><p>Statistics -&gt; Conversations</p></blockquote><p>then look at the TCP tab. The number after the colon is the number of TCP conversations/streams.</p><p>CLI:</p><blockquote><p>tshark -nr input.pcap -q -z conv,tcp</p></blockquote><p>Then count the lines</p></div><div id="comment-31994-info" class="comment-info"><span class="comment-age">(19 Apr '14, 14:48)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="32044"></span><div id="comment-32044" class="comment"><div id="post-32044-score" class="comment-score"></div><div class="comment-text"><p>thanks, it's what i need</p></div><div id="comment-32044-info" class="comment-info"><span class="comment-age">(21 Apr '14, 20:38)</span> <span class="comment-user userinfo">fred</span></div></div></div><div id="comment-tools-31874" class="comment-tools"></div><div class="clear"></div><div id="comment-31874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

