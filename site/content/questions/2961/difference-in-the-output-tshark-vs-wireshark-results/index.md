+++
type = "question"
title = "difference in the output: tshark Vs Wireshark results"
description = '''Installed the 1.5.0 build and I see scsi,rtt commandline arguments. There is a difference in the output compared to UI. Is this a known issue? Via CLI started the capture interface:   - tshark -S -i 2 -w capture_out.pcap   - tshark -r capture_out.pcap -q -z scsi,rtt,0 returns avg SRT value: 0.021678...'''
date = "2011-03-20T18:07:00Z"
lastmod = "2011-03-21T15:26:00Z"
weight = 2961
keywords = [ "tshark" ]
aliases = [ "/questions/2961" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [difference in the output: tshark Vs Wireshark results](/questions/2961/difference-in-the-output-tshark-vs-wireshark-results)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2961-score" class="post-score" title="current number of votes">0</div><span id="post-2961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Installed the 1.5.0 build and I see scsi,rtt commandline arguments. There is a difference in the output compared to UI. Is this a known issue?</p><p>Via CLI started the capture interface: - tshark -S -i 2 -w capture_out.pcap - tshark -r capture_out.pcap -q -z scsi,rtt,0</p><p>returns avg SRT value: 0.021678.</p><p>Via UI capture,</p><ul><li>Started the capture interface via UI</li><li>send some traffice</li><li>View the statistics: Statistics-&gt;Service Response Time-&gt;SCSI-&gt;Filter&lt;iscsi.time&gt; returns: Avg SRT value: 0.081465.</li></ul><p>Which avg SRT is correct, UI or CLI? Yes, I've made sure I start the capture trace first before i send data.</p><p>Any help is appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '11, 18:07</strong></p><img src="https://secure.gravatar.com/avatar/009622f35eab24cfbde3547b04a5bbea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="asif&#39;s gravatar image" /><p><span>asif</span><br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="asif has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Mar '11, 18:21</strong> </span></p></div></div><div id="comments-container-2961" class="comments-container"><span id="2966"></span><div id="comment-2966" class="comment"><div id="post-2966-score" class="comment-score">1</div><div class="comment-text"><p>Are you gathering statistics using the same capture file for both tshark and Wireshark? It seems as if you are not comparing apples to apples.</p></div><div id="comment-2966-info" class="comment-info"><span class="comment-age">(21 Mar '11, 07:00)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-2961" class="comment-tools"></div><div class="clear"></div><div id="comment-2961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2983"></span>

<div id="answer-container-2983" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2983-score" class="post-score" title="current number of votes">1</div><span id="post-2983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What statistics are generated by Wireshark if you load the data captured by tshark?</p><p>Anything else is going to be, as asif noted, apples and oranges. Response time can vary significantly from one moment to the next.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '11, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-2983" class="comments-container"></div><div id="comment-tools-2983" class="comment-tools"></div><div class="clear"></div><div id="comment-2983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

