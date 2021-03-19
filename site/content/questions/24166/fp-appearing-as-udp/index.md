+++
type = "question"
title = "FP appearing as UDP"
description = '''Hi, I managed to take a capture of an IuB interace (link between NodeB and RNC) on my laptop. I am expecting to see FP PDUs, however they all appear as UDP. How can I setup/configure Wireshark so that it recognizes that these frames are FP? Wireshark doesn&#x27;t give me the option to decode as FP. Do I ...'''
date = "2013-08-29T08:07:00Z"
lastmod = "2013-08-29T08:46:00Z"
weight = 24166
keywords = [ "fp", "umts", "iub", "umts-fp" ]
aliases = [ "/questions/24166" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [FP appearing as UDP](/questions/24166/fp-appearing-as-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24166-score" class="post-score" title="current number of votes">0</div><span id="post-24166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I managed to take a capture of an IuB interace (link between NodeB and RNC) on my laptop. I am expecting to see FP PDUs, however they all appear as UDP. How can I setup/configure Wireshark so that it recognizes that these frames are FP? Wireshark doesn't give me the option to decode as FP. Do I require additional information to decode these frames? Is this possible without obtaining Catapult DCT2000 or Tektronix K12 format traces? I'd like to see a protocol stack similar to what's posted on Wireshark's wiki in regards to FP. <a href="http://wiki.wireshark.org/FP">http://wiki.wireshark.org/FP</a></p><p>Thanks, Davide</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fp" rel="tag" title="see questions tagged &#39;fp&#39;">fp</span> <span class="post-tag tag-link-umts" rel="tag" title="see questions tagged &#39;umts&#39;">umts</span> <span class="post-tag tag-link-iub" rel="tag" title="see questions tagged &#39;iub&#39;">iub</span> <span class="post-tag tag-link-umts-fp" rel="tag" title="see questions tagged &#39;umts-fp&#39;">umts-fp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '13, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/f39df66f24ae13ebcdb2662e2a1e4095?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davide0089&#39;s gravatar image" /><p><span>davide0089</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davide0089 has no accepted answers">0%</span></p></div></div><div id="comments-container-24166" class="comments-container"></div><div id="comment-tools-24166" class="comment-tools"></div><div class="clear"></div><div id="comment-24166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24167"></span>

<div id="answer-container-24167" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24167-score" class="post-score" title="current number of votes">3</div><span id="post-24167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check out similar questions here <a href="http://ask.wireshark.org/tags/fp/">http://ask.wireshark.org/tags/fp/</a> Basically Wireshark needs a lot of information on the FP stream to be able to dissect it, if you have Wireshark 1.10.x and the NBAP and RRC setup information is present in the trace Wireshark can dissect some FP flows.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '13, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-24167" class="comments-container"></div><div id="comment-tools-24167" class="comment-tools"></div><div class="clear"></div><div id="comment-24167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

