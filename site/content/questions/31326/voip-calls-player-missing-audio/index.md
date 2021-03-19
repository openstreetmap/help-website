+++
type = "question"
title = "voip calls player missing audio"
description = '''I am unable to hear audio after capturing a sip phone call. I am able to see the call in the player but no audio is available when playing. Any suggestions'''
date = "2014-03-31T12:54:00Z"
lastmod = "2014-04-02T13:37:00Z"
weight = 31326
keywords = [ "voipcalls" ]
aliases = [ "/questions/31326" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [voip calls player missing audio](/questions/31326/voip-calls-player-missing-audio)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31326-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am unable to hear audio after capturing a sip phone call. I am able to see the call in the player but no audio is available when playing. Any suggestions</p></div><div id="question-tags" class="tags-container tags">voipcalls</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Mar '14, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/1de1487406e24f768efe103fb9cd3ec0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bou401&#39;s gravatar image" /><p>bou401<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bou401 has no accepted answers">0%</span></p></div></div><div id="comments-container-31326" class="comments-container"><span id="50936"></span><div id="comment-50936" class="comment"><div id="post-50936-score" class="comment-score"></div><div class="comment-text"><p>Same problem here, with wireshark 2.0.2 version new version from the site, i'am trouble shooting And have a tracé in the "old" version i have voipcalls And i can listen to them In the new version same tracé i have voipcalls but if i try to listen is see "no audio" And in the Callflow i also dont see the RTP pakket</p><p>-A</p></div><div id="comment-50936-info" class="comment-info"><span class="comment-age">(15 Mar '16, 11:15)</span> the cube</div></div><span id="50940"></span><div id="comment-50940" class="comment"><div id="post-50940-score" class="comment-score">1</div><div class="comment-text"><p>I'm not sure whether it is a good idea to piggyback your question to the older one although the symptoms are similar, but can you publish the trace? If there is a difference in behaviour between "old" and "new" wireshark <strong>on the very same file</strong>, it is likely a bug (or incompleteness of the development) which may not have been reported yet.</p></div><div id="comment-50940-info" class="comment-info"><span class="comment-age">(15 Mar '16, 11:37)</span> sindy</div></div><span id="50942"></span><div id="comment-50942" class="comment"><div id="post-50942-score" class="comment-score"></div><div class="comment-text"><p>Made a new topic tnx</p></div><div id="comment-50942-info" class="comment-info"><span class="comment-age">(15 Mar '16, 11:43)</span> the cube</div></div></div><div id="comment-tools-31326" class="comment-tools"></div><div class="clear"></div><div id="comment-31326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31432"></span>

<div id="answer-container-31432" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31432-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Any suggestions</p></blockquote><p>switch on the speakers of your PC? Just kidding. ;-))</p><p>What is</p><ul><li>your OS and OS version</li><li>your Wireshark version</li><li>Are you able to hear something in the following file?</li></ul><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=MagicJack%2B_short_call.pcap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=MagicJack%2B_short_call.pcap</a></p></blockquote><p>You should hear "Testing 1, 2, 3" at the end.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31432" class="comments-container"></div><div id="comment-tools-31432" class="comment-tools"></div><div class="clear"></div><div id="comment-31432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

