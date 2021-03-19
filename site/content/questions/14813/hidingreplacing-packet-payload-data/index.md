+++
type = "question"
title = "Hiding/Replacing Packet Payload Data"
description = '''We will be performing analysis on a network in an environment governed by strict security laws and client policies. The user data cannot be removed from the facility.  We would like to be able to take our captures back to the office and review them there, rather than analyzing under the watchful gaz...'''
date = "2012-10-09T04:45:00Z"
lastmod = "2012-10-11T04:51:00Z"
weight = 14813
keywords = [ "security", "hide", "payload", "analysis", "wireshark" ]
aliases = [ "/questions/14813" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Hiding/Replacing Packet Payload Data](/questions/14813/hidingreplacing-packet-payload-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14813-score" class="post-score" title="current number of votes">0</div><span id="post-14813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We will be performing analysis on a network in an environment governed by strict security laws and client policies. The user data cannot be removed from the facility.<br />
</p><p>We would like to be able to take our captures back to the office and review them there, rather than analyzing under the watchful gaze of our client. We can obfuscate the address info, but do not know a way to selectively remove (or replace) the packet payloads based on the highest level protocol in the packet, and still leave the protocol info, packet sizes, and other info needed to perform our analysis.</p><p>This capability is also needed to construct our report without exposing secured information.</p><p>Does anyone know of any Wireshark settings or good tools for that purpose? Alternative suggestions?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-security" rel="tag" title="see questions tagged &#39;security&#39;">security</span> <span class="post-tag tag-link-hide" rel="tag" title="see questions tagged &#39;hide&#39;">hide</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '12, 04:45</strong></p><img src="https://secure.gravatar.com/avatar/27f9a3366649276c114a10cbb7a7b277?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bmcmanus&#39;s gravatar image" /><p><span>bmcmanus</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bmcmanus has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-14813" class="comments-container"></div><div id="comment-tools-14813" class="comment-tools"></div><div class="clear"></div><div id="comment-14813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14815"></span>

<div id="answer-container-14815" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14815-score" class="post-score" title="current number of votes">1</div><span id="post-14815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Basically you're in need of trace file anonymization techniques. You might want to take a look at a presentation I did at Sharkfest 2011 about that topic, which you can find on the retrospective page here: <a href="http://sharkfest.wireshark.org/sharkfest.11/index.html">http://sharkfest.wireshark.org/sharkfest.11/index.html</a></p><p>I have to admit that none of the tools I mention in the presentation are to my full liking, mostly because they're targeted at modifying replay data for packet generators (tcprewrite/bittwiste) or very automatic anonymization without much chance of adjusting specific packets (pktanon). Also, they all do not work with pcapng files (last time I checked), which is another problem.</p><p>Right now I am working on a tool that (hopefully) will be making things easier (and processes pcapng), but it is still a long way to go before it is of any use.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '12, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14815" class="comments-container"><span id="14816"></span><div id="comment-14816" class="comment"><div id="post-14816-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the excellent overview of what's out there. I don't see anything that's much better than our old WildPackets PacketScrubber. PktAnon looks quite flexible, and would likely be the tool if it could handle and obfuscate dot1q/ad. MPLS is a growing concern, too.</p><p>Look forward to seeing your new tool for pcapng!</p></div><div id="comment-14816-info" class="comment-info"><span class="comment-age">(09 Oct '12, 06:31)</span> <span class="comment-user userinfo">bmcmanus</span></div></div></div><div id="comment-tools-14815" class="comment-tools"></div><div class="clear"></div><div id="comment-14815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14819"></span>

<div id="answer-container-14819" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14819-score" class="post-score" title="current number of votes">0</div><span id="post-14819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Alternative suggestions?</p></blockquote><p>Unfortunately, the best alternative is to do the analysis on site in such an environment. You can ask the client not to "disturb" the analysis, as you might oversee some important things, if your concentration is distracted by questions and "suggestions" of the customer.</p><p>If you anonymize/scrub/remove the payload data, there are only limited analysis "tests" you can do with that data, often limited to network performance issues (basically !), based on packet flow and timing. If you need to analyze any higher level problem, how would you do that without the real data?</p><p>Any intelligent packet scrubber would have to modify the data in a consistent way for a big bunch of protocols and I doubt that there is any single tool out there that can do this. Imagine just the effort to modify CIFS/SMB in a consistent way (change names of users, shares, credentials, content of files, etc.) or SSL (replace cert, fake private keys, etc.) or even HTTP with all the SESSION IDs, internal URLs, and the content ;-))</p><p>May I ask what kind of problem you are after?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '12, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14819" class="comments-container"><span id="14919"></span><div id="comment-14919" class="comment"><div id="post-14919-score" class="comment-score"></div><div class="comment-text"><p>In this case, we have been asked to investigate the perennial "slow network". Based on what we've been told, sight unseen, we suspect that the problem may be layer 1/2 (bad GBICs and/or STP issues), with perhaps a bit of TCP/SMB (multiple AD versions are present) to sweeten the pot. oh, joy.<br />
</p><p>Of course, we would have to have the full packet contents for the expected AD issues, but any L1/L2 issues will need to be cleared up first. In our experience, once the problems through L3 are resolved, most systems typically run well.</p></div><div id="comment-14919-info" class="comment-info"><span class="comment-age">(11 Oct '12, 04:51)</span> <span class="comment-user userinfo">bmcmanus</span></div></div></div><div id="comment-tools-14819" class="comment-tools"></div><div class="clear"></div><div id="comment-14819-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

