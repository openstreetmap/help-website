+++
type = "question"
title = "Extract TCP Payload from PDML file"
description = '''Hi, I am currently trying to write a program which parses a PDML file and extracts the TCP payload for packets sent from a particular IP, I need this in the form of a Hex dump. The problem I have, is not all packets have a simple &quot;fake-field-wrapper&quot;. And some contain application layer data such as ...'''
date = "2014-08-25T03:55:00Z"
lastmod = "2014-08-26T08:51:00Z"
weight = 35706
keywords = [ "hexdump", "pdml", "smb", "parsing" ]
aliases = [ "/questions/35706" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract TCP Payload from PDML file](/questions/35706/extract-tcp-payload-from-pdml-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35706-score" class="post-score" title="current number of votes">0</div><span id="post-35706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am currently trying to write a program which parses a PDML file and extracts the TCP payload for packets sent from a particular IP, I need this in the form of a Hex dump.</p><p>The problem I have, is not all packets have a simple "fake-field-wrapper". And some contain application layer data such as SMB.</p><p>What would be the best way of dumping the hex for these packets?</p><p>Also, I would only like to output all of the TCP payload from a single TCP stream. How do you know what is a 'single' TCP stream, any type of identifier? Or would I just have to do a for loop and fetch every packet until an ACK/SYN packet?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hexdump" rel="tag" title="see questions tagged &#39;hexdump&#39;">hexdump</span> <span class="post-tag tag-link-pdml" rel="tag" title="see questions tagged &#39;pdml&#39;">pdml</span> <span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '14, 03:55</strong></p><img src="https://secure.gravatar.com/avatar/5f3cd9d744398542caac634e2f608a61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WireTshark&#39;s gravatar image" /><p><span>WireTshark</span><br />
<span class="score" title="5 reputation points">5</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WireTshark has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Aug '14, 04:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-35706" class="comments-container"><span id="35708"></span><div id="comment-35708" class="comment"><div id="post-35708-score" class="comment-score"></div><div class="comment-text"><p>Is it a requirement that this be done through PDML, or is working with the raw .pcap file a possibility?</p></div><div id="comment-35708-info" class="comment-info"><span class="comment-age">(25 Aug '14, 06:58)</span> <span class="comment-user userinfo">Quadratic</span></div></div><span id="35709"></span><div id="comment-35709" class="comment"><div id="post-35709-score" class="comment-score"></div><div class="comment-text"><p>I would like to see if it could be done with PDML output. If the possibility of this is limited, I could consider looking at raw.pcap files</p></div><div id="comment-35709-info" class="comment-info"><span class="comment-age">(25 Aug '14, 07:14)</span> <span class="comment-user userinfo">WireTshark</span></div></div></div><div id="comment-tools-35706" class="comment-tools"></div><div class="clear"></div><div id="comment-35706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35758"></span>

<div id="answer-container-35758" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35758-score" class="post-score" title="current number of votes">1</div><span id="post-35758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So I assume my answer to <a href="https://ask.wireshark.org/questions/35749/dumping-tcp-payload-of-a-specific-tcp-stream">this</a> question helps you with most of what you're asking for here, leaving only the last part of your question regarding how to output all of the TCP payload from a single TCP stream.</p><p>I would say that probably the easiest ways to achieve this are to use one of the following methods:</p><ul><li>Apply a display filter for the tcp stream number you're interested in, e.g., <code>tcp.stream == 1</code>, and then only export those displayed packets. The <code>tcp.stream</code> field is a Wireshark-generated field, which you can find by expanding the TCP protocol in the packet details pane.</li><li>In the packet details pane, right-click on a packet of interest and choose, <em>"Conversation Filter -&gt; TCP"</em>. This effectively accomplishes the same thing as the first method.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '14, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-35758" class="comments-container"></div><div id="comment-tools-35758" class="comment-tools"></div><div class="clear"></div><div id="comment-35758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

