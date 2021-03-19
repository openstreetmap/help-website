+++
type = "question"
title = "Export packets in &quot;Decode as&quot; format"
description = '''I&#x27;m trying to export a packet capture, which is decoded as &quot;PEEKREMOTE&quot;. For example: tshark -r -d udp.port==5000,peekremote &amp;lt;file.pcap&amp;gt; ...and I&#x27;d like to save/export the &#x27;decoded version&#x27; of file.pcap. Is that possible in either tshark or wireshark?'''
date = "2013-11-25T21:05:00Z"
lastmod = "2013-11-26T03:58:00Z"
weight = 27371
keywords = [ "decode", "as" ]
aliases = [ "/questions/27371" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Export packets in "Decode as" format](/questions/27371/export-packets-in-decode-as-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27371-score" class="post-score" title="current number of votes">0</div><span id="post-27371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to export a packet capture, which is decoded as "PEEKREMOTE". For example: tshark -r -d udp.port==5000,peekremote &lt;file.pcap&gt; ...and I'd like to save/export the 'decoded version' of file.pcap. Is that possible in either tshark or wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-as" rel="tag" title="see questions tagged &#39;as&#39;">as</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '13, 21:05</strong></p><img src="https://secure.gravatar.com/avatar/cee21d07959f54316e2e540897a9a523?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mike909&#39;s gravatar image" /><p><span>mike909</span><br />
<span class="score" title="15 reputation points">15</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mike909 has no accepted answers">0%</span></p></div></div><div id="comments-container-27371" class="comments-container"></div><div id="comment-tools-27371" class="comment-tools"></div><div class="clear"></div><div id="comment-27371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27408"></span>

<div id="answer-container-27408" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27408-score" class="post-score" title="current number of votes">1</div><span id="post-27408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mike909 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is that possible in either tshark or wireshark?</p></blockquote><p>No, that's not possible, as the "Decode as" action is only performed within Wireshark/tshark while it is running. If you save a decoded capture file, there will be <strong>no information</strong> added about your special configuration (decoding port 5000 as PEEKREMOTE).</p><p>Solution: If you want to have that as a permanent option, you can change the Wireshark preferences.</p><ul><li>Select one of those packets with port 5000</li><li>then &gt;Analyze -&gt; Decode As -&gt; Transport [tab] -&gt; PEEKREMOTE (will only show up for UDP frames)</li><li>click <strong>Apply</strong></li><li>click <strong>Show current</strong></li><li>click <strong>Save</strong></li></ul><p>Wireshark will now save your 'Decode As' setting to the file 'decode_as_entries' in the folder %APPDATA%\Wireshark\, or a sub-folder if you are using profiles. Just search for the file name.</p><p>Content of <code>decode_as_entries</code></p><pre><code># &quot;Decode As&quot; entries file for Wireshark 1.11.0-SVN-52212.
#
# This file is regenerated when saving the &quot;Decode As...&quot; list.
# So be careful, if you want to make manual changes here.
######## Decode As table entries, can be altered through command line ########
decode_as_entry: udp.port,5000,(none),PEEKREMOTE</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Nov '13, 04:08</strong> </span></p></div></div><div id="comments-container-27408" class="comments-container"></div><div id="comment-tools-27408" class="comment-tools"></div><div class="clear"></div><div id="comment-27408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27382"></span>

<div id="answer-container-27382" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27382-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27382-score" class="post-score" title="current number of votes">0</div><span id="post-27382-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What do you mean by "export" and "decoded"? [Wire|t]shark can print the protocol tree as text or various forms of ML. Look under the File | Export Packet Dissections ... menu in Wireshark, and look at the -T options for tshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '13, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-27382" class="comments-container"></div><div id="comment-tools-27382" class="comment-tools"></div><div class="clear"></div><div id="comment-27382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

