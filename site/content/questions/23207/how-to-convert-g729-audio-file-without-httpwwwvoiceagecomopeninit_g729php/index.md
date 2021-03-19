+++
type = "question"
title = "How to convert g729 audio file without http://www.voiceage.com/openinit_g729.php"
description = '''How to convert g729 audio file without http://www.voiceage.com/openinit_g729.php'''
date = "2013-07-21T06:29:00Z"
lastmod = "2013-11-13T11:44:00Z"
weight = 23207
keywords = [ "g729" ]
aliases = [ "/questions/23207" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to convert g729 audio file without http://www.voiceage.com/openinit\_g729.php](/questions/23207/how-to-convert-g729-audio-file-without-httpwwwvoiceagecomopeninit_g729php)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23207-score" class="post-score" title="current number of votes">0</div><span id="post-23207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to convert g729 audio file without <a href="http://www.voiceage.com/openinit_g729.php">http://www.voiceage.com/openinit_g729.php</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-g729" rel="tag" title="see questions tagged &#39;g729&#39;">g729</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jul '13, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/8112981c1dbe1884fcebacf3d613d93e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="support&#39;s gravatar image" /><p><span>support</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="support has no accepted answers">0%</span></p></div></div><div id="comments-container-23207" class="comments-container"><span id="23256"></span><div id="comment-23256" class="comment"><div id="post-23256-score" class="comment-score">1</div><div class="comment-text"><p>Is this a Wireshark question?</p><p>If so, please add some information what you captured and why/how you need to convert that data from g729 to what exactly?</p></div><div id="comment-23256-info" class="comment-info"><span class="comment-age">(22 Jul '13, 14:46)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="23272"></span><div id="comment-23272" class="comment"><div id="post-23272-score" class="comment-score"></div><div class="comment-text"><p>how to play audio/voice in g729 codec capture file by using wireshark , without the software voiceage???? cause voiceage software is not available to download and probably it needs license.Is there any other software without voiceage which we can use alternately on voiceage? i tried a lots of time to download the voiceage by using the link <a href="http://www.voiceage.com/openinit_g729.php">http://www.voiceage.com/openinit_g729.php</a> but it redirects me to the page <a href="http://www.voiceage.com/PRODUCTS.html">http://www.voiceage.com/PRODUCTS.html</a> . so is there any alternate way to listen the voice from wireshark in g729 ? or can anyone help me out to download the software voiceage????</p><p>regards</p><p>shajib/<span class="__cf_email__" data-cfemail="8ee5e6fdeff4e7eccee9e3efe7e2a0ede1e3">[email protected]</span></p></div><div id="comment-23272-info" class="comment-info"><span class="comment-age">(22 Jul '13, 16:57)</span> <span class="comment-user userinfo">support</span></div></div></div><div id="comment-tools-23207" class="comment-tools"></div><div class="clear"></div><div id="comment-23207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23298"></span>

<div id="answer-container-23298" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23298-score" class="post-score" title="current number of votes">1</div><span id="post-23298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>how to play audio/voice in g729 codec capture file by using wireshark</p></blockquote><p>There is no way, as Wireshark does not support that codec. However, you can try to save the recorded audio stream and then try to convert it with <a href="http://sox.sourceforge.net/">sox</a> or <a href="http://www.germanixsoft.de/">GermaniX Transcoder</a>.</p><p>Anyway, the conversion part is a question you better ask in a VoIP forum.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '13, 10:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23298" class="comments-container"></div><div id="comment-tools-23298" class="comment-tools"></div><div class="clear"></div><div id="comment-23298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26957"></span>

<div id="answer-container-26957" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26957-score" class="post-score" title="current number of votes">0</div><span id="post-26957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use the CodecPro software here: <a href="http://codecpro.com/openInitG729.html">http://codecpro.com/openInitG729.html</a></p><p>The procedure in the wiki was also modify to point to that decoder. (<a href="http://wiki.wireshark.org/HowToDecodeG729)">http://wiki.wireshark.org/HowToDecodeG729)</a></p><p>Regards, Richard</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '13, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/2d223d8402ec9a96e942b69ebd8464b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RichardPOirier&#39;s gravatar image" /><p><span>RichardPOirier</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RichardPOirier has no accepted answers">0%</span></p></div></div><div id="comments-container-26957" class="comments-container"></div><div id="comment-tools-26957" class="comment-tools"></div><div class="clear"></div><div id="comment-26957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

