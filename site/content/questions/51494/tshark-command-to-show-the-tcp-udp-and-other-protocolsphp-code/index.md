+++
type = "question"
title = "Tshark command to show the tcp , udp and other protocols(PHP code)"
description = '''Dear wireskarks experts, Hope this topis find you well. I am doing a project for my course network forensics. I build a website that allow users to upload the pcap file and I send it to the terminal with tshark command and then store it as csv file and then parse that file and store it in database p...'''
date = "2016-04-07T13:41:00Z"
lastmod = "2016-04-19T13:53:00Z"
weight = 51494
keywords = [ "tshark" ]
aliases = [ "/questions/51494" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark command to show the tcp , udp and other protocols(PHP code)](/questions/51494/tshark-command-to-show-the-tcp-udp-and-other-protocolsphp-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51494-score" class="post-score" title="current number of votes">0</div><span id="post-51494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear wireskarks experts, Hope this topis find you well.</p><p>I am doing a project for my course network forensics. I build a website that allow users to upload the pcap file and I send it to the terminal with tshark command and then store it as csv file and then parse that file and store it in database phpmyadmine. My question I want the command that can specify or extract the tcp and udp instead of getting numbers(I want the explicit name of the protocol tcp or udp instead of getting numbers(6, 17) i want to get tcp or udp). : Here is my Command system('tshark -r '.$final.' -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e ip.src -e ip.dst -e ip.proto -e tcp.analysis.spurious_retransmission -E header=y -E separator=, -E quote=d -E occurrence=f &gt; file.csv');</p><p>Also, I want to do a piechart, and graph. Do you have any suggestions for that ? maybe commands, or any other ideas?</p><p>I am using php for front and backend(shell_exec());</p><p>Best-wishes Small and humble wire shark Samia M</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2016-04-07_at_4.34.03_PM.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '16, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/cf5f8227601bc4073445493848b0f8c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Samia%20Muhammad&#39;s gravatar image" /><p><span>Samia Muhammad</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Samia Muhammad has no accepted answers">0%</span></p></img></div></div><div id="comments-container-51494" class="comments-container"></div><div id="comment-tools-51494" class="comment-tools"></div><div class="clear"></div><div id="comment-51494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51803"></span>

<div id="answer-container-51803" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51803-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51803-score" class="post-score" title="current number of votes">0</div><span id="post-51803-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>instead of getting numbers(6, 17) i want to get tcp or udp<br />
<strong>I am using php</strong> for front and backend(shell_exec());</p></blockquote><p>Well, if you are using PHP anyway, why not simply replace 6 with TCP and 17 with UDP, before you store/process the data !?!</p><blockquote><p>Also, I want to do a piechart, and graph. Do you have any suggestions for that ? maybe commands, or any other ideas?</p></blockquote><p>There are tons of PHP chart libraries out there. Simply pick one of them.</p><blockquote><p><a href="https://www.google.com/?q=php+chart+library">https://www.google.com/?q=php+chart+library</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '16, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Apr '16, 13:53</strong> </span></p></div></div><div id="comments-container-51803" class="comments-container"></div><div id="comment-tools-51803" class="comment-tools"></div><div class="clear"></div><div id="comment-51803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

