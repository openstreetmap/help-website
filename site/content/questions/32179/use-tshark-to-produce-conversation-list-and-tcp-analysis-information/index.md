+++
type = "question"
title = "Use Tshark to Produce Conversation list and TCP Analysis Information"
description = '''I can produce conversation and traffic information with &quot;tshark -r filename.pcap -q -z conv,tcp -n&quot; and I can look for TCP problem indicators with filters like tcp.analysis.retransmission or tcp.analysis.fast_retransmission or tcp.analysis.zero_window. I would like to be able to produce a conversati...'''
date = "2014-04-25T10:06:00Z"
lastmod = "2014-04-26T12:44:00Z"
weight = 32179
keywords = [ "stats", "tshark", "analysis", "conversationlist" ]
aliases = [ "/questions/32179" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Use Tshark to Produce Conversation list and TCP Analysis Information](/questions/32179/use-tshark-to-produce-conversation-list-and-tcp-analysis-information)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32179-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can produce conversation and traffic information with "tshark -r filename.pcap -q -z conv,tcp -n" and I can look for TCP problem indicators with filters like tcp.analysis.retransmission or tcp.analysis.fast_retransmission or tcp.analysis.zero_window. I would like to be able to produce a conversation list with traffic and the number of instances a problem indicator occured but I do not know if this is possible.<br />
</p><p>It would be great to be able to get a text file that can be parsed automatically so I can be alerted to this type of information. In a perfect world, I would also have RTT type information on a per session basis as well.</p></div><div id="question-tags" class="tags-container tags">stats tshark analysis conversationlist</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '14, 10:06</strong></p><img src="https://secure.gravatar.com/avatar/95124144fcecaae3a7771935ce5a4e1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reece&#39;s gravatar image" /><p>Reece<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reece has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-32179" class="comments-container"></div><div id="comment-tools-32179" class="comment-tools"></div><div class="clear"></div><div id="comment-32179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32201"></span>

<div id="answer-container-32201" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32201-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can do this:</p><blockquote><p>tshark -nr input.pcap -Y "tcp.analysis.retransmission or tcp.analysis.fast_retransmission or tcp.analysis.zero_window" -T fields -e tcp.stream</p></blockquote><p>Then use the streams creates with the first command (you'll have to eliminate duplicates for this step) and build a filter for the second command (can be done with a script).</p><blockquote><p>tshark -nr input.pcap -Y "tcp.stream == aaa or tcp.stream == bbb" -q -z conv,tcp</p></blockquote><p>If -Y does not work, try -R instead.</p><p>Now, you have two outputs.</p><p><strong>First:</strong> The amount of errors per stream (stream number)<br />
<strong>Second:</strong> The conversation list for those streams</p><p>You can "merge" the two with a script and create whatever output/result you may need.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '14, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-32201" class="comments-container"><span id="32236"></span><div id="comment-32236" class="comment"><div id="post-32236-score" class="comment-score"></div><div class="comment-text"><p>This is really helpful - thankyou.</p><p>I can't seem to get the filter working with the conv,tcp command though, maybe this is pilot error.</p><p>As I want to collect stats in both well behaved and badly behaved streams it would be ideal if I could either output the conv,tcp command without sorting (so I can match line number to stream error) or to include the stream number in the table output. This doesnt seem to be possible, however, I think I can probably match the two tables with the following:</p><p>tshark -nr input.pcap -R "tcp.analysis.retransmission or tcp.analysis.fast_retransmission or tcp.analysis.zero_window" -e tcp.stream -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e expert.message -T fields</p></div><div id="comment-32236-info" class="comment-info"><span class="comment-age">(28 Apr '14, 02:33)</span> Reece</div></div><span id="32260"></span><div id="comment-32260" class="comment"><div id="post-32260-score" class="comment-score"></div><div class="comment-text"><blockquote><p>maybe this is <strong>pilot error</strong>.</p></blockquote><p>pilot error? Did you try to use that filter in Riverbed/Cascade Pilot? If so, I'm not sure if the filters are compatible with the ones of wireshark/tshark.</p><blockquote><p>I think I can probably match the two tables with the following:</p></blockquote><p>looks O.K.</p></div><div id="comment-32260-info" class="comment-info"><span class="comment-age">(28 Apr '14, 08:23)</span> Kurt Knochner ♦</div></div><span id="32264"></span><div id="comment-32264" class="comment"><div id="post-32264-score" class="comment-score"></div><div class="comment-text"><p>I think Reece was using the term <em>"pilot error"</em> as defined at <a href="http://dictionary.reference.com/browse/pilot+error">http://dictionary.reference.com/browse/pilot+error</a>.</p></div><div id="comment-32264-info" class="comment-info"><span class="comment-age">(28 Apr '14, 08:57)</span> cmaynard ♦♦</div></div><span id="32270"></span><div id="comment-32270" class="comment"><div id="post-32270-score" class="comment-score"></div><div class="comment-text"><p>Ah, I didn't know that one. Thanks for the hint....</p></div><div id="comment-32270-info" class="comment-info"><span class="comment-age">(28 Apr '14, 14:46)</span> Kurt Knochner ♦</div></div><span id="32293"></span><div id="comment-32293" class="comment"><div id="post-32293-score" class="comment-score"></div><div class="comment-text"><p>Sorry for the oblique language and thanks for looking into this. I am happy enough with this to proceed. it would be nice to be able to do this with a single command to reduce load - my files are large - but this will do me.</p></div><div id="comment-32293-info" class="comment-info"><span class="comment-age">(29 Apr '14, 10:20)</span> Reece</div></div></div><div id="comment-tools-32201" class="comment-tools"></div><div class="clear"></div><div id="comment-32201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

