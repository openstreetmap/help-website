+++
type = "question"
title = "deleting error packets"
description = '''Is there a way to remove/delete packets that Wrieshark lists as errors, such as &quot;Expert Info&quot;. I would like to remove these packets from the pcap file so the resultant file is contains only traffic that is valid.'''
date = "2011-02-03T09:17:00Z"
lastmod = "2011-02-03T13:51:00Z"
weight = 2128
keywords = [ "info", "expert" ]
aliases = [ "/questions/2128" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [deleting error packets](/questions/2128/deleting-error-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2128-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2128-score" class="post-score" title="current number of votes">1</div><span id="post-2128-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to remove/delete packets that Wrieshark lists as errors, such as "Expert Info". I would like to remove these packets from the pcap file so the resultant file is contains only traffic that is valid.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-info" rel="tag" title="see questions tagged &#39;info&#39;">info</span> <span class="post-tag tag-link-expert" rel="tag" title="see questions tagged &#39;expert&#39;">expert</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '11, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/8666e2b3cddf396091e29a008ac7d8dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mvossberg&#39;s gravatar image" /><p><span>mvossberg</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mvossberg has no accepted answers">0%</span></p></div></div><div id="comments-container-2128" class="comments-container"></div><div id="comment-tools-2128" class="comment-tools"></div><div class="clear"></div><div id="comment-2128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2129"></span>

<div id="answer-container-2129" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2129-score" class="post-score" title="current number of votes">2</div><span id="post-2129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sure. Use a display filter to filter on "<code>not expert.severity==error</code>" and save the file, using the "Displayed" radiobutton setting in the "Packet Range" pane of the save dialog.</p><p>I wonder why you would want to remove errors from the trace as they might be the most interesting part of it, but I'm sure you have something in mind :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '11, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Feb '11, 09:33</strong> </span></p></div></div><div id="comments-container-2129" class="comments-container"><span id="2138"></span><div id="comment-2138" class="comment"><div id="post-2138-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper - things worked - I appreciate it. mvossberg</p></div><div id="comment-2138-info" class="comment-info"><span class="comment-age">(03 Feb '11, 13:51)</span> <span class="comment-user userinfo">mvossberg</span></div></div></div><div id="comment-tools-2129" class="comment-tools"></div><div class="clear"></div><div id="comment-2129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2130"></span>

<div id="answer-container-2130" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2130-score" class="post-score" title="current number of votes">1</div><span id="post-2130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On a side-note, what do you mean by "valid"? All packets that are shown in Wireshark were captured on the network, so they are by definition "valid". Bare in mind that the way the packets were captured might have an influence on the way Wireshark is displaying them.</p><p>By far the most source of "errors" is capturing outgoing traffic on a host that has TCP checksum offloading enabled. In that case the packets pass Wireshark <strong>before</strong> the checksum has been calculated causing "Bad Checksum" errors. Of course the checksums will be correct once the NIC has calculated them before putting the packets on the wire(less). If you "delete" these packets from your tracefile, you have only half of the conversation left.</p><p>So... be really careful which packets you delete, as they might be packets that you do want to see in your tracefile, even though at some layer wireshark thinks they might be "invalid"...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '11, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2130" class="comments-container"></div><div id="comment-tools-2130" class="comment-tools"></div><div class="clear"></div><div id="comment-2130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

