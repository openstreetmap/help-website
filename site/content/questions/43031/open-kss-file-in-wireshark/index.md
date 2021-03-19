+++
type = "question"
title = "Open KSS file in wireshark"
description = '''Hello, Is it possible to somehow open KSS file (KISS - ax.25) file in wireshark ?  Looks like wireshark already has some support for it There&#x27;s some reference to kiss-framing.lua file here https://wiki.wireshark.org/AmateurRadioProtocolFamily But the file itself is not attached. I&#x27;m contemplating wr...'''
date = "2015-06-10T03:21:00Z"
lastmod = "2015-06-10T05:24:00Z"
weight = 43031
keywords = [ "lua", "ax.25-kiss" ]
aliases = [ "/questions/43031" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Open KSS file in wireshark](/questions/43031/open-kss-file-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43031-score" class="post-score" title="current number of votes">0</div><span id="post-43031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Is it possible to somehow open KSS file (KISS - ax.25) file in wireshark ? Looks like wireshark already has some support for it</p><p>There's some reference to kiss-framing.lua file here <a href="https://wiki.wireshark.org/AmateurRadioProtocolFamily">https://wiki.wireshark.org/AmateurRadioProtocolFamily</a></p><p>But the file itself is not attached.</p><p>I'm contemplating writing lua file reader but I might be reinventing the wheel.</p><p>Thanks</p><p>m</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-ax.25-kiss" rel="tag" title="see questions tagged &#39;ax.25-kiss&#39;">ax.25-kiss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '15, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-43031" class="comments-container"></div><div id="comment-tools-43031" class="comment-tools"></div><div class="clear"></div><div id="comment-43031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43040"></span>

<div id="answer-container-43040" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43040-score" class="post-score" title="current number of votes">0</div><span id="post-43040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The AX.25 KISS dissector is not a Lua script, but is a <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-ax25-kiss.c;h=f9743d56da5781ba6d6a5fc4292ab3771803eeb4;hb=refs/heads/master-1.12">built-in dissector</a> in Wireshark source code.</p><p>According to the comments in the code, it supports the Linux capture format, and the small Lua script on the wiki page allows to support an encapsulation over UDP (or TCP).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '15, 05:24</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-43040" class="comments-container"></div><div id="comment-tools-43040" class="comment-tools"></div><div class="clear"></div><div id="comment-43040-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

