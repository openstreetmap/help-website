+++
type = "question"
title = "Decoding SNMP Trap HEX to OIDS?  Only getting garbled text"
description = '''Hello, I&#x27;ve done a bit of searching, but I cannot seem to find an appropriate answer. I&#x27;ve seen wireshark displays before where you can capture on port 162 and see all the trap oids and varbinds. I&#x27;m in the process right now of writing trap definitions for an NMS suite, and need to see the trap cont...'''
date = "2015-08-21T10:44:00Z"
lastmod = "2015-08-21T13:38:00Z"
weight = 45297
keywords = [ "snmptrap", "smmp" ]
aliases = [ "/questions/45297" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding SNMP Trap HEX to OIDS? Only getting garbled text](/questions/45297/decoding-snmp-trap-hex-to-oids-only-getting-garbled-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45297-score" class="post-score" title="current number of votes">0</div><span id="post-45297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I've done a bit of searching, but I cannot seem to find an appropriate answer. I've seen wireshark displays before where you can capture on port 162 and see all the trap oids and varbinds. I'm in the process right now of writing trap definitions for an NMS suite, and need to see the trap contents, rather than hex or un-normalized trap garble.</p><p>Currently, I sent a test trap from a test box of mine, and in the "data" section of the packet capture, it displays hex on one side and some of the trap information spaced between "...." and other garbled text. How do I get wireshark to display this as a list of OID's? This is the view I have of a trap, which is basically very unhelpful <img src="https://scontent-dfw1-1.xx.fbcdn.net/hphotos-xfp1/v/t1.0-9/11892038_956021754457342_715962632653815477_n.jpg?oh=a3fcbc01f2716736c227894fd8d9c1a3&amp;oe=5643D30B" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-snmptrap" rel="tag" title="see questions tagged &#39;snmptrap&#39;">snmptrap</span> <span class="post-tag tag-link-smmp" rel="tag" title="see questions tagged &#39;smmp&#39;">smmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '15, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/ecda95444a97effadc104911a8a3b490?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="James%20Newman&#39;s gravatar image" /><p><span>James Newman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="James Newman has no accepted answers">0%</span></p></img></div></div><div id="comments-container-45297" class="comments-container"><span id="45300"></span><div id="comment-45300" class="comment"><div id="post-45300-score" class="comment-score"></div><div class="comment-text"><p>Also, I notice that the SNMP layer of the packet is not even displayed. It's being seen as protocol 0x0800 instead of SNMP. Any idea what's going on? I'm very confused =(</p><p>I am on 1.12.7 release btw</p></div><div id="comment-45300-info" class="comment-info"><span class="comment-age">(21 Aug '15, 11:12)</span> <span class="comment-user userinfo">James Newman</span></div></div></div><div id="comment-tools-45297" class="comment-tools"></div><div class="clear"></div><div id="comment-45297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45302"></span>

<div id="answer-container-45302" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45302-score" class="post-score" title="current number of votes">0</div><span id="post-45302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>0x0800 means the frame contains an IPv4 packet. Try an SNMP sample capture from <a href="https://wiki.wireshark.org/SampleCaptures#SNMP">here</a> and check if it's being displayed correctly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '15, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-45302" class="comments-container"><span id="45303"></span><div id="comment-45303" class="comment"><div id="post-45303-score" class="comment-score"></div><div class="comment-text"><p>I tried the b6300a.cap file and it displays Protocol SNMP correctly and I can see varbinds. Any idea why my capture is not being registered as SNMP?</p></div><div id="comment-45303-info" class="comment-info"><span class="comment-age">(21 Aug '15, 11:53)</span> <span class="comment-user userinfo">James Newman</span></div></div><span id="45304"></span><div id="comment-45304" class="comment"><div id="post-45304-score" class="comment-score"></div><div class="comment-text"><p>How did you capture the traffic? Can you please post a link to the packet capture.</p></div><div id="comment-45304-info" class="comment-info"><span class="comment-age">(21 Aug '15, 13:38)</span> <span class="comment-user userinfo">Roland</span></div></div></div><div id="comment-tools-45302" class="comment-tools"></div><div class="clear"></div><div id="comment-45302-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

