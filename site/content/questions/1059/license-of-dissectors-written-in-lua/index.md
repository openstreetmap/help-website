+++
type = "question"
title = "License of dissectors written in Lua?"
description = '''I started developing some dissectors in Lua for a non public communication protocol for a commercial product. According to discussions some time ago on the wireshark-dev mailing list (e.g. [Wireshark-dev] wireshark dissector and GPL) you&#x27;ll have to apply the GPL to your dissector, but I assume topic...'''
date = "2010-11-22T06:40:00Z"
lastmod = "2010-11-24T00:24:00Z"
weight = 1059
keywords = [ "gpl", "lua", "dissector" ]
aliases = [ "/questions/1059" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [License of dissectors written in Lua?](/questions/1059/license-of-dissectors-written-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1059-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1059-score" class="post-score" title="current number of votes">1</div><span id="post-1059-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I started developing some dissectors in Lua for a non public communication protocol for a commercial product. According to discussions some time ago on the wireshark-dev mailing list (e.g. <a href="http://www.mail-archive.com/wireshark-dev@wireshark.org/msg05823.html" title="[Wireshark-dev] wireshark dissector and GPL">[Wireshark-dev] wireshark dissector and GPL</a>) you'll have to apply the GPL to your dissector, but I assume topic of the discussion was a dissector written in C. Does this also apply to dissectors written in Lua?</p><p>Bonus question: Regardless how the code must be licensed, it will be used internally only and not selled or given to customers. Do I remember correctly, that the GPL does not force you to publish your code? As far as I remember I can develop tons of GPL code internally here and never have to show it to anyone. Right?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gpl" rel="tag" title="see questions tagged &#39;gpl&#39;">gpl</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '10, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/45504755fd94c65c58d8697cb53eeebb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LeSpocky&#39;s gravatar image" /><p><span>LeSpocky</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LeSpocky has no accepted answers">0%</span></p></div></div><div id="comments-container-1059" class="comments-container"></div><div id="comment-tools-1059" class="comment-tools"></div><div class="clear"></div><div id="comment-1059-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1071"></span>

<div id="answer-container-1071" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1071-score" class="post-score" title="current number of votes">1</div><span id="post-1071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="LeSpocky has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not a licensing lawyer, so I can't give an authoritative answer about the license for Lua code written for Wireshark (which is not, as far as I know, restricted to dissectors). The Lua interpreter itself is not GPL, but it's linked into a program that's GPLed, and the Wireshark version offers primitives that call GPLed code in Wireshark. I don't know whether that's sufficient to make Lua code that uses those primitives GPLed or not. (<em>Jaap</em>: Yes, it does make the GPL apply).</p><p>The GPL does <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0-faq.html#GPLRequireSourcePostedPublic">does <em>not</em> require that you make your code public</a>; it just requires that you make the source code available to whoever gets the binary code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '10, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Nov '10, 22:55</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-1071" class="comments-container"><span id="1074"></span><div id="comment-1074" class="comment"><div id="post-1074-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I don't know whether that's sufficient to make Lua code that uses those primitives GPLed or not.</p></blockquote><p>That is the very question. From my point of view I only write a script which is interpreted by a GPL software. Does this force me to license the script under GPL?</p><p>(I understand I'm forced to, if I write C code which is compiled and directly linked to Wireshark.)</p><p>Thanks for clarifying the publication issue.</p></div><div id="comment-1074-info" class="comment-info"><span class="comment-age">(23 Nov '10, 01:15)</span> <span class="comment-user userinfo">LeSpocky</span></div></div><span id="1077"></span><div id="comment-1077" class="comment"><div id="post-1077-score" class="comment-score">2</div><div class="comment-text"><p>As said: making use of functions in Wireshark makes the GPL apply. This condition is programming language agnostic.</p><p>In order to stay clear of GPL'ed code your code has to stay 'at arms length', either communicate through sockets or other common communication channels, or make OS API calls.</p></div><div id="comment-1077-info" class="comment-info"><span class="comment-age">(23 Nov '10, 05:49)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="1106"></span><div id="comment-1106" class="comment"><div id="post-1106-score" class="comment-score"></div><div class="comment-text"><p>Ok thank you, the last explanation was sufficient (although I'm still a bit confused about this editing existing posts thing). :-)</p></div><div id="comment-1106-info" class="comment-info"><span class="comment-age">(24 Nov '10, 00:24)</span> <span class="comment-user userinfo">LeSpocky</span></div></div></div><div id="comment-tools-1071" class="comment-tools"></div><div class="clear"></div><div id="comment-1071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

