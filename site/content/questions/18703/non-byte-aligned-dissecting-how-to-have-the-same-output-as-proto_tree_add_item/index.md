+++
type = "question"
title = "Non byte aligned dissecting: how to have the same output as proto_tree_add_item() ?"
description = '''Hi all, I&#x27;m dissecting non byte aligned fields. I use proto_tree_add_bits_item() it works pretty well but I would like to have the same output as proto_tree_add_item(). I don&#x27;t want to have the output like: ..10 1010 10.. .... &quot;value&quot;  But : value: 10 1010 10 (Like byte aligned standard output). My ...'''
date = "2013-02-18T05:29:00Z"
lastmod = "2013-03-07T08:36:00Z"
weight = 18703
keywords = [ "proto_tree_add_item", "display" ]
aliases = [ "/questions/18703" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Non byte aligned dissecting: how to have the same output as proto\_tree\_add\_item() ?](/questions/18703/non-byte-aligned-dissecting-how-to-have-the-same-output-as-proto_tree_add_item)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18703-score" class="post-score" title="current number of votes">0</div><span id="post-18703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I'm dissecting non byte aligned fields. I use proto_tree_add_bits_item() it works pretty well but I would like to have the same output as proto_tree_add_item().</p><p>I don't want to have the output like: ..10 1010 10.. .... "value" But : value: 10 1010 10 (Like byte aligned standard output).</p><p>My problem is that this output is very difficult to read because my fields are not aligned at all (once 6 bits, once 2 bits, once 18 bits ...). Wireshark display it in lines and it is difficult to figure out what we are looking for.</p><p>Is it possible to change the output or do I need to format it manually with proto_item_set_text() and re-write the output format of proto_tree_add_item() ?</p><p>Regards.</p><p>Eric</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proto_tree_add_item" rel="tag" title="see questions tagged &#39;proto_tree_add_item&#39;">proto_tree_add_item</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '13, 05:29</strong></p><img src="https://secure.gravatar.com/avatar/a3c7296b7e451716df45ef2737552881?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricST&#39;s gravatar image" /><p><span>EricST</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricST has no accepted answers">0%</span></p></div></div><div id="comments-container-18703" class="comments-container"></div><div id="comment-tools-18703" class="comment-tools"></div><div class="clear"></div><div id="comment-18703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18717"></span>

<div id="answer-container-18717" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18717-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18717-score" class="post-score" title="current number of votes">0</div><span id="post-18717-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go have a look at the <code>_format_value()</code> variants of <code>proto_tree_add_</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Feb '13, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-18717" class="comments-container"><span id="18771"></span><div id="comment-18771" class="comment"><div id="post-18771-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I looked for _format_value() variants but there is no variant for add_bits_item. Others are all byte aligned (offset in byte) and I would like to read several non aligned fields.</p><p>It works but it looks like:</p><p>.... ..00 = Field1: 0x00</p><p>0000 01.. = Field2: 1</p><p>.... ..00 1010 .... = Field3: 0x0a</p><p>.... 0001 1000 0110 1010 00.. = Field4: 0x0061a8</p><p>And it is not very human readable, I would prefer to hide the fact that it is not byte aligned and print as usually:</p><p>Field1: 0x00</p><p>Field2: 1</p><p>Field3: 0x0a</p><p>Field4: 0x0061a8</p><p>Do I need to get each field's value by _ret_value variant and make my own string ?</p><p>Thanks for help,</p><p>Eric</p></div><div id="comment-18771-info" class="comment-info"><span class="comment-age">(20 Feb '13, 07:25)</span> <span class="comment-user userinfo">EricST</span></div></div><span id="19270"></span><div id="comment-19270" class="comment"><div id="post-19270-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Could someone give me just a track to solve my issue?</p><p>Best regards, Eric</p></div><div id="comment-19270-info" class="comment-info"><span class="comment-age">(07 Mar '13, 05:47)</span> <span class="comment-user userinfo">EricST</span></div></div><span id="19271"></span><div id="comment-19271" class="comment"><div id="post-19271-score" class="comment-score"></div><div class="comment-text"><p>Forget about add_bits_item. Go look at proto_tree_add_uint[_format_value()]. This goes something like: 1. extract the byte field from the TVB, 2. extract your bitfield from that. 3. proto_tree_add_uint() / proto_tree_add_uint_format_value() are now free of bitmasks for representation.</p></div><div id="comment-19271-info" class="comment-info"><span class="comment-age">(07 Mar '13, 06:43)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="19272"></span><div id="comment-19272" class="comment"><div id="post-19272-score" class="comment-score"></div><div class="comment-text"><blockquote><p>And it is not very human readable, I would prefer to hide the fact that it is not byte aligned and print as usually</p></blockquote><p>N.B The output of proto_add_bits_item() is chosen so you can understand which bits makes up the field highligted in the bytes pane which I at least finds more useful than just displaying the field. I would think twice before going for a different format.</p></div><div id="comment-19272-info" class="comment-info"><span class="comment-age">(07 Mar '13, 07:08)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="19275"></span><div id="comment-19275" class="comment"><div id="post-19275-score" class="comment-score"></div><div class="comment-text"><p>I'm with Anders - the truth is your fields <em>are</em> bitfields, for all intents and purposes. It might be more confusing to someone using your dissector for the purpose of troubleshooting your protocol to see bytes that are not bytes. It might help you out too, to see them the way they really are. It usually helps me when I'm writing a dissector, anyway.</p></div><div id="comment-19275-info" class="comment-info"><span class="comment-age">(07 Mar '13, 08:36)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="19276"></span><div id="comment-19276" class="comment not_top_scorer"><div id="post-19276-score" class="comment-score"></div><div class="comment-text"><p>Also, if they're unaligned fields that are related and all together form a larger aligned byte field, you can always hide them in a subtree and have the top-level tree item show their aggregated aligned byte form. For example open any capture file with IP packets and look at the "Differentiated Services Field" of the IP header in Wireshark. It shows it as a subtree, with a descriptive top-level that gives the info, but if the user wants to see the details they can expand the subtree to see it as the bitfields.</p></div><div id="comment-19276-info" class="comment-info"><span class="comment-age">(07 Mar '13, 08:36)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-18717" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-18717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

