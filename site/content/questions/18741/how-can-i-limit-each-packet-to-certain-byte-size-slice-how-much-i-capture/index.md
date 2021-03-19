+++
type = "question"
title = "How can I limit each packet to certain byte size (slice how much I capture)?"
description = '''I&#x27;ve tried selecting the &quot;Limit each packet to&quot; field checkbox so I can slice off the amount of data captured so my capture files will be smaller. I don&#x27;t need all the payload, but all the headers really. I&#x27;m using wireshark version 1.6.8. I can check the box and start capturing, but the packets are...'''
date = "2013-02-19T09:40:00Z"
lastmod = "2013-02-19T12:28:00Z"
weight = 18741
keywords = [ "capture-setup" ]
aliases = [ "/questions/18741" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I limit each packet to certain byte size (slice how much I capture)?](/questions/18741/how-can-i-limit-each-packet-to-certain-byte-size-slice-how-much-i-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18741-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I've tried selecting the "Limit each packet to" field checkbox so I can slice off the amount of data captured so my capture files will be smaller. I don't need all the payload, but all the headers really. I'm using wireshark version 1.6.8. I can check the box and start capturing, but the packets are still full size.</p></div><div id="question-tags" class="tags-container tags">capture-setup</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '13, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/4a453f3dd28d87db5bbd6bb6fd79be79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dja0301&#39;s gravatar image" /><p>dja0301<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dja0301 has no accepted answers">0%</span></p></div></div><div id="comments-container-18741" class="comments-container"></div><div id="comment-tools-18741" class="comment-tools"></div><div class="clear"></div><div id="comment-18741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18747"></span>

<div id="answer-container-18747" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18747-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure the packets are full size? The Packet Length column will show the full frame size, even if the full frame wasn't captured.</p><p>I just did a test capture using Wireshark 1.8.5 with "Limit each packet to" set to 100 bytes. I'm looking at a frame that's listed as 1066 bytes in the Packet Length column. However, in the Frame section of the Packet Details pane, I see "1066 bytes on wire (8528 bits), 100 bytes captured (800 bits) on interface 0." I also see "[Packet size limited during capture]" in the Info column of the Packet List pane.</p><p>Check the Frame section and see if the packet really is full size. If it is, I suggest upgrading to the latest stable version of Wireshark (1.8.5).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '13, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-18747" class="comments-container"><span id="18749"></span><div id="comment-18749" class="comment"><div id="post-18749-score" class="comment-score"></div><div class="comment-text"><p>2 minutes faster, almost the same text :)</p></div><div id="comment-18749-info" class="comment-info"><span class="comment-age">(19 Feb '13, 12:29)</span> Jasper ♦♦</div></div><span id="18754"></span><div id="comment-18754" class="comment"><div id="post-18754-score" class="comment-score"></div><div class="comment-text"><p>Nice answer!</p></div><div id="comment-18754-info" class="comment-info"><span class="comment-age">(19 Feb '13, 14:08)</span> Jim Aragon</div></div><span id="18808"></span><div id="comment-18808" class="comment"><div id="post-18808-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answers. You spot on... I was looking at the length column and didn't see that actual captured amount is restricted to what I provisioned. Thanks guys! I appreciate the answers.</p></div><div id="comment-18808-info" class="comment-info"><span class="comment-age">(21 Feb '13, 15:55)</span> dja0301</div></div></div><div id="comment-tools-18747" class="comment-tools"></div><div class="clear"></div><div id="comment-18747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18748"></span>

<div id="answer-container-18748" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18748-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure? Keep in mind that Wireshark will of course still show the actual packet size in the length column, but if you take a look at the first decoded layer you'll see that it says something like "1514 bytes on wire, 64 bytes captured" (for a packet that had originally 1514 bytes (plus FCS) and was limited to 64 bytes at capture).</p><p>Wireshark will still show and use the size of the full packet for all statistics and displays, but the payload isn't there if it was cut short.</p><p>Also, you should notice that your capture files are quite small when you do sliced captures.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '13, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-18748" class="comments-container"></div><div id="comment-tools-18748" class="comment-tools"></div><div class="clear"></div><div id="comment-18748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

