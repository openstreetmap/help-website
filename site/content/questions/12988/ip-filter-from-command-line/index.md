+++
type = "question"
title = "IP filter from command line"
description = '''Hi all ,  I am looking for a command that i can use to filter a particular IP . For example I just want to get info about 10.82.23.343 and store in file hello.cap , how will I go about doing that from command line [linux] ?  FYI I have used the commands tshark -i 2 -p -w hello.cap to capture and it ...'''
date = "2012-07-25T08:22:00Z"
lastmod = "2012-07-26T09:13:00Z"
weight = 12988
keywords = [ "filter", "ip" ]
aliases = [ "/questions/12988" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [IP filter from command line](/questions/12988/ip-filter-from-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12988-score" class="post-score" title="current number of votes">0</div><span id="post-12988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all , I am looking for a command that i can use to filter a particular IP . For example I just want to get info about 10.82.23.343 and store in file hello.cap , how will I go about doing that from command line [linux] ? FYI I have used the commands tshark -i 2 -p -w hello.cap to capture and it works but I want to know how do i filter on a particular IP address</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '12, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/9b296b0c1a89a6d15e65215e5e6c69b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld0722&#39;s gravatar image" /><p><span>helloworld0722</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld0722 has no accepted answers">0%</span></p></div></div><div id="comments-container-12988" class="comments-container"><span id="13002"></span><div id="comment-13002" class="comment"><div id="post-13002-score" class="comment-score"></div><div class="comment-text"><p>Kurt I also wanted to know if the capture/filter can be done on multiple files for example tshark -i 2 -p -w hello.cap hello2.cap host 10.82.23.343 is this possible ??? or is there a way to merge capture into two files ?</p></div><div id="comment-13002-info" class="comment-info"><span class="comment-age">(25 Jul '12, 14:01)</span> <span class="comment-user userinfo">helloworld0722</span></div></div><span id="13003"></span><div id="comment-13003" class="comment"><div id="post-13003-score" class="comment-score"></div><div class="comment-text"><p>You can specify the option -w serveral times, but only the last one will be used (just tested).</p><p>Why do you want to write the file two times? You can just copy it after you're done with capturing? Can you please add some more information?</p><p>BTW: The IP Address 10.82.23.<strong>343</strong> is not going to work, unless you have your own special IP stack ;-)</p></div><div id="comment-13003-info" class="comment-info"><span class="comment-age">(25 Jul '12, 14:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="13018"></span><div id="comment-13018" class="comment"><div id="post-13018-score" class="comment-score"></div><div class="comment-text"><p>I have serveral .cap files for which I use mergecap to combine into one file , my question is that can i use mergecap and tshark together and apply filter so that the result file only contains the filtered IP ?</p></div><div id="comment-13018-info" class="comment-info"><span class="comment-age">(26 Jul '12, 06:21)</span> <span class="comment-user userinfo">helloworld0722</span></div></div><span id="13020"></span><div id="comment-13020" class="comment"><div id="post-13020-score" class="comment-score"></div><div class="comment-text"><p>You can do that with tshark, after you merged the files.</p><blockquote><p><code>tshark -r input.cap -w output.cap -R "ip.addr == 10.82.23.x"</code><br />
</p></blockquote><p>HINT: -R requires <a href="http://wiki.wireshark.org/DisplayFilters/">Display Filters</a>!</p></div><div id="comment-13020-info" class="comment-info"><span class="comment-age">(26 Jul '12, 08:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="13024"></span><div id="comment-13024" class="comment"><div id="post-13024-score" class="comment-score"></div><div class="comment-text"><p>yes I got that to work , but what if I want to filter out multiple IPs ?</p></div><div id="comment-13024-info" class="comment-info"><span class="comment-age">(26 Jul '12, 09:08)</span> <span class="comment-user userinfo">helloworld0722</span></div></div><span id="13026"></span><div id="comment-13026" class="comment not_top_scorer"><div id="post-13026-score" class="comment-score"></div><div class="comment-text"><p>just specify them:</p><blockquote><p><code>tshark -r input.cap -w output.cap -R "ip.addr == 10.82.23.x or ip.addr == 1.2.3.4 or ip.addr == 2.3.4.5"</code></p></blockquote></div><div id="comment-13026-info" class="comment-info"><span class="comment-age">(26 Jul '12, 09:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-12988" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-12988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12989"></span>

<div id="answer-container-12989" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12989-score" class="post-score" title="current number of votes">1</div><span id="post-12989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="helloworld0722 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this.</p><blockquote><p><code>tshark -i 2 -p -w hello.cap host 10.82.23.x43</code><br />
</p></blockquote><p><strong>host x.x.x.x</strong> will filter only traffic from and to that IP address.</p><p>Please read the wiki for a more complete list of capture filters:</p><blockquote><p><code>http://wiki.wireshark.org/CaptureFilters</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '12, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jul '12, 14:13</strong> </span></p></div></div><div id="comments-container-12989" class="comments-container"><span id="12990"></span><div id="comment-12990" class="comment"><div id="post-12990-score" class="comment-score"></div><div class="comment-text"><p>thanks it works !!</p></div><div id="comment-12990-info" class="comment-info"><span class="comment-age">(25 Jul '12, 08:43)</span> <span class="comment-user userinfo">helloworld0722</span></div></div></div><div id="comment-tools-12989" class="comment-tools"></div><div class="clear"></div><div id="comment-12989-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

