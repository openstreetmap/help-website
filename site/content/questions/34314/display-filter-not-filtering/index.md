+++
type = "question"
title = "Display filter not filtering"
description = '''hey. i&#x27;m trying to filter some specific result from 100K packets by mac addr. i can see the mac addr under &quot;Source&quot; and i even let wireshark filter for me (apply as filter&amp;gt;selected), and still when i press apply it shows nothing. i.e &quot;eth.src == 00:0c:43:44:a1:a5&quot; (yes, I Tx over eth not wlan) th...'''
date = "2014-07-01T02:58:00Z"
lastmod = "2014-07-01T04:15:00Z"
weight = 34314
keywords = [ "packet-display", "display-filter" ]
aliases = [ "/questions/34314" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Display filter not filtering](/questions/34314/display-filter-not-filtering)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34314-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hey.</p><p>i'm trying to filter some specific result from 100K packets by mac addr. i can see the mac addr under "Source" and i even let wireshark filter for me (apply as filter&gt;selected), and still when i press apply it shows nothing.</p><p>i.e "eth.src == 00:0c:43:44:a1:a5" (yes, I Tx over eth not wlan)</p><p>thx!</p></div><div id="question-tags" class="tags-container tags">packet-display display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '14, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/0989cfd5339ac55d3f56bdb1b46ec8fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AranZaiger&#39;s gravatar image" /><p>AranZaiger<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AranZaiger has no accepted answers">0%</span></p></div></div><div id="comments-container-34314" class="comments-container"></div><div id="comment-tools-34314" class="comment-tools"></div><div class="clear"></div><div id="comment-34314-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34316"></span>

<div id="answer-container-34316" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34316-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you apply the following filter on the sample capture file below, do you see any frames?</p><blockquote><p>eth.src == 00:0a:95:67:49:3c</p></blockquote><p>Sample capture file: <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=http_gzip.cap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=http_gzip.cap</a></p><p><strong>Case #1:</strong><br />
If you see some frames, then something is wrong with your capture file or you chose the wrong mac address, or you are not using ethernet.</p><p>TODO: Please post a sample capture file that should contain the mac address you mentioned. You can post it on google drive, dropbox or cloudshark.org.</p><p><strong>Case #2:</strong><br />
If you don't see any frames with the sample file, then something is wrong with your Wireshark installation.</p><p>TODO: Please post</p><ul><li>OS and OS version</li><li>Wireshark version</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '14, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-34316" class="comments-container"><span id="34324"></span><div id="comment-34324" class="comment"><div id="post-34324-score" class="comment-score"></div><div class="comment-text"><p>problame was half solved. worked when i used wlan.sa == &lt;some mac="" addr=""&gt;</p><p>ty!</p></div><div id="comment-34324-info" class="comment-info"><span class="comment-age">(01 Jul '14, 07:33)</span> AranZaiger</div></div></div><div id="comment-tools-34316" class="comment-tools"></div><div class="clear"></div><div id="comment-34316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

