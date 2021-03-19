+++
type = "question"
title = "Cisco WIDS parsing"
description = '''The actual decoder for CWIDS displays many fields as unknown. Do you have any information about these fields ? I am specifically interested by fields showing the Power lever. (I have reasons to think it is the last byte of the CWIDS header but whithout any proof). Do you plan to improve the decoder ...'''
date = "2016-05-08T04:54:00Z"
lastmod = "2016-05-08T11:49:00Z"
weight = 52306
keywords = [ "cwids", "cisco", "wids" ]
aliases = [ "/questions/52306" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cisco WIDS parsing](/questions/52306/cisco-wids-parsing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52306-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The actual decoder for CWIDS displays many fields as unknown. Do you have any information about these fields ? I am specifically interested by fields showing the Power lever. (I have reasons to think it is the last byte of the CWIDS header but whithout any proof). Do you plan to improve the decoder for this protocol ?</p><p>Best regards, And thanks for all K</p></div><div id="question-tags" class="tags-container tags">cwids cisco wids</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '16, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/179741848f421342036af539577996cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ken1234&#39;s gravatar image" /><p>ken1234<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ken1234 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 May '16, 11:50</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-52306" class="comments-container"></div><div id="comment-tools-52306" class="comment-tools"></div><div class="clear"></div><div id="comment-52306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52317"></span>

<div id="answer-container-52317" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52317-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the source code (packet-cisco-wids.c):</p><pre><code>/* 2do:
 *  - Find out more about the contents of the capture header
 *  - Protect the address fields etc (all columns?)
 *  - Create subelements and put each header and packet into it
 *  - fuzz-test the dissector
 *  - Find some heuristic to detect the packet automagically and
 *    convert dissector into a heuristic dissector
 *  - Is the TRY/CATCH stuff OK?
 */</code></pre><p>So nothing planned. Access to a specification document would be nice, along with some sample captures.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '16, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 May '16, 15:24</p></div></div><div id="comments-container-52317" class="comments-container"></div><div id="comment-tools-52317" class="comment-tools"></div><div class="clear"></div><div id="comment-52317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52318"></span>

<div id="answer-container-52318" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52318-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Do you have any information about these fields ?</p></blockquote><p>If "you" refers to all the people who have contributed to that dissector, the answer is "no, otherwise they would have used that information to add support for those fields to the dissector."</p><blockquote><p>Do you plan to improve the decoder for this protocol ?</p></blockquote><p>If we could get more information about the protocol, we would use it to improve the dissector. Do you have any idea where we could get a complete specification of the protocol?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '16, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-52318" class="comments-container"><span id="52323"></span><div id="comment-52323" class="comment"><div id="post-52323-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thank you for your answers.</p><p>I think I read somewhere that omnipeek could decode the headers, but I am not sure and i do not have it. I searched on cisco site but got nothing. I can provide some capture samples "for further use" within one or two days if that can help.</p><p>Thanks again K</p></div><div id="comment-52323-info" class="comment-info"><span class="comment-age">(08 May '16, 15:13)</span> ken1234</div></div><span id="52325"></span><div id="comment-52325" class="comment"><div id="post-52325-score" class="comment-score"></div><div class="comment-text"><p>This is <a href="https://en.wikipedia.org/wiki/Reverse_engineering">reverse engineering</a> of the protocol; more captures, without any interpretation from some other program, won't necessarily help unless a pattern can be detected from the captures. If you have some good reason to think the last byte is a power level, e.g. if some interpretation of its value matches the power levels that you're expecting to see or that you're seeing from some other source, then we could add code to dissect it as such - but if you need proof, you're only going to get it from Cisco or from a program for which there's a reason to trust it (for example, perhaps Wildpackets^WSavvius got a protocol spec and are using it to capture a stream of Cisco WIDS packets just as it can capture packets from some access points).</p></div><div id="comment-52325-info" class="comment-info"><span class="comment-age">(08 May '16, 15:41)</span> Guy Harris ♦♦</div></div><span id="52373"></span><div id="comment-52373" class="comment"><div id="post-52373-score" class="comment-score"></div><div class="comment-text"><p>Well,</p><p>You are perfectly right. I will try to find more information about this header. I will tell you if I find something valuable.</p><p>Best regards.</p><p>K.</p></div><div id="comment-52373-info" class="comment-info"><span class="comment-age">(09 May '16, 14:26)</span> ken1234</div></div></div><div id="comment-tools-52318" class="comment-tools"></div><div class="clear"></div><div id="comment-52318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

