+++
type = "question"
title = "How to analyze pcap files for slow internet communication"
description = '''Dear All, I am a new user therefore I need some help. I need to analyze 2 pcap files for a job interview. Unfortunately I dont have experience on wireshark. Here is the given case and the given pcap files:  &quot;There are complaints in a specific region from 3G customers that internet communication is s...'''
date = "2015-04-05T02:40:00Z"
lastmod = "2015-04-05T09:57:00Z"
weight = 41197
keywords = [ "pcapng", "pcap", "tcp", "analysis", "wireshark" ]
aliases = [ "/questions/41197" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to analyze pcap files for slow internet communication](/questions/41197/how-to-analyze-pcap-files-for-slow-internet-communication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41197-score" class="post-score" title="current number of votes">0</div><span id="post-41197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear All,</p><p>I am a new user therefore I need some help. I need to analyze 2 pcap files for a job interview. Unfortunately I dont have experience on wireshark. Here is the given case and the given pcap files:</p><p>"There are complaints in a specific region from 3G customers that internet communication is slow. PS Core network is working on totally IP infrastructure. It is determined that this problem is related with customers that served by a specific RNC(Radio Network Controller). It is taken a Gn interface trace for complainant over SGSN (Serving GPRS Service Node). Also we request him to take a trace. These two traces are at the attachment.</p><p>Could you please prepare a report about how to analyse the problem and the result that you have reached. What can be the problem according to you?" <a href="http://s000.tinyupload.com/?file_id=09762649765123260212">link text</a> - sgsn trace pcap file <a href="http://s000.tinyupload.com/?file_id=14698443904908310890">link text</a> - ue trace pcap file</p><p>I dont know where to start on pcap files. I am welcome any comments and suggestions so at least I can have idea.</p><p>thanks in advance .</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '15, 02:40</strong></p><img src="https://secure.gravatar.com/avatar/82e9d09d14a568559473abff4d40071a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chndrkn&#39;s gravatar image" /><p><span>chndrkn</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chndrkn has no accepted answers">0%</span></p></div></div><div id="comments-container-41197" class="comments-container"></div><div id="comment-tools-41197" class="comment-tools"></div><div class="clear"></div><div id="comment-41197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41199"></span>

<div id="answer-container-41199" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41199-score" class="post-score" title="current number of votes">1</div><span id="post-41199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The obvious thing here is packet loss, with retransmissions taking two or three digit numbers of milliseconds, which may add up to significant delay if it happens multiple times. The CRC errors on the GPRS tunneled segments can be ignored as the same packet has a correct CRC in the other trace, so it's probably caused by a local capture setup.</p><p>I have to add three things here here though:</p><ol><li>are you sure you were authorized to post those pcap files on public sites? It may contain sensitive data, e.g. internal network structures or user/customer data which should not be exposed to the public</li><li>if they are interviewing you for a job which requires reading pcaps, all the help from this forum will not enable you to actually do it, as it is something that needs experience and can't be learned quickly</li><li>are you aware that the guys giving you the files for the interview may be monitoring this Q&amp;A site?</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '15, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41199" class="comments-container"><span id="41200"></span><div id="comment-41200" class="comment"><div id="post-41200-score" class="comment-score"></div><div class="comment-text"><p>Dear Jasper</p><p>thank you very much for your answer. Also thanks a lot for informing me about my mistake. I have removed the files. I am a fresh graduate student and dont have experience on wireshark. therefore I need some help to have idea at least.</p></div><div id="comment-41200-info" class="comment-info"><span class="comment-age">(05 Apr '15, 09:57)</span> <span class="comment-user userinfo">chndrkn</span></div></div></div><div id="comment-tools-41199" class="comment-tools"></div><div class="clear"></div><div id="comment-41199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

