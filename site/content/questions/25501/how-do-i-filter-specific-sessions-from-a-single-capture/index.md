+++
type = "question"
title = "How do I filter specific sessions from a single capture?"
description = '''I&#x27;m investigating some page timeout issues in a live system. The root problem is a link between Atlassian&#x27;s Confluence and Jira; pages in the former time out when embedding content from the latter. This data exchange is primarily JSON and XML over HTTP; a typical single page load might result in 50-...'''
date = "2013-10-02T04:03:00Z"
lastmod = "2013-10-02T09:41:00Z"
weight = 25501
keywords = [ "filtering", "http" ]
aliases = [ "/questions/25501" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do I filter specific sessions from a single capture?](/questions/25501/how-do-i-filter-specific-sessions-from-a-single-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25501-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm investigating some page timeout issues in a live system. The root problem is a link between Atlassian's Confluence and Jira; pages in the former time out when embedding content from the latter. This data exchange is primarily JSON and XML over HTTP; a typical single page load might result in 50-70 HTTP requests. Both systems are behind an apache proxy.</p><p>At the moment, I don't have the luxury of testing this in isolation and I can't replicate it in the lab setup, so I'm running tshark captures between the proxy to the live JIRA system. So far so good; I can use the TCP stats to get the session times and see some requests taking far too long to process, but I can't be sure which are as a result of the specific page load I triggered.</p><p>There's a unique cookie that should identify a given session's requests. What I'd like is a filter that shows me the <em>entire</em> TCP session traffic where that specific cookie somewhere in the payload. Is that possible within Wireshark?</p></div><div id="question-tags" class="tags-container tags">filtering http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '13, 04:03</strong></p><img src="https://secure.gravatar.com/avatar/0595a1f6d702238164e5b3bd121759bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TerryD&#39;s gravatar image" /><p>TerryD<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TerryD has no accepted answers">0%</span></p></div></div><div id="comments-container-25501" class="comments-container"><span id="25503"></span><div id="comment-25503" class="comment"><div id="post-25503-score" class="comment-score"></div><div class="comment-text"><p>Maybe I don't quite understand the subtlety of your question...but it sounds like you simply want to isolate a specific TCP connection given a segment with a specific string. If that's the case, there are plenty of ways to do that. What I would do personally is search for the packet containing the cookie. Once you find it, expand the TCP header and look at the value of [Stream Index] - this is Wireshark's way of labeling each unique TCP session. Take that value, and use it as a filter. For example of the stream number is 416, you would use this simple display filter:</p><p>tcp.stream == 416</p><p>There are other ways to do this, such right-click on the packet containing the cookie value, and select Conversation Filter -&gt; TCP or simply "Follow TCP Stream". But I find the TCP stream number so useful, I have added a custom column to my preferences so I am always aware of it.</p></div><div id="comment-25503-info" class="comment-info"><span class="comment-age">(02 Oct '13, 05:37)</span> smp</div></div><span id="25519"></span><div id="comment-25519" class="comment"><div id="post-25519-score" class="comment-score"></div><div class="comment-text"><p>Hi smp. That's the start of what I'm looking to do. I can use Statistics-&gt;Conversation List-&gt;TCP to get a list and duration of every TCP session with the capture and I can ,usefully, isolate individual streams. However, what I can't do is isolate all of the streams related to a particular page load.</p><p>Every one of those streams will have an HTTP GET request in there and each of those requests will share a single, unique cookie. If Wirehark had a plain english parser, I'd say "Show me all of the full TCP streams that contain HTTP requests with 'SESSIONID=xyz' in the request header". That's the best way I can phrase it.</p></div><div id="comment-25519-info" class="comment-info"><span class="comment-age">(02 Oct '13, 08:03)</span> TerryD</div></div><span id="25521"></span><div id="comment-25521" class="comment"><div id="post-25521-score" class="comment-score"></div><div class="comment-text"><p>Oh, that clarifies it perfectly, and it's a great question. Unfortunately, I don't know the answer so I'm going to sit back and watch for a more knowledgeable response. Sorry I couldn't help further.</p></div><div id="comment-25521-info" class="comment-info"><span class="comment-age">(02 Oct '13, 08:10)</span> smp</div></div></div><div id="comment-tools-25501" class="comment-tools"></div><div class="clear"></div><div id="comment-25501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25537"></span>

<div id="answer-container-25537" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25537-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you look at the SharkFest'11 session on command line scripting from @SYN-bit <a href="http://sharkfest.wireshark.org/sharkfest.11/presentations/A-2_Blok-Using_Wireshark_Command_Line_Tools_&amp;_Scripting.pdf">here</a>, Example 3 (slide 42) Sake shows you to find all sessions with a specific http cookie.</p><p>I did a PowerShell version of this at SharkFest'12, the session is <a href="http://sharkfest.wireshark.org/sharkfest.12/presentations/MB-8_Powershell-The_New_Command_Shell_for_Windows_in_Combination_with_T-Shark.pdf">here</a>, and you should look around page 30 for the section "All sessions with cookie xxxx".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '13, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-25537" class="comments-container"><span id="25702"></span><div id="comment-25702" class="comment"><div id="post-25702-score" class="comment-score"></div><div class="comment-text"><p>Thanks! Not only does that answer my question perfectly, but it's introduced me to whole new source of wizardry. (Using tshark to generate a filter for tshark. The mind boggles...)</p></div><div id="comment-25702-info" class="comment-info"><span class="comment-age">(07 Oct '13, 01:35)</span> TerryD</div></div></div><div id="comment-tools-25537" class="comment-tools"></div><div class="clear"></div><div id="comment-25537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

