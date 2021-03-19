+++
type = "question"
title = "error: passing argument 1 of &#x27;new_create_dissector_handle&#x27; from incompatible pointer type"
description = '''I wrote a plugin for wireshark 1.7.1 which was working fine then. When i tried same source with 1.9.0 , it gives me following error while make install. packet-extl2.c: In function &#x27;proto_reg_handoff_extl2&#x27;: packet-extl2.c:265: error: passing argument 1 of &#x27;new_create_dissector_handle&#x27; from incompati...'''
date = "2013-02-28T06:00:00Z"
lastmod = "2013-02-28T07:34:00Z"
weight = 18969
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/18969" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [error: passing argument 1 of 'new\_create\_dissector\_handle' from incompatible pointer type](/questions/18969/error-passing-argument-1-of-new_create_dissector_handle-from-incompatible-pointer-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18969-score" class="post-score" title="current number of votes">0</div><span id="post-18969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wrote a plugin for wireshark 1.7.1 which was working fine then. When i tried same source with 1.9.0 , it gives me following error while make install.</p><p>packet-extl2.c: In function 'proto_reg_handoff_extl2':<br />
packet-extl2.c:265: error: passing argument 1 of 'new_create_dissector_handle' from incompatible pointer type<br />
packet-extl2.c:266: error: implicit declaration of function 'dissector_add'<br />
make[3]: <strong><em>[packet-extl2.lo] Error 1<br />
make[3]: Leaving directory <code>/root/wireshark/wireshark-1.9.0/plugins/extl2' make[2]: *** [install-recursive] Error 1 make[2]: Leaving directory</code>/root/wireshark/wireshark-1.9.0/plugins'<br />
make[1]:</em></strong> [install-recursive] Error 1<br />
make[1]: Leaving directory `/root/wireshark/wireshark-1.9.0'<br />
make: *** [install] Error 2<br />
[<span class="__cf_email__" data-cfemail="482c213b3b2d2b3c273a08">[email protected]</span> wireshark-1.9.0]$</p><p>Here is my function which is creating problems:</p><p>void<br />
proto_reg_handoff_extl2(void)<br />
{<br />
dissector_handle_t extl2_handle;<br />
ip_handle = find_dissector("ip");<br />
extl2_handle = new_create_dissector_handle(dissect_extl2,proto_extl2);<br />
dissector_add("ethertype", 0x0800,extl2_handle);<br />
dissector_add("ethertype",0x86DD,extl2_handle);<br />
}</p><p>I am not sure what's wrong. dissect_extl2 returns "tvb_length" and has return type of static int. And also what header i am missing to get "implicit declaration of dissector_add" . Any help appreciated.</p><p>Thanks for your time.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p><span>yogeshg</span><br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Feb '13, 06:11</strong> </span></p></div></div><div id="comments-container-18969" class="comments-container"></div><div id="comment-tools-18969" class="comment-tools"></div><div class="clear"></div><div id="comment-18969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18972"></span>

<div id="answer-container-18972" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18972-score" class="post-score" title="current number of votes">1</div><span id="post-18972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yogeshg has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think the problem you're experiencing is that the prototype for the dissectors' top-level dissection routine has changed. Here's how I get around it with my (private) dissector (which I compile on into Wireshark versions before and after this change):</p><pre><code>static int
#if defined(VERSION_MAJOR) &amp;&amp; (VERSION_MAJOR &gt; 1 || (VERSION_MAJOR == 1 &amp;&amp; VERSION_MINOR &gt; 8))
dissect_XXX(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *data _U_)
#else
dissect_XXX(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
#endif</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span> </br></br></p></div></div><div id="comments-container-18972" class="comments-container"><span id="18979"></span><div id="comment-18979" class="comment"><div id="post-18979-score" class="comment-score"></div><div class="comment-text"><p>at least error is not coming now , thank you.</p></div><div id="comment-18979-info" class="comment-info"><span class="comment-age">(28 Feb '13, 07:34)</span> <span class="comment-user userinfo">yogeshg</span></div></div></div><div id="comment-tools-18972" class="comment-tools"></div><div class="clear"></div><div id="comment-18972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18970"></span>

<div id="answer-container-18970" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18970-score" class="post-score" title="current number of votes">1</div><span id="post-18970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try changing dissector_add() to dissector_add_uint().</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span> </br></br></p></div></div><div id="comments-container-18970" class="comments-container"></div><div id="comment-tools-18970" class="comment-tools"></div><div class="clear"></div><div id="comment-18970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

