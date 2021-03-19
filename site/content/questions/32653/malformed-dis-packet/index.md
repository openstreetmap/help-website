+++
type = "question"
title = "Malformed DIS packet?"
description = '''I am seeing a &quot;Malformed Packet (Exception occured)&quot; message with a DIS packet while using Wireshark 1.10.7 (v1.10.7-0-g6b931a1 from master-1.10) on Windows 7. We are generating this packet ourselves and I think it is valid. But I&#x27;m eager to learn if there is something wrong with it. And also I&#x27;m tr...'''
date = "2014-05-08T20:49:00Z"
lastmod = "2014-05-11T22:53:00Z"
weight = 32653
keywords = [ "malformed", "dis" ]
aliases = [ "/questions/32653" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed DIS packet?](/questions/32653/malformed-dis-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32653-score" class="post-score" title="current number of votes">0</div><span id="post-32653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am seeing a "Malformed Packet (Exception occured)" message with a DIS packet while using Wireshark 1.10.7 (v1.10.7-0-g6b931a1 from master-1.10) on Windows 7. We are generating this packet ourselves and I think it is valid. But I'm eager to learn if there is something wrong with it. And also I'm trying to find out if we can trust/use the DIS dissector or not, because it would be helpful to us if it is reliable.</p><p>The K12 text packet is here: <a href="http://pastebin.com/AaB8vQnn">http://pastebin.com/AaB8vQnn</a></p><p>The pcap is here: <a href="https://www.cloudshark.org/captures/4bb6d12660f4">https://www.cloudshark.org/captures/4bb6d12660f4</a></p><p>I grabbed the wireshark source and looked around at the DIS dissector, but did not find it easy to follow. I would like to build the source and debug, but I'm not sure when/if I will be have the time to do that. So I'm just wondering if someone has any idea what is wrong here.</p><p>Thanks for any ideas.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-malformed" rel="tag" title="see questions tagged &#39;malformed&#39;">malformed</span> <span class="post-tag tag-link-dis" rel="tag" title="see questions tagged &#39;dis&#39;">dis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '14, 20:49</strong></p><img src="https://secure.gravatar.com/avatar/fc8f6788ea7222dd275e4b5641ef857b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pwinston&#39;s gravatar image" /><p><span>pwinston</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pwinston has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 May '14, 13:54</strong> </span></p></div></div><div id="comments-container-32653" class="comments-container"><span id="32672"></span><div id="comment-32672" class="comment"><div id="post-32672-score" class="comment-score"></div><div class="comment-text"><p>please post the <strong>pcap</strong> file!</p></div><div id="comment-32672-info" class="comment-info"><span class="comment-age">(09 May '14, 11:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="32689"></span><div id="comment-32689" class="comment"><div id="post-32689-score" class="comment-score"></div><div class="comment-text"><p>Sure, but how? I saw someone else say "post the K12 on pastebin" so that's what I did. Let me know where I will put it up!</p></div><div id="comment-32689-info" class="comment-info"><span class="comment-age">(09 May '14, 13:23)</span> <span class="comment-user userinfo">pwinston</span></div></div><span id="32690"></span><div id="comment-32690" class="comment"><div id="post-32690-score" class="comment-score"></div><div class="comment-text"><p>Google drive, dropbox, cloudshark.org</p></div><div id="comment-32690-info" class="comment-info"><span class="comment-age">(09 May '14, 13:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="32691"></span><div id="comment-32691" class="comment"><div id="post-32691-score" class="comment-score"></div><div class="comment-text"><p>Okay I added cloudshark link to pcap in the question above, thanks for the tip that was simple.</p></div><div id="comment-32691-info" class="comment-info"><span class="comment-age">(09 May '14, 13:54)</span> <span class="comment-user userinfo">pwinston</span></div></div></div><div id="comment-tools-32653" class="comment-tools"></div><div class="clear"></div><div id="comment-32653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32695"></span>

<div id="answer-container-32695" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32695-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32695-score" class="post-score" title="current number of votes">0</div><span id="post-32695-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There seems to be one byte missing at the end (record end marker: DIS_FIELDTYPE_END). I've corrected the pcap file with a HEX editor (added one byte and fixed all length and checksum values).</p><blockquote><p><a href="https://www.cloudshark.org/captures/c02b4867d4a2">https://www.cloudshark.org/captures/c02b4867d4a2</a></p></blockquote><p>Now Wireshark shows the frame without errors. I leave it up to you to check if the dissected values make any sense.</p><p>HINT: I'm not sure if my modification made the frame a valid DIS frame. I did not check the code very thoroughly. I just believed Wireshark when it stopped showing an error, without knowing <strong>exactly</strong> why it stopped!!</p><p>HINT#2: The <strong>PDU Length</strong> might be wrong as well in your frame, however Wireshark does not check the value. Header PDU Lenght value: 48. DATA PDU bytes: 36.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '14, 16:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32695" class="comments-container"><span id="32708"></span><div id="comment-32708" class="comment"><div id="post-32708-score" class="comment-score"></div><div class="comment-text"><p>Wow thanks for figuring that out. How did you know what wireshark thought was wrong, run it in debug? However based on what I know the DIS dissector is wrong here, the code that generated this packet is 10+ years old and in use in 1000's of simulators with no reported issues. Of course that is not proof. I will located the fulls spec and take a look. But I have seen informal descriptions of this packet, and they say there is nothing tacked on to the end.</p><p>Interesting though, and cloudshark is very impressive. I think I will accept this answer soon because it does show why wireshark does not like the packet. Although I think the jury is still out, at least a bit, on whether the original packet I posted is truly malformed, or if wireshark just thinks it is.</p></div><div id="comment-32708-info" class="comment-info"><span class="comment-age">(10 May '14, 20:56)</span> <span class="comment-user userinfo">pwinston</span></div></div><span id="32719"></span><div id="comment-32719" class="comment"><div id="post-32719-score" class="comment-score"></div><div class="comment-text"><p>How I did it? Code review and some guesswork ;-) As I don't have the protocol specs, I don't know who is right, your frame or my modified one.</p></div><div id="comment-32719-info" class="comment-info"><span class="comment-age">(11 May '14, 22:53)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32695" class="comment-tools"></div><div class="clear"></div><div id="comment-32695-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

