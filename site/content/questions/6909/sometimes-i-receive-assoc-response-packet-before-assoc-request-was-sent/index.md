+++
type = "question"
title = "Sometimes I receive Assoc response packet before Assoc request was sent"
description = '''Image of the packet trace -&amp;gt; http://postimage.org/image/984jj38/ This is also happens with Auth packets the client -&amp;gt; AP packet has a timestamp which occurs after the AP -&amp;gt; client Auth packet Does anyone know whats going on? is it a bug in the driver?'''
date = "2011-10-16T11:08:00Z"
lastmod = "2011-10-18T09:33:00Z"
weight = 6909
keywords = [ "802.11", "association" ]
aliases = [ "/questions/6909" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Sometimes I receive Assoc response packet before Assoc request was sent](/questions/6909/sometimes-i-receive-assoc-response-packet-before-assoc-request-was-sent)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6909-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Image of the packet trace -&gt; <a href="http://postimage.org/image/984jj38/">http://postimage.org/image/984jj38/</a></p><p>This is also happens with Auth packets the client -&gt; AP packet has a timestamp which occurs after the AP -&gt; client Auth packet</p><p>Does anyone know whats going on? is it a bug in the driver?</p></div><div id="question-tags" class="tags-container tags">802.11 association</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '11, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/5d64d21de6598960bf2db61f1ca705cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddayan&#39;s gravatar image" /><p>ddayan<br />
<span class="score" title="41 reputation points">41</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddayan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '11, 13:21</p></div></div><div id="comments-container-6909" class="comments-container"><span id="6914"></span><div id="comment-6914" class="comment"><div id="post-6914-score" class="comment-score"></div><div class="comment-text"><p>Do the frames contain the same Association ID?<br />
http://www.wildpackets.com/resources/compendium/wireless_lan/wlan_packet_types/printable<br />
http://www.wi-fiplanet.com/tutorials/article.php/1447501</p></div><div id="comment-6914-info" class="comment-info"><span class="comment-age">(16 Oct '11, 23:31)</span> joke</div></div><span id="6915"></span><div id="comment-6915" class="comment"><div id="post-6915-score" class="comment-score">2</div><div class="comment-text"><p>If this happens multiple times, your capture setup might irritate you. Buffered frames waiting to be delivered to your analyzer may change their original order - happens more often when capturing your own, local machine during its own association. In that case, just ignore is.</p><p>I would <em>always</em> recommend capturing wireless traffic with a second "capture only" device.</p><p>@ Joke, Association ID is assigned by the AP - NOT requested by the client. It's just a number for the wireless client to remember in case the AP later on tells e.g. "buffered packets for Assoc ID 2".</p></div><div id="comment-6915-info" class="comment-info"><span class="comment-age">(17 Oct '11, 03:16)</span> Landi</div></div><span id="6929"></span><div id="comment-6929" class="comment"><div id="post-6929-score" class="comment-score"></div><div class="comment-text"><p>@Landi<br />
You are absolutely right. Thank you.<br />
<br />
@ddayan<br />
Sorry for the noise.</p></div><div id="comment-6929-info" class="comment-info"><span class="comment-age">(17 Oct '11, 08:03)</span> joke</div></div><span id="6954"></span><div id="comment-6954" class="comment"><div id="post-6954-score" class="comment-score"></div><div class="comment-text"><p>@Landi</p><p>I think you are right. I did captured on the same machine. Where can i get more info about the way buffered frames are delivered? I would like to know more about why the original order is changed.</p></div><div id="comment-6954-info" class="comment-info"><span class="comment-age">(18 Oct '11, 05:11)</span> ddayan</div></div><span id="6956"></span><div id="comment-6956" class="comment"><div id="post-6956-score" class="comment-score"></div><div class="comment-text"><p>Good question - if you find something give me the link ;) No, honestly - that's stack internals as far as i figured that out plus the way the driver handles stuff... no idea - sorry</p></div><div id="comment-6956-info" class="comment-info"><span class="comment-age">(18 Oct '11, 09:32)</span> Landi</div></div></div><div id="comment-tools-6909" class="comment-tools"></div><div class="clear"></div><div id="comment-6909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6958"></span>

<div id="answer-container-6958" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6958-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>--- from comment to answer ---</p><p>If this happens multiple times, your capture setup might irritate you. Buffered frames waiting to be delivered to your analyzer may change their original order - happens more often when capturing your own, local machine during its own association. In that case, just ignore is.</p><p>I would <em>always</em> recommend capturing wireless traffic with a second "capture only" device.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '11, 09:33</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span> </br></br></p></div></div><div id="comments-container-6958" class="comments-container"></div><div id="comment-tools-6958" class="comment-tools"></div><div class="clear"></div><div id="comment-6958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

