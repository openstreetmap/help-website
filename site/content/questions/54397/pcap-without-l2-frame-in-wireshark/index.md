+++
type = "question"
title = "pcap without L2 frame in Wireshark"
description = '''Hi all, I have a pcap file which packets don&#x27;t have a L2 header but each packet start with a L3 header (every packet is a L3 packet). When I open this pcap in Wireshark it tries to parse each packet as Ethernet, which obviously don&#x27;t work. Is there any option in Wireshark to start packet parsing at ...'''
date = "2016-07-28T06:16:00Z"
lastmod = "2016-07-28T11:57:00Z"
weight = 54397
keywords = [ "parsing", "pcap", "wireshark" ]
aliases = [ "/questions/54397" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [pcap without L2 frame in Wireshark](/questions/54397/pcap-without-l2-frame-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54397-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54397-score" class="post-score" title="current number of votes">0</div><span id="post-54397-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I have a pcap file which packets don't have a L2 header but each packet start with a L3 header (every packet is a L3 packet). When I open this pcap in Wireshark it tries to parse each packet as Ethernet, which obviously don't work.</p><p>Is there any option in Wireshark to start packet parsing at L3 not in L2?</p><p>For a ad hoc solution, I've written a small program which insert a mock ethernet header before every packet in the pcap, and this is fine for me, wireshark correctly read it. But I wondering is there any easier way in wireshark?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '16, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/12ea80c01c9446634dc59c64516afbd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmajor&#39;s gravatar image" /><p><span>dmajor</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmajor has no accepted answers">0%</span></p></div></div><div id="comments-container-54397" class="comments-container"></div><div id="comment-tools-54397" class="comment-tools"></div><div class="clear"></div><div id="comment-54397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54399"></span>

<div id="answer-container-54399" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54399-score" class="post-score" title="current number of votes">2</div><span id="post-54399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dmajor has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If Wireshark tries to decode L3 as L2 information, the encapsulation type of that file must be incorrect. You can verify the encapsulation type with capinfos (command line tool installed with Wireshark), or in Wireshark itself using the Statistics -&gt; "Capture File Properties" menu option.</p><p>You can try to fix it using editcap (command line tool installed with Wireshark), using the -T parameter. Most likely "editcap -T rawip infile outfile" might do the trick.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '16, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-54399" class="comments-container"><span id="54400"></span><div id="comment-54400" class="comment"><div id="post-54400-score" class="comment-score"></div><div class="comment-text"><p>Thanks, "editcap -T rawip infile outfile" its work. But for some reason capinfos print: "File encapsulation: Ethernet" to my original pcap, and correctly, to the new file: "File encapsulation: Raw IP"</p></div><div id="comment-54400-info" class="comment-info"><span class="comment-age">(28 Jul '16, 06:31)</span> <span class="comment-user userinfo">dmajor</span></div></div><span id="54414"></span><div id="comment-54414" class="comment"><div id="post-54414-score" class="comment-score"></div><div class="comment-text"><p>... then the encapsulation of the original capture file is incorrectly set by whatever application was used to create that capture file. You should inform the creator of that program of this flaw.</p></div><div id="comment-54414-info" class="comment-info"><span class="comment-age">(28 Jul '16, 11:57)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-54399" class="comment-tools"></div><div class="clear"></div><div id="comment-54399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

