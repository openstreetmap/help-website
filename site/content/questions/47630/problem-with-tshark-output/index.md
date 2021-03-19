+++
type = "question"
title = "Problem with tshark output"
description = '''Hello! I run tshark with -T fields and -e to convert pcaps to CSVs for future processing. One problem I run into is that tshark bundles all the fields with the same name together. For example, -e tcp.srcport will result in one value; -e ip.addr will result in two values, and other fields may potenti...'''
date = "2015-11-16T06:55:00Z"
lastmod = "2015-11-16T07:59:00Z"
weight = 47630
keywords = [ "tshark" ]
aliases = [ "/questions/47630" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Problem with tshark output](/questions/47630/problem-with-tshark-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47630-score" class="post-score" title="current number of votes">0</div><span id="post-47630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I run tshark with -T fields and -e to convert pcaps to CSVs for future processing. One problem I run into is that tshark bundles all the fields with the same name together. For example, -e tcp.srcport will result in one value; -e ip.addr will result in two values, and other fields may potentially result in many values taken from different locations in the packet - all written consecutively. Parsing the result may be problematic or sometimes nearly impossible; for example, if you have more than one ethernet/ip load on top of TCP.</p><p>Is it possible to do anything, e.g. add some flags to tshark, to help unravel the output?</p><p>Thanks!</p><p>Update: Just to clarify: the question referred to complex application-level protocols that have multiple occurrences of the same field - and may themselves appear several times in a single packet. IP addresses was just an initial example - of course, there are always two. And PDML is the best we can do, so the question is resolved.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '15, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/75140f629174b4cf63999463e47be93a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dfrumkin&#39;s gravatar image" /><p><span>dfrumkin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dfrumkin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Nov '15, 08:27</strong> </span></p></div></div><div id="comments-container-47630" class="comments-container"></div><div id="comment-tools-47630" class="comment-tools"></div><div class="clear"></div><div id="comment-47630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="47632"></span>

<div id="answer-container-47632" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47632-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47632-score" class="post-score" title="current number of votes">1</div><span id="post-47632-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dfrumkin has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible to do anything, e.g. add some flags to tshark, to help unravel the output?</p></blockquote><p>Yes. Don't use <strong>ip.addr</strong>, because that will be the <strong>src and dst</strong> IP address and tshark will print them together, according to the settings in <strong>-E aggregator=</strong>.</p><p>Instead, you could use: <strong>ip.src</strong> and <strong>ip.dst</strong></p><blockquote><p>tshark -ni input.pcap -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e xxx</p></blockquote><p>If you want to use <strong>ip.addr</strong>, you should define the <strong>separator</strong> and the <strong>aggregator</strong> character/string to ease the parsing process.</p><blockquote><p>tshark -ni input.pcap -T fields -e ip.addr tcp.port -E separator=, -E aggregator=: -E header=y</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '15, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Nov '15, 07:20</strong> </span></p></div></div><div id="comments-container-47632" class="comments-container"><span id="47634"></span><div id="comment-47634" class="comment"><div id="post-47634-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the aggregator; it saves some hacks. However, the major problem s that the fields of the same type are bundled together. In the example I gave in the original question, where you have multiple ethernet/ip loads on top of TCP, how would I know what belongs to each one?</p></div><div id="comment-47634-info" class="comment-info"><span class="comment-age">(16 Nov '15, 07:22)</span> <span class="comment-user userinfo">dfrumkin</span></div></div><span id="47635"></span><div id="comment-47635" class="comment"><div id="post-47635-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>how would I know what belongs to each one?</p></blockquote><p>You won't, as there is no marker for the layer at which the IP address appears. Usually, they will be printed serially, one after the other.</p><p>If you need more insight, please run one of the following commands and parse the full output.</p><blockquote><p>tshark -nr input.pcap -V<br />
thsark -nr input.pcap -T pdml</p></blockquote><p>That way you will get everything in the order as it appears in the frames.</p><p>But maybe I'm misunderstanding your request. If so, please upload a small sample pcap somwhere (dropbox, etc.) and post the link here, together with the desired output.</p></div><div id="comment-47635-info" class="comment-info"><span class="comment-age">(16 Nov '15, 07:28)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="47637"></span><div id="comment-47637" class="comment"><div id="post-47637-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot, Kurt! Looks like pdml (pyshark?) is the way to go. You understood my question correctly; I was just looking for a simple solution where there is none.</p></div><div id="comment-47637-info" class="comment-info"><span class="comment-age">(16 Nov '15, 07:47)</span> <span class="comment-user userinfo">dfrumkin</span></div></div><span id="47638"></span><div id="comment-47638" class="comment"><div id="post-47638-score" class="comment-score"></div><div class="comment-text"><p>Yes, maybe pyshark is an option as well....</p></div><div id="comment-47638-info" class="comment-info"><span class="comment-age">(16 Nov '15, 07:59)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-47632" class="comment-tools"></div><div class="clear"></div><div id="comment-47632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47631"></span>

<div id="answer-container-47631" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47631-score" class="post-score" title="current number of votes">0</div><span id="post-47631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's the <code>-E occurrence=f|l|a</code> option to print first, last or all occurrences of each field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '15, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div></div><div id="comments-container-47631" class="comments-container"><span id="47633"></span><div id="comment-47633" class="comment"><div id="post-47633-score" class="comment-score"></div><div class="comment-text"><p>How would it help? Don't I get all the occurrences by default?</p></div><div id="comment-47633-info" class="comment-info"><span class="comment-age">(16 Nov '15, 07:07)</span> <span class="comment-user userinfo">dfrumkin</span></div></div><span id="47636"></span><div id="comment-47636" class="comment"><div id="post-47636-score" class="comment-score"></div><div class="comment-text"><p>Those flags (that's all that are available in this area currently) do allow you to pick the first or last.</p></div><div id="comment-47636-info" class="comment-info"><span class="comment-age">(16 Nov '15, 07:35)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-47631" class="comment-tools"></div><div class="clear"></div><div id="comment-47631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

