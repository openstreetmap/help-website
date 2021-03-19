+++
type = "question"
title = "MATE snmp session"
description = '''I need to examine snmp session that are longer that 30 seconds I`m using this mate.config Pdu snmp_pdu Proto snmp Transport udp/ip {  Extract addr From ip.addr;  Extract port From udp.port;  Extract oid From snmp.name;  Extract snmp_data From snmp.data; }; Gop snmp_ses On snmp_pdu Match (addr, addr,...'''
date = "2014-03-04T06:38:00Z"
lastmod = "2014-03-12T17:45:00Z"
weight = 30394
keywords = [ "mate", "snmpwireshark", "wireshark" ]
aliases = [ "/questions/30394" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MATE snmp session](/questions/30394/mate-snmp-session)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30394-score" class="post-score" title="current number of votes">0</div><span id="post-30394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to examine snmp session that are longer that 30 seconds</p><p>I`m using this mate.config</p><pre><code>Pdu snmp_pdu Proto snmp Transport udp/ip {
    Extract addr From ip.addr;
    Extract port From udp.port;
    Extract oid From snmp.name;
    Extract snmp_data From snmp.data;
};
Gop snmp_ses On snmp_pdu Match (addr, addr, port, port){
    Start();
    Stop(never);
};
Done;</code></pre><p>So in one Gop i have all packets with same addr and ports. But after awhile (2-3 minutes) i have another snmp packets with sames ports, so them got to one Gop and i can`t use mate.snmp_ses.Duration&gt;30 filter. What conditions i need to group snmp sessions?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mate" rel="tag" title="see questions tagged &#39;mate&#39;">mate</span> <span class="post-tag tag-link-snmpwireshark" rel="tag" title="see questions tagged &#39;snmpwireshark&#39;">snmpwireshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '14, 06:38</strong></p><img src="https://secure.gravatar.com/avatar/c49782b85371ef3b20e7cb67161e9c96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fullmetal8ender&#39;s gravatar image" /><p><span>Fullmetal8ender</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fullmetal8ender has no accepted answers">0%</span></p></div></div><div id="comments-container-30394" class="comments-container"></div><div id="comment-tools-30394" class="comment-tools"></div><div class="clear"></div><div id="comment-30394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30746"></span>

<div id="answer-container-30746" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30746-score" class="post-score" title="current number of votes">0</div><span id="post-30746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So you're saying the first group of packets had an end and a new group started (or at least you want them in different GoPs)?</p><p>In that case you'll need some kind of Stop() condition other than "never". I don't know enough about SNMP to know what, if anything, you could use to do that.</p><p>(BTW I don't think you need to say "addr, addr" and "port, port" in the GoP match; just "addr, port" would be sufficient.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '14, 17:45</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-30746" class="comments-container"></div><div id="comment-tools-30746" class="comment-tools"></div><div class="clear"></div><div id="comment-30746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

