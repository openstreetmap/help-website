+++
type = "question"
title = "ssl_print_string in Wireshark"
description = '''I&#x27;d like to know what the function does in line 1165 of this link. it is ssl_print_string(a, b) function in packe-ssl-utils.h file. I&#x27;ve seen it is been called in several places where it was given a string as a first argument and a variable as the second one. However, I&#x27;m not able to tell from the c...'''
date = "2014-11-10T09:57:00Z"
lastmod = "2014-11-11T02:51:00Z"
weight = 37733
keywords = [ "development", "ssl", "function", "wireshark" ]
aliases = [ "/questions/37733" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [ssl\_print\_string in Wireshark](/questions/37733/ssl_print_string-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37733-score" class="post-score" title="current number of votes">0</div><span id="post-37733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to know what the function does in <strong>line 1165</strong> of this <a href="http://fossies.org/dox/wireshark-1.12.1/packet-ssl-utils_8h_source.html#l01165">link</a>. it is <strong>ssl_print_string(a, b)</strong> function in <strong>packe-ssl-utils.h</strong> file. I've seen it is been called in several places where it was given a string as a first argument and a variable as the second one. However, I'm not able to tell from the context what it does and not able to find its body (if it has one!).</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-function" rel="tag" title="see questions tagged &#39;function&#39;">function</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '14, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div></div><div id="comments-container-37733" class="comments-container"></div><div id="comment-tools-37733" class="comment-tools"></div><div class="clear"></div><div id="comment-37733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37735"></span>

<div id="answer-container-37735" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37735-score" class="post-score" title="current number of votes">1</div><span id="post-37735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flora has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That definition is simply a macro definition that compiles to nothing when <code>SSL_DECRYPT_DEBUG</code> isn't defined. When it is defined the function is defined as an external one, but I can't find where the external function comes from.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '14, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37735" class="comments-container"><span id="37736"></span><div id="comment-37736" class="comment"><div id="post-37736-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your quick response and useful explanation. It helps a lot and I found the definition for the external function. It is in the packet-ssl-utils.c. It just prints to the ssl debug file.</p></div><div id="comment-37736-info" class="comment-info"><span class="comment-age">(10 Nov '14, 11:44)</span> <span class="comment-user userinfo">flora</span></div></div><span id="37748"></span><div id="comment-37748" class="comment"><div id="post-37748-score" class="comment-score"></div><div class="comment-text"><p>OK, somehow I missed that in the grep output.</p></div><div id="comment-37748-info" class="comment-info"><span class="comment-age">(11 Nov '14, 02:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-37735" class="comment-tools"></div><div class="clear"></div><div id="comment-37735-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

