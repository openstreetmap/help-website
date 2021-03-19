+++
type = "question"
title = "rpcap support in Wireshark 1.8"
description = '''In Wireshark 1.6.8 in the capture options I was able to replace the selection of a local interface into: rpcap://[ip-address]/[interface] In version 1.8 this isn&#x27;t possible anymore. Please could you explain how I need to make a pcap of a remote machine in version 1.8. Best regards, Theo '''
date = "2012-07-09T06:26:00Z"
lastmod = "2012-07-09T06:51:00Z"
weight = 12526
keywords = [ "rpcap", "1.8" ]
aliases = [ "/questions/12526" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [rpcap support in Wireshark 1.8](/questions/12526/rpcap-support-in-wireshark-18)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12526-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In Wireshark 1.6.8 in the capture options I was able to replace the selection of a local interface into: rpcap://[ip-address]/[interface]</p><p>In version 1.8 this isn't possible anymore. Please could you explain how I need to make a pcap of a remote machine in version 1.8.</p><p>Best regards, Theo</p></div><div id="question-tags" class="tags-container tags">rpcap 1.8</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '12, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/77e2d1d8e4e22333998f355c03f93352?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Theo&#39;s gravatar image" /><p>Theo<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Theo has no accepted answers">0%</span></p></div></div><div id="comments-container-12526" class="comments-container"></div><div id="comment-tools-12526" class="comment-tools"></div><div class="clear"></div><div id="comment-12526-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12528"></span>

<div id="answer-container-12528" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12528-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Start Wireshark</li><li>Open Capture Options</li><li>Select Button "Manage Interfaces"</li><li>Select Tab called "Remote Interfaces"</li><li>Click "Add"</li><li>Enter details</li><li>Close Dialog</li><li>Select the new remote interface as capture device by checkmarking it</li><li>Start the capture</li></ol><p>Done.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '12, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jul '12, 06:52</p></div></div><div id="comments-container-12528" class="comments-container"><span id="15159"></span><div id="comment-15159" class="comment"><div id="post-15159-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>This isn't working. In 1.6.8 I also use an rpcap link. But when I try this with 1.8.3 I must search the interface via the host IP and that isn't working. I guess the rcap server doesn't support this. I hope there will be a future to just add the rpcap link.</p><p>Regards</p><p>Peter</p></div><div id="comment-15159-info" class="comment-info"><span class="comment-age">(22 Oct '12, 07:35)</span> p_vanpoucke</div></div><span id="16347"></span><div id="comment-16347" class="comment"><div id="post-16347-score" class="comment-score"></div><div class="comment-text"><p>When I follow the steps you posted everything works except step 9. When I select the remote interface the start button is grayed out. (Wireshark 1.8.3 on Win7-64)</p></div><div id="comment-16347-info" class="comment-info"><span class="comment-age">(27 Nov '12, 01:00)</span> Wire-Rob</div></div></div><div id="comment-tools-12528" class="comment-tools"></div><div class="clear"></div><div id="comment-12528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

