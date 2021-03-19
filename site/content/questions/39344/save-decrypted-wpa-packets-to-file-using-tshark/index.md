+++
type = "question"
title = "Save decrypted WPA packets to file using TShark"
description = '''Hi, I am trying to save the decrypted packets from a WPA2 network for further analysis using other tools that can&#x27;t do the decryption. I am aware of the following answers but they both use wireshark. This is script running on a headless client so I cannot use &quot;Export PDUs&quot; in the wireshark menu. htt...'''
date = "2015-01-21T13:00:00Z"
lastmod = "2015-01-21T15:56:00Z"
weight = 39344
keywords = [ "decrypt", "pcap", "wpa2" ]
aliases = [ "/questions/39344" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Save decrypted WPA packets to file using TShark](/questions/39344/save-decrypted-wpa-packets-to-file-using-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39344-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to save the decrypted packets from a WPA2 network for further analysis using other tools that can't do the decryption. I am aware of the following answers but they both use wireshark. This is script running on a headless client so I cannot use "Export PDUs" in the wireshark menu.</p><p><a href="https://ask.wireshark.org/questions/23606/decrypting-browser-https-wrapped-into-stunnel-ssl">https://ask.wireshark.org/questions/23606/decrypting-browser-https-wrapped-into-stunnel-ssl</a> <a href="https://ask.wireshark.org/questions/30235/save-decrypted-wpa-packets-to-a-new-file">https://ask.wireshark.org/questions/30235/save-decrypted-wpa-packets-to-a-new-file</a></p><p>Any suggestions how to do that?</p><p>Thanks, Joseph</p></div><div id="question-tags" class="tags-container tags">decrypt pcap wpa2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '15, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/b23cfdd98d2abfc4a426226ee7cde147?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joerango&#39;s gravatar image" /><p>joerango<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joerango has no accepted answers">0%</span></p></div></div><div id="comments-container-39344" class="comments-container"></div><div id="comment-tools-39344" class="comment-tools"></div><div class="clear"></div><div id="comment-39344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39345"></span>

<div id="answer-container-39345" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39345-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For now the answer, as far as I know, is you can't (with Wireshark).</p><p>But, there is some progress: see <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3444">bug 3444</a> and <a href="https://code.wireshark.org/review/5890">change 5890</a>; the goal there is to implement "export PDU" in tshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '15, 15:56</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-39345" class="comments-container"></div><div id="comment-tools-39345" class="comment-tools"></div><div class="clear"></div><div id="comment-39345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

