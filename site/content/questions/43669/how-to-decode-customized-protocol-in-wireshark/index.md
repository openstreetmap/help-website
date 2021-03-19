+++
type = "question"
title = "How to decode customized protocol in Wireshark?"
description = '''Hi all, i want to build my own protocol which will run over SCTP. But during the message encode-decode, i want to see those packets in Wireshark to debug my protocol stack. Is there any way to add my customized protocol by which i can see those decoded packets in Wireshark? I&#x27;m using Wireshark of ve...'''
date = "2015-06-29T09:16:00Z"
lastmod = "2015-06-29T09:44:00Z"
weight = 43669
keywords = [ "decode", "sctp", "customprotocols" ]
aliases = [ "/questions/43669" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode customized protocol in Wireshark?](/questions/43669/how-to-decode-customized-protocol-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43669-score" class="post-score" title="current number of votes">0</div><span id="post-43669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, i want to build my own protocol which will run over SCTP. But during the message encode-decode, i want to see those packets in Wireshark to debug my protocol stack.</p><p>Is there any way to add my customized protocol by which i can see those decoded packets in Wireshark?</p><p>I'm using Wireshark of version 1.10.1.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-sctp" rel="tag" title="see questions tagged &#39;sctp&#39;">sctp</span> <span class="post-tag tag-link-customprotocols" rel="tag" title="see questions tagged &#39;customprotocols&#39;">customprotocols</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '15, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/e82780891a1e938f0bf3a529adc858a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baila&#39;s gravatar image" /><p><span>baila</span><br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baila has no accepted answers">0%</span></p></div></div><div id="comments-container-43669" class="comments-container"></div><div id="comment-tools-43669" class="comment-tools"></div><div class="clear"></div><div id="comment-43669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43673"></span>

<div id="answer-container-43673" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43673-score" class="post-score" title="current number of votes">0</div><span id="post-43673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at the current master sctp dissector (which may be somewhat different to the old 1.10.1 version) a dissector can register with the sctp dissector either on a specific port or with a payload identifier (which must be different from those currently supported) or as a heuristic dissector.</p><p>The dissector for your protocol can definitely be written in C, and possibly in Lua, but I'm not sure how good the Lua support is in your old version.</p><p>The <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Developers Guide</a> (for master, I'm not sure if a 1.10.x version is available) along with the README.xxx files in the doc directory of the source files gives details of writing C dissectors.</p><p>You may find it easier to move to a more current version, as support for 1.10.x ended on 5th June 2015.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '15, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-43673" class="comments-container"></div><div id="comment-tools-43673" class="comment-tools"></div><div class="clear"></div><div id="comment-43673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

