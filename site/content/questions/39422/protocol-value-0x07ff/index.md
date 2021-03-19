+++
type = "question"
title = "protocol value &quot;0x07ff&quot;"
description = '''Hi, I got a &quot;0x07ff&quot; protocol value when I used wireshark to collect net packet info. I don&#x27;t know what does this value &quot;0x07ff&quot; mean. I search it in the IANA, and found there is not a protocol value like this. who can tell me. or It just mean a undefined protocol?'''
date = "2015-01-27T00:07:00Z"
lastmod = "2015-01-27T02:43:00Z"
weight = 39422
keywords = [ "0x07ff", "protocol" ]
aliases = [ "/questions/39422" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [protocol value "0x07ff"](/questions/39422/protocol-value-0x07ff)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39422-score" class="post-score" title="current number of votes">0</div><span id="post-39422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I got a "0x07ff" protocol value when I used wireshark to collect net packet info. I don't know what does this value "0x07ff" mean. I search it in the IANA, and found there is not a protocol value like this. who can tell me. or It just mean a undefined protocol?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-0x07ff" rel="tag" title="see questions tagged &#39;0x07ff&#39;">0x07ff</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '15, 00:07</strong></p><img src="https://secure.gravatar.com/avatar/3998e8ac7d132cc30aac9237ca6a69ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itachi007&#39;s gravatar image" /><p><span>itachi007</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itachi007 has no accepted answers">0%</span></p></div></div><div id="comments-container-39422" class="comments-container"></div><div id="comment-tools-39422" class="comment-tools"></div><div class="clear"></div><div id="comment-39422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39431"></span>

<div id="answer-container-39431" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39431-score" class="post-score" title="current number of votes">0</div><span id="post-39431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Since the "protocol" field at the IP layer is an 8-bit field, I assume that by "protocol" you mean "Ethertype".</p><p>Then it looks like 0x07ff is being used by DynaCore, see: <a href="https://www12.informatik.uni-erlangen.de/spprr/colloquium06/DynaCore_Muenchen.pdf">https://www12.informatik.uni-erlangen.de/spprr/colloquium06/DynaCore_Muenchen.pdf</a> Is it feasible that you have DynaCore traffic in your network (I did not really dig into the protocol, just found it on google). If not, can you share a little capture file on www.cloudshark.org?</p><p>If you did not mean "Ethertype", then please tell us which "protocol" field you are referring to.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '15, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39431" class="comments-container"></div><div id="comment-tools-39431" class="comment-tools"></div><div class="clear"></div><div id="comment-39431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

