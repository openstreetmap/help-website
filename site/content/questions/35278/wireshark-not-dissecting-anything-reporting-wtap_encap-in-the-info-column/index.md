+++
type = "question"
title = "Wireshark not dissecting anything, reporting WTAP_ENCAP = in the Info column"
description = '''Wireshark Admin, Not sure what happened here … One Day I went to open a PCAP and it looked like this ??? UNKNOWN WTAP_ENCAP ??? Look at PIC attachmrny  I have uninstalled … installed Wireshark numerous times and am not able to get back the proper format of my PCAPs (Below). I have had IT department ...'''
date = "2014-08-06T14:10:00Z"
lastmod = "2014-08-06T14:54:00Z"
weight = 35278
keywords = [ "dissection" ]
aliases = [ "/questions/35278" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not dissecting anything, reporting WTAP\_ENCAP = in the Info column](/questions/35278/wireshark-not-dissecting-anything-reporting-wtap_encap-in-the-info-column)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35278-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_1.jpg" alt="alt text" />Wireshark Admin,</p><p>Not sure what happened here … One Day I went to open a PCAP and it looked like this ??? UNKNOWN WTAP_ENCAP ???</p><p>Look at PIC attachmrny</p><p>I have uninstalled … installed Wireshark numerous times and am not able to get back the proper format of my PCAPs (Below). I have had IT department wipe my PC clean and re-install Wireshark and it still comes back the same way.<br />
</p><p>Can anyone assist me as to why the format has changed to these UNKNOWN / WTAG_ENCAP whenever I open a PCAP on my laptop?<br />
</p><p>Regards,</p><p>MP</p></div><div id="question-tags" class="tags-container tags">dissection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '14, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/ca205aaca5bfe579116eea7506094647?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mperricvc&#39;s gravatar image" /><p>mperricvc<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mperricvc has no accepted answers">0%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 06 Aug '14, 21:57</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-35278" class="comments-container"></div><div id="comment-tools-35278" class="comment-tools"></div><div class="clear"></div><div id="comment-35278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35279"></span>

<div id="answer-container-35279" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35279-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like your dissectors could all be disabled. Press CTRL + Shift + E and check if all have a check mark in the status column. To make sure you could click on "Enable All".</p><p>Or you can try to create a new profile and see if that helps. The pop up menu for that is on the status bar to the right.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Aug '14, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35279" class="comments-container"></div><div id="comment-tools-35279" class="comment-tools"></div><div class="clear"></div><div id="comment-35279-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

