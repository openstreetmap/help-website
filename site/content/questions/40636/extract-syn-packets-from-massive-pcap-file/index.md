+++
type = "question"
title = "Extract syn packets from massive pcap file"
description = '''Hi I&#x27;m trying to baseline SYN rates on our network. I have a 145GB pcap and I&#x27;m trying to use tshark to extract them. tshark -Y tcp[13]==02 -r &quot;reallybigpcap.cap&quot; -w syns.pcap This eventually fails with an failed to allocate memory error.  I think it&#x27;s trying to load the whole file into ram and fail...'''
date = "2015-03-17T07:30:00Z"
lastmod = "2015-03-19T15:42:00Z"
weight = 40636
keywords = [ "extract", "tshark", "scan" ]
aliases = [ "/questions/40636" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Extract syn packets from massive pcap file](/questions/40636/extract-syn-packets-from-massive-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40636-score" class="post-score" title="current number of votes">0</div><span id="post-40636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I'm trying to baseline SYN rates on our network. I have a 145GB pcap and I'm trying to use tshark to extract them.</p><p>tshark -Y tcp[13]==02 -r "reallybigpcap.cap" -w syns.pcap</p><p>This eventually fails with an failed to allocate memory error. I think it's trying to load the whole file into ram and fails.</p><p>Can anyone suggest another tool that can do what I want ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-scan" rel="tag" title="see questions tagged &#39;scan&#39;">scan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '15, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/c90e6211d7de6094aa050ddba621dc99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="20fathoms&#39;s gravatar image" /><p><span>20fathoms</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="20fathoms has no accepted answers">0%</span></p></div></div><div id="comments-container-40636" class="comments-container"><span id="40672"></span><div id="comment-40672" class="comment"><div id="post-40672-score" class="comment-score"></div><div class="comment-text"><p>thanks all!</p></div><div id="comment-40672-info" class="comment-info"><span class="comment-age">(18 Mar '15, 13:05)</span> <span class="comment-user userinfo">20fathoms</span></div></div><span id="40675"></span><div id="comment-40675" class="comment"><div id="post-40675-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-40675-info" class="comment-info"><span class="comment-age">(18 Mar '15, 16:03)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-40636" class="comment-tools"></div><div class="clear"></div><div id="comment-40636-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40642"></span>

<div id="answer-container-40642" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40642-score" class="post-score" title="current number of votes">0</div><span id="post-40642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might first try truncating the file to only the first 66 bytes (IPv4) to limit the amount of additional protocol decoding that tshark needs to do. Use editcap to create a new file.</p><pre><code>editcap -s 66 reallybigcap.cap newsmallercap.cap</code></pre><p>This will only grab the bytes up through the IPv4 header in each packet. Then, re-try your tshark command with the "newsmallercap.cap" file. Tshark will still use up memory, but hopefully less than before.</p><p>If there's a better way, please let me know too!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '15, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/365cfc3c62b61b2ed219b5d146e8ad3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zachad&#39;s gravatar image" /><p><span>zachad</span><br />
<span class="score" title="331 reputation points">331</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zachad has 3 accepted answers">21%</span></p></div></div><div id="comments-container-40642" class="comments-container"></div><div id="comment-tools-40642" class="comment-tools"></div><div class="clear"></div><div id="comment-40642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40643"></span>

<div id="answer-container-40643" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40643-score" class="post-score" title="current number of votes">0</div><span id="post-40643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use tcpdump or windump for this purpose as it does not keep (as much) state (as tshark). If the file is still too big to process, you can use editcap to split it into chunks and then process each chunk and then merge the filtered parts back to one file with mergecap.</p><p>Editcap and mergecap came with wireshark and tcpdump/windump are separate programs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '15, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40643" class="comments-container"><span id="40699"></span><div id="comment-40699" class="comment"><div id="post-40699-score" class="comment-score"></div><div class="comment-text"><p>I wonder if this is a good use case for enhancing <code>dumpcap</code> to be able to read capture files?</p><p>By the way, I'll just mention another possible method for getting information from a big file. It involves the use of <a href="http://linux.die.net/man/1/tail"><code>tail</code></a>, <a href="https://www.wireshark.org/docs/man-pages/rawshark.html"><code>rawshark</code></a> and <a href="http://linux.die.net/man/1/grep"><code>grep</code></a>. Admittedly, it's sort of a hack, and you can't save the resulting packets to a new file, but it <em>might</em> be useful to someone:</p><p><code>    tail -c +25 file.pcap | rawshark -d encap:EN10MB -F field1 -F field2 ... -F fieldn -R "tcp.flags.syn == 1" -r - | grep "1 \-$"</code></p></div><div id="comment-40699-info" class="comment-info"><span class="comment-age">(19 Mar '15, 14:44)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="40701"></span><div id="comment-40701" class="comment"><div id="post-40701-score" class="comment-score"></div><div class="comment-text"><p>I would rather see editcap extended with capture filter capabilities, seems like a more logical place :-)</p></div><div id="comment-40701-info" class="comment-info"><span class="comment-age">(19 Mar '15, 15:42)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-40643" class="comment-tools"></div><div class="clear"></div><div id="comment-40643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

