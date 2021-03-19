+++
type = "question"
title = "Enabling reassembly of TCP packets"
description = '''According to this guide: https://www.wireshark.org/docs/wsug_html_chunked/AppMessages.html you can enable TCP packet reassembly through the UI with Edit&amp;gt;Preferences. But I didn&#x27;t see anything that would suggest that aside from &quot;Allow subdissector to reassemble TCP stream&quot; in the Protocols&amp;gt;TCP ...'''
date = "2011-02-11T15:58:00Z"
lastmod = "2011-02-14T10:20:00Z"
weight = 2289
keywords = [ "reassembly", "reassemble", "tcp" ]
aliases = [ "/questions/2289" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Enabling reassembly of TCP packets](/questions/2289/enabling-reassembly-of-tcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2289-score" class="post-score" title="current number of votes">1</div><span id="post-2289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>According to this guide:</p><p><a href="https://www.wireshark.org/docs/wsug_html_chunked/AppMessages.html">https://www.wireshark.org/docs/wsug_html_chunked/AppMessages.html</a></p><p>you can enable TCP packet reassembly through the UI with Edit&gt;Preferences. But I didn't see anything that would suggest that aside from "Allow subdissector to reassemble TCP stream" in the Protocols&gt;TCP panel.</p><p>But according to this doc:</p><p><a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectReassemble.html">http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectReassemble.html</a></p><p>you can do it through your code with the tcp_dissect_pdus function.</p><p>I would rather do it through it the UI as it would be more convenient. Anyone how I can do that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-reassemble" rel="tag" title="see questions tagged &#39;reassemble&#39;">reassemble</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '11, 15:58</strong></p><img src="https://secure.gravatar.com/avatar/3d3535b19a6debac9e2b855465a2027b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rodayo&#39;s gravatar image" /><p><span>Rodayo</span><br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rodayo has no accepted answers">0%</span></p></div></div><div id="comments-container-2289" class="comments-container"></div><div id="comment-tools-2289" class="comment-tools"></div><div class="clear"></div><div id="comment-2289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2310"></span>

<div id="answer-container-2310" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2310-score" class="post-score" title="current number of votes">2</div><span id="post-2310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rodayo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To clarify a bit:</p><p>Reassembly of packets for protocols running on top of TCP requires that:</p><ol><li>The dissector for the protocol running on top of TCP support it - for some protocols, using tcp_dissect_pdus() in the dissector can do that (but not for all protocols);</li><li>If that dissector has a preference to control whether to do reassembly of packets, that preference is set to "do reassembly";</li><li>The "Allow subdisector to reassemble TCP stream" preference for TCP is set to "allow".</li></ol><p>If the first of those is already true, you can do it through the UI, by turning on the "Allow subdisector to reassemble TCP stream" preference and, if the dissector in question has a preference to control whether to do reassembly, turning that preference on as well.</p><p>If the first of those is <em>not</em> already true, either you or somebody else will have to modify the dissector to support reassembly; once that's done, reassembly could be controlled through the UI.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '11, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2310" class="comments-container"><span id="2326"></span><div id="comment-2326" class="comment"><div id="post-2326-score" class="comment-score"></div><div class="comment-text"><p>I figured that was probably the case. But like you said, I've added the reassembly code to my source and it was already enabled through the UI.</p><p>But the code doesn't actually change anything. The full data is still being split across multiple packets...</p></div><div id="comment-2326-info" class="comment-info"><span class="comment-age">(14 Feb '11, 10:20)</span> <span class="comment-user userinfo">Rodayo</span></div></div></div><div id="comment-tools-2310" class="comment-tools"></div><div class="clear"></div><div id="comment-2310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2291"></span>

<div id="answer-container-2291" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2291-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2291-score" class="post-score" title="current number of votes">1</div><span id="post-2291-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TCP packet reassembly is in fact controlled through the "Allow subdisector to reassemble TCP stream" in the TCP protocol preferences, if that's what you're asking.</p><p>Using "Edit" -&gt; "Preferences" is a little too much clicking work for me though - if you're running Wireshark 1.2.x or later you can just select a frame containing TCP headers, select the "Transmission Control Protocol" header line in the decode and use the popup menu where you find the same settings listed in the "Protocol Settings" submenu. That way you can access all protocol settings a lot faster than always going into the preferences dialog.</p><p>The third way would be to create different profiles, one with reassembly enabled and one with reassembly disabled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '11, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2291" class="comments-container"><span id="2293"></span><div id="comment-2293" class="comment"><div id="post-2293-score" class="comment-score">1</div><div class="comment-text"><p>Reassembly is only possible if the protocol running on top of TCP allows it e.g thetre is code in the dissector to handle reassembly as the TCP dissector has no notion about the content of the TCP payload.</p></div><div id="comment-2293-info" class="comment-info"><span class="comment-age">(12 Feb '11, 04:03)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="2294"></span><div id="comment-2294" class="comment"><div id="post-2294-score" class="comment-score"></div><div class="comment-text"><p>True, good additional info :-)</p></div><div id="comment-2294-info" class="comment-info"><span class="comment-age">(12 Feb '11, 04:16)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-2291" class="comment-tools"></div><div class="clear"></div><div id="comment-2291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

