+++
type = "question"
title = "Decode RTP outside of conversations (WS 2.0)"
description = '''I recently installed the latest version of Wireshark (version 2.0.0). I am having a difficult time decoding voice traffic. In the older version I could modify my protocol preferences for RTP using these steps. &quot;Decode RTP outside of conversations&quot; enabled (in Edit-&amp;gt;Preferences-&amp;gt;Protocols-&amp;gt;R...'''
date = "2015-12-01T13:13:00Z"
lastmod = "2015-12-01T18:12:00Z"
weight = 48159
keywords = [ "capture", "udp", "voice", "wireshark-2.0", "rtp" ]
aliases = [ "/questions/48159" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Decode RTP outside of conversations (WS 2.0)](/questions/48159/decode-rtp-outside-of-conversations-ws-20)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48159-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently installed the latest version of Wireshark (version 2.0.0). I am having a difficult time decoding voice traffic. In the older version I could modify my protocol preferences for RTP using these steps.</p><p>"Decode RTP outside of conversations" enabled (in Edit-&gt;Preferences-&gt;Protocols-&gt;RTP).</p><p>In the new version this is not an option. Some forum talked about going through each packet and right clicking on it and selecting decode as. This is very cumbersome. Isn't there a way to universally set this preference?</p></div><div id="question-tags" class="tags-container tags">capture udp voice wireshark-2.0 rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '15, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/da3ac9a37a91755ddd0a66045e5cdc39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="livef7ee&#39;s gravatar image" /><p>livef7ee<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="livef7ee has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Dec '15, 01:15</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-48159" class="comments-container"></div><div id="comment-tools-48159" class="comment-tools"></div><div class="clear"></div><div id="comment-48159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48170"></span>

<div id="answer-container-48170" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48170-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are two ways to get UDP packets to be dissected as RTP if Wireshark doesn't see a session set up as UDP and automatically dissect them as UDP:</p><ol><li>explicitly say "decode this port as UDP";</li><li>enable the heuristic RTP-over-UDP dissector, which looks at all UDP packets to see if they look like RTP packets and, if so, dissects them as RTP.</li></ol><p>The first of those is what is done with "Decode As".</p><p>The second of those is what used to be done with the "Decode RTP outside of conversations" and is now done with the "Enabled Protocols" dialog - enable the "RTP over UDP" dissector (which, arguably somewhat confusingly, only controls whether the <em>heuristic</em> dissector is enabled).</p><p>So there isn't a "Decode RTP outside of conversations" option, but there is a setting that does the same thing, it's now in the "Enabled Protocols" dialog.</p><p>(The heuristic dissector is disabled by default, because it's a very weak heuristic (a better heuristic might not be possible) and thus would identify a lot of non-RTP traffic as RTP.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '15, 18:12</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-48170" class="comments-container"><span id="48172"></span><div id="comment-48172" class="comment"><div id="post-48172-score" class="comment-score"></div><div class="comment-text"><p>@Guy Harris, if I get it right, the identification of RTP streams belonging to VoIP calls whose signalling messages are present in the capture is completely independent of the "weak heuristisc" you've mentioned above, right? I'm asking because while this worked in let's say 95 % of cases in 1.12.x, it behaves much more randomly now (like e.g. the UDP flows are not identified as RTP until you display the VoIP calls ladder diagram). Has a bug been filed already or should I file one?</p></div><div id="comment-48172-info" class="comment-info"><span class="comment-age">(02 Dec '15, 00:31)</span> sindy</div></div><span id="48208"></span><div id="comment-48208" class="comment"><div id="post-48208-score" class="comment-score"></div><div class="comment-text"><blockquote><p>if I get it right, the identification of RTP streams belonging to VoIP calls whose signalling messages are present in the capture is completely independent of the "weak heuristisc" you've mentioned above, right?</p></blockquote><p>Correct.</p><blockquote><p>Has a bug been filed already or should I file one?</p></blockquote><p>File one.</p></div><div id="comment-48208-info" class="comment-info"><span class="comment-age">(02 Dec '15, 11:35)</span> Guy Harris ♦♦</div></div><span id="48237"></span><div id="comment-48237" class="comment"><div id="post-48237-score" class="comment-score"></div><div class="comment-text"><p>This helped me. My captures (mostly) are on interfaces only passing voice traffic. This makes it much easier to gather info. Thx.</p></div><div id="comment-48237-info" class="comment-info"><span class="comment-age">(03 Dec '15, 09:01)</span> livef7ee</div></div><span id="48239"></span><div id="comment-48239" class="comment"><div id="post-48239-score" class="comment-score"></div><div class="comment-text"><p>As you've just said Guy's answer has helped you, please click the "accept" icon - nobody else but you can do it. The goal is to mark useful answers for other people coming with the same question. See FAQ for details.</p></div><div id="comment-48239-info" class="comment-info"><span class="comment-age">(03 Dec '15, 09:53)</span> sindy</div></div></div><div id="comment-tools-48170" class="comment-tools"></div><div class="clear"></div><div id="comment-48170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

