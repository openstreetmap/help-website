+++
type = "question"
title = "No RTP packets are displayed in VOIP Call flow with wireshark 64 bit"
description = '''Hello, Please help me to check this issue, Wireshark 2.0 64 bit (on windows server 2008 64bit) does not display RTP packets in VOIP call graph analysis.  BUT If I use Wireshark 2 v.32 bit (on windows 7 32 bit), it can display full RTP packets.  Thank you!'''
date = "2015-12-24T01:51:00Z"
lastmod = "2016-04-19T05:43:00Z"
weight = 48697
keywords = [ "flow", "display", "rtp" ]
aliases = [ "/questions/48697" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No RTP packets are displayed in VOIP Call flow with wireshark 64 bit](/questions/48697/no-rtp-packets-are-displayed-in-voip-call-flow-with-wireshark-64-bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48697-score" class="post-score" title="current number of votes">0</div><span id="post-48697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Please help me to check this issue, Wireshark 2.0 64 bit (on windows server 2008 64bit) does not display RTP packets in VOIP call graph analysis.</p><p><img src="http://s23.postimg.org/tsujehim3/64b.jpg" alt="alt text" /></p><p>BUT If I use Wireshark 2 v.32 bit (on windows 7 32 bit), it can display full RTP packets.</p><p><img src="http://s14.postimg.org/cs45x71f5/32b.jpg" alt="alt text" /></p><p>Thank you!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-flow" rel="tag" title="see questions tagged &#39;flow&#39;">flow</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Dec '15, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/dacda9118a4e13768835566ad6757ebf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ConnieSmith&#39;s gravatar image" /><p><span>ConnieSmith</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ConnieSmith has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Dec '15, 02:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></img></div></div><div id="comments-container-48697" class="comments-container"><span id="48698"></span><div id="comment-48698" class="comment"><div id="post-48698-score" class="comment-score"></div><div class="comment-text"><p>Be patient, the flow graphs are WiP, several bugs are open for that.</p><p>The "32-bit" picture is also not what it should be, each flow should be represented by a single fat arrow, not by a million ones.</p></div><div id="comment-48698-info" class="comment-info"><span class="comment-age">(24 Dec '15, 02:25)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="48699"></span><div id="comment-48699" class="comment"><div id="post-48699-score" class="comment-score"></div><div class="comment-text"><p>Please show me how to solve this issue.</p><p>Thank you!</p></div><div id="comment-48699-info" class="comment-info"><span class="comment-age">(24 Dec '15, 05:10)</span> <span class="comment-user userinfo">ConnieSmith</span></div></div></div><div id="comment-tools-48697" class="comment-tools"></div><div class="clear"></div><div id="comment-48697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48737"></span>

<div id="answer-container-48737" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48737-score" class="post-score" title="current number of votes">0</div><span id="post-48737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure that the second image RTP belongs to first image flow? First image flow ends 16:24:59 and the second image flow start at 16:39:18. If "fat arrows" more than one with the same timestamp it can be problem in switch configuration. You have to check if same packet appears more than once in dump.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '15, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/ae9a73c94923328e3fdaf4998174c35e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vladimir%20R%C3%B5kovanov&#39;s gravatar image" /><p><span>Vladimir Rõk...</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vladimir Rõkovanov has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Dec '15, 08:57</strong> </span></p></div></div><div id="comments-container-48737" class="comments-container"><span id="51767"></span><div id="comment-51767" class="comment"><div id="post-51767-score" class="comment-score"></div><div class="comment-text"><p>I has the same problem, only i can see the SIP packet but the RTP packet no. I has windos 7 with Dell XPS L502X, 64bit. Please help to resolv this issues. thanks</p></div><div id="comment-51767-info" class="comment-info"><span class="comment-age">(18 Apr '16, 15:24)</span> <span class="comment-user userinfo">MauricioGO</span></div></div><span id="51779"></span><div id="comment-51779" class="comment"><div id="post-51779-score" class="comment-score"></div><div class="comment-text"><p>It may or may not be the same issue although it looks similar. In particular, it may be an issue of the flow graph or an issue of RTP identification based on SIP/SDP contents.</p><p>A link to your capture published somewhere at Cloudshark (preferred), Google drive, MS One Drive, ... would allow to see what is the actual reason, and to eventually file a bug if it is not one of already open ones.</p></div><div id="comment-51779-info" class="comment-info"><span class="comment-age">(19 Apr '16, 05:43)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-48737" class="comment-tools"></div><div class="clear"></div><div id="comment-48737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

