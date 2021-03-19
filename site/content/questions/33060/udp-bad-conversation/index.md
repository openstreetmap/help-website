+++
type = "question"
title = "UDP bad conversation"
description = '''Dear all, I&#x27;m working with a capture and I would like to classify UDP conversations in two groups. One group with all UDP conversations that finish right and another group with UDP conversations that don&#x27;t finish. How can I do it? Thanks in advance.'''
date = "2014-05-25T10:32:00Z"
lastmod = "2014-05-25T11:35:00Z"
weight = 33060
keywords = [ "udp" ]
aliases = [ "/questions/33060" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [UDP bad conversation](/questions/33060/udp-bad-conversation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33060-score" class="post-score" title="current number of votes">0</div><span id="post-33060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear all,</p><p>I'm working with a capture and I would like to classify UDP conversations in two groups. One group with all UDP conversations that finish right and another group with UDP conversations that don't finish. How can I do it?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 May '14, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/e7791a76dfd358e21aa3ce09047c0c03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="meri&#39;s gravatar image" /><p><span>meri</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="meri has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 May '14, 10:35</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-33060" class="comments-container"><span id="33061"></span><div id="comment-33061" class="comment"><div id="post-33061-score" class="comment-score"></div><div class="comment-text"><p>What's your definition of "finish right" ?</p></div><div id="comment-33061-info" class="comment-info"><span class="comment-age">(25 May '14, 10:36)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="33062"></span><div id="comment-33062" class="comment"><div id="post-33062-score" class="comment-score"></div><div class="comment-text"><p>With no errors. I tried to search icmp and then destinations unreachables but I don't know if all icmp mean a wrong UDP conversation or not, for example time exceed.</p></div><div id="comment-33062-info" class="comment-info"><span class="comment-age">(25 May '14, 10:44)</span> <span class="comment-user userinfo">meri</span></div></div><span id="33063"></span><div id="comment-33063" class="comment"><div id="post-33063-score" class="comment-score"></div><div class="comment-text"><p>UDP is not connection oriented, so its up to the application to determine if successful communication was achieved. What application are you talking about?</p></div><div id="comment-33063-info" class="comment-info"><span class="comment-age">(25 May '14, 10:45)</span> <span class="comment-user userinfo">Rooster_50</span></div></div><span id="33066"></span><div id="comment-33066" class="comment"><div id="post-33066-score" class="comment-score"></div><div class="comment-text"><p>I'm thinking about and I think that is better to say that I'm looking UDP established conversations and no established. I hope you understand me.</p></div><div id="comment-33066-info" class="comment-info"><span class="comment-age">(25 May '14, 11:03)</span> <span class="comment-user userinfo">meri</span></div></div></div><div id="comment-tools-33060" class="comment-tools"></div><div class="clear"></div><div id="comment-33060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33068"></span>

<div id="answer-container-33068" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33068-score" class="post-score" title="current number of votes">2</div><span id="post-33068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm thinking about and I think that is better to say that I'm looking UDP established conversations and no established. I hope you understand me.</p></blockquote><p>There are <strong>no</strong> 'established' connections in UDP, as the protocol has no session establishment process. The client just sends data to the server within the first frame (and vice versa), so that's totally different than the TCP 3-way handshake (SYN,SYN-ACK,ACK).</p><p>There might be a protocol on top of UDP that uses some kind of 'session concept'. As you did not mention that, I cannot give any good advice in that direction.</p><p>So, to answer your question: You cannot filter for 'established' UDP connections, as there is no concept of an 'established connection' in UDP. Therefore, there is <strong>no way</strong> to filter for what you are asking, unless you can add some details about the protocol used on top of UDP (if there is one), like DNS, DTLS, etc. In some cases, you could then at least filter if you've ever received an answer for a certain request, which could be treated as a kind of an indicator for something like an 'established session'.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 May '14, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 May '14, 11:37</strong> </span></p></div></div><div id="comments-container-33068" class="comments-container"></div><div id="comment-tools-33068" class="comment-tools"></div><div class="clear"></div><div id="comment-33068-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

