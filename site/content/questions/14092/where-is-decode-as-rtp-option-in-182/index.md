+++
type = "question"
title = "Where is Decode as RTP option in 1.8.2?"
description = '''I normally work with Wireshark for tracing and troubleshooting VoIP calls, and whenever Wireshark shows me UDP packets instead of RTP, I am used to &#x27;Decode as...&#x27; RTP the UDP packets and then I see my RTP streams correctly. I just downloaded 1.8.2, and I can&#x27;t find RTP in the list of protocols insid...'''
date = "2012-09-06T07:53:00Z"
lastmod = "2012-09-06T08:36:00Z"
weight = 14092
keywords = [ "decode_rtp", "rtp" ]
aliases = [ "/questions/14092" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Where is Decode as RTP option in 1.8.2?](/questions/14092/where-is-decode-as-rtp-option-in-182)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14092-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I normally work with Wireshark for tracing and troubleshooting VoIP calls, and whenever Wireshark shows me UDP packets instead of RTP, I am used to 'Decode as...' RTP the UDP packets and then I see my RTP streams correctly. I just downloaded 1.8.2, and I can't find RTP in the list of protocols inside 'Decode as...' window any more. How can I tell now to Wireshark to decode some RTP streams as RTP if it is not doing so correctly from the beginning?</p></div><div id="question-tags" class="tags-container tags">decode_rtp rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '12, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/c41658c7603ba1306236bcd93c633b82?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_Flores&#39;s gravatar image" /><p>Christian_Fl...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_Flores has no accepted answers">0%</span></p></div></div><div id="comments-container-14092" class="comments-container"></div><div id="comment-tools-14092" class="comment-tools"></div><div class="clear"></div><div id="comment-14092-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14093"></span>

<div id="answer-container-14093" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14093-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Go to the RTP protocol preferences and tick "Try to decode RTP outside of conversations".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '12, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-14093" class="comments-container"><span id="14101"></span><div id="comment-14101" class="comment"><div id="post-14101-score" class="comment-score"></div><div class="comment-text"><p>Well, that didn't work. I still see a bunch of UDP packets that I know that are RTP and Wireshark could not decode them as RTP. Any other option?</p></div><div id="comment-14101-info" class="comment-info"><span class="comment-age">(06 Sep '12, 19:01)</span> Christian_Fl...</div></div><span id="14103"></span><div id="comment-14103" class="comment"><div id="post-14103-score" class="comment-score"></div><div class="comment-text"><p>If you can share the capture, or just a clip of some of these UDP packets on Bugzilla then by all means file a bugreport at <a href="http://bugs.wireshark.org">bugs.wireshark.org</a>.</p></div><div id="comment-14103-info" class="comment-info"><span class="comment-age">(06 Sep '12, 23:42)</span> Jaap ♦</div></div></div><div id="comment-tools-14093" class="comment-tools"></div><div class="clear"></div><div id="comment-14093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

