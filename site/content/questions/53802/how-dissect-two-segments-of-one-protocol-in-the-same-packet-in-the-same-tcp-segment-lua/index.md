+++
type = "question"
title = "How dissect two segments of one protocol in the same packet , in the same TCP segment (LUA)?"
description = '''I want to use my bgp dissector to dissect other BGP segments in the same packet. I don´t know how to recall dissection function.  Now only dissect the first BGP segment. I want to do like in the picture example : 3 diferent BGP segment in the same TCP segment. '''
date = "2016-07-04T04:23:00Z"
lastmod = "2016-07-06T07:57:00Z"
weight = 53802
keywords = [ "bgp", "lua", "dissector", "tcp" ]
aliases = [ "/questions/53802" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How dissect two segments of one protocol in the same packet , in the same TCP segment (LUA)?](/questions/53802/how-dissect-two-segments-of-one-protocol-in-the-same-packet-in-the-same-tcp-segment-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53802-score" class="post-score" title="current number of votes">0</div><span id="post-53802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to use my bgp dissector to dissect other BGP segments in the same packet. I don´t know how to recall dissection function. Now only dissect the first BGP segment.</p><p>I want to do like in the picture example : 3 diferent BGP segment in the same TCP segment.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2016-07-04_13-17-25.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bgp" rel="tag" title="see questions tagged &#39;bgp&#39;">bgp</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '16, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/0164b3a0b6fca8e2931eb42defb1ebfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="javiguembe&#39;s gravatar image" /><p><span>javiguembe</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="javiguembe has no accepted answers">0%</span></p></img></div></div><div id="comments-container-53802" class="comments-container"><span id="53803"></span><div id="comment-53803" class="comment"><div id="post-53803-score" class="comment-score"></div><div class="comment-text"><p>My dissector take all tcp segment as buffer but i need to limit with the BGP segment len and repeat the proccess while tcp segment len &gt;0 . how?</p></div><div id="comment-53803-info" class="comment-info"><span class="comment-age">(04 Jul '16, 04:48)</span> <span class="comment-user userinfo">javiguembe</span></div></div></div><div id="comment-tools-53802" class="comment-tools"></div><div class="clear"></div><div id="comment-53802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53821"></span>

<div id="answer-container-53821" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53821-score" class="post-score" title="current number of votes">0</div><span id="post-53821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>EDIT:</strong> answer improved according to what <span><span>@grahamb</span></span> has pointed in a comment below.</p><p>Although borders of PDUs of application protocols using TCP as transport are often aligned with borders of TCP packets, it is not a law, so your dissector should be able to treat the TCP payload as a continuous stream and find the PDUs in it regardless the packet border. So if you finish dissecting a BGP segment and there is still data in the tvb, simply <code>return</code> the length of the part of the tvb you have processed, the TCP dissector will invoke your one again, giving it the rest of the tvb and the proper branch in the dissection tree to hook the result to. And this will repeat until there is either nothing left in the payload to be dissected, or until the remainder of the payload is just the beginning of a PDU.</p><p>In the latter case, i.e. if you reach the end of the tvb and your application protocol's PDU is not complete yet, you have to <code>return</code> zero as the number of tvb bytes you could dissect successfully. This tells the TCP dissector that you could not completely dissect the contents of the tvb as it was, and it will prepend this remainder to the payload of the next packet of the TCP stream when invoking your dissector on that packet.</p><p>Just to emphasize what is implicitly mentioned above: there are also cases where the capture starts mid-session, so your application protocol dissector should be able to synchronize on the stream also if it starts in the middle of a PDU. I don't know whether it can happen in case of BGP, but if I've understood you well, you've only chosen BGP as a model case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jul '16, 00:46</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jul '16, 09:48</strong> </span></p></div></div><div id="comments-container-53821" class="comments-container"><span id="53823"></span><div id="comment-53823" class="comment"><div id="post-53823-score" class="comment-score"></div><div class="comment-text"><p>For C-based dissectors, they just process each PDU separately, and return the number of bytes they dissected, and the TCP dissector calls sub-dissectors again if there are still bytes left to be processed. Are Lua dissectors not the same?</p></div><div id="comment-53823-info" class="comment-info"><span class="comment-age">(05 Jul '16, 01:35)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53840"></span><div id="comment-53840" class="comment"><div id="post-53840-score" class="comment-score"></div><div class="comment-text"><p>There is no reason why it should behave differently for Lua dissectors than for C dissectors (especially as the TCP dissector itself is the same and it doesn't even know whether the dissector it invokes is a C or Lua one), but I wasn't sure whether it cycles through the payload until all of it is dissected or whether it can only handle a single "blind tail". So I'll edit my Answer accordingly.</p></div><div id="comment-53840-info" class="comment-info"><span class="comment-age">(05 Jul '16, 09:27)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-53821" class="comment-tools"></div><div class="clear"></div><div id="comment-53821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53859"></span>

<div id="answer-container-53859" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53859-score" class="post-score" title="current number of votes">0</div><span id="post-53859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are many examples and sample Lua scripts available on the Wireshark wiki that you can use to help you solve this problem. For example, the <code>fpm.lua</code> script, written by <a href="https://ask.wireshark.org/users/4318/hadriel">Hadriel Kaplan</a> and available on either the <a href="https://wiki.wireshark.org/Lua/Examples">Lua Examples</a> or <a href="https://wiki.wireshark.org/Contrib">Contrib</a> wiki pages, seems to be written to illustrate the exact problem of TCP reassembly in Lua.</p><p>Some useful Lua-related links then:</p><ul><li><a href="https://wiki.wireshark.org/Lua">Wireshark Lua (wiki page)</a></li><li><a href="https://wiki.wireshark.org/Lua/Examples">Wireshark Lua Examples (wiki page)</a></li><li><a href="https://wiki.wireshark.org/Lua/Dissectors">Wireshark Lua Dissectors (wiki page)</a></li><li><a href="https://wiki.wireshark.org/Lua/Taps">Wireshark Lua Taps (wiki page)</a></li><li><a href="https://wiki.wireshark.org/Contrib">Wireshark Contributed scripts, macros, colouring rules and plugins (wiki page)</a></li><li><a href="https://www.wireshark.org/docs/wsdg_html_chunked/wsluarm.html">Chapter 10. Lua Support in Wireshark (Wireshark Developer's Guide)</a></li><li><a href="https://www.wireshark.org/docs/wsdg_html_chunked/wsluarm_modules.html">Chapter 11. Wireshark's Lua API Reference Manual (Wireshark Developer's Guide)</a></li><li><a href="https://wiki.wireshark.org/LuaAPI">Wireshark Lua API Reference Manual Addendum (wiki page)</a></li><li><a href="http://lua-users.org/wiki/LuaDirectory">Lua Directory</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '16, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-53859" class="comments-container"></div><div id="comment-tools-53859" class="comment-tools"></div><div class="clear"></div><div id="comment-53859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

