+++
type = "question"
title = "Does wire shark decode SS7 messages obtained from a protocol analyser?"
description = '''I am unable to decode certain SS7 messages coming from an SMLC to an MSC in 3G scenario. Can Wire shark tool help in this?'''
date = "2011-01-25T05:12:00Z"
lastmod = "2012-11-07T02:40:00Z"
weight = 1921
keywords = [ "ss7" ]
aliases = [ "/questions/1921" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Does wire shark decode SS7 messages obtained from a protocol analyser?](/questions/1921/does-wire-shark-decode-ss7-messages-obtained-from-a-protocol-analyser)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1921-score" class="post-score" title="current number of votes">0</div><span id="post-1921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am unable to decode certain SS7 messages coming from an SMLC to an MSC in 3G scenario. Can Wire shark tool help in this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ss7" rel="tag" title="see questions tagged &#39;ss7&#39;">ss7</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '11, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/c0f2c857df95dcf47d1c8162e8def76d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kochu1981&#39;s gravatar image" /><p><span>kochu1981</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kochu1981 has no accepted answers">0%</span></p></div></div><div id="comments-container-1921" class="comments-container"></div><div id="comment-tools-1921" class="comment-tools"></div><div class="clear"></div><div id="comment-1921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1925"></span>

<div id="answer-container-1925" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1925-score" class="post-score" title="current number of votes">1</div><span id="post-1925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That will depend on several things such as can your analyser save its trace in a format such as .pcap that Wireshark understands and does Wireshark have an SS7 dissector.</p><p>I have often exported D channel decodes from an anlayser called "Mty Eye" for E1 protocols such as DPNSS &amp; Q.Sig. Wireshark does have good decoders for these and with careful use of custom columns, you can get somewhere near that of your own analyser's expert software.</p><p>I have also posted a development request in bugzilla to see if it is possible to get a TDM version of "VoIP Calls" to give a CDR style output with facilities to filter &amp; graph TDM calls in a similar way to "VoIP Calls".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '11, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/030196d67dc4e2b8f4ecff65eefdb63e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithFrench&#39;s gravatar image" /><p><span>KeithFrench</span><br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithFrench has no accepted answers">0%</span></p></div></div><div id="comments-container-1925" class="comments-container"></div><div id="comment-tools-1925" class="comment-tools"></div><div class="clear"></div><div id="comment-1925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="15599"></span>

<div id="answer-container-15599" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15599-score" class="post-score" title="current number of votes">0</div><span id="post-15599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is there any suggestion for E1/T1 PCI Card which provides pcap output for all the D Channels? Looking forward for a solution which will give pcap so that we can analyze the SS7 protocol with wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '12, 20:20</strong></p><img src="https://secure.gravatar.com/avatar/75230c5361a844f6aa6d74051f6a8120?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rolland&#39;s gravatar image" /><p><span>rolland</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rolland has no accepted answers">0%</span></p></div></div><div id="comments-container-15599" class="comments-container"><span id="15601"></span><div id="comment-15601" class="comment"><div id="post-15601-score" class="comment-score"></div><div class="comment-text"><p>Some old info can be found here <a href="http://wiki.wireshark.org/CaptureSetup/SS7">http://wiki.wireshark.org/CaptureSetup/SS7</a> updates welcome.</p></div><div id="comment-15601-info" class="comment-info"><span class="comment-age">(06 Nov '12, 20:54)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="15621"></span><div id="comment-15621" class="comment"><div id="post-15621-score" class="comment-score"></div><div class="comment-text"><p>Any updates on this. As this details are not applicable today, as far as I have searched.</p></div><div id="comment-15621-info" class="comment-info"><span class="comment-age">(07 Nov '12, 02:40)</span> <span class="comment-user userinfo">rolland</span></div></div></div><div id="comment-tools-15599" class="comment-tools"></div><div class="clear"></div><div id="comment-15599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

