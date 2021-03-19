+++
type = "question"
title = "SIP Sequence Number Question"
description = '''I have a PCAP for a SIP session that has the relative sequence number start at 1509 and then after 6 packets it restarts at zero and then subsequently thinking that everything afterwards is out of sequence. What is value &quot;SET&quot; mean in the Marker column? I see it as set to True in the Packet detail s...'''
date = "2012-09-24T14:21:00Z"
lastmod = "2012-09-25T06:43:00Z"
weight = 14486
keywords = [ "sip" ]
aliases = [ "/questions/14486" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SIP Sequence Number Question](/questions/14486/sip-sequence-number-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14486-score" class="post-score" title="current number of votes">0</div><span id="post-14486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a PCAP for a SIP session that has the relative sequence number start at 1509 and then after 6 packets it restarts at zero and then subsequently thinking that everything afterwards is out of sequence. What is value "SET" mean in the Marker column? I see it as set to True in the Packet detail screen in the Marker parameter field. Normally this occurs at the very beginning of the session.</p><p>Thanks for your help.</p><p>Eric</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '12, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p><span>EricKnaus</span><br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div></div><div id="comments-container-14486" class="comments-container"></div><div id="comment-tools-14486" class="comment-tools"></div><div class="clear"></div><div id="comment-14486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14511"></span>

<div id="answer-container-14511" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14511-score" class="post-score" title="current number of votes">0</div><span id="post-14511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Command Sequence number should be increasing in a SIP dialog, so it shouldn't reset, other than after an unregister I suppose.</p><p>As for "Set" in the marker column that's probably an RTP question. The meaning of the mark bit is defined through RTP profiles. For speech related streams it can mean resumption of speech after silence suppression in G.729B or VAD/CNG in addition to G.711. For video streams it can mark the start of a new video frame.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '12, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-14511" class="comments-container"></div><div id="comment-tools-14511" class="comment-tools"></div><div class="clear"></div><div id="comment-14511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

