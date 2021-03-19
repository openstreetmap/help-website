+++
type = "question"
title = "cisco erspan id as a filter method?"
description = '''Hi, I have a single cisco 6500 running two erspan sessions with different erspan id&#x27;s. I have a server running wireshark as the destination of the erspans. I would like to split the capture into two separate captures based on the erspan id. Is this possible? I cannot seem to find a way to display an...'''
date = "2012-03-11T19:11:00Z"
lastmod = "2012-03-11T20:36:00Z"
weight = 9478
keywords = [ "erspan" ]
aliases = [ "/questions/9478" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [cisco erspan id as a filter method?](/questions/9478/cisco-erspan-id-as-a-filter-method)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9478-score" class="post-score" title="current number of votes">0</div><span id="post-9478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a single cisco 6500 running two erspan sessions with different erspan id's. I have a server running wireshark as the destination of the erspans. I would like to split the capture into two separate captures based on the erspan id. Is this possible? I cannot seem to find a way to display an erspan id in the gui.</p><p>thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-erspan" rel="tag" title="see questions tagged &#39;erspan&#39;">erspan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '12, 19:11</strong></p><img src="https://secure.gravatar.com/avatar/6c04ff5565db8af4787b6ab1e28b01d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jonno&#39;s gravatar image" /><p><span>jonno</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jonno has no accepted answers">0%</span></p></div></div><div id="comments-container-9478" class="comments-container"></div><div id="comment-tools-9478" class="comment-tools"></div><div class="clear"></div><div id="comment-9478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9480"></span>

<div id="answer-container-9480" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9480-score" class="post-score" title="current number of votes">1</div><span id="post-9480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jonno has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For the Cisco Erspan dissector, I do see a field labeled "SpanID" with filter name "erspan.spanid".</p><p>I would expect that you'd see this field in the GUI.</p><p>(You can use tshark with a Read Filter (-R) to filter for packets with a particular spanid or you can use Wireshark to filter as needed and then do "save as: displayed").</p><p>Tshark output from a capture file with ERSPAN:</p><pre><code>Generic Routing Encapsulation (ERSPAN)
   Flags and Version: 0x1000
        0... .... .... .... = Checksum Bit: No
        .0.. .... .... .... = Routing Bit: No
        ..0. .... .... .... = Key Bit: No
        ...1 .... .... .... = Sequence Number Bit: Yes
        .... 0... .... .... = Strict Source Route Bit: No
        .... .000 .... .... = Recursion control: 0
        .... .... 0000 0... = Flags (Reserved): 0
        .... .... .... .000 = Version: GRE (0)
    Protocol Type: ERSPAN (0x88be)
    Sequence Number: 1086760
Encapsulated Remote Switch Packet ANalysis
    0001 .... .... .... = Version: Type II (1)
    .... 0000 0110 0101 = Vlan: 101
    110. .... .... .... = Priority: 6
    ...0 .... .... .... = Unknown2: 0
    .... 0... .... .... = Direction: Incoming (0)
    .... .0.. .... .... = Truncated: Not truncated (0)
    .... ..00 0000 0001 = SpanID: 1
    Unknown7: 00084065</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '12, 19:38</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Mar '12, 19:41</strong> </span></p></div></div><div id="comments-container-9480" class="comments-container"><span id="9481"></span><div id="comment-9481" class="comment"><div id="post-9481-score" class="comment-score"></div><div class="comment-text"><p>thanks, looking at it, I can use the "erspand.id == " in the gui filter. I had a problem where I was using erspan packets with the first 50 bytes chopped, so I couldn't see it :)</p></div><div id="comment-9481-info" class="comment-info"><span class="comment-age">(11 Mar '12, 20:36)</span> <span class="comment-user userinfo">jonno</span></div></div></div><div id="comment-tools-9480" class="comment-tools"></div><div class="clear"></div><div id="comment-9480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

