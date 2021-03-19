+++
type = "question"
title = "TCP ACKed lost segment"
description = '''Hi Guys, I&#x27;m quite new to wireshark but i am using it to try and diagnose an issue with have with slow connectivity to our web site. I am see a lot of the following lines in the capture and wondered if anyone could help explain what they are: [TCP ACKed lost segment] 55312 &amp;gt; http [ACK] Seq=183316...'''
date = "2011-02-19T03:53:00Z"
lastmod = "2013-08-13T10:54:00Z"
weight = 2425
keywords = [ "segment", "lost" ]
aliases = [ "/questions/2425" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [TCP ACKed lost segment](/questions/2425/tcp-acked-lost-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2425-score" class="post-score" title="current number of votes">1</div><span id="post-2425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>I'm quite new to wireshark but i am using it to try and diagnose an issue with have with slow connectivity to our web site. I am see a lot of the following lines in the capture and wondered if anyone could help explain what they are:</p><pre><code>[TCP ACKed lost segment] 55312 &gt; http [ACK] Seq=1833164 Ack=9463120 Win=131072 Len=0
[TCP ACKed lost segment] 55253 &gt; http [ACK] Seq=13802249 Ack=65723974 Win=512 Len=0
[TCP Segment of a reassembled PDU]
HTTP/1.1 100 Continue
[TCP Segment of a reassembled PDU]</code></pre><p>Any ideas? I'm a little concerned about the lost segments should i be?</p><p>Regards</p><p>Andi</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-segment" rel="tag" title="see questions tagged &#39;segment&#39;">segment</span> <span class="post-tag tag-link-lost" rel="tag" title="see questions tagged &#39;lost&#39;">lost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '11, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/346f2e817bc85953d4832e8aa72bc73f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spike420&#39;s gravatar image" /><p><span>Spike420</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spike420 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 May '11, 03:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-2425" class="comments-container"></div><div id="comment-tools-2425" class="comment-tools"></div><div class="clear"></div><div id="comment-2425-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="2426"></span>

<div id="answer-container-2426" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2426-score" class="post-score" title="current number of votes">2</div><span id="post-2426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The TCP ACKed lost segment means that Wireshark missed at least one packet in the other direction. The receiving IP stack would not have ack'd unless it received it. So I'd check my placement of Wireshark and make sure that it is in the path for both directions. If so, is it on the one of the endpoints? The reason I ask is that sometimes TCP Chimney has to be disabled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '11, 04:27</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-2426" class="comments-container"></div><div id="comment-tools-2426" class="comment-tools"></div><div class="clear"></div><div id="comment-2426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2427"></span>

<div id="answer-container-2427" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2427-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2427-score" class="post-score" title="current number of votes">1</div><span id="post-2427-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You often see "ACKed lost segment" when your capture dropped packets due to performance reasons, meaning that is was there and was received by the target (resulting in the ACK), but Wireshark didn't capture it. It happens a lot on very active links, in my experiency usually with throughput above 300Mbit/s. Other reasons can be an asymmetric routing table which has a different path for the ACKed packet than the ACK packed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '11, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2427" class="comments-container"></div><div id="comment-tools-2427" class="comment-tools"></div><div class="clear"></div><div id="comment-2427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3912"></span>

<div id="answer-container-3912" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3912-score" class="post-score" title="current number of votes">0</div><span id="post-3912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, sorry to jump in on this thread, but I have a client with a Server 2008 machine that is having these lost segments show up in great quantity in our captures, they're also having difficulty with their main database program which is what prompted the captures in the first place.</p><p>Hope you can help, we've replaced NICS, Cables, switches and Router, and still the issue persists.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '11, 05:29</strong></p><img src="https://secure.gravatar.com/avatar/9ecc7272c3e72ff36f53fea310ee6208?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stsanford&#39;s gravatar image" /><p><span>stsanford</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stsanford has no accepted answers">0%</span></p></div></div><div id="comments-container-3912" class="comments-container"><span id="3913"></span><div id="comment-3913" class="comment"><div id="post-3913-score" class="comment-score"></div><div class="comment-text"><p>Do you see retransmissions for the lost segments? If not, you're probably experiencing drops like I pointed out before. Can you point out what the "difficulties" with the database are?</p></div><div id="comment-3913-info" class="comment-info"><span class="comment-age">(04 May '11, 05:45)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="3915"></span><div id="comment-3915" class="comment"><div id="post-3915-score" class="comment-score"></div><div class="comment-text"><p>Will have to connect in again and re-examine the captures, but the database question I can answer. They're using a flat-file database that I think was built on delphi, so the database is .DAT and .IDX files. They are getting errors reported from the software that file already in use, file not found, resource record not found. It looks on first blush that it would be a problem with file permissions, but it's everyone has full control to the database at this point.</p><p>Support for the software only has the recommendation to reload the server (currently Server 2008 R2) as a Server 2003 server, as their testing doesn't yet certify the 2008 product line. I'd really like to avoid that pain if at all possible as you can imagine... Thanks for your speedy response Jasper, really appreciate the help.</p></div><div id="comment-3915-info" class="comment-info"><span class="comment-age">(04 May '11, 06:21)</span> <span class="comment-user userinfo">stsanford</span></div></div><span id="3921"></span><div id="comment-3921" class="comment"><div id="post-3921-score" class="comment-score"></div><div class="comment-text"><p>I guess you're experiencing SMB file locking trouble then, you should look for "LOCK NOT GRANTED" messages and similar SMB based errors. Tell the programmers to use a TCP port based database instead of a flat file DB, those usually suck in multi user environments ;-)</p></div><div id="comment-3921-info" class="comment-info"><span class="comment-age">(04 May '11, 07:26)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-3912" class="comment-tools"></div><div class="clear"></div><div id="comment-3912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23750"></span>

<div id="answer-container-23750" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23750-score" class="post-score" title="current number of votes">0</div><span id="post-23750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"They are getting errors reported from the software that file already in use, file not found, resource record not found." I have had clients use real-time online backups that caused exactly what you are describing as database issues. Things like "Carbonite", "Mozy" and "Symform". The issue seems to be that the backup has the file locked (even though they claim it will not) creating the file in use error. If you are still having the issue I would look there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '13, 10:54</strong></p><img src="https://secure.gravatar.com/avatar/796f99a255fd224342d5c614ab46aa0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GAltiero&#39;s gravatar image" /><p><span>GAltiero</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GAltiero has no accepted answers">0%</span></p></div></div><div id="comments-container-23750" class="comments-container"></div><div id="comment-tools-23750" class="comment-tools"></div><div class="clear"></div><div id="comment-23750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

