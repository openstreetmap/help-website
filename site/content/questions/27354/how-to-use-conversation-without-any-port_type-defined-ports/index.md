+++
type = "question"
title = "How to use conversation without any port_type defined ports"
description = '''Hello all, I have my own protocol what lays direct over ethernet. My dissector gets called over an defined ethertype and here is the problem. My protocol has a 4 x 8 bit header ... one field is a unique number. The header looks like this ethernet [destination address(6)][source address(6)][ethertype...'''
date = "2013-11-25T07:55:00Z"
lastmod = "2013-11-25T07:55:00Z"
weight = 27354
keywords = [ "conversation", "dissector" ]
aliases = [ "/questions/27354" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to use conversation without any port\_type defined ports](/questions/27354/how-to-use-conversation-without-any-port_type-defined-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27354-score" class="post-score" title="current number of votes">0</div><span id="post-27354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I have my own protocol what lays direct over ethernet. My dissector gets called over an defined ethertype and here is the problem.</p><p>My protocol has a 4 x 8 bit header ... one field is a unique number.</p><p>The header looks like this ethernet [destination address(6)][source address(6)][ethertype(2)] my protocol [my protocol field one(1)][my protocol field two(1)][my protocol number(1)] [my protocol field four(1)]</p><p>I would like to use the conversation_xxxx() functions on "destination address" and "my protocol number" is this somehow possible? Or is there another way, perhaps entering a custom port_type.</p><p>Thanks Gath</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '13, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/9b1dc01f2575b09d0852f7a4245a0318?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gatherer&#39;s gravatar image" /><p><span>Gatherer</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gatherer has no accepted answers">0%</span></p></div></div><div id="comments-container-27354" class="comments-container"></div><div id="comment-tools-27354" class="comment-tools"></div><div class="clear"></div><div id="comment-27354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

