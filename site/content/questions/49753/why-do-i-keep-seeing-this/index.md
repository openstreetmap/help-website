+++
type = "question"
title = "why do i keep seeing this?"
description = '''i keep seeing this character in my cmd line captures. why and how do i get rif of it? thanks! â+&#x27; as in the following: 192.168.0.16 TCP 60 443 â+&#x27; 20413 [ACK] Seq=1 Ack=1702 Win=513  192.168.0.16 TCP 62 9571 â+&#x27; 20450 [PSH, ACK] Seq=729 Ack=37 Win etc'''
date = "2016-02-02T19:35:00Z"
lastmod = "2016-02-03T03:46:00Z"
weight = 49753
keywords = [ "capture", "odd", "characters", "in" ]
aliases = [ "/questions/49753" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [why do i keep seeing this?](/questions/49753/why-do-i-keep-seeing-this)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49753-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49753-score" class="post-score" title="current number of votes">0</div><span id="post-49753-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i keep seeing this character in my cmd line captures. why and how do i get rif of it? thanks!</p><p>â+'</p><p>as in the following: 192.168.0.16 TCP 60 443 â+' 20413 [ACK] Seq=1 Ack=1702 Win=513 192.168.0.16 TCP 62 9571 â+' 20450 [PSH, ACK] Seq=729 Ack=37 Win</p><p>etc</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-odd" rel="tag" title="see questions tagged &#39;odd&#39;">odd</span> <span class="post-tag tag-link-characters" rel="tag" title="see questions tagged &#39;characters&#39;">characters</span> <span class="post-tag tag-link-in" rel="tag" title="see questions tagged &#39;in&#39;">in</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '16, 19:35</strong></p><img src="https://secure.gravatar.com/avatar/91879a16d398f907c691aa7d2e0edd31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="McKittrick&#39;s gravatar image" /><p><span>McKittrick</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="McKittrick has no accepted answers">0%</span></p></div></div><div id="comments-container-49753" class="comments-container"><span id="49763"></span><div id="comment-49763" class="comment"><div id="post-49763-score" class="comment-score"></div><div class="comment-text"><p>At what operating system it happens?</p></div><div id="comment-49763-info" class="comment-info"><span class="comment-age">(03 Feb '16, 03:02)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-49753" class="comment-tools"></div><div class="clear"></div><div id="comment-49753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49760"></span>

<div id="answer-container-49760" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49760-score" class="post-score" title="current number of votes">0</div><span id="post-49760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>why</p></blockquote><p>Because Wireshark and TShark use the Unicode RIGHT ARROW character, rather than "-&gt;", between the source and destination port number in the "Info" column for TCP (and UDP and DCCP) packets, and because whatever is showing that output (terminal emulator, text editor, etc.) apparently isn't properly handling the UTF-8 encoding of that character. If, for example, the terminal emulator or text editor is expecting ISO 8859/1 ("ISO Latin 1") text, it's <em>not</em> going to properly display the text output from Wireshark.</p><blockquote><p>how do i get rif of it?</p></blockquote><p>Either modify Wireshark and TShark not to use that character, or somehow arrange that the software displaying Wireshark's/TShark's output properly handle the UTF-8 encoding of that character.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '16, 01:50</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49760" class="comments-container"><span id="49764"></span><div id="comment-49764" class="comment"><div id="post-49764-score" class="comment-score"></div><div class="comment-text"><p>Basically, it helps to try different fonts until you find one that works, e.g. "Consolas" if you're on Windows.</p></div><div id="comment-49764-info" class="comment-info"><span class="comment-age">(03 Feb '16, 03:46)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-49760" class="comment-tools"></div><div class="clear"></div><div id="comment-49760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

