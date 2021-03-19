+++
type = "question"
title = "how the function dissect_http works?"
description = '''i want to do some data mining work on some key fields of the network packets, then I have downloaded the sourcecode of wireshark-1.6.4,and try to use tshark to analyze some packets.but i need to do some change or just define a new struct to store my own variables,i have to find out where is the fiel...'''
date = "2012-11-13T02:36:00Z"
lastmod = "2012-11-14T07:50:00Z"
weight = 15857
keywords = [ "dissect_http" ]
aliases = [ "/questions/15857" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how the function dissect\_http works?](/questions/15857/how-the-function-dissect_http-works)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15857-score" class="post-score" title="current number of votes">0</div><span id="post-15857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i want to do some data mining work on some key fields of the network packets, then I have downloaded the sourcecode of wireshark-1.6.4,and try to use tshark to analyze some packets.but i need to do some change or just define a new struct to store my own variables,i have to find out where is the field i need and copy their value to my own variables.</p><p>in the <code>dissect_http</code> function, there are two paths, one is for proxied connection, another is <code>dissect_http_message</code>, in the <code>dissect_http_message</code>, HTTP headers struct is defined, and assigned some initial value (such as 0 and etc) but i didn't see the assignment process from a real packet value, if i want to find the HTTP content-type of the packet, where is the final position from which i can copy value,could you give me some help?</p><p>there is a related question, if i want to get the HTTP content,where should i get it?</p><p>i am desperately need your answer.thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissect_http" rel="tag" title="see questions tagged &#39;dissect_http&#39;">dissect_http</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '12, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/18b671a9df9f8c8d67a5fce658c10e81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rodman&#39;s gravatar image" /><p><span>rodman</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rodman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Nov '12, 16:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-15857" class="comments-container"></div><div id="comment-tools-15857" class="comment-tools"></div><div class="clear"></div><div id="comment-15857-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15882"></span>

<div id="answer-container-15882" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15882-score" class="post-score" title="current number of votes">1</div><span id="post-15882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>in the <code>dissect_http</code> function, there are two paths, one is for proxied connection, another is <code>dissect_http_message</code>, in the <code>dissect_http_message</code>, HTTP headers struct is defined, and assigned some initial value (such as 0 and etc) but i didn't see the assignment process from a real packet value</p></blockquote><p><code>dissect_http</code> calls <code>process_header</code>, passing it a pointer to the header structure; <code>process_header</code> fills that structure in.</p><blockquote><p>if i want to find the HTTP content-type of the packet, where is the final position from which i can copy value</p></blockquote><p>The <code>content_type</code> member of the HTTP headers struct.</p><blockquote><p>if i want to get the HTTP content,where should i get it?</p></blockquote><p>You'd have to write your own code to handle that; it's not easy to get.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '12, 19:22</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-15882" class="comments-container"><span id="15884"></span><div id="comment-15884" class="comment"><div id="post-15884-score" class="comment-score"></div><div class="comment-text"><p>Infact, i have also noticed the process_header function,but in the code, there is a<br />
if(is_request_or_reply){...} else{...process_header...} sentence,i wonder if the process_header maynot be called,then where to get the header info?</p></div><div id="comment-15884-info" class="comment-info"><span class="comment-age">(13 Nov '12, 21:52)</span> <span class="comment-user userinfo">rodman</span></div></div><span id="15905"></span><div id="comment-15905" class="comment"><div id="post-15905-score" class="comment-score"></div><div class="comment-text"><p>is_request_or_reply is a variable and it contains the return value of is_http_request_or_reply(), which just checks if there is a typical sign for a request (GET,POST,etc.) or a repsonse (200 OK) in the currently processed data. If there is none, that part of the HTTP request/response has already been processed and everything after that must be the HTTP headers. So for the first "line" of the HTTP request (e.g. "GET / HTTP/1.1") the first part of the if clause will be executed. For all remaining "lines" of the HTTP request (e.g. "Host: www.xxx.xxx", "Content-Type: text/html") the else part of the if clause will be executed, which calls process_header().</p></div><div id="comment-15905-info" class="comment-info"><span class="comment-age">(14 Nov '12, 07:50)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-15882" class="comment-tools"></div><div class="clear"></div><div id="comment-15882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

