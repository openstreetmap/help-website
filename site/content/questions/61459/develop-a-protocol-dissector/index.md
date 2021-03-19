+++
type = "question"
title = "Develop a protocol dissector"
description = '''I want to integrate two new dissectors to Wireshark. First dissector is packet-foo.c and second is packet-poo.c. in these dissectors we want, if poo existence field value is 0x01 in foo, then poo dissects packet. FOO Protocol FOO DATA Type (1 Byte) FOO FLAG (1 Byte) FOO DATA (5 Byte) POO EXSISTANCE ...'''
date = "2017-05-17T06:42:00Z"
lastmod = "2017-05-18T04:31:00Z"
weight = 61459
keywords = [ "develop", "dissector", "protocol" ]
aliases = [ "/questions/61459" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Develop a protocol dissector](/questions/61459/develop-a-protocol-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61459-score" class="post-score" title="current number of votes">0</div><span id="post-61459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to integrate two new dissectors to Wireshark. First dissector is packet-foo.c and second is packet-poo.c. in these dissectors we want, if poo existence field value is 0x01 in foo, then poo dissects packet.</p><p>FOO Protocol</p><p>FOO DATA Type (1 Byte)</p><p>FOO FLAG (1 Byte)</p><p>FOO DATA (5 Byte)</p><p>POO EXSISTANCE (1 Byte)</p><p>I write in packet-poo.c (proto_reg_handoff_poo function) :</p><p>proto_reg_handoff_poo(void) {</p><p>static dissector_handle_t poo_handle;</p><p>poo_handle = create_dissector_handle(dissect_poo, proto_poo);</p><p>dissector_add_uint("poo.existance", 0x01, poo_handle);</p><p>register_dissector("poo", dissect_poo, proto_poo);</p><p>} But it doesn’t work,what is the problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-develop" rel="tag" title="see questions tagged &#39;develop&#39;">develop</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '17, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/28d5dc133c31193058a99892f00a0213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ghader&#39;s gravatar image" /><p><span>ghader</span><br />
<span class="score" title="61 reputation points">61</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ghader has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 May '17, 06:46</strong> </span></p></div></div><div id="comments-container-61459" class="comments-container"></div><div id="comment-tools-61459" class="comment-tools"></div><div class="clear"></div><div id="comment-61459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61460"></span>

<div id="answer-container-61460" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61460-score" class="post-score" title="current number of votes">1</div><span id="post-61460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ghader has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to use a dissector table named "poo.existence", you must create it in packet-foo.c with register_table_dissector() and once you get the poo.existence field, call the table with dissector_try_uint_new(). I recommend you to have a look at the various dissectors using a dissector table, like proto-ip.c.</p><p>That said, if you have a single value to be filled in this dissector table, it might be easier to call the poo dissector directly when poo.existence = 1. Simply find the corresponding handle by using find_dissector() in proto_reg_handoff_foo() and call the dissector with call_dissector() or call_dissector_with_data(). Again you will find plenty of exemples in the source code.</p><p>Note also that the call to register_dissector("poo", dissect_poo, proto_poo) must be done in proto_register_poo(), not in proto_reg_handoff_poo(). This function returns a handle that can be used as input for dissector_add_uint().</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '17, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 May '17, 07:18</strong> </span></p></div></div><div id="comments-container-61460" class="comments-container"><span id="61464"></span><div id="comment-61464" class="comment"><div id="post-61464-score" class="comment-score"></div><div class="comment-text"><p>thank you very much, I look at the packet-ip.c but i dont understand correctly.</p><p>first in packet-foo.c define :</p><p>static dissector_table_t foo_dissector_table;</p><p>then in proto_register_foo() function :</p><p>foo_dissector_table = register_dissector_table("foo.existance", "FOO EXISTANCE",proto_foo, FT_UINT8, BASE_DEC);</p><p>but I don’t understand how to use dissector_try_uint_new.</p><p>dissector_try_uint_new(foo_dissector_table,…….)</p></div><div id="comment-61464-info" class="comment-info"><span class="comment-age">(17 May '17, 09:56)</span> <span class="comment-user userinfo">ghader</span></div></div><span id="61465"></span><div id="comment-61465" class="comment"><div id="post-61465-score" class="comment-score"></div><div class="comment-text"><p>You need to create a new tvb containing the payload you want to send to your poo dissector, and call it via dissector_try_uint(foo_dissector_table, 1, tvb_payload, pinfo, tree);</p><p>You can find plenty of examples in the code.</p></div><div id="comment-61465-info" class="comment-info"><span class="comment-age">(17 May '17, 10:34)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="61472"></span><div id="comment-61472" class="comment"><div id="post-61472-score" class="comment-score"></div><div class="comment-text"><p>excuse me, how can i create a new tvb containing the payload i want to send to my poo dissector?</p></div><div id="comment-61472-info" class="comment-info"><span class="comment-age">(17 May '17, 21:41)</span> <span class="comment-user userinfo">ghader</span></div></div><span id="61482"></span><div id="comment-61482" class="comment"><div id="post-61482-score" class="comment-score"></div><div class="comment-text"><p>if i want to use find_dissector and call_dissector ,In packet-foo.c I define:</p><p>In proto_reg_handoff_foo():</p><p>find_dissector(poo);</p><blockquote><p>In dissect_foo(tvbuff <em>tvb,packet_info</em> pinfo,proto_tree <em>tree <em>U</em>,void</em> data <em>U</em>):</p></blockquote><p>guint8 poo_e= tvb_get_guint8(tvb,7)</p><p>if (poo_e==01)</p><p>call_dissector(poo_handler,tvb,pinfo,tree)</p><p>In packet-poo.c I define:</p><p>In proto_register_poo():</p><p>register_dissector("poo", dissect_poo, proto_poo)</p><p>but,these chnges not work correctly,what is the problem?</p></div><div id="comment-61482-info" class="comment-info"><span class="comment-age">(18 May '17, 00:51)</span> <span class="comment-user userinfo">ghader</span></div></div><span id="61484"></span><div id="comment-61484" class="comment"><div id="post-61484-score" class="comment-score">1</div><div class="comment-text"><p>I guess in proto_reg_handoff_foo() you wrote:</p><p>poo_handler = find_dissector("poo");</p><p>right?</p><p>How does it fail? Is poo_handler == NULL? of is call_dissector() not called?</p><p>With a debugger you should easily find where your error is.</p></div><div id="comment-61484-info" class="comment-info"><span class="comment-age">(18 May '17, 02:14)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="61486"></span><div id="comment-61486" class="comment not_top_scorer"><div id="post-61486-score" class="comment-score"></div><div class="comment-text"><p>i use this format and work correctly.</p><p>if (poo_e==01)</p><p>tvbuff_t tvb_new_subset_remaining(tvb,offset);</p><p>call_dissector(poo_handler,tvb,pinfo,tree);</p></div><div id="comment-61486-info" class="comment-info"><span class="comment-age">(18 May '17, 04:31)</span> <span class="comment-user userinfo">ghader</span></div></div></div><div id="comment-tools-61460" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-61460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

