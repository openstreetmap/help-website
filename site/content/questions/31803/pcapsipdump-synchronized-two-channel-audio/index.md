+++
type = "question"
title = "pcapsipdump synchronized two channel audio"
description = '''i use pcapsipdump to create individual pcap files of specific voip calls. each pcap file is a two channel pcap file with each talker in one of the channels. use RTP stream analysis and the &quot;save payload&quot; button wireshark is able to save the audio in these files to raw or au files in one or both dire...'''
date = "2014-04-14T14:02:00Z"
lastmod = "2014-04-15T02:07:00Z"
weight = 31803
keywords = [ "pcapsipdump", "audio", "two", "synchronized", "channel" ]
aliases = [ "/questions/31803" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [pcapsipdump synchronized two channel audio](/questions/31803/pcapsipdump-synchronized-two-channel-audio)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31803-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31803-score" class="post-score" title="current number of votes">0</div><span id="post-31803-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i use pcapsipdump to create individual pcap files of specific voip calls. each pcap file is a two channel pcap file with each talker in one of the channels. use RTP stream analysis and the "save payload" button wireshark is able to save the audio in these files to raw or au files in one or both directions and with au files is able to mix the audio into a single channel. The issue is that when doing it this way the channels are not in sync with each other and the conversations drifts between the two channels such that after a few minutes of audio the speakers' conversation can be out by 10 or more seconds between the channels.</p><p>However, If i use the VoIP call analyzer and play the file back through the sound card the two channels playback in perfect sync. if this dialog has a "save audio" button then a synchronized one or two channel recording file could be created (either is acceptible) directly.</p><p>As it stands now the audio had to be replayed back into a recording system to produce the synchronized audio, undesirable because this is done in real time, so a 1 hour recording takes 1 hour to replay and synchronize.</p><p>I have looked into at least half a dozen rtp pcap tools to do the same but have yet to find one that can do this correctly (the all produced individual audio files)</p><p>Please let me know if a "save audio" feature could be added to the player option in VoIP Calls. Thanks, Les</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcapsipdump" rel="tag" title="see questions tagged &#39;pcapsipdump&#39;">pcapsipdump</span> <span class="post-tag tag-link-audio" rel="tag" title="see questions tagged &#39;audio&#39;">audio</span> <span class="post-tag tag-link-two" rel="tag" title="see questions tagged &#39;two&#39;">two</span> <span class="post-tag tag-link-synchronized" rel="tag" title="see questions tagged &#39;synchronized&#39;">synchronized</span> <span class="post-tag tag-link-channel" rel="tag" title="see questions tagged &#39;channel&#39;">channel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '14, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/4f0333e937a4fedb373ee9ffa592483a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shekster&#39;s gravatar image" /><p><span>shekster</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shekster has no accepted answers">0%</span></p></div></div><div id="comments-container-31803" class="comments-container"></div><div id="comment-tools-31803" class="comment-tools"></div><div class="clear"></div><div id="comment-31803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31833"></span>

<div id="answer-container-31833" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31833-score" class="post-score" title="current number of votes">0</div><span id="post-31833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Please let me know if a "save audio" feature could be added to the player option in VoIP Calls. Thanks, Les</p></blockquote><p>if you need this feature and you think it's something others might need as well, please file an enhancement request at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and post the link in a comment here.</p><p>BTW: What are the tools you already tested?</p><p>Did you test the ones mentioned in my answer to the following question?</p><blockquote><p><a href="http://ask.wireshark.org/questions/21193/extracting-rtp-payload-and-dumping-to-a-ts-file">http://ask.wireshark.org/questions/21193/extracting-rtp-payload-and-dumping-to-a-ts-file</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '14, 02:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31833" class="comments-container"></div><div id="comment-tools-31833" class="comment-tools"></div><div class="clear"></div><div id="comment-31833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

