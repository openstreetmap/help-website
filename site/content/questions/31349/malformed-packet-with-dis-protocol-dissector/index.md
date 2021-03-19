+++
type = "question"
title = "Malformed Packet with DIS protocol dissector"
description = '''I am trying to dissect a set of DIS messages but am having problems with Action Request message. The data all seems to be available and the number of fixed data fields shows 7 with 0 in number of variable data fields. Then I get a list of the Fixed data fields but only 6 are shown. If I expand the l...'''
date = "2014-04-01T08:39:00Z"
lastmod = "2014-04-01T08:39:00Z"
weight = 31349
keywords = [ "dissector", "dis" ]
aliases = [ "/questions/31349" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed Packet with DIS protocol dissector](/questions/31349/malformed-packet-with-dis-protocol-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31349-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to dissect a set of DIS messages but am having problems with Action Request message. The data all seems to be available and the number of fixed data fields shows 7 with 0 in number of variable data fields. Then I get a list of the Fixed data fields but only 6 are shown. If I expand the last one I can see the Datum Id and the Datum value, both of which are correct. But the remaining 8 bytes are not decoded even though they are visible in the Hex message dump. Again they hold the correct values, so what is going on? Why does the DIS dissector not decode the final Datum?</p></div><div id="question-tags" class="tags-container tags">dissector dis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '14, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/6f03e295bc383344055ae09928b42781?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roger%20Arthur&#39;s gravatar image" /><p>Roger Arthur<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roger Arthur has no accepted answers">0%</span></p></div></div><div id="comments-container-31349" class="comments-container"><span id="31467"></span><div id="comment-31467" class="comment"><div id="post-31467-score" class="comment-score"></div><div class="comment-text"><p>Because this issue was preventing me to progress a task I have tried earlier versions of Wireshark. Original problem reported with Wireshark-win32-1.10.6 I still have the problem in Wireshark-win32-1.8.13 But I do not have this issue with Wireshark-win32-1.6.16 So something has changed in the DIS Dissector between these issues.</p></div><div id="comment-31467-info" class="comment-info"><span class="comment-age">(03 Apr '14, 02:52)</span> Roger Arthur</div></div><span id="31469"></span><div id="comment-31469" class="comment"><div id="post-31469-score" class="comment-score"></div><div class="comment-text"><p>If you can post a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">Cloudshark</a> that would help tremendously.</p></div><div id="comment-31469-info" class="comment-info"><span class="comment-age">(03 Apr '14, 03:05)</span> grahamb ♦</div></div></div><div id="comment-tools-31349" class="comment-tools"></div><div class="clear"></div><div id="comment-31349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

