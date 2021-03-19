+++
type = "question"
title = "Decoding Vonage call via PCAP"
description = '''Hello, I have an old phone call with my Grandfather (now passed - why I am trying to extract the audio) where I was recording the call to him via my Vonage line and Wireshark. This was from February of 2007 if that helps. When opening the PCAP and selecting Telephony/VoIP calls, 0 calls are detected...'''
date = "2015-11-07T22:19:00Z"
lastmod = "2015-11-08T00:37:00Z"
weight = 47363
keywords = [ "vonage", "pcap", "extract", "voip" ]
aliases = [ "/questions/47363" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding Vonage call via PCAP](/questions/47363/decoding-vonage-call-via-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47363-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47363-score" class="post-score" title="current number of votes">0</div><span id="post-47363-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have an old phone call with my Grandfather (now passed - why I am trying to extract the audio) where I was recording the call to him via my Vonage line and Wireshark. This was from February of 2007 if that helps.</p><p>When opening the PCAP and selecting Telephony/VoIP calls, 0 calls are detected.</p><p>Just hoping someone may have an idea as to how I can extract this call as audio once again.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vonage" rel="tag" title="see questions tagged &#39;vonage&#39;">vonage</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '15, 22:19</strong></p><img src="https://secure.gravatar.com/avatar/49d48663aaba92616a3832ff21da6302?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jamesbl&#39;s gravatar image" /><p><span>jamesbl</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jamesbl has no accepted answers">0%</span></p></div></div><div id="comments-container-47363" class="comments-container"></div><div id="comment-tools-47363" class="comment-tools"></div><div class="clear"></div><div id="comment-47363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47364"></span>

<div id="answer-container-47364" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47364-score" class="post-score" title="current number of votes">0</div><span id="post-47364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you are 100% sure you took the proper .pcap file, I'd suspect an issue with VoIP call detection in your version of Wireshark (which is...?).</p><p>So try to use lower level tools to tell Wireshark which packets belong to the call: go to Statistics -&gt; Conversations. A new window will open, select the "UDP: X" tab in that window (X is the number of UDP conversations detected), and click at the column header "packets A-&gt;B". This sorts the conversations starting from the shortest one, so click again to have the longest ones on top of the list.</p><p>Now select one of them (start from the longest one) and press the "Follow stream" button.</p><p>Another window will open, but what really interests us is that a display filter will be set for that UDP stream. So now return to the packet list. If the packets are not decoded as RTP (probably not but I don't know what the real trouble is), right-click any of them, and select "decode as" from the context menu. Find "RTP" in the rightmost list in the "decode as" window, select it and press "apply".</p><p>Now select any of the RTP packets in the list, go to Telephony -&gt; RTP -&gt; Stream analysis, you should get a new window with "Forward Direction" and "Reverse direction" tabs, and should be able to use "Player" and "Save payload" buttons.</p><p>Good luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '15, 00:37</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Nov '15, 01:09</strong> </span></p></div></div><div id="comments-container-47364" class="comments-container"></div><div id="comment-tools-47364" class="comment-tools"></div><div class="clear"></div><div id="comment-47364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

