+++
type = "question"
title = "Capturing GSM identification or beacon frames"
description = '''Will wireshark work in capturing the identification or beacon frame in GSM traffic? I am not interesting in intercepting or decrypting calls. I just need to capture of log the mobile presence with any unique identifier.'''
date = "2016-06-29T04:28:00Z"
lastmod = "2016-06-29T07:21:00Z"
weight = 53720
keywords = [ "beacon", "gsm" ]
aliases = [ "/questions/53720" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing GSM identification or beacon frames](/questions/53720/capturing-gsm-identification-or-beacon-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53720-score" class="post-score" title="current number of votes">0</div><span id="post-53720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Will wireshark work in capturing the identification or beacon frame in GSM traffic? I am not interesting in intercepting or decrypting calls. I just need to capture of log the mobile presence with any unique identifier.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-beacon" rel="tag" title="see questions tagged &#39;beacon&#39;">beacon</span> <span class="post-tag tag-link-gsm" rel="tag" title="see questions tagged &#39;gsm&#39;">gsm</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '16, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/3c29e67417c977300d35f90dea1de00f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sherine&#39;s gravatar image" /><p><span>Sherine</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sherine has no accepted answers">0%</span></p></div></div><div id="comments-container-53720" class="comments-container"></div><div id="comment-tools-53720" class="comment-tools"></div><div class="clear"></div><div id="comment-53720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53727"></span>

<div id="answer-container-53727" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53727-score" class="post-score" title="current number of votes">0</div><span id="post-53727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is just the last element of the toolchain which starts from an antenna and continues basically by hardware capable of receiving the signal and demodulating it and a software creating a frame stream out of the received bit stream.</p><p>Wireshark has recently been enhanced with an API for capturing from any such software in real time. It is called extcap and the description is <a href="https://www.wireshark.org/docs/man-pages/extcap.html">here</a>, but it doesn't relieve the software from the need to provide the data in the form of a stream of frames with additional information in pcap format - the "only" advantage of this API is that it has made live capture from such sources possible.</p><p>As the air interface of GSM is TDM, the software part of your capturing setup may have to do quite a lot to extract something that Wireshark could handle.</p><p>Google is your friend here as several projects deal with the task, using COTS hardware (usually USB DVB-T tuners) for the job. Before you ask, GSM modems (neither USB sticks nor modules embedded into notebooks) aren't usable for the purpose.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '16, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53727" class="comments-container"></div><div id="comment-tools-53727" class="comment-tools"></div><div class="clear"></div><div id="comment-53727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

