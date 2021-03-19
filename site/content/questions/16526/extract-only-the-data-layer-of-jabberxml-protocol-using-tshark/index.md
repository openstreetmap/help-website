+++
type = "question"
title = "Extract only the data layer of jabber/xml protocol using tshark"
description = '''Hi fellows, In order to get only the data of each TCP packets ( separated from the headers ) it is sufficient to use the data field.  A command such as tshark -r test.pcap -T fields -e data is enough. Now the tricky part comes when i try to do the same for XMPP packets. Those packet don&#x27;t have a &quot;da...'''
date = "2012-12-04T02:11:00Z"
lastmod = "2012-12-04T02:11:00Z"
weight = 16526
keywords = [ "xmpp", "follow.tcp.stream", "jabber", "tshark" ]
aliases = [ "/questions/16526" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extract only the data layer of jabber/xml protocol using tshark](/questions/16526/extract-only-the-data-layer-of-jabberxml-protocol-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16526-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi fellows,</p><p>In order to get only the data of each TCP packets ( separated from the headers ) it is sufficient to use the data field.</p><p>A command such as <code>tshark -r test.pcap -T fields -e data</code> is enough. Now the tricky part comes when i try to do the same for XMPP packets. Those packet don't have a "data" layer identified in wireshark, but a xml layer.</p><p>Using a command such that `tshark -r test.pcap -T fields -e xml.tag -e xml.unknown' gives me inexact data.</p><p>What I would like to achieve is to remove completely the headers and keep only the "xml" part. The data at the end should be stored raw in a data file, and the content of this file should look like the content of the Follow TCP Stream option in wireshark. Do you have an idea on what field I should use in order to get this result ? Or maybe should i try to crop the headers if they have fix length? Any suggestion of an expert is welcome :D</p><p>Cheers !</p></div><div id="question-tags" class="tags-container tags">xmpp follow.tcp.stream jabber tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '12, 02:11</strong></p><img src="https://secure.gravatar.com/avatar/9bb1da23c32fbda015a6cbc5356ba124?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="faboul&#39;s gravatar image" /><p>faboul<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="faboul has no accepted answers">0%</span></p></div></div><div id="comments-container-16526" class="comments-container"><span id="16589"></span><div id="comment-16589" class="comment"><div id="post-16589-score" class="comment-score"></div><div class="comment-text"><p>Maybe foolish suggestion - have you tried just <code>tshark -r test.pcap -T fields -e xml</code> ?</p></div><div id="comment-16589-info" class="comment-info"><span class="comment-age">(05 Dec '12, 05:15)</span> lojza</div></div><span id="16593"></span><div id="comment-16593" class="comment"><div id="post-16593-score" class="comment-score"></div><div class="comment-text"><p>Hi, First of all thanks for the answer !</p><p>I tried that and it just print "xml" for every packet that contains xml and a blank line for the others. SO , it's not a valid solution :)</p></div><div id="comment-16593-info" class="comment-info"><span class="comment-age">(05 Dec '12, 06:44)</span> faboul</div></div></div><div id="comment-tools-16526" class="comment-tools"></div><div class="clear"></div><div id="comment-16526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

