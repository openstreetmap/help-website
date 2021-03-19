+++
type = "question"
title = "Wireshark Documentation"
description = '''Hi, im kind of new developing with wireshark. Im now working with custom dissectors, and im having trouble finding documentation for it. Is there a place qhere i can find a complete guide? Or at least, what im looking for is to know the functions that we have, and what parameters you have to put int...'''
date = "2014-08-19T10:30:00Z"
lastmod = "2014-08-20T04:48:00Z"
weight = 35584
keywords = [ "code", "dissector", "help", "guide", "wireshark" ]
aliases = [ "/questions/35584" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Documentation](/questions/35584/wireshark-documentation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35584-score" class="post-score" title="current number of votes">0</div><span id="post-35584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, im kind of new developing with wireshark. Im now working with custom dissectors, and im having trouble finding documentation for it. Is there a place qhere i can find a complete guide? Or at least, what im looking for is to know the functions that we have, and what parameters you have to put into them. For example proto_item_add_subtree() or col_add_fstr(). Maybe im missing something, but so far, i can find some third parties guides to make a baseic foo disector. But i start having trouble when i try to do something more complex. Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-code" rel="tag" title="see questions tagged &#39;code&#39;">code</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-guide" rel="tag" title="see questions tagged &#39;guide&#39;">guide</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '14, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/3f60a30a327fa363a0166009000c466d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ingcpt&#39;s gravatar image" /><p><span>ingcpt</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ingcpt has no accepted answers">0%</span></p></div></div><div id="comments-container-35584" class="comments-container"></div><div id="comment-tools-35584" class="comment-tools"></div><div class="clear"></div><div id="comment-35584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35588"></span>

<div id="answer-container-35588" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35588-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35588-score" class="post-score" title="current number of votes">0</div><span id="post-35588-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Developers Guide</a> and the content of the docs directory in the source tree, in particular README.dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '14, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-35588" class="comments-container"><span id="35617"></span><div id="comment-35617" class="comment"><div id="post-35617-score" class="comment-score"></div><div class="comment-text"><p>Ive been reading this documentation, and theres something basic I cant find. How do you know the legnth of the data in the packet? In my protocol, i have an initial header, and then an unkown amount of structures. These structures have 1 byte for legnth, and then the data itself. Id like to do something like while(offset&lt;TotalLength) { //Work with the structures }</p><p>How do i know the Total Length? Thanks in advance</p></div><div id="comment-35617-info" class="comment-info"><span class="comment-age">(20 Aug '14, 04:32)</span> <span class="comment-user userinfo">ingcpt</span></div></div><span id="35618"></span><div id="comment-35618" class="comment"><div id="post-35618-score" class="comment-score"></div><div class="comment-text"><p>The tvb contains the data handed to your dissector. There are two length options, the reported length (<code>tvb_reported_length(tvb)</code>) which is the length that data originally had "on-the-wire" and the captured length (<code>tvb_captured_length(tvb)</code>) which is the length that was actually captured.</p><p>In general you should be using the reported length and allow your dissector to cause an exception if the captured length is less than the reported length so the UI can show the packet has been truncated.</p></div><div id="comment-35618-info" class="comment-info"><span class="comment-age">(20 Aug '14, 04:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="35619"></span><div id="comment-35619" class="comment"><div id="post-35619-score" class="comment-score"></div><div class="comment-text"><p>One thing to know, in Wireshark all packet data is passed on through TVB's. It might be time to go deeper and familiarize yourself with the inner workings of Wireshark (coding a dissector <em>IS</em> using the inner workings). For instance start with reading the epan/tvbuff.h</p></div><div id="comment-35619-info" class="comment-info"><span class="comment-age">(20 Aug '14, 04:48)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-35588" class="comment-tools"></div><div class="clear"></div><div id="comment-35588-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

