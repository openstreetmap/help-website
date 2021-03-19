+++
type = "question"
title = "Protocol Hierarchy Meaning"
description = '''Hi,  I want to know what the &quot;DATA&quot; protocol under &quot;Statistics&amp;gt; Protocol Hierarchy&amp;gt; Frame&amp;gt; Ethernet&amp;gt; IPv4&amp;gt; TCP &amp;gt; DATA&quot; means. I&#x27;m analizing several captures but I don´t have any idea what this DATA means. Best regards and thank for the help. '''
date = "2012-01-12T12:15:00Z"
lastmod = "2012-01-12T14:08:00Z"
weight = 8357
keywords = [ "protocol", "statistics", "data", "ipv4", "tcp" ]
aliases = [ "/questions/8357" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Protocol Hierarchy Meaning](/questions/8357/protocol-hierarchy-meaning)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8357-score" class="post-score" title="current number of votes">0</div><span id="post-8357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to know what the "DATA" protocol under "Statistics&gt; Protocol Hierarchy&gt; Frame&gt; Ethernet&gt; IPv4&gt; TCP &gt; <strong>DATA</strong>" means.</p><p>I'm analizing several captures but I don´t have any idea what this DATA means.</p><p>Best regards and thank for the help.</p><p><img src="http://i41.tinypic.com/jt08lt.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-ipv4" rel="tag" title="see questions tagged &#39;ipv4&#39;">ipv4</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '12, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/9c69f864079a3a7f1d3133e23e5901c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavOz&#39;s gravatar image" /><p><span>DavOz</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavOz has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jan '12, 12:40</strong> </span></p></div></div><div id="comments-container-8357" class="comments-container"></div><div id="comment-tools-8357" class="comment-tools"></div><div class="clear"></div><div id="comment-8357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8358"></span>

<div id="answer-container-8358" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8358-score" class="post-score" title="current number of votes">1</div><span id="post-8358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"data" just means that some dissector (say TCP) didn't know how to dissect a payload (e.g. couldn't dispatch to a dissector for the payload) and so chose to just display the payload bytes as "data".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '12, 12:46</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-8358" class="comments-container"><span id="8359"></span><div id="comment-8359" class="comment"><div id="post-8359-score" class="comment-score"></div><div class="comment-text"><p>Thanks,</p><p>Just to be really clear, this means that Wireshark couldnt detect which TCP protocol is this Payload and just display ai as Data? Is there any statistic or way to find who is generating this DATA?</p><p>(Note: I've converted your answer to a comment per the way this site works. Please see the FAQ).</p></div><div id="comment-8359-info" class="comment-info"><span class="comment-age">(12 Jan '12, 12:59)</span> <span class="comment-user userinfo">DavOz</span></div></div><span id="8360"></span><div id="comment-8360" class="comment"><div id="post-8360-score" class="comment-score"></div><div class="comment-text"><p>You certainly can use 'data' as a display filter to find frames showing 'data'.</p><p>You would need to look in detail at the relevant frames, determine the source machine, determine what on that machine is sending the frames, etc, etc). (I'm leaving out the details).</p><p>Note that it may be perfectly normal to see Wireshark decode something as 'data'.</p><p>For example, if I write a client/server application which sends data over TCP with my own format (i.e., using my own protocol) then obviously Wireshark wouldn't be able to decode the data (unless I wrote a dissector for that protocol).</p></div><div id="comment-8360-info" class="comment-info"><span class="comment-age">(12 Jan '12, 13:12)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="8361"></span><div id="comment-8361" class="comment"><div id="post-8361-score" class="comment-score"></div><div class="comment-text"><p>Also: there are certainly many protocols which Wireshark doesn't know how to dissect. New &amp; updated protocol dissectors are being added all the time.</p></div><div id="comment-8361-info" class="comment-info"><span class="comment-age">(12 Jan '12, 13:15)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="8362"></span><div id="comment-8362" class="comment"><div id="post-8362-score" class="comment-score"></div><div class="comment-text"><p>Thank you Bill, I really appreciate your help. Can you tell me how this filter could be used? I'm just an Wireshark amateur.</p></div><div id="comment-8362-info" class="comment-info"><span class="comment-age">(12 Jan '12, 13:26)</span> <span class="comment-user userinfo">DavOz</span></div></div><span id="8363"></span><div id="comment-8363" class="comment"><div id="post-8363-score" class="comment-score"></div><div class="comment-text"><p>You can find instructions in the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChUseFilterToolbarSection.html">Wireshark User's Guide</a>. See <a href="http://www.wireshark.org/docs/wsug_html_chunked/">the section on filters</a>.</p><p>Basically, in this case it boils down to entering <code>data</code> in the filter toolbar text entry field and then clicking <code>apply</code>.</p><p>Wireshark will then show only frames containing a 'data' display.</p></div><div id="comment-8363-info" class="comment-info"><span class="comment-age">(12 Jan '12, 13:44)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="8364"></span><div id="comment-8364" class="comment not_top_scorer"><div id="post-8364-score" class="comment-score"></div><div class="comment-text"><p>Thank you again... Really thank you...</p></div><div id="comment-8364-info" class="comment-info"><span class="comment-age">(12 Jan '12, 14:08)</span> <span class="comment-user userinfo">DavOz</span></div></div></div><div id="comment-tools-8358" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-8358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

