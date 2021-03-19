+++
type = "question"
title = "build error for 1.8 with VS 2013"
description = '''Hi, Started testing builds with VS 2013 Pro (nmake build), complaints about redefinitions: C:&#92;Program Files (x86)&#92;Windows Kits&#92;8.1&#92;include&#92;um&#92;ws2tcpip.h(531) : error C2373: &#x27;ws_inet_pton&#x27; : redefinition; different type modifiers  E:&#92;Wireshark&#92;trunk&#92;wsutil/inet_v6defs.h(44) : see declaration of &#x27;ws_i...'''
date = "2015-11-18T17:16:00Z"
lastmod = "2015-11-19T03:15:00Z"
weight = 47733
keywords = [ "vs2013", "nmake", "1.8", "build", "error" ]
aliases = [ "/questions/47733" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [build error for 1.8 with VS 2013](/questions/47733/build-error-for-18-with-vs-2013)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47733-score" class="post-score" title="current number of votes">0</div><span id="post-47733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Started testing builds with VS 2013 Pro (nmake build), complaints about redefinitions:</p><pre><code>C:\Program Files (x86)\Windows Kits\8.1\include\um\ws2tcpip.h(531) : error
C2373: &#39;ws_inet_pton&#39; : redefinition; different type modifiers

E:\Wireshark\trunk\wsutil/inet_v6defs.h(44) : see declaration of
&#39;ws_inet_pton&#39;

C:\Program Files (x86)\Windows Kits\8.1\include\um\ws2tcpip.h(548) : error
C2373: &#39;ws_inet_ntop&#39; : redefinition; different type modifiers

E:\Wireshark\trunk\wsutil/inet_v6defs.h(46) : see declaration of
&#39;ws_inet_ntop&#39;</code></pre><p>Looking at the definitions of these I can't see what's up.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vs2013" rel="tag" title="see questions tagged &#39;vs2013&#39;">vs2013</span> <span class="post-tag tag-link-nmake" rel="tag" title="see questions tagged &#39;nmake&#39;">nmake</span> <span class="post-tag tag-link-1.8" rel="tag" title="see questions tagged &#39;1.8&#39;">1.8</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '15, 17:16</strong></p><img src="https://secure.gravatar.com/avatar/0283ed843e0bdf9b028de468cf37bad8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Govindarao%20Bandaru&#39;s gravatar image" /><p><span>Govindarao B...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Govindarao Bandaru has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Nov '15, 03:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-47733" class="comments-container"><span id="47740"></span><div id="comment-47740" class="comment"><div id="post-47740-score" class="comment-score"></div><div class="comment-text"><p>Note that if you're trying to build 2.0, then the Windows build system has switched to CMake.</p></div><div id="comment-47740-info" class="comment-info"><span class="comment-age">(19 Nov '15, 02:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-47733" class="comment-tools"></div><div class="clear"></div><div id="comment-47733-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47734"></span>

<div id="answer-container-47734" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47734-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47734-score" class="post-score" title="current number of votes">0</div><span id="post-47734-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What version of the Wireshark source are you building from ?.</p><p>This problem was fixed in Dec 2013. The fix appeared in Wireshark-1.12 sources.</p><p>(See the wireshark-dev message thread beginning at: <a href="https://www.wireshark.org/lists/wireshark-dev/201312/msg00066.html">https://www.wireshark.org/lists/wireshark-dev/201312/msg00066.html</a></p><p>The actual commit: <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=3ccec6e23b8fa7f2601118660a1f01d325eb2dd4">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commit;h=3ccec6e23b8fa7f2601118660a1f01d325eb2dd4</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '15, 19:50</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-47734" class="comments-container"><span id="47743"></span><div id="comment-47743" class="comment"><div id="post-47743-score" class="comment-score"></div><div class="comment-text"><p>I am using wireshark- 1.8.15</p></div><div id="comment-47743-info" class="comment-info"><span class="comment-age">(19 Nov '15, 02:52)</span> <span class="comment-user userinfo">Govindarao B...</span></div></div><span id="47744"></span><div id="comment-47744" class="comment"><div id="post-47744-score" class="comment-score"></div><div class="comment-text"><blockquote>I am using wireshark- 1.8.15</blockquote><p>OK, VS2013 isn't supported for that version.</p></div><div id="comment-47744-info" class="comment-info"><span class="comment-age">(19 Nov '15, 03:15)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-47734" class="comment-tools"></div><div class="clear"></div><div id="comment-47734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

