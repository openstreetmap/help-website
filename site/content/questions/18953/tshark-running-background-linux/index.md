+++
type = "question"
title = "tshark running background linux"
description = '''Im running this tshark filter and cannot get it to start in background or at least run without an active session. Is there some limitation im missing with tshark? Is there anything I can do to get this to run with me having to ssh and manually start the command? OS= Linux/Debian Squeeze. tshark -R &quot;...'''
date = "2013-02-27T20:34:00Z"
lastmod = "2013-02-28T08:13:00Z"
weight = 18953
keywords = [ "linux", "tshark", "background", "debian" ]
aliases = [ "/questions/18953" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tshark running background linux](/questions/18953/tshark-running-background-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18953-score" class="post-score" title="current number of votes">0</div><span id="post-18953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im running this tshark filter and cannot get it to start in background or at least run without an active session. Is there some limitation im missing with tshark? Is there anything I can do to get this to run with me having to ssh and manually start the command? OS= Linux/Debian Squeeze. tshark -R "http.request ==1 and http.user_agent" -T fields -e ip.addr -e http.user_agent -w tshark.log I also tried to redirect output to a file and not use -w (&gt;tshark.log) Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-background" rel="tag" title="see questions tagged &#39;background&#39;">background</span> <span class="post-tag tag-link-debian" rel="tag" title="see questions tagged &#39;debian&#39;">debian</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '13, 20:34</strong></p><img src="https://secure.gravatar.com/avatar/136679ce18caf13bfdc7eee59208694d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sectech&#39;s gravatar image" /><p><span>sectech</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sectech has no accepted answers">0%</span></p></div></div><div id="comments-container-18953" class="comments-container"><span id="18961"></span><div id="comment-18961" class="comment"><div id="post-18961-score" class="comment-score"></div><div class="comment-text"><blockquote><p>and cannot get it to start in background or at least run without an active session</p></blockquote><p>how did you try that?</p></div><div id="comment-18961-info" class="comment-info"><span class="comment-age">(27 Feb '13, 23:46)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="18968"></span><div id="comment-18968" class="comment"><div id="post-18968-score" class="comment-score"></div><div class="comment-text"><p>I tried adding -q and &amp; at the end, it strips my filter and strips my stdout redirection. I tried an init script for debian i found, and using this command from shell. and output different ways it does the same strips my filter and redirects stdout to /tmp/wiresharkxxx<em>. Im not a</em> nix guru. Im just trying to figure this out as I go. Thanks! <code></code></p><p><code></code></p><h1 id="binbash."><code>!/bin/bash.</code></h1><code></code><h1 id="add-more-options-to-tshark-as-appropriate-to-your-command....">Add more options to tshark, as appropriate to your command....</h1></code><p><code>setsid tshark -R "http.request ==1 and http.user_agent" -T fields -e ip.addr -e http.user_agent -w tshark.log</code></p></div><div id="comment-18968-info" class="comment-info"><span class="comment-age">(28 Feb '13, 04:25)</span> <span class="comment-user userinfo">sectech</span></div></div></div><div id="comment-tools-18953" class="comment-tools"></div><div class="clear"></div><div id="comment-18953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18973"></span>

<div id="answer-container-18973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18973-score" class="post-score" title="current number of votes">0</div><span id="post-18973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>tshark -R "http.request ==1 and http.user_agent" -T fields -e ip.addr -e http.user_agent -w tshark.log</p></blockquote><p>please run that command in a terminal and read the error message!</p><p>It should be something similar than this (depending on the tshark version):</p><blockquote><p><code>tshark: Read filters aren't supported when capturing and saving the captured packets.</code><br />
</p></blockquote><p>BTW: What are you trying to do? Logging the User-Agent and IP address of HTTP requests as soon as the system starts? If yes: How long do you intend to run that command (minutes, hours, days)?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Feb '13, 06:47</strong> </span></p></div></div><div id="comments-container-18973" class="comments-container"><span id="18974"></span><div id="comment-18974" class="comment"><div id="post-18974-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the info! hmm so i didnt realize they werent supported. I plan running this 24x7 reading the log and clearing every 5 minutes. Do you have a better solution in mind? I would use iptable logging but they dont read header :(</p></div><div id="comment-18974-info" class="comment-info"><span class="comment-age">(28 Feb '13, 06:58)</span> <span class="comment-user userinfo">sectech</span></div></div><span id="18981"></span><div id="comment-18981" class="comment"><div id="post-18981-score" class="comment-score"></div><div class="comment-text"><p>does it matter if you miss 'some' sessions?</p></div><div id="comment-18981-info" class="comment-info"><span class="comment-age">(28 Feb '13, 08:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-18973" class="comment-tools"></div><div class="clear"></div><div id="comment-18973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18976"></span>

<div id="answer-container-18976" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18976-score" class="post-score" title="current number of votes">0</div><span id="post-18976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't see how you want to start an application without actually initiating an interactive shell.</p><p>Anyway, what I normally do is start tshark in a screen session, then leave it running and detach from the screen session. When I need to access the data, I can reattach to screen.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/89981ff7056cf5f19881f813132a2390?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gsgleason&#39;s gravatar image" /><p><span>gsgleason</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gsgleason has no accepted answers">0%</span></p></div></div><div id="comments-container-18976" class="comments-container"></div><div id="comment-tools-18976" class="comment-tools"></div><div class="clear"></div><div id="comment-18976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

