+++
type = "question"
title = "RTP out of seq/wrong timestamp"
description = '''I have a co-worker setting up a paging system via SIP/RTP and they are seeing/hearing issues with a delay between the page beep and when the voice is heard. They wiresharked it and saw a small amount of wrong timestamp errors on their RTP stream analysis. e.g. 2 packets (1.9%)out of a 5 second call....'''
date = "2013-10-31T11:10:00Z"
lastmod = "2013-10-31T11:10:00Z"
weight = 26596
keywords = [ "rtp", "wrongtimestamp" ]
aliases = [ "/questions/26596" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP out of seq/wrong timestamp](/questions/26596/rtp-out-of-seqwrong-timestamp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26596-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a co-worker setting up a paging system via SIP/RTP and they are seeing/hearing issues with a delay between the page beep and when the voice is heard. They wiresharked it and saw a small amount of wrong timestamp errors on their RTP stream analysis. e.g. 2 packets (1.9%)out of a 5 second call. They are concerned about this and think the network is at fault. However this is UDP, thus connectionless and makes no guarantees on when or how the packets can get to the end device.<br />
</p><p>I am not sure how to proceed as I am a wireshark noob :) Any help would be appreciated!</p></div><div id="question-tags" class="tags-container tags">rtp wrongtimestamp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '13, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/2b08ea0443006e943bf3d65563e93d4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kyuss&#39;s gravatar image" /><p>Kyuss<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kyuss has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-26596" class="comments-container"><span id="26600"></span><div id="comment-26600" class="comment"><div id="post-26600-score" class="comment-score"></div><div class="comment-text"><p>So I have seen that this could be a bug in wireshark. I am not sure if the bug has been addressed yet. I see this time stamp errors when I run &gt; RTP stream analysis I see no errors, when I click on the player button on the rtp stream analysis window and then decode I get to the RTP player which there it shows that I have the errors.</p><p>So, which window do I believe? Or is it a bug?</p><p>Thanks in advance!!</p></div><div id="comment-26600-info" class="comment-info"><span class="comment-age">(31 Oct '13, 12:00)</span> Kyuss</div></div></div><div id="comment-tools-26596" class="comment-tools"></div><div class="clear"></div><div id="comment-26596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

