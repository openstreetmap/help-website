+++
type = "question"
title = "how else can I fix this error?"
description = '''I have wireshark shows error &quot;The capabilities of The capture device &quot;mon0&quot; could not be obtained (That device doesn&#x27;t support monitor mode). Please check to make sure you have sufficient permissions, and that you have the proper interface or pipe specified. Try using airmon-ng, as suggested by Capt...'''
date = "2013-11-12T21:18:00Z"
lastmod = "2013-11-14T06:17:00Z"
weight = 26925
keywords = [ "airmon" ]
aliases = [ "/questions/26925" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how else can I fix this error?](/questions/26925/how-else-can-i-fix-this-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26925-score" class="post-score" title="current number of votes">0</div><span id="post-26925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have wireshark shows error</p><p>"The capabilities of The capture device "mon0" could not be obtained (That device doesn't support monitor mode). Please check to make sure you have sufficient permissions, and that you have the proper interface or pipe specified.</p><p>Try using airmon-ng, as suggested by CaptureSetup/WLAN in the Wireshark Wiki."</p><p>I did airmon-ng start wlan0, the error appears again, I killed all the processes, only "NetworkManager, wpa_supplicant, dhclient." but if you kill them falls to the Internet, which could be causing this error?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-airmon" rel="tag" title="see questions tagged &#39;airmon&#39;">airmon</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '13, 21:18</strong></p><img src="https://secure.gravatar.com/avatar/348b58b10734f511c32ddaa3f6c15488?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sokolov%20%20Andrey&#39;s gravatar image" /><p><span>Sokolov Andrey</span><br />
<span class="score" title="1 reputation points">1</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sokolov  Andrey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Nov '13, 21:27</strong> </span></p></div></div><div id="comments-container-26925" class="comments-container"><span id="26993"></span><div id="comment-26993" class="comment"><div id="post-26993-score" class="comment-score"></div><div class="comment-text"><p>sounds like your kernel driver for your wifi/wlan interface does not support monitor mode. Please post:</p><ul><li>OS and version</li><li>wifi/wlan brand and model</li></ul><p>Regards<br />
Kurt</p></div><div id="comment-26993-info" class="comment-info"><span class="comment-age">(14 Nov '13, 05:04)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="26995"></span><div id="comment-26995" class="comment"><div id="post-26995-score" class="comment-score"></div><div class="comment-text"><p>OC-ubuntu Wi-Fi adapter- ALFA AWUS036H and standart modele Aspire E1-531G 802.11 b/g/n</p></div><div id="comment-26995-info" class="comment-info"><span class="comment-age">(14 Nov '13, 05:17)</span> <span class="comment-user userinfo">Sokolov Andrey</span></div></div></div><div id="comment-tools-26925" class="comment-tools"></div><div class="clear"></div><div id="comment-26925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27000"></span>

<div id="answer-container-27000" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27000-score" class="post-score" title="current number of votes">0</div><span id="post-27000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>ALFA AWUS036H</p></blockquote><p>strange, the AWUS036H should support monitor mode. Which version of Ubuntu did you try?</p><p>Suggestion: Please try <a href="http://www.kali.org/">Kali Linux</a> instead of Ubuntu.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '13, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-27000" class="comments-container"><span id="27002"></span><div id="comment-27002" class="comment"><div id="post-27002-score" class="comment-score"></div><div class="comment-text"><p>ubuntu 12.04</p></div><div id="comment-27002-info" class="comment-info"><span class="comment-age">(14 Nov '13, 06:01)</span> <span class="comment-user userinfo">Sokolov Andrey</span></div></div><span id="27003"></span><div id="comment-27003" class="comment"><div id="post-27003-score" class="comment-score"></div><div class="comment-text"><p>apparently others have similar problems.</p><blockquote><p><a href="http://www.backtrack-linux.org/forums/showthread.php?t=53559">http://www.backtrack-linux.org/forums/showthread.php?t=53559</a></p></blockquote><p>please try Kali Linux (not sure if that works)</p></div><div id="comment-27003-info" class="comment-info"><span class="comment-age">(14 Nov '13, 06:17)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-27000" class="comment-tools"></div><div class="clear"></div><div id="comment-27000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

