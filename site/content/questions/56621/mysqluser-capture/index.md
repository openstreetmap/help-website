+++
type = "question"
title = "mysql.user capture"
description = '''Hi guys, I&#x27;m testing tshark 1.10.14 on Centos 7.2.1511 and tshark 1.0.15 on Centos 5.11. I&#x27;d like to save for a range of 10 minutes or more mysql.user, ip.src and mysql.query. I arrived to test these commands:  tshark -i any -n -Y &quot;mysql.command==3&quot; -T fields -e ip.src -e mysql.query &quot;dst port 3306 ...'''
date = "2016-10-24T09:38:00Z"
lastmod = "2016-10-24T09:38:00Z"
weight = 56621
keywords = [ "capture-options", "command-line", "mysql" ]
aliases = [ "/questions/56621" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [mysql.user capture](/questions/56621/mysqluser-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56621-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys,</p><p>I'm testing tshark 1.10.14 on Centos 7.2.1511 and tshark 1.0.15 on Centos 5.11. I'd like to save for a range of 10 minutes or more mysql.user, ip.src and mysql.query.</p><p>I arrived to test these commands:</p><ul><li>tshark -i any -n -Y "mysql.command==3" -T fields -e ip.src -e mysql.query "dst port 3306 and (host x.x.x.x or host y.y.y.y)" # tshark 1.10.14</li><li>tshark -i any -n -f "dst port 3306 and tcp[(((tcp[12:1]&amp;0xf0)&gt;&gt;2)+4):1]=0x03 and (host x.x.x.x or host y.y.y.y)" -T fields -e ip.src -e mysql.query # tshark 1.0.15</li></ul><p><strong>ADDITION</strong></p><p>I'm able to capture mysql.user with these comands:</p><ol><li>tshark -i any -n -Y "mysql.user" -T fields -e mysql.user "dst port 3306 and (host x.x.x.x or host y.y.y.y)"</li><li>tshark -i any -n -d tcp.port==3306,mysql -T fields -e mysql.user -e ip.src -e mysql.query "dst port 3306 and (host x.x.x.x or host y.y.y.y)"</li></ol><p>The second configuration capture different records: records with only mysql.user and ip.src and records with ip.src and mysql.query. @Jaap and @sindy confirmed only with an ad hoc script I can create a unique line with all three fields.</p><p>Is improvable the second configuration?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">capture-options command-line mysql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '16, 09:38</strong></p><img src="https://secure.gravatar.com/avatar/0154cb933fdbb0b41331dcf0df6d688d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bilardi&#39;s gravatar image" /><p>bilardi<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bilardi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Oct '16, 01:34</p></div></div><div id="comments-container-56621" class="comments-container"><span id="56636"></span><div id="comment-56636" class="comment"><div id="post-56636-score" class="comment-score">1</div><div class="comment-text"><p>Do you have an (unfiltered) capture taken here, where the user field is filled in? Then you should be able to reverse engineer what you'll need to change.</p></div><div id="comment-56636-info" class="comment-info"><span class="comment-age">(25 Oct '16, 02:55)</span> Jaap ♦</div></div><span id="56642"></span><div id="comment-56642" class="comment"><div id="post-56642-score" class="comment-score"></div><div class="comment-text"><p>@Jaap, I added the paragraph ADDITION. I'd like to be sure that I can only use the second configuration to elaborate the output with an ad hoc script to create records with the format mysql.user\tip.src\tmysql.query, or does it exist a tshark configuration to incorporate the action of this ad hoc script?</p></div><div id="comment-56642-info" class="comment-info"><span class="comment-age">(25 Oct '16, 05:23)</span> bilardi</div></div><span id="56648"></span><div id="comment-56648" class="comment"><div id="post-56648-score" class="comment-score">1</div><div class="comment-text"><p>are you sure that <code>mysql.user</code> and <code>mysql.query</code> exist in the same PDU? The thing is that the dissectors print fields of individual packets or reassembled PDUs, not from established sessions. So if a field is not present in a given packet (or a reassembled PDU), it is not printed for that packet/PDU even if the packet/PDU belongs to a session whose other packets do contain that field.</p><p>If a PDU is split into several packets, field of that PDU are printed for the last packet of the PDU.</p></div><div id="comment-56648-info" class="comment-info"><span class="comment-age">(25 Oct '16, 08:55)</span> sindy</div></div><span id="56649"></span><div id="comment-56649" class="comment"><div id="post-56649-score" class="comment-score"></div><div class="comment-text"><p>Thank you @sindy: you confirmed me that only with an ad hoc script I can create one line mysql.user\tip.src\tmysql.query because the output data gives me two different lines: mysql.user\tip.src and \tip.src\tmysql.query.</p></div><div id="comment-56649-info" class="comment-info"><span class="comment-age">(25 Oct '16, 09:35)</span> bilardi</div></div></div><div id="comment-tools-56621" class="comment-tools"></div><div class="clear"></div><div id="comment-56621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

