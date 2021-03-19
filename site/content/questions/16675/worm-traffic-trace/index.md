+++
type = "question"
title = "Worm traffic trace"
description = '''Hi I need samples of differnt worms&#x27; traffic capture, that I can use them safely. Any body knows where I can find something like that?? and what procedures should be taken when I handle some traces like these??or even any other forum where I can ask . There are two sample captures in wireshark.org, ...'''
date = "2012-12-07T03:15:00Z"
lastmod = "2012-12-17T02:26:00Z"
weight = 16675
keywords = [ "capture", "trace", "wireshark" ]
aliases = [ "/questions/16675" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Worm traffic trace](/questions/16675/worm-traffic-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16675-score" class="post-score" title="current number of votes">0</div><span id="post-16675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I need samples of differnt worms' traffic capture, that I can use them safely. Any body knows where I can find something like that?? and what procedures should be taken when I handle some traces like these??or even any other forum where I can ask . There are two sample captures in <a href="http://wireshark.org">wireshark.org</a>, I'm interested in slammer.pcap but I tried once to download it and there was a warning of opening this file, what I should do when I work with such files safely, I have a program that has to detect the scanning activity of worms and I need a capture to try it with to know if it is working with. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-trace" rel="tag" title="see questions tagged &#39;trace&#39;">trace</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '12, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/912ebc145cb38ec3da99be6003d7d9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leena&#39;s gravatar image" /><p><span>Leena</span><br />
<span class="score" title="51 reputation points">51</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leena has no accepted answers">0%</span></p></div></div><div id="comments-container-16675" class="comments-container"><span id="16686"></span><div id="comment-16686" class="comment"><div id="post-16686-score" class="comment-score"></div><div class="comment-text"><p>Sample captures in <a href="http://wireshark.org">wireshark.org</a> don't agree with what I'm looking for,the first one contains a packet of the worm, and the other is containing a packet showing an anomaly which is not what I'm looking for, I need a trace showing the scanning activity of the worm. I googled it too much but with no result!!!!!</p></div><div id="comment-16686-info" class="comment-info"><span class="comment-age">(07 Dec '12, 08:00)</span> <span class="comment-user userinfo">Leena</span></div></div><span id="16689"></span><div id="comment-16689" class="comment"><div id="post-16689-score" class="comment-score"></div><div class="comment-text"><p>Why don't you simply trace a nmap scan or <a href="http://s.th">s.th</a>. similar or what exactly do you mean with "scanning activity of a worm"?!</p></div><div id="comment-16689-info" class="comment-info"><span class="comment-age">(07 Dec '12, 08:10)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="16697"></span><div id="comment-16697" class="comment"><div id="post-16697-score" class="comment-score"></div><div class="comment-text"><p>Before worm break out it first scans either random ip addresses or sequential ones to get some vulnerable targets and then complete attack, I just need real examples because it looks more persuasive and maybe I could found other works on them to compare with mine to identify the advantages and disadvantages of the program,and maintain factors such as speed and other capabilities. It is a research work</p></div><div id="comment-16697-info" class="comment-info"><span class="comment-age">(07 Dec '12, 09:47)</span> <span class="comment-user userinfo">Leena</span></div></div></div><div id="comment-tools-16675" class="comment-tools"></div><div class="clear"></div><div id="comment-16675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16699"></span>

<div id="answer-container-16699" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16699-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16699-score" class="post-score" title="current number of votes">1</div><span id="post-16699-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Leena has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As you are trying to build an IPS (based on your question history), I recommend this:</p><blockquote><p><code>http://www.iscx.ca/datasets</code><br />
</p></blockquote><p><strong>UPDATE</strong>:</p><p>These datasets might be interesting as well.</p><blockquote><p><code>http://www.caida.org/data/passive/passive_2012_dataset.xml</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '12, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Dec '12, 01:15</strong> </span></p></div></div><div id="comments-container-16699" class="comments-container"><span id="16701"></span><div id="comment-16701" class="comment"><div id="post-16701-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Kurt, I'll check it. May God Bless you</p></div><div id="comment-16701-info" class="comment-info"><span class="comment-age">(07 Dec '12, 10:31)</span> <span class="comment-user userinfo">Leena</span></div></div><span id="16702"></span><div id="comment-16702" class="comment"><div id="post-16702-score" class="comment-score"></div><div class="comment-text"><p>good luck.</p><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-16702-info" class="comment-info"><span class="comment-age">(07 Dec '12, 12:11)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16717"></span><div id="comment-16717" class="comment"><div id="post-16717-score" class="comment-score"></div><div class="comment-text"><p>Sure,I won't forget.</p></div><div id="comment-16717-info" class="comment-info"><span class="comment-age">(07 Dec '12, 17:45)</span> <span class="comment-user userinfo">Leena</span></div></div><span id="16961"></span><div id="comment-16961" class="comment"><div id="post-16961-score" class="comment-score"></div><div class="comment-text"><p>There is also a link that contains a list of public pcap files for download <a href="http://www.netresec.com/?page=PcapFiles">http://www.netresec.com/?page=PcapFiles</a> It may help who needs pcap repositories. Thanks Kurt you are always helping</p></div><div id="comment-16961-info" class="comment-info"><span class="comment-age">(17 Dec '12, 02:26)</span> <span class="comment-user userinfo">Leena</span></div></div></div><div id="comment-tools-16699" class="comment-tools"></div><div class="clear"></div><div id="comment-16699-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

