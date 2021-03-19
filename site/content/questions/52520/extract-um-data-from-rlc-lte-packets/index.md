+++
type = "question"
title = "Extract UM Data from RLC-LTE packets"
description = '''I need to extract the UM data from RLC-LTE packets so I can compare this data between two captures to see which one is missing what.... Based on experience so far, I don&#x27;t think Wireshark has the capability of doing this, but is there a way to extract this data, or am I out of luck? Below is a pictu...'''
date = "2016-05-13T09:31:00Z"
lastmod = "2016-05-13T11:19:00Z"
weight = 52520
keywords = [ "extraction", "data", "dataextraction", "rlc-lte" ]
aliases = [ "/questions/52520" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Extract UM Data from RLC-LTE packets](/questions/52520/extract-um-data-from-rlc-lte-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52520-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to extract the UM data from RLC-LTE packets so I can compare this data between two captures to see which one is missing what.... Based on experience so far, I don't think Wireshark has the capability of doing this, but is there a way to extract this data, or am I out of luck?</p><p>Below is a picture of what I am trying to extract. Certain portions of the picure are blacked out for confidenciality reasons. The data of interest is circled in red: <img src="https://www.dropbox.com/s/o8fnmz1skkve31x/Extracting%20UM%20Data%20Question%20V2.png?dl=1" alt="Wireshark PCAP screenshot outlining UM data of interest" /></p><p>Let me know if you have any questions; I will try to answer them as best I can.</p></div><div id="question-tags" class="tags-container tags">extraction data dataextraction rlc-lte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '16, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/3a4bc2ba5c09d24f214dc472eb5b7993?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Midimistro&#39;s gravatar image" /><p>Midimistro<br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Midimistro has one accepted answer">50%</span></p></img></div></div><div id="comments-container-52520" class="comments-container"><span id="52540"></span><div id="comment-52540" class="comment"><div id="post-52540-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure exactly what you want to compare in terms of missing data, but if you turn on UM sequence analysis you will find out about any lost packets at the RLC/UM level. If you configure PDCP to be decoded, you can enable sequence analysis at that level too. And if PDCP is carrying unencrypted IP traffic you can decode that and maybe the protocol it is carrying will highlight missing data. If PDCP is encrypted and you have the key information, you may be able to decrypt it.</p><p>I don't remember what versions of Wireshark first had these features, 1.10 is a fairly old.</p></div><div id="comment-52540-info" class="comment-info"><span class="comment-age">(13 May '16, 13:33)</span> MartinM</div></div></div><div id="comment-tools-52520" class="comment-tools"></div><div class="clear"></div><div id="comment-52520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52527"></span>

<div id="answer-container-52527" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52527-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As usual help via screenshots is difficult, in particular when you've redacted the bit of the status bar that would give you the answer.</p><p>The field name for UM Data is <code>rlc-lte.um.data</code>, as would be seen in the status bar (in parentheses) when you click on a field of interest in the packet details pane.</p><p>This field name can be used in a command line tshark command to print out the field values, e.g. <code>tshark -r &lt;capturefile&gt; -T fields -e rlc-lte.um.data</code>. Add additional <code>-e</code> options for additional fields and then post process the results from your captures to compare the data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '16, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-52527" class="comments-container"><span id="52545"></span><div id="comment-52545" class="comment"><div id="post-52545-score" class="comment-score"></div><div class="comment-text"><p>I'll test that to see if it works next week. Thank you.</p></div><div id="comment-52545-info" class="comment-info"><span class="comment-age">(13 May '16, 14:12)</span> Midimistro</div></div></div><div id="comment-tools-52527" class="comment-tools"></div><div class="clear"></div><div id="comment-52527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

