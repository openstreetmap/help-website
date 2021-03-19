+++
type = "question"
title = "About the conversations table"
description = '''Hello everyone, I am writing you about the source code for the conversation table in WireShark. More specifically, I am interested into the function that is in the menu Statistics -&amp;gt; Conversations. I found some source code file under the name conversations_table.c.  Unfortunately, there is a seri...'''
date = "2012-09-10T07:52:00Z"
lastmod = "2012-09-11T01:46:00Z"
weight = 14165
keywords = [ "source-code", "conversations", "table", "conversation" ]
aliases = [ "/questions/14165" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [About the conversations table](/questions/14165/about-the-conversations-table)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14165-score" class="post-score" title="current number of votes">0</div><span id="post-14165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone, I am writing you about the source code for the conversation table in WireShark. More specifically, I am interested into the function that is in the menu Statistics -&gt; Conversations. I found some source code file under the name conversations_table.c. Unfortunately, there is a serious lack of comments, thus making the code impossible to read.</p><p>I would like to ask you, if it is possible, to tell me if this is the source code file for the conversations table?</p><p>If it is, please send me some version with more comments if possible, or maybe explain to me shortly where exactly can I find the part where this conversations are made? I am really interested in this, and I would very much appreciate if you answer me as soon as possible.</p><p>Thank you in advance. Kiril</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-source-code" rel="tag" title="see questions tagged &#39;source-code&#39;">source-code</span> <span class="post-tag tag-link-conversations" rel="tag" title="see questions tagged &#39;conversations&#39;">conversations</span> <span class="post-tag tag-link-table" rel="tag" title="see questions tagged &#39;table&#39;">table</span> <span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '12, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/755cc43ee92b9171108d1438724f5e06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bluzerot&#39;s gravatar image" /><p><span>bluzerot</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bluzerot has no accepted answers">0%</span></p></div></div><div id="comments-container-14165" class="comments-container"></div><div id="comment-tools-14165" class="comment-tools"></div><div class="clear"></div><div id="comment-14165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14168"></span>

<div id="answer-container-14168" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14168-score" class="post-score" title="current number of votes">1</div><span id="post-14168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I would like to ask you, if it is possible, to tell me if this is the source code file for the conversations table?</p></blockquote><p>Yes it is, together with the other conversations_*.c files, which are each just "handlers" for a certain protocol.</p><blockquote><p>If it is, please send me some version with more comments if possible,</p></blockquote><p>I don't think there is a "better/secret" version with more comments other than the code in the official sources. Unfortunately you are right, there is a serious lack of comments.</p><blockquote><p>or maybe explain to me shortly where exactly can I find the part where this conversations are made?</p></blockquote><p>Most of it is in that file. If you choose "Statistics -&gt; Conversations" the 'callback' function <code>init_conversation_notebook_cb()</code> gets called which builds the GUI mask for the conversations.</p><p>The conversations table(s) is/are filled by listeners, which are registered in the files conversations_*.c, like this:</p><p>conversations_ip.c:register_tap_listener_ip_conversation().</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '12, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14168" class="comments-container"><span id="14184"></span><div id="comment-14184" class="comment"><div id="post-14184-score" class="comment-score"></div><div class="comment-text"><p>Thank you Kurt, you have already helped me a lot!</p><p>You said that most of the explanation to where the conversations are made are in conversations_table.c. Can you please tell me in which functions exactly is the algorithm of the conversations?</p><p>Thank you in advance</p><p>Kiril</p></div><div id="comment-14184-info" class="comment-info"><span class="comment-age">(11 Sep '12, 01:46)</span> <span class="comment-user userinfo">bluzerot</span></div></div></div><div id="comment-tools-14168" class="comment-tools"></div><div class="clear"></div><div id="comment-14168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

