+++
type = "question"
title = "cannot see GSM protocol etc on windows 10 with various wireshark builds"
description = '''Frame 1: 69 bytes on wire (552 bits), 69 bytes captured (552 bits)  Encapsulation type: USER 15 (60)  Arrival Time: Oct 3, 2017 07:50:05.620600000 SA Pacific Standard Time  [Time shift for this packet: 0.000000000 seconds]  Epoch Time: 1507035005.620600000 seconds  [Time delta from previous captured...'''
date = "2017-10-06T12:18:00Z"
lastmod = "2017-10-10T00:28:00Z"
weight = 63714
keywords = [ "see", "cannot", "protocol" ]
aliases = [ "/questions/63714" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [cannot see GSM protocol etc on windows 10 with various wireshark builds](/questions/63714/cannot-see-gsm-protocol-etc-on-windows-10-with-various-wireshark-builds)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63714-score" class="post-score" title="current number of votes">0</div><span id="post-63714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>Frame 1: 69 bytes on wire (552 bits), 69 bytes captured (552 bits)
    Encapsulation type: USER 15 (60)
    Arrival Time: Oct  3, 2017 07:50:05.620600000 SA Pacific Standard Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1507035005.620600000 seconds
    [Time delta from previous captured frame: 0.000000000 seconds]
    [Time delta from previous displayed frame: 0.000000000 seconds]
    [Time since reference or first frame: 0.000000000 seconds]
    Frame Number: 1
    Frame Length: 69 bytes (552 bits)
    Capture Length: 69 bytes (552 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: user_dlt:data]
DLT: 162
Data (69 bytes)
    Data: 000100046d7470330002003985ec2c0ac80c05011020010a...
    [Length: 69]</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-see" rel="tag" title="see questions tagged &#39;see&#39;">see</span> <span class="post-tag tag-link-cannot" rel="tag" title="see questions tagged &#39;cannot&#39;">cannot</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '17, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/e09f53497c838fce1e6074d249103e9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pagan_barr&#39;s gravatar image" /><p><span>pagan_barr</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pagan_barr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Oct '17, 18:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-63714" class="comments-container"><span id="63717"></span><div id="comment-63717" class="comment"><div id="post-63717-score" class="comment-score"></div><div class="comment-text"><p>You need to know and configure what protocol should be decoded as user dlt 15. In the user dlt preferences.</p></div><div id="comment-63717-info" class="comment-info"><span class="comment-age">(06 Oct '17, 12:36)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="63720"></span><div id="comment-63720" class="comment"><div id="post-63720-score" class="comment-score"></div><div class="comment-text"><p>DLT USER 15</p></div><div id="comment-63720-info" class="comment-info"><span class="comment-age">(06 Oct '17, 14:24)</span> <span class="comment-user userinfo">pagan_barr</span></div></div><span id="63781"></span><div id="comment-63781" class="comment"><div id="post-63781-score" class="comment-score"></div><div class="comment-text"><p>Did you capture this on the Windows 10 machine?</p><p>If so, how did you capture it?</p><p>If not, on what machine was it captured, and with what software was it captured? There's no standard for encapsulating GSM packets, so Wireshark might, or might not, be able to be told to decode the traffic as GSM packets, depending on how the packets are encapsulated.</p></div><div id="comment-63781-info" class="comment-info"><span class="comment-age">(10 Oct '17, 00:28)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-63714" class="comment-tools"></div><div class="clear"></div><div id="comment-63714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63724"></span>

<div id="answer-container-63724" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63724-score" class="post-score" title="current number of votes">0</div><span id="post-63724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pagan_barr has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>DLT 162 is USER_15, that is what the file says. That is one step, now Wireshark knows what it is, a user defined encapsulation. What it doesn't know is how to dissect that, because it doesn't know about this user-defined encapsulation, unless you tell it.</p><p>That is where the DLT_USER protocol preference comes in. If you look that up in the Wireshark preferences you'll see that you can edit the Encapsulation table. This table lets you define how to dissect user encapsulations.</p><p>It starts off with the DLT you use, then the protocol the data should be dissected as.</p><p>If your protocol data is wrapped inside a header and/or trailer these can be dissected as well, but these are a bit more exotic situations.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '17, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-63724" class="comments-container"><span id="63766"></span><div id="comment-63766" class="comment"><div id="post-63766-score" class="comment-score"></div><div class="comment-text"><p>Thank you. It appears to happen on windows 10.</p></div><div id="comment-63766-info" class="comment-info"><span class="comment-age">(09 Oct '17, 08:43)</span> <span class="comment-user userinfo">pagan_barr</span></div></div><span id="63767"></span><div id="comment-63767" class="comment"><div id="post-63767-score" class="comment-score"></div><div class="comment-text"><p>It's not really clear (at least to me) from your reaction whether you can see the dissected GSM protocol or not after following <a href="https://ask.wireshark.org/users/4/jaap">@Jaap</a>'s advice. If not, does your repeated mentioning of Windows 10 mean that you've tried on other OSes as well (other Windows than 10, Linux, Mac OS) and the same pcap file was dissected fine there?</p></div><div id="comment-63767-info" class="comment-info"><span class="comment-age">(09 Oct '17, 10:27)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-63724" class="comment-tools"></div><div class="clear"></div><div id="comment-63724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

