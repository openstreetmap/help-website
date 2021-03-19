+++
type = "question"
title = "Removing duplicate packets"
description = '''I have found that when mirroring packets on at least some Cisco platforms, in some cases the ehthernet MAC address is that of the sending/receiving device, and in others it&#x27;s the MAC address of the switch -- this is true for the same TCP session and creates duplicates. When this happens, editcap -d ...'''
date = "2011-07-19T15:46:00Z"
lastmod = "2012-08-05T22:55:00Z"
weight = 5135
keywords = [ "duplicates", "remove" ]
aliases = [ "/questions/5135" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Removing duplicate packets](/questions/5135/removing-duplicate-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5135-score" class="post-score" title="current number of votes">0</div><span id="post-5135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have found that when mirroring packets on at least some Cisco platforms, in some cases the ehthernet MAC address is that of the sending/receiving device, and in others it's the MAC address of the switch -- this is true for the same TCP session and creates duplicates. When this happens, editcap -d does not remove the duplicates. Is there a way to cause editcap to ignore the ehthernet portion when de-duplicating? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicates" rel="tag" title="see questions tagged &#39;duplicates&#39;">duplicates</span> <span class="post-tag tag-link-remove" rel="tag" title="see questions tagged &#39;remove&#39;">remove</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '11, 15:46</strong></p><img src="https://secure.gravatar.com/avatar/de310d5db6f9967a52b6b132c7ba7049?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jowimi&#39;s gravatar image" /><p><span>jowimi</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jowimi has no accepted answers">0%</span></p></div></div><div id="comments-container-5135" class="comments-container"></div><div id="comment-tools-5135" class="comment-tools"></div><div class="clear"></div><div id="comment-5135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5136"></span>

<div id="answer-container-5136" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5136-score" class="post-score" title="current number of votes">4</div><span id="post-5136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The MAC address of the switch should not appear in a layer 3 packet since the switch is a layer 2 device - unless you are running a layer 3 switch. And if the MAC address is different it is not a duplicate (and editcap is right in not removing them), unless you want to ignore layer 2.</p><p>Usually you get two frames identical except for layer 2 when using VLANs, so you're seeing the frame in one VLAN and then also in another after it was routed. Have you checked if the frames are in different VLANs? Keep in mind that, depending on your capture card, you might not be able to record the VLAN tag even though it's in the original frame coming in - that way you see the same frame with different MAC addresses without VLAN tag because the card didn't record it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '11, 16:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jul '11, 16:46</strong> </span></p></div></div><div id="comments-container-5136" class="comments-container"><span id="5142"></span><div id="comment-5142" class="comment"><div id="post-5142-score" class="comment-score"></div><div class="comment-text"><p>In most cases, I'm not concerned with the ethernet layer -- I would just like to have a "clean" TCP/IP layer trace to go over with the application folks. I hate having to explain that the duplicates are normal and to be expected.</p></div><div id="comment-5142-info" class="comment-info"><span class="comment-age">(20 Jul '11, 07:48)</span> <span class="comment-user userinfo">jowimi</span></div></div><span id="5143"></span><div id="comment-5143" class="comment"><div id="post-5143-score" class="comment-score">1</div><div class="comment-text"><p>Ok, I see. Did you check if your duplicates are due to seeing a routed frame twice? You can detect this by looking at VLAN tags or the TTL - if the same packet has 2 different TTLs (usually +/-1) it got routed in the meantime. BTW, I forgot to mention another reason for missing VLAN tags: the SPAN port strips them, too, if not told otherwise; use the "encapsulation dot1q" command (if you're using cisco devices to include them, otherwise check your manuals).</p><p>If you can find different VLANs or TTLs in the duplicate and original you can easily filter one group away and save the rest, dupe free.</p></div><div id="comment-5143-info" class="comment-info"><span class="comment-age">(20 Jul '11, 07:53)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="5146"></span><div id="comment-5146" class="comment"><div id="post-5146-score" class="comment-score"></div><div class="comment-text"><p>I editcap -d'd a trace first -- that got rid of the clearly duplicate packets. Then I applied a display filter ip.ttl == nn or ip.ttl == nn to include the TTL for each side of the non-duoplicated packets. Worked great!! Thanks for the advice.</p></div><div id="comment-5146-info" class="comment-info"><span class="comment-age">(20 Jul '11, 09:10)</span> <span class="comment-user userinfo">jowimi</span></div></div><span id="5147"></span><div id="comment-5147" class="comment"><div id="post-5147-score" class="comment-score"></div><div class="comment-text"><p>Good to see it worked itself out :-) You might want to accept the answer to get it out of the ton of "unanswered" questions.</p></div><div id="comment-5147-info" class="comment-info"><span class="comment-age">(20 Jul '11, 09:13)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="13365"></span><div id="comment-13365" class="comment"><div id="post-13365-score" class="comment-score"></div><div class="comment-text"><p>This thread was JUST what I was looking for. I'm seeing "dupes" and, like jowimi, "I hate having to explain that the duplicates are normal and to be expected." And my dupes DO seem to be caused by VLAN routing, as their TTL's are off by one.</p><p>However, my cranial density prevents me from grasping the solution :-). jowimi says "I applied a display filter ip.ttl == nn or ip.ttl == nn", and it got rid of the dupes. In my case, I see TTL's of my dupes as 61 &amp; 62, and then sometimes they are 63 &amp; 64, and i could maybe find other pairs if I kept looking. What do i set "nn" to, and how does it work?</p><p>Thx guys - GREAT stuff!</p><p>feenyman99</p></div><div id="comment-13365-info" class="comment-info"><span class="comment-age">(04 Aug '12, 07:30)</span> <span class="comment-user userinfo">feenyman99</span></div></div><span id="13367"></span><div id="comment-13367" class="comment not_top_scorer"><div id="post-13367-score" class="comment-score"></div><div class="comment-text"><pre><code>You can use display filter:
ip.ttl==61 || ip.ttl=62 || ip.ttl==63 || ip.ttl==63

Or you can use a display filter like:
ip.ttl&gt;60 &amp;&amp; ip.ttl&lt;70</code></pre></div><div id="comment-13367-info" class="comment-info"><span class="comment-age">(04 Aug '12, 23:42)</span> <span class="comment-user userinfo">joke</span></div></div><span id="13376"></span><div id="comment-13376" class="comment not_top_scorer"><div id="post-13376-score" class="comment-score"></div><div class="comment-text"><p>The best way for you to remove the dups is to filter on vlan-id or mac-addresses and then either save the resulting packets to a new file or choose to ignore one side of the conversation with "Edit -&gt; Ignore all displayed packets"</p></div><div id="comment-13376-info" class="comment-info"><span class="comment-age">(05 Aug '12, 22:55)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-5136" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-5136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5150"></span>

<div id="answer-container-5150" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5150-score" class="post-score" title="current number of votes">3</div><span id="post-5150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Jasper's tips work great when you have a tracefile that has traffic of two sides of a router. A good way to prevent these duplicates to turn up in your capture file is to narrow down the configuration of your monitor session.</p><p>In case there are multiple vlans on a switchport it might be better to span the vlan instead of the physical port. Beware to capture only RX packets and not both TX and RX, as each packet that enters the switch on a particular vlan usually leaves the switch on that vlan too (even if it is just to the routing engine). It's always a good idea to run a (few) test captures until you are sure you see all traffic of interest and only traffic of interest :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '11, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5150" class="comments-container"></div><div id="comment-tools-5150" class="comment-tools"></div><div class="clear"></div><div id="comment-5150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

