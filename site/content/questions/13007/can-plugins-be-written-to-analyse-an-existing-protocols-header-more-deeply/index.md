+++
type = "question"
title = "Can plugins be written to analyse an existing protocol&#x27;s header more deeply?"
description = '''Hi!  I want to add a module to the wireshark source to extract more details from the Options field of the tcp header and display them. I found out elsewhere that I need to edit ip_tcp_opt structure of the ip_opts header file in the epan folder. However, I would prefer a plugin that does the the same...'''
date = "2012-07-25T22:06:00Z"
lastmod = "2012-07-26T23:34:00Z"
weight = 13007
keywords = [ "dissector", "postdissector", "tcp", "plugins" ]
aliases = [ "/questions/13007" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can plugins be written to analyse an existing protocol's header more deeply?](/questions/13007/can-plugins-be-written-to-analyse-an-existing-protocols-header-more-deeply)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13007-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13007-score" class="post-score" title="current number of votes">0</div><span id="post-13007-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! I want to add a module to the wireshark source to extract more details from the Options field of the tcp header and display them. I found out elsewhere that I need to edit ip_tcp_opt structure of the ip_opts header file in the epan folder. However, I would prefer a plugin that does the the same. I have been going through the READMEs, and from what little I've understood, plugins can be written for new dissectors. But I don't understand if one is allowed to write plugin that further analyse the fields of a protocol for which a dissector already exits. I'm very new to wireshark development, so can anyone please tell me if it should be possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-postdissector" rel="tag" title="see questions tagged &#39;postdissector&#39;">postdissector</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-plugins" rel="tag" title="see questions tagged &#39;plugins&#39;">plugins</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '12, 22:06</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p><span>SidR</span><br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Nov '12, 08:31</strong> </span></p></div></div><div id="comments-container-13007" class="comments-container"></div><div id="comment-tools-13007" class="comment-tools"></div><div class="clear"></div><div id="comment-13007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13021"></span>

<div id="answer-container-13021" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13021-score" class="post-score" title="current number of votes">1</div><span id="post-13021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SidR has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you can also use a Postdissector, written in Lua.</p><p><code>http://wiki.wireshark.org/Lua/Dissectors</code></p><blockquote><p><strong>Cite:</strong> A postdissector is a dissector registered to be called after every other dissector has been called already. <strong>These are handy as all protocol fields are already there so they can be accessed</strong> and they can add items to the dissection tree.</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '12, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jul '12, 09:00</strong> </span></p></div></div><div id="comments-container-13021" class="comments-container"><span id="13049"></span><div id="comment-13049" class="comment"><div id="post-13049-score" class="comment-score"></div><div class="comment-text"><p>This looks promising. Where can I find the register_postdissector() declaration in the source?</p></div><div id="comment-13049-info" class="comment-info"><span class="comment-age">(26 Jul '12, 22:44)</span> <span class="comment-user userinfo">SidR</span></div></div><span id="13051"></span><div id="comment-13051" class="comment"><div id="post-13051-score" class="comment-score"></div><div class="comment-text"><p>That's a built-in wslua function (there is no declaration). The <a href="http://wiki.wireshark.org/Lua/Dissectors#postdissectors">wiki link</a> above shows an example of how to use it. The <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Proto.html#lua_fn_register_postdissector_proto_">user manual</a> gives a brief description.</p></div><div id="comment-13051-info" class="comment-info"><span class="comment-age">(26 Jul '12, 22:55)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="13052"></span><div id="comment-13052" class="comment"><div id="post-13052-score" class="comment-score"></div><div class="comment-text"><p>I see. However, I was asking for the equivalent C function that can be found within the wireshark source. I just found found it in epan/packet.h so nevermind. Thanks a lot!</p></div><div id="comment-13052-info" class="comment-info"><span class="comment-age">(26 Jul '12, 23:08)</span> <span class="comment-user userinfo">SidR</span></div></div><span id="13054"></span><div id="comment-13054" class="comment"><div id="post-13054-score" class="comment-score">1</div><div class="comment-text"><p>BTW: There are some samples available.</p><blockquote><p><code>http://wiki.wireshark.org/Lua/Examples/PostDissector</code><br />
<code>http://diablohorn.wordpress.com/2010/12/05/dnscat-traffic-post-dissector/</code></p></blockquote></div><div id="comment-13054-info" class="comment-info"><span class="comment-age">(26 Jul '12, 23:34)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-13021" class="comment-tools"></div><div class="clear"></div><div id="comment-13021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13008"></span>

<div id="answer-container-13008" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13008-score" class="post-score" title="current number of votes">1</div><span id="post-13008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Probably not, and why should it be possible? Isn't it much better to enhance the existing dissector and offer the enhancment to the Wireshark project to have it included in the code base?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '12, 22:20</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span> </br></p></div></div><div id="comments-container-13008" class="comments-container"><span id="13009"></span><div id="comment-13009" class="comment"><div id="post-13009-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your quick reply Anders. And I agree with you, enhancing the existing dissector sounds cooler.</p></div><div id="comment-13009-info" class="comment-info"><span class="comment-age">(25 Jul '12, 22:33)</span> <span class="comment-user userinfo">SidR</span></div></div></div><div id="comment-tools-13008" class="comment-tools"></div><div class="clear"></div><div id="comment-13008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

