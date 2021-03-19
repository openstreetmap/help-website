+++
type = "question"
title = "Damaged capture file"
description = '''I was trying to capture the GNS3 serial traffic with Wireshark (ver 1.6.5). But every time the same error message is showing up when i tried to open the cap file. The error message is &quot;The capture file appears to be damaged or corrupt (pcap: File has 67109120-bye packet, bigger than maximum of 65535...'''
date = "2012-07-06T01:48:00Z"
lastmod = "2012-07-06T10:07:00Z"
weight = 12478
keywords = [ "gns3", "capture" ]
aliases = [ "/questions/12478" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Damaged capture file](/questions/12478/damaged-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12478-score" class="post-score" title="current number of votes">0</div><span id="post-12478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was trying to capture the GNS3 serial traffic with Wireshark (ver 1.6.5). But every time the same error message is showing up when i tried to open the cap file. The error message is "The capture file appears to be damaged or corrupt (pcap: File has 67109120-bye packet, bigger than maximum of 65535.). Just wondering how is this possible? cap file is only 10 KB size?</p><p>Thomas, Technical Trainer, <a href="http://www.joera.in"></a><a href="http://www.joera.in">http://www.joera.in</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gns3" rel="tag" title="see questions tagged &#39;gns3&#39;">gns3</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '12, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/bf502b6cfad1f9a6707ecb0fad157f0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joera&#39;s gravatar image" /><p><span>joera</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joera has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>06 Jul '12, 07:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-12478" class="comments-container"></div><div id="comment-tools-12478" class="comment-tools"></div><div class="clear"></div><div id="comment-12478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12484"></span>

<div id="answer-container-12484" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12484-score" class="post-score" title="current number of votes">0</div><span id="post-12484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In pcap files, the packet size is a value written to the packet header each packet has stored just in front of the actual packet bytes. So if the write process writes a funny number into that space you might end up with the error message you see, and it has nothing to do with the actual file size. I'd say your file is indeed corrupt, but I can't say how it happened. What application did you capture the data with? Was it really Wireshark? If so, this is probably an issue you should report in the bug tracker.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '12, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-12484" class="comments-container"><span id="12487"></span><div id="comment-12487" class="comment"><div id="post-12487-score" class="comment-score"></div><div class="comment-text"><p>And:</p><ol><li><p>If the file is being captured with Wireshark, was it the same Wireshark, on the same machine, that's being used to open it?</p></li><li><p>If the file isn't being captured with Wireshark, is it being opened by Wireshark running on the same machine?</p></li><li><p>If the capturing program and the opening program aren't running on the same machine, how is the file being transferred between the machines?</p></li></ol><p>Some forms of file transfer can, if transferring between Windows and UN*X, damage files if they're transferring the file as text.</p></div><div id="comment-12487-info" class="comment-info"><span class="comment-age">(06 Jul '12, 10:07)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-12484" class="comment-tools"></div><div class="clear"></div><div id="comment-12484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

