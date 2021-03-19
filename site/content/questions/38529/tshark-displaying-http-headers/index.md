+++
type = "question"
title = "tshark displaying http headers"
description = '''Hello, I have a capture file and need to display just the source and destination addresses and ports along with the http request and response headers. I have done a lot of searching but haven&#x27;t found the correct tshark command to accomplish this task. I want to use tshark because the windows ui for ...'''
date = "2014-12-11T10:03:00Z"
lastmod = "2015-07-10T10:00:00Z"
weight = 38529
keywords = [ "tshark" ]
aliases = [ "/questions/38529" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark displaying http headers](/questions/38529/tshark-displaying-http-headers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38529-score" class="post-score" title="current number of votes">0</div><span id="post-38529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have a capture file and need to display just the source and destination addresses and ports along with the http request and response headers. I have done a lot of searching but haven't found the correct tshark command to accomplish this task. I want to use tshark because the windows ui for wireshark is inaccessible for a blind user.</p><p>Any tips would be greatly appreciated</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '14, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/7ea73b8266e267e80d6f2724f1b7a4c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dnraikes&#39;s gravatar image" /><p><span>dnraikes</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dnraikes has no accepted answers">0%</span></p></div></div><div id="comments-container-38529" class="comments-container"><span id="38530"></span><div id="comment-38530" class="comment"><div id="post-38530-score" class="comment-score"></div><div class="comment-text"><p>Are you looking for all the http headers, e.g. Content-Length etc., or do you want just the request URI and the response code?</p><p>For accessibility, have you tried the QT version of Wireshark to determine if it suits your needs any better?</p></div><div id="comment-38530-info" class="comment-info"><span class="comment-age">(11 Dec '14, 10:43)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38532"></span><div id="comment-38532" class="comment"><div id="post-38532-score" class="comment-score"></div><div class="comment-text"><p>I am looking for all headers. I am using this to help in preparing scripts for fuzzing a web application so I need to see all the headers.</p><p>I haven't tried the qt version of wireshark yet, but I will take a look at it.</p></div><div id="comment-38532-info" class="comment-info"><span class="comment-age">(11 Dec '14, 16:20)</span> <span class="comment-user userinfo">dnraikes</span></div></div></div><div id="comment-tools-38529" class="comment-tools"></div><div class="clear"></div><div id="comment-38529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38539"></span>

<div id="answer-container-38539" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38539-score" class="post-score" title="current number of votes">0</div><span id="post-38539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think getting all the headers is very easy. There is no filter field that contains all the headers, instead each header is given it's own filter. Users can also define custom headers each with their own filter field.</p><p>As it stands the best option may be to use the pdml output of tshark and post-process that, e.g. using the <code>-T pdml</code> option.</p><p>You might also consider raising an enhancement request on the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a> to add all http headers to a single filter field, e.g. <code>http.headers</code> so that could then be output using the <code>-e</code> option, but this might be difficult as headers are CRLF separated and that would be awkward for tshark output. Maybe they could be delimited by some other character.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '14, 01:40</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38539" class="comments-container"><span id="44059"></span><div id="comment-44059" class="comment"><div id="post-44059-score" class="comment-score"></div><div class="comment-text"><p>Hi, so I tried the QT version of wireshark and it is not accessible either (on windows) on Linux it is fine.</p><p>I have decided that what I really need at the moment is the request uri / http version and the response status. This is just an initial test of a fuzzing run.</p></div><div id="comment-44059-info" class="comment-info"><span class="comment-age">(10 Jul '15, 10:00)</span> <span class="comment-user userinfo">dnraikes</span></div></div></div><div id="comment-tools-38539" class="comment-tools"></div><div class="clear"></div><div id="comment-38539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

