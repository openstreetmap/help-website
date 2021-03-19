+++
type = "question"
title = "HOw to analyze TCP dump"
description = '''Hi Team, I have taken TCP dump from Linux system &amp;amp; I want to analyze the dump with wireshark tool.  plz help'''
date = "2016-10-06T07:04:00Z"
lastmod = "2016-10-07T04:21:00Z"
weight = 56191
keywords = [ "howtoanalyzetcpdump" ]
aliases = [ "/questions/56191" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [HOw to analyze TCP dump](/questions/56191/how-to-analyze-tcp-dump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56191-score" class="post-score" title="current number of votes">0</div><span id="post-56191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Team, I have taken TCP dump from Linux system &amp; I want to analyze the dump with wireshark tool.</p><p>plz help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-howtoanalyzetcpdump" rel="tag" title="see questions tagged &#39;howtoanalyzetcpdump&#39;">howtoanalyzetcpdump</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '16, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/c5e2d82cdc065a81e19107be13d99a9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay2016&#39;s gravatar image" /><p><span>Vijay2016</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay2016 has no accepted answers">0%</span></p></div></div><div id="comments-container-56191" class="comments-container"><span id="56201"></span><div id="comment-56201" class="comment"><div id="post-56201-score" class="comment-score"></div><div class="comment-text"><p>I think you need to be more specific with what you need help for. I guess you are skilled enough to open the dump file in Wireshark. What are you looking for? What's the problem?</p></div><div id="comment-56201-info" class="comment-info"><span class="comment-age">(06 Oct '16, 09:13)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="56204"></span><div id="comment-56204" class="comment"><div id="post-56204-score" class="comment-score"></div><div class="comment-text"><p>How did you take the tcpdump? Using the -w flag you will get a capture file that you can open with wireshark example sudo tcpdump -w tcpdump.pcap -i interface</p></div><div id="comment-56204-info" class="comment-info"><span class="comment-age">(06 Oct '16, 13:13)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="56212"></span><div id="comment-56212" class="comment"><div id="post-56212-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper &amp; mrEEde,</p><p>We have taken tcp dump with out any condition from server ana I am able to open the dump through wireshark.I need a help , how to analyze in wireshark. Need some tips / trick if any for analysis.</p></div><div id="comment-56212-info" class="comment-info"><span class="comment-age">(07 Oct '16, 00:03)</span> <span class="comment-user userinfo">Vijay2016</span></div></div></div><div id="comment-tools-56191" class="comment-tools"></div><div class="clear"></div><div id="comment-56191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56218"></span>

<div id="answer-container-56218" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56218-score" class="post-score" title="current number of votes">1</div><span id="post-56218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://www.wireshark.org/#learnWS">Here are some very good resources</a> to learn about network analysis.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '16, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-56218" class="comments-container"></div><div id="comment-tools-56218" class="comment-tools"></div><div class="clear"></div><div id="comment-56218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

