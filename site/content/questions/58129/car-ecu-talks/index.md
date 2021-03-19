+++
type = "question"
title = "Car ECU talks"
description = '''firstly hi! i&#x27;m a noob I can directly connect to my car&#x27;s ECU(computer) via ethernet cable so i decided to sniff that data. I don&#x27;t know the name of this connection protocol but my laptop gets an ip starts with 169.254.x.x opened wireshark connected ethernet cable to ECU. Turn on to ignition and the...'''
date = "2016-12-14T20:35:00Z"
lastmod = "2016-12-15T15:35:00Z"
weight = 58129
keywords = [ "ethernet", "ecu", "car" ]
aliases = [ "/questions/58129" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Car ECU talks](/questions/58129/car-ecu-talks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58129-score" class="post-score" title="current number of votes">0</div><span id="post-58129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>firstly hi! i'm a noob</p><p>I can directly connect to my car's ECU(computer) via ethernet cable so i decided to sniff that data.</p><p>I don't know the name of this connection protocol but my laptop gets an ip starts with 169.254.x.x</p><p>opened wireshark connected ethernet cable to ECU. Turn on to ignition and the first package received. Than I run the software of the ECU from my laptop which allows me to change the calibration of the ecu. Downloaded a map and saved it. All the packages are captured by wireshark!</p><p>2749 216.169396 LifeECU_80:00:a7 Inventec_18:a6:dc 0x88af 1048 Ethernet II</p><p>but encrypted i believe.. Is there anyway I can learn the protocol and how the software communicates with ecu..?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-ecu" rel="tag" title="see questions tagged &#39;ecu&#39;">ecu</span> <span class="post-tag tag-link-car" rel="tag" title="see questions tagged &#39;car&#39;">car</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '16, 20:35</strong></p><img src="https://secure.gravatar.com/avatar/e4879d0c19d35f93ce15fcc158160fdf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="secured-nor1&#39;s gravatar image" /><p><span>secured-nor1</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="secured-nor1 has no accepted answers">0%</span></p></div></div><div id="comments-container-58129" class="comments-container"></div><div id="comment-tools-58129" class="comment-tools"></div><div class="clear"></div><div id="comment-58129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58133"></span>

<div id="answer-container-58133" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58133-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58133-score" class="post-score" title="current number of votes">0</div><span id="post-58133-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I see ethertype 0x88af in your packet. Googling for it gives:</p><pre><code>88af

Life Racing Limited
Unit 6 Repton Close
Basildon  Essex  SS13 1LE

Proprietary automotive control unit protocol used by UK OEM Life
Racing Ltd.</code></pre><p>(From: <a href="http://standards-oui.ieee.org/ethertype/eth.txt)">http://standards-oui.ieee.org/ethertype/eth.txt)</a></p><p>As it is a proprietary protocol, you would need to reverse engineer the data. It might or might not be encrypted so you might have luck or not in being able to decipher the messages. In my experience a lot of protocols have some sort of PDU structure with a length and/or sequence number in them, I would start by lookig for those items first.</p><p>It would be nice to look at the protocol data, are you able to share the capture on cloudshark, dropbox, onedrive or another filesharing service (please first make sure there is no sensitive data in it)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '16, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-58133" class="comments-container"><span id="58152"></span><div id="comment-58152" class="comment"><div id="post-58152-score" class="comment-score"></div><div class="comment-text"><p>Thanks! I googled it and came up with nothing.</p><p>There is no sensitive data for me but it may hurt Life Racing may be? I've no commercial attitude and dont want to publicate their commercial secrets.</p><p>The software monitors the all the datas of the car. I just sniffed it if i can make my own software on Android platform. The sniffed data consist of my car's calibration(tuning) map which is not sensitive for me as I'm a tuner.</p><p>I can send the data by email if anyone interested artattech &gt; gmail com</p><p>Btw, the data is encrypted I believe. There are tons of dots =) I can only read the cars map comment section which i manually written. Can wireshark decode it? Its the first time i'm using it.</p></div><div id="comment-58152-info" class="comment-info"><span class="comment-age">(15 Dec '16, 15:30)</span> <span class="comment-user userinfo">secured-nor1</span></div></div><span id="58153"></span><div id="comment-58153" class="comment"><div id="post-58153-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment" as that is how this site works best, please see the FAQ if you want to know why)</p><p>The data does not necessarily be encrypted if you see a lot of dots. It could be just binary data in which all the non-ascii values are displayed as dots. As you are able to read a comment, I guess the data is not encrypted, just binary...</p><p>(I'll email you for the trace file, thanks!)</p></div><div id="comment-58153-info" class="comment-info"><span class="comment-age">(15 Dec '16, 15:35)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-58133" class="comment-tools"></div><div class="clear"></div><div id="comment-58133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

