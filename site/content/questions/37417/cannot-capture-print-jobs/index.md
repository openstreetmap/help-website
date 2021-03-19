+++
type = "question"
title = "cannot capture print jobs"
description = '''Hi, I&#x27;m trying to capture frames from print jobs via a span port on cisco switch, however nothing from print jobs gets captured. The span port mirrors the packets from the port where the printer is connected. I expected frames with destination printer ip and port 9100, but nothing of that kind. When...'''
date = "2014-10-28T13:41:00Z"
lastmod = "2014-10-28T13:41:00Z"
weight = 37417
keywords = [ "print", "capture", "job" ]
aliases = [ "/questions/37417" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [cannot capture print jobs](/questions/37417/cannot-capture-print-jobs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37417-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to capture frames from print jobs via a span port on cisco switch, however nothing from print jobs gets captured. The span port mirrors the packets from the port where the printer is connected. I expected frames with destination printer ip and port 9100, but nothing of that kind. When I ping the printer I do see these packages appear, as well as snmp messages. Am I missing something obvious ?</p><p>Thanks for any help</p></div><div id="question-tags" class="tags-container tags">print capture job</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '14, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/85955d464143637996056ec67e7815a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Koen&#39;s gravatar image" /><p>Koen<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Koen has no accepted answers">0%</span></p></div></div><div id="comments-container-37417" class="comments-container"><span id="37418"></span><div id="comment-37418" class="comment"><div id="post-37418-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Am I missing something obvious ?</p></blockquote><p>maybe there are currently no print jobs?</p><p>BTW: Do you see ping/snmp frames that are sent from the Wireshark PC or from other systems? If other systems, your mirror port configuration should be O.K. If it's just your own ping/snmp frames, your mirror port configuration might be broken.</p></div><div id="comment-37418-info" class="comment-info"><span class="comment-age">(28 Oct '14, 15:44)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-37417" class="comment-tools"></div><div class="clear"></div><div id="comment-37417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

