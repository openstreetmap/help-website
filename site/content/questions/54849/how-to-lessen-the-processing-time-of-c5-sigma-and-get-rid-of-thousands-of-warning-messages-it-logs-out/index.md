+++
type = "question"
title = "[closed] How to lessen the processing time of C5 Sigma, and get rid of thousands of warning messages it logs out?"
description = '''I have run tshark for a duration of 5 sec, and saved the tshark output to a .pcap file. Then I have run C5 Sigma on this file. It creates the MySQL database successfully but I have a couple of problems: The problem I am facing is thousands of warnings of the form [WARNING] - Unknown field: something...'''
date = "2016-08-16T00:44:00Z"
lastmod = "2016-08-16T00:44:00Z"
weight = 54849
keywords = [ "sniffing", "pcap", "packet-capture", "sigma", "packet" ]
aliases = [ "/questions/54849" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to lessen the processing time of C5 Sigma, and get rid of thousands of warning messages it logs out?](/questions/54849/how-to-lessen-the-processing-time-of-c5-sigma-and-get-rid-of-thousands-of-warning-messages-it-logs-out)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54849-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have run tshark for a duration of 5 sec, and saved the tshark output to a .pcap file. Then I have run C5 Sigma on this file. It creates the MySQL database successfully but I have a couple of problems:</p><p>The problem I am facing is thousands of warnings of the form [WARNING] - Unknown field: something.. and the processing time. <a href="http://pastebin.com/LTpyK5wf">Complete paste of logs here.</a></p><p>For example for a 921KB .pcap file having (1085 packets), it printed 2021065 warnings and took about 8.45 minutes to run.</p><p>More interestingly, when I tried to pass a path to an empty folder (in Windows) to the --inputpath parameter, and it still took 7 minutes to process, and printed 2021065 warnings.</p><p>So I have two questions:</p><p>How can I lessen the processing time of C5 Sigma? What are these fields that C5 Sigma is generating warnings about? Has anyone else faced this problem? Any tips or suggestions or advice is welcome.</p></div><div id="question-tags" class="tags-container tags">sniffing pcap packet-capture sigma packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '16, 00:44</strong></p><img src="https://secure.gravatar.com/avatar/d2c205566b4047d6494161edbd1223c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jesss&#39;s gravatar image" /><p>Jesss<br />
<span class="score" title="51 reputation points">51</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jesss has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 16 Aug '16, 03:11</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54849" class="comments-container"><span id="54851"></span><div id="comment-54851" class="comment"><div id="post-54851-score" class="comment-score">1</div><div class="comment-text"><p>You'll have to go to the <a href="https://www.commandfive.com/downloads/c5sigma.html">folks</a> who make C5 Sigma for support on their product.</p><p>As such, this is off-topic for this site.</p></div><div id="comment-54851-info" class="comment-info"><span class="comment-age">(16 Aug '16, 03:11)</span> grahamb ♦</div></div></div><div id="comment-tools-54849" class="comment-tools"></div><div class="clear"></div><div id="comment-54849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by grahamb 16 Aug '16, 03:11

</div>

</div>

</div>

